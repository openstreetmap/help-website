+++
type = "question"
title = "How can we display parcel outlines or boundaries on OpenStreetMap?"
description = '''Please help provide an example of how to display third-party information on top of OSM for displaying parcel boundaries. Any link with a sample for example will be helpful. I have also attached an image.'''
date = "2023-02-07T11:35:00Z"
lastmod = "2023-02-07T12:24:00Z"
weight = 86638
keywords = [ "map-with-parcel" ]
aliases = [ "/questions/86638" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can we display parcel outlines or boundaries on OpenStreetMap?](/questions/86638/how-can-we-display-parcel-outlines-or-boundaries-on-openstreetmap)

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
<span id="post-86638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please help provide an example of how to display third-party information on top of OSM for displaying parcel boundaries. Any link with a sample for example will be helpful. I have also attached an image.<img src="https://help.openstreetmap.org/upfiles/openstreet_with_boundaries.jpg" alt="Image with parcel boundaries" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map-with-parcel" rel="tag" title="see questions tagged &#39;map-with-parcel&#39;">map-with-parcel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '23, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9cacdc2caa368cfa3c8eb73574d850be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vijaypandeychetu&#39;s gravatar image" />
<p><span>vijaypandeyc...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vijaypandeychetu has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-86638" class="comments-container">
&#10;</div>
<div id="comment-tools-86638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86638-form-container" class="comment-form-container">
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

<span id="86639"></span>

<div id="answer-container-86639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86639-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This depends on what medium you want to use - the techniques you would use for a browser map are different from those you would use for a printed map or maybe an app.</p>
<p>One option for a browser-based solution is to use the popular "Leaflet" library to display an OSM map (when accessing OSM's severs, always honour the <a href="https://operations.osmfoundation.org/policies/tiles/">Tile Usage Policy</a>) and then draw your parcel polygons on top. The source of the parcel polygons could e.g. be a GeoJSON file that you have created. See here for an example that does this: <a href="https://www.igismap.com/add-load-geojson-file-point-polyline-polygon-map-leaflet-js/">https://www.igismap.com/add-load-geojson-file-point-polyline-polygon-map-leaflet-js/</a></p>
<p>If you have a very large number of polygons to draw, you will want to implement a server-side filter (so that the Leaflet library can request from the server only those polygons needed for the current map view, not the whole data set). This could be a simple PostGIS database or something like GeoServer (both Open Source).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '23, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86639" class="comments-container">
&#10;</div>
<div id="comment-tools-86639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86639-form-container" class="comment-form-container">
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

