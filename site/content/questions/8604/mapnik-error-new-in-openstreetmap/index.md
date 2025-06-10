+++
type = "question"
title = "mapnik error. New in OpenStreetMap"
description = '''Hi,  I&#x27;m new using OpenStreetMap and I can&#x27;t obtein a render map :( I downloaded only my country: spain.osm  I&#x27;m working on Windows System and mi configuration es: PostgresSQL + PosGIS + osmosis  Using osmosis I have be able to import de spain.osm into the data base.  Looking in the wiki for how to ...'''
date = "2011-10-23T20:16:00Z"
lastmod = "2011-10-24T07:15:00Z"
weight = 8604
keywords = [ "mapnik" ]
aliases = [ "/questions/8604" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik error. New in OpenStreetMap](/questions/8604/mapnik-error-new-in-openstreetmap)

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
<span id="post-8604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8604-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm new using OpenStreetMap and I can't obtein a render map :(</p>
<p>I downloaded only my country: spain.osm I'm working on Windows System and mi configuration es:</p>
<pre><code>PostgresSQL + PosGIS + osmosis
&#10;Using osmosis I have be able to import de spain.osm into the data base.
&#10;Looking in the wiki for how to configure the Mapnik for render I am using the python solution using xml file.</code></pre>
<p>;** part of the xml file</p>
<pre><code>&lt;Datasource&gt;
  &lt;Parameter name=&quot;type&quot;&gt;postgis&lt;/Parameter&gt;
  &lt;Parameter name=&quot;host&quot;&gt;localhost&lt;/Parameter&gt;
  &lt;Parameter name=&quot;dbname&quot;&gt;osm&lt;/Parameter&gt;
  &lt;Parameter name=&quot;user&quot;&gt;postgres&lt;/Parameter&gt;
  &lt;Parameter name=&quot;password&quot;&gt;admin&lt;/Parameter&gt;
  &lt;Parameter name=&quot;table&quot;&gt;(select ST_Buffer(ST_Centroid(geometry),2) as geometry, name  from world_worldborders) as world&lt;/Parameter&gt;
  &lt;Parameter name=&quot;extimate_extent&quot;&gt;false&lt;/Parameter&gt;
  &lt;Parameter name=&quot;extent&quot;&gt;-180,-90,180,89.99&lt;/Parameter&gt;
&lt;/Datasource&gt;</code></pre>
<p>;***</p>
<p>test python file ;<strong>*</strong></p>
<pre><code>from mapnik import *
&#10;mapfile = &#39;test2.xml&#39;
map_output = &#39;mymap.png&#39;
m = Map(4*1024,4*1024)
load_map(m, mapfile)
&#10;bbox=(Envelope( 36.4817,-6.245,36.4518,-6.1443 ))
&#10;m.zoom_to_box(bbox)
print &quot;Scale = &quot; , m.scale()
render_to_file(m, map_output)</code></pre>
<p>;<strong>*</strong>*</p>
<p>When I launch the script I have the issue that world_worldborders table are not in the data base</p>
<p>Searching for the wiki I found that we need to incorporated in the tables the shp files: - 10m-populated-place - 110m-admin-0-boundary-lines - processed_p - shoreline_300 - world_boundaries-spherical</p>
<p>After insert then using the "PostGIS shapefile and DBF loader", I launch again the python script and I have the following error on the screen:</p>
<p>"not relationship for world_worldborders"</p>
<p>What do I need to do for making work this?</p>
<p>Thanks in advance, Manolo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '11, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f3c6eaf7ba6b7517081b485c274d52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manolo%20quijano&#39;s gravatar image" />
<p><span>manolo quijano</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manolo quijano has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8604" class="comments-container">
&#10;</div>
<div id="comment-tools-8604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8604-form-container" class="comment-form-container">
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

<span id="8605"></span>

<div id="answer-container-8605" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8605-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to render with mapnik, you have to use osm2pgsql to import osm data. This program does some preprocessing on multipolygons and route relations, and it creates the database fields in the way mapnik expects then.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '11, 07:15</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-8605" class="comments-container">
&#10;</div>
<div id="comment-tools-8605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8605-form-container" class="comment-form-container">
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

