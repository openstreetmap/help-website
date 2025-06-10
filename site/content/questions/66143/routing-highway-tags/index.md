+++
type = "question"
title = "routing + highway tags"
description = '''Hi All, For a project, I need to optimize routing between about 5000 locations. Now, for this test, we need to apply our own speed mapping based on the highway tags which makes it a lot harder. I found graphhopper, but that would cost a lot (because we can only use the routing api to get the highway...'''
date = "2018-10-03T08:29:00Z"
lastmod = "2018-10-04T09:41:00Z"
weight = 66143
keywords = [ "openstreetmap", "routing", "highway", "graphhopper" ]
aliases = [ "/questions/66143" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [routing + highway tags](/questions/66143/routing-highway-tags)

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
<span id="post-66143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66143-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>For a project, I need to optimize routing between about 5000 locations. Now, for this test, we need to apply our own speed mapping based on the highway tags which makes it a lot harder. I found graphhopper, but that would cost a lot (because we can only use the routing api to get the highway tags, and we need the fastest route from every point to every point (=5000 x 5000 = 25 mil).</p>
<p>Does anyone know of an easier or cheaper tool/way to achieve this? Many thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '18, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/abc9cd26fc1df70831396718b2e18737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bcoghe&#39;s gravatar image" />
<p><span>Bcoghe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bcoghe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66143" class="comments-container">
&#10;</div>
<div id="comment-tools-66143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66143-form-container" class="comment-form-container">
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

<span id="66158"></span>

<div id="answer-container-66158" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66158-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can set up Graphhopper or OSRM on your own server, or on one you have rented from a provider such as Amazon AWS, Google Cloud Platform, Hetzner or OVH.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '18, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66158" class="comments-container">
&#10;</div>
<div id="comment-tools-66158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66158-form-container" class="comment-form-container">
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

