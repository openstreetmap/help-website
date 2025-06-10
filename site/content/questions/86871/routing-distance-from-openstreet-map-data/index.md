+++
type = "question"
title = "Routing distance from Openstreet Map data"
description = '''We have a application where we need routing information(Transport distance) between two points so I am trying to setup my own routing server. I used OSRM backend API to calculate routing waypoints but they have usage limit. Alternatives to that are Mapbox(Paid APIs), Openlayers(Free APIs).  Geofabri...'''
date = "2023-03-03T14:05:00Z"
lastmod = "2023-03-06T11:35:00Z"
weight = 86871
keywords = [ "openstreetmap.de" ]
aliases = [ "/questions/86871" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Routing distance from Openstreet Map data](/questions/86871/routing-distance-from-openstreet-map-data)

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
<span id="post-86871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86871-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a application where we need routing information(Transport distance) between two points so I am trying to setup my own routing server. I used OSRM backend API to calculate routing waypoints but they have usage limit. Alternatives to that are Mapbox(Paid APIs), Openlayers(Free APIs).</p>
<p>Geofabrik provides data extracts in .osm.pbf format But how can I use the data to to get routing information(distance between two LatLong).</p>
<p>I explored leaflet library also, but they seems to be using same OSRM backend API.</p>
<p>Should I create my own library to access this data or using Openlayers is good option? Any suggestions, ideas or if I am mising out anything, Please guide me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap.de" rel="tag" title="see questions tagged &#39;openstreetmap.de&#39;">openstreetmap.de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '23, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/5ad7f3355e56126c366d8cabe7021aff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vikas%20Singla&#39;s gravatar image" />
<p><span>Vikas Singla</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vikas Singla has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86871" class="comments-container">
&#10;</div>
<div id="comment-tools-86871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86871-form-container" class="comment-form-container">
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

<span id="86872"></span>

<div id="answer-container-86872" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86872-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vikas Singla has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can set up either GraphHopper or OSRM on your own infrastructure, then load a PBF file from Geofabrik into that software, and then use the API on your own server. Both Leaflet and OpenLayers can be used but the routing software's API could also be used directly by the application that requires the distance, no need to use a Javascript library.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '23, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86872" class="comments-container">
<span id="86879"></span>
<div id="comment-86879" class="comment">
<div id="post-86879-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey thanks, I was able set up my own OSRM and load pbf file from Geofabrik. However, if I load for smaller region like berlin. It works. But if I try it for entire US. It does not. I am trying to figure out.</p>
</div>
<div id="comment-86879-info" class="comment-info">
<span class="comment-age">(06 Mar '23, 04:49)</span> <span class="comment-user userinfo">Vikas Singla</span>
</div>
</div>
<span id="86883"></span>
<div id="comment-86883" class="comment">
<div id="post-86883-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OSRM has hefty hardware requirements and you may need a bigger server to run the whole US.</p>
</div>
<div id="comment-86883-info" class="comment-info">
<span class="comment-age">(06 Mar '23, 11:35)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86872-form-container" class="comment-form-container">
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

