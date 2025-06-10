+++
type = "question"
title = "Get distance (in km) from a location to many other locations."
description = '''Here is what I need to do: on a mobile application, get the road distance in km from the user location to all nearby hospitals and clinics. I am looking for a free solution that will accept a high number of queries. I saw the Project OSRM server API and find it very interesting. However, the number ...'''
date = "2015-08-31T20:51:00Z"
lastmod = "2015-09-01T17:15:00Z"
weight = 45004
keywords = [ "mobile", "distance", "api", "km", "osrm" ]
aliases = [ "/questions/45004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get distance (in km) from a location to many other locations.](/questions/45004/get-distance-in-km-from-a-location-to-many-other-locations)

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
<span id="post-45004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here is what I need to do: on a mobile application, get the road distance in km from the user location to all nearby hospitals and clinics. I am looking for a free solution that will accept a high number of queries.</p>
<p>I saw the Project OSRM server API and find it very interesting. However, the number of distances needed by user is too high for individual queries and the "table" service delivers travel time instead of distance length.</p>
<p>An API would be ideal but I am open to installing a local version of openstreetmap on the server for internal queries. Sadly, I am rather unsure how to proceed with that.</p>
<p>Thank you for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-km" rel="tag" title="see questions tagged &#39;km&#39;">km</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '15, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/678f324d0992002ba025c366d605e9ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc%20Perreault&#39;s gravatar image" />
<p><span>Marc Perreault</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc Perreault has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45004" class="comments-container">
<span id="45005"></span>
<div id="comment-45005" class="comment">
<div id="post-45005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Marc, try to inform or create cooperation with the clinics and hospitals. Just to avoid needles journeys with sick emergency patients to a nearby hospital that has room nor bed four your patient.</p>
</div>
<div id="comment-45005-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 21:26)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="45006"></span>
<div id="comment-45006" class="comment">
<div id="post-45006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is actually the point of this application. It finds the hospitals and clinics nearest to your location and show how full they are. Right now, it calculates that distance using crow flight. This create obvious problems in cases where the hospital is right on the other side of a river but there are no nearby bridges or anything like that.</p>
</div>
<div id="comment-45006-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 21:57)</span> <span class="comment-user userinfo">Marc Perreault</span>
</div>
</div>
</div>
<div id="comment-tools-45004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45004-form-container" class="comment-form-container">
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

<span id="45015"></span>

<div id="answer-container-45015" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45015-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can install OSRM on your own server and feed a "planet extract" (= OpenStreetMap data for one country or region) into it. You can then tweak the maximum grid size returned by OSRM's table service.</p>
<p>To get distance rather than travel time, you will (currently) need to alter the Lua speed profile used by OSRM, such that all roads have the same speed. This will, of course, mean that the shortest route is found rather than the fastest. There's an open issue to show distances in the OSRM table call by default: <a href="https://github.com/Project-OSRM/osrm-backend/issues/544">https://github.com/Project-OSRM/osrm-backend/issues/544</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '15, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '15, 16:09</strong> </span></p>
</div>
</div>
<div id="comments-container-45015" class="comments-container">
<span id="45016"></span>
<div id="comment-45016" class="comment">
<div id="post-45016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer, I will check into it.</p>
</div>
<div id="comment-45016-info" class="comment-info">
<span class="comment-age">(01 Sep '15, 17:15)</span> <span class="comment-user userinfo">Marc Perreault</span>
</div>
</div>
</div>
<div id="comment-tools-45015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45015-form-container" class="comment-form-container">
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

