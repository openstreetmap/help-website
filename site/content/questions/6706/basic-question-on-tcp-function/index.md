+++
type = "question"
title = "basic question on tcp function"
description = '''Hi, I would like to ask a beginners question, hope someone takes the time... As much as I read a packet is said to be lost if there is no acknowledge packet returned to the sender before the corresponding RTT timer runs out. Now my question is, how it can be detected that a segment is lost and then ...'''
date = "2011-10-04T08:14:00Z"
lastmod = "2011-10-04T08:27:00Z"
weight = 6706
keywords = [ "segment", "retransmission", "lost" ]
aliases = [ "/questions/6706" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [basic question on tcp function](/questions/6706/basic-question-on-tcp-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6706-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to ask a beginners question, hope someone takes the time...</p><p>As much as I read a packet is said to be lost if there is no acknowledge packet returned to the sender before the corresponding RTT timer runs out. Now my question is, how it can be detected that a segment is lost and then retansmitted when being on the receiver side. I also found a filter tcp.analysis.retransmission. Would this lead to the same results as tcp.analysis.lost_segment ?? Or do they refer to different transmission directions?</p><p>Thank you for any help</p><p>Martin</p></div><div id="question-tags" class="tags-container tags">segment retransmission lost</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '11, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/3a8ca29741032bd7a1c89a6204788138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mr_M_from_R&#39;s gravatar image" /><p>Mr_M_from_R<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mr_M_from_R has no accepted answers">0%</span></p></div></div><div id="comments-container-6706" class="comments-container"></div><div id="comment-tools-6706" class="comment-tools"></div><div class="clear"></div><div id="comment-6706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6707"></span>

<div id="answer-container-6707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6707-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark marks a segment as lost when there is a gap in the sequence numbers it has seen. So if you have 3 packets and Wireshark sees only packet 1 and 3 it can tell by the gap in the sequence numbers that after packet 1 there should have been packet 2. If it isn't you'll get a "previous segment lost" message for packet 3.</p><p>Retransmissions are detected by seeing another packet with the same sequence number as a previous packet, or if a packet was lost and issued later. In the case mentioned above you might get a "suspected retransmission" message when packet 2 comes in later.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '11, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '11, 08:27</p></div></div><div id="comments-container-6707" class="comments-container"></div><div id="comment-tools-6707" class="comment-tools"></div><div class="clear"></div><div id="comment-6707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

