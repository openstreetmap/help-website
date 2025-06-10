+++
type = "question"
title = "Ferry route not found for motor_vehicle"
description = '''I have a route like this: https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;amp;route=52.85652%2C5.70547%3B53.38942%2C5.30609 It says a route between the two points cannot be found. However, when I look at the ferry route: https://www.openstreetmap.org/way/40118831 It says: motor_vehic...'''
date = "2023-06-26T07:33:00Z"
lastmod = "2023-07-04T08:56:00Z"
weight = 87392
keywords = [ "ferry", "motor_vehicle" ]
aliases = [ "/questions/87392" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ferry route not found for motor_vehicle](/questions/87392/ferry-route-not-found-for-motor_vehicle)

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
<span id="post-87392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87392-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a route like this:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=52.85652%2C5.70547%3B53.38942%2C5.30609">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=52.85652%2C5.70547%3B53.38942%2C5.30609</a></p>
<p>It says a route between the two points cannot be found. However, when I look at the ferry route:</p>
<p><a href="https://www.openstreetmap.org/way/40118831">https://www.openstreetmap.org/way/40118831</a></p>
<p>It says: motor_vehicles:yes</p>
<p>The route only seems to work by bicycle, not even on foot, while that also says yes. Am I missing something here, or is this an issue with OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ferry" rel="tag" title="see questions tagged &#39;ferry&#39;">ferry</span> <span class="post-tag tag-link-motor_vehicle" rel="tag" title="see questions tagged &#39;motor_vehicle&#39;">motor_vehicle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '23, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1562f208082e6af0e48be53864749019?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JesseKoper&#39;s gravatar image" />
<p><span>JesseKoper</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JesseKoper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87392" class="comments-container">
&#10;</div>
<div id="comment-tools-87392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87392-form-container" class="comment-form-container">
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

<span id="87394"></span>

<div id="answer-container-87394" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87394-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JesseKoper has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ferry route looks fine but various elements leading to or from the ferry route don't.</p>
<p>There is a <a href="https://www.openstreetmap.org/node/9804585643">gate</a> that doesn't have any access tags. Many routers treat this as <code>access=no</code>. Other gates do have <code>access=permissive</code> set instead.</p>
<p>There is a <a href="https://www.openstreetmap.org/way/463535985">way</a> that has a <code>foot=no</code> tag. The <a href="https://www.openstreetmap.org/way/555811659">adjacent way</a> has <code>access=no</code> with <code>bicycle=yes</code> set but no <code>foot=yes</code>. It also has a <a href="https://www.openstreetmap.org/node/5362039292">gate</a> with missing access tags (this also applies to other gates in this area, like <a href="https://www.openstreetmap.org/node/1286942350">this one</a> and the others next to it).</p>
<p>Try to fix all those access tags and the routing will probably work. Keep in mind that routers take quite a while to update their data (days, sometimes even weeks).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '23, 08:31</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '23, 08:33</strong> </span></p>
</div>
</div>
<div id="comments-container-87394" class="comments-container">
<span id="87395"></span>
<div id="comment-87395" class="comment">
<div id="post-87395-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll give it a try!</p>
</div>
<div id="comment-87395-info" class="comment-info">
<span class="comment-age">(26 Jun '23, 10:50)</span> <span class="comment-user userinfo">JesseKoper</span>
</div>
</div>
<span id="87403"></span>
<div id="comment-87403" class="comment">
<div id="post-87403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've made some changes like you suggested, this seems to work since I can now use the following route which did not work before as I recall: <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=53.1752%2C5.4142%3B53.3892%2C5.3056#map=11/53.2820/5.2879">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=53.1752%2C5.4142%3B53.3892%2C5.3056#map=11/53.2820/5.2879</a></p>
<p>I need this route to work for GraphHopper specifically though, is this something that just takes time to process for different systems, or is it likely there is a difference between the two for road acceptance that causes this?</p>
</div>
<div id="comment-87403-info" class="comment-info">
<span class="comment-age">(28 Jun '23, 21:37)</span> <span class="comment-user userinfo">JesseKoper</span>
</div>
</div>
<span id="87404"></span>
<div id="comment-87404" class="comment">
<div id="post-87404-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The time it takes to update the routing data is different for each service. I don't know the update interval of OSRM, however, it is not unusual if it takes a little bit longer than others.</p>
</div>
<div id="comment-87404-info" class="comment-info">
<span class="comment-age">(29 Jun '23, 11:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="87427"></span>
<div id="comment-87427" class="comment">
<div id="post-87427-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, it's working now!</p>
</div>
<div id="comment-87427-info" class="comment-info">
<span class="comment-age">(04 Jul '23, 08:56)</span> <span class="comment-user userinfo">JesseKoper</span>
</div>
</div>
</div>
<div id="comment-tools-87394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87394-form-container" class="comment-form-container">
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

