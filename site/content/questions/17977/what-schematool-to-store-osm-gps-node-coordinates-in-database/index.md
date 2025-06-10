+++
type = "question"
title = "What Schema/Tool to store OSM GPS node coordinates in database?"
description = '''I need to store data of an area (.osm file) to a DB, specifically road and intersection data and points along these roads, both including their GPS coordinates. The idea is to give the system a GPS coordinate and be able to relate that coordinate to a node or road (way?) within the area. (No map ren...'''
date = "2012-11-26T07:50:00Z"
lastmod = "2012-11-26T09:41:00Z"
weight = 17977
keywords = [ "schema", "database", "osm", "postgresql", "gps" ]
aliases = [ "/questions/17977" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What Schema/Tool to store OSM GPS node coordinates in database?](/questions/17977/what-schematool-to-store-osm-gps-node-coordinates-in-database)

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
<span id="post-17977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17977-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to store data of an area (.osm file) to a DB, specifically road and intersection data and points along these roads, both including their <strong>GPS coordinates</strong>. The idea is to give the system a GPS coordinate and be able to relate that coordinate to a node or road (way?) within the area. (No map rendering is requires; strictly just the coordinate data)</p>
<p>I've tried loading an osm file to a PostGreSQL + PostGIS database using osm2pgsql, however I later found out that this method maps nodes and ways to lines and polygons...problem there :/</p>
<p>Could anyone suggest the right tool for the cause? Would PostGIS snapshot do the trick?</p>
<p><strong>Note: This is a follow-up question to <a href="https://help.openstreetmap.org/questions/17787/right-importerdatabase-schema-to-store-osm-road-nodes-and-intersections-relations">https://help.openstreetmap.org/questions/17787/right-importerdatabase-schema-to-store-osm-road-nodes-and-intersections-relations</a></strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '12, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/afbf8ac71c39825569d7ba732a0c304c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JuZeeMan&#39;s gravatar image" />
<p><span>JuZeeMan</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JuZeeMan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17977" class="comments-container">
&#10;</div>
<div id="comment-tools-17977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17977-form-container" class="comment-form-container">
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

<span id="17979"></span>

<div id="answer-container-17979" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17979-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please explain in more detail why the osm2pgsql database doesn't work for you.</p>
<p>Of course it creates lines for way features but you can always get the coordinates of a way with <code>st_astext(way)</code> or similar, and you can find out all ways in the vicinity of a point with <code>st_dwithin</code> - for example</p>
<pre><code>SELECT 
   name,highway,st_astext(way)
FROM
   planet_osm_line
WHERE
   highway IS NOT NULL
AND
   st_dwithin(way, 
      st_setsrid(st_makepoint(8.1234,49.1234),4326), .01)</code></pre>
<p>This gives you all ways that touch within approx. 1km (0.01 degrees) of the point whose coordinates are given as a lon,lat pair. This works for a database imported with the <code>-l</code> (ell) flag. A database imported without that will have geometries stored in a different coordinate system, and will require something like</p>
<pre><code>   st_dwithin(way, 
      st_transform(st_setsrid(st_makepoint(8.1234,49.1234),4326),900913), 1000)</code></pre>
<p>(note that in this case the unit of distance is roughly metres, not degrees). To list the coordinates in degrees you would also want to use <code>st_astext(st_transform(way,4326))</code> instead of just <code>st_astext(way)</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '12, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17979" class="comments-container">
&#10;</div>
<div id="comment-tools-17979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17979-form-container" class="comment-form-container">
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

