+++
type = "question"
title = "Religious Area not showing well on map"
description = '''So, I recently updated a church in my village, replacing a point marker for the church with a Religious Area multipoly. However, it seems to have the map less obvious/clear in terms of showing the church. Have I done something wrong? https://www.openstreetmap.org/#map=19/53.71105/-1.02019'''
date = "2020-12-11T08:55:00Z"
lastmod = "2020-12-11T13:49:00Z"
weight = 77898
keywords = [ "map", "tagging" ]
aliases = [ "/questions/77898" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Religious Area not showing well on map](/questions/77898/religious-area-not-showing-well-on-map)

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
<span id="post-77898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77898-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, I recently updated a church in my village, replacing a point marker for the church with a Religious Area multipoly. However, it seems to have the map less obvious/clear in terms of showing the church. Have I done something wrong?</p>
<p><a href="https://www.openstreetmap.org/#map=19/53.71105/-1.02019">https://www.openstreetmap.org/#map=19/53.71105/-1.02019</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '20, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ebaae25b9312694c3342e8d58b3ae42a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Beranek&#39;s gravatar image" />
<p><span>John Beranek</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Beranek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77898" class="comments-container">
&#10;</div>
<div id="comment-tools-77898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77898-form-container" class="comment-form-container">
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

<span id="77899"></span>

<div id="answer-container-77899" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77899-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John Beranek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi John,</p>
<p>you are missing the <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dplace_of_worship"><code>amenity=place_of_worship</code></a> key. Add it either to the church building or the area as your feel appropriate.</p>
<p>I also noticed you have created the grave yard as multipolygon (relation) composed of three outer lines. Not sure you did that by intention or if the editor messed things up. There isn't really a need for doing it that way. If you are familiar enough with editing of relations please simplify the grave yard to a simple closed line.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '20, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-77899" class="comments-container">
<span id="77902"></span>
<div id="comment-77902" class="comment">
<div id="post-77902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I think that looks better now. I've attempted to improve the graveyard object too.</p>
</div>
<div id="comment-77902-info" class="comment-info">
<span class="comment-age">(11 Dec '20, 13:49)</span> <span class="comment-user userinfo">John Beranek</span>
</div>
</div>
</div>
<div id="comment-tools-77899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77899-form-container" class="comment-form-container">
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

