+++
type = "question"
title = "rendering performance zoomlevel 16-&gt;17 from ~0.5 secs/tile -&gt; ~70.0 secs/tile"
description = '''Rendering tiles for zoom levels from 0 to 18. This is the render_list output for levels 14, 15, and 16: Rendering z: 14 debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 16 rendering threads Rendering all tiles from zoom 14 to zoom 14 Rend...'''
date = "2020-01-24T02:30:00Z"
lastmod = "2020-01-24T23:19:00Z"
weight = 72649
keywords = [ "zoomlevel", "performance", "17" ]
aliases = [ "/questions/72649" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [rendering performance zoomlevel 16-\>17 from ~0.5 secs/tile -\> ~70.0 secs/tile](/questions/72649/rendering-performance-zoomlevel-16-17-from-05-secstile-700-secstile)

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
<span id="post-72649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Rendering tiles for zoom levels from 0 to 18.</p>
<p>This is the render_list output for levels 14, 15, and 16:</p>
<p>Rendering z: 14 debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 16 rendering threads Rendering all tiles from zoom 14 to zoom 14 Rendering all tiles for zoom 14 from (7680, 3328) to (9471, 6655) Waiting for rendering threads to finish</p>
<hr />
<hr />
<p>Total for all tiles rendered Meta tiles rendered: Rendered 93184 tiles in 7027.39 seconds (13.26 tiles/s) Total tiles rendered: Rendered 5963776 tiles in 7027.39 seconds (848.65 tiles/s) Total tiles handled: Rendered 93184 tiles in 7027.39 seconds (13.26 tiles/s)</p>
<hr />
<p>Zoom 14: min: 0.2 avg: 1.1 max: 50.8 over a total of 98611.9s in 93184 requests</p>
<hr />
<hr />
<p>Rendering z: 15 debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 16 rendering threads Rendering all tiles from zoom 15 to zoom 15 Rendering all tiles for zoom 15 from (15360, 6656) to (18943, 13311) Waiting for rendering threads to finish</p>
<hr />
<hr />
<p>Total for all tiles rendered Meta tiles rendered: Rendered 372736 tiles in 19153.29 seconds (19.46 tiles/s) Total tiles rendered: Rendered 23855104 tiles in 19153.29 seconds (1245.48 tiles/s) Total tiles handled: Rendered 372736 tiles in 19153.29 seconds (19.46 tiles/s)</p>
<hr />
<p>Zoom 15: min: 0.2 avg: 0.8 max: 31.6 over a total of 285028.0s in 372736 requests</p>
<hr />
<hr />
<p>Rendering z: 16 debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 16 rendering threads Rendering all tiles from zoom 16 to zoom 16 Rendering all tiles for zoom 16 from (30720, 13312) to (37887, 26623) Waiting for rendering threads to finish</p>
<hr />
<hr />
<p>Total for all tiles rendered Meta tiles rendered: Rendered 1490944 tiles in 67264.35 seconds (22.17 tiles/s) Total tiles rendered: Rendered 95420416 tiles in 67264.35 seconds (1418.59 tiles/s) Total tiles handled: Rendered 1490944 tiles in 67264.35 seconds (22.17 tiles/s)</p>
<hr />
<p>Zoom 16: min: 0.3 avg: 0.7 max: 11.5 over a total of 1012432.8s in 1490944 requests</p>
<hr />
<p>Generally rendering of the tiles is fast. When rendering tiles for zoom level 17, the process slows down to taking ~70 seconds per tile. (v.s. 1.1, 0.8, 0.7 second per tile in on zoom levels 14, 15, 16).</p>
<p>What the is reason for the incredible performance difference? What is the data added to the tiles on zoom level 17 that causes this type of slowdown? A quick look showed that house numbers are not displayed in zoom level 16, while they are in zoom level 17.</p>
<p>Is there anything that can be done to mitigate this performance gap?</p>
<p>Thanks! Jan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-17" rel="tag" title="see questions tagged &#39;17&#39;">17</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '20, 02:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f1449f80015277210e933d5cfa916f6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="janknepper&#39;s gravatar image" />
<p><span>janknepper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="janknepper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '20, 02:32</strong> </span></p>
</div>
</div>
<div id="comments-container-72649" class="comments-container">
<span id="72663"></span>
<div id="comment-72663" class="comment">
<div id="post-72663-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You provide next to no useful information about your database set-up, the area which you are trying to render, or why you are appear to be rendering all tiles at z17. By far and away the easiest way to resolve this is to log SQL statements under PostgreSQL, and then have a look at individual queries by seeing which ones are bottlenecks and looking at their plans. You may have data volume issues, missing indexes or any one of a number of other issues. Machine configuration, which program you are running etc are all necessary information if you wish to have useful commentary on your issue. I</p>
</div>
<div id="comment-72663-info" class="comment-info">
<span class="comment-age">(24 Jan '20, 12:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="72670"></span>
<div id="comment-72670" class="comment">
<div id="post-72670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I figured I could always add more 'specifics' as required. The issue might be something obvious I as a beginning OSM user am not aware of.</p>
<p>Used the instructions here <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a> to setup a server.</p>
<p>Imported <a href="http://download.geofabrik.de/europe-latest.osm.pbf">http://download.geofabrik.de/europe-latest.osm.pbf</a> instead of the example data.</p>
<p>The indexes according to this suggestion were added: <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/indexes.sql">https://github.com/gravitystorm/openstreetmap-carto/blob/master/indexes.sql</a></p>
<p>Have started to look at PostgreSQL logging of the SQL statements and rendering code as the problem could be in either or both.</p>
<p>Generally in my experience with an increasing level, alike the zoom level in render_list (*4), with the progression in statistics as shown, things do not change a factor 140 between levels, unless something is significantly different. This is why the question if zoom level 17+ rendering includes more or particular data.</p>
</div>
<div id="comment-72670-info" class="comment-info">
<span class="comment-age">(24 Jan '20, 19:23)</span> <span class="comment-user userinfo">janknepper</span>
</div>
</div>
</div>
<div id="comment-tools-72649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72649-form-container" class="comment-form-container">
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

<span id="72671"></span>

<div id="answer-container-72671" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did some research...</p>
<p>Turns out there is a query related to addr:housenumber and addr:housename that changes between zoom level 16 and 17 rendering.</p>
<p>In zoom level 17 rendering the query is as follows:</p>
<p>SELECT ST_AsBinary("way") AS geom,"addr_housename","addr_housenumber","addr_unit" FROM (SELECT ST_PointOnSurface(way) AS way, "addr:housenumber" AS addr_housenumber, "addr:housename" AS addr_housename, tags-&gt;'addr:unit' AS addr_unit, way_area/NULLIF(POW(4265.46<em>0.001</em>0.28,2),0) AS way_pixels FROM planet_osm_polygon WHERE way &amp;&amp; ST_SetSRID('BOX3D(511057.9711149631 6775225.31314509,513809.7041332314 6777977.046163358)'::box3d, 3857) AND (("addr:housenumber" IS NOT NULL) OR ("addr:housename" IS NOT NULL) OR ((tags-&gt;'addr:unit') IS NOT NULL)) AND building IS NOT NULL UNION ALL SELECT way, "addr:housenumber" AS addr_housenumber, "addr:housename" AS addr_housename, tags-&gt;'addr:unit' AS addr_unit, NULL AS way_pixels FROM planet_osm_point WHERE way &amp;&amp; ST_SetSRID('BOX3D(511057.9711149631 6775225.31314509,513809.7041332314 6777977.046163358)'::box3d, 3857) AND ("addr:housenumber" IS NOT NULL) OR ("addr:housename" IS NOT NULL) OR ((tags-&gt;'addr:unit') IS NOT NULL) ORDER BY way_pixels DESC NULLS LAST ) AS addresses</p>
<p>In zoom level 16 the second part of the UNION ALL has "LIMIT 0", which results in that part being ignored by SQL.</p>
<p>In zoom level 17 the second part is executed (as there is no LIMIT 0), but a close look at the WHERE clause reveals it is slightly different from the WHERE clause in the first part of the UNION ALL... A "(" and ")" is missing...</p>
<p>WHERE way &amp;&amp; ST_SetSRID('BOX3D(511057.9711149631 6775225.31314509,513809.7041332314 6777977.046163358)'::box3d, 3857) AND (("addr:housenumber" IS NOT NULL) OR ("addr:housename" IS NOT NULL) OR ((tags-&gt;'addr:unit') IS NOT NULL))</p>
<p>v.s.</p>
<p>WHERE way &amp;&amp; ST_SetSRID('BOX3D(511057.9711149631 6775225.31314509,513809.7041332314 6777977.046163358)'::box3d, 3857) AND ("addr:housenumber" IS NOT NULL) OR ("addr:housename" IS NOT NULL) OR ((tags-&gt;'addr:unit') IS NOT NULL)</p>
<p>The first ( after the AND is missing and the second ) after the NULL is missing.</p>
<p>This changes this QUERY from a couple of milliseconds into a query to 20+ seconds and an enormous result set.</p>
<p>Now the question is... Which code changes this???</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '20, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f1449f80015277210e933d5cfa916f6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="janknepper&#39;s gravatar image" />
<p><span>janknepper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="janknepper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '20, 23:29</strong> </span></p>
</div>
</div>
<div id="comments-container-72671" class="comments-container">
&#10;</div>
<div id="comment-tools-72671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72671-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

