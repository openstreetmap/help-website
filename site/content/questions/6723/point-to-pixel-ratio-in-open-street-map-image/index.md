+++
type = "question"
title = "Point to pixel ratio in open street map image"
description = '''I am planning to use .osm data for solving graph problems (TSP, VRP, etc.). After solving routes using the osm xml data, I plan to plot the results on a osm image using markers for vertices and paths so the end user could see the routes in a readable and comprehensible image. The problem is the data...'''
date = "2011-07-30T13:58:00Z"
lastmod = "2011-07-30T17:35:00Z"
weight = 6723
keywords = [ "marker", "image", "osm" ]
aliases = [ "/questions/6723" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Point to pixel ratio in open street map image](/questions/6723/point-to-pixel-ratio-in-open-street-map-image)

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
<span id="post-6723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6723-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am planning to use .osm data for solving graph problems (TSP, VRP, etc.). After solving routes using the osm xml data, I plan to plot the results on a osm image using markers for vertices and paths so the end user could see the routes in a readable and comprehensible image.</p>
<p>The problem is the data given on osm xml data is only latitude longitude values. So how is it scaled in the image given zoom level and bounding box? Or any suggestions on solving this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '11, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/09c53c06e6f8073f66b588f3257dbd56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jplaras&#39;s gravatar image" />
<p><span>jplaras</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jplaras has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6723" class="comments-container">
&#10;</div>
<div id="comment-tools-6723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6723-form-container" class="comment-form-container">
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

<span id="6727"></span>

<div id="answer-container-6727" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6727-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-6727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jplaras has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tiles offered by the OpenStreetMap tile servers are in the spherical mercator projection. As described in the <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#lon.2Flat_to_tile_numbers">wiki</a> you can convert from latitude to longitude using the following formulae:</p>
<pre><code>n = 2 ^ zoom
xtile = ((lon_deg + 180) / 360) * n
ytile = (1 - (log(tan(lat_rad) + sec(lat_rad)) / pi)) / 2 * n</code></pre>
<p>If you do so you normally only keep the integral part of xtile and ytile which determine the name of the tile in the <a href="http://a.tile.openstreetmap.org/zoom/xtile/ytile.png">http://a.tile.openstreetmap.org/zoom/xtile/ytile.png</a> naming scheme.</p>
<p>You can however keep the fractional part of xtile and ytile and multiply by 256 - the width of the tile - and derive which pixel of the tile contains the longitude and latitude that you started with. This allows you to plot your coordinates on top of standard OpenStreetMap tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '11, 17:35</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-6727" class="comments-container">
&#10;</div>
<div id="comment-tools-6727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6727-form-container" class="comment-form-container">
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

