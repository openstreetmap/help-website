+++
type = "question"
title = "Too many TCP DUP ACK and Retransmission"
description = '''Dear all, I have too many TCP dup ack and retransmission, can someone help me to determine what is the root cause of those too many tcp dup ack and retransmission? Thank you in andvance for your help. Regards'''
date = "2015-03-12T06:23:00Z"
lastmod = "2015-03-12T09:37:00Z"
weight = 40512
keywords = [ "dup", "ack", "tcp" ]
aliases = [ "/questions/40512" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Too many TCP DUP ACK and Retransmission](/questions/40512/too-many-tcp-dup-ack-and-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40512-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all, I have too many TCP dup ack and retransmission, can someone help me to determine what is the root cause of those too many tcp dup ack and retransmission? Thank you in andvance for your help.</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">dup ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '15, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/77f21a4ea21f798253b0f8d7641322a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="optimus&#39;s gravatar image" /><p>optimus<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="optimus has no accepted answers">0%</span></p></div></div><div id="comments-container-40512" class="comments-container"></div><div id="comment-tools-40512" class="comment-tools"></div><div class="clear"></div><div id="comment-40512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40514"></span>

<div id="answer-container-40514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40514-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Duplicate ACKs and retransmissions are signs of packet loss. You need to investigate the interconnecting devices along the path between the sender and the receiver to see which device or devices are dropping packets. Note that if you are communicating with hosts outside your network, the device dropping packets might be outside your network, in which case you probably won't be able to do anything about it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '15, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-40514" class="comments-container"></div><div id="comment-tools-40514" class="comment-tools"></div><div class="clear"></div><div id="comment-40514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

