+++
type = "question"
title = "Where is tvb_length() defined?"
description = '''I&#x27;ve been grepping through the entire code base to find for the definition of tvb_length() but it is too widely used. The only definition I found is the variable ##define tvb_length tvb_captured_length in epan/tvbuff.h. The reason for asking is because I see many instances of tvb_length(tvb) but I d...'''
date = "2014-05-12T18:52:00Z"
lastmod = "2014-05-12T20:01:00Z"
weight = 32741
keywords = [ "tvb_length" ]
aliases = [ "/questions/32741" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where is tvb\_length() defined?](/questions/32741/where-is-tvb_length-defined)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32741-score" class="post-score" title="current number of votes">1</div><span id="post-32741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been grepping through the entire code base to find for the definition of <code>tvb_length()</code> but it is too widely used. The only definition I found is the variable <code>##define tvb_length tvb_captured_length</code> in <code>epan/tvbuff.h</code>. The reason for asking is because I see many instances of <code>tvb_length(tvb)</code> but I don't know which file was included that has it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvb_length" rel="tag" title="see questions tagged &#39;tvb_length&#39;">tvb_length</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '14, 18:52</strong></p><img src="https://secure.gravatar.com/avatar/894c405be44d2f68c507f7525408a2c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drum&#39;s gravatar image" /><p><span>drum</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drum has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 May '14, 18:55</strong> </span></p></div></div><div id="comments-container-32741" class="comments-container"></div><div id="comment-tools-32741" class="comment-tools"></div><div class="clear"></div><div id="comment-32741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32744"></span>

<div id="answer-container-32744" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32744-score" class="post-score" title="current number of votes">3</div><span id="post-32744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="drum has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>tvb_length()</code> has been renamed to be <code>tvb_captured_length()</code> [which is defined in epan/tvbuff.c]</p><p><code>tvbuff.h</code> has the declaration for <code>tvb_captured_length()</code></p><p>The <code>#define tvb_length tvb_captured_length</code> in tvbuff.h is so that existing (unchanged) code will still compile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '14, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 May '14, 20:04</strong> </span></p></div></div><div id="comments-container-32744" class="comments-container"></div><div id="comment-tools-32744" class="comment-tools"></div><div class="clear"></div><div id="comment-32744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

