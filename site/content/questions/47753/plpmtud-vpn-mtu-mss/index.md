+++
type = "question"
title = "PLPMTUD, vpn, mtu, mss"
description = '''hi all,  can ayone please tell me, why sometimes when tunneling or any other sort of encapsulation is performed along the network path from A to B, it is necessary to lower the MTU / MSS value on a router ? Why is Packetization Layer Path MTU Discovery (PLPMTUD) no enough to sort the MTU issue out. ...'''
date = "2015-11-19T08:21:00Z"
lastmod = "2015-11-19T09:17:00Z"
weight = 47753
keywords = [ "vpn", "plpmtud", "mss", "mtu" ]
aliases = [ "/questions/47753" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PLPMTUD, vpn, mtu, mss](/questions/47753/plpmtud-vpn-mtu-mss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>can ayone please tell me, why sometimes when tunneling or any other sort of encapsulation is performed along the network path from A to B, it is necessary to lower the MTU / MSS value on a router ?</p><p>Why is Packetization Layer Path MTU Discovery (PLPMTUD) no enough to sort the MTU issue out. As per RFC 4821</p><p>"Packetization Layer Path MTU Discovery (PLPMTUD) is a method for TCP or other Packetization Protocols to dynamically discover the MTU of a path by probing with progressively larger packets. It is most efficient when used in conjunction with the ICMP-based Path MTU Discovery mechanism as specified in RFC 1191 and RFC 1981, but resolves many of the robustness problems of the classical techniques since it does not depend on the delivery of ICMP messages.</p><p>The general strategy is for the Packetization Layer to find an appropriate Path MTU by probing the path with progressively larger packets. If a probe packet is successfully delivered, then the effective Path MTU is raised to the probe size."</p><p>Also I created a small lab with two VM's and VyOS as router between and configured the MTU on both interfaces to 1500 and 700 respectively. I was not able to capture any ICMP messages as per RFC 1191</p><p>" The basic idea is that a source host initially assumes that the PMTU of a path is the (known) MTU of its first hop, and sends all datagrams on that path with the DF bit set. If any of the datagrams are too large to be forwarded without fragmentation by some router along the path, that router will discard them and return ICMP Destination Unreachable messages with a code meaning "fragmentation needed and DF set" [7]. Upon receipt of such a message (henceforth called a "Datagram Too Big" message), the source host reduces its assumed PMTU for the path."</p><p>But when using mturoute toll i can clearly see that it sends packages with different payload to determine the PMTU!</p><p>Please help my with this issue.</p><p>Bet Regards</p><p>Adam</p></div><div id="question-tags" class="tags-container tags">vpn plpmtud mss mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-47753" class="comments-container"><span id="47763"></span><div id="comment-47763" class="comment"><div id="post-47763-score" class="comment-score"></div><div class="comment-text"><p>WHochgraef interface has the MTU of 700?</p></div><div id="comment-47763-info" class="comment-info"><span class="comment-age">(19 Nov '15, 09:49)</span> Christian_R</div></div></div><div id="comment-tools-47753" class="comment-tools"></div><div class="clear"></div><div id="comment-47753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47758"></span>

<div id="answer-container-47758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47758-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because broken systems, and over-zealous admins, either fail to generate the ICMP fragmentation needed message, or block them entirely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47758" class="comments-container"></div><div id="comment-tools-47758" class="comment-tools"></div><div class="clear"></div><div id="comment-47758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

