+++
type = "question"
title = "how to display an array in proto_tree?????"
description = '''I want to dispaly an array of guint8 in proto_tree. is there any api for this??????'''
date = "2012-11-02T04:09:00Z"
lastmod = "2012-11-02T15:14:00Z"
weight = 15490
keywords = [ "proto_tree" ]
aliases = [ "/questions/15490" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to display an array in proto\_tree?????](/questions/15490/how-to-display-an-array-in-proto_tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15490-score" class="post-score" title="current number of votes">0</div><span id="post-15490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to dispaly an array of guint8 in proto_tree.</p><p>is there any api for this??????</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree" rel="tag" title="see questions tagged &#39;proto_tree&#39;">proto_tree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '12, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p><span>Akhil</span><br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div></div><div id="comments-container-15490" class="comments-container"></div><div id="comment-tools-15490" class="comment-tools"></div><div class="clear"></div><div id="comment-15490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15493"></span>

<div id="answer-container-15493" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15493-score" class="post-score" title="current number of votes">0</div><span id="post-15493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Akhil has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, you would have to construct the proto_tree your self and put the guint's in there individualy in a loop.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-15493" class="comments-container"><span id="15518"></span><div id="comment-15518" class="comment"><div id="post-15518-score" class="comment-score"></div><div class="comment-text"><p>Or put the entire array in as a single FT_BYTES item if that's more appropriate for this particular array.</p></div><div id="comment-15518-info" class="comment-info"><span class="comment-age">(02 Nov '12, 15:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-15493" class="comment-tools"></div><div class="clear"></div><div id="comment-15493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

