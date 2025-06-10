+++
type = "question"
title = "Rendering blank tiles on Raspberry Pi Setup"
description = '''Currently I&#x27;m trying to build a very basic map server running on a Raspberry Pi (Archlinux). I&#x27;ve installed Mapnik and can render a png image using this simple python script: #!/usr/bin/env python import mapnik stylesheet = &#x27;world_style.xml&#x27; image = &#x27;world_style.png&#x27; m = mapnik.Map(2*1024, 2*1024) m...'''
date = "2014-11-01T05:48:00Z"
lastmod = "2014-11-01T05:48:00Z"
weight = 38209
keywords = [ "renderd", "mapnik", "raspberry", "arm_cpu" ]
aliases = [ "/questions/38209" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering blank tiles on Raspberry Pi Setup](/questions/38209/rendering-blank-tiles-on-raspberry-pi-setup)

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
<span id="post-38209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38209-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Currently I'm trying to build a very basic map server running on a Raspberry Pi (Archlinux). I've installed Mapnik and can render a png image using this simple python script:</p>
<pre><code>#!/usr/bin/env python
import mapnik
stylesheet = &#39;world_style.xml&#39;
image = &#39;world_style.png&#39;
m = mapnik.Map(2*1024, 2*1024)
mapnik.load_map(m, stylesheet)
m.zoom_all()
mapnik.render_to_file(m, image)
print &quot;rendered image to &#39;%s&#39;&quot; % image</code></pre>
<p>Using this style XML:</p>
<p>&lt;map background-color="#ffeaea" srs="+proj=latlong +datum=WGS84 +no_defs"&gt;</p>
<pre><code>&lt;Style name=&quot;My Style&quot;&gt;
  &lt;Rule&gt;
    &lt;PolygonSymbolizer fill=&quot;#eaeaff&quot; /&gt;
    &lt;LineSymbolizer stroke=&quot;rgb(25%,25%,25%)&quot; stroke-width=&quot;1.0&quot; /&gt;
  &lt;/Rule&gt;
&lt;/Style&gt;
&#10;&lt;Layer name=&quot;world&quot; srs=&quot;+proj=latlong +datum=WGS84 +no_defs&quot;&gt;
  &lt;StyleName&gt;My Style&lt;/StyleName&gt;
  &lt;Datasource&gt;
    &lt;Parameter name=&quot;type&quot;&gt;shape&lt;/Parameter&gt;
    &lt;Parameter name=&quot;file&quot;&gt;/home/pi/world/MyEurope.shp&lt;/Parameter&gt;
    &lt;Parameter name=&quot;extents&quot;&gt;-180,-90,180,90&lt;/Parameter&gt;
  &lt;/Datasource&gt;
&lt;/Layer&gt;</code></pre>
<p>&lt;/map&gt;</p>
<p>I got the shapefile from <a href="http://my5cent.spdns.de/en/beaglebone-black-raspberry-pi/einfacher-karten-server-mit-mapserver-schape-files-und-openlayers.html">http://my5cent.spdns.de/en/beaglebone-black-raspberry-pi/einfacher-karten-server-mit-mapserver-schape-files-und-openlayers.html</a> (Look for the 2nd section where a link to Europe SHP is shown)</p>
<p>Unfortunately, all I get when trying to load the map, either using leaflet or openlayers is empty.</p>
<p>Renderd seems to be working, and this is a sample of the logs shown:</p>
<pre><code>renderd[2756]: DEBUG: START TILE default 7 64-71 56-63, new metatile
renderd[2756]: Rendering projected coordinates 7 64 56 -&gt; 0.000000|0.000000 2504688.542850|2504688.542850 to a 8 x 8 tile
renderd[2756]: DEBUG: DONE TILE default 6 32-39 24-31 in 19.404 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/6/0/0/0/33/8.meta
&#10;renderd[2756]: DEBUG: START TILE default 7 64-71 64-71, new metatile
renderd[2756]: Rendering projected coordinates 7 64 64 -&gt; 0.000000|-2504688.542850 2504688.542850|0.000000 to a 8 x 8 tile
renderd[2756]: DEBUG: DONE TILE default 7 56-63 64-71 in 17.699 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/7/0/0/0/52/128.meta
&#10;renderd[2756]: DEBUG: Sending render cmd(3 default 7/63/64) with protocol version 2 to fd 7
renderd[2756]: DEBUG: Failed to read cmd on fd 7
renderd[2756]: DEBUG: Connection 0, fd 7 closed, now 5 left
renderd[2756]: DEBUG: Sending render cmd(3 default 7/62/64) with protocol version 2 to fd 11
renderd[2756]: DEBUG: Failed to read cmd on fd 11
renderd[2756]: DEBUG: Connection 4, fd 11 closed, now 4 left
renderd[2756]: DEBUG: Got incoming connection, fd 7, number 5
renderd[2756]: DEBUG: Got incoming connection, fd 11, number 6
renderd[2756]: DEBUG: Got incoming request with protocol version 2
renderd[2756]: DEBUG: Got command RenderPrio fd(7) xml(default), z(7), x(65), y(63), mime(image/png), options()
renderd[2756]: DEBUG: Got incoming request with protocol version 2
renderd[2756]: DEBUG: Got command RenderPrio fd(11) xml(default), z(7), x(65), y(64), mime(image/png), options()
renderd[2756]: DEBUG: DONE TILE default 7 56-63 56-63 in 17.540 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/7/0/0/0/51/136.meta
&#10;renderd[2756]: DEBUG: Sending render cmd(3 default 7/63/63) with protocol version 2 to fd 8
renderd[2756]: DEBUG: Failed to read cmd on fd 8
renderd[2756]: DEBUG: Connection 0, fd 8 closed, now 5 left
renderd[2756]: DEBUG: Sending render cmd(3 default 7/62/63) with protocol version 2 to fd 9
renderd[2756]: DEBUG: Failed to read cmd on fd 9
renderd[2756]: DEBUG: Connection 2, fd 9 closed, now 4 left
renderd[2756]: DEBUG: Got incoming connection, fd 8, number 5
renderd[2756]: DEBUG: Got incoming request with protocol version 2
renderd[2756]: DEBUG: Got command RenderPrio fd(8) xml(default), z(7), x(64), y(62), mime(image/png), options()
renderd[2756]: DEBUG: Got incoming connection, fd 9, number 6
renderd[2756]: DEBUG: Got incoming request with protocol version 2
renderd[2756]: DEBUG: Got command RenderPrio fd(9) xml(default), z(7), x(65), y(62), mime(image/png), options()
renderd[2756]: DEBUG: DONE TILE default 7 64-71 56-63 in 11.791 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/7/0/0/0/67/8.meta</code></pre>
<p>I've tried a lot of guides out there but nothing seems to work. I've even tried changing the style xml file so that the data source used is postgres (previously importing the shp to a database and trying by rendering with the python script), with no success.</p>
<p>What am I doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-raspberry" rel="tag" title="see questions tagged &#39;raspberry&#39;">raspberry</span> <span class="post-tag tag-link-arm_cpu" rel="tag" title="see questions tagged &#39;arm_cpu&#39;">arm_cpu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '14, 05:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0b3f17cc300b593d40619c5c695f111e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfgomez86&#39;s gravatar image" />
<p><span>jfgomez86</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfgomez86 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 00:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38209" class="comments-container">
&#10;</div>
<div id="comment-tools-38209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

