+++
type = "question"
title = "points all going to (0,0)"
description = '''I am building an openstreetmap with some geometry points, using this example, and using the OpenLayers.mobile.js. map = new OpenLayers.Map({  div: &quot;mapdiv&quot;,  theme: null,  projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),  displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;),  maxExtent: ne...'''
date = "2013-01-30T16:27:00Z"
lastmod = "2013-08-27T10:02:00Z"
weight = 19463
keywords = [ "development", "vector", "openlayers", "points" ]
aliases = [ "/questions/19463" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [points all going to (0,0)](/questions/19463/points-all-going-to-00)

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
<span id="post-19463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19463-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building an openstreetmap with some geometry points, using <a href="https://github.com/jumpinjackie/rhok-spatialtruth/blob/master/js/OpenLayers-2.12/examples/vector-features.html">this example</a>, and using the OpenLayers.mobile.js.</p>
<pre><code>map = new OpenLayers.Map({
    div: &quot;mapdiv&quot;,
    theme: null,
    projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
    displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;),
    maxExtent: new OpenLayers.Bounds(-20037508.34,-20037508.34,20037508.34,20037508.34),
    maxResolution: 156543.0399,
    numZoomLevels: 19,
    units: &#39;m&#39;,
    controls: [
         new OpenLayers.Control.Attribution(),
         new OpenLayers.Control.TouchNavigation({
                dragPanOptions: {
                    enableKinetic: true
                }
         }),
         new OpenLayers.Control.Zoom()
    ]
});
&#10;map.addLayer(new OpenLayers.Layer.OSM());
map.zoomToMaxExtent();
var style = OpenLayers.Util.extend({}, OpenLayers.Feature.Vector.style[&#39;default&#39;]);
style.graphicWidth = 30;
style.graphicHeight = 32;
&#10;style.externalGraphic = &quot;img/point.png&quot;;
&#10;var mapmarkers = new OpenLayers.Layer.Vector( &quot;Markers&quot;);
&#10;var features = [];
var points = [];
&#10;map.addLayer(mapmarkers);
for (var i = markers.length - 1; i &gt;= 0; i--) {
    points[i] = new OpenLayers.Geometry.Point( markers[i].latlng[0], markers[i].latlng[1] );
    features[i] = new OpenLayers.Feature.Vector( points[i], null, style);
}
mapmarkers.addFeatures(features);
map.setCenter(new OpenLayers.LonLat(points[0].x, points[0].y), 5);</code></pre>
<p>I'm getting the correct number of points on the map, but they are sitting at a lat/lang of 0,0. The only difference between the <code>features</code> variable I'm sending to <code>addFeatures</code> .. <code>features.geometry</code> is that it has a bounds object with top/bottom/right/left equivalent to the x and y that isn't present in the example..</p>
<p>If I use the example's <code>map.addLayer(new OpenLayers.Layer.WMS( "OpenLayers WMS", "http://vmap0.tiles.osgeo.org/wms/vmap0", {layers: 'basic'} ));</code> both points get placed but they are in Antarctica instead of Quebec (at least in different places then)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '13, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e95cce1d08ec6482987231fda024c414?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thedamon&#39;s gravatar image" />
<p><span>thedamon</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thedamon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>26 Aug '13, 10:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-19463" class="comments-container">
<span id="25815"></span>
<div id="comment-25815" class="comment">
<div id="post-25815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You will have better chances of getting an answer if you rephrase this as an actual question.</p>
</div>
<div id="comment-25815-info" class="comment-info">
<span class="comment-age">(26 Aug '13, 14:56)</span> <span class="comment-user userinfo">MagicFab</span>
</div>
</div>
</div>
<div id="comment-tools-19463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19463-form-container" class="comment-form-container">
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

<span id="25843"></span>

<div id="answer-container-25843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is with different map projections. Probably you'll have to project your latLon points (which are in WGS84 / EPSG:4326) to Web Mercartor (EPSG:900913) by using something like the projection example from OpenLayers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '13, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-25843" class="comments-container">
&#10;</div>
<div id="comment-tools-25843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25843-form-container" class="comment-form-container">
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

