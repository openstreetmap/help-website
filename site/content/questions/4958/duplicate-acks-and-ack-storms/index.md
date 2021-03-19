+++
type = "question"
title = "Duplicate ACKs and ACK storms"
description = '''We are having a strange issue with one of our clients. We have an SSL app that accepts an XML post, processes data and sends the response back to the client. We recently moved data centers and now are having an intermittent issue with one customer (our largest of course!). While most of the transact...'''
date = "2011-07-08T09:28:00Z"
lastmod = "2011-07-12T05:33:00Z"
weight = 4958
keywords = [ "ack", "storm" ]
aliases = [ "/questions/4958" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate ACKs and ACK storms](/questions/4958/duplicate-acks-and-ack-storms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4958-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>We are having a strange issue with one of our clients. We have an SSL app that accepts an XML post, processes data and sends the response back to the client. We recently moved data centers and now are having an intermittent issue with one customer (our largest of course!). While most of the transactions complete in less than 6 seconds, a small percentage is taking 20 seconds. The analysis of those transactions shows some very odd communication.</p><p>Basically everything starts out fine. We receive the request, process it and start streaming data back. About a second in to the response streaming we start to have duplicate ACKs, fast retransmissions and retranmissions. This continues to get worse until it becomes an ACK storm. For 16 seconds the client sends two duplicate ACKs (for the same original ACK) and our server responds with 2 ACKS. This continues until our server retrasmits a 78 byte data packet and communication normalizes. The pattern, including the retransmission of a small packet is fairly consitent. I have at least one capture that shows over 3400 dup ACKs to the same original!</p><p>Some duplicate ACKs are not unexpected. We have a DMZ firewall that is connected via multi-gigabit etherchannel. With this particular firewall that results in out-of-order packets.</p><p>We have taken captures at the host, at the Internet router and in between. We do not see packet loss occurring in our network. We have pinned the traffic to each of our two ISPs without any change in performance. We now have opened a ticket with our ISP. We have requested a capture from the customer but have not yet received that.</p><p>Many references to ACK Storms suggest a man-in-the-middle attack. Without a capture from the client I cannot validate or confirm whether this is occurring. In <strong>some</strong> of the ugly captures there are a few ACKs from the customer that have the PSH bit set (while this is not set on the bulk of the ACKs) and have a <strong>different</strong> <strong>TTL</strong> than the other responses from this customer.</p><p>Obviously I really want to see things from the customer perspective. Does anyone have an additional suggestions? <strong>Thank</strong> <strong>You</strong>!</p></div><div id="question-tags" class="tags-container tags">ack storm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '11, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/bdbf9eb175760c2fdcab4d7a2187945c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ericinsd&#39;s gravatar image" /><p>ericinsd<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ericinsd has no accepted answers">0%</span></p></div></div><div id="comments-container-4958" class="comments-container"></div><div id="comment-tools-4958" class="comment-tools"></div><div class="clear"></div><div id="comment-4958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4992"></span>

<div id="answer-container-4992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all - Good luck!</p><p>Are you using a load balancer or any kind of layer4 firewall? We've had problems in the past with certain devices (points finger at DataPower boxes) having very strange issues when it comes to XML scrubbing when using SSL with digital certificates. Our eventual bandaid was to reboot the boxes every friday evening - this would stop all issues for about a week. A firmware update eventually provided a permanent fix.</p><p>I think you're on the right path by looking at the path. How far off are the TTLs? Don't worry about the PSH bits - those may or may not be a symptom of the issue. When considering the total amount of data transmitted from you to them - does a "bad" capture resemble the "good" capture? Have you performed a double-sided capture - one on your side and one on the client side? How do those captures compare? Is the end client actually sending all of those ACKs? Is there a VPN in play somewhere - could this be a simple MTU issue?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '11, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-4992" class="comments-container"></div><div id="comment-tools-4992" class="comment-tools"></div><div class="clear"></div><div id="comment-4992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

