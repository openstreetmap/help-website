+++
type = "question"
title = "How can I select  a LineString with OpenLayer&#x27;s SelectFeture at any position of the line?"
description = '''Following problem: My base layer is a OpenLayers.Layer.OSM.Osmarender layer. I draw a line with OpenLayers.Geometry.LineString in a second vector layer. With the Openlayer SelectFeature I want to select this line. But this is only possible at the startpoint and the endpoint. Is this a bug in the ope...'''
date = "2012-01-06T08:20:00Z"
lastmod = "2012-01-06T08:20:00Z"
weight = 9823
keywords = [ "openlayers" ]
aliases = [ "/questions/9823" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I select a LineString with OpenLayer's SelectFeture at any position of the line?](/questions/9823/how-can-i-select-a-linestring-with-openlayers-selectfeture-at-any-position-of-the-line)

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
<span id="post-9823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9823-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-9823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Following problem: My base layer is a OpenLayers.Layer.OSM.Osmarender layer. I draw a line with OpenLayers.Geometry.LineString in a second vector layer. With the Openlayer SelectFeature I want to select this line. But this is only possible at the startpoint and the endpoint. Is this a bug in the openlayer source?</p>
<p>This is my example: Click on the blue thick line selects the line only at startpoint and endpoint.</p>
<pre><code>&lt;html&gt;
&lt;head&gt;
&lt;title&gt;OpenLayers Example&lt;/title&gt;
&lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;src=&quot;https://www.openstreetmap.org/openlayers/OpenStreetMap.js&quot;&gt;&lt;/script&gt;
&lt;/head&gt;
&#10;&lt;body&gt;
&lt;div style=&quot;width:100%; height:100%&quot; id=&quot;map&quot;&gt;&lt;/div&gt;
&lt;script defer=&quot;defer&quot; type=&quot;text/javascript&quot;&gt;
&#10;//create map
var options = {
            projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
    displayProjection: &#39;EPSG:4326&#39;,
    units: &quot;m&quot;,
    maxResolution: 156543.0339,
    maxExtent: new OpenLayers.Bounds(-20037508.34, -20037508.34,
                                      20037508.34, 20037508.34),
            controls: [new OpenLayers.Control.PanZoom(), 
                       new OpenLayers.Control.Navigation(),
                       new OpenLayers.Control.MousePosition({&quot;numDigits&quot;: 8,
                         displayProjection: new  OpenLayers.Projection(&quot;EPSG:4326&quot;),emptyString:&quot;outside the map&quot;}),
                       ]
  };        
map = new OpenLayers.Map(&#39;map&#39;, options);
&#10;// create OSM layer
osm_osma = new OpenLayers.Layer.OSM.Osmarender(&#39;OpenStreetMap Osmarender&#39;,
    {minZoomLevel: 0,
     maxZoomLevel: 100,
     isBaseLayer: true
    }
);
map.addLayers([osm_osma]);      
var lonlat=transformLonLat(&quot;8.3191929972096&quot;, &quot;49.015806343698&quot;, false);
map.setCenter(lonlat, 17);
&#10;//create vector-layer
// Layerstyle
var vlayer_style = OpenLayers.Util.extend({}, OpenLayers.Feature.Vector.style[&#39;default&#39;]);
vlayer_style.fillOpacity = 0.6;
vlayer_style.fillColor = &quot;green&quot;;
vlayer_style.strokeWidth = 6;
vlayer_style.strokeColor = &quot;blue&quot;;
vlayer_style.strokeOpacity = 1;
&#10;var select_style = OpenLayers.Util.extend({}, vlayer_style);
select_style.fillOpacity = 0.6;
select_style.strokeWidth = 10;
select_style.strokeColor = &quot;black&quot;;
select_style.fillColor = &quot;black&quot;;
vlayer_style.strokeOpacity = 1;
&#10;var vStyleMap = new OpenLayers.StyleMap( {
   &quot;default&quot; :vlayer_style,
   &quot;select&quot; :select_style
});
var vlayer = new OpenLayers.Layer.Vector(&quot;vlayer&quot;, {styleMap: vStyleMap});
map.addLayer(vlayer);
&#10;//create SelectFeatures
var selectControl=new OpenLayers.Control.SelectFeature(vlayer,{displayClass: &quot;selectButton&quot;, title: &#39;Select Ways&#39;, 
onSelect:selected, onUnselect:unselected,toggle:false,clickout:true,multiple:false,
hover:false,toggleKey:&quot;ctrlKey&quot;, multipleKey:&quot;shiftKey&quot;,geometryTypes: [&quot;OpenLayers.Geometry.LineString&quot;],
callbacks: {
    &#39;over&#39;: feature_hover,
    &#39;out&#39;: feature_hover_out
        }
  });
map.addControl(selectControl);
selectControl.activate();
&#10;//Draw Linestring
var waypoint_lon=&quot;8.3096336042805&quot;;
var waypoint_lat=&quot;49.016608500028&quot;;
var lonlat=transformLonLat(waypoint_lon, waypoint_lat, false);      
var point=new OpenLayers.Geometry.Point(lonlat.lon, lonlat.lat);
var arrPoint =[];
arrPoint.push(point);
&#10;waypoint_lon=&quot;8.3274863874837&quot;;
waypoint_lat=&quot;49.016249642214&quot;;
lonlat=transformLonLat(waypoint_lon, waypoint_lat, false);      
point=new OpenLayers.Geometry.Point(lonlat.lon, lonlat.lat);
arrPoint.push(point);
&#10;var line = new OpenLayers.Geometry.LineString(arrPoint);    
var lineF = new OpenLayers.Feature.Vector(line,null);
&#10;vlayer.addFeatures([lineF]);
&#10;//Functions
function transformLonLat(lon, lat, anzeige) {
var lonlat1 = null;
if (anzeige==true)
    lonlat1=new OpenLayers.LonLat(lon, lat).transform(
            new OpenLayers.Projection(&quot;EPSG:900913&quot;), // Spherical Mercator Projection
            new OpenLayers.Projection(&quot;EPSG:4326&quot;) // WGS 1984,
            );
else
    lonlat1=new OpenLayers.LonLat(lon, lat).transform(
            new OpenLayers.Projection(&quot;EPSG:4326&quot;), // WGS 1984,
            new OpenLayers.Projection(&quot;EPSG:900913&quot;) // Spherical Mercator Projection
            );
return lonlat1;
}
&#10;function feature_hover( feature ){ 
    feature.layer.div.style.cursor = &quot;crosshair&quot;;
}
&#10;function feature_hover_out( feature ){ 
    feature.layer.div.style.cursor = &quot;&quot;;
}
&#10;function selected (obj) {
    alert(&quot;select&quot;);
}
&#10;function unselected (obj) {  
    alert(&quot;deselect&quot;);
}
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '12, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a26097bd93d7cf1ca042a216198735c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stafy&#39;s gravatar image" />
<p><span>stafy</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stafy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9823" class="comments-container">
&#10;</div>
<div id="comment-tools-9823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9823-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

