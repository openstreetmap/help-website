+++
type = "question"
title = "Static linking of libpcap while compilation of tshark"
description = '''Hi, I am compiling tshark (1.6.4) without wireshark. I am using following configure option: ./configure --with-ssl=/usr --with-krb5 --disable-wireshark --disable-gtk2 --disable-editcap --disable-idl2wrs --disable-ipv6 --enable-setuid-install --libdir=/usr/lib64 On my build server libpcap-devel 1.3.0...'''
date = "2013-04-16T23:24:00Z"
lastmod = "2013-04-18T09:27:00Z"
weight = 20499
keywords = [ "compilation", "static", "tshark" ]
aliases = [ "/questions/20499" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Static linking of libpcap while compilation of tshark](/questions/20499/static-linking-of-libpcap-while-compilation-of-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am compiling tshark (1.6.4) without wireshark. I am using following configure option:</p><p>./configure --with-ssl=/usr --with-krb5 --disable-wireshark --disable-gtk2 --disable-editcap --disable-idl2wrs --disable-ipv6 --enable-setuid-install --libdir=/usr/lib64</p><p>On my build server libpcap-devel 1.3.0 is installed. But on production system (on which tshark rpm will be installed) have libpcap 0.9.4 version installed. When I instal tshark rpm (created on build server) on production system, it gives error message that libpcap.so.1(64 bit) not found.</p><p>I can not upgrade libpcap version on production system.</p><p>Can I do static linking of libpcap with tshark binary while compilation of tshark so that I don't need libpcap on production system.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">compilation static tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/a273217076451fb71206e452cf39243e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="friends&#39;s gravatar image" /><p>friends<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="friends has no accepted answers">0%</span></p></div></div><div id="comments-container-20499" class="comments-container"><span id="20528"></span><div id="comment-20528" class="comment"><div id="post-20528-score" class="comment-score"></div><div class="comment-text"><p>What version of what OS are your build server and your production system running? From "tshark rpm", I assume the production system is running some Linux distribution that uses RPMs.</p><p>What do <code>ls -l /usr/lib64/libpcap.so* /usr/lib/libpcap.so*</code> print on the build server and on the production machine?</p></div><div id="comment-20528-info" class="comment-info"><span class="comment-age">(17 Apr '13, 10:34)</span> Guy Harris ♦♦</div></div><span id="20567"></span><div id="comment-20567" class="comment"><div id="post-20567-score" class="comment-score"></div><div class="comment-text"><p>Output of ls commands:</p><pre><code>lrwxrwxrwx 1 root root     16 Apr 18 13:59 /usr/lib64/libpcap.so -&gt; libpcap.so.0.9.4
lrwxrwxrwx 1 root root     16 Jul  6  2011 /usr/lib64/libpcap.so.0 -&gt; libpcap.so.0.9.4
lrwxrwxrwx 1 root root     16 Jul  6  2011 /usr/lib64/libpcap.so.0.9 -&gt; libpcap.so.0.9.4
-rwxr-xr-x 1 root root 171848 Nov 11  2009 /usr/lib64/libpcap.so.0.9.4</code></pre><p>My production system and build server are using RHEL 5.7. On both the server libpcap 0.9.4 is installed. But when I compile tshark using libpcap-devel 0.9.4 and install the rpm, then it gives memory corruption error.</p><pre><code>TShark 1.6.14 (SVN Rev Unknown from unknown)

Copyright 1998-2013 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.12.3, with libpcap (version unknown), with libz
1.2.3, with POSIX capabilities (Linux), without libpcre, without SMI, without
c-ares, without ADNS, without Lua, without Python, without GnuTLS, with Gcrypt
1.4.4, with MIT Kerberos, without GeoIP.
NOTE: this build doesn&#39;t support the &quot;matches&quot; operator for Wireshark filter
syntax.

Running on Linux 2.6.18-274.18.1.el5, with libpcap version 0.9.4, with libz 1.2.3.

Error:
*** glibc detected *** tshark: double free or corruption (fasttop): 0x000000000c135a40 ***
======= Backtrace: =========
/lib64/libc.so.6[0x3707a7247f]
/lib64/libc.so.6(cfree+0x4b)[0x3707a728db]
/usr/lib64/libwiretap.so.1(wtap_close+0x39)[0x2b869b7e2439]
/usr/lib64/libwiretap.so.1(wtap_open_offline+0x28b)[0x2b869b7c68ab]
tshark(cf_open+0x55)[0x424385]
tshark(main+0x1a91)[0x427cf1]
/lib64/libc.so.6(__libc_start_main+0xf4)[0x3707a1d9b4]
tshark(register_all_protocol_handoffs+0xc31)[0x40d4b9]</code></pre></div><div id="comment-20567-info" class="comment-info"><span class="comment-age">(18 Apr '13, 04:42)</span> friends</div></div><span id="20582"></span><div id="comment-20582" class="comment"><div id="post-20582-score" class="comment-score"></div><div class="comment-text"><blockquote><p>My production system and build server are using RHEL 5.7. On both the server libpcap 0.9.4 is installed.</p></blockquote><p>But you said earlier that</p><blockquote><p>On my build server libpcap-devel 1.3.0 is installed.</p></blockquote><p>So do you mean that, on the build server, you have libpcap 0.9.4 and libpcap-devel 1.3.0 installed? That sounds inconsistent - shouldn't the same version of libpcap and libpcap-devel be installed?</p></div><div id="comment-20582-info" class="comment-info"><span class="comment-age">(18 Apr '13, 09:22)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-20499" class="comment-tools"></div><div class="clear"></div><div id="comment-20499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="20519"></span>

<div id="answer-container-20519" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20519-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could remove the dynamic libpcap.so files on your compile server, forcing the linker to use the static one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-20519" class="comments-container"><span id="20527"></span><div id="comment-20527" class="comment"><div id="post-20527-score" class="comment-score"></div><div class="comment-text"><p>I'd be more inclined to temporarily rename them, and then move them back, in case somebody wants to run, on that machine, a program dynamically linked with libpcap. Renaming and then renaming them back still leaves a window in which those programs won't work, but it's only open while Wireshark is being built.</p></div><div id="comment-20527-info" class="comment-info"><span class="comment-age">(17 Apr '13, 10:31)</span> Guy Harris ♦♦</div></div><span id="20564"></span><div id="comment-20564" class="comment"><div id="post-20564-score" class="comment-score"></div><div class="comment-text"><p>I compiled tshark with static linking of libpcap 1.3.0.</p><pre><code>$ tshark -v
TShark 1.6.14 (SVN Rev Unknown from unknown)

Copyright 1998-2013 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.12.3, with libpcap (version unknown), with libz
1.2.3, with POSIX capabilities (Linux), without libpcre, without SMI, without
c-ares, without ADNS, without Lua, without Python, without GnuTLS, with Gcrypt
1.4.4, with MIT Kerberos, without GeoIP.
NOTE: this build doesn&#39;t support the &quot;matches&quot; operator for Wireshark filter
syntax.

Running on Linux 2.6.18-274.18.1.el5, with libpcap version 0.9.4, with libz
1.2.3.</code></pre><p>============</p><p>When I am running tshark, it throws memory corruption error:</p><pre><code>$ cat file.pcap | tshark -r - -R&quot;gsm_map&quot;
*** glibc detected *** tshark: double free or corruption (fasttop): 0x0000000008ec6a20 ***
======= Backtrace: =========
/lib64/libc.so.6[0x3707a7247f]
/lib64/libc.so.6(cfree+0x4b)[0x3707a728db]
/usr/lib64/libwiretap.so.1(wtap_close+0x39)[0x2b93f2ce4439]
/usr/lib64/libwiretap.so.1(wtap_open_offline+0x28b)[0x2b93f2cc88ab]
tshark(cf_open+0x55)[0x421375]
tshark(main+0x1a91)[0x424cb1]
/lib64/libc.so.6(__libc_start_main+0xf4)[0x3707a1d9b4]
tshark(register_all_protocol_handoffs+0xae9)[0x40a729]
======= Memory map: ========
00400000-00435000 r-xp 00000000 68:02 6777031                            /usr/local/bin/tshark
00635000-00636000 rw-p 00035000 68:02 6777031                            /usr/local/bin/tshark
00636000-0064b000 rw-p 00636000 00:00 0
080a9000-08f01000 rw-p 080a9000 00:00 0                                  [heap]
3707600000-370761c000 r-xp 00000000 68:02 5243201                        /lib64/ld-2.5.so
370781c000-370781d000 r--p 0001c000 68:02 5243201                        /lib64/ld-2.5.so
370781d000-370781e000 rw-p 0001d000 68:02 5243201                        /lib64/ld-2.5.so
3707a00000-3707b4e000 r-xp 00000000 68:02 5243202                        /lib64/libc-2.5.so</code></pre></div><div id="comment-20564-info" class="comment-info"><span class="comment-age">(18 Apr '13, 03:49)</span> friends</div></div></div><div id="comment-tools-20519" class="comment-tools"></div><div class="clear"></div><div id="comment-20519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20500"></span>

<div id="answer-container-20500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20500-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your OS has a linker that's not stupid, i.e. a linker that allows you to specify that <em>certain particular</em> libraries be linked statically without requiring that <em>everything</em> be linked statically, it should be possible to link libpcap statically. That would require that you manually edit the Makefile; you'd put, for example, "-Bstatic" before "-lpcap" and "-Bdynamic" after it.</p><p>Finding the appropriate places to edit is left as an exercise for the reader (i.e., I'm not going to provide any more help here).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20500" class="comments-container"><span id="20510"></span><div id="comment-20510" class="comment"><div id="post-20510-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response..</p><p>Is there any parameter supported which can be passed to configure script??</p><p>Whenever I create tshark rpm, it does configure, make, install and build rpm. Manually modifying Makefile will not be feasible.</p></div><div id="comment-20510-info" class="comment-info"><span class="comment-age">(17 Apr '13, 03:44)</span> friends</div></div><span id="20520"></span><div id="comment-20520" class="comment"><div id="post-20520-score" class="comment-score"></div><div class="comment-text"><p>No, there's no configure parameter for that.</p><p>The way to do this kind of thing when building RPMs is to create a patch against the Makefile and apply it in the RPM spec file (e.g., after 'configure' but before 'make').</p></div><div id="comment-20520-info" class="comment-info"><span class="comment-age">(17 Apr '13, 07:34)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-20500" class="comment-tools"></div><div class="clear"></div><div id="comment-20500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20583"></span>

<div id="answer-container-20583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20583-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>On both the server libpcap 0.9.4 is installed. But when I compile tshark using libpcap-devel 0.9.4</p></blockquote><p>...which is what you <em>should</em> be doing; the libpcap-devel version should match the libpcap version!</p><blockquote><p>and install the rpm, then it gives memory corruption error.</p></blockquote><p>...which almost certainly has nothing whatsoever to do with the libpcap-devel version, given that you're getting the same crash when building with a later version of libpcap.</p><p>That's probably just a Wireshark bug; try building a newer version of TShark than 1.6.4, such as the current version, 1.8.6 - perhaps the bug will be fixed in that version.</p><p>(By the way, unless you're trying to test whether TShark can read from a pipe, doing</p><pre><code> cat file.pcap | tshark -r - -R&quot;gsm_map&quot;</code></pre><p>is silly; you could just do</p><pre><code>tshark -r file.pcap -R&quot;gsm_map&quot;</code></pre><p>This is what's called a <a href="http://en.wikipedia.org/wiki/Cat_(Unix)#Useless_use_of_cat">"useless use of cat"</a>.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '13, 09:34</p></div></div><div id="comments-container-20583" class="comments-container"></div><div id="comment-tools-20583" class="comment-tools"></div><div class="clear"></div><div id="comment-20583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

