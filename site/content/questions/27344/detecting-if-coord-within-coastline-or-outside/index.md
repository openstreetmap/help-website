+++
type = "question"
title = "Detecting if coord within coastline or outside"
description = '''So I have been trying to get a query that shows data that is within a coastline like foreach(way._[&quot;coastline&quot;]);is_in(47.995206,-122.225926);out; but it returns state and country data even though I use coord&#x27;s outside of a coastline. I would just like to know if the coord is on land or not. Any ide...'''
date = "2013-10-20T08:12:00Z"
lastmod = "2013-10-21T01:19:00Z"
weight = 27344
keywords = [ "is_in" ]
aliases = [ "/questions/27344" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Detecting if coord within coastline or outside](/questions/27344/detecting-if-coord-within-coastline-or-outside)

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
<span id="post-27344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I have been trying to get a query that shows data that is within a coastline like <code>foreach(way._["coastline"]);is_in(47.995206,-122.225926);out;</code> but it returns state and country data even though I use coord's outside of a coastline. I would just like to know if the coord is on land or not. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-is_in" rel="tag" title="see questions tagged &#39;is_in&#39;">is_in</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '13, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/e979da4d0fe3115016b4300416380452?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JacobKukuk&#39;s gravatar image" />
<p><span>JacobKukuk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JacobKukuk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27344" class="comments-container">
&#10;</div>
<div id="comment-tools-27344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27344-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="27346"></span>

<div id="answer-container-27346" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27346-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JacobKukuk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not possible to find out whether a coordinate is on land through the Overpass API, or any other OSM driven web service that I know of. The main reason for that is that land/water areas are not kept in OSM as polygons. The perfect solution for your problem would be to load the OSM coastline polygons from www.openstreetmapdata.com into a spatial database and make a query to that database. A less-than-perfect solution would be computing which tile your coordinate is on, loading that tile from an existing tile server, and checking whether the corresponding pixel is blue.</p>
<p>For the tiles@home project, we used to keep an "index PNG file" of, I believe, 4096x4096 pixels for the whole world (corresponding to one pixel per zoom level 12 tile) that would say whether a certain tile is fully water, fully land, or had coastline in it. Such a PNG file is relatively small and easy to query so maybe if your precision requirements aren't high, you could revive that old technology.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '13, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-27346" class="comments-container">
<span id="27366"></span>
<div id="comment-27366" class="comment">
<div id="post-27366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response, looks like i'm just going to setup a postgis that returns true or false if lat long is over land from a shape file. Thanks for pointing me in the right direction.</p>
</div>
<div id="comment-27366-info" class="comment-info">
<span class="comment-age">(20 Oct '13, 23:53)</span> <span class="comment-user userinfo">JacobKukuk</span>
</div>
</div>
</div>
<div id="comment-tools-27346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27346-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27369"></span>

<div id="answer-container-27369" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27369-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To add this this if you are making a postgis query you can use this query with <a href="http://openstreetmapdata.com/data/land-polygons.">http://openstreetmapdata.com/data/land-polygons.</a> This will return true or false.</p>
<p>Also Make point is somewhat backwards, instead of lat long its long lat... ST_MakePoint(Long, Lat)</p>
<pre><code>select (count(*) &gt;0) as isLand from &quot;land_polygons&quot; where 
ST_Intersects(ST_MakePoint(-122.222863,47.999535), geom);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '13, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e979da4d0fe3115016b4300416380452?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JacobKukuk&#39;s gravatar image" />
<p><span>JacobKukuk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JacobKukuk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27369" class="comments-container">
&#10;</div>
<div id="comment-tools-27369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27369-form-container" class="comment-form-container">
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

