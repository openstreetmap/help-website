+++
type = "question"
title = "[closed] Plot 200 points using open street map"
description = '''I am trying to plot 200 locations on map using open street map layer. I have stored all addresses in array. I am running the loop but my code doesn&#x27;t plot more than 9 locations on map. My code is: &amp;lt;body background-color=&quot;green&quot;&amp;gt;   &amp;lt;script&amp;gt;  map = new OpenLayers.Map(&#x27;mapdiv&#x27;); map.addLaye...'''
date = "2015-07-21T22:44:00Z"
lastmod = "2015-07-21T22:44:00Z"
weight = 44332
keywords = [ "openstreetmap", "openlayers" ]
aliases = [ "/questions/44332" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Plot 200 points using open street map](/questions/44332/plot-200-points-using-open-street-map)

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
<span id="post-44332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to plot 200 locations on map using open street map layer. I have stored all addresses in array. I am running the loop but my code doesn't plot more than 9 locations on map.</p>
<p>My code is:</p>
<p>&lt;body background-color="green"&gt;</p>
<div>
&#10;</div>
&lt;script&gt;
<pre><code>map = new OpenLayers.Map(&#39;mapdiv&#39;);
map.addLayer(new OpenLayers.Layer.OSM());
&#10;epsg4326 =  new OpenLayers.Projection(&#39;EPSG:4326&#39;); //WGS 1984 projection
projectTo = map.getProjectionObject();
&#10;var lonLat = new OpenLayers.LonLat( 90.417931,36.778259).transform(epsg4326, projectTo);
&#10;var zoom=4;
map.setCenter (lonLat, zoom);
&#10;var vectorLayer = new OpenLayers.Layer.Vector(&#39;Overlay&#39;);
&#10;var geocoder = new google.maps.Geocoder();</code></pre>
<p>var address = ['address1','address2'------'address200']; for (i = 0; i&lt; 200; i++) { geocoder.geocode( { 'address': address[i]}, function(results, status) {</p>
<p>if (status == google.maps.GeocoderStatus.OK) {</p>
<p>var feature = new OpenLayers.Feature.Vector( new OpenLayers.Geometry.Point( results[0].geometry.location.lng(),results[0].geometry.location.lat()).transform(epsg4326, projectTo),{description:'This is the value of<br />
the description attribute'} , {externalGraphic: 'http://leafletjs.com/dist/images/marker-icon-2x.png', graphicHeight: 25, graphicWidth: 21, graphicXOffset:-12,graphicYOffset:-25 } );</p>
<pre><code>vectorLayer.addFeatures(feature);
map.addLayer(vectorLayer);</code></pre>
<p>} }); } map.addLayer(vectorLayer);</p>
&lt;/script&gt;
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '15, 22:44</strong></p>
<img src="https://secure.gravatar.com/avatar/09bd09f31c49d237d773a26f0dc3b88d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashnav&#39;s gravatar image" />
<p><span>Ashnav</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashnav has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>21 Jul '15, 23:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-44332" class="comments-container">
&#10;</div>
<div id="comment-tools-44332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question seems to be about Google geo-coding with OpenLayers" by SK53 21 Jul '15, 23:52

</div>

</div>

</div>

