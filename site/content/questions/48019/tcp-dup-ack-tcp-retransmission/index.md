+++
type = "question"
title = "TCP Dup ACK / TCP Retransmission"
description = '''Hey all I&#x27;m new to this whole Wireshark / internet problem solving thing so go easy on me. I have currently been having issues with my internet in regards to a 5-15% packet loss that comes and goes whenever it pleases. I Had a Telstra (ISP) technician check the line connecting my house to the road l...'''
date = "2015-11-27T03:27:00Z"
lastmod = "2015-11-27T05:26:00Z"
weight = 48019
keywords = [ "dup-ack", "retransmissions", "tcp" ]
aliases = [ "/questions/48019" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dup ACK / TCP Retransmission](/questions/48019/tcp-dup-ack-tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48019-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all</p><p>I'm new to this whole Wireshark / internet problem solving thing so go easy on me. I have currently been having issues with my internet in regards to a 5-15% packet loss that comes and goes whenever it pleases. I Had a Telstra (ISP) technician check the line connecting my house to the road line and all was fine on their end of things. I switched to a brand new modem and the problem went away for 2-3 weeks then it started occurring yesterday out of nowhere.</p><p>Here is the capture for my local area network (Ethernet connection) :</p><p><a href="https://www.cloudshark.org/captures/bd644f6be8fb">https://www.cloudshark.org/captures/bd644f6be8fb</a></p><p>I tried to interpret all the numbers but I'm not experienced enough to know what to look for. Any help would be appreciated / comment for any information I need to add.</p></div><div id="question-tags" class="tags-container tags">dup-ack retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '15, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/14c55da58e6be307e2abd25c66d73335?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HarrisonT&#39;s gravatar image" /><p>HarrisonT<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HarrisonT has no accepted answers">0%</span></p></div></div><div id="comments-container-48019" class="comments-container"></div><div id="comment-tools-48019" class="comment-tools"></div><div class="clear"></div><div id="comment-48019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48022"></span>

<div id="answer-container-48022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Work from 'the ground up' so to speak. Go over all cables, connectors, power supplies and other networking gear to make sure these are up to par (you wouldn't believe the trouble bad cables can bring).</p><p>If that all checks out go check all network interface configurations. Are they configured the same (Speed, duplexity, MTU, etc.). Ie. connecting one end as auto-configuration and the other fixed doesn't result in a working setup, oddly enough.</p><p>If that all checks out go find a well defined scenario in which the problem can be reproduced. This may be tricky to do with intermittent problems, but usually will start to point in a certain direction.</p><p>Then if you have that scenario and can capture that add these details to the question and maybe an analysis can be made from that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '15, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-48022" class="comments-container"><span id="48037"></span><div id="comment-48037" class="comment"><div id="post-48037-score" class="comment-score"></div><div class="comment-text"><p>I went through and replaced all the cables isolating each one and it turned out to be the ADSL cable. Feel like a bit of a goofball not doing that before I posted this question, my apologies. Thanks for the simple but effective advice :)</p></div><div id="comment-48037-info" class="comment-info"><span class="comment-age">(27 Nov '15, 18:41)</span> HarrisonT</div></div></div><div id="comment-tools-48022" class="comment-tools"></div><div class="clear"></div><div id="comment-48022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48023"></span>

<div id="answer-container-48023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From this short capture it is hard to even spot any packet loss. Yes, the packet in frame 52 is a retransmission of packet in frame 23, but the other retransmissions are caused by the MTU negotiation - your PC has sent a packet which was too big for your router to be transported as a whole, so the home router has sent back an ICMP message asking your PC to split the packet in two smaller ones ("fragment" it), and the PC has sent the same data in two packets, and Wireshark has marked these two smaller packets as a retransmission of the first bigger one, which is correct, except that it may be misleading without taking the context into account.</p><p>So there can actually be more cases like this, and you'd need to provide far more data to say whether there is really a packet loss somewhere or only your misinterpretation of what Wireshark is telling you.</p><p>Plus you have to bear in mind that the packet loss can occur anywhere between your PC and the remote server, so to check the quality of your line connecting you to the ISP, you'd need to track communication between your home router and the LAN of the ISP's PoP. Ping test should be enough &amp; only available for that purpose as you'd hardly find any tcp server in the PoP LAN which you'd be allowed to connect to.</p><p>In another words, even if there really is a packet loss, your ISP may be really innocent and the packet loss may happen between them and the web server you connect to, or already your home router may not handle the volume traffic you ask you to, or the ISP is guilty and the xDSL line is noisy or... So the general rule is to split the path into as many sections as you can and isolate the section which causes the trouble.</p><p>Also bear in mind that if the line speed is much lower than the LAN speed and your PC sends more packets than "fit" into the bandwidth of the line, to drop them is the only possible action taken by the router once it exhausts its buffers intended to accommodate for bursts of traffic which exceed the line capacity only for a short period of time. Some protocols (like tcp) provide a feedback to the sending side, effectively accommodating the sending speed to line bandwidth, some don't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '15, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48023" class="comments-container"></div><div id="comment-tools-48023" class="comment-tools"></div><div class="clear"></div><div id="comment-48023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

