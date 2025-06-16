+++
type = "question"
title = "[closed] Add a custom marker - issues, need an example"
description = '''Hi I have a couple of issues: I am trying to add my own marker to a map, but it does not seem to work. Also when I try to refer the OpenLayer.js file locally the default red marker disappears. I have found some examples on the net, but they have been unsuccessful I am afraid. So I thought to ask for...'''
date = "2013-05-24T14:11:00Z"
lastmod = "2013-05-24T15:05:00Z"
weight = 22724
keywords = [ "marker", "gis", "osm" ]
aliases = [ "/questions/22724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Add a custom marker - issues, need an example](/questions/22724/add-a-custom-marker-issues-need-an-example)

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
<span id="post-22724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22724-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I have a couple of issues:</p>
<p>I am trying to add my own marker to a map, but it does not seem to work. Also when I try to refer the OpenLayer.js file locally the default red marker disappears.</p>
<p>I have found some examples on the net, but they have been unsuccessful I am afraid. So I thought to ask for some help here.</p>
<p>Now my code looks like this:</p>
<pre><code>&lt;div id=&quot;Map&quot; style=&quot;height: 250px; width: 400px&quot; &gt;&lt;/div&gt;
&lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
&lt;!--&lt;script src=&quot;js/osm/api/OpenLayers.js&quot;&gt;&lt;/script&gt;--&gt;
&lt;script&gt;
    var lat = 55.676098;
    var lon = 12.568337;
    var zoom = 11;
&#10;    var fromProjection = new OpenLayers.Projection(&quot;EPSG:4326&quot;);   // Transform from WGS 1984
    var toProjection = new OpenLayers.Projection(&quot;EPSG:900913&quot;); // to Spherical Mercator Projection
    var position = new OpenLayers.LonLat(lon, lat).transform(fromProjection, toProjection);
&#10;    map = new OpenLayers.Map(&quot;Map&quot;);
    var mapnik = new OpenLayers.Layer.OSM();
    map.addLayer(mapnik);
&#10;    var markers = new OpenLayers.Layer.Markers(&quot;Markers&quot;);//(&quot;Images/Icons/map-marker.png&quot;);
    map.addLayer(markers);
    markers.addMarker(new OpenLayers.Marker(position));
&#10;    map.setCenter(position, zoom);
&lt;/script&gt;</code></pre>
<p>and as you can see I have tried to refer to my own marker from 'Images/Icons/map-marker.png' without any luck.</p>
<p>Also you can see that I have tried to use a local copy of the 'OpenLayers.js', I don't know whether I should have it locally or always refer to 'www.openlayers.org', I believe referring local is good enough?</p>
<p>Also as I wrote earlier, if I refer the local .js file, the red marker, the zoom buttons and the OSM link disappears.</p>
<p>Can anyone help me out?</p>
<p>I have tried to follow the guidelines below, but unsuccesful. <a href="https://wiki.openstreetmap.org/wiki/Marker_API">https://wiki.openstreetmap.org/wiki/Marker_API</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '13, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a36ba7a39bc0d985dde8e60eb0cf884a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zorroguy&#39;s gravatar image" />
<p><span>zorroguy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zorroguy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>24 May '13, 14:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-22724" class="comments-container">
<span id="22728"></span>
<div id="comment-22728" class="comment">
<div id="post-22728-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, but seen aside from the openlayers part. Can I get some help here with setting custom marks on my openstreetmap, without openlayers? I am rather new in this, and I would like to learn and master OSM.</p>
</div>
<div id="comment-22728-info" class="comment-info">
<span class="comment-age">(24 May '13, 15:05)</span> <span class="comment-user userinfo">zorroguy</span>
</div>
</div>
</div>
<div id="comment-tools-22724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22724-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 24 May '13, 14:29

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22726"></span>

<div id="answer-container-22726" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22726-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your problem is an OpenLayers problem, not an OpenStreetMap problem. Check the documentation/mailing lists linked on www.openlayers.org for OpenLayers help.</p>
<p>The documentation you mention at the end of your post is not related to OpenLayers, it uses a different library named KHtml and is therefore not relevant to your problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '13, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22726" class="comments-container">
&#10;</div>
<div id="comment-tools-22726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22726-form-container" class="comment-form-container">
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

