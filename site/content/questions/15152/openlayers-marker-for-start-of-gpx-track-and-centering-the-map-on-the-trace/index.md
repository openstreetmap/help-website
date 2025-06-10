+++
type = "question"
title = "Openlayers - marker for start of GPX track and centering the map on the trace"
description = '''Using the example http://wiki.openstreetmap.org/wiki/Openlayers_Track_example I can make a map with a GPX trace on it but I have to centre the map by finding the co-ordinates separately and assigning them to variables for lat lon, and getting the zoom level by trial and error.  I can also add a pin ...'''
date = "2012-08-16T15:59:00Z"
lastmod = "2017-10-09T13:57:00Z"
weight = 15152
keywords = [ "marker", "track", "gpx", "openlayers", "start" ]
aliases = [ "/questions/15152" ]
osqa_answers = 6
osqa_accepted = true
+++

<div class="headNormal">

# [Openlayers - marker for start of GPX track and centering the map on the trace](/questions/15152/openlayers-marker-for-start-of-gpx-track-and-centering-the-map-on-the-trace)

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
<span id="post-15152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using the example <a href="http://wiki.openstreetmap.org/wiki/Openlayers_Track_example">http://wiki.openstreetmap.org/wiki/Openlayers_Track_example</a> I can make a map with a GPX trace on it but I have to centre the map by finding the co-ordinates separately and assigning them to variables for lat lon, and getting the zoom level by trial and error. I can also add a pin to mark the start but again have to position it by manually entering the co-ordinates. It's entirely possible to use javascript to parse the GPX file to find the bounds of the trace, and the centre point. The start point is also simply the first trackpoint.</p>
<p>Does anyone have any idea how to do this? I'm capable of adapting examples but not of generating this complexity of scripting!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-start" rel="tag" title="see questions tagged &#39;start&#39;">start</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '12, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/e82dee06cd9f989e30bc1c57f2afc2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="digby&#39;s gravatar image" />
<p><span>digby</span><br />
<span class="score" title="46 reputation points">46</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="digby has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '12, 16:17</strong> </span></p>
</div>
</div>
<div id="comments-container-15152" class="comments-container">
&#10;</div>
<div id="comment-tools-15152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15152-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="15176"></span>

<div id="answer-container-15176" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15176-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="digby has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Although this question is more related to OpenLayers than OSM, you can try with this code:</p>
<blockquote>
<p>map.zoomToExtent(lgpx.getDataExtent());</p>
</blockquote>
<p>EDIT: this code add also the marker at the startpoint and should be placed after adding the layer lgpx to the map (map.addLayer(lgpx))</p>
<pre><code>lgpx.events.register(&quot;loadend&quot;, lgpx, function() {
  this.map.zoomToExtent(this.getDataExtent());
  var startPoint = this.features[0].geometry.components[0];
  layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(startPoint.x, startPoint.y),icon));
});</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '12, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '12, 11:27</strong> </span></p>
</div>
</div>
<div id="comments-container-15176" class="comments-container">
<span id="15191"></span>
<div id="comment-15191" class="comment">
<div id="post-15191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Am I asking in the wrong forum?</p>
</div>
<div id="comment-15191-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 08:23)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="15192"></span>
<div id="comment-15192" class="comment">
<div id="post-15192-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you want to be sure to get an answer (and a good one), it's better to ask your question to the OpenLayers community. Anyway, what about my answer?</p>
</div>
<div id="comment-15192-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 08:31)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15198"></span>
<div id="comment-15198" class="comment">
<div id="post-15198-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure where to put it. Does it just go in as is? Does it override the vars of lat lon and zoom? Tried it in various places without success. <a href="http://www.carnethy.com/maps/mapping%20info/osm_map_layer_to_use_in_iframe.htm">http://www.carnethy.com/maps/mapping%20info/osm_map_layer_to_use_in_iframe.htm</a></p>
</div>
<div id="comment-15198-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 09:22)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="15200"></span>
<div id="comment-15200" class="comment">
<div id="post-15200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, it works by adding this code after map.addLayer(lgpx): lgpx.events.register("loadend", lgpx, function() { this.map.zoomToExtent(this.getDataExtent()) } );</p>
</div>
<div id="comment-15200-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 09:42)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15202"></span>
<div id="comment-15202" class="comment">
<div id="post-15202-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Wow! It works! Thanks. And any idea how to get the start point from the GPX to set the pin in the right place?</p>
</div>
<div id="comment-15202-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 09:58)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="15204"></span>
<div id="comment-15204" class="comment not_top_scorer">
<div id="post-15204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can add the marker at the startpoint by modifying the previous giving code as follow:</p>
<p>lgpx.events.register("loadend", lgpx, function() {</p>
<p>this.map.zoomToExtent(this.getDataExtent());</p>
<p>var startPoint = this.features[0].geometry.components[0];</p>
<p>layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(startPoint.x, startPoint.y),icon));</p>
<p>});</p>
</div>
<div id="comment-15204-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 10:15)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15207"></span>
<div id="comment-15207" class="comment not_top_scorer">
<div id="post-15207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can only laugh in amazement! Never in a milliion years could I have worked that out!</p>
</div>
<div id="comment-15207-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 11:32)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="15216"></span>
<div id="comment-15216" class="comment not_top_scorer">
<div id="post-15216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can I further try your patience and ask how you would return the end point of a trace to place a finish pin? Would you adapt var startPoint = this.features[0].geometry.components[0];<br />
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(startPoint.x, startPoint.y),icon));</p>
<p>to var endPoint = something?</p>
</div>
<div id="comment-15216-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 15:01)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="15217"></span>
<div id="comment-15217" class="comment not_top_scorer">
<div id="post-15217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, something like that: var endPoint = this.features[0].geometry.components[this.features[0].geometry.components.length - 1];</p>
</div>
<div id="comment-15217-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 15:33)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15218"></span>
<div id="comment-15218" class="comment not_top_scorer">
<div id="post-15218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm. Didn't work! It puts a pin at the start, or maybe -1 trackpoint from the start</p>
</div>
<div id="comment-15218-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 17:00)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
</div>
<div id="comment-tools-15176" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15176-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15179"></span>

<div id="answer-container-15179" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Two methods of finding a lat lon in a trace are open the GPX with a text editor and just read them or upload the trace to OSM then click on edit trace and in polatch2 under options tick the box that shows lat lon. EDIT You can display the whole trace on an up to date OSM map and pick out boundary Lan Lons by opening the GPX with GPS Prune it's free from the activity workshop, but it does need Java to run ( as does JOSM ). <a href="https://activityworkshop.net/software/gpsprune/">https://activityworkshop.net/software/gpsprune/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '12, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '17, 21:23</strong> </span></p>
</div>
</div>
<div id="comments-container-15179" class="comments-container">
<span id="15201"></span>
<div id="comment-15201" class="comment">
<div id="post-15201-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I know I can open the trace in a text editor and read it, but this doesn't help with setting the centre and bounds of an openlayers map.</p>
</div>
<div id="comment-15201-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 09:47)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
</div>
<div id="comment-tools-15179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15179-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60003"></span>

<div id="answer-container-60003" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60003-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, how i put a marker on the end of gps track? i try use the similar code that you provided, but doesn't work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '17, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a27cae3d949a53902bd3c0600e0de893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wesley&#39;s gravatar image" />
<p><span>Wesley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wesley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60003" class="comments-container">
&#10;</div>
<div id="comment-tools-60003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60003-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60004"></span>

<div id="answer-container-60004" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>lgpx.events.register(&quot;loadend&quot;, lgpx, function() {
                    this.map.zoomToExtent(this.getDataExtent());
                    var startPoint = this.features[0].geometry.components[0];               
                    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(startPoint.x, startPoint.y),icon));</code></pre>
<p>Add this to the previous code, and add a new finish icon in the same way as the start point icon. By the way, I have no idea how this all works!</p>
<pre><code>var endPoint = this.features[0].geometry.components[this.features[0].geometry.components.length - 1];
                    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(endPoint.x, endPoint.y),icon2));
                });</code></pre>
<p>In our case the icons are set so:</p>
<pre><code>var size = new OpenLayers.Size(21, 25);
            var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
            var icon = new OpenLayers.Icon(&#39;../../mapping%20info/small_red_pin.png&#39;,size,offset);
            var icon2 = new OpenLayers.Icon(&#39;../../mapping%20info/small_blue_pin.png&#39;,size,offset);</code></pre>
<p>If the map has a circular route on it the finish icon will overlay the start icon which will be hidden if it's the same shape. But you could set the offset to deal with that. Increasing the negative number on length pushes the marker back down the trace.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '17, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e82dee06cd9f989e30bc1c57f2afc2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="digby&#39;s gravatar image" />
<p><span>digby</span><br />
<span class="score" title="46 reputation points">46</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="digby has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '17, 08:19</strong> </span></p>
</div>
</div>
<div id="comments-container-60004" class="comments-container">
&#10;</div>
<div id="comment-tools-60004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60004-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60029"></span>

<div id="answer-container-60029" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you, this problem was solved, now i'm fencing another problem: i want that the my app calculate the distance between two points.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '17, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a27cae3d949a53902bd3c0600e0de893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wesley&#39;s gravatar image" />
<p><span>Wesley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wesley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60029" class="comments-container">
&#10;</div>
<div id="comment-tools-60029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60029-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60030"></span>

<div id="answer-container-60030" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's got nothing to do with this question. You should start a new topic or find one that is relevant.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '17, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e82dee06cd9f989e30bc1c57f2afc2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="digby&#39;s gravatar image" />
<p><span>digby</span><br />
<span class="score" title="46 reputation points">46</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="digby has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60030" class="comments-container">
&#10;</div>
<div id="comment-tools-60030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60030-form-container" class="comment-form-container">
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

