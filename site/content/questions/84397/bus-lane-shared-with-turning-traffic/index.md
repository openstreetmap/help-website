+++
type = "question"
title = "Bus lane shared with turning traffic"
description = '''How would I map a bus lane that is shared with cars that are allowed to turn right into side streets and parking lots? Cars are not allowed to cross a block. Is there a way I can map it so buses are allowed to continue straight and map that cars must turn?'''
date = "2022-05-07T05:04:00Z"
lastmod = "2022-05-07T10:25:00Z"
weight = 84397
keywords = [ "buslane", "lanes", "turnlanes" ]
aliases = [ "/questions/84397" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bus lane shared with turning traffic](/questions/84397/bus-lane-shared-with-turning-traffic)

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
<span id="post-84397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84397-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would I map a bus lane that is shared with cars that are allowed to turn right into side streets and parking lots? Cars are not allowed to cross a block. Is there a way I can map it so buses are allowed to continue straight and map that cars must turn?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buslane" rel="tag" title="see questions tagged &#39;buslane&#39;">buslane</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '22, 05:04</strong></p>
<img src="https://secure.gravatar.com/avatar/b5868b476e46281d48855dc281357d01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timbot4x4&#39;s gravatar image" />
<p><span>Timbot4x4</span><br />
<span class="score" title="101 reputation points">101</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timbot4x4 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84397" class="comments-container">
&#10;</div>
<div id="comment-tools-84397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84397-form-container" class="comment-form-container">
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

<span id="84400"></span>

<div id="answer-container-84400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84400-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming 3 lanes:<br />
<code>bus:lanes:forward=yes|yes|designated motor_vehicle:lanes:forward=yes|yes|yes turn:lanes:forward=left|through|right turn:bus:lanes:forward=left|through|through;right</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '22, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-84400" class="comments-container">
&#10;</div>
<div id="comment-tools-84400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84400-form-container" class="comment-form-container">
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

