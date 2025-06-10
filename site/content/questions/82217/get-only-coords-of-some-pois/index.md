+++
type = "question"
title = "Get only coords of some POIs"
description = '''How to get only coordinates of some POIs, for example only parks in some city? I want to use this great data in my school project written in c#!'''
date = "2021-10-17T23:23:00Z"
lastmod = "2021-10-19T03:39:00Z"
weight = 82217
keywords = [ "c#", "poi" ]
aliases = [ "/questions/82217" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get only coords of some POIs](/questions/82217/get-only-coords-of-some-pois)

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
<span id="post-82217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82217-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to get only coordinates of some POIs, for example only parks in some city?</p>
<p>I want to use this great data in my school project written in c#!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '21, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/dd0fc5e6995397459d448637e249b120?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CAESIUM137&#39;s gravatar image" />
<p><span>CAESIUM137</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CAESIUM137 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82217" class="comments-container">
&#10;</div>
<div id="comment-tools-82217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82217-form-container" class="comment-form-container">
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

<span id="82231"></span>

<div id="answer-container-82231" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82231-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CAESIUM137 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you only want a few POI types the easiest way to download the data is probably with <a href="https://overpass-turbo.eu/">Overpass turbo</a>. If you only want centroids there is an <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Geometry_attributes"><code>out center</code></a> option for this.</p>
<p>If you want to query more of the data you're probably better off downloading <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">an extract</a> and processing locally. I haven't used any of them but there are a variety of pre-existing <a href="https://wiki.openstreetmap.org/wiki/Frameworks">frameworks</a> to choose from.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 03:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-82231" class="comments-container">
&#10;</div>
<div id="comment-tools-82231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82231-form-container" class="comment-form-container">
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

