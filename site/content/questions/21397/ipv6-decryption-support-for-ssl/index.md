+++
type = "question"
title = "IPv6 decryption support for SSL"
description = '''Hi,  I am trying to decrypt SSL IPv6 packets by supplying all the correct information (Full format of IPV6 address, the RSA key, port &amp;amp; protocol). But still I am seeing that the application data contained in the SSL record is still encrypted &amp;amp; not in decrypted format. The same works fine wit...'''
date = "2013-05-23T01:55:00Z"
lastmod = "2013-05-23T02:38:00Z"
weight = 21397
keywords = [ "ipv6decryptionforssl" ]
aliases = [ "/questions/21397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPv6 decryption support for SSL](/questions/21397/ipv6-decryption-support-for-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to decrypt SSL IPv6 packets by supplying all the correct information (Full format of IPV6 address, the RSA key, port &amp; protocol). But still I am seeing that the application data contained in the SSL record is still encrypted &amp; not in decrypted format. The same works fine with IPv4 packets. I found the below link on the internet wherein other users too have brought this to notice, but unfortunately I am not able to find if this issue is resolved &amp; if yes, then which version it was resolved.</p><p><a href="http://www.wireshark.org/lists/wireshark-bugs/200903/msg00279.html">http://www.wireshark.org/lists/wireshark-bugs/200903/msg00279.html</a></p><p>The version that I am using is as below: Version 1.8.0rc2 (SVN Rev 43337 from /trunk-1.8) Compiled (64-bit) with GTK+ 2.24.10, with Cairo 1.10.2, with Pango 1.30.0, with GLib 2.32.2, with WinPcap (4_1_2), with libz 1.2.5, without POSIX capabilities, with SMI 0.4.8, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS 2.12.18, with Gcrypt 1.4.6, without Kerberos, with GeoIP, with PortAudio V19-devel (built Jun 18 2012), with AirPcap.</p><p>Running on 64-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.2 (packet.dll version 4.1.0.2001), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.12.18, Gcrypt 1.4.6, without AirPcap.</p><p>Built using Microsoft Visual C++ 10.0 build 40219</p></div><div id="question-tags" class="tags-container tags">ipv6decryptionforssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/8fb9a104b43265fe5e270a7ca1ba0352?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prabhat&#39;s gravatar image" /><p>Prabhat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prabhat has no accepted answers">0%</span></p></div></div><div id="comments-container-21397" class="comments-container"></div><div id="comment-tools-21397" class="comment-tools"></div><div class="clear"></div><div id="comment-21397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21400"></span>

<div id="answer-container-21400" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21400-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've no idea whether it will fix your problem, but try upgrading to an actual release version of Wireshark. 1.8.7 is the current stable release, see the <a href="http://www.wireshark.org/download.html">Download</a> page for more options.</p><p>The email you quote referenced <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3343">Bug 3343</a> and that was closed as fixed in April 2011 so should have been in 1.8.0rc2 (released 6 Jun 2012).</p><p>Can you post the contents of your ssl debug log (set in preferences for SSL) as a comment?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21400" class="comments-container"></div><div id="comment-tools-21400" class="comment-tools"></div><div class="clear"></div><div id="comment-21400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

