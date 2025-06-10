+++
type = "question"
title = "Is there a quick and free way to display raster map data offline?"
description = '''I have a raster layer that I would like to use as a basemap and overlay vector OSM data (cities and the such). I would also like to have the capabilities to view it offline on a Windows desktop computer, such as that the marginalia stays on the current screen when I zoom and pan, coordinates are acc...'''
date = "2013-04-24T23:10:00Z"
lastmod = "2013-04-25T08:09:00Z"
weight = 21803
keywords = [ "offline", "offlinemaps" ]
aliases = [ "/questions/21803" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a quick and free way to display raster map data offline?](/questions/21803/is-there-a-quick-and-free-way-to-display-raster-map-data-offline)

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
<span id="post-21803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21803-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a raster layer that I would like to use as a basemap and overlay vector OSM data (cities and the such). I would also like to have the capabilities to view it offline on a Windows desktop computer, such as that the marginalia stays on the current screen when I zoom and pan, coordinates are accessible, etc. Perhaps what I'm looking for is an offline version of Google Maps, but stripped down since I am not concerned with editability. Is there a free/widely available way to do this?</p>
<p>I am currently playing around with ArcGIS-exported PDFs, which preserve geographic coordinates, but do not retain marginalia within the Adobe Reader viewing frame when I zoom in.</p>
<p>I started looking at the <a href="http://wiki.openstreetmap.org/wiki/Software">Software</a> link, but have had no luck thus far.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '13, 23:10</strong></p>
<img src="https://secure.gravatar.com/avatar/c0eadec55b03974f8871b933c48b07a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="melynnduh&#39;s gravatar image" />
<p><span>melynnduh</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="melynnduh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '13, 23:16</strong> </span></p>
</div>
</div>
<div id="comments-container-21803" class="comments-container">
&#10;</div>
<div id="comment-tools-21803" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21803-form-container" class="comment-form-container">
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

<span id="21819"></span>

<div id="answer-container-21819" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21819-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have your raster data in tiles and your OSM vector overlay in KML form then you can easily run an offline OpenLayers "website" (opening something like <code>file:///my-usb-stick/index.html</code> in your web browser). The Javascript/HTML needed for this is minimal, however bringing your data into a suitable form might require some work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '13, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21819" class="comments-container">
&#10;</div>
<div id="comment-tools-21819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21819-form-container" class="comment-form-container">
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

