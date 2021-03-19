+++
type = "question"
title = "Ack before even a packet is recevied."
description = '''I am getting troubled by what seems to be a peculiar problem. we have a situation wherein we are trying to access an application over VPN but for some users its failing. VPN terminates on the FW, while client is on the inside. In the traces what I am seeing is that packets are out-of-order but Wires...'''
date = "2017-06-17T04:45:00Z"
lastmod = "2017-06-17T06:00:00Z"
weight = 62068
keywords = [ "ack", "out-of-order", "tcp", "wireshark" ]
aliases = [ "/questions/62068" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ack before even a packet is recevied.](/questions/62068/ack-before-even-a-packet-is-recevied)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62068-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting troubled by what seems to be a peculiar problem. we have a situation wherein we are trying to access an application over VPN but for some users its failing. VPN terminates on the FW, while client is on the inside. In the traces what I am seeing is that packets are out-of-order but Wireshark is not mentioning it. There is no packet loss just that packets are not arriving in order, there are no dup acks either.</p><p>What is strange is that on the ASA's inside interface I am seeing the ACK for the packets from the client which server hasnt even sent yet. I see those packets in the next frame. But I cant get my head around how I am seeing ACK even before the packets are seen on the interface. This could be something really silly but I just cant get my head around it.</p></div><div id="question-tags" class="tags-container tags">ack out-of-order tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '17, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/9a1a0de12bb57758046b74161b3d746b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravneet&#39;s gravatar image" /><p>Ravneet<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravneet has no accepted answers">0%</span></p></div></div><div id="comments-container-62068" class="comments-container"></div><div id="comment-tools-62068" class="comment-tools"></div><div class="clear"></div><div id="comment-62068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62069"></span>

<div id="answer-container-62069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62069-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know how you're actually capturing, but it's not unheard of that a monitor port can't always keep the temporal order of packet traversing the various interfaces intact.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '17, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62069" class="comments-container"></div><div id="comment-tools-62069" class="comment-tools"></div><div class="clear"></div><div id="comment-62069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

