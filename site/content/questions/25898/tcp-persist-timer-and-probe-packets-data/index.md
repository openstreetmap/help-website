+++
type = "question"
title = "TCP persist timer and probe packet&#x27;s data"
description = '''I have a doubt regarding the persist timer and the associated probe packets.  Lets say the receiver has sent out an ACK with window set to 0. As a result, the sender starts its persist timer. Now, the receiver sends an ACK with window set to 1000 and lets assume this ACK is lost in transit. So, when...'''
date = "2013-10-10T18:27:00Z"
lastmod = "2013-10-11T02:50:00Z"
weight = 25898
keywords = [ "zero-window", "tcp" ]
aliases = [ "/questions/25898" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP persist timer and probe packet's data](/questions/25898/tcp-persist-timer-and-probe-packets-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25898-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a doubt regarding the persist timer and the associated probe packets.</p><ol><li>Lets say the receiver has sent out an ACK with window set to 0.</li><li>As a result, the sender starts its persist timer.</li><li>Now, the receiver sends an ACK with window set to 1000 and lets assume this ACK is lost in transit.</li><li>So, when the persist timer pops off, the sender sends a probe packet to the receiver with a random byte in the data field.</li></ol><p>Now, what will happen at the receiver: Will it see the 1-byte as application data or is there any for the receiver to identify that this is a probe segment?</p><p>If the receiver assumes this to be application data, this might lead to consequences as the application might interpret the data in its own way.</p></div><div id="question-tags" class="tags-container tags">zero-window tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/ebc6c07016107ce674e93e9d7293e59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hdnivara&#39;s gravatar image" /><p>hdnivara<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hdnivara has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Oct '13, 18:34</p></div></div><div id="comments-container-25898" class="comments-container"></div><div id="comment-tools-25898" class="comment-tools"></div><div class="clear"></div><div id="comment-25898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25912"></span>

<div id="answer-container-25912" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25912-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 'garbage' data will be sent using an incorrect sequence number so the receiving tcp will discard the segment and not pass invalid data to the application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '13, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-25912" class="comments-container"><span id="25946"></span><div id="comment-25946" class="comment"><div id="post-25946-score" class="comment-score"></div><div class="comment-text"><p>Thanks.</p><p>I've a follow-up question: How would TCP on the sender side inform the application that the receiver will not able to receive more data at this moment?</p><p>In other words, what will be the effect on the data that the sender application pushes on to TCP if the sender's TCP buffer is full due to the zero window ACK from receiver? i.e., sender's TCP buffer is full of application data which TCP couldn't send as the receiver has not advertised a non-zero window yet. Now, the sender's application pushes more data to TCP, which can't be accommodated in the buffer.</p><p>I had a quick look on send()' man page; the error code ENOBUFS will be returned to the application if the sender's TCP buffer is full.</p><p>"ENOBUFS The output queue for a network interface was full. This generally indicates that the interface has stopped sending, but may be caused by transient congestion. (Normally, this does not occur in Linux. Packets are just silently dropped when a device queue overflows.)"</p><p>So, in Linux, if a scenario like this should arise, the sending application will have no clue on what's going on and whatever data it sends, would be lost forever. Talk about reliability :)</p></div><div id="comment-25946-info" class="comment-info"><span class="comment-age">(13 Oct '13, 07:52)</span> hdnivara</div></div></div><div id="comment-tools-25912" class="comment-tools"></div><div class="clear"></div><div id="comment-25912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

