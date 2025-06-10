+++
type = "question"
title = "Display GPX on OSM on my website"
description = '''Hi, I&#x27;m creating a website that uses OSM: https://www.marcopanichi.com/work/trasimenobike/trasimeno-bike-park/percorsi/ I would display on this map some GPX traces. How to do this? I read many times these threads but I&#x27;m really missing out the point :/ https://stackoverflow.com/questions/23654251/dr...'''
date = "2022-08-27T09:22:00Z"
lastmod = "2022-09-08T09:11:00Z"
weight = 85454
keywords = [ "gpx" ]
aliases = [ "/questions/85454" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display GPX on OSM on my website](/questions/85454/display-gpx-on-osm-on-my-website)

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
<span id="post-85454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm creating a website that uses OSM: <a href="https://www.marcopanichi.com/work/trasimenobike/trasimeno-bike-park/percorsi/">https://www.marcopanichi.com/work/trasimenobike/trasimeno-bike-park/percorsi/</a></p>
<p>I would display on this map some GPX traces.</p>
<p>How to do this?</p>
<p>I read many times these threads but I'm really missing out the point :/ <a href="https://stackoverflow.com/questions/23654251/draw-path-in-openstreetmap">https://stackoverflow.com/questions/23654251/draw-path-in-openstreetmap</a> <a href="https://forum.openstreetmap.org/viewtopic.php?id=63585">https://forum.openstreetmap.org/viewtopic.php?id=63585</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '22, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c890204ea4e4d166318f3fb06a798152?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marco%20Panichi&#39;s gravatar image" />
<p><span>Marco Panichi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marco Panichi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85454" class="comments-container">
&#10;</div>
<div id="comment-tools-85454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85454-form-container" class="comment-form-container">
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

<span id="85456"></span>

<div id="answer-container-85456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85456-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-85456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are using the Leaflet library to display your map. You will have to create one or more additional layers in Leaflet showing your GPX track. Leaflet cannot show GPX tracks out of the box; you will either have to convert them a to GeoJSON (for example with the Open Source software QGIS), or you will have to install a Leaflet plugin that makes it possible to read GPX directly into Leaflet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '22, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85456" class="comments-container">
<span id="85585"></span>
<div id="comment-85585" class="comment">
<div id="post-85585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok thank you :)</p>
<p>I've converted my GPX into GeoJSON format with this tool: <a href="https://mygeodata.cloud/converter/gpx-to-geojson">https://mygeodata.cloud/converter/gpx-to-geojson</a></p>
<p>I've got many files:</p>
<ul>
<li>route_points.geojson</li>
<li>routes.geojson</li>
<li>track_points.geojson</li>
<li>tracks.geojson</li>
<li>waypoints.geojson</li>
</ul>
<p>Now, the question is: how to show these layers(?) into my map?</p>
</div>
<div id="comment-85585-info" class="comment-info">
<span class="comment-age">(08 Sep '22, 09:11)</span> <span class="comment-user userinfo">Marco Panichi</span>
</div>
</div>
</div>
<div id="comment-tools-85456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85456-form-container" class="comment-form-container">
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

