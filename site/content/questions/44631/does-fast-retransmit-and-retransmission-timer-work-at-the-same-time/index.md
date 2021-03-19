+++
type = "question"
title = "Does Fast Retransmit and Retransmission Timer work at the same time?"
description = '''When Fast Retransmit is implemented, if I received packet 1, then I will send an ACK that says I need packet 2, and then if I received packet 3, I will send a duplicate ACK that says that I need packet 2 (and not packet 4). But will packet 2 on the sender side also have a Retransmission Timer assign...'''
date = "2015-07-30T06:10:00Z"
lastmod = "2015-07-31T02:02:00Z"
weight = 44631
keywords = [ "windows", "networking", "tcp" ]
aliases = [ "/questions/44631" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does Fast Retransmit and Retransmission Timer work at the same time?](/questions/44631/does-fast-retransmit-and-retransmission-timer-work-at-the-same-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44631-score" class="post-score" title="current number of votes">0</div><span id="post-44631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When Fast Retransmit is implemented, if I received <strong>packet 1</strong>, then I will send an ACK that says I need <strong>packet 2</strong>, and then if I received <strong>packet 3</strong>, I will send a duplicate ACK that says that I need <strong>packet 2</strong> (and not <strong>packet 4</strong>).</p><p>But will <strong>packet 2</strong> on the sender side also have a Retransmission Timer assigned to it, that is, will there be a timer that is waiting for an ACK for <strong>packet 2</strong> to arrive, and if it did not arrive it will retransmit it?</p><p>I think that the answer is Yes, because what if the duplicate ACK got lost! is this correct or am I missing something?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/e15d1d4db326472a053064f3e26fc079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_857&#39;s gravatar image" /><p><span>John_857</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_857 has no accepted answers">0%</span></p></div></div><div id="comments-container-44631" class="comments-container"></div><div id="comment-tools-44631" class="comment-tools"></div><div class="clear"></div><div id="comment-44631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44672"></span>

<div id="answer-container-44672" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44672-score" class="post-score" title="current number of votes">0</div><span id="post-44672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John_857 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not entirely sure I understand your question, however:</p><p>The ACK you send merely confirms you have received Data to xxx Bytes. The sender then sends the next sequence to you and you then ACK that Number of Bytes. If Packet(s) go missing you will ACK what you have and ask for the missing ones, if there is no SACK running, you will stop at the missing Packet and wait for it. If you have SACK (which you should) then the new packets will continue to be received and you will simply keep asking for the missing packets until they arrive.</p><p>The RTO will also be set on the retransmissions, if a Server does not receive an ACK inside of the RTO, then it should retransmit up to the Maximum No. of Retransmissions you have set before giving up and [RST]ing your connection.</p><p>usually the Duplicate Acks will arrive before the RTO kicks in and a (Fast)Retransmission will occur in an established connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '15, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44672" class="comments-container"></div><div id="comment-tools-44672" class="comment-tools"></div><div class="clear"></div><div id="comment-44672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

