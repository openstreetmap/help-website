+++
type = "question"
title = "Edit Open Cycle Maps in Qgis"
description = '''Dear all, Pretty new to OSM and GIS software overall here. I am working on a publication with the birding hotspots in Georgia (Caucasus). I would need to create some maps to indicate places of interest. As a baselayer I like the looks of Open Cyclemap, OCMlandscape or similar. So what I would need t...'''
date = "2021-05-25T17:16:00Z"
lastmod = "2021-05-26T08:29:00Z"
weight = 80291
keywords = [ "qgis", "opencyclemap" ]
aliases = [ "/questions/80291" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Edit Open Cycle Maps in Qgis](/questions/80291/edit-open-cycle-maps-in-qgis)

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
<span id="post-80291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80291-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>Pretty new to OSM and GIS software overall here.</p>
<p>I am working on a publication with the birding hotspots in Georgia (Caucasus). I would need to create some maps to indicate places of interest.</p>
<p>As a baselayer I like the looks of Open Cyclemap, OCMlandscape or similar.</p>
<p>So what I would need to do is edit these maps in Qgis to leave out some information and add some others (place names in English or English and Georgian). So can I edit this information straight in Qgis (and how) or do I need to go through OpenMapTiles or anything like that? </p>
<p>Thanks a lot in advance for your advice, B</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '21, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a917ca4a6fd423dad723d6416d8899b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brecht&#39;s gravatar image" />
<p><span>Brecht</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brecht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80291" class="comments-container">
&#10;</div>
<div id="comment-tools-80291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80291-form-container" class="comment-form-container">
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

<span id="80299"></span>

<div id="answer-container-80299" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80299-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tile servers provide raster information, hence the only edits are on a pixel basis. If you don't find georgian language generated tiles, go for a different approach.</p>
<p>If you don't need routing, go for <a href="http://umap.openstreetmap.fr/it/">umap</a>: chooose an aerial imagery background and vector layers with the OSM elements useful for the project (bird watching stands, paths, place names etc); if you don't plan to add your elements to OSM, you can straight edit the umap and/or import datasets in several formats (csv, geojson, gpx, kml...); vector layers styles are customizeble.</p>
<p>Umap provides user some funcions for interaction, typically click to get pop-up element info; see <a href="http://umap.openstreetmap.fr/it/map/alberi-monumentali_605261">example</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '21, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80299" class="comments-container">
&#10;</div>
<div id="comment-tools-80299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80299-form-container" class="comment-form-container">
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

