+++
type = "question"
title = "Different ways to mark a POI - why?"
description = '''Hey everyone, I noticed that there are different ways to mark buildings. For example there is a gas station where the building itself is marked as Fuel and another gas station has a point as gas station on it. If I am just looking at openstreetmap.org I don&#x27;t see a different in both ways but on my g...'''
date = "2022-07-09T09:20:00Z"
lastmod = "2022-07-11T14:23:00Z"
weight = 85016
keywords = [ "building", "points", "poi" ]
aliases = [ "/questions/85016" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Different ways to mark a POI - why?](/questions/85016/different-ways-to-mark-a-poi-why)

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
<span id="post-85016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85016-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone, I noticed that there are different ways to mark buildings. For example there is a gas station where the building itself is marked as Fuel and another gas station has a point as gas station on it. If I am just looking at openstreetmap.org I don't see a different in both ways but on my garmin I just find the gas station marked with the point. And I havent figured out yet how I can change this. So why are there different ways to mark a building?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '22, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/bcef061c410dc656e1b00d1cb723e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Morbit&#39;s gravatar image" />
<p><span>Morbit</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Morbit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85016" class="comments-container">
<span id="85029"></span>
<div id="comment-85029" class="comment">
<div id="post-85029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Both approaches are correct. So please don't "fix" the data by converting one to the other just because one application can't handle one of these approaches.</p>
</div>
<div id="comment-85029-info" class="comment-info">
<span class="comment-age">(11 Jul '22, 14:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85016-form-container" class="comment-form-container">
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

<span id="85018"></span>

<div id="answer-container-85018" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85018-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-85018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both approaches are used (and if nodes are used, some people place them at the entrance, and some people in vaguely the middle of the building).</p>
<p>If a building is used for more than one thing (e.g. on multiple floors) then using nodes for POIs is probably the easier approach.</p>
<p>What's happening on your garmin map is probably that whoever created the map didn't use the "--add-pois-to-areas" flag when creating it with <a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/How_to_create_a_map">mkgmap</a>.</p>
<p>In the default "<a href="https://github.com/openstreetmap/mkgmap/blob/master/resources/styles/default/points#L134">points</a>" file there is an entry for "amenity=fuel", but in the default "<a href="https://github.com/openstreetmap/mkgmap/blob/master/resources/styles/default/lines">lines</a>" file there is not. The "--add-pois-to-areas" flag allows POIs mapped in OSM as areas to also be processed by mkgmap as points.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '22, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-85018" class="comments-container">
&#10;</div>
<div id="comment-tools-85018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85018-form-container" class="comment-form-container">
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

