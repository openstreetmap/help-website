+++
type = "question"
title = "Renderd issue"
description = '''Imported just part of the world using  osm2pgsql -d gis --slim -C 1000 --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua --hstore ~trent/data/oklahoma-latest.osm.pbf no issues. ran fine. use renderd  An error occurred while loading the map layer &#x27;ajt&#x27;: Postgis Plugin: ERROR: r...'''
date = "2020-06-27T20:35:00Z"
lastmod = "2020-06-28T11:43:00Z"
weight = 75449
keywords = [ "renderd" ]
aliases = [ "/questions/75449" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Renderd issue](/questions/75449/renderd-issue)

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
<span id="post-75449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75449-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Imported just part of the world using osm2pgsql -d gis --slim -C 1000 --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua --hstore ~trent/data/oklahoma-latest.osm.pbf</p>
<p>no issues. ran fine.</p>
<p>use renderd An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: relation "icesheet_polygons" does not exist LINE 1: SELECT ST_SRID("way") AS srid FROM icesheet_polygons WHERE "... ^</p>
<p>any ideas what I may be missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '20, 20:35</strong></p>
<img src="https://secure.gravatar.com/avatar/cbea797cf56fb87a893b11776614d836?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trent&#39;s gravatar image" />
<p><span>Trent</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trent has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75449" class="comments-container">
<span id="75452"></span>
<div id="comment-75452" class="comment">
<div id="post-75452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is the import</p>
<p>osm2pgsql -d gis --create --slim -C 1000 --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua --hstore ~trent/data/oklahoma-latest.osm.bz2 osm2pgsql version 1.2.1 (64 bit id space)</p>
<p>Allocating memory for dense node cache Allocating dense node cache in one big chunk Allocating memory for sparse node cache Sharing dense sparse Node-cache: cache=1000MB, maxblocks=16000*65536, allocation method=11 Mid: pgsql, cache=1000 Setting up table: planet_osm_nodes Setting up table: planet_osm_ways Setting up table: planet_osm_rels Using lua based tag processing pipeline with script /home/renderaccount/src/openstreetmap-carto/openstreetmap-carto.lua Using projection SRS 3857 (Spherical Mercator) Setting up table: planet_osm_point Setting up table: planet_osm_line Setting up table: planet_osm_polygon Setting up table: planet_osm_roads</p>
<p>Reading in file: /home/trent/data/oklahoma-latest.osm.bz2 Using XML parser. Processing: Node(14516k 241.9k/s) Way(1034k 13.98k/s) Relation(7730 1932.50/s) parse time: 138s Node stats: total(14516137), max(7650266568) in 60s Way stats: total(1034427), max(819194812) in 74s Relation stats: total(12246), max(11228623) in 4s Sorting data and creating indexes for planet_osm_point Sorting data and creating indexes for planet_osm_line Sorting data and creating indexes for planet_osm_polygon Sorting data and creating indexes for planet_osm_roads Copying planet_osm_roads to cluster by geometry finished Creating geometry index on planet_osm_roads Copying planet_osm_point to cluster by geometry finished Creating geometry index on planet_osm_point Creating osm_id index on planet_osm_roads Creating indexes on planet_osm_roads finished All indexes on planet_osm_roads created in 7s Completed planet_osm_roads Stopping table: planet_osm_nodes Stopped table: planet_osm_nodes in 0s Stopping table: planet_osm_ways Building index on table: planet_osm_ways Creating osm_id index on planet_osm_point Creating indexes on planet_osm_point finished All indexes on planet_osm_point created in 13s Completed planet_osm_point Stopping table: planet_osm_rels Building index on table: planet_osm_rels Stopped table: planet_osm_rels in 1s Copying planet_osm_polygon to cluster by geometry finished Creating geometry index on planet_osm_polygon Creating osm_id index on planet_osm_polygon Creating indexes on planet_osm_polygon finished All indexes on planet_osm_polygon created in 40s Completed planet_osm_polygon Stopped table: planet_osm_ways in 79s Copying planet_osm_line to cluster by geometry finished Creating geometry index on planet_osm_line Creating osm_id index on planet_osm_line Creating indexes on planet_osm_line finished All indexes on planet_osm_line created in 97s Completed planet_osm_line</p>
<p>Osm2pgsql took 237s overall node cache: stored: 14516137(100.00%), storage efficiency: 55.33% (dense blocks: 654, sparse nodes: 10439284), hit rate: 100.00%</p>
</div>
<div id="comment-75452-info" class="comment-info">
<span class="comment-age">(28 Jun '20, 01:10)</span> <span class="comment-user userinfo">Trent</span>
</div>
</div>
<span id="75457"></span>
<div id="comment-75457" class="comment">
<div id="post-75457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide more details about what versions of everything you are using?</p>
</div>
<div id="comment-75457-info" class="comment-info">
<span class="comment-age">(28 Jun '20, 11:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75449-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="75450"></span>

<div id="answer-container-75450" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75450-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At the risk of stating the bleeding obvious, something has gone wrong with the way that you've loaded the data - the "Shapefile download" section in each of the guides at <a href="https://switch2osm.org"></a><a href="https://switch2osm.org">https://switch2osm.org</a> has changed recently to matches the changes in OSM Carto itself. I'd rerun the steps from there downwards, keeping an eye on any errors displayed on screen.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '20, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-75450" class="comments-container">
&#10;</div>
<div id="comment-tools-75450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75450-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75454"></span>

<div id="answer-container-75454" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75454-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Figured out what I was doing wrong. if I use --create on the osm2pgsql and dont rerun the scripts/get-shapefiles.py it will not be in the database. that got me past the earlier error.</p>
<p>now I have this renderd[215378]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: COALESCE types text and integer cannot be matched LINE 15: ORDER BY COALESCE(layer,0) ^ in executeQuery Full sql was: 'SELECT * FROM (SELECT way, waterway, name, CASE WHEN tags-&gt;'intermittent' IN ('yes') OR tags-&gt;'seasonal' IN ('yes', 'spring', 'summer', 'autumn', 'winter', 'wet_season', 'dry_season') THEN 'yes' ELSE 'no' END AS int_intermittent, CASE WHEN tunnel IN ('yes', 'culvert') OR waterway = 'canal' AND tunnel = 'flooded' THEN 'yes' ELSE 'no' END AS int_tunnel, 'no' AS bridge FROM planet_osm_line WHERE waterway IN ('river', 'canal', 'stream', 'drain', 'ditch') AND (bridge IS NULL OR bridge NOT IN ('yes', 'aqueduct')) ORDER BY COALESCE(layer,0) ) AS water_lines LIMIT 0' encountered during parsing of layer 'water-lines' in Layer at line 7054 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml'</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '20, 04:04</strong></p>
<img src="https://secure.gravatar.com/avatar/cbea797cf56fb87a893b11776614d836?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trent&#39;s gravatar image" />
<p><span>Trent</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trent has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75454" class="comments-container">
&#10;</div>
<div id="comment-tools-75454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75456"></span>

<div id="answer-container-75456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75456-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you miss to include the style file in your osm2pgsql call?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '20, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-75456" class="comments-container">
&#10;</div>
<div id="comment-tools-75456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75456-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75458"></span>

<div id="answer-container-75458" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75458-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As @Spekerooger pointed out I forgot my style file on import. Thank everyone Solved if you forget your style file expect the following</p>
<p>renderd[215378]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: COALESCE types text and integer cannot be matched LINE 15: ORDER BY COALESCE(layer,0) ^ in executeQuery Full sql was: 'SELECT * FROM (SELECT way, waterway, name, CASE WHEN tags-&gt;'intermittent' IN ('yes') OR tags-&gt;'seasonal' IN ('yes', 'spring', 'summer', 'autumn', 'winter', 'wet_season', 'dry_season') THEN 'yes' ELSE 'no' END AS int_intermittent, CASE WHEN tunnel IN ('yes', 'culvert') OR waterway = 'canal' AND tunnel = 'flooded' THEN 'yes' ELSE 'no' END AS int_tunnel, 'no' AS bridge FROM planet_osm_line WHERE waterway IN ('river', 'canal', 'stream', 'drain', 'ditch') AND (bridge IS NULL OR bridge NOT IN ('yes', 'aqueduct')) ORDER BY COALESCE(layer,0) ) AS water_lines LIMIT 0'</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '20, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/cbea797cf56fb87a893b11776614d836?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trent&#39;s gravatar image" />
<p><span>Trent</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trent has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75458" class="comments-container">
&#10;</div>
<div id="comment-tools-75458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75458-form-container" class="comment-form-container">
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

