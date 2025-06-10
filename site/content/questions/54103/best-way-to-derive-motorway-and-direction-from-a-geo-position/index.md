+++
type = "question"
title = "Best way to derive motorway and direction from a geo position"
description = '''Hi, I&#x27;m trying to find the motorway and direction from a GPS coordinate of a car driving on a motorway in France. For example for [47.980539, 3.190048], I want to be able to determine that the driver is on motorway called A6 towards city called Lyon.  Initially I tried to use the nearest service but...'''
date = "2017-01-17T15:57:00Z"
lastmod = "2017-01-17T16:36:00Z"
weight = 54103
keywords = [ "road_from_coord" ]
aliases = [ "/questions/54103" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to derive motorway and direction from a geo position](/questions/54103/best-way-to-derive-motorway-and-direction-from-a-geo-position)

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
<span id="post-54103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54103-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to find the motorway and direction from a GPS coordinate of a car driving on a motorway in France. For example for [47.980539, 3.190048], I want to be able to determine that the driver is on motorway called A6 towards city called Lyon. Initially I tried to use the nearest service but the data returned is not always populated and I could not trust it. As a result, the only solution I found was to call the route/v1/driving service by feeding it the driver's GPS coordinate and some far GPS position (in my case: close to Spain border). Then from the JSON object returned I take routes[0]-&gt;legs[0]-&gt;steps[0]-&gt;Ref which gives me the motorway on which the user is. Then for direction I use again route/v1/driving to compute the route distance between beginning location of the motorway and driver and then from driver to end of the motorway and I compare it to a the real length of the motorway. If I find a close match for 1 of the 2 directions, I assume the driver is driving in this direction.</p>
<p>It's a bit complicated and not always reliable. Is there a better way to retrieve such information ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-road_from_coord" rel="tag" title="see questions tagged &#39;road_from_coord&#39;">road_from_coord</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '17, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/7998acb6628483825d62dc4f11055d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="06pboivin06&#39;s gravatar image" />
<p><span>06pboivin06</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="06pboivin06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54103" class="comments-container">
&#10;</div>
<div id="comment-tools-54103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54103-form-container" class="comment-form-container">
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

<span id="54110"></span>

<div id="answer-container-54110" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54110-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A single location won't suffice. Ideally you should wait until having obtained multiple locations. Then use these locations to calculate the driving direction and the most plausible way(s) the driver is on.</p>
<p>You can also go through the source of one of the many open source routing engines for OSM. See <a href="https://wiki.openstreetmap.org/wiki/Routing">routing</a> as well as the list of <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">online routers</a> and <a href="https://wiki.openstreetmap.org/wiki/Routing/offline_routers">offline routers</a> for various examples.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54110" class="comments-container">
&#10;</div>
<div id="comment-tools-54110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54110-form-container" class="comment-form-container">
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

