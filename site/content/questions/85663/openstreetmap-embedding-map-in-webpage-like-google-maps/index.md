+++
type = "question"
title = "Openstreetmap: embedding map in webpage (like Google Maps)"
description = '''Is there a way to embed/mashup the OpenStreetMap in your page (like the way Google Maps API works)? I need to show a map inside my page with some markers and allow dragging/zooming around, maybe routing. I suspect there would be some Javascript API for this, but I can&#x27;t seem to find it. Searching ge...'''
date = "2022-09-20T13:34:00Z"
lastmod = "2022-09-20T17:50:00Z"
weight = 85663
keywords = [ "skytv" ]
aliases = [ "/questions/85663" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Openstreetmap: embedding map in webpage (like Google Maps)](/questions/85663/openstreetmap-embedding-map-in-webpage-like-google-maps)

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
<span id="post-85663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85663-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to embed/mashup the OpenStreetMap in your page (like the way Google Maps API works)?</p>
<p>I need to show a map inside my page with some markers and allow dragging/zooming around, maybe routing. I suspect there would be some Javascript API for this, but I can't seem to find it.</p>
<p>Searching gets me an API for access to raw map data , but that seems to be more for map editing; besides, working with that would be a heavy task for AJAX.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-skytv" rel="tag" title="see questions tagged &#39;skytv&#39;">skytv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '22, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/192f37b12d31ff2a8559ae0ce0eb4b8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dexter&#39;s gravatar image" />
<p><span>dexter</span><br />
<span class="score" title="19 reputation points">19</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dexter has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '22, 18:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-85663" class="comments-container">
&#10;</div>
<div id="comment-tools-85663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85663-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="85664"></span>

<div id="answer-container-85664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85664-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi!</p>
<p>Javacript packages like <a href="https://leafletjs.com/">Leaflet</a> and <a href="https://maplibre.org/">MapLibre</a> allow you to create web maps really easily. If you check out their docs they'll give you a bunch of examples displaying Open Street Map! The first page on Leaflet shows you how to display an OSM map and add a marker.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '22, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c5208ea7cd2caac363699008cde909ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danhirst&#39;s gravatar image" />
<p><span>danhirst</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danhirst has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '22, 13:43</strong> </span></p>
</div>
</div>
<div id="comments-container-85664" class="comments-container">
&#10;</div>
<div id="comment-tools-85664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85668"></span>

<div id="answer-container-85668" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>UMap and facilmap can do that.</p>
<p>Search this site if you need more details, this question has been answered many times...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '22, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-85668" class="comments-container">
&#10;</div>
<div id="comment-tools-85668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85668-form-container" class="comment-form-container">
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

