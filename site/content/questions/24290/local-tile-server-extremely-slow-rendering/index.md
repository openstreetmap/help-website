+++
type = "question"
title = "Local Tile Server - EXTREMELY slow rendering"
description = '''I have my own tile server on Oracle Linux. My rendering is extremely slow. I rendered an 8x8 Z16 metatile that took 124 minutes to complete. Foreground Renderd put out: renderd[5601]: DEBUG: Got incoming connection, fd 8, number 1 renderd[5601]: DEBUG: Got command RenderPrio fd(8) xml(default), z(16...'''
date = "2013-07-16T17:30:00Z"
lastmod = "2013-07-16T22:37:00Z"
weight = 24290
keywords = [ "tileserver", "renderd", "postgresql", "mapnik", "mod_tile" ]
aliases = [ "/questions/24290" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Local Tile Server - EXTREMELY slow rendering](/questions/24290/local-tile-server-extremely-slow-rendering)

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
<span id="post-24290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have my own tile server on Oracle Linux. My rendering is <strong>extremely</strong> slow. I rendered an 8x8 Z16 metatile that took 124 minutes to complete. Foreground Renderd put out:</p>
<pre><code>renderd[5601]: DEBUG: Got incoming connection, fd 8, number 1
renderd[5601]: DEBUG: Got command RenderPrio fd(8) xml(default), z(16), x(17723), y(25170)
renderd[5601]: DEBUG: Connection 0, fd 8 closed, now 0 left
renderd[5601]: DEBUG: DONE TILE default 16 17720-17727 25168-25175 in 7474.548 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/16/0/70/82/53/128.meta</code></pre>
<p>I have some PostgreSQL log statements on the order of 300,000 ms as in:</p>
<pre><code>2013-07-15 18:31:04 EDT:::1(33790):user@osm_planet:[5610]:LOG:  duration: 340648.541 ms  execute &lt;unnamed&gt;: SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;amenity&quot;,&quot;ele&quot;,&quot;landuse&quot;,&quot;leisure&quot;,&quot;man_made&quot;,&quot;military&quot;,&quot;name&quot;,&quot;natural&quot;,&quot;place&quot;,&quot;point&quot;,&quot;shop&quot;,&quot;tourism&quot;,&quot;waterway&quot; FROM (select way,aeroway,shop,access,amenity,leisure,landuse,man_made,&quot;natural&quot;,place,tourism,NULL as ele,name,ref,military,waterway,historic,&#39;no&#39;::text as point
               from planet_osm_polygon
               where amenity is not null
                  or shop in (&#39;supermarket&#39;,&#39;bakery&#39;,&#39;clothes&#39;,&#39;fashion&#39;,&#39;convenience&#39;,&#39;doityourself&#39;,&#39;hairdresser&#39;,&#39;department_store&#39;, &#39;butcher&#39;,&#39;car&#39;,&#39;car_repair&#39;,&#39;bicycle&#39;)
                  or leisure is not null
                  or landuse is not null
                  or tourism is not null
                  or &quot;natural&quot; is not null
                  or man_made in (&#39;lighthouse&#39;,&#39;windmill&#39;)
                  or place=&#39;island&#39;
                  or military=&#39;danger_area&#39;
                  or historic in (&#39;memorial&#39;,&#39;archaeological_site&#39;)
              ) as text WHERE &quot;way&quot; &amp;&amp; ST_SetSRID(&#39;BOX3D(-9202100.961200738 4642173.601817815,-9196597.495164203 4647677.067854352)&#39;::box3d, 900913)
&#10;2013-07-15 18:36:25 EDT:::1(33790):user@osm_planet:[5610]:LOG:  duration: 320782.717 ms  execute &lt;unnamed&gt;: SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;name&quot;,&quot;way_area&quot; FROM (select way,way_area,name
               from planet_osm_polygon
               where name is not null
                 and (waterway is null or waterway != &#39;riverbank&#39;)
                 and place is null
               order by way_area desc
              ) as text WHERE &quot;way&quot; &amp;&amp; ST_SetSRID(&#39;BOX3D(-9202100.961200738 4642173.601817815,-9196597.495164203 4647677.067854352)&#39;::box3d, 900913)
&#10;2013-07-15 18:41:49 EDT:::1(33790):user@osm_planet:[5610]:LOG:  duration: 324224.378 ms  execute &lt;unnamed&gt;: SELECT ST_AsBinary(&quot;way&quot;) AS geom FROM (select way,way_area,name,boundary from planet_osm_polygon where boundary=&#39;national_park&#39; and building is null) as boundary WHERE &quot;way&quot; &amp;&amp; ST_SetSRID(&#39;BOX3D(-9202100.961200738 4642173.601817815,-9196597.495164203 4647677.067854352)&#39;::box3d, 900913)</code></pre>
<p>I am using Mapnik 2.1.0, PostgreSQL 9.2, PostGIS 2. I have a 16GB instance in my company's virtual environment.</p>
<p>I tried adjusting my postgres.conf settings with pg_tune, but no luck. Something must be really wrong for 1 metatile to take 2 hours to render LOL. Any thoughts at all????</p>
<p><strong>In Response to Frederik's answer:</strong> I think you nailed it. On my sick tile server I ran EXPLAIN and got back:</p>
<pre><code>Seq Scan on planet_osm_polygon  (cost=0.00..6997002.90 rows=2 width=362)
   Filter: ((way &amp;&amp; &#39;010300002031BF0D0001000000050000000D28C29E368D61C1DE2E84665FB551410D28C29E368D61C1C8B95744BFBA51419962D8AF868A61C1C8B95744BFBA51419962D8AF868A61C1DE2E84665FB551410D28C29E368D61C1DE2E84665FB55141&#39;::geometry) AND ((ame
nity IS NOT NULL) OR (shop = ANY (&#39;{supermarket,bakery,clothes,fashion,convenience,doityourself,hairdresser,department_store,butcher,car,car_repair,bicycle}&#39;::text[])) OR (leisure IS NOT NULL) OR (landuse IS NOT NULL) OR (tourism IS NOT
NULL) OR (&quot;natural&quot; IS NOT NULL) OR (man_made = ANY (&#39;{lighthouse,windmill}&#39;::text[])) OR (place = &#39;island&#39;::text) OR (military = &#39;danger_area&#39;::text) OR (historic = ANY (&#39;{memorial,archaeological_site}&#39;::text[]))))
(2 rows)</code></pre>
<p>On a different tile server that is working better I ran the same query and got back:</p>
<pre><code> Index Scan using planet_osm_polygon_index on planet_osm_polygon  (cost=0.00..9.44 rows=1 width=1133)
   Index Cond: (way &amp;&amp; &#39;010300002031BF0D0001000000050000000D28C29E368D61C1DE2E84665FB551410D28C29E368D61C1C8B95744BFBA51419962D8AF868A61C1C8B95744BFBA51419962D8AF868A61C1DE2E84665FB551410D28C29E368D61C1DE2E84665FB55141&#39;::geometry)
   Filter: ((amenity IS NOT NULL) OR (shop = ANY (&#39;{supermarket,bakery,clothes,fashion,convenience,doityourself,hairdresser,department_store,butcher,car,car_repair,bicycle}&#39;::text[])) OR (leisure IS NOT NULL) OR (landuse IS NOT NULL) OR
(tourism IS NOT NULL) OR (&quot;natural&quot; IS NOT NULL) OR (man_made = ANY (&#39;{lighthouse,windmill}&#39;::text[])) OR (place = &#39;island&#39;::text) OR (military = &#39;danger_area&#39;::text) OR (historic = ANY (&#39;{memorial,archaeological_site}&#39;::text[])))
(3 rows)</code></pre>
<p>To my untrained eyes, this looks like my indexes are messed up on the slow server? Here is the exact osm2pgsql statement I ran, do you see anything wrong with it? Or do you think something just got arbitrarily messed up during the import and I should just try again?</p>
<pre><code>time /tiles/osm2pgsql/osm2pgsql-master/osm2pgsql -S /tiles/osm2pgsql/osm2pgsql-master/default.style --flat-nodes /tiles/flat --number-processes 4 --cache-strategy dense --slim -d osm_planet -C 8192 /tiles/planet-1304121/planet-latest.osm.pbf</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '13, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '13, 19:07</strong> </span></p>
</div>
</div>
<div id="comments-container-24290" class="comments-container">
&#10;</div>
<div id="comment-tools-24290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24290-form-container" class="comment-form-container">
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

<span id="24291"></span>

<div id="answer-container-24291" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24291-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maw269 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd normally say the performance of your virtual disk must be the culprit and it is quite possible to achieve rendering times in excess of one hour for a z7 or z8 tile if your disk is very slow, but a z16 tile - unlikely. I suggest you check whether your geometry indexes have been created correctly, by running one of the above queries past "explain" and see if it uses the index at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '13, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24291" class="comments-container">
<span id="24294"></span>
<div id="comment-24294" class="comment">
<div id="post-24294-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I put my response in my question. I think you nailed it. Any thoughts?</p>
</div>
<div id="comment-24294-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 19:09)</span> <span class="comment-user userinfo">maw269</span>
</div>
</div>
<span id="24295"></span>
<div id="comment-24295" class="comment">
<div id="post-24295-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Check whether the index actually exists (start the psql shell and type \d planet_osm_polygon). If the index does not exist: A standard osm2pgsql run will always create these indexes, so either the import was aborted or you accidentally deleted the indexes. Re-create them with "create index planet_osm_polygon_index on planet_osm_polygon using gist(way)". Same for line, road, point. If the index does exist, then for some reason PostgreSQL seems to think it isn't worth using; a simple "analyze" command might fix that (takes a couple hours though).</p>
</div>
<div id="comment-24295-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 20:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="24296"></span>
<div id="comment-24296" class="comment">
<div id="post-24296-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Perfect, I did a "\d" from the psql shell, and I am definitely missing the planet_osm_polygon_index. I am currently creating the index with "CREATE INDEX planet_osm_polygon_index ON planet_osm_polygon USING gist (way);" I compared a \d to a working tile server I have using PostgreSQL 8.4 (PostGIS 1.5), and noticed my broken 9.2 osm_planet DB also doesn't have the "geometry_columns_pg" constraint nor the "planet_osm_ways_nodes" index. Should I create these also on my broken 9.2 DB?</p>
</div>
<div id="comment-24296-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 21:05)</span> <span class="comment-user userinfo">maw269</span>
</div>
</div>
<span id="24297"></span>
<div id="comment-24297" class="comment">
<div id="post-24297-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Problem Fixed. Now rendering Z15 8x8 metatiles in around 1 second. Thanks Frederik.</p>
</div>
<div id="comment-24297-info" class="comment-info">
<span class="comment-age">(16 Jul '13, 22:37)</span> <span class="comment-user userinfo">maw269</span>
</div>
</div>
</div>
<div id="comment-tools-24291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24291-form-container" class="comment-form-container">
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

