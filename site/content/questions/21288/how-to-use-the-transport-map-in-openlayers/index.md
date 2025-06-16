+++
type = "question"
title = "How to use the Transport map in OpenLayers"
description = '''I&#x27;m new to OpenStreetMap and OpenLayers and want my map to resemble the Transport Map on the OpenStreetMap website. My init() function looks like this: function init() {  map = new OpenLayers.Map(&quot;map&quot;);  var mapnik = new OpenLayers.Layer.OSM();  map.addLayer(mapnik);  var fromProjection = new OpenL...'''
date = "2013-04-07T13:18:00Z"
lastmod = "2013-04-08T19:20:00Z"
weight = 21288
keywords = [ "map", "openlayers", "transport" ]
aliases = [ "/questions/21288" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use the Transport map in OpenLayers](/questions/21288/how-to-use-the-transport-map-in-openlayers)

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
<span id="post-21288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21288-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OpenStreetMap and OpenLayers and want my map to resemble the Transport Map on the OpenStreetMap website.</p>
<p>My init() function looks like this: <code>function init() { map = new OpenLayers.Map("map"); var mapnik = new OpenLayers.Layer.OSM(); map.addLayer(mapnik); var fromProjection = new OpenLayers.Projection("EPSG:4326"); // Transform from WGS 1984 var toProjection = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection var position = new OpenLayers.LonLat(-1.83, 52.60).transform(fromProjection, toProjection); var zoom = 7; map.setCenter(position, zoom); }</code></p>
<p>My map currently looks like the Standard one. Does the OpenLayers.Layer.OSM() constructor take any parameters?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-transport" rel="tag" title="see questions tagged &#39;transport&#39;">transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '13, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c7b32e47325a06e10f86f724d4f5dee2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="id94&#39;s gravatar image" />
<p><span>id94</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="id94 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '13, 15:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21288" class="comments-container">
&#10;</div>
<div id="comment-tools-21288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21288-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="21329"></span>

<div id="answer-container-21329" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21329-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this</p>
<pre><code>function init() {
        map = new OpenLayers.Map(&quot;map&quot;);
        map.addControl(new OpenLayers.Control.LayerSwitcher());
        var mapnik = new OpenLayers.Layer.OSM();
        map.addLayer(mapnik);
        var transportmap = new  OpenLayers.Layer.OSM.TransportMap(&quot;OpenTransportMap&quot;); //defined here https://www.openstreetmap.org/openlayers/OpenStreetMap.js
        map.addLayer(transportmap);
        var fromProjection = new OpenLayers.Projection(&quot;EPSG:4326&quot;);   // Transform from WGS 1984
        var toProjection = new OpenLayers.Projection(&quot;EPSG:900913&quot;); // to Spherical Mercator Projection
        var position = new OpenLayers.LonLat(-1.83, 52.60).transform(fromProjection, toProjection);
        var zoom = 7;
        map.setCenter(position, zoom);
    }</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '13, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-21329" class="comments-container">
&#10;</div>
<div id="comment-tools-21329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21329-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21297"></span>

<div id="answer-container-21297" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21297-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've figured it out. I used WireShark to watch what my browser was doing while using the Transport Map and I can see the following HTTP headers being sent:</p>
<pre><code>GET /transport/16/35668/20346.png HTTP/1.1
Host: b.tile2.opencyclemap.org
...</code></pre>
<p>Looks like it using a tile server hosted by opencyclemap.org.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '13, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c7b32e47325a06e10f86f724d4f5dee2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="id94&#39;s gravatar image" />
<p><span>id94</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="id94 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21297" class="comments-container">
<span id="21300"></span>
<div id="comment-21300" class="comment">
<div id="post-21300-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please make sure that you abide by the <a href="http://www.thunderforest.com/terms/">terms and conditions</a> under which these tiles are offered!</p>
</div>
<div id="comment-21300-info" class="comment-info">
<span class="comment-age">(07 Apr '13, 21:18)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="21310"></span>
<div id="comment-21310" class="comment">
<div id="post-21310-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the link to Thunderforest and the Ts &amp; Cs. Doh! I've only just noticed the attribution at the bottom of the Transport map to Andy Allan and opencyclemap.org so perhaps my super-sleuthing was unnecessary!</p>
</div>
<div id="comment-21310-info" class="comment-info">
<span class="comment-age">(08 Apr '13, 09:56)</span> <span class="comment-user userinfo">id94</span>
</div>
</div>
</div>
<div id="comment-tools-21297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21297-form-container" class="comment-form-container">
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

