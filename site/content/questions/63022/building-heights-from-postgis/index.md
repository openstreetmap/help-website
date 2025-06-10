+++
type = "question"
title = "Building heights from PostGIS"
description = '''Hello, I have downloaded a PBF file for Europe, and loaded it to a PostGIS database (well, it&#x27;s still ongoing actually after 5 days but hopefully it&#x27;ll be done soon). In a separate PostGIS table, I have a 3.5 million point pairs which represent the start and end of road sections. These aren&#x27;t from O...'''
date = "2018-04-18T12:35:00Z"
lastmod = "2018-04-18T16:37:00Z"
weight = 63022
keywords = [ "buildings", "levels", "postgresql", "postgis", "height" ]
aliases = [ "/questions/63022" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Building heights from PostGIS](/questions/63022/building-heights-from-postgis)

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
<span id="post-63022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63022-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have downloaded a PBF file for Europe, and loaded it to a PostGIS database (well, it's still ongoing actually after 5 days but hopefully it'll be done soon).</p>
<p>In a separate PostGIS table, I have a 3.5 million point pairs which represent the start and end of road sections. These aren't from OSM.</p>
<p>What I would like to do is to find the average building height and/or number of levels in a bounding box of each point pair. I think I need to do something like this, but I'm unfamiliar with the structure of the OSM data and hope someone can help.</p>
<pre><code>SELECT     points_table.id,
           AVG(buildings.building:height)
FROM       points_table
LEFT JOIN  (SELECT building:height AS height,
                   building:levels AS levels,
                   the_geom 
            FROM   osm_polygon
            WHERE  building:height IS NOT NULL
            OR     building:levels IS NOT NULL) AS buildings
ON         st_intersects(
           st_buffer(st_makeline(points_table.point_a, points_table.pointb),100), 
           buildings.the_geom
                         )
GROUP BY  points_table.id</code></pre>
<p>Thanks,</p>
<p>James</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-levels" rel="tag" title="see questions tagged &#39;levels&#39;">levels</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-height" rel="tag" title="see questions tagged &#39;height&#39;">height</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '18, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f05b22ddc881f05935a5416414825f5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheRealJimShady&#39;s gravatar image" />
<p><span>TheRealJimShady</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheRealJimShady has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '18, 13:01</strong> </span></p>
</div>
</div>
<div id="comments-container-63022" class="comments-container">
<span id="63023"></span>
<div id="comment-63023" class="comment">
<div id="post-63023-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have you enabled the hstore option in osm2pgsql? Otherwise you won't have all the tags (such as building heights), just the default subset.</p>
</div>
<div id="comment-63023-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 13:29)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="63026"></span>
<div id="comment-63026" class="comment">
<div id="post-63026-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello Richard. Thanks for the reply. I did this...</p>
<p>osm2pgsql -d osm_europe --style openstreetmap-carto/openstreetmap-carto.style -U james -H localhost --hstore --slim -G europe-latest.osm.pbf</p>
<p>Hopefully this looks ok - it includes the hstore option.</p>
</div>
<div id="comment-63026-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 14:54)</span> <span class="comment-user userinfo">TheRealJimShady</span>
</div>
</div>
</div>
<div id="comment-tools-63022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63022-form-container" class="comment-form-container">
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

<span id="63025"></span>

<div id="answer-container-63025" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63025-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TheRealJimShady has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't say <em>how</em> you are loading the data into a PostGIS database; there are several ways (osm2pgsql, osmosis, imposm, ogr2ogr in descending order of popularity) and each will result in different data schemas. Assuming that you have used osm2pgsql, your buildings will be in <code>planet_osm_polygons</code>, and the building heights will only be available, in the <code>tags</code> column, if you have imported with <code>--hstore</code>.</p>
<p>To ease further processing, I would then create a table with all building centroids of buildings that have a height, like this</p>
<pre><code>SELECT ST_CENTROID(way) geom, tags-&gt;&#39;height&#39; as height
INTO mybuildings
FROM planet_osm_polygon
WHERE building is not null and tags?&#39;height&#39;;</code></pre>
<p>Ideally you would also want to convert the height value to a floating point value during this step, however simply casting it will fail as soon as someone has added a non-numeric value to the field. People typically use a regular expression match for that:</p>
<pre><code>SELECT ST_CENTROID(way) geom, (tags-&gt;&#39;height&#39;)::numeric as height
INTO mybuildings
FROM planet_osm_polygon
WHERE building is not null and tags-&gt;&#39;height&#39; ~ &#39;^\s*[0-9]+(\.[0-9]+)?\s*$&#39;;</code></pre>
<p>Next, you want a spatial index on your new table</p>
<pre><code>CREATE INDEX foo ON mybuildings USING gist(geom);</code></pre>
<p>Now, you'll proceed almost as planned, but be sure to use ST_DWITHIN since it can benefit from the index whereas the ST_CONTAINS/ST_BUFFER construct cannot:</p>
<pre><code>SELECT     points_table.id,
           AVG(mybuildings.height)
FROM       points_table
LEFT JOIN  mybuildings
ON         ST_DWITHIN(st_makeline(point_a, pointb), geom, 100)
GROUP BY  points_table.id;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '18, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63025" class="comments-container">
<span id="63027"></span>
<div id="comment-63027" class="comment">
<div id="post-63027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Frederik. I've loaded the data like this...:</p>
<p>osm2pgsql -d osm_europe --style openstreetmap-carto/openstreetmap-carto.style -U james -H localhost --hstore --slim -G europe-latest.osm.pbf</p>
<p>So once it has finished loading, I should be good to go I think? Thank you for your inspiration on the SQL too, much appreciated.</p>
</div>
<div id="comment-63027-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 14:56)</span> <span class="comment-user userinfo">TheRealJimShady</span>
</div>
</div>
<span id="63028"></span>
<div id="comment-63028" class="comment">
<div id="post-63028-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, that looks ok.</p>
</div>
<div id="comment-63028-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 15:23)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63029"></span>
<div id="comment-63029" class="comment">
<div id="post-63029-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thanks for your help. One final thing, the log of my import to PostGIS is still running. It says the below. Has it almost finished?</p>
<p>Committing transaction for planet_osm_point</p>
<pre><code>Committing transaction for planet_osm_line
&#10;Committing transaction for planet_osm_polygon
&#10;Committing transaction for planet_osm_roads
&#10;
Going over pending ways...
&#10;    186420914 ways are pending
&#10;
Using 1 helper-processes
&#10;
processing way (39917k) at 0.45k/s
&#10;--- skipped 46804 bytes ---
&#10;processing way (71218k) at 0.51k/s</code></pre>
</div>
<div id="comment-63029-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 15:34)</span> <span class="comment-user userinfo">TheRealJimShady</span>
</div>
</div>
<span id="63030"></span>
<div id="comment-63030" class="comment">
<div id="post-63030-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>From these numbers, the "going over pending ways" stage is likely to continue for ~ 3 days, after which the index building will take another couple of days. If you order an SSD on the Internet today, get it delivered on Friday, shut down your machine, add the SSD, and restart the whole import, it is likely to finish quicker ;)</p>
</div>
<div id="comment-63030-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 15:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63031"></span>
<div id="comment-63031" class="comment">
<div id="post-63031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Haha. Well yes. I'm using a virtual machine ran by our IT team though. Not much control over it. You've made me a tad worried about disk space now. I'm at 93%. I've got about 50GB of space left. Index's won't take that much up will they?</p>
</div>
<div id="comment-63031-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 16:09)</span> <span class="comment-user userinfo">TheRealJimShady</span>
</div>
</div>
<span id="63032"></span>
<div id="comment-63032" class="comment not_top_scorer">
<div id="post-63032-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm afraid they will, a full Europe import with indexes will likely take round about 400 GB. You can save some of that (and some processing time) if you import with <code>--drop</code> in addition to <code>--slim</code> which will get rid of some temporary tables after import, at the expense of not being able to run updates. If your machine has a ton of RAM (about 96 GB or so) you could perhaps even manage without <code>--slim</code> which would need a lot less disk space (just about 200 GB) but would not be updatable either.</p>
</div>
<div id="comment-63032-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 16:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63025" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63025-form-container" class="comment-form-container">
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

