+++
type = "question"
title = "How do I route from a pedestrian area to the roads?"
description = '''The map that I&#x27;m working on has a pedestrian area. I&#x27;m trying to route from a point near there to another spot on the map but because the pedestrian area isn&#x27;t connected to the rest of the streets, the routing algorithm gives up. Should the map be modified to connect the pedestrian area to the road ...'''
date = "2011-07-25T18:37:00Z"
lastmod = "2011-07-26T18:15:00Z"
weight = 6548
keywords = [ "pedestrian", "routing", "area" ]
aliases = [ "/questions/6548" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I route from a pedestrian area to the roads?](/questions/6548/how-do-i-route-from-a-pedestrian-area-to-the-roads)

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
<span id="post-6548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6548-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The map that I'm working on has a pedestrian area. I'm trying to route from a point near there to another spot on the map but because the pedestrian area isn't connected to the rest of the streets, the routing algorithm gives up.</p>
<p>Should the map be modified to connect the pedestrian area to the road near it? Or is there some appropriate fix in the routing algorithm?</p>
<p><strong>Edit</strong>: Here's an example:</p>
<p><a href="http://www.yournavigation.org/?flat=32.122709107475&amp;flon=34.817094386304&amp;tlat=32.1092743&amp;tlon=34.8398295&amp;v=foot&amp;fast=1&amp;layer=mapnik">http://www.yournavigation.org/?flat=32.122709107475&amp;flon=34.817094386304&amp;tlat=32.1092743&amp;tlon=34.8398295&amp;v=foot&amp;fast=1&amp;layer=mapnik</a></p>
<p>Move the red marker around and you can see that when it looks for the closest node, sometimes it find a small, four-sided pedestrian area that has no path to the rest of the map. <a href="http://yournavigation.org">yournavigation.org</a> is using pyroute as far as I can tell.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '11, 18:37</strong></p>
<img src="https://secure.gravatar.com/avatar/de66513930801b968e559804884e41bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyal0&#39;s gravatar image" />
<p><span>eyal0</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyal0 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '11, 09:03</strong> </span></p>
</div>
</div>
<div id="comments-container-6548" class="comments-container">
&#10;</div>
<div id="comment-tools-6548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6548-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="6551"></span>

<div id="answer-container-6551" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6551-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the pedestrian area is connected to the road, you should add those connections to OSM. Sometimes it may be necessary for those areas parallel to a road to add either additional, somewhat artificial ways between them or directly connect them along a whole side with the road.</p>
<p>Routing engines need these kind of ways. If they will start doing approximations instead, they may also route you along ways that are impassable in reality. You don't want that either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '11, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6551" class="comments-container">
&#10;</div>
<div id="comment-tools-6551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6551-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6571"></span>

<div id="answer-container-6571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6571-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the area is connected in reality, you should connect it also in OSM. Routing algorithms can't assume connections, because some areas are not connected in reality.</p>
<p>Be sure to draw the pedestrian areas at their actual position (i.e. draw the actual borders, as it is a polygon and not a center line). Usually if there is car traffic going over the area (you will draw explicit roads for this crossing the area) you get a lot of intersections each of which should be connections (nodes).</p>
<p>If you can't deal otherwise in an appropriate manner with the situation, you will have to draw short explicit "virtual" connections (footways or similar) to connect the roads with the area, like <span>@scai</span> suggested.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '11, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-6571" class="comments-container">
&#10;</div>
<div id="comment-tools-6571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6571-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6550"></span>

<div id="answer-container-6550" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6550-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without knowing what area you are talking about it is hard to dertermine wether it is tagged correct. However there are many pedestrian areas that are not connected with the surrounding streets.</p>
<p>The routing engine should probably consider the case you are describing. It is hard to help you any more without knowing what routing engine and the area you are talking about.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '11, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-6550" class="comments-container">
<span id="6553"></span>
<div id="comment-6553" class="comment">
<div id="post-6553-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I added an example to the question.</p>
</div>
<div id="comment-6553-info" class="comment-info">
<span class="comment-age">(26 Jul '11, 09:03)</span> <span class="comment-user userinfo">eyal0</span>
</div>
</div>
</div>
<div id="comment-tools-6550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6550-form-container" class="comment-form-container">
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

