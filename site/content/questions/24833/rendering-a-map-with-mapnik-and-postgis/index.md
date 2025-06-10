+++
type = "question"
title = "Rendering a map with Mapnik and PostGIS"
description = '''I’m trying to render a map using Mapnik and PostGIS, I feel I’m close but it doesn’t work yet. Here is what I’ve done so far (it’s the first time I work with a database, so it’s likely that there are stupid mistakes due to the fact that I don’t know how databases work). I’m working in Arch Linux wit...'''
date = "2013-08-02T12:37:00Z"
lastmod = "2014-11-01T10:09:00Z"
weight = 24833
keywords = [ "rendering", "postgis", "mapnik" ]
aliases = [ "/questions/24833" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering a map with Mapnik and PostGIS](/questions/24833/rendering-a-map-with-mapnik-and-postgis)

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
<span id="post-24833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24833-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I’m trying to render a map using Mapnik and PostGIS, I feel I’m close but it doesn’t work yet. Here is what I’ve done so far (it’s the first time I work with a database, so it’s likely that there are stupid mistakes due to the fact that I don’t know how databases work).</p>
<p>I’m working in Arch Linux with Mapnik 2.2.0, PostgreSQL 9.2.4, PostGIS 2.0.3 and osm2pgsql-git 20130512.</p>
<p>I downloaded the montpellier.osm.pbf file from <a href="http://metro.teczno.com/#montpellier">http://metro.teczno.com/#montpellier</a> (I didn’t download any coastline file, for now I’m just trying to render some part in the middle of a city). I created a database with PostGIS enabled and imported the pbf file (using osm2pgsql), using various instructions on the Wiki. I don’t fully understand the various usernames needed for a PostgreSQL database, but I think the main PostgreSQL username is "postgres" and the other username (not sure what this one is for) is my Unix login ("fractal"). Anyway, the import seems to have done something (it took something like an hour to complete) and I have the following:</p>
<pre><code>$ psql --username=postgres --dbname=osm --command=&quot;\d+&quot;
                           List of relations
 Schema |        Name        | Type  |  Owner   |  Size   | Description 
--------+--------------------+-------+----------+---------+-------------
 public | geography_columns  | view  | postgres | 0 bytes | 
 public | geometry_columns   | view  | postgres | 0 bytes | 
 public | planet_osm_line    | table | postgres | 32 kB   | 
 public | planet_osm_nodes   | table | postgres | 104 kB  | 
 public | planet_osm_point   | table | postgres | 24 kB   | 
 public | planet_osm_polygon | table | postgres | 24 kB   | 
 public | planet_osm_rels    | table | postgres | 2184 kB | 
 public | planet_osm_roads   | table | postgres | 16 kB   | 
 public | planet_osm_ways    | table | postgres | 141 MB  | 
 public | spatial_ref_sys    | table | postgres | 3216 kB | 
(10 rows)</code></pre>
<p>So it seems that the database has been populated with stuff.</p>
<p>Then I tried to adapt the tutorial at <a href="http://wiki.openstreetmap.org/wiki/Mapnik:_Rendering_OSM_XML_data_directly">http://wiki.openstreetmap.org/wiki/Mapnik:_Rendering_OSM_XML_data_directly</a>. I downloaded the style file there, made it compatible with Mapnik 2, changed various details, and tried to change the datasource from XML to PostGIS. What I have now is the following (in the file test.xml):</p>
<p><a href="http://pastebin.archlinux.fr/467464">http://pastebin.archlinux.fr/467464</a></p>
<p>(I looked at the OSM style files to see what kind of parameters are needed for postgis)</p>
<p>Then I have the following Python script (adapted from the other tutorial):</p>
<pre><code>!/usr/bin/env python2
&#10;from mapnik import *
&#10;mapfile = &#39;test.xml&#39;
map_output = &#39;mymap.png&#39;
&#10;m = Map(4*1024,4*1024)
load_map(m, mapfile)
bbox=(Envelope( 3.873,43.603,3.878,43.606 ))
&#10;m.zoom_to_box(bbox)
print &quot;Scale = &quot; , m.scale()
render_to_file(m, map_output)</code></pre>
<p>(the bounding box is supposed to be a place with several roads)</p>
<p>When I run the script, there are no error and the mymap.png file is created, but it’s completely yellow (the background color in the style file) with no road. Maybe that’s because there is a problem with the connection to the database, but I don’t know how to fix it. I also tried with planet_osm_line instead of planet_osm_roads (I’m not sure where the highways are supposed to be) but it’s the same, and I tried with planet_osm_ways but it failed with the error:</p>
<pre><code>RuntimeError: PostGIS: geometry name lookup failed for table &#39;planet_osm_ways&#39;. Please manually provide the &#39;geometry_field&#39; parameter or add an entry in the geometry_columns for &#39;planet_osm_ways&#39;.</code></pre>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '13, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/579b240041b084d221aaf999e0de2929?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fractal&#39;s gravatar image" />
<p><span>Fractal</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fractal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24833" class="comments-container">
&#10;</div>
<div id="comment-tools-24833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24833-form-container" class="comment-form-container">
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

<span id="24849"></span>

<div id="answer-container-24849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24849-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't try to use the approach described in <a href="http://wiki.openstreetmap.org/wiki/Mapnik:_Rendering_OSM_XML_data_directly">http://wiki.openstreetmap.org/wiki/Mapnik:_Rendering_OSM_XML_data_directly</a> . It reads the OSM XML file directly using a broken, unsupported and likely-to-be-removed input plugin for Mapnik. The first steps, where you use osm2pgsql to load the OSM data into postgresql, are the correct steps.</p>
<p>When you have the data loaded in your database, there are two general approaches.</p>
<p>1) Use command-line tools. <a href="http://code.google.com/p/mapnik-utils/wiki/Nik2Img">nik2img.py</a> is the swiss army knife of command-line mapnik image generation, and is basically a fully-working version of the script you'd start writing yourself. You need a stylesheet to go with it, and I'd suggest <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a>.</p>
<p>2) Use a graphical interface. Tilemill is the best approach. When you have that installed, you can either create your own stylesheet and add your layers from postgis, or use a pre-created stylesheet. I'd again suggest <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a> or <a href="https://github.com/mapbox/osm-bright">osm-bright</a>, which are both Tilemill-compatible stylesheets for OSM data which has been loaded into postgis.</p>
<p>But overall, avoid the osm input plugin and anything related to it - it's a dead-end!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '13, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-24849" class="comments-container">
&#10;</div>
<div id="comment-tools-24849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24849-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24845"></span>

<div id="answer-container-24845" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24845-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>planet_osm_ways is a table without geometry so the error is not a surprise. planet_osm_line should work for your purpose. Your error is probably that your import has generated a database with projected coordinates, but in your script you're requesting an unprojected area. Compare your script to <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/generate_image.py">http://svn.openstreetmap.org/applications/rendering/mapnik/generate_image.py</a> and make sure to reproject your coordinates before using m.zoom_to_box like it is done there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '13, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24845" class="comments-container">
&#10;</div>
<div id="comment-tools-24845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24845-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38219"></span>

<div id="answer-container-38219" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38219-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-38219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a detailed description on <a href="http://sourceforge.net/projects/topomapcreator/">TopoMapCreator</a> about <a href="http://sourceforge.net/p/topomapcreator/wiki/TileMill">How to render OSM data with TileMill on Windows</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/6c696b469aba99282f03a4a1f33528b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaki007&#39;s gravatar image" />
<p><span class="suspended-user">kaki007</span><br />
(suspended)<br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaki007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38219" class="comments-container">
&#10;</div>
<div id="comment-tools-38219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38219-form-container" class="comment-form-container">
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

