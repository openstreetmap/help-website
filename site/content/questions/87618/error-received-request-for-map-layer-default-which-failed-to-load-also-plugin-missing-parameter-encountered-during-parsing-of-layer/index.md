+++
type = "question"
title = "ERROR **: Received request for map layer &#x27;default&#x27; which failed to load .... also Plugin: missing  parameter  encountered during parsing of layer"
description = '''Following this tutorial: https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/ when trying to load the tiles using renderd, I get **ERROR **: Received request for map layer &#x27;default&#x27; which failed to load**  looking further into into it, I  ran: renderd -f -c /etc/ren...'''
date = "2023-08-06T20:29:00Z"
lastmod = "2023-08-07T01:11:00Z"
weight = 87618
keywords = [ "landcover", "switch2osm", "osm", "mapnik", "tileserver" ]
aliases = [ "/questions/87618" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ERROR \*\*: Received request for map layer 'default' which failed to load .... also Plugin: missing parameter encountered during parsing of layer](/questions/87618/error-received-request-for-map-layer-default-which-failed-to-load-also-plugin-missing-parameter-encountered-during-parsing-of-layer)

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
<span id="post-87618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87618-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Following this tutorial: <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a></p>
<p>when trying to load the tiles using renderd, I get</p>
<pre><code>**ERROR **: Received request for map layer &#39;default&#39; which failed to load**</code></pre>
<p>looking further into into it, I ran:</p>
<pre><code>renderd -f -c /etc/renderd.conf</code></pre>
<p>and obtained:</p>
<pre><code>**ERROR **: 14:57:30.531: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: missing &lt;table&gt; parameter  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 803 of &#39;/home/mapserver/src/openstreetmap-carto/style.xml&#39;**</code></pre>
<p>So I open the style.xml starting at line 803 and don't quite understand what the issue would be, here's what I get at line 803 of the style.xml file:</p>
<pre><code>line 803 --&gt;    &lt;Layer cache-features=&quot;true&quot; maximum-scale-denominator=&quot;25000000&quot; minimum-scale-denominator=&quot;750000&quot; name=&quot;landcover-low-zoom&quot; srs=&quot;+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over&quot;&gt;
        &lt;StyleName&gt;&lt;![CDATA[landcover-low-zoom-low-zoom]]&gt;&lt;/StyleName&gt;
        &lt;Datasource&gt;
          &lt;Parameter name=&quot;type&quot;&gt;&lt;![CDATA[postgis]]&gt;&lt;/Parameter&gt;
          &lt;Parameter name=&quot;dbname&quot;&gt;&lt;![CDATA[gis]]&gt;&lt;/Parameter&gt;
          &lt;Parameter name=&quot;key_field&quot;&gt;&lt;![CDATA[]]&gt;&lt;/Parameter&gt;
          &lt;Parameter name=&quot;geometry_field&quot;&gt;&lt;![CDATA[way]]&gt;&lt;/Parameter&gt;
          &lt;Parameter name=&quot;extent&quot;&gt;&lt;![CDATA[-20037508,-20037508,20037508,20037508]]&gt;&lt;/Parameter&gt;
          &lt;Parameter name=&quot;table&quot;&gt;&lt;![CDATA[(SELECT
        way, way_pixels,
        COALESCE(wetland, landuse, &quot;natural&quot;) AS feature
      FROM (SELECT
          way,
          (&#39;landuse_&#39; || (CASE WHEN landuse IN (&#39;forest&#39;, &#39;farmland&#39;, &#39;residential&#39;, &#39;commercial&#39;, &#39;retail&#39;, &#39;industrial&#39;,
                                                &#39;meadow&#39;, &#39;grass&#39;, &#39;village_green&#39;, &#39;vineyard&#39;, &#39;orchard&#39;) THEN landuse END)) AS landuse,
          (&#39;natural_&#39; || (CASE WHEN &quot;natural&quot; IN (&#39;wood&#39;, &#39;sand&#39;, &#39;scree&#39;, &#39;shingle&#39;, &#39;bare_rock&#39;, &#39;heath&#39;, &#39;grassland&#39;, &#39;scrub&#39;) THEN &quot;natural&quot; END)) AS &quot;natural&quot;,
      (&#39;wetland_&#39; || (CASE WHEN &quot;natural&quot; IN (&#39;wetland&#39;, &#39;mud&#39;) THEN (CASE WHEN &quot;natural&quot; IN (&#39;mud&#39;) THEN &quot;natural&quot; ELSE tags-&gt;&#39;wetland&#39; END) END)) AS wetland,
      way_area/NULLIF(POW(!scale_denominator!*0.001*0.28,2),0) AS way_pixels,
      way_area
    FROM planet_osm_polygon
    WHERE (landuse IN (&#39;forest&#39;, &#39;farmland&#39;, &#39;residential&#39;, &#39;commercial&#39;, &#39;retail&#39;, &#39;industrial&#39;, &#39;meadow&#39;, &#39;grass&#39;, &#39;village_green&#39;, &#39;vineyard&#39;, &#39;orchard&#39;)
      OR &quot;natural&quot; IN (&#39;wood&#39;, &#39;wetland&#39;, &#39;mud&#39;, &#39;sand&#39;, &#39;scree&#39;, &#39;shingle&#39;, &#39;bare_rock&#39;, &#39;heath&#39;, &#39;grassland&#39;, &#39;scrub&#39;))
      AND way_area &gt; 0.01*!pixel_width!::real*!pixel_height!::real
      AND building IS NULL
  ) AS features
  ORDER BY way_area DESC, feature
) AS landcover_low_zoom]]&gt;&lt;/Parameter&gt;
    &lt;/Datasource&gt;</code></pre>
<p>I'v debugged and I've looked everywhere online and can't find an answer that could guide me in the right direction.</p>
<p>Could anyone help?</p>
<p><img src="/upfiles/error_goKC3DZ.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landcover" rel="tag" title="see questions tagged &#39;landcover&#39;">landcover</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '23, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6e3fc3b81e63f6e12a3114840d482c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="compic&#39;s gravatar image" />
<p><span>compic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="compic has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '23, 20:48</strong> </span></p>
</div>
</div>
<div id="comments-container-87618" class="comments-container">
<span id="87619"></span>
<div id="comment-87619" class="comment">
<div id="post-87619-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That just means "it didn't work". If you can provide more details, such as messages from syslog people may be able to provide more help.</p>
</div>
<div id="comment-87619-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 20:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87620"></span>
<div id="comment-87620" class="comment">
<div id="post-87620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've updated my question.</p>
<p>All I get from syslog is:</p>
<p><strong>ERROR</strong> : Received request for map layer 'default' which failed to load**</p>
</div>
<div id="comment-87620-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 20:50)</span> <span class="comment-user userinfo">compic</span>
</div>
</div>
</div>
<div id="comment-tools-87618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87618-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="87621"></span>

<div id="answer-container-87621" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87621-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe the "postgis" part of the setup didn't work for some reason? I'd try doing that again and reloading.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '23, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87621" class="comments-container">
<span id="87622"></span>
<div id="comment-87622" class="comment">
<div id="post-87622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are you suggesting to delete the gis db and and set it all up and import the region?</p>
</div>
<div id="comment-87622-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 21:00)</span> <span class="comment-user userinfo">compic</span>
</div>
</div>
<span id="87623"></span>
<div id="comment-87623" class="comment">
<div id="post-87623-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm suggesting to add the postgis extension to it. You will need to import data again (just a small region first to check it works).</p>
</div>
<div id="comment-87623-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 21:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87626"></span>
<div id="comment-87626" class="comment">
<div id="post-87626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I followed the instructions again, and imported a smaller area, and still get the same error.</p>
<p>What I did, I deleted the gis db. And started following the instructions in <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a></p>
<p>from here: createdb -E UTF8 -O _renderd gis</p>
<p>I created also a new mapnik.xml and modified the renderd.conf file to point to that... and I'm still getting</p>
<p><strong>(process:112517): ERROR</strong> : 16:51:50.159: An error occurred while loading the map layer 'sav': Postgis Plugin: missing</p>
<p>parameter encountered during parsing of layer 'landcover-low-zoom' in Layer at line 803 of '/home/mapserver/src/openstreetmap-carto/mapnik.xml'</p>
<p>the only different is I had built mapnik instead of installing it from package. However, when I import it in python it all works.</p>
<p>Sorry to keep bugging you, but would you have any idea?</p>
<table>
</table>
</div>
<div id="comment-87626-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 21:57)</span> <span class="comment-user userinfo">compic</span>
</div>
</div>
<span id="87627"></span>
<div id="comment-87627" class="comment">
<div id="post-87627-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When you ran "CREATE EXTENSION postgis;" what did it say?</p>
<p>"map layer 'sav':" suggests you're using a different map layer (which should workproviding that you change all the references) or aomething has gone very wrong.</p>
</div>
<div id="comment-87627-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 22:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87628"></span>
<div id="comment-87628" class="comment">
<div id="post-87628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when I created the extension, it just returned (I can't quite remember) something along EXTENSION added/created.</p>
<p>This is my renderd.conf</p>
<pre><code>; BASIC AND SIMPLE CONFIGURATION:
&#10;[renderd]
stats_file=/var/run/renderd/renderd.stats
socketname=/var/run/renderd/renderd.sock
num_threads=10
tile_dir=/var/cache/renderd/tiles
&#10;[mapnik]
plugins_dir=/usr/local/lib/mapnik/input/
font_dir=/usr/share/fonts/truetype
font_dir_recurse=true
&#10;; ADD YOUR LAYERS:
[default]
URI=/utm_nav/
TILEDIR=/var/lib/mod_tile
XML=/home/mapserver/src/openstreetmap-carto/style.xml
HOST=localhost
TILESIZE=256
MINZOOM=0
MAXZOOM=20
&#10;[sav]
URI=/nav/
XML=/home/mapserver/src/openstreetmap-carto/mapnik.xml
HOST=localhost
TILESIZE=256
MINZOOM=0
MAXZOOM=20</code></pre>
</div>
<div id="comment-87628-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 22:42)</span> <span class="comment-user userinfo">compic</span>
</div>
</div>
</div>
<div id="comment-tools-87621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87621-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87629"></span>

<div id="answer-container-87629" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ok, finally! I fixed it. But I still don't know exactly what the problem is.</p>
<p>This line in the renderd.conf file: plugins_dir=/usr/local/lib/mapnik/input/</p>
<p>I changed it to plugins_dir=/usr/lib/mapnik/3.1/input</p>
<p>and it works.</p>
<p>But!, when I list what's in both folders, I pretty much have the same files:</p>
<h1 id="mapserver-mapserver-in-usrlocallibmapnikinput-180043">mapserver @ mapserver in /usr/local/lib/mapnik/input [18:00:43]</h1>
<pre><code>$ ls -la
total 92252
drwxr-xr-x 2 root root     4096 Nov  9  2022 .
drwxr-xr-x 4 root root     4096 Nov  9  2022 ..
-rwxrwxr-x 1 root root 24042072 Nov  9  2022 csv.input
-rwxrwxr-x 1 root root  1771688 Nov  9  2022 gdal.input
-rwxrwxr-x 1 root root  3425888 Nov  9  2022 geobuf.input
-rwxrwxr-x 1 root root 28465976 Nov  9  2022 geojson.input
-rwxrwxr-x 1 root root  2595000 Nov  9  2022 ogr.input
-rwxrwxr-x 1 root root  4517992 Nov  9  2022 pgraster.input
-rwxrwxr-x 1 root root  4037912 Nov  9  2022 postgis.input
-rwxrwxr-x 1 root root  2242328 Nov  9  2022 raster.input
-rwxrwxr-x 1 root root  3325256 Nov  9  2022 shape.input
-rwxrwxr-x 1 root root  3654488 Nov  9  2022 sqlite.input
-rwxrwxr-x 1 root root 16359328 Nov  9  2022 topojson.input</code></pre>
<h1 id="mapserver-mapserver-in-usrlibmapnik3.1input-180145">mapserver @ mapserver in /usr/lib/mapnik/3.1/input [18:01:45]</h1>
<pre><code>$ ls -la
total 2152
drwxr-xr-x 2 root root   4096 Dec  5  2022 .
drwxr-xr-x 3 root root   4096 Aug  9  2022 ..
-rwxr-xr-x 1 root root 460856 Aug  3  2022 csv.input
-rwxr-xr-x 1 root root  79904 Aug  3  2022 gdal.input
-rwxr-xr-x 1 root root 428072 Aug  3  2022 geojson.input
-rwxr-xr-x 1 root root 112672 Aug  3  2022 ogr.input
-rwxr-xr-x 1 root root 178216 Aug  3  2022 pgraster.input
-rwxr-xr-x 1 root root 215080 Aug  3  2022 postgis.input
-rwxr-xr-x 1 root root 133168 Aug  3  2022 raster.input
-rwxr-xr-x 1 root root 124976 Aug  3  2022 shape.input
-rwxr-xr-x 1 root root 145456 Aug  3  2022 sqlite.input
-rwxr-xr-x 1 root root 297000 Aug  3  2022 topojson.input</code></pre>
<p>so maybe the postgis plugin install in the /usr/local/... could be corrupted or not properly built (this is why I'm not sure what the problem is).</p>
<p>The big difference between the plugins are the size, so maybe I built mapnik with the wrong dependencies? I don't know.</p>
<p>However, I do appreciate your support in this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '23, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/6e3fc3b81e63f6e12a3114840d482c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="compic&#39;s gravatar image" />
<p><span>compic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="compic has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '23, 23:09</strong> </span></p>
</div>
</div>
<div id="comments-container-87629" class="comments-container">
<span id="87633"></span>
<div id="comment-87633" class="comment">
<div id="post-87633-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Actually, <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a> doesn't suggest building mapnik at all - it just suggests installing the one that comes out of the box with Ubuntu 22.04 LTS!</p>
</div>
<div id="comment-87633-info" class="comment-info">
<span class="comment-age">(07 Aug '23, 01:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87635"></span>
<div id="comment-87635" class="comment">
<div id="post-87635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's correct, thing is, I had mapnik installed from last year and I didn't want to uninstall it. So that was the issue.</p>
<p>Thanks again, I really do appreciate it.</p>
</div>
<div id="comment-87635-info" class="comment-info">
<span class="comment-age">(07 Aug '23, 01:11)</span> <span class="comment-user userinfo">compic</span>
</div>
</div>
</div>
<div id="comment-tools-87629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87629-form-container" class="comment-form-container">
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

