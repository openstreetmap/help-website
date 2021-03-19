+++
type = "question"
title = "Udp packet are duplicated  in capture"
description = '''Yesterday I was debugging one my program and found bug in wireshark or somewhere else. Wireshark shows me two UDP packets on transmit with small time difference and with all matching bytes. Even IP identifier is same in both packets. When I send this packet to my router and make packet capture it sh...'''
date = "2017-08-26T07:58:00Z"
lastmod = "2017-08-28T10:28:00Z"
weight = 63519
keywords = [ "capture", "udp", "udp-transmit", "duplicated" ]
aliases = [ "/questions/63519" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Udp packet are duplicated in capture](/questions/63519/udp-packet-are-duplicated-in-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63519-score" class="post-score" title="current number of votes">0</div><span id="post-63519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Yesterday I was debugging one my program and found bug in wireshark or somewhere else.</p><p>Wireshark shows me two UDP packets on transmit with small time difference and with all matching bytes.<br />
Even IP identifier is same in both packets.<br />
When I send this packet to my router and make packet capture it shows that only one packet is send from my PC.</p><p>Wireshark is version 2.4.0</p><p>How can I find where it comes to this problem ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-udp-transmit" rel="tag" title="see questions tagged &#39;udp-transmit&#39;">udp-transmit</span> <span class="post-tag tag-link-duplicated" rel="tag" title="see questions tagged &#39;duplicated&#39;">duplicated</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '17, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/0c028905e72e5648f7a9b9dcdb74c0d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marenr&#39;s gravatar image" /><p><span>marenr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marenr has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-63519" class="comments-container"><span id="63520"></span><div id="comment-63520" class="comment"><div id="post-63520-score" class="comment-score"></div><div class="comment-text"><p>You'll need to provide much more info on your capturing setup, i.e.</p><ol><li>Is this on-machine or via a tap or router?</li><li>If on-machine, what is the host OS?</li><li>What is the capture library, e.g. libpcap, WinPcap, npcap?</li><li>What type of interface are you capturing\transmitting on?</li><li>Is there a VM involved?</li></ol><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc?</p></div><div id="comment-63520-info" class="comment-info"><span class="comment-age">(26 Aug '17, 09:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63529"></span><div id="comment-63529" class="comment"><div id="post-63529-score" class="comment-score"></div><div class="comment-text"><p>I make capture again.</p><p>Router capture: <a href="https://www.cloudshark.org/captures/d8a18c34c5de">https://www.cloudshark.org/captures/d8a18c34c5de</a> Computer capture: <a href="https://www.cloudshark.org/captures/765cda700089">https://www.cloudshark.org/captures/765cda700089</a></p><p>This is Win 10 Pc and capture is made on Ethernet controller with VirtualBox and VmWare Workstation installed but not running at capture time. I also found that all outgoing packets from my PC are duplicated.</p><p>I googled how to find which library does Wireshark use but I did not find it. Can I get some instructions?</p></div><div id="comment-63529-info" class="comment-info"><span class="comment-age">(28 Aug '17, 04:16)</span> <span class="comment-user userinfo">marenr</span></div></div><span id="63530"></span><div id="comment-63530" class="comment"><div id="post-63530-score" class="comment-score"></div><div class="comment-text"><p>If you post the content of the Help-About dialog, that will show the capture library being used.</p></div><div id="comment-63530-info" class="comment-info"><span class="comment-age">(28 Aug '17, 04:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63532"></span><div id="comment-63532" class="comment"><div id="post-63532-score" class="comment-score"></div><div class="comment-text"><p>I also read this but I missed mention of libpcap.<br />
Here is About:</p><p>Version 2.4.0 (v2.4.0-0-g9be0fa500d)</p><p>Copyright 1998-2017 Gerald Combs <span><span class="__cf_email__" data-cfemail="4f282a3d2e232b0f38263d2a3c272e3d2461203d28">[email protected]</span></span> and contributors. License GPLv2+: GNU GPL version 2 or later <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with Qt 5.9.1, with WinPcap (4_1_3), with GLib 2.42.0, with zlib 1.2.8, with SMI 0.4.8, with c-ares 1.12.0, with Lua 5.2.4, with GnuTLS 3.4.11, with Gcrypt 1.7.6, with MIT Kerberos, with GeoIP, with nghttp2 1.14.0, with LZ4, with Snappy, with libxml2 2.9.4, with QtMultimedia, with AirPcap, with SBC, with SpanDSP.</p><p>Running on 64-bit Windows 10, build 15063, with Intel(R) Core(TM) i7-4810MQ CPU @ 2.80GHz (with SSE4.2), with 32683 MB of physical memory, with locale Slovenian_Slovenia.1250, with WinPcap version 4.1.3 (packet.dll version 0.78 r5), based on libpcap version 1.0 branch 1_0_rel0b (20091008), with GnuTLS 3.4.11, with Gcrypt 1.7.6, without AirPcap.</p><p>Built using Microsoft Visual C++ 14.0 build 24215</p></div><div id="comment-63532-info" class="comment-info"><span class="comment-age">(28 Aug '17, 04:56)</span> <span class="comment-user userinfo">marenr</span></div></div></div><div id="comment-tools-63519" class="comment-tools"></div><div class="clear"></div><div id="comment-63519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63533"></span>

<div id="answer-container-63533" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63533-score" class="post-score" title="current number of votes">1</div><span id="post-63533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="marenr has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote>Running on 64-bit Windows 10, build 15063, with Intel(R) Core(TM) i7-4810MQ CPU @ 2.80GHz (with SSE4.2), with 32683 MB of physical memory, with locale Slovenian_Slovenia.1250, with WinPcap version 4.1.3 <strong>(packet.dll version 0.78 r5)</strong></blockquote><p>It looks like you're not using the default WinPcap capture library, I suspect it's some older version of npcap.</p><p>Can you remove npcap, reboot and re-install Wireshark allowing it to install WinPcap?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '17, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-63533" class="comments-container"><span id="63534"></span><div id="comment-63534" class="comment"><div id="post-63534-score" class="comment-score"></div><div class="comment-text"><p>After removing nmap and reinstalling Wireshark with WinPcap it works as it must.<br />
Thank you.</p></div><div id="comment-63534-info" class="comment-info"><span class="comment-age">(28 Aug '17, 06:00)</span> <span class="comment-user userinfo">marenr</span></div></div><span id="63537"></span><div id="comment-63537" class="comment"><div id="post-63537-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/42006/marenr">@marenr</a></p><p>I've moved my comment to an answer as it seems to have resolved your issue.</p><p>Can you accept the answer by clicking the check mark icon on the answer so that others may see the correct answer for the issue?</p></div><div id="comment-63537-info" class="comment-info"><span class="comment-age">(28 Aug '17, 10:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-63533" class="comment-tools"></div><div class="clear"></div><div id="comment-63533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

