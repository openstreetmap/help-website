+++
type = "question"
title = "Vector layer disappears when switching to OSM layer..."
description = '''In the following code if I use the WMS layer my polygons (the geos variable) are displayed properly. If I switch to the OSM layer the OSM layer displays just fine, but the vector layer disappears from the map (despite being in the layers collection. Any ideas? var options = {  projection: &quot;EPSG:4326...'''
date = "2012-03-01T04:09:00Z"
lastmod = "2012-03-01T04:09:00Z"
weight = 10891
keywords = [ "wms", "osm", "vector", "openlayers" ]
aliases = [ "/questions/10891" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Vector layer disappears when switching to OSM layer...](/questions/10891/vector-layer-disappears-when-switching-to-osm-layer)

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
<span id="post-10891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10891-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the following code if I use the WMS layer my polygons (the geos variable) are displayed properly. If I switch to the OSM layer the OSM layer displays just fine, but the vector layer disappears from the map (despite being in the layers collection. Any ideas?</p>
<pre><code>var options = {
                projection: &quot;EPSG:4326&quot;,
                displayProjection: &quot;EPSG:4326&quot;,
                numZoomLevels: 20
            };
            that.map = new OpenLayers.Map(&#39;map&#39;, options);
//            that.layer = new OpenLayers.Layer.WMS(&quot;OpenLayers WMS&quot;,
//                &quot;http://vmap0.tiles.osgeo.org/wms/vmap0&quot;,
//                { layers: &#39;basic&#39; });
&#10;            that.layer = new OpenLayers.Layer.OSM({ opacity: 50 });
&#10;            var featurecollection = {
                &quot;type&quot;: &quot;FeatureCollection&quot;,
                &quot;features&quot;: [
                    { &quot;geometry&quot;: {
                        &quot;type&quot;: &quot;GeometryCollection&quot;,
                        &quot;geometries&quot;: geos
                    },
                        &quot;type&quot;: &quot;Feature&quot;,
                        &quot;properties&quot;: {}
                    }
                ]
            };
&#10;            var geojson_format = new OpenLayers.Format.GeoJSON();            
            var vector_layer = new OpenLayers.Layer.Vector();
&#10;            that.map.addLayers([vector_layer, that.layer]);
&#10;            vector_layer.events.register(&quot;featureadded&quot;, that.map.layers[1], that.zoomToLeftHalf);
            vector_layer.addFeatures(geojson_format.read(featurecollection));</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '12, 04:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4063cd31f7de485431927b28f82828c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coreyperkins&#39;s gravatar image" />
<p><span>coreyperkins</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coreyperkins has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '12, 17:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-10891" class="comments-container">
&#10;</div>
<div id="comment-tools-10891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10891-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

