+++
type = "question"
title = "TCP packet size"
description = '''I captured a TCP stream from a linux server and a linux client (both running backtrack 5 (based on ubuntu 11.04) MSS on server and client = 1460 bytes must packets have a payload of 1448 bytes, yet some packets have larger payloads e.g 7240 = 5*1448 Does that mean the MTU set on the server OS is lar...'''
date = "2011-11-27T02:36:00Z"
lastmod = "2011-11-27T03:01:00Z"
weight = 7659
keywords = [ "mss", "tcp", "mtu" ]
aliases = [ "/questions/7659" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP packet size](/questions/7659/tcp-packet-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured a TCP stream from a linux server and a linux client (both running backtrack 5 (based on ubuntu 11.04) MSS on server and client = 1460 bytes must packets have a payload of 1448 bytes, yet some packets have larger payloads e.g 7240 = 5*1448</p><p>Does that mean the MTU set on the server OS is larger than 1500? if so how do I find the MTU value?</p><p><img src="http://s8.postimage.org/rvizqydbn/Screen_shot_2011_11_27_at_12_25_57.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">mss tcp mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '11, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p>ddayan<br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></img></div></div><div id="comments-container-7659" class="comments-container"></div><div id="comment-tools-7659" class="comment-tools"></div><div class="clear"></div><div id="comment-7659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7661"></span>

<div id="answer-container-7661" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7661-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ths MSS is what the TCP stack will use to segment data before it is being send out the network interface. However, libpcap captures the packets between the TCP stack and the NIC driver. In modern NICs, some functions of the TCP/IP stack can be offloaded to the NIC, saving CPU cycles on the system. One of the offloaded features is TCP segmentation.</p><p>So you see the large segment being sent to the NIC and the NIC will segment it into packets that will fit the MTU of the network.</p><p>You can verify this by making the trace on both sides, only on the sending side you will see the large packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '11, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7661" class="comments-container"><span id="17824"></span><div id="comment-17824" class="comment"><div id="post-17824-score" class="comment-score"></div><div class="comment-text"><p>I found this old post, which describes exactly the problem I'm having. The capture shows only large segments, but I'd like to see the individual segments (after the NIC breaks it down). I even tried capturing at the receiver side, but it seems it performs the exact same operation. Can this be done? I'm using Linux.</p></div><div id="comment-17824-info" class="comment-info"><span class="comment-age">(21 Jan '13, 13:50)</span> clod1977</div></div><span id="17825"></span><div id="comment-17825" class="comment"><div id="post-17825-score" class="comment-score"></div><div class="comment-text"><p>Or alternatively, can I set TCP to segment the packets, rather than have the NIC do it?</p></div><div id="comment-17825-info" class="comment-info"><span class="comment-age">(21 Jan '13, 14:02)</span> clod1977</div></div><span id="17826"></span><div id="comment-17826" class="comment"><div id="post-17826-score" class="comment-score"></div><div class="comment-text"><p>@clod1977 , have a look at the following links:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup/Offloading#Linux">http://wiki.wireshark.org/CaptureSetup/Offloading#Linux</a></li><li><a href="http://www.ryanfrantz.com/2011/02/03/tcp-segmentation-offload/">http://www.ryanfrantz.com/2011/02/03/tcp-segmentation-offload/</a></li></ul></div><div id="comment-17826-info" class="comment-info"><span class="comment-age">(21 Jan '13, 14:21)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-7661" class="comment-tools"></div><div class="clear"></div><div id="comment-7661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

