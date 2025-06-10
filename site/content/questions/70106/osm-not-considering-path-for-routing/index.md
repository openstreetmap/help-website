+++
type = "question"
title = "OSM not considering path for routing"
description = '''I&#x27;m referring to this route planning result: https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;amp;route=54.46938%2C9.09168%3B54.46745%2C9.09299#map=18/54.46915/9.09350 In the south of the housing area where the start point is there is an abandoned railway - of which a part was conve...'''
date = "2019-07-17T06:39:00Z"
lastmod = "2019-07-17T09:13:00Z"
weight = 70106
keywords = [ "path", "routing" ]
aliases = [ "/questions/70106" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [OSM not considering path for routing](/questions/70106/osm-not-considering-path-for-routing)

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
<span id="post-70106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm referring to this route planning result: <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=54.46938%2C9.09168%3B54.46745%2C9.09299#map=18/54.46915/9.09350">https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=54.46938%2C9.09168%3B54.46745%2C9.09299#map=18/54.46915/9.09350</a></p>
<p>In the south of the housing area where the start point is there is an abandoned railway - of which a part was converted to a path. I did the according change in OSM (Way: 704741047) and added the connection path (Way: 704741048) between the housing area and the new path (former railway). However this seems not to be considered for route planning. I'm new to OSM, did I do something wrong connecting the ways?</p>
<p><img src="https://i.ibb.co/d0xDGkm/Screenshot-2019-07-17-at-07-34-24.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '19, 06:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e127393545863834c3adceca92cb1499?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smichaelsen&#39;s gravatar image" />
<p><span>smichaelsen</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smichaelsen has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '19, 06:47</strong> </span></p>
</div>
</div>
<div id="comments-container-70106" class="comments-container">
&#10;</div>
<div id="comment-tools-70106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70106-form-container" class="comment-form-container">
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

<span id="70107"></span>

<div id="answer-container-70107" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70107-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smichaelsen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I tested your route with the routing plugin of JOSM and it produced the route as expected. So there is nothing wrong with your mapping. It maybe that the router you used does not have up to date data or is lacking in its performance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '19, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-70107" class="comments-container">
<span id="70108"></span>
<div id="comment-70108" class="comment">
<div id="post-70108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I assumed since the changes are immediately displayed on openstreetmap.org it will also directly be reflected in the routing used there. This seems not to be the case. Thanks for your response!</p>
</div>
<div id="comment-70108-info" class="comment-info">
<span class="comment-age">(17 Jul '19, 07:40)</span> <span class="comment-user userinfo">smichaelsen</span>
</div>
</div>
</div>
<div id="comment-tools-70107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70107-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70111"></span>

<div id="answer-container-70111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70111-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi smichaelsen,</p>
<p>It should have worked as expected with just a little patience. Please have a look at this example of routing on a so called unset path just to the east of yours (tagged as highway=path surface=ground) :- <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=54.46766%2C9.09774%3B54.46794%2C9.10003#map=17/54.46771/9.09767">https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=54.46766%2C9.09774%3B54.46794%2C9.10003#map=17/54.46771/9.09767</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '19, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-70111" class="comments-container">
&#10;</div>
<div id="comment-tools-70111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70111-form-container" class="comment-form-container">
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

