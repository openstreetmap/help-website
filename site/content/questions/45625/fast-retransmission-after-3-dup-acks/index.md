+++
type = "question"
title = "fast retransmission after 3 DUP ACKs"
description = '''fast retranmission will kick in after 3 DUP ACK received by the sender, however in case the tcp segment before the last gets lost, does this mean TCP cannot guarantee to deliver the data ?'''
date = "2015-09-03T23:52:00Z"
lastmod = "2015-09-03T23:58:00Z"
weight = 45625
keywords = [ "retransmission" ]
aliases = [ "/questions/45625" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [fast retransmission after 3 DUP ACKs](/questions/45625/fast-retransmission-after-3-dup-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45625-score" class="post-score" title="current number of votes">0</div><span id="post-45625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>fast retranmission will kick in after 3 DUP ACK received by the sender, however in case the tcp segment before the last gets lost, does this mean TCP cannot guarantee to deliver the data ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '15, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/d34d46c446519a90354c32688a14dc51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hermau&#39;s gravatar image" /><p><span>hermau</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hermau has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '15, 23:53</strong> </span></p></div></div><div id="comments-container-45625" class="comments-container"></div><div id="comment-tools-45625" class="comment-tools"></div><div class="clear"></div><div id="comment-45625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45626"></span>

<div id="answer-container-45626" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45626-score" class="post-score" title="current number of votes">1</div><span id="post-45626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hermau has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You mean if the last segment gets lost I guess (because then there is no segment after the lost segment by which the receiver could detect a loss easily). And no, even if there's no fast retransmission the good old RTO ("Retransmission Time Out") based retransmission will make sure that all segments are transferred until acknowledged.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '15, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45626" class="comments-container"></div><div id="comment-tools-45626" class="comment-tools"></div><div class="clear"></div><div id="comment-45626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

