+++
type = "question"
title = "[closed] Markers not displayed in xhtml"
description = '''Hello, I just started working with OpenLayers because I want to include a map on my JSF page (.xhtml files). I want to use the same feature that is demonstrated in this example: http://openlayers.org/dev/examples/styles-context.html I played with the code a little bit in the html example files that ...'''
date = "2012-05-10T14:57:00Z"
lastmod = "2012-05-10T14:57:00Z"
weight = 12658
keywords = [ "marker", "xhtml", "openlayers" ]
aliases = [ "/questions/12658" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Markers not displayed in xhtml](/questions/12658/markers-not-displayed-in-xhtml)

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
<span id="post-12658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12658-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I just started working with OpenLayers because I want to include a map on my JSF page (.xhtml files). I want to use the same feature that is demonstrated in this example: <a href="http://openlayers.org/dev/examples/styles-context.html">http://openlayers.org/dev/examples/styles-context.html</a></p>
<p>I played with the code a little bit in the html example files that come with the .zip download.</p>
<p>When I copied the code into my JSF .xhtml page, the map appears but the markers are not displayed. Here is the example code:</p>
<pre><code>&lt;script type=&quot;text/javascript&quot;&gt;
//&lt;![CDATA[
var map;
function init(){
 map = new OpenLayers.Map(&#39;map&#39;, {maxResolution:&#39;auto&#39;});
var wms = new OpenLayers.Layer.WMS.InlineXhtml( &quot;OpenLayers WMS&quot;,
 &quot;http://vmap0.tiles.osgeo.org/wms/vmap0&quot;, {layers: &#39;basic&#39;, format: &#39;image/svg+xml&#39;} );
 map.addLayer(wms);
&#10;// create 50 random features in the northern hemisphere
 // give them a &quot;type&quot; attribute that will be used to style
// them by size
var features = new Array(50);
            for (var i=0; i&lt;features.length; i++) {
 features[i] = new OpenLayers.Feature.Vector(
new OpenLayers.Geometry.Point(
                        (360 * Math.random()) - 180, 90 * Math.random()
), {
 type: 5 + parseInt(5 * Math.random())
}
);
 }
&#10; // allow testing of specific renderers via &quot;?renderer=Canvas&quot;, etc
 var renderer = OpenLayers.Util.getParameters(window.location.href).renderer;
 renderer = (renderer) ? [renderer] : OpenLayers.Layer.Vector.prototype.renderers;
&#10;            // create the layer styleMap with a simple symbolizer template
yer1 = new OpenLayers.Layer.Vector(&#39;Points&#39;, {
styleMap: new OpenLayers.StyleMap({
pointRadius: &quot;${type}&quot;, // based on feature.attributes.type
 fillColor: &quot;#000000&quot;
 }),
 renderers: renderer
});
layer1.addFeatures(features);
&#10; map.addLayers([layer1]);
map.zoomToExtent(layer1.getDataExtent());
 }
//]]&gt;
 &lt;/script&gt;</code></pre>
<p>I added:</p>
<pre><code>map.zoomToExtent(layer1.getDataExtent());</code></pre>
<p>and changed the markers from 50 random to 2 markers of the coordinates of London and Berlin. And the map was centered exactly to show them, but the markers are still not displayed. But that proves that the markers are read and loaded to the map correctly, just not displayed. If I do the same back in the example .html page the map is again centered properly and the markers are displayed.</p>
<p>Is it the problem of xhtml? How to fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-xhtml" rel="tag" title="see questions tagged &#39;xhtml&#39;">xhtml</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '12, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/96eef35222da3d02a2bd5fe9e66548bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srd_pl&#39;s gravatar image" />
<p><span>srd_pl</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srd_pl has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>10 May '12, 15:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-12658" class="comments-container">
&#10;</div>
<div id="comment-tools-12658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12658-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This is not an OpenLayers support forum. Your Question is not OpenStreetMap related. Please see http://openlayers.org/ for OpenLayers mailing lists and support." by Frederik Ramm 10 May '12, 15:19

</div>

</div>

</div>

