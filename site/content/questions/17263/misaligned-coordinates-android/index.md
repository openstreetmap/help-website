+++
type = "question"
title = "misaligned coordinates android"
description = '''Hi I am making an android app which uses an OpenStreetMap. I have my own tile server which serves the street map. When I tell the app to centre on a specifc area on the map by passing in the coordinates as a GeoPoint, it centres somewhere around Africa when it should centre on Edinburgh. Here is the...'''
date = "2012-10-29T15:07:00Z"
lastmod = "2012-10-30T09:34:00Z"
weight = 17263
keywords = [ "openstreetmap", "android", "osmdroid" ]
aliases = [ "/questions/17263" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [misaligned coordinates android](/questions/17263/misaligned-coordinates-android)

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
<span id="post-17263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17263-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I am making an android app which uses an OpenStreetMap. I have my own tile server which serves the street map.</p>
<p>When I tell the app to centre on a specifc area on the map by passing in the coordinates as a GeoPoint, it centres somewhere around Africa when it should centre on Edinburgh.</p>
<p>Here is the code:</p>
<pre><code>// osm map view 
MapView osmMap;
&#10;@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
&#10;    osmMap = (MapView) findViewById(R.id.mapview);
    osmMap.setMultiTouchControls(true);
&#10;    // Create custom map source pointing to Tile Server
    XYTileSource myMapSource = new XYTileSource(&quot;myMap&quot;, null, 0, 16, 256, &quot;.png&quot;, Constants.LOCAL_SERVER_URL);
&#10;    // Set the source and default map coordinates/zoom
    osmMap.setTileSource(myMapSource);
&#10;    osmMap.getController().animateTo(new GeoPoint(55.95223359877632*1e6, -3.188550710678032*1e6));
    osmMap.getController().setZoom(Constants.DEFAULT_ZOOM); 
}</code></pre>
<p>Anyone know how I can get the coorindates to align with the map correctly?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '12, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17263" class="comments-container">
&#10;</div>
<div id="comment-tools-17263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17263-form-container" class="comment-form-container">
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

<span id="17291"></span>

<div id="answer-container-17291" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17291-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srose has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your map is centering off the african coast around here: <a href="https://www.openstreetmap.org/?mlat=0&amp;mlon=0&amp;zoom=4&amp;layers=M">https://www.openstreetmap.org/?mlat=0&amp;mlon=0&amp;zoom=4&amp;layers=M</a></p>
<p>Then your coordinates are not working correctly. that location is the 0,0 of lat/long. Do a thorough check on whether your GeoPoint is working properly</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7ced9ba139adb4087bbe8935b2eab74d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samlarsen1&#39;s gravatar image" />
<p><span>samlarsen1</span><br />
<span class="score" title="124 reputation points">124</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samlarsen1 has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-17291" class="comments-container">
&#10;</div>
<div id="comment-tools-17291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17291-form-container" class="comment-form-container">
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

