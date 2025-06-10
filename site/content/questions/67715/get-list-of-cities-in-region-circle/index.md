+++
type = "question"
title = "Get list of cities in region (circle)."
description = '''Hello guys! I need to get list of cities in region.  pick a point on a map enter the circle radius paint a circle around point with this radius get all cities in circle  Now I&#x27;m using OpenLayers and draw circle with RegularPolygon. I think I need your advice how should I make it if it is possible. T...'''
date = "2019-01-24T15:15:00Z"
lastmod = "2019-01-25T06:47:00Z"
weight = 67715
keywords = [ "region", "cities" ]
aliases = [ "/questions/67715" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get list of cities in region (circle).](/questions/67715/get-list-of-cities-in-region-circle)

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
<span id="post-67715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys! I need to get list of cities in region.</p>
<ol>
<li>pick a point on a map</li>
<li>enter the circle radius</li>
<li>paint a circle around point with this radius</li>
<li>get all cities in circle</li>
</ol>
<p>Now I'm using OpenLayers and draw circle with RegularPolygon.</p>
<p>I think I need your advice how should I make it if it is possible.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '19, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c978aa69a5b16d82a91cf599398a9ee3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aaalexxx&#39;s gravatar image" />
<p><span>Aaalexxx</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aaalexxx has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '19, 15:47</strong> </span></p>
</div>
</div>
<div id="comments-container-67715" class="comments-container">
&#10;</div>
<div id="comment-tools-67715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67715-form-container" class="comment-form-container">
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

<span id="67734"></span>

<div id="answer-container-67734" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67734-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aaalexxx has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry for being very brief, but you can use OverPass to query anything you want around a certain point with the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#.22around.22_-_finding_something_near_something_else">around function</a></p>
<p>So in OpenLayers you have to convert the click to lat/lon, then construct an http-request to the Overpass API with around in the query, do the http-request, parse the result and show it somehow. I'm sure you can find examples of combining Overpass and OpenLayers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '19, 06:47</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-67734" class="comments-container">
&#10;</div>
<div id="comment-tools-67734" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67734-form-container" class="comment-form-container">
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

