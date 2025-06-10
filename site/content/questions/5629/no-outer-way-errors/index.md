+++
type = "question"
title = "No outer way errors"
description = '''I have inner and outer ways in a relation. I split the outer way to get under the 2,000 node api limit. Now I get a message that says that no outer ways for multipolygon when trying to upload. JOSM gives me errors when trying to upload. Is it still ok to upload a relation that has been split into mu...'''
date = "2011-06-08T09:06:00Z"
lastmod = "2011-06-08T09:20:00Z"
weight = 5629
keywords = [ "josm", "errors", "relations" ]
aliases = [ "/questions/5629" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No outer way errors](/questions/5629/no-outer-way-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have inner and outer ways in a relation. I split the outer way to get under the 2,000 node api limit. Now I get a message that says that no outer ways for multipolygon when trying to upload. JOSM gives me errors when trying to upload. Is it still ok to upload a relation that has been split into multiple part even with the error messages and still have it show up correctly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '11, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/5b617670d373ec7c3c87ad9c557327c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nmixter&#39;s gravatar image" />
<p><span>nmixter</span><br />
<span class="score" title="131 reputation points">131</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nmixter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5629" class="comments-container">
&#10;</div>
<div id="comment-tools-5629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5629-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5630"></span>

<div id="answer-container-5630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5630-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM's validator is sometimes a bit over-eager. In practice, most programs that deal with multipolygons don't even look at the outer/inner roles (because it is obvious from the geometry which rings are outside and which are inside).</p>
<p>Having said that, if you split an "outer" member of a multipolygon relation, JOSM's default behaviour is to keep both halves as relation members, with the "outer" role; so it seems that you might have done something else than what you are describing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '11, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-5630" class="comments-container">
&#10;</div>
<div id="comment-tools-5630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5630-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

