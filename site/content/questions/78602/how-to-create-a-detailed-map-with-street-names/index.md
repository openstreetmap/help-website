+++
type = "question"
title = "how to create a detailed map with street names"
description = '''Hello group, I would be grateful if you could help me in a project I am working. In essence I want to create maps with street names(like in the screenshot) I actually have a qgis 2.18 app but when i try to download shapefiles it only get roads layers. '''
date = "2021-01-30T18:39:00Z"
lastmod = "2021-01-31T12:59:00Z"
weight = 78602
keywords = [ "map", "street", "names" ]
aliases = [ "/questions/78602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to create a detailed map with street names](/questions/78602/how-to-create-a-detailed-map-with-street-names)

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
<span id="post-78602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello group, I would be grateful if you could help me in a project I am working.</p>
<p>In essence I want to create maps with street names(like in the screenshot) I actually have a qgis 2.18 app but when i try to download shapefiles it only get roads layers.</p>
<p><img src="/upfiles/Screenshot_NpdGQnZ.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '21, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f98892b805fbf265a4c38f5cf8330328?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boxhibonks&#39;s gravatar image" />
<p><span>boxhibonks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boxhibonks has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-78602" class="comments-container">
<span id="78605"></span>
<div id="comment-78605" class="comment">
<div id="post-78605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where are you downloading your shapefiles? OSM isn't divided into layers like most GIS, so your provider may be filtering what you've downloaded.</p>
</div>
<div id="comment-78605-info" class="comment-info">
<span class="comment-age">(31 Jan '21, 00:40)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-78602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78602-form-container" class="comment-form-container">
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

<span id="78612"></span>

<div id="answer-container-78612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78612-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a another simple approach (without uploading OSM data into PostGIS) I would recommend a series of overpass queries to build layers in QGIS. There is a QGIS plugin which uses overpass syntax to populate layers. However, if you need areas then directly running queries in Overpass-turbo and downloading the geojson is more appropriate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '21, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-78612" class="comments-container">
&#10;</div>
<div id="comment-tools-78612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78612-form-container" class="comment-form-container">
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

