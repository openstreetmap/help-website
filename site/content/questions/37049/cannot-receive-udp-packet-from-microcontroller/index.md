+++
type = "question"
title = "cannot receive UDP Packet from microcontroller"
description = '''I&#x27;m currently working on a UDP communication PC &amp;lt;-&amp;gt; ARM LM3S6965 (Luminary) through the Ethernet. On the PC there is an VB.net application that simulates a UDP server/client. When the packet is sent from the PC to the ARM LM3S6965, the packet is received without errors, but when the ARM LM3S69...'''
date = "2014-10-15T00:00:00Z"
lastmod = "2014-10-16T04:01:00Z"
weight = 37049
keywords = [ "vb.net" ]
aliases = [ "/questions/37049" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cannot receive UDP Packet from microcontroller](/questions/37049/cannot-receive-udp-packet-from-microcontroller)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37049-score" class="post-score" title="current number of votes">0</div><span id="post-37049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm currently working on a UDP communication PC &lt;-&gt; ARM LM3S6965 (Luminary) through the Ethernet. On the PC there is an VB.net application that simulates a UDP server/client.</p><p>When the packet is sent from the PC to the ARM LM3S6965, the packet is received without errors, but when the ARM LM3S6965 sends the UDP packet back to the PC, the packet is lost somewhere (the application doesn’t receive it).</p><p>The strange thing is that WireShark captures these packets coming to the PC and it seems they are valid.</p><p>Turning off Firewall in Windows did not help. I know that this topic might be wrong for this forum, but can anybody explain why WireShark captures these packets, but my application doesn’t? ARM LM3S6965 (192.168.0.100), PC (192.168.0.116), sending and receiving goes through port number 3040.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vb.net" rel="tag" title="see questions tagged &#39;vb.net&#39;">vb.net</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/dd3373f0b458e392f2d8634be735c501?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sushant%20Naik&#39;s gravatar image" /><p><span>Sushant Naik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sushant Naik has no accepted answers">0%</span></p></div></div><div id="comments-container-37049" class="comments-container"></div><div id="comment-tools-37049" class="comment-tools"></div><div class="clear"></div><div id="comment-37049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37050"></span>

<div id="answer-container-37050" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37050-score" class="post-score" title="current number of votes">0</div><span id="post-37050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There have been a few questions like this before, maybe you could search?</p><p>A guess (based on the previous questions), as you haven't provided a capture file (on a public share, e.g. Cloudshark, DropBox, Google Drive), is that the microcontroller isn't setting the destination MAC address correctly, so the PC NIC will normally discard it. When you run Wireshark it will usually capture in promiscuous mode so that all traffic that comes to the PC NIC will be accepted. You can try turning off promiscuous mode in the capture options and check if you now receive the packets from the microcontroller.</p><p>As we've had a few of these, I wonder if there's a bug in the example code or TCP/IP stack that folks are using on their microcontrollers?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '14, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37050" class="comments-container"><span id="37092"></span><div id="comment-37092" class="comment"><div id="post-37092-score" class="comment-score"></div><div class="comment-text"><p>i tried with promiscuous mode off setting, still Wireshark shows both packets PC - MCU and MCU to PC.</p></div><div id="comment-37092-info" class="comment-info"><span class="comment-age">(15 Oct '14, 21:36)</span> <span class="comment-user userinfo">Sushant Naik</span></div></div><span id="37095"></span><div id="comment-37095" class="comment"><div id="post-37095-score" class="comment-score"></div><div class="comment-text"><p>here is cloudshark link, refer line 196 and 197 <a href="https://www.cloudshark.org/captures/d76ee4287ebb?filter=udp">https://www.cloudshark.org/captures/d76ee4287ebb?filter=udp</a></p></div><div id="comment-37095-info" class="comment-info"><span class="comment-age">(16 Oct '14, 02:17)</span> <span class="comment-user userinfo">Sushant Naik</span></div></div><span id="37100"></span><div id="comment-37100" class="comment"><div id="post-37100-score" class="comment-score"></div><div class="comment-text"><p>You forgot to mention you are using UDP broadcasts. You need to ensure your PC application is setting up the UDP listener to receive broadcast messages, or modify the application and the ARM app to use actual IP addresses.</p></div><div id="comment-37100-info" class="comment-info"><span class="comment-age">(16 Oct '14, 04:01)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37050" class="comment-tools"></div><div class="clear"></div><div id="comment-37050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

