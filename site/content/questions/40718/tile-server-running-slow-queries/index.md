+++
type = "question"
title = "Tile server running slow queries"
description = '''Hi all, i recently installed my own OSM Tileserver on a very capable machine, expecting the performance to be quite good. Unlucky for me, most tiles even at high zoom levels take much too long for a smooth user interaction. I will append information about the system and used software below. I found ...'''
date = "2015-01-30T17:45:00Z"
lastmod = "2016-06-07T18:09:00Z"
weight = 40718
keywords = [ "performance", "slow", "postgresql", "mapnik" ]
aliases = [ "/questions/40718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server running slow queries](/questions/40718/tile-server-running-slow-queries)

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
<span id="post-40718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40718-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>i recently installed my own OSM Tileserver on a very capable machine, expecting the performance to be quite good. Unlucky for me, most tiles even at high zoom levels take much too long for a smooth user interaction. I will append information about the system and used software below.</p>
<p>I found the actual slow part to be the Database, particulary some queries involving postgis functions on larger geometries. An example is the following query:</p>
<pre><code>SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;area&quot;,&quot;name&quot;,&quot;type&quot; FROM
(
    SELECT COALESCE(landuse, leisure, &quot;natural&quot;, highway, amenity, tourism) AS type,
    name, way_area AS area,   ST_PointOnSurface(way) AS way
    FROM planet_osm_polygon
    WHERE name IS NOT NULL
    AND way &amp;&amp; ST_SetSRID(&#39;BOX3D(1335354.884142745 6090349.539709539,1338106.617161014 6093101.272727807)&#39;::box3d, 900913)
    AND ST_IsValid(way)
&#10;    UNION ALL
&#10;    SELECT &#39;building&#39; AS type, name, way_area AS area, ST_PointOnSurface(way) AS way
    FROM planet_osm_polygon
    WHERE name IS NOT NULL
    AND building NOT IN (&#39;&#39;, &#39;no&#39;, &#39;0&#39;, &#39;false&#39;)
    AND way &amp;&amp; ST_SetSRID(&#39;BOX3D(1335354.884142745 6090349.539709539,1338106.617161014 6093101.272727807)&#39;::box3d, 900913)
    AND ST_IsValid(way)
    ORDER BY area DESC
) AS data
;</code></pre>
<p>The actual slow part seems to be, much to my surprise, the ST_IsValid and ST_PointOnSurface function, which take ~400ms each on a geometry that contains 134283 points. The question now is, can i - and how - reduce the time spent for those queries? 400ms for ST_IsValid seems unreasonable to me. Any help is much appreciated.</p>
<hr />
<p><strong>Stats and diagnostics</strong></p>
<p>I used the very nice tutorial at: <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
<p>Server specs:</p>
<pre><code>Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz
6 Cores, Hyperthreading
128 GiB RAM
2x 480GB SSD in Hardware RAID1</code></pre>
<p>Software used:</p>
<pre><code>Debian wheezy
Linux kernel 3.2.0
postgreSQL 9.4
postGIS 2.1
mapnik 2.2
mod_tile master from git@github.com:openstreetmap/mod_tile.git</code></pre>
<p>Mapnik style:</p>
<pre><code>OSM Bright from https://github.com/mapbox/osm-bright/archive/master.zip</code></pre>
<p>PostgreSQL configuration:</p>
<pre><code>shared_buffers = 24576MB
temp_buffers = 8MB
work_mem = 256MB
maintenance_work_mem = 32768MB</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '15, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ed73ebf04854610a34d47e2bd9068a94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markusd&#39;s gravatar image" />
<p><span>markusd</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markusd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40718" class="comments-container">
&#10;</div>
<div id="comment-tools-40718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40718-form-container" class="comment-form-container">
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

<span id="50076"></span>

<div id="answer-container-50076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50076-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've noticed the same problem with our tile server. Queries which use ST_PointOnSurface and ST_IsValid -- even in combination with a bounding box -- take several seconds to run, which kills our rendering performance. I found an <a href="http://workshops.boundlessgeo.com/postgis-intro/geometry_returning.html">intro to PostGIS</a> on Boundless which states, "ST_PointOnSurface(geometry) returns a point that is guaranteed to be inside the input argument. It is substantially more computationally expensive than the centroid operation." In my testing, I found that replacing ST_PointOnSurface with ST_Centroid and removing ST_IsValid from the query can result in about a 10-fold performance gain (396 ms vs 4533 ms for my test query, which is similar to the one in the question above).</p>
<p>The problem with changing to ST_Centroid is that the centroid of a polygon may not fall within its bounds. I ran a couple of queries to see how many OSM polygons with labels have a centroid outside of their bounds:</p>
<pre><code>SELECT count(*) FROM planet_osm_polygon WHERE name IS NOT NULL AND ST_Contains(way, ST_Centroid(way));
  count
---------
 6392511
(1 row)
&#10;select count(*) from planet_osm_polygon where name is not null;
  count  
---------
 6624842
(1 row)</code></pre>
<p>It appears that roughly 4% of the labeled polygons do not contain their centroid.</p>
<h3 id="alternate-queries">Alternate queries</h3>
<p>If speed is the most important consideration in rendering, you can rework your query to output the centroid of the geometry as follows:</p>
<pre><code>SELECT COALESCE(landuse, leisure, &quot;natural&quot;, highway, amenity, tourism) AS type,
    name, way_area AS area,
    ST_Centroid(way) AS way
  FROM planet_osm_polygon
  WHERE name IS NOT NULL
    AND way &amp;&amp; !bbox!
&#10;  UNION ALL
&#10;  SELECT &#39;building&#39; AS type, name, way_area AS area,
    ST_Centroid(way) AS way
  FROM planet_osm_polygon
  WHERE name IS NOT NULL
    AND building NOT IN (&#39;&#39;, &#39;no&#39;, &#39;0&#39;, &#39;false&#39;)
    AND way &amp;&amp; !bbox!
  ORDER BY area DESC</code></pre>
<p>The following form of the query uses the centroid when it is inside the polygon and ST_PointOnSurface when it is outside. It will always return a point within the polygon, at the cost of a little extra processing time:</p>
<pre><code>SELECT COALESCE(landuse, leisure, &quot;natural&quot;, highway, amenity, tourism) AS type,
    name, way_area AS area,
    CASE WHEN ST_Contains(way, ST_Centroid(way)) THEN ST_Centroid(way) WHEN ST_IsValid(way) THEN ST_PointOnSurface(way) ELSE null END AS way
  FROM planet_osm_polygon
  WHERE name IS NOT NULL
    AND way &amp;&amp; !bbox!
&#10;  UNION ALL
&#10;  SELECT &#39;building&#39; AS type, name, way_area AS area,
    CASE WHEN ST_Contains(way, ST_Centroid(way)) THEN ST_Centroid(way) WHEN ST_IsValid(way) THEN ST_PointOnSurface(way) ELSE null END AS way
  FROM planet_osm_polygon
  WHERE name IS NOT NULL
    AND building NOT IN (&#39;&#39;, &#39;no&#39;, &#39;0&#39;, &#39;false&#39;)
    AND way &amp;&amp; !bbox!
  ORDER BY area DESC</code></pre>
<p>In my measurements, the first query is about 10x as fast as the original, and the second about 5x as fast. We are planning to try the faster query on our tile servers. If the label placement looks strange, we will probably switch to the second version to see if there is any improvement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '16, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a62c619b246ce5027efe473b5613bc01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pegli&#39;s gravatar image" />
<p><span>pegli</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pegli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50076" class="comments-container">
&#10;</div>
<div id="comment-tools-50076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50076-form-container" class="comment-form-container">
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

