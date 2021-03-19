+++
type = "question"
title = "Memory corruption with Wireshark 2.0 GTK2 on CentOS 6.5 when using a patched TTE dissector"
description = '''I encountered a very weird issue, and need expertise on Wireshark internals. First, a few context informations :  we use a home compiled version of Wireshark 2.0 where we disable a lot of features such as Qt and GTK3 interface or Lua. Main point is being able to run a recent version of Wireshark (be...'''
date = "2016-11-04T10:04:00Z"
lastmod = "2016-11-04T10:29:00Z"
weight = 56988
keywords = [ "gtk", "dissector", "crash", "sub-dissector", "patch" ]
aliases = [ "/questions/56988" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Memory corruption with Wireshark 2.0 GTK2 on CentOS 6.5 when using a patched TTE dissector](/questions/56988/memory-corruption-with-wireshark-20-gtk2-on-centos-65-when-using-a-patched-tte-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I encountered a very weird issue, and need expertise on Wireshark internals. First, a few context informations :</p><ul><li>we use a home compiled version of Wireshark 2.0 where we disable a lot of features such as Qt and GTK3 interface or Lua. Main point is being able to run a recent version of Wireshark (because we developed a plugin infrastructure on top of Wireshark 2 API) on an old distribution based on CentOS 6.5, as well as a more recent one, based on CentOS 7. This "home" version is properly compiled on systems with the right distribution (ie the version we run on CentOS 6.5 is compiled on CentOS 6.5, same with CentOS 7)</li><li>this "home version" features a patch of the TTE protocol dissector, since we need to use dissectors on top of it, and bundled version doesn't support this feature. So we added a dissector table allowing to add dissectors based on "tte.ctid" field</li></ul><p>The problem we observe is a crash when we use a dissector based on this tte.ctid field, but only in CentOS 6.5 context. On CentOS 7, no problem. To exactly pinpoint the problem we used Valgrind, and we don't observe the valgrind error on the CentOS 7 version.</p><p>So I guess we did something wrong with the patch, since going through subdissectors overwrites freed memory originally belonging to GDK. My guess is that the problem might be that <code>call_dissector_with_data</code> is called (original TTE dissector code), and then we call <code>dissector_try_uint</code> to call the subdissectors. Is that the way to do it?</p><p>Now for the data that will help detect the problem. First, our patch of the TTE dissector :</p><pre><code>--- wireshark-2.0.3/epan/dissectors/packet-tte.c    2016-07-19 18:53:17.721839071 +0200
+++ wireshark-2.0.3-patch/epan/dissectors/packet-tte.c  2016-07-20 10:43:25.441521228 +0200
@@ -57,6 +57,8 @@
 static gint ett_tte = -1;
 static gint ett_tte_macdest = -1;

+/* ASL Patch for sub-dissectors */
+static dissector_table_t tte_dissector_table;

 /* Code to actually dissect the packets */
 static int
@@ -68,6 +70,9 @@
     /* Set up structures needed to add the protocol subtree and manage it */
     proto_item *tte_root_item, *tte_macdest_item;
     proto_tree *tte_tree, *tte_macdest_tree;
+    /* ASL Patch for sub-dissectors */
+    guint16 ctid = -1;
+    int ret;

     /* Check that there&#39;s enough data */
     if (tvb_reported_length(tvb) &lt; TTE_HEADER_LENGTH)
@@ -96,6 +100,8 @@
         col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;Bogus TTEthernet Frame&quot;);
     }

+    
+
     if (tree) {

         /* create display subtree for the protocol */
@@ -120,9 +126,9 @@
         proto_tree_add_item(tte_macdest_tree,
             hf_tte_dst_cf, tvb, 0, TTE_MACDEST_CF_LENGTH, ENC_BIG_ENDIAN);

-        proto_tree_add_item(tte_macdest_tree,
+        proto_tree_add_item_ret_uint(tte_macdest_tree,
             hf_tte_ctid, tvb, TTE_MACDEST_CF_LENGTH,
-            TTE_MACDEST_CTID_LENGTH, ENC_BIG_ENDIAN);
+            TTE_MACDEST_CTID_LENGTH, ENC_BIG_ENDIAN, (guint32*)&amp;ctid);
     }

     /* prevent clearing the Columns...appending cannot be prevented */
@@ -137,7 +143,19 @@
     ethertype_data.fcs_len = 0;

     call_dissector_with_data(ethertype_handle, tvb, pinfo, tree, &amp;ethertype_data);
-    return tvb_reported_length(tvb);
+
+    /* ASL Patch for sub-dissectors */
+    /*    return tvb_reported_length(tvb);*/
+    ret = TTE_HEADER_LENGTH;
+    if (ctid &gt; 0) {
+        int bytes = dissector_try_uint(tte_dissector_table, ctid, tvb, pinfo, tree);
+
+        if (bytes &gt; ret) {
+            ret = bytes;
+        }
+    }
+
+    return ret;
 }

@@ -172,6 +185,9 @@
     proto_register_field_array(proto_tte, hf, array_length(hf));
     proto_register_subtree_array(ett, array_length(ett));

+    /* ASL Patch for sub-dissectors */
+    tte_dissector_table = register_dissector_table(&quot;tte.ctid&quot;, &quot;CT ID&quot;, FT_UINT16, BASE_DEC);
+
     /* Register preferences module */
     tte_module = prefs_register_protocol(proto_tte, NULL);</code></pre><p>The valgrind crash trace (only occurring on CentOS 6.5) :</p><pre><code>==11024== Invalid write of size 8
==11024==    at 0x65FCA88: dissector_try_heuristic (packet.c:2194)
==11024==    by 0x68BE54A: dissect_eth_common (packet-eth.c:337)
==11024==    by 0x68BF0B8: dissect_eth (packet-eth.c:841)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FE0A5: dissector_try_uint_new (packet.c:1163)
==11024==    by 0x68F03B4: dissect_frame (packet-frame.c:499)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FD400: call_dissector_with_data (packet.c:2563)
==11024==    by 0x65FF495: dissect_record (packet.c:498)
==11024==    by 0x65F20C9: epan_dissect_run (epan.c:332)
==11024==  Address 0x18240000 is 64 bytes inside a block of size 192 free&#39;d
==11024==    at 0x4A063F0: free (vg_replace_malloc.c:446)
==11024==    by 0x3598A10D22: ??? (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598A1580A: ??? (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598A1589A: ??? (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598A0FB0F: cairo_restore (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3597E26F3F: ??? (in /usr/lib64/libgdk-x11-2.0.so.0.2000.1)
==11024==    by 0x3597E2C88F: ??? (in /usr/lib64/libgdk-x11-2.0.so.0.2000.1)
==11024==    by 0x3597E2CF63: ??? (in /usr/lib64/libgdk-x11-2.0.so.0.2000.1)
==11024==    by 0x3597A2887C: pango_renderer_draw_glyphs (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==    by 0x3597A29064: pango_renderer_draw_layout_line (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==    by 0x3597A29364: pango_renderer_draw_layout (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==    by 0x3597E2BB66: gdk_draw_layout_with_colors (in /usr/lib64/libgdk-x11-2.0.so.0.2000.1)
==11024==
==11024== Invalid write of size 8
==11024==    at 0x65FCA90: dissector_try_heuristic (packet.c:2195)
==11024==    by 0x68BE54A: dissect_eth_common (packet-eth.c:337)
==11024==    by 0x68BF0B8: dissect_eth (packet-eth.c:841)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FE0A5: dissector_try_uint_new (packet.c:1163)
==11024==    by 0x68F03B4: dissect_frame (packet-frame.c:499)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FD400: call_dissector_with_data (packet.c:2563)
==11024==    by 0x65FF495: dissect_record (packet.c:498)
==11024==    by 0x65F20C9: epan_dissect_run (epan.c:332)
==11024==  Address 0x18240158 is not stack&#39;d, malloc&#39;d or (recently) free&#39;d
==11024==
==11024== Invalid write of size 2
==11024==    at 0x65FCA9C: dissector_try_heuristic (packet.c:2196)
==11024==    by 0x68BE54A: dissect_eth_common (packet-eth.c:337)
==11024==    by 0x68BF0B8: dissect_eth (packet-eth.c:841)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FE0A5: dissector_try_uint_new (packet.c:1163)
==11024==    by 0x68F03B4: dissect_frame (packet-frame.c:499)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FD400: call_dissector_with_data (packet.c:2563)
==11024==    by 0x65FF495: dissect_record (packet.c:498)
==11024==    by 0x65F20C9: epan_dissect_run (epan.c:332)
==11024==  Address 0x182400c0 is 0 bytes inside a block of size 16 free&#39;d
==11024==    at 0x4A063F0: free (vg_replace_malloc.c:446)
==11024==    by 0x3598A4393A: ??? (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598A2AA5D: ??? (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598A13982: ??? (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598A0E146: cairo_show_glyphs (in /usr/lib64/libcairo.so.2.10800.8)
==11024==    by 0x3598E086D5: ??? (in /usr/lib64/libpangocairo-1.0.so.0.2800.1)
==11024==    by 0x3598E0899A: ??? (in /usr/lib64/libpangocairo-1.0.so.0.2800.1)
==11024==    by 0x3597A2887C: pango_renderer_draw_glyphs (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==    by 0x3598E074DB: ??? (in /usr/lib64/libpangocairo-1.0.so.0.2800.1)
==11024==    by 0x3597A2887C: pango_renderer_draw_glyphs (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==    by 0x3597A29064: pango_renderer_draw_layout_line (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==    by 0x3597A29364: pango_renderer_draw_layout (in /usr/lib64/libpango-1.0.so.0.2800.1)
==11024==
==11024==
==11024== Process terminating with default action of signal 11 (SIGSEGV): dumping core
==11024==  Access not within mapped region at address 0x7FEFF0000
==11024==    at 0x65FCA88: dissector_try_heuristic (packet.c:2194)
==11024==    by 0x68BE54A: dissect_eth_common (packet-eth.c:337)
==11024==    by 0x68BF0B8: dissect_eth (packet-eth.c:841)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FE0A5: dissector_try_uint_new (packet.c:1163)
==11024==    by 0x68F03B4: dissect_frame (packet-frame.c:499)
==11024==    by 0x65FCB6E: call_dissector_through_handle (packet.c:618)
==11024==    by 0x65FD073: call_dissector_work (packet.c:706)
==11024==    by 0x65FD400: call_dissector_with_data (packet.c:2563)
==11024==    by 0x65FF495: dissect_record (packet.c:498)
==11024==    by 0x65F20C9: epan_dissect_run (epan.c:332)
==11024==  If you believe this happened as a result of a stack
==11024==  overflow in your program&#39;s main thread (unlikely but
==11024==  possible), you can try to increase the size of the
==11024==  main thread stack using the --main-stacksize= flag.
==11024==  The main thread stack size used in this run was 8388608.</code></pre><p>About box information of our CentOS 6.5 Wireshark version :</p><pre><code>Version 2.0.7 (Git Rev Unknown from unknown)

Copyright 1998-2016 Gerald Combs &lt;[email protected]&gt; and contributors.
License GPLv2+: GNU GPL version 2 or later &lt;http://www.gnu.org/licenses/old-licenses/gpl-2.0.html&gt;
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GTK+ 2.20.1, with Cairo 1.8.8, with Pango 1.28.1, with
libpcap, without POSIX capabilities, without libnl, with libz 1.2.3, with GLib
2.26.1, without SMI, without c-ares, without ADNS, without Lua, without GnuTLS,
with Gcrypt 1.4.5, with MIT Kerberos, without GeoIP, without PortAudio, without
AirPcap.

Running on Linux 3.10.47-rt50-RedHawk-6.5.2-trace, with locale en_US.UTF-8, with
libpcap version 1.7.4, with libz 1.2.3, with Gcrypt 1.4.5.
       Intel(R) Xeon(R) CPU E5-2407 0 @ 2.20GHz (with SSE4.2)

Built using gcc 4.4.7 20120313 (Red Hat 4.4.7-4).</code></pre><p>About box of our CentOS 7 version, where the problem does not occur :</p><pre><code>Version 2.0.7 (Git Rev Unknown from unknown)

Copyright 1998-2016 Gerald Combs &lt;[email protected]&gt; and contributors.
License GPLv2+: GNU GPL version 2 or later &lt;http://www.gnu.org/licenses/old-licenses/gpl-2.0.html&gt;
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GTK+ 2.24.22, with Cairo 1.12.14, with Pango 1.34.1, with
libpcap, without POSIX capabilities, without libnl, with libz 1.2.7, with GLib
2.36.3, without SMI, without c-ares, without ADNS, without Lua, without GnuTLS,
without Gcrypt, with MIT Kerberos, without GeoIP, without PortAudio, without
AirPcap.

Running on Linux 3.16.7-RedHawk-7.0.2-trace, with locale en_US.UTF-8, with
libpcap version 1.7.4, with libz 1.2.7.
Intel(R) Xeon(R) CPU E5-2637 v3 @ 3.50GHz (with SSE4.2)

Built using gcc 4.8.2 20140120 (Red Hat 4.8.2-16).</code></pre><p>Thanks in advance for any help you can provide, because I'm a bit lost here :)</p></div><div id="question-tags" class="tags-container tags">gtk dissector crash sub-dissector patch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '16, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/1b1240dfe83b6bd6af805b6c96b3b1b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Florian%20Haradji&#39;s gravatar image" /><p>Florian Haradji<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Florian Haradji has no accepted answers">0%</span></p></div></div><div id="comments-container-56988" class="comments-container"></div><div id="comment-tools-56988" class="comment-tools"></div><div class="clear"></div><div id="comment-56988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56989"></span>

<div id="answer-container-56989" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56989-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all ctid should be a guint32, not a guint16 (you cannot make assumption on the alignment rules done by the compiler/processor and cast a pointer on guint 16 variable as guint32).</p><p>Calling dissector_try_uint after call_dissector_with_data is not an issue by its own, it just means that you give the same payload to 2 different dissectors (so the same data might be dissected twice with different protocols, which is weird).</p><p>There are changces your issue is in the dissectors registered to the newly created tte.ctid table. But as you did not share the code, it's up to you to find what's wrong ;)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '16, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-56989" class="comments-container"><span id="56990"></span><div id="comment-56990" class="comment"><div id="post-56990-score" class="comment-score"></div><div class="comment-text"><p>Well ctid fits on two bytes in the message, but yes, I'll try to use a guint32 instead, and see how it goes.</p><p>Yes I need the same data twice, which is weird...I have reasons for that but it will be too long and uninteresting to explain them here :)</p><p>I don't think the problem is in the dissectors on top of it, since their exact same code is used on top of the more classic "udp.port" dissector table, and no problem then.</p><p>Also, the fact that the problem appears only in CentOS 6.5 where GTK2 and associated libs are in a different version than in CentOS 7, and the valgrind trace explicitly showing gdk/cairo code is quite weird, don't you think?</p></div><div id="comment-56990-info" class="comment-info"><span class="comment-age">(04 Nov '16, 10:37)</span> Florian Haradji</div></div><span id="57009"></span><div id="comment-57009" class="comment"><div id="post-57009-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Well ctid fits on two bytes in the message,</p></blockquote><p>That's completely irrelevant. <code>proto_tree_add_item_ret_uint()</code> is passed a pointer to a <code>guint32</code>, and assumes that the pointer does, in fact, point to a <code>guint32</code>, and thus stores into <em>four</em> bytes starting at the location in the pointer. If you cast a pointer to a <code>guint16</code> to <code>guint32 *</code>, and pass that to <code>proto_tree_add_item_ret_uint()</code>, <code>proto_tree_add_item_ret_uint()</code> will store into that variable <strong><em>and the two bytes after that variable</em></strong>.</p><p>(We didn't complicate the API by having multiple <code>proto_tree_add_item_ret_</code> routines for different data types, taking return-value arguments of different sizes, so the return value will be bigger than the field for types narrower than <code>FT_UINT32</code>.)</p><p>So <strong><em>don't do that</em></strong>. It will cause two random bytes to be overwritten, and where those two bytes happen to be could depend on...</p><blockquote><p>Also, the fact that the problem appears only in CentOS 6.5 where GTK2 and associated libs are in a different version than in CentOS 7</p></blockquote><p>...the version of the compiler used to compile the program, so the behavior could differ between a Wireshark compiled with gcc 4.4.7 20120313 (Red Hat 4.4.7-4) and one compiled with gcc 4.8.2 20140120 (Red Hat 4.8.2-16). That difference could even include one version crashing and another version not crashing.</p><p>Valgrind will also complain about the store into the two bytes after the variable; that's what the "Invalid write of size 2" error probably is (unfortunately, Valgrind apparently doesn't handle the way the stack is handled by the call to the dissector, so it's probably not including the dissector itself in the stack trace).</p><blockquote><p>and the valgrind trace explicitly showing gdk/cairo code</p></blockquote><p>It's explicitly showing that <em>one</em> of the invalid writes is to memory that was <em>freed</em> (and presumably allocated) by gdk/cairo code. That's an 8-byte write, so it's probably a completely separate problem from the 2-byte invalid write. It's not immediately obvious what's causing <em>that</em> problem.</p></div><div id="comment-57009-info" class="comment-info"><span class="comment-age">(04 Nov '16, 18:00)</span> Guy Harris ♦♦</div></div><span id="57048"></span><div id="comment-57048" class="comment"><div id="post-57048-score" class="comment-score"></div><div class="comment-text"><p>And...that was it! It was a pretty obvious mistake, but I guess the valgrind stack trace was a little misleading. Plus the fact it didn't crash in another compiler/OS environment...I did not look in the right place.</p><p>So thank you all :)</p></div><div id="comment-57048-info" class="comment-info"><span class="comment-age">(07 Nov '16, 03:47)</span> Florian Haradji</div></div></div><div id="comment-tools-56989" class="comment-tools"></div><div class="clear"></div><div id="comment-56989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

