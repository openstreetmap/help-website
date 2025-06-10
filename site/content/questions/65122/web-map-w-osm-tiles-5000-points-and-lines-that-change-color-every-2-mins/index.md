+++
type = "question"
title = "Web map w OSM tiles &amp; 5,000 points and lines that change color every 2 mins"
description = '''I&#x27;m looking for advice and recommendations.  We want to create a web map that has client pan/zoom capabilities for around 10,000 clients. We want to use custom rendered OSM tiles served from our own server. On top of the OSM tiles we need to map point and line features that change color(state) every...'''
date = "2018-08-04T00:16:00Z"
lastmod = "2019-10-30T19:52:00Z"
weight = 65122
keywords = [ "leaflet", "osm" ]
aliases = [ "/questions/65122" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Web map w OSM tiles & 5,000 points and lines that change color every 2 mins](/questions/65122/web-map-w-osm-tiles-5000-points-and-lines-that-change-color-every-2-mins)

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
<span id="post-65122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65122-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for advice and recommendations.</p>
<p>We want to create a web map that has client pan/zoom capabilities for around 10,000 clients. We want to use custom rendered OSM tiles served from our own server. On top of the OSM tiles we need to map point and line features that change color(state) every two minutes. How would you recommend we do this? Would Leaflet work? How should we store/serve the point/line features. Should we store them in a shapefile, csv file, sql server database, etc? We can't store them in the OSM tiles because they need to change colors. Also, we don't want to buy anything if possible.</p>
<p>Any help, insights you can offer would be most appreciated.<br />
Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '18, 00:16</strong></p>
<img src="https://secure.gravatar.com/avatar/41a7fedf2793f657dcef6efefeb10b49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeattleHeather&#39;s gravatar image" />
<p><span>SeattleHeather</span><br />
<span class="score" title="220 reputation points">220</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeattleHeather has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Aug '18, 00:18</strong> </span></p>
</div>
</div>
<div id="comments-container-65122" class="comments-container">
&#10;</div>
<div id="comment-tools-65122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65122-form-container" class="comment-form-container">
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

<span id="65124"></span>

<div id="answer-container-65124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65124-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, you have the option of transferring your overlay to the client either as raster data (ie an image) or as vector data (ie structured information that contains the coordinates and status of every feature and the client then draws them). If you can construct a mechanism whereby the client is only informed of <em>changes</em> of object state, so that initially you transmit youe 5000 objects but then regularly you only transmit a (supposedly much smaller) state change information, that could work well with vectors. Vectors will also have the advantage that the client knows about them, so you can do something like hovering over an object changes its colour or so.</p>
<p>If you have to basically refresh all objects all the time, vector might be too resource intensive, and transmitting just a PNG with all the overlay stuff is preferable. Typically you could use simple WMS server in the backend for that, translating the data from a database into a PNG image for display by OpenLayers or Leaflet. Check out the OSM Inspector (tools.geofabrik.de/osmi) or an example of a web page that uses a tiled OSM base map and displays database-controlled WMS layers on top.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '18, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-65124" class="comments-container">
<span id="71382"></span>
<div id="comment-71382" class="comment">
<div id="post-71382-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik Ramm, do you have any suggestions/guidance as to how to create database-controlled WMS layers? Free software that we can use to do this? Thanks so much for your help so far. :)</p>
</div>
<div id="comment-71382-info" class="comment-info">
<span class="comment-age">(30 Oct '19, 17:55)</span> <span class="comment-user userinfo">SeattleHeather</span>
</div>
</div>
<span id="71386"></span>
<div id="comment-71386" class="comment">
<div id="post-71386-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>MapServer (see mapserver.org) or GeoServer (see geoserver.org) are the obvious Open Source choices.</p>
</div>
<div id="comment-71386-info" class="comment-info">
<span class="comment-age">(30 Oct '19, 19:52)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65124-form-container" class="comment-form-container">
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

