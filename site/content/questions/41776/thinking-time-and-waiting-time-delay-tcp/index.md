+++
type = "question"
title = "thinking time and waiting time delay TCP"
description = '''Hello, i am capturing packets on wireshark and i should calculate the simple delays between each 2 packets, for example the time between receiving a packet and sending an ack ..i need someone to clarify for me the difference between the THINKING TIME and WAITING TIME delays .'''
date = "2015-04-24T06:14:00Z"
lastmod = "2015-04-24T06:33:00Z"
weight = 41776
keywords = [ "tcp", "wireshark" ]
aliases = [ "/questions/41776" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [thinking time and waiting time delay TCP](/questions/41776/thinking-time-and-waiting-time-delay-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41776-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i am capturing packets on wireshark and i should calculate the simple delays between each 2 packets, for example the time between receiving a packet and sending an ack ..i need someone to clarify for me the difference between the THINKING TIME and WAITING TIME delays .</p></div><div id="question-tags" class="tags-container tags">tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-41776" class="comments-container"></div><div id="comment-tools-41776" class="comment-tools"></div><div class="clear"></div><div id="comment-41776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41777"></span>

<div id="answer-container-41777" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41777-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those terms are somewhat made up, but for example consider an ICMP ping. The originator or client sends an ICMP echo request, the target or server receives the request, thinks a bout it and then sends the ICMP echo reply, which is received sometime later by the waiting client.</p><p>So, to calculate the "waiting time", you capture at the client and measure the time between the request being transmitted and the response being received.</p><p>To calculate the "thinking time", you capture at the server and measure the time between the request being received and the response being transmitted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '15, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41777" class="comments-container"><span id="41786"></span><div id="comment-41786" class="comment"><div id="post-41786-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much !</p></div><div id="comment-41786-info" class="comment-info"><span class="comment-age">(24 Apr '15, 08:45)</span> yas1234</div></div><span id="41789"></span><div id="comment-41789" class="comment"><div id="post-41789-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41789-info" class="comment-info"><span class="comment-age">(24 Apr '15, 08:56)</span> grahamb ♦</div></div></div><div id="comment-tools-41777" class="comment-tools"></div><div class="clear"></div><div id="comment-41777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

