+++
type = "question"
title = "How to calculate north east lat/lon coordinates of a tile?"
description = '''HI there! I know the below code calculates the north west corner long/lat coordinates of a tile, but is there a way to calculate the north east, south east or south west corner long/lat coordinates? (I&#x27;m terrible at maths...). I&#x27;m programming in java, and any zoom around 17 - 19 would do. static dou...'''
date = "2019-05-30T02:18:00Z"
lastmod = "2019-05-30T03:06:00Z"
weight = 69372
keywords = [ "tiles", "coordinates", "java", "slippy", "slippymap" ]
aliases = [ "/questions/69372" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate north east lat/lon coordinates of a tile?](/questions/69372/how-to-calculate-north-east-latlon-coordinates-of-a-tile)

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
<span id="post-69372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>HI there! I know the below code calculates the north west corner long/lat coordinates of a tile, but is there a way to calculate the north east, south east or south west corner long/lat coordinates? (I'm terrible at maths...).</p>
<p>I'm programming in java, and any zoom around 17 - 19 would do.</p>
<p>static double tile2lon(int x, int z) { return x / Math.pow(2.0, z) * 360.0 - 180; }</p>
<p>static double tile2lat(int y, int z) { double n = Math.PI - (2.0 * Math.PI * y) / Math.pow(2.0, z); return Math.toDegrees(Math.atan(Math.sinh(n))); }</p>
<p>Thank you very much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-slippy" rel="tag" title="see questions tagged &#39;slippy&#39;">slippy</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '19, 02:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b0cd27a74487c0bf28f737a948d17e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xj18205&#39;s gravatar image" />
<p><span>xj18205</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xj18205 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69372" class="comments-container">
&#10;</div>
<div id="comment-tools-69372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69372-form-container" class="comment-form-container">
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

<span id="69373"></span>

<div id="answer-container-69373" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69373-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just realised I can use the NW corner of the surround tiles to work out this answer!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '19, 03:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b0cd27a74487c0bf28f737a948d17e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xj18205&#39;s gravatar image" />
<p><span>xj18205</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xj18205 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69373" class="comments-container">
&#10;</div>
<div id="comment-tools-69373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69373-form-container" class="comment-form-container">
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

