+++
type = "question"
title = "Postgis Plugin: ERROR:  relation &quot;planet_osm_polygon&quot; does not exist"
description = '''Hi, I am setting up mapserver on a local system following instructions at: https://switch2osm.org/manually-building-a-tile-server-18-04-lts. This went well and afterwords, I have tried to import entire planet (planet-latest.osm.pbf) using osm2pgsql the same way as mentioned in the post. After succes...'''
date = "2018-12-12T14:57:00Z"
lastmod = "2018-12-12T17:52:00Z"
weight = 67143
keywords = [ "rendering" ]
aliases = [ "/questions/67143" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Postgis Plugin: ERROR: relation "planet_osm_polygon" does not exist](/questions/67143/postgis-plugin-error-relation-planet_osm_polygon-does-not-exist)

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
<span id="post-67143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67143-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,<br />
I am setting up mapserver on a local system following instructions at: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts.">https://switch2osm.org/manually-building-a-tile-server-18-04-lts.</a> This went well and afterwords, I have tried to import entire planet (planet-latest.osm.pbf) using osm2pgsql the same way as mentioned in the post. After successful import, I have tried to pre-render tiles using render_list (render_list -m ajt -a -z $zoom_level -Z $zoom_level) and I did it from layer 0 to 14. During this time I observed an error in the log file saying that relation "planet_osm_polygon" does not exist and also map did not look at all like it had layer 14 pre-rendered (at zoom level 10 or so it was mostly blank). So, I stopped rendering and have tried to re-import a small island Saba (planet-saba-141121.osm.pbf) and I have tried to initiate rendering through zoom in/out on the map. This worked well for all layer. After that, I have tried to re-import South America and initiate rendering of some area again through zoom in/out, but rendering of certain areas resulted in the same error that I hit with render_list. Below is excerpt from the log file. I have checked postgres and table in question is there (see below). Could somebody please help me understand the problem and solve the issue? I am running this on a system that has 132GB memory and 16 Intel Xeon cpus <a href="https://help.openstreetmap.org/users/2422/25or6to4">@2</a>.1GHz.<br />
Thanks a lot!</p>
<pre><code>renderd[3347]: Rendering projected coordinates 18 82368 123296 -&gt;
-7445578.051206|1187525.671439 -7444355.058754|1188748.663892 to a 8 x 8 tile renderd[3347]: ERROR: failed to render TILE ajt 18 82368-82375 123296-123303 renderd[3347]:    reason: Postgis Plugin: ERROR:  relation &quot;planet_osm_polygon&quot; does not exist LINE 28:     FROM planet_osm_polygon
                  ^ in executeQuery Full sql was: &#39;SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;feature&quot;,&quot;name&quot;,&quot;religion&quot;,&quot;way_pixels&quot; FROM (SELECT
    way, name, religion, way_pixels,
    COALESCE(aeroway, amenity, wetland, power, landuse, leisure, man_made, &quot;natural&quot;, tourism, highway, railway) AS feature   FROM (SELECT
      way, COALESCE(name, &#39;&#39;) AS name,
      (&#39;aeroway_&#39; || (CASE WHEN aeroway IN (&#39;apron&#39;, &#39;aerodrome&#39;) THEN aeroway ELSE NULL END)) AS aeroway,
      (&#39;amenity_&#39; || (CASE WHEN amenity IN (&#39;parking&#39;, &#39;bicycle_parking&#39;, &#39;motorcycle_parking&#39;, &#39;university&#39;, &#39;college&#39;, &#39;school&#39;, &#39;taxi&#39;,
                                            &#39;hospital&#39;, &#39;kindergarten&#39;, &#39;grave_yard&#39;, &#39;prison&#39;, &#39;place_of_worship&#39;, &#39;clinic&#39;, &#39;ferry_terminal&#39;,
                                            &#39;marketplace&#39;, &#39;community_centre&#39;, &#39;social_facility&#39;, &#39;arts_centre&#39;, &#39;parking_space&#39;, &#39;bus_station&#39;,
                                            &#39;fire_station&#39;, &#39;police&#39;) THEN amenity ELSE NULL END)) AS amenity,
      (&#39;landuse_&#39; || (CASE WHEN landuse IN (&#39;quarry&#39;, &#39;vineyard&#39;, &#39;orchard&#39;, &#39;cemetery&#39;, &#39;residential&#39;, &#39;garages&#39;, &#39;meadow&#39;, &#39;grass&#39;,
                                            &#39;allotments&#39;, &#39;forest&#39;, &#39;farmyard&#39;, &#39;farmland&#39;, &#39;greenhouse_horticulture&#39;,
                                            &#39;recreation_ground&#39;, &#39;village_green&#39;, &#39;retail&#39;, &#39;industrial&#39;, &#39;railway&#39;, &#39;commercial&#39;,
                                            &#39;brownfield&#39;, &#39;landfill&#39;, &#39;construction&#39;, &#39;plant_nursery&#39;, &#39;religious&#39;) THEN landuse ELSE NULL END)) AS landuse,
      (&#39;leisure_&#39; || (CASE WHEN leisure IN (&#39;swimming_pool&#39;, &#39;playground&#39;, &#39;park&#39;, &#39;recreation_ground&#39;, &#39;common&#39;, &#39;garden&#39;,
                                            &#39;golf_course&#39;, &#39;miniature_golf&#39;, &#39;sports_centre&#39;, &#39;stadium&#39;, &#39;pitch&#39;,
                                            &#39;track&#39;, &#39;dog_park&#39;, &#39;fitness_station&#39;) THEN leisure ELSE NULL END)) AS leisure,
      (&#39;man_made_&#39; || (CASE WHEN man_made IN (&#39;works&#39;, &#39;wastewater_plant&#39;, &#39;water_works&#39;) THEN man_made ELSE NULL END)) AS man_made,
      (&#39;natural_&#39; || (CASE WHEN &quot;natural&quot; IN (&#39;beach&#39;, &#39;shoal&#39;, &#39;heath&#39;, &#39;grassland&#39;, &#39;wood&#39;, &#39;sand&#39;, &#39;scree&#39;, &#39;shingle&#39;, &#39;bare_rock&#39;, &#39;scrub&#39;) THEN &quot;natural&quot; ELSE NULL END)) AS &quot;natural&quot;,
      (&#39;wetland_&#39; || (CASE WHEN &quot;natural&quot; IN (&#39;wetland&#39;, &#39;marsh&#39;, &#39;mud&#39;) THEN (CASE WHEN &quot;natural&quot; IN (&#39;marsh&#39;, &#39;mud&#39;) THEN &quot;natural&quot; ELSE tags-&gt;&#39;wetland&#39; END) ELSE NULL END)) AS wetland,
      (&#39;power_&#39; || (CASE WHEN power IN (&#39;station&#39;, &#39;sub_station&#39;, &#39;substation&#39;, &#39;generator&#39;) THEN power ELSE NULL END)) AS power,
      (&#39;tourism_&#39; || (CASE WHEN tourism IN (&#39;camp_site&#39;, &#39;caravan_site&#39;, &#39;picnic_site&#39;) THEN tourism ELSE NULL END)) AS tourism,
      (&#39;highway_&#39; || (CASE WHEN highway IN (&#39;services&#39;, &#39;rest_area&#39;) THEN highway ELSE NULL END)) AS highway,
      (&#39;railway_&#39; || (CASE WHEN railway = &#39;station&#39; THEN railway ELSE NULL END)) AS railway,
      CASE WHEN religion IN (&#39;christian&#39;, &#39;jewish&#39;, &#39;muslim&#39;) THEN religion ELSE &#39;INT-generic&#39;::text END AS religion,
      way_area/NULLIF(0.597164::real*0.597164::real,0) AS way_pixels,
      way_area
    FROM planet_osm_polygon
    WHERE (landuse IS NOT NULL
      OR leisure IS NOT NULL
      OR aeroway IN (&#39;apron&#39;, &#39;aerodrome&#39;)
      OR amenity IN (&#39;parking&#39;, &#39;bicycle_parking&#39;, &#39;motorcycle_parking&#39;, &#39;taxi&#39;, &#39;university&#39;, &#39;college&#39;, &#39;school&#39;, &#39;hospital&#39;, &#39;kindergarten&#39;,
                     &#39;grave_yard&#39;, &#39;place_of_worship&#39;, &#39;prison&#39;, &#39;clinic&#39;, &#39;ferry_terminal&#39;, &#39;marketplace&#39;, &#39;community_centre&#39;, &#39;social_facility&#39;,
                     &#39;arts_centre&#39;, &#39;parking_space&#39;, &#39;bus_station&#39;, &#39;fire_station&#39;, &#39;police&#39;)
      OR man_made IN (&#39;works&#39;, &#39;wastewater_plant&#39;,&#39;water_works&#39;)
      OR &quot;natural&quot; IN (&#39;beach&#39;, &#39;shoal&#39;, &#39;heath&#39;, &#39;mud&#39;, &#39;marsh&#39;, &#39;wetland&#39;, &#39;grassland&#39;, &#39;wood&#39;, &#39;sand&#39;, &#39;scree&#39;, &#39;shingle&#39;, &#39;bare_rock&#39;, &#39;scrub&#39;)
      OR power IN (&#39;station&#39;, &#39;sub_station&#39;, &#39;substation&#39;, &#39;generator&#39;)
      OR tourism IN (&#39;camp_site&#39;, &#39;caravan_site&#39;, &#39;picnic_site&#39;)
      OR highway IN (&#39;services&#39;, &#39;rest_area&#39;)
      OR railway = &#39;station&#39;)
      AND way_area &gt; 1*0.597164::real*0.597164::real   ) AS landcover   ORDER BY way_area DESC, feature ) AS features WHERE &quot;way&quot; &amp;&amp; ST_SetSRID(&#39;BOX3D(-7445654.48823473
1187449.234410851,-7444278.621725596 1188825.100919985)&#39;::box3d, 3857)&#39; renderd[3347]: DEBUG: DONE TILE ajt 18 82368-82375 123296-123303 in 0.027 seconds renderd[3347]: DEBUG: Sending render cmd(4 ajt 18/82368/123298) with protocol version 2 to fd 9
&#10;postgres=# \c gis
You are now connected to database &quot;gis&quot; as user &quot;postgres&quot;.
gis=# \dt;
              List of relations
 Schema |        Name        | Type  | Owner 
--------+--------------------+-------+-------
 public | planet_osm_line    | table | user
 public | planet_osm_nodes   | table | user
 public | planet_osm_point   | table | user
 public | planet_osm_polygon | table | user
 public | planet_osm_rels    | table | user
 public | planet_osm_roads   | table | user
 public | planet_osm_ways    | table | user
 public | spatial_ref_sys    | table | user
(8 rows)
&#10;gis=# \dx;
                                     List of installed extensions
  Name   | Version |   Schema   |                             Description
&#10;---------+---------+------------+---------------------------------------------------------------------
 hstore  | 1.4     | public     | data type for storing sets of (key, value) pairs
 plpgsql | 1.0     | pg_catalog | PL/pgSQL procedural language
 postgis | 2.4.3   | public     | PostGIS geometry, geography, and raster spatial types and functions
(3 rows)
&#10;gis=#</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '18, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/04a62413b4cd3894e81352544e5c31a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brh2&#39;s gravatar image" />
<p><span>brh2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brh2 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '18, 15:21</strong> </span></p>
</div>
</div>
<div id="comments-container-67143" class="comments-container">
<span id="67145"></span>
<div id="comment-67145" class="comment">
<div id="post-67145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing that perhaps you're trying to access something in postgres that you don't have access to? Perhaps double-check the user you're doing things from?</p>
</div>
<div id="comment-67145-info" class="comment-info">
<span class="comment-age">(12 Dec '18, 17:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67143-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

