+++
type = "question"
title = "Wireshark with customized Radius dissector crashing on RHEL 6.1 64 bit OS"
description = '''Hi, We are using Wireshark 1.0.1, customized RADIUS dissector to suit our requirements. We developed this on RHEL4.7, few years back for one of our clients.  Currently we are moving on to RHEL 6.1 64 bit OS with the same source code and when we try to run our wireshark, it opens up good and when we ...'''
date = "2013-08-08T00:39:00Z"
lastmod = "2013-09-12T04:06:00Z"
weight = 23628
keywords = [ "rhel6", "crash", "radius" ]
aliases = [ "/questions/23628" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with customized Radius dissector crashing on RHEL 6.1 64 bit OS](/questions/23628/wireshark-with-customized-radius-dissector-crashing-on-rhel-61-64-bit-os)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23628-score" class="post-score" title="current number of votes">0</div><span id="post-23628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are using Wireshark 1.0.1, customized RADIUS dissector to suit our requirements. We developed this on RHEL4.7, few years back for one of our clients.</p><p>Currently we are moving on to RHEL 6.1 64 bit OS with the same source code and when we try to run our wireshark, it opens up good and when we try to load a capture file, it crashes.</p><p>As per our requirements, we cant directly move on to latest version of Wireshark before solving this issue with v1.0.1.</p><ul><li>The same source code runs perfectly on Windows XP and RHEL 4.7 32 bit without any issues.<br />
</li><li>The source code compiles good on RHEL 6.1 64 bit OS.</li><li>The problem is there only when we try to run compiled wireshark on RHEL 6.1 64 bit OS.<ul><li>The Wireshark GUI opens good, But when I load a RADIUS capture file (the dissector for which is enhanced) wireshark crashes.</li><li>Capture file containing other protocols (example SNMP, TCP) loads good.</li></ul></li></ul><p>When I try to debug using gdb, these are the logs that i see,</p><pre><code>*Program received signal SIGSEGV, Segmentation fault.
except_pop () at except.c:258
258     set_top(top-&gt;except_down);
Missing separate debuginfos, use: debuginfo-install GConf2-2.28.0-6.el6.x86_64 ORBit2-2.14.17-3.1.el6.x86_64 PackageKit-gtk-module-0.5.8-19.el6.x86_64 atk-1.28.0-2.el6.x86_64*</code></pre><p>and the list of Missing separate debuginfos goes on.</p><hr /><p>When i back traced the stack, here is what i see,</p><pre><code>(gdb) bt
0  except_pop () at except.c:258
1  0x00007ffff6165e41 in dissect_packet (edt=0x16c7430,  pseudo_header=&lt;value optimized out&gt;, pd=0x167c700 &quot;&quot;, fd=0x1538ba0, cinfo=0x16c7440) at packet.c:349
2 0x0000000000430f02 in add_packet_to_packet_list (fdata=0x1538ba0, cf=0x7932c0, dfcode=&lt;value optimized out&gt;, pseudo_header=0x8b1928, buf= 0x167c700 &quot;&quot;, refilter=&lt;value&gt; optimized out&gt;) at file.c:1004
3 0x00000000004329c8 in cf_read (cf=0x7932c0) at file.c:532
4 0x000000000044973a in menu_open_recent_file_cmd (w=0x1539cd0) at menu.c:1709
5 0x00000036d240bb3e in g_closure_invoke () from /lib64/libgobject-2.0.so.0
6 0x00000036d2420e23 in ?? () from /lib64/libgobject-2.0.so.0
7 0x00000036d24220af in g_signal_emit_valist () from /lib64/libgobject-2.0.so.0
8 0x00000036d24225f3 in g_signal_emit () from /lib64/libgobject-2.0.so.0
9 0x00000036d8a7dcce in gtk_widget_activate () from /usr/lib64/libgtk-x11-2.0.so.0
10 0x00000036d8964bdd in gtk_menu_shell_activate_item () from /usr/lib64/libgtk-x11-2.0.so.0
11 0x00000036d896688a in ?? () from /usr/lib64/libgtk-x11-2.0.so.0
12 0x00000036d8953ef3 in ?? () from /usr/lib64/libgtk-x11-2.0.so.0
13 0x00000036d240bb3e in g_closure_invoke () from /lib64/libgobject-2.0.so.0
14 0x00000036d24209ed in ?? () from /lib64/libgobject-2.0.so.0
15 0x00000036d2421f4a in g_signal_emit_valist () from /lib64/libgobject-2.0.so.0
16 0x00000036d24225f3 in g_signal_emit () from /lib64/libgobject-2.0.so.0
17 0x00000036d8a76b2f in ?? () from /usr/lib64/libgtk-x11-2.0.so.0
18 0x00000036d894ac6a in gtk_propagate_event () from /usr/lib64/libgtk-x11-2.0.so.0
19 0x00000036d894bddc in gtk_main_do_event () from /usr/lib64/libgtk-x11-2.0.so.0
20 0x00000036d7c5fffc in ?? () from /usr/lib64/libgdk-x11-2.0.so.0
21 0x00000036d1838f0e in g_main_context_dispatch () from /lib64/libglib-2.0.so.0
22 0x00000036d183c938 in ?? () from /lib64/libglib-2.0.so.0
23 0x00000036d183cd55 in g_main_loop_run () from /lib64/libglib-2.0.so.0
24 0x00000036d894c2c7 in gtk_main () from /usr/lib64/libgtk-x11-2.0.so.0
25 0x00000000004470ca in main (argc=0, argv=0x7fffffffe2f0) at main.c:3197</code></pre><p>Linux Server Details:</p><hr /><pre><code>[[email protected] ~]# uname -a Linux
rmonpa64 2.6.32-131.0.15.el6.x86_64 #1 SMP Tue May 10 15:42:40 EDT 2011 x86_64 x86_64 x86_64 GNU/Linux
[[email protected] ~]#</code></pre><p>Wireshark Details:</p><hr /><pre><code>[[email protected] ~]# wireshark --version
wireshark 1.0.1

Copyright 1998-2008 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled with GTK+ 2.18.9, with GLib 2.22.5, with libpcap 1.0.0, with libz
1.2.3, without POSIX capabilities, without libpcre, without SMI, without ADNS,
without Lua, with GnuTLS 2.8.5, with Gcrypt 1.4.5, with MIT Kerberos, without
PortAudio, without AirPcap.
NOTE: this build doesn&#39;t support the &quot;matches&quot; operator for Wireshark filter
syntax.

Running on Linux 2.6.32-131.0.15.el6.x86_64, with libpcap version 1.0.0.

Built using gcc 4.4.5 20110214 (Red Hat 4.4.5-6).
[[email protected] ~]#</code></pre><p>Any information in this regard would be greatly helpful to us.</p><p>ldd <code>which wireshark</code> command output <a href="http://pastebin.com/iHPcPUEM">http://pastebin.com/iHPcPUEM</a></p><p>strace output: <a href="http://pastebin.com/jDbwwkf9">http://pastebin.com/jDbwwkf9</a></p><p>Thanks, Purandhar K</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rhel6" rel="tag" title="see questions tagged &#39;rhel6&#39;">rhel6</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '13, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/a811fcbfa3be32d52c491c061274a8e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Purandhar%20K&#39;s gravatar image" /><p><span>Purandhar K</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Purandhar K has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '13, 15:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23628" class="comments-container"><span id="23640"></span><div id="comment-23640" class="comment"><div id="post-23640-score" class="comment-score"></div><div class="comment-text"><p>Does vanilla 1.01 work? It's probably a waist of time trying to get the old director to work when you probably can get away with just adding a custom dictionary on the latest version possibly With vsa subdissectors.</p></div><div id="comment-23640-info" class="comment-info"><span class="comment-age">(08 Aug '13, 06:06)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="23667"></span><div id="comment-23667" class="comment"><div id="post-23667-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>Thanks for the information. I will have to get this v1.0.1 working for RHEL6 64 bit, which i am pretty close now, before moving on to latest wireshark-1.10.1. Please see my comments to Jeff.</p><p>-Purandhar</p></div><div id="comment-23667-info" class="comment-info"><span class="comment-age">(08 Aug '13, 23:01)</span> <span class="comment-user userinfo">Purandhar K</span></div></div></div><div id="comment-tools-23628" class="comment-tools"></div><div class="clear"></div><div id="comment-23628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23639"></span>

<div id="answer-container-23639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23639-score" class="post-score" title="current number of votes">1</div><span id="post-23639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks similar to the crash reported in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7978">bug 7978</a>. That was fixed in <a href="https://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=46066">r46066</a> by taking out a 'return' from within a TRY/CATCH/ENTRY block. Is it possible your modifications have introduced such a return?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-23639" class="comments-container"><span id="23666"></span><div id="comment-23666" class="comment"><div id="post-23666-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff,</p><p>Thanks for your reply.</p><p>Tried debug the issue using eclipse and also with gdb, didnt give me any useful information on the crash. (may be i am missing something in them). I tried with Valgrid and it took me through to the issue directly.</p><p>The issues were,</p><ol><li><p>I am trying to use 'pinfo' in my dissector and that crashes saying that I am trying to use an undeclared variable. Strange, pinfo is declared in wireshark's packet.c file and used in few other places in dissector.</p></li><li><p>in except.c, the except_pop() was throwing segmentation fault. Changing the following 'set_top(top-&gt;except_down);' to 'set_top(top);' worked. I havent changed anything in except.c.</p></li></ol><p>Now that wireshark with my customized Radius dissector can load the capture files, i will dig in to see the actual reason for crash. I will keep your comments in mind while doing it.</p><p>thanks again!</p><p>-Purandhar</p></div><div id="comment-23666-info" class="comment-info"><span class="comment-age">(08 Aug '13, 22:55)</span> <span class="comment-user userinfo">Purandhar K</span></div></div><span id="23668"></span><div id="comment-23668" class="comment"><div id="post-23668-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am trying to use 'pinfo' in my dissector and that crashes saying that I am trying to use an undeclared variable.</p></blockquote><p>In C and C++, an "undeclared variable" is a compile-time error, not a crash (a crash is a run-time error); is your dissector written in C (or C++), or in Lua?</p></div><div id="comment-23668-info" class="comment-info"><span class="comment-age">(08 Aug '13, 23:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="23670"></span><div id="comment-23670" class="comment"><div id="post-23670-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>I have customized the default Radius dissector in C, extended it to dissect custom AVPs in Radius packets.</p><p>My bad (tired eyes), its 'Conditional jump or move depends on uninitialised value(s)' and not undeclared.</p><p>-Purandhar</p></div><div id="comment-23670-info" class="comment-info"><span class="comment-age">(09 Aug '13, 01:55)</span> <span class="comment-user userinfo">Purandhar K</span></div></div><span id="23677"></span><div id="comment-23677" class="comment"><div id="post-23677-score" class="comment-score"></div><div class="comment-text"><blockquote><p>in except.c, the except_pop() was throwing segmentation fault. Changing the following 'set_top(top-&gt;except_down);' to 'set_top(top);' worked. I havent changed anything in except.c.</p></blockquote><p>That change does not look correct to me. You may have band-aided the problem to avoid the crash but it's likely the functionality will not be correct with such a change.</p><p>But anyway if you can "fix" the crash like and thus be allowed to upgrade to an at least half-modern version, hopefully the crash will just be fixed in the newer version.</p></div><div id="comment-23677-info" class="comment-info"><span class="comment-age">(09 Aug '13, 07:11)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="23678"></span><div id="comment-23678" class="comment"><div id="post-23678-score" class="comment-score"></div><div class="comment-text"><p>Thats the plan, quick fix the issues and move on to the latest wireshark version, 1.10.1 as soon as possible :) .</p><p>However, i will keep looking for the root cause for the crash and will update here when i find it.</p></div><div id="comment-23678-info" class="comment-info"><span class="comment-age">(09 Aug '13, 07:24)</span> <span class="comment-user userinfo">Purandhar K</span></div></div><span id="24099"></span><div id="comment-24099" class="comment not_top_scorer"><div id="post-24099-score" class="comment-score"></div><div class="comment-text"><p>Hi, I have been looking for the root cause for the issue mentioned in this ticket. The problem within the custom Radius dissector is resolved. I had to write up few lines of code as work around for 'Conditional jump or move depends on uninitialized value(s)'.</p><p>Wireshark still crashes when i load a Radius capture file. I dont have any returns from TRY CATCH Blocks.</p><p>Backtrace of the recent crash:</p><pre><code>==27733== Invalid read of size 8
==27733==    at 0x59ADA37: except_pop (except.c:258)
==27733==    by 0x5B7CD61: dissect_frame (packet-frame.c:346)
==27733==    by 0x59B3D9F: call_dissector_through_handle (packet.c:396)
==27733==    by 0x59B44E5: call_dissector_work (packet.c:485)
==27733==    by 0x59B4630: call_dissector (packet.c:1787)
==27733==    by 0x59B5F51: dissect_packet (packet.c:332)
==27733==    by 0x430F01: add_packet_to_packet_list (file.c:1004)
==27733==    by 0x4329C7: cf_read (file.c:532)
==27733==    by 0x449739: menu_open_recent_file_cmd (menu.c:1709)
==27733==    by 0x36D240BB3D: g_closure_invoke (in /lib64/libgobject-2.0.so.0.2200.5)
==27733==    by 0x36D2420E22: ??? (in /lib64/libgobject-2.0.so.0.2200.5)
==27733==    by 0x36D24220AE: g_signal_emit_valist (in /lib64/libgobject-2.0.so.0.2200.5)
==27733==  Address 0x3604 is not stack&#39;d, malloc&#39;d or (recently) free&#39;d

==27733== Process terminating with default action of signal 11 (SIGSEGV)
==27733==  Access not within mapped region at address 0x3604
==27733==    at 0x59ADA37: except_pop (except.c:258)
==27733==    by 0x5B7CD61: dissect_frame (packet-frame.c:346)
==27733==    by 0x59B3D9F: call_dissector_through_handle (packet.c:396)
==27733==    by 0x59B44E5: call_dissector_work (packet.c:485)
==27733==    by 0x59B4630: call_dissector (packet.c:1787)
==27733==    by 0x59B5F51: dissect_packet (packet.c:332)
==27733==    by 0x430F01: add_packet_to_packet_list (file.c:1004)
by 0x4329C7: cf_read (file.c:532)
 by 0x449739: menu_open_recent_file_cmd (menu.c:1709)
by 0x36D240BB3D: g_closure_invoke (in /lib64/libgobject-2.0.so.0.2200.5)
 by 0x36D2420E22: ??? (in /lib64/libgobject-2.0.so.0.2200.5)
   by 0x36D24220AE: g_signal_emit_valist (in /lib64/libgobject-2.0.so.0.2200.5)</code></pre><p>Your guidance would be of great help to me. I am still using wireshark-1.0.1 version, and can only move on to 1.10.1 after seeing the packets loaded on 1.0.1 :(</p><p>Thanks!</p></div><div id="comment-24099-info" class="comment-info"><span class="comment-age">(27 Aug '13, 07:57)</span> <span class="comment-user userinfo">Purandhar K</span></div></div></div><div id="comment-tools-23639" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-23639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24604"></span>

<div id="answer-container-24604" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24604-score" class="post-score" title="current number of votes">0</div><span id="post-24604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Issue has been resolved. problem was with one of the strcpy function, trying to copy a bigger string in to smaller one. Strange thing is same code runs well without crashing on RHEL4.7 32 bit.</p><p>Anyway, thanks for your time and guidance.</p><p>-Purandhar</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '13, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/a811fcbfa3be32d52c491c061274a8e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Purandhar%20K&#39;s gravatar image" /><p><span>Purandhar K</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Purandhar K has no accepted answers">0%</span></p></div></div><div id="comments-container-24604" class="comments-container"></div><div id="comment-tools-24604" class="comment-tools"></div><div class="clear"></div><div id="comment-24604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

