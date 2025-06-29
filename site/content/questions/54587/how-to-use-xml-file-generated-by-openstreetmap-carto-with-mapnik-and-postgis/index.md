+++
type = "question"
title = "How to use .xml file generated by openstreetmap-carto with mapnik and postgis"
description = '''Hi, I&#x27;m struggling for 2 weeks now to render a map using mapnik, mapnik-python, postigs and carto. I&#x27;m able to render a map from a local .osm file and I&#x27;ve compiled and installed the latest mapnik library and python bidings. I&#x27;ve exported a .osm file to a local postgis DB using osm2pgsql and using Q...'''
date = "2017-02-10T12:11:00Z"
lastmod = "2017-02-13T15:12:00Z"
weight = 54587
keywords = [ "python", "openstreetmap", "carto", "mapnik", "postgis" ]
aliases = [ "/questions/54587" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use .xml file generated by openstreetmap-carto with mapnik and postgis](/questions/54587/how-to-use-xml-file-generated-by-openstreetmap-carto-with-mapnik-and-postgis)

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
<span id="post-54587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm struggling for 2 weeks now to render a map using mapnik, mapnik-python, postigs and carto. I'm able to render a map from a local .osm file and I've compiled and installed the latest mapnik library and python bidings.</p>
<p>I've exported a .osm file to a local postgis DB using osm2pgsql and using QGIS Browser (a windows postgis client) I can validate that the export was successful. In order to render a map from this DB I generated a .xml stylesheet using <code>carto -a "3.0.0" ../openstreetmap-carto/project.mml &gt; mapnik2.xml</code> and I modified project.mml and added my DB credentials like this:</p>
<pre><code>  osm2pgsql: &amp;osm2pgsql
  type: &quot;postgis&quot;
  dbname: &quot;gis&quot;
  port: &quot;5432&quot;
host: &quot;localhost&quot;
user: &quot;maps&quot;
password: &quot;asdfe&quot;
key_field: &quot;&quot;
geometry_field: &quot;way&quot;
extent: &quot;-20037508,-20037508,20037508,20037508&quot;</code></pre>
<p>I checked the generated mapnik2.xml file and all DB queries now have information about my DB credentials and it looks like this (snapshot from mapnik2.xml):</p>
<pre><code>&lt;/Style&gt;
&lt;Layer name=&quot;cliffs&quot;
maximum-scale-denominator=&quot;100000&quot;
srs=&quot;+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over&quot;&gt;
&lt;StyleName&gt;cliffs&lt;/StyleName&gt;
&lt;StyleName&gt;cliffs-man_made&lt;/StyleName&gt;
&lt;Datasource&gt;
&lt;Parameter name=&quot;type&quot;&gt;&lt;![CDATA[postgis]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;dbname&quot;&gt;&lt;![CDATA[gis]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;port&quot;&gt;&lt;![CDATA[5432]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;host&quot;&gt;&lt;![CDATA[localhost]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;user&quot;&gt;&lt;![CDATA[maps]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;password&quot;&gt;&lt;![CDATA[asdfe]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;key_field&quot;&gt;&lt;![CDATA[]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;geometry_field&quot;&gt;&lt;![CDATA[way]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;extent&quot;&gt;&lt;![CDATA[-20037508,-20037508,20037508,20037508]]&gt;&lt;/Parameter&gt;
&lt;Parameter name=&quot;table&quot;&gt;&lt;![CDATA[(SELECT
way, &quot;natural&quot;, man_made
FROM planet_osm_line
WHERE &quot;natural&quot; = &#39;cliff&#39; OR man_made = &#39;embankment&#39;
) AS cliffs]]&gt;&lt;/Parameter&gt;
&lt;/Datasource&gt;
&lt;/Layer&gt;</code></pre>
<p>This is the python script: #!/usr/bin/env python</p>
<pre><code>import mapnik
from mapnik import *
&#10;mapnik.logger.set_severity(mapnik.severity_type.Debug)
&#10;mapfile = &#39;mapnik2.xml&#39;
map_output = &#39;mymap33.png&#39;
&#10;m = Map(1024, 1024)
load_map(m, mapfile)
bbox=(Box2d(-6.5, 49.5, 2.1, 59))
&#10;m.zoom_to_box(bbox) 
render_to_file(m, map_output)</code></pre>
<p>The output image is always blank and I see no errors in the logs. I also tried to use nik4.py with the same result, blank image. Is this because mapnik can't connect to my local postgis DB? Did I miss a step ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '17, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/9a081afc9d2ea8fa735de1b5c393f1b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="biliuta&#39;s gravatar image" />
<p><span>biliuta</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="biliuta has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '17, 12:19</strong> </span></p>
</div>
</div>
<div id="comments-container-54587" class="comments-container">
<span id="54592"></span>
<div id="comment-54592" class="comment">
<div id="post-54592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Switch statement logging on for your PostgresQL server &amp; you can see if the statements are getting executed.</p>
</div>
<div id="comment-54592-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 14:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="54596"></span>
<div id="comment-54596" class="comment">
<div id="post-54596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've enabled the logs for postgresql and it seems the queries are executed with the correct user but the image is still blank.</p>
</div>
<div id="comment-54596-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 15:05)</span> <span class="comment-user userinfo">biliuta</span>
</div>
</div>
<span id="54618"></span>
<div id="comment-54618" class="comment">
<div id="post-54618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a way to see more detailed logs from mapnik library? I've compiled mapnik for debuging but I can't see any errors in the logs.</p>
<p>The logs look something like this and it repeats this pattern a lot of times (from mapnik lib when running python script):</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: Start processing style</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: End processing style</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: Start processing style</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: End processing style</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: End layer processing</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: Start processing layer=paths-text-name</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: -- datasource=0x2cae640</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: - query_extent=box2d(-6.9500000000000002,49.5000000000000000,2.5499999999999998,59.0000000000000000)</p>
<p>At the end of the log this is what it prints out:</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: agg_renderer: End map processing</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: stroker: Destroy stroker=0x3b87680</p>
<p>Mapnik LOG&gt; 2017-02-10 06:46:28: postgis_connection: postgresql connection closed - 0x2ccd430</p>
</div>
<div id="comment-54618-info" class="comment-info">
<span class="comment-age">(13 Feb '17, 09:05)</span> <span class="comment-user userinfo">biliuta</span>
</div>
</div>
<span id="54619"></span>
<div id="comment-54619" class="comment">
<div id="post-54619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also I have some doubts about the box that I'm trying to use in my python script:</p>
<p>bbox=(Box2d(-6.5, 49.5, 2.1, 59))</p>
<p>Can someone please explain a bit on how to use this Box2d and what parameters do I need to set? Maybe the params that I'm giving do not represent a zone of the map that I've exported to my postgisDB. I only exported the map of Bucharest not the entire world.</p>
</div>
<div id="comment-54619-info" class="comment-info">
<span class="comment-age">(13 Feb '17, 10:22)</span> <span class="comment-user userinfo">biliuta</span>
</div>
</div>
</div>
<div id="comment-tools-54587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54587-form-container" class="comment-form-container">
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

<span id="54621"></span>

<div id="answer-container-54621" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54621-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Frederik Ramm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I figured out the mistake. The map was exported in ESPG:4326 and I wasn't converting the box to this type of coordinates. I used mapnik.ProjTransform and now it works fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '17, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/9a081afc9d2ea8fa735de1b5c393f1b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="biliuta&#39;s gravatar image" />
<p><span>biliuta</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="biliuta has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-54621" class="comments-container">
&#10;</div>
<div id="comment-tools-54621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54621-form-container" class="comment-form-container">
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

