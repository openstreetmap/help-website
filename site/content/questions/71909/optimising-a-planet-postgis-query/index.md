+++
type = "question"
title = "Optimising a planet PostGIS query"
description = '''Hello, I&#x27;m using the OSM planet file, imported into Postgres with osm2pgsql. I&#x27;m trying to calculate a &#x27;greenery index&#x27; for each road on the planet, and one of the approaches involves working out what portion of each road lies within a 30 meter buffer of a green space (a polygon in this instance). T...'''
date = "2019-11-30T17:33:00Z"
lastmod = "2019-11-30T17:33:00Z"
weight = 71909
keywords = [ "osm2pgsql", "postgis" ]
aliases = [ "/questions/71909" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Optimising a planet PostGIS query](/questions/71909/optimising-a-planet-postgis-query)

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
<span id="post-71909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71909-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm using the OSM planet file, imported into Postgres with osm2pgsql. I'm trying to calculate a 'greenery index' for each road on the planet, and one of the approaches involves working out what portion of each road lies within a 30 meter buffer of a green space (a polygon in this instance).</p>
<p>The query works fine and produces the expected results, but it takes incredibly long. The simple version of the query below takes approximately 35 hours using the full OSM planet dataset.</p>
<p>A vastly simplified version of my query looks like the following:</p>
<pre><code>SELECT
   road.osm_id,
   -- the fuller version of the query has a lot more inside this select
   count(*)
FROM planet_osm_line AS road
INNER JOIN planet_osm_polygon_feature AS building ON ST_Intersects(road.way, building.wayb)
group by road.osm_id;</code></pre>
<p>My tables and indexes are defined as follows:</p>
<pre><code>gis=# \d+ planet_osm_line
                                         Table &quot;public.planet_osm_line&quot;
   Column   |           Type            | Collation | Nullable | Default | Storage  | Stats target | Description
------------+---------------------------+-----------+----------+---------+----------+--------------+-------------
 osm_id     | bigint                    |           |          |         | plain    |              |
 access     | text                      |           |          |         | extended |              |
 area       | text                      |           |          |         | extended |              |
 bicycle    | text                      |           |          |         | extended |              |
 bridge     | text                      |           |          |         | extended |              |
 embankment | text                      |           |          |         | extended |              |
 foot       | text                      |           |          |         | extended |              |
 harbour    | text                      |           |          |         | extended |              |
 highway    | text                      |           |          |         | extended |              |
 historic   | text                      |           |          |         | extended |              |
 landuse    | text                      |           |          |         | extended |              |
 leisure    | text                      |           |          |         | extended |              |
 name       | text                      |           |          |         | extended |              |
 network    | text                      |           |          |         | extended |              |
 natural    | text                      |           |          |         | extended |              |
 place      | text                      |           |          |         | extended |              |
 route      | text                      |           |          |         | extended |              |
 tracktype  | text                      |           |          |         | extended |              |
 tunnel     | text                      |           |          |         | extended |              |
 water      | text                      |           |          |         | extended |              |
 waterway   | text                      |           |          |         | extended |              |
 wetland    | text                      |           |          |         | extended |              |
 width      | text                      |           |          |         | extended |              |
 wood       | text                      |           |          |         | extended |              |
 z_order    | integer                   |           |          |         | plain    |              |
 way_area   | real                      |           |          |         | plain    |              |
 way        | geometry(LineString,3857) |           |          |         | main     |              |
Indexes:
    &quot;planet_osm_line_osm_id_idx&quot; btree (osm_id)
    &quot;planet_osm_line_way_idx&quot; gist (way)
    &quot;road_way&quot; btree (highway)
Access method: heap
&#10;
gis=# \d+ planet_osm_polygon_feature
                                   Table &quot;public.planet_osm_polygon_feature&quot;
   Column   |          Type           | Collation | Nullable | Default | Storage  | Stats target | Description
------------+-------------------------+-----------+----------+---------+----------+--------------+-------------
 osm_id     | bigint                  |           |          |         | plain    |              |
 access     | text                    |           |          |         | extended |              |
 area       | text                    |           |          |         | extended |              |
 bicycle    | text                    |           |          |         | extended |              |
 bridge     | text                    |           |          |         | extended |              |
 embankment | text                    |           |          |         | extended |              |
 foot       | text                    |           |          |         | extended |              |
 harbour    | text                    |           |          |         | extended |              |
 highway    | text                    |           |          |         | extended |              |
 historic   | text                    |           |          |         | extended |              |
 landuse    | text                    |           |          |         | extended |              |
 leisure    | text                    |           |          |         | extended |              |
 name       | text                    |           |          |         | extended |              |
 network    | text                    |           |          |         | extended |              |
 natural    | text                    |           |          |         | extended |              |
 place      | text                    |           |          |         | extended |              |
 route      | text                    |           |          |         | extended |              |
 tracktype  | text                    |           |          |         | extended |              |
 tunnel     | text                    |           |          |         | extended |              |
 water      | text                    |           |          |         | extended |              |
 waterway   | text                    |           |          |         | extended |              |
 wetland    | text                    |           |          |         | extended |              |
 width      | text                    |           |          |         | extended |              |
 wood       | text                    |           |          |         | extended |              |
 z_order    | integer                 |           |          |         | plain    |              |
 way_area   | real                    |           |          |         | plain    |              |
 way        | geometry(Geometry,3857) |           |          |         | main     |              |
 wayb       | geometry(Geometry,3857) |           |          |         | main     |              |
Indexes:
    &quot;feature_wayb&quot; gist (wayb) CLUSTER
    &quot;planet_osm_polygon_feature_leisure_idx&quot; btree (leisure)
    &quot;planet_osm_polygon_feature_natural_idx&quot; btree (&quot;natural&quot;)
    &quot;planet_osm_polygon_feature_osm_id_idx&quot; btree (osm_id)
    &quot;planet_osm_polygon_feature_waterway_idx&quot; btree (waterway)
    &quot;planet_osm_polygon_feature_way_idx&quot; gist (way)
Access method: heap</code></pre>
<p>The <code>planet_osm_polygon_feature.wayb</code> field is just created with st_buffer(way,30).</p>
<p>Here is my query plan:</p>
<pre><code>gis=# explain SELECT road.osm_id, count(*)
FROM planet_osm_line AS road
INNER JOIN planet_osm_polygon_feature AS building ON ST_Intersects(road.way, building.wayb)
group by road.osm_id;
                                                                      QUERY PLAN
-------------------------------------------------------------------------------------------------------------------------------------------------------
 Finalize GroupAggregate  (cost=1001.15..222836071810.48 rows=42674141 width=16)
   Group Key: road.osm_id
   -&gt;  Gather Merge  (cost=1001.15..222833724732.72 rows=384067269 width=16)
         Workers Planned: 9
         -&gt;  Partial GroupAggregate  (cost=0.99..222786057281.88 rows=42674141 width=16)
               Group Key: road.osm_id
               -&gt;  Nested Loop  (cost=0.99..222449112574.99 rows=67303593096 width=8)
                     -&gt;  Parallel Index Scan using planet_osm_line_osm_id_idx on planet_osm_line road  (cost=0.57..9513398.17 rows=19532914 width=306)
                     -&gt;  Index Scan using feature_wayb on planet_osm_polygon_feature building  (cost=0.41..11383.39 rows=455 width=2634)
                           Index Cond: (wayb &amp;&amp; road.way)
                           Filter: st_intersects(road.way, wayb)
(11 rows)</code></pre>
<p>And here are the row counts:</p>
<pre><code>gis=# select count(*) from planet_osm_line;
   count
-----------
 175796232
(1 row)
&#10;gis=# select count(*) from planet_osm_polygon_feature;
  count
---------
 4551875
(1 row)</code></pre>
<p>My Postgres config is:</p>
<pre><code>shared_buffers = 128GB
work_mem = 512MB
effective_io_concurrency = 200
max_worker_processes = 12
max_parallel_workers_per_gather = 12
max_parallel_workers = 12</code></pre>
<p>The server is a Xeon E5-1650 v3, with 256GB DDR4, and a 2TB SSD (which Postgres is allocated to use).</p>
<p>During the ~35 hour execution time, I see that the server uses approximately 80% of the CPU cores pretty much solidly, and there's almost zero disk IO.</p>
<p>I'd like to find a way of reducing the query time. I'm iterating on the SQL rules quite frequently, and the reprocessing delay is quite burdensome.</p>
<p>I fully realise I'm attempting to join two <em>massive</em> tables, I've indexed it as sensibly as I can, and my query plan seems to look okay. If I run the query just on the England dataset (which I realise is tiny in comparison to the planet), then it only takes a few minutes.</p>
<p>Anyway, if anyone has any ideas on how to improve a ~35 hour execution time, I'm all ears! Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '19, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/3599a5b9b3013b0230d176a7d98657c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samcrawford&#39;s gravatar image" />
<p><span>samcrawford</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samcrawford has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71909" class="comments-container">
&#10;</div>
<div id="comment-tools-71909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71909-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

