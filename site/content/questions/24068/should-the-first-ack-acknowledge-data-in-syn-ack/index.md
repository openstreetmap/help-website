+++
type = "question"
title = "Should the first ACK acknowledge data in Syn-Ack?"
description = '''If a Syn-Ack with data is seen, should the first ACK acknowledge the data in Syn-Ack?'''
date = "2013-08-26T09:55:00Z"
lastmod = "2013-08-26T11:23:00Z"
weight = 24068
keywords = [ "ack" ]
aliases = [ "/questions/24068" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should the first ACK acknowledge data in Syn-Ack?](/questions/24068/should-the-first-ack-acknowledge-data-in-syn-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24068-score" class="post-score" title="current number of votes">0</div><span id="post-24068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If a Syn-Ack with data is seen, should the first ACK acknowledge the data in Syn-Ack?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '13, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/ef3e021b61d2c2982734bc68dff113b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sachin%20Kulkarni&#39;s gravatar image" /><p><span>Sachin Kulkarni</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sachin Kulkarni has no accepted answers">0%</span></p></div></div><div id="comments-container-24068" class="comments-container"></div><div id="comment-tools-24068" class="comment-tools"></div><div class="clear"></div><div id="comment-24068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24071"></span>

<div id="answer-container-24071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24071-score" class="post-score" title="current number of votes">0</div><span id="post-24071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, if you mean the ACK packet that is part of the three way handshake. It is a direct reaction to the SYN-ACK and has to adjust it's acknowledge number to whatever was sent in that packet. In this case: <em>Sequence number + 1 ghost byte</em> for the SYN bit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24071" class="comments-container"></div><div id="comment-tools-24071" class="comment-tools"></div><div class="clear"></div><div id="comment-24071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

