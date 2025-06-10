+++
type = "question"
title = "Nodes displayed on tiles"
description = '''Can you advice how can I filter city part nodes displayed on tiles (standard layer) with parent relation from OSM database? I need to export hierarchy: city(city, town, village, hamlet in OSM) &amp;gt; cityPart(suburb, cityDistrict, administrative in OSM) https://nominatim.openstreetmap.org/details.php?...'''
date = "2019-10-24T08:55:00Z"
lastmod = "2019-10-24T10:37:00Z"
weight = 71300
keywords = [ "tiles", "nodes", "database" ]
aliases = [ "/questions/71300" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nodes displayed on tiles](/questions/71300/nodes-displayed-on-tiles)

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
<span id="post-71300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71300-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can you advice how can I filter city part nodes displayed on tiles (standard layer) with parent relation from OSM database?</p>
<p>I need to export hierarchy: city(city, town, village, hamlet in OSM) &gt; cityPart(suburb, cityDistrict, administrative in OSM)</p>
<p><a href="https://nominatim.openstreetmap.org/details.php?place_id=198526448">https://nominatim.openstreetmap.org/details.php?place_id=198526448</a> <img src="https://help.openstreetmap.org/upfiles/Zilina_8usFYsI.JPG" alt="Zilina example" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '19, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/199acbf6ccda81e10cb3379a8f89f5b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atom-systems&#39;s gravatar image" />
<p><span>atom-systems</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atom-systems has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '19, 09:32</strong> </span></p>
</div>
</div>
<div id="comments-container-71300" class="comments-container">
&#10;</div>
<div id="comment-tools-71300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71300-form-container" class="comment-form-container">
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

<span id="71308"></span>

<div id="answer-container-71308" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71308-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="atom-systems has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nodes are not suitable for the upper levels of the hierarchy because you cannot find out which other nodes are "below" them. Nodes are only suitable for the lowest level of the hierarchy.</p>
<p>One possible way is to install your own copy of Nominatim and extract the pre-computed hierarchies from Nominatim either through the API or by querying the database directly.</p>
<p>What you can also do is use <code>osm2pgsql</code> to import OSM data for the region you are interested in into a local PostGIS database; you can modify the "style" file to only load "boundary" and "place" objects to speed up the process.</p>
<p>Then, you can build SQL queries that give you the hierarchy you want, for example to compute a list of cities and their suburbs</p>
<pre><code>SELECT city.name, suburb.name 
FROM planet_osm_polygon city, planet_osm_point suburb
WHERE city.boundary=&#39;administrative&#39; AND city.admin_level=&#39;8&#39;
AND suburb.place=&#39;suburb&#39;
AND st_contains(city.way, suburb.way);</code></pre>
<p>And so on. (Note that this assumes cities are on admin level 8 which some larger cities might not be, and that suburbs are just points - they could also be polygons so you'd want to repeat the query above for polygonal suburbs, etc.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '19, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71308" class="comments-container">
<span id="71312"></span>
<div id="comment-71312" class="comment">
<div id="post-71312-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's working, thank you! Is there quick way how to add latitude and longitude to the select?</p>
</div>
<div id="comment-71312-info" class="comment-info">
<span class="comment-age">(24 Oct '19, 10:20)</span> <span class="comment-user userinfo">atom-systems</span>
</div>
</div>
<span id="71313"></span>
<div id="comment-71313" class="comment">
<div id="post-71313-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Quick for the database, just not quick for you typing it:</p>
<pre><code>SELECT city.name, st_x(st_centroid(st_transform(city.way,4326))) as city_lon,
  st_y(st_centroid(st_transform(city.way,4326))) as city_lat,
  suburb.name,
  st_x(st_transform(suburb.way,4326)) as sub_lon,
  st_y(st_transform(suburb.way,4326)) as sub_lat</code></pre>
<p>and then continue as above. The complexity arises from (1) having to convert the database coordinates to lat/lon with <code>st_transform</code> and (2) having to compute the centre point of the city polygon with <code>st_centroid</code>.</p>
</div>
<div id="comment-71313-info" class="comment-info">
<span class="comment-age">(24 Oct '19, 10:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71308-form-container" class="comment-form-container">
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

