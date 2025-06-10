+++
type = "question"
title = "Load OSM tiles using URL in custom QGIS application (C++)"
description = '''I am trying to write a C++ version of a custom QGIS (v 3.10) application I initially wrote in Python that overlays data onto OpenStreetMap. I am able to do this successfully by loading online tiles via URL as a raster layer in Python using WMS provider; however the same URL does not work when using ...'''
date = "2021-04-06T15:45:00Z"
lastmod = "2021-04-07T08:32:00Z"
weight = 79549
keywords = [ "qgis", "url", "tiles", "osm", "c++" ]
aliases = [ "/questions/79549" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Load OSM tiles using URL in custom QGIS application (C++)](/questions/79549/load-osm-tiles-using-url-in-custom-qgis-application-c)

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
<span id="post-79549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to write a C++ version of a custom QGIS (v 3.10) application I initially wrote in Python that overlays data onto OpenStreetMap. I am able to do this successfully by loading online tiles via URL as a raster layer in Python using WMS provider; however the same URL does not work when using the C++ API, despite being able to load other raster files (e.g. GeoTIFF).</p>
<p>Code in Python:</p>
<pre><code>url = &#39;type=xyz&amp;url=https://a.tile.openstreetmap.org&#39;
url += &#39;/%7Bz%7D/%7Bx%7D/%7By%7D.png&amp;zmax=19&amp;zmin=0&amp;crs=EPSG3857&#39;
prj = QgsProject()
qmc = QgsMapCanvas()
layers = []
ras = QgsRasterLayer(url,&#39;OpenStreetMap&#39;,&#39;wms&#39;)
&#10;if ras.isValid():
    print(&quot;Basemap loaded successfully!&quot;)
    prj.instance().addMapLayer(ras)
    qmc.setExtent(ras.extent())
    layers.append(ras)
    qmc.setLayers(layers)
&#10; else:
     print(&quot;Unable to load basemap.&quot;)</code></pre>
<p>C++ version:</p>
<pre><code>QString url = &quot;type=xyz&amp;url=https://a.tile.openstreetmap.org&quot;;
url.append(&quot;/%7Bz%7D/%7Bx%7D/%7By%7D.png&amp;zmax=19&amp;zmin=0&amp;crs=EPSG3857&quot;);
QgsProject() *prj = new QgsProject();
QgsMapCanvas *qmc = new QgsMapCanvas();
QList &lt;QgsMapLayer *&gt; layers;
QgsRasterLayer *ras = new QgsRasterLayer(url,&#39;OpenStreetMap&#39;,&#39;wms&#39;);
&#10;if ( ras.isValid() )
{
    qDebug() &lt;&lt; &quot;Basemap loaded successfully!&quot;;
    prj-&gt;instance()-&gt;addMapLayer(ras);
    qmc-&gt;setExtent(ras-&gt;extent());
    layers.append(ras);
    qmc-&gt;setLayers(layers);
 } else
{
     qDebug() &lt;&lt; &quot;Unable to load basemap.&quot;;
 }</code></pre>
<p>(Note: the layer list takes QgsMapLayer pointers in C++ but couldn't escape the vectors using &amp;lt/&amp;gt). I get the successful message and loaded map in Python and the invalid message and no map in C++. I have tried using other URL's but nothing has worked thus far. If there are plugins available that might help, but I would still need to write workable code without the use of the QGIS gui itself (as in most examples using plugins).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '21, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/4e8b9c3c62c5f7dd127898fd67c04828?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raisehellpraisedale&#39;s gravatar image" />
<p><span>raisehellpra...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raisehellpraisedale has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79549" class="comments-container">
<span id="79558"></span>
<div id="comment-79558" class="comment">
<div id="post-79558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/393139/loading-online-osm-raster-tiles-using-url-in-custom-qgis-application-c">https://gis.stackexchange.com/questions/393139/loading-online-osm-raster-tiles-using-url-in-custom-qgis-application-c</a></p>
</div>
<div id="comment-79558-info" class="comment-info">
<span class="comment-age">(07 Apr '21, 08:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79549-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

