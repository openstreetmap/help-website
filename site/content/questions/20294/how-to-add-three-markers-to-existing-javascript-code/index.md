+++
type = "question"
title = "[closed] How to add three markers to existing javascript code"
description = '''Hi All I am new to this and need to complete an assignment, i am unable to add three additional markers into this code, i found the below info but it still doesnt help me. //ADD LAYER MARKERS var markers = new OpenLayers.Layer.Markers( &quot;Markers&quot; );  map.addLayer(markers);  markers.addMarker(new Open...'''
date = "2013-02-26T07:48:00Z"
lastmod = "2013-02-26T08:03:00Z"
weight = 20294
keywords = [ "javascript", "multiple", "markers" ]
aliases = [ "/questions/20294" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to add three markers to existing javascript code](/questions/20294/how-to-add-three-markers-to-existing-javascript-code)

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
<span id="post-20294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20294-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All</p>
<p>I am new to this and need to complete an assignment, i am unable to add three additional markers into this code, i found the below info but it still doesnt help me.</p>
<p><strong>//ADD LAYER MARKERS var markers = new OpenLayers.Layer.Markers( "Markers" ); map.addLayer(markers); markers.addMarker(new OpenLayers.Marker(lonLat,icon));</strong></p>
<p>Below is the code, i have tried to copy "var lonLat = new OpenLayers.LonLat( 13.0 ,47.0 ) //define a new location with these coordinates in WGS84" with new lat lon 13.1, 47.8 but that doesnt work.</p>
<p>WHAT AM I DOING WRONG, PLEASE HELP ME ....</p>
<pre><code> &lt;!-- COPYRIGHT: http://wiki.openstreetmap.org --&gt;
    &lt;html&gt;
    &lt;head&gt;
    &lt;title&gt;OpenLayers Demo&lt;/title&gt;
    &lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
    &lt;script&gt;
    function init() {
    map = new OpenLayers.Map(&quot;mapdiv&quot;); //create a new map
    var mapnik = new OpenLayers.Layer.OSM(); //add an OpenStreetMap layer to have some data in the mapview
    map.addLayer(mapnik); //add the OSM layer to the map
    var vectorLayer = new OpenLayers.Layer.Vector // Overlay new line
    var feature = new OpenLayers.Feature.Vector // new line
    var markers = new OpenLayers.Layer.Markers( &quot;Markers&quot; ); //add a layer where markers can be put
    map.addLayer(markers); //add the markers layer to the current map
    var lonLat = new OpenLayers.LonLat( 13.0 ,47.0 ) //define a new location with these coordinates in WGS84
    .transform( //transform the location to the coordinate system of our OpenLayers map
    new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
    map.getProjectionObject() // to Spherical Mercator Projection
    );
    markers.addMarker(new OpenLayers.Marker(lonLat, icon)); //add the newly created marker to the markers layer
    map.setCenter(lonLat, 13); // Use maker to center the map above and set zoom level to 15
    }
    &lt;/script&gt;
    &lt;/head&gt;
    &lt;body onload=&quot;init();&quot;&gt;
    &lt;div style=&quot;width: 100%; height: 100%;&quot; id=&quot;mapdiv&quot;&gt;&lt;/div&gt;
    ---Here I describe how I solved the assignment---
    &lt;/body&gt;
    &lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '13, 07:48</strong></p>
<img src="https://secure.gravatar.com/avatar/7e06a6562801673bf4a3e3fe43c208b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lizzy7&#39;s gravatar image" />
<p><span>Lizzy7</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lizzy7 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>26 Feb '13, 08:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-20294" class="comments-container">
&#10;</div>
<div id="comment-tools-20294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20294-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 26 Feb '13, 08:04

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20296"></span>

<div id="answer-container-20296" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20296-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not an OpenLayers support forum. See www.openlayers.org for help on OpenLayers. There's a multi-marker example here: <a href="http://openlayers.org/dev/examples/markers.html">http://openlayers.org/dev/examples/markers.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '13, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20296" class="comments-container">
&#10;</div>
<div id="comment-tools-20296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20296-form-container" class="comment-form-container">
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

