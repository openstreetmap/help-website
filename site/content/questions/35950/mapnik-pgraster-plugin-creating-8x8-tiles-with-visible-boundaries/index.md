+++
type = "question"
title = "Mapnik PGRaster Plugin creating 8x8 tiles with visible boundaries"
description = '''I have used the latest addition to Mapnik PGRaster plugin (https://github.com/mapnik/mapnik/tree/2.3.x) by Strk(https://github.com/strk/mapnik/tree/2.3.x-pgraster) and merged recently I am able to get the images properly projected on the Map. But the images are tiled into 8x8 manner and I could see ...'''
date = "2014-08-18T10:00:00Z"
lastmod = "2014-08-18T10:00:00Z"
weight = 35950
keywords = [ "raster", "renderd", "osm", "mapnik", "mod_tile" ]
aliases = [ "/questions/35950" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik PGRaster Plugin creating 8x8 tiles with visible boundaries](/questions/35950/mapnik-pgraster-plugin-creating-8x8-tiles-with-visible-boundaries)

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
<span id="post-35950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35950-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have used the latest addition to Mapnik PGRaster plugin (<a href="https://github.com/mapnik/mapnik/tree/2.3.x)">https://github.com/mapnik/mapnik/tree/2.3.x)</a> by Strk(<a href="https://github.com/strk/mapnik/tree/2.3.x-pgraster)">https://github.com/strk/mapnik/tree/2.3.x-pgraster)</a> and merged recently</p>
<p>I am able to get the images properly projected on the Map. But the images are tiled into 8x8 manner and I could see the boundaries of the images at certain zoom levels.</p>
<p>The boundaries are between the 8x8 tiles I suppose and the apparent feeling of the map is like they are stitched together (Having to explain in this manner since I am not able to upload an Image)</p>
<p>I am using OSM, Mapnik(2.3.x branch), ModTile and Renderd.</p>
<p>Also, when I run renderd, I am getting logs like,</p>
<p>renderd[15011]: Rendering projected coordinates 14 4896 6056 -&gt; -8061966.247298|5205055.878110 -8042398.368057|5224623.757351 to a 8 x 8 tile</p>
<p>I have added a layer via layer-shapefile xml as follows,</p>
<pre><code>&lt;Layer name=&quot;MS-GIS&quot; status=&quot;on&quot; srs=&quot;+proj=utm +zone=18 +datum=WGS84 +units=m +no_defs&quot;&gt;
    &lt;StyleName&gt;raster&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;type&quot;&gt;pgraster&lt;/Parameter&gt;
      &lt;Parameter name=&quot;table&quot;&gt;ms_test&lt;/Parameter&gt;
      &lt;Parameter name=&quot;raster_field&quot;&gt;rast&lt;/Parameter&gt;
      &lt;Parameter name=&quot;dbname&quot;&gt;gis&lt;/Parameter&gt;
      &lt;Parameter name=&quot;estimate_extent&quot;&gt;false&lt;/Parameter&gt;
      &lt;Parameter name=&quot;extent&quot;&gt;-20037508,-19929239,20037508,19929239&lt;/Parameter&gt;
    &lt;/Datasource&gt;
&lt;/Layer&gt;</code></pre>
<p>How can get the tiling to be smooth without boundaries? Any help greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-raster" rel="tag" title="see questions tagged &#39;raster&#39;">raster</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '14, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f33507c19871e0c1dff92d4e5a2bdffb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aditya&#39;s gravatar image" />
<p><span>Aditya</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aditya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '14, 10:15</strong> </span></p>
</div>
</div>
<div id="comments-container-35950" class="comments-container">
&#10;</div>
<div id="comment-tools-35950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35950-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

