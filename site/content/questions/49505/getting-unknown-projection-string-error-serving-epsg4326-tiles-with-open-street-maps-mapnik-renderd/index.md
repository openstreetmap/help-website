+++
type = "question"
title = "getting &quot;Unknown projection string error&quot; serving EPSG:4326 tiles with open street maps mapnik renderd"
description = '''The goal: I am attempting to generate map tiles with EPSG:4326 instead of web mercator by specifying EPSG:4326 in the mapnik style file srs attributes  My current setup:  I am running Ubuntu 14.14 LTS and have followed the switch2osm.org manually-building-a-tile-server-14-04 instructions. Using the ...'''
date = "2016-04-29T19:49:00Z"
lastmod = "2023-06-30T09:55:00Z"
weight = 49505
keywords = [ "renderd", "projection", "mapnik" ]
aliases = [ "/questions/49505" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [getting "Unknown projection string error" serving EPSG:4326 tiles with open street maps mapnik renderd](/questions/49505/getting-unknown-projection-string-error-serving-epsg4326-tiles-with-open-street-maps-mapnik-renderd)

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
<span id="post-49505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49505-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<h2 id="the-goal">The goal:</h2>
<p>I am attempting to generate map tiles with EPSG:4326 instead of web mercator by specifying EPSG:4326 in the mapnik style file srs attributes</p>
<p><br />
My current setup:</p>
<hr />
<p>I am running Ubuntu 14.14 LTS and have followed the switch2osm.org manually-building-a-tile-server-14-04 instructions. Using the default projection, I was able to successfully import data and serve tiles to a client. I am using the stack of osm2pgsql, renderd, mapnik, mod_tile, apache, postgres, and the OSM Bright stylesheet.</p>
<p><strong>To import I used:</strong></p>
<pre><code>osm2pgsql --slim -d gis -C 16000 --number-processes 3 mapdata.osm.pbf</code></pre>
<p><strong>Then to run renderd:</strong></p>
<pre><code>sudo -u mapnik renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>At this point, I had everything working to serve up web mercator.</p>
<p><br />
Attempting to serve tiles in EPSG:4326:</p>
<hr />
<p><strong>First I reimported the data with osm2pgsql using the -l flag:</strong></p>
<pre><code>osm2pgsql  -l --slim -d gis -C 16000 --number-processes 3 mapdata.osm.pbf</code></pre>
<p>I then updated the mapnik stylesheet map and layer srs attributes to match what was defined in <a href="http://spatialreference.org/ref/epsg/4326/mapnik/">http://spatialreference.org/ref/epsg/4326/mapnik/</a></p>
<pre><code>srs=&quot;+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs&quot;</code></pre>
<p><strong>When starting renderd I will then receive the error:</strong></p>
<pre><code>&quot;Unknown projection string, using web mercator as never the less.
 +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs&quot;</code></pre>
<p><strong>I also attempted a few other options:</strong></p>
<pre><code>srs=&quot;+init=epsg:4326&quot;
&#10;srs=&quot;+proj=longlat +datum=WGS84 +no_defs&quot;</code></pre>
<p>After seeing a post recommending to check if proj-epsg package is installed, I was heading down the path that proj was missing on my system (<a href="https://github.com/mapnik/mapnik/wiki/InstallationTroubleshooting#proj_init_error)">https://github.com/mapnik/mapnik/wiki/InstallationTroubleshooting#proj_init_error)</a></p>
<p>Per this proj init error guide I reinstalled proj to no effect.</p>
<p>I confirmed I do have it:</p>
<pre><code>~$ proj
Rel. 4.8.0, 6 March 2012
usage: proj [ -beEfiIlormsStTvVwW [args] ] [ +opts[=arg] ] [ files ]</code></pre>
<p>I have checked my <strong>/usr/share/proj/epsg</strong> file and it contains an entry:</p>
<pre><code># WGS 84
&lt;4326&gt; +proj=longlat +datum=WGS84 +no_defs  &lt;&gt;</code></pre>
<p>The guide shows a different path to /usr/local/share/proj/epsg. On my system it is /usr/share/proj/epsg</p>
<p><br />
Questions:</p>
<hr />
<p><strong>Do I need to configure mapnik or renderd somehow to be able to use proj?</strong></p>
<p><strong>Is my proj epsg file in an atypical location?</strong></p>
<p><strong>Is there any other information that would be useful?</strong></p>
<p><strong>Also, are there any other methods I could attempt to use to get finer debugging?</strong></p>
<p><br />
Some of the configuration files:</p>
<hr />
<p><strong>renderd.conf:</strong></p>
<pre><code>[renderd]
socketname=/var/run/renderd/renderd.sock
num_threads=4
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;
[mapnik]
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/share/fonts/truetype/ttf-dejavu
font_dir_recurse=1
&#10;[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_tile
XML=/usr/local/share/maps/style/OSMBright/OSMBright.xml
HOST=localhost
TILESIZE=256</code></pre>
<p><strong>problem snippet EPSG:4326 version of mapnik OSMBright.xml:</strong></p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;!DOCTYPE Map[]&gt;
&lt;Map srs=&quot;+proj=longlat +datum=WGS84 +no_defs&quot; 
font-directory=&quot;./fonts&quot; background-color=&quot;#c4dff6&quot;
maximum-extent=&quot;-20037508.34,-20037508.34,20037508.34,20037508.34&quot;&gt;</code></pre>
<p><strong>working snippet web mercator version of mapnik OSMBright.xml:</strong></p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;!DOCTYPE Map[]&gt;
&lt;Map srs=&quot;+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over&quot; 
font-directory=&quot;./fonts&quot; background-color=&quot;#c4dff6&quot;
maximum-extent=&quot;-20037508.34,-20037508.34,20037508.34,20037508.34&quot;&gt;</code></pre>
<p>Thanks for any thoughts.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '16, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9a0311e6e866d542bed3d4aefdc0fd9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsitarski&#39;s gravatar image" />
<p><span>jsitarski</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsitarski has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-49505" class="comments-container">
<span id="87406"></span>
<div id="comment-87406" class="comment">
<div id="post-87406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am struggling with the same problem, and do not want to use MapProxy. Did you find a solution?</p>
</div>
<div id="comment-87406-info" class="comment-info">
<span class="comment-age">(30 Jun '23, 09:55)</span> <span class="comment-user userinfo">Kcok</span>
</div>
</div>
</div>
<div id="comment-tools-49505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49505-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

