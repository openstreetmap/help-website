+++
type = "question"
title = "overpass API Query for own installed server"
description = '''Hi, I am new to OSM and overpass API. Is it possible to get list of Mcdonalds in a particular area for example  1. List all Mcdonalds in paris 2. List all Mcdonalds in London etc.. I have setup my server with OSM and overpass api, how can make aquery to request the above ? Help very much appriciated'''
date = "2017-04-20T11:55:00Z"
lastmod = "2017-04-20T15:45:00Z"
weight = 55716
keywords = [ "openstreetmap", "overpassapi" ]
aliases = [ "/questions/55716" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overpass API Query for own installed server](/questions/55716/overpass-api-query-for-own-installed-server)

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
<span id="post-55716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am new to OSM and overpass API. Is it possible to get list of Mcdonalds in a particular area for example 1. List all Mcdonalds in paris 2. List all Mcdonalds in London etc.. I have setup my server with OSM and overpass api, how can make aquery to request the above ?</p>
<p>Help very much appriciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '17, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/dd43c315f1c0d409d48ce8029c73122e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mptkarthikeyan_82&#39;s gravatar image" />
<p><span>mptkarthikey...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mptkarthikeyan_82 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55716" class="comments-container">
&#10;</div>
<div id="comment-tools-55716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55716-form-container" class="comment-form-container">
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

<span id="55718"></span>

<div id="answer-container-55718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's an example Overpass API script for finding McDonald's in Paris, generated using the Overpass Turbo wizard:</p>
<p><a href="http://overpass-turbo.eu/s/ou4">http://overpass-turbo.eu/s/ou4</a></p>
<p>Here I've replaced the Overpass Turbo geocode function with a direct reference to the Paris area id, to make the query work directly against Overpass API:</p>
<p><a href="http://overpass-turbo.eu/s/ou5">http://overpass-turbo.eu/s/ou5</a></p>
<p>The id for the area is related to the id for the OSM object, as described here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '17, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55718" class="comments-container">
&#10;</div>
<div id="comment-tools-55718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55718-form-container" class="comment-form-container">
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

