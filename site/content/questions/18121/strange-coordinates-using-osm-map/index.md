+++
type = "question"
title = "strange coordinates using OSM map"
description = '''Hi I am making an app which uses a map downloaded from OpenStreetMap. The map is of Edinburgh and I have used osm2pgsql to store the map in a PostGIS database. Here is an example of the coordinates of points in the database when I execute the following query: select ST_AsGeoJSON(way) from planet_osm...'''
date = "2012-11-30T14:43:00Z"
lastmod = "2012-11-30T15:10:00Z"
weight = 18121
keywords = [ "osm", "postgis", "coordinates" ]
aliases = [ "/questions/18121" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [strange coordinates using OSM map](/questions/18121/strange-coordinates-using-osm-map)

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
<span id="post-18121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18121-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I am making an app which uses a map downloaded from OpenStreetMap.</p>
<p>The map is of Edinburgh and I have used osm2pgsql to store the map in a PostGIS database.</p>
<p>Here is an example of the coordinates of points in the database when I execute the following query: <code>select ST_AsGeoJSON(way) from planet_osm_point;</code></p>
<pre><code>{&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[-397408.355686851020437,7575590.819041009992361]}
 {&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[-397373.846644709992688,7527300.011806310154498]}
 {&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[-397357.148721093020868,7514300.569031129591167]}
 {&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[-397356.035526185994968,7529052.908609829843044]}</code></pre>
<p>These coordinates are different than coordinates I have taken of map websites such as: <a href="http://itouchmap.com/latlong.html"><code>http://itouchmap.com/latlong.html</code></a> where coordinates in Edinburgh are like: <code>55.951324,-3.188095</code></p>
<p>Does anyone know why this is and how I convert my coordinates into the normal coordinates that are used on these mapping websites?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '12, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18121" class="comments-container">
&#10;</div>
<div id="comment-tools-18121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18121-form-container" class="comment-form-container">
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

<span id="18123"></span>

<div id="answer-container-18123" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18123-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-18123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srose has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The coordinates you are seeing are in a different projection (called "Spherical Mercator"). Either re-run your osm2pgsql import with the <code>-l</code> (ell) flag to have standard WGS84 lat/lon values in the database, or modify your query to <code>select ST_AsGeoJSON(ST_Transform(way,4326))</code> to re-project on the fly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '12, 15:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18123" class="comments-container">
&#10;</div>
<div id="comment-tools-18123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18123-form-container" class="comment-form-container">
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

