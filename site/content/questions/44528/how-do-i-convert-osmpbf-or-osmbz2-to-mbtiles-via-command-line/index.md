+++
type = "question"
title = "How do I convert .osm.pbf or .osm.bz2 to .mbtiles via command line"
description = '''How do I convert .osm.pbf or .osm.bz2 http://download.geofabrik.de/africa-latest.osm.bz2. to Geo .tiff via commandline? I want is end results to convert files to .mbtiles. If I have Geo .tiff I can convert using Gdal to .mbtiles easily. This is the response I got from the guys at geofabrik.de.  This...'''
date = "2015-07-30T03:43:00Z"
lastmod = "2021-08-19T19:47:00Z"
weight = 44528
keywords = [ "openstreetmap", "tilemill", "osm", "gdal", "mbtiles" ]
aliases = [ "/questions/44528" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I convert .osm.pbf or .osm.bz2 to .mbtiles via command line](/questions/44528/how-do-i-convert-osmpbf-or-osmbz2-to-mbtiles-via-command-line)

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
<span id="post-44528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44528-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-44528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I convert .osm.pbf or .osm.bz2 <a href="http://download.geofabrik.de/africa-latest.osm.bz2.">http://download.geofabrik.de/africa-latest.osm.bz2.</a> to Geo .tiff via commandline? I want is end results to convert files to .mbtiles. If I have Geo .tiff I can convert using Gdal to .mbtiles easily. This is the response I got from the guys at geofabrik.de.</p>
<pre><code> This is not so easy. You will want to have different zoom levels
 generated, so it is better to go osm-&gt;mbtiles directly without GDAL and
 GeoTiff. However, osm-&gt;mbtiles requires map rendering and style
 information. If it is for a small area, you can probably use Maperitive
 for this (unsure if it has a command line). Otherwise you will need to
 import OSM data into a PostGIS database, and then you can use e.g.
 Tilemill to batch-process</code></pre>
<p>(Credits Frederik Ramm)</p>
<p>Can someone translate this? How do I import OSM data into PostGIS database. Reference: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">https://wiki.openstreetmap.org/wiki/Osm2pgsql</a></p>
<pre><code>osm2pgsql -s -U postgres -d nameofdatabase /file/path/toosm/fileorpbf/name.osm</code></pre>
<p>Will this work for .OSM.PBF?</p>
<p>How do I use a Tilemill to do a batch process? What is the commandline arguments?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-gdal" rel="tag" title="see questions tagged &#39;gdal&#39;">gdal</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '15, 03:43</strong></p>
<img src="https://secure.gravatar.com/avatar/614e3e56882743b78234c816965f4040?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chathu&#39;s gravatar image" />
<p><span>Chathu</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chathu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44528" class="comments-container">
&#10;</div>
<div id="comment-tools-44528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44528-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="44537"></span>

<div id="answer-container-44537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44537-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Frederick / woodpeck points out this is not easy and contains multiple steps:</p>
<ol>
<li>rendering OSM geodata to rasterdata</li>
<li>converting map rasterdata to mbtiles</li>
</ol>
<p>I'm not familar if Tilemill/<a href="https://www.mapbox.com/mapbox-studio/#linux">Mapbox studio</a> can handle both steps. But this platform runs completely online and without any CLI preprocessing.</p>
<p>Usually you pick an <a href="https://wiki.openstreetmap.org/wiki/Rendering#Popular">desktop renderer</a> as Maperitive (or the full <a href="https://switch2osm.org/serving-tiles/">OSM rendering stack</a>) and convert the resulting tiles structure to <a href="https://wiki.openstreetmap.org/wiki/MBTiles">MBtiles</a> (no idea which tool to use).<br />
Anyway, you should start with an pretty small area! An whole continent doesn't sound like a good idea for usual hardware!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '15, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-44537" class="comments-container">
&#10;</div>
<div id="comment-tools-44537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44537-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44538"></span>

<div id="answer-container-44538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44538-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best guide to setting up osm2pgsql etc. is probably the <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">switch2osm</a> guide. You can point TileMill at the database that you set up using those instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '15, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44538" class="comments-container">
<span id="44555"></span>
<div id="comment-44555" class="comment">
<div id="post-44555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@Someoneelse</a> can you let me know how to point TileMill to this database?</p>
</div>
<div id="comment-44555-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 02:56)</span> <span class="comment-user userinfo">Chathu</span>
</div>
</div>
<span id="44597"></span>
<div id="comment-44597" class="comment">
<div id="post-44597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mapbox's "use TileMill with a database" instructions are here:</p>
<p><a href="https://www.mapbox.com/tilemill/docs/guides/postgis-work/">https://www.mapbox.com/tilemill/docs/guides/postgis-work/</a></p>
<p>But that's probably only needed if you're setting up a TileMill project from scratch. If you're using an existing stylesheet and your database is called "gis" I'd imagine things will "just work" as far as database access is concerned</p>
</div>
<div id="comment-44597-info" class="comment-info">
<span class="comment-age">(03 Aug '15, 17:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44538-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81372"></span>

<div id="answer-container-81372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can create MBTiles from any .osm.pbf file using this tool - <a href="https://github.com/systemed/tilemaker">https://github.com/systemed/tilemaker</a></p>
<ol>
<li><p>Download .osm.pbf file from <a href="https://download.geofabrik.de/">Geofabric</a>. To download for a custom area, you can use <a href="https://protomaps.com/extracts">Protomaps</a> or <a href="https://extract.bbbike.org/">BBBike Extract</a></p></li>
<li><p>Download <a href="https://github.com/systemed/tilemaker/releases">tilemaker</a></p></li>
<li><p>Execute the following command</p></li>
</ol>
<p><code>tilemaker --input netherlands.osm.pbf --output netherlands.mbtiles --process resources/process-openmaptiles.lua --config resources/config-openmaptiles.json</code></p>
<p>You can read more about it in this blog post - <a href="https://blog.kleunen.nl/blog/tilemaker-generate-map">https://blog.kleunen.nl/blog/tilemaker-generate-map</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '21, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/79e65eed0a4d543a7229550d59f0e309?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protos29&#39;s gravatar image" />
<p><span>protos29</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protos29 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81372" class="comments-container">
&#10;</div>
<div id="comment-tools-81372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81372-form-container" class="comment-form-container">
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

