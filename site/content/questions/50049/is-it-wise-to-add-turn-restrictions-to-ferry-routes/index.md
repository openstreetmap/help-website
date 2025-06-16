+++
type = "question"
title = "Is it wise to add turn restrictions to ferry routes?"
description = '''I&#x27;ve been bothered by the routing on some local Ferry routes for a while, all the default routing providers on the OSM site recommend changing ferries mid-route, at a node 500m or so away from the ferry terminal where the change should actually take place. example (presently showing the recommended ...'''
date = "2016-06-06T22:16:00Z"
lastmod = "2016-06-08T12:02:00Z"
weight = 50049
keywords = [ "ferry", "turn_restrictions", "routing" ]
aliases = [ "/questions/50049" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it wise to add turn restrictions to ferry routes?](/questions/50049/is-it-wise-to-add-turn-restrictions-to-ferry-routes)

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
<span id="post-50049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50049-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been bothered by the routing on some local Ferry routes for a while, all the default routing providers on the OSM site recommend changing ferries mid-route, at a node 500m or so away from the ferry terminal where the change should actually take place. <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=49.4331%2C-123.4723%3B49.3795%2C-123.3315">example</a> (presently showing the recommended route transferring at the node offshore of Horseshoe Bay terminal)</p>
<p>This may be due to a poor choice of mapping approach for the routes, but as the ferries may leave from multiple berths it seems to be well mapped to me. I've added turn restrictions to the routes at the node (edit <a href="https://www.openstreetmap.org/changeset/39849339">here</a>). Is this a reasonable approach? Please check the edit, and let me know if it should be reverted, or if there is a more elegant way of doing this.</p>
<p><strong>Edit:</strong> Some (All?) of the routing engines have now updated to take into account the turn restrictions, so the example link is no longer behaving as before.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ferry" rel="tag" title="see questions tagged &#39;ferry&#39;">ferry</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '16, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '16, 20:12</strong> </span></p>
</div>
</div>
<div id="comments-container-50049" class="comments-container">
&#10;</div>
<div id="comment-tools-50049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50049-form-container" class="comment-form-container">
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

<span id="50054"></span>

<div id="answer-container-50054" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50054-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-50054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems to me that it would be better to remove the shared node. There's no relation between the routes, so there's no reason to have the ways intersect rather than crossing without intersection.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '16, 06:49</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-50054" class="comments-container">
<span id="50055"></span>
<div id="comment-50055" class="comment">
<div id="post-50055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's no relation between the 3 major routes, but all three do have a relationship with all three berths that the minor route=ferry ways lead to.</p>
<p>If we had the routes cross each other w/o a common node we'd have to inaccurately show each route connect w/ a single berth, or have each one split to 3 ways that go to each berth -- resulting in messy duplication.</p>
<p>Neither solution seems to be an improvement using turn restrictions.</p>
</div>
<div id="comment-50055-info" class="comment-info">
<span class="comment-age">(07 Jun '16, 07:49)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-50054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50054-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50062"></span>

<div id="answer-container-50062" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50062-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-50062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I doubt that turn restrictions on a ferry route will be taken into account. One way you could fix this is by not sharing the ways that reach the berths (so that each berth has 3 routes arriving to it). Or try to take you question directly to <a href="https://github.com/Project-OSRM/osrm-backend/issues">the router's bugtracker</a>, as the proper fix might have to be done on the software side.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '16, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-50062" class="comments-container">
<span id="50079"></span>
<div id="comment-50079" class="comment">
<div id="post-50079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't you think that each berth having 3 ways arriving to it is very messy?</p>
</div>
<div id="comment-50079-info" class="comment-info">
<span class="comment-age">(08 Jun '16, 08:39)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="50082"></span>
<div id="comment-50082" class="comment">
<div id="post-50082-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes it would look probably messy, but the current geometry (with its 3 routes joining at one point and separating again) already looks messy. Not sharing ways would fix the routing, and arguably match reallity better.</p>
</div>
<div id="comment-50082-info" class="comment-info">
<span class="comment-age">(08 Jun '16, 12:02)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50062-form-container" class="comment-form-container">
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

