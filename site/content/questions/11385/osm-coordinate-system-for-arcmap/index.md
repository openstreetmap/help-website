+++
type = "question"
title = "OSM coordinate system for ArcMap"
description = '''I downloaded multiple street layers using OSM and converted them to shapefiles using OSM2SHP. Now when I try to give it a Projected Coordinate System (Specifically UTM Zone 19) for Dominican Republic the layers have a big exponential value. Something like 10^17 or close and therefore, they are not b...'''
date = "2012-03-21T13:29:00Z"
lastmod = "2012-03-22T00:39:00Z"
weight = 11385
keywords = [ "gis", "osm", "arcmap" ]
aliases = [ "/questions/11385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM coordinate system for ArcMap](/questions/11385/osm-coordinate-system-for-arcmap)

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
<span id="post-11385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11385-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded multiple street layers using OSM and converted them to shapefiles using OSM2SHP. Now when I try to give it a Projected Coordinate System (Specifically UTM Zone 19) for Dominican Republic the layers have a big exponential value. Something like 10^17 or close and therefore, they are not being displayed on the screen.</p>
<p>I did some research and found out OSM coordinate system but I can't find it in GIS. I see other people don't have allot of trouble with this therefore I must be doing a simple mistake.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-arcmap" rel="tag" title="see questions tagged &#39;arcmap&#39;">arcmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '12, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/137209dde38a0674b1fdd63b7757f167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vaironxxrd&#39;s gravatar image" />
<p><span>Vaironxxrd</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vaironxxrd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11385" class="comments-container">
&#10;</div>
<div id="comment-tools-11385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11385-form-container" class="comment-form-container">
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

<span id="11403"></span>

<div id="answer-container-11403" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11403-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap data uses EPSG:4326 (WGS84). <a href="http://spatialreference.org/ref/epsg/4326/prj/">Adding a .prj file</a> to matching the .shp filename should resolve the issues.</p>
<p>eg: if the file is called Africa.shp, download the .prj file from the above link and rename it to Africa.prj</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '12, 00:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-11403" class="comments-container">
&#10;</div>
<div id="comment-tools-11403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11403-form-container" class="comment-form-container">
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

