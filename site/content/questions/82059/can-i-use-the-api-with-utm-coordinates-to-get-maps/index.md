+++
type = "question"
title = "Can I use the API with UTM Coordinates to get maps?"
description = '''Hi, apologies if this is a silly question. I want to use the API for a school project to get some map data overlayed with satellite images. My GIS data is in UTM format and I was wondering if I can do the API call (left, right, up, down) with that instead of longitude and latitude? Thanks for any po...'''
date = "2021-10-07T14:26:00Z"
lastmod = "2021-10-08T05:13:00Z"
weight = 82059
keywords = [ "osmapi_python", "osm", "coordinates", "utm" ]
aliases = [ "/questions/82059" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I use the API with UTM Coordinates to get maps?](/questions/82059/can-i-use-the-api-with-utm-coordinates-to-get-maps)

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
<span id="post-82059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82059-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, apologies if this is a silly question.</p>
<p>I want to use the API for a school project to get some map data overlayed with satellite images. My GIS data is in UTM format and I was wondering if I can do the API call (left, right, up, down) with that instead of longitude and latitude?</p>
<p>Thanks for any pointers, or general resources you could share. I've never used OSM before but I'm excited to learn.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-utm" rel="tag" title="see questions tagged &#39;utm&#39;">utm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '21, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/cdbcea9c4b54ebbd5c124713a663f464?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oliver&#39;s gravatar image" />
<p><span>oliver</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oliver has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82059" class="comments-container">
&#10;</div>
<div id="comment-tools-82059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82059-form-container" class="comment-form-container">
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

<span id="82071"></span>

<div id="answer-container-82071" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82071-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="oliver has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>No</strong>, OSM &amp; Overpass only understand WGS lat/lon.</p>
<p>The slightly more complex answer is that if you are using QGIS you can query OSM data with the QuickOSM plugin which talks to overpass &amp; can set the bounds to your current canvas. (I've just checked this with a project in EPSG:27700).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '21, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-82071" class="comments-container">
<span id="82080"></span>
<div id="comment-82080" class="comment">
<div id="post-82080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for the answer!</p>
</div>
<div id="comment-82080-info" class="comment-info">
<span class="comment-age">(08 Oct '21, 05:13)</span> <span class="comment-user userinfo">oliver</span>
</div>
</div>
</div>
<div id="comment-tools-82071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82071-form-container" class="comment-form-container">
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

