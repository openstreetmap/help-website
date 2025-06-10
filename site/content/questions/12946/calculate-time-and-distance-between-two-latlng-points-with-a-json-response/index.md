+++
type = "question"
title = "Calculate time and distance between two LatLng points with a JSON response"
description = '''I want to know the distance and the time that is between two points. They would be a latitude and longitude coordenates, and i need a JSON or equivalent type response, because I want to save this information, and i need to make it a few times. i have being looking in mapquest and in cloud made, but ...'''
date = "2012-05-25T09:14:00Z"
lastmod = "2012-05-25T15:13:00Z"
weight = 12946
keywords = [ "latitude", "distance", "routing", "longitude", "time" ]
aliases = [ "/questions/12946" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Calculate time and distance between two LatLng points with a JSON response](/questions/12946/calculate-time-and-distance-between-two-latlng-points-with-a-json-response)

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
<span id="post-12946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12946-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to know the distance and the time that is between two points. They would be a latitude and longitude coordenates, and i need a JSON or equivalent type response, because I want to save this information, and i need to make it a few times.</p>
<p>i have being looking in mapquest and in cloud made, but i cant find the way to do it with a latitude and longitude point, only with a street name.</p>
<p>Any Idea? A lot of thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '12, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/363fa1cba3ca360b0259c51adb003c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dreamcacher&#39;s gravatar image" />
<p><span>Dreamcacher</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dreamcacher has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12946" class="comments-container">
&#10;</div>
<div id="comment-tools-12946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12946-form-container" class="comment-form-container">
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

<span id="12947"></span>

<div id="answer-container-12947" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12947-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dreamcacher has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This can easily be done via CloudMade which accepts lat/lon as start, end and intermediate points, just take a look at the <a href="http://developers.cloudmade.com/projects/routing-http-api/examples">Routing HTTP API Examples</a>. In fact, it is even more work to do it with an address instead of lat/lon :).</p>
<p>As a fast and open alternative you can also use <a href="http://project-osrm.org/">OSRM</a> which also offers an <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Server-api">API</a> to its routing service with JSON responses. It only provides routing for cars so far, but is actively developed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '12, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '12, 10:32</strong> </span></p>
</div>
</div>
<div id="comments-container-12947" class="comments-container">
<span id="12948"></span>
<div id="comment-12948" class="comment">
<div id="post-12948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it's a good option, but i need the route by walking and with car, and this looks like only is available in the car option, but it's a great point to start.</p>
<p>Thanks!</p>
</div>
<div id="comment-12948-info" class="comment-info">
<span class="comment-age">(25 May '12, 10:32)</span> <span class="comment-user userinfo">Dreamcacher</span>
</div>
</div>
<span id="12949"></span>
<div id="comment-12949" class="comment">
<div id="post-12949-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, please just take a look at the link I provided. CloudMade allows you to choose the route type between car, foot and bicycle.</p>
</div>
<div id="comment-12949-info" class="comment-info">
<span class="comment-age">(25 May '12, 10:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="12950"></span>
<div id="comment-12950" class="comment">
<div id="post-12950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>oh! i'm sorry, i saw the route_type_modifier (modifier of the route type, for now only valid value is "shortest" for route type "car") and i didnt see anymore ^^</p>
<p>but you are right in route_type (type of the route ("car", "foot", "bicycle")) appears what you say</p>
<p>A lot of thanks!</p>
</div>
<div id="comment-12950-info" class="comment-info">
<span class="comment-age">(25 May '12, 10:49)</span> <span class="comment-user userinfo">Dreamcacher</span>
</div>
</div>
<span id="12952"></span>
<div id="comment-12952" class="comment">
<div id="post-12952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're welcome :)</p>
</div>
<div id="comment-12952-info" class="comment-info">
<span class="comment-age">(25 May '12, 15:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12947-form-container" class="comment-form-container">
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

