+++
type = "question"
title = "How to extract relation&#x27;s polyline as array of coordinates?"
description = '''I want to get the polyline&#x27;s coordinates without any extra info from a relation like this one: [[40.54,40.65],[40.55,40.64]...] Here are some relations for which I need this data: 29322, 19782, 19763 How can I do it? I tried to use overpass turbo but it gives me ways and nodes which is not what I wa...'''
date = "2020-05-13T09:21:00Z"
lastmod = "2020-05-13T10:40:00Z"
weight = 74782
keywords = [ "overpass-turbo", "polyline" ]
aliases = [ "/questions/74782" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract relation's polyline as array of coordinates?](/questions/74782/how-to-extract-relations-polyline-as-array-of-coordinates)

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
<span id="post-74782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74782-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get the polyline's coordinates without any extra info from a relation like this one:</p>
<p>[[40.54,40.65],[40.55,40.64]...]</p>
<p>Here are some relations for which I need this data: 29322, 19782, 19763</p>
<p>How can I do it? I tried to use overpass turbo but it gives me ways and nodes which is not what I want.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-polyline" rel="tag" title="see questions tagged &#39;polyline&#39;">polyline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '20, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/56693f02b17ce6e1a3fe3705b7579362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dimitar155&#39;s gravatar image" />
<p><span>Dimitar155</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dimitar155 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '20, 09:22</strong> </span></p>
</div>
</div>
<div id="comments-container-74782" class="comments-container">
&#10;</div>
<div id="comment-tools-74782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74782-form-container" class="comment-form-container">
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

<span id="74783"></span>

<div id="answer-container-74783" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74783-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass Turbo also lets you export GeoJSON which comes very close to what you are looking for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '20, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-74783" class="comments-container">
<span id="74785"></span>
<div id="comment-74785" class="comment">
<div id="post-74785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Overpas turbo gives me multiple arrays and the polyline is broken for some reason. <a href="https://i.imgur.com/2VNyWBe.png">https://i.imgur.com/2VNyWBe.png</a> The red line should be following the black markers. Also here the line is fine but only for the one direction. On the other it gets wiggly. <a href="https://i.imgur.com/d1fznCF.png">https://i.imgur.com/d1fznCF.png</a></p>
</div>
<div id="comment-74785-info" class="comment-info">
<span class="comment-age">(13 May '20, 09:37)</span> <span class="comment-user userinfo">Dimitar155</span>
</div>
</div>
<span id="74787"></span>
<div id="comment-74787" class="comment">
<div id="post-74787-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I tried an Overpass query like relation(19763); out geom; and loaded that in geojson.io and it looks all right...</p>
</div>
<div id="comment-74787-info" class="comment-info">
<span class="comment-age">(13 May '20, 09:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="74788"></span>
<div id="comment-74788" class="comment">
<div id="post-74788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like something went wrong when I saved the data to the database which caused the problem.</p>
<p>edit: It doesn't work for relation 19777. Overpass Turbo returns multilinestring instead of linestring which breaks something. How can I convert multilinestring to linestring?</p>
<p>edit 2: This query fixed everything:</p>
<p>[out:json][timeout:300];</p>
<p>(</p>
<p>relation(relation_id);</p>
<p>&lt;;</p>
<p>);</p>
<p>out geom;</p>
</div>
<div id="comment-74788-info" class="comment-info">
<span class="comment-age">(13 May '20, 10:40)</span> <span class="comment-user userinfo">Dimitar155</span>
</div>
</div>
</div>
<div id="comment-tools-74783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74783-form-container" class="comment-form-container">
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

