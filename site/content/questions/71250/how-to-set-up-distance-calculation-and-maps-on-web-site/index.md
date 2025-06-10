+++
type = "question"
title = "How to set up distance calculation (and maps) on web site"
description = '''Hi, we have a php web app using Google Maps in the moment where you can check for the nearest shop from your location. Then the 10 nearest shops with driving time are offered. The area which has to be covered is about 100 x 400 km, there are about 100 users per day doing this request (so 1000 times ...'''
date = "2019-10-21T10:37:00Z"
lastmod = "2019-10-21T13:31:00Z"
weight = 71250
keywords = [ "distance", "php" ]
aliases = [ "/questions/71250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to set up distance calculation (and maps) on web site](/questions/71250/how-to-set-up-distance-calculation-and-maps-on-web-site)

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
<span id="post-71250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71250-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, we have a php web app using Google Maps in the moment where you can check for the nearest shop from your location. Then the 10 nearest shops with driving time are offered. The area which has to be covered is about 100 x 400 km, there are about 100 users per day doing this request (so 1000 times a distance maxtrix has to be called).</p>
<p>I am just getting started with OSRM, so I have very basic questions:</p>
<ul>
<li>Do I have to - or would it be better - to set up the map on our own (shared) server?</li>
<li>What capacity would I need for our task?</li>
<li>If yes, is there a way to do this just using php? I only came across this <a href="https://datawookie.netlify.com/blog/2017/09/building-a-local-osrm-instance/">https://datawookie.netlify.com/blog/2017/09/building-a-local-osrm-instance/</a> which needs access on Linux, which we don't have in the moment. I found an api on githup, but that seems untouched for many years.</li>
</ul>
<p>So any basic tutorial on how to achieve the task would be very helpful!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '19, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/8ec6fcaf40327c008e65a4dfccab8850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kratz&#39;s gravatar image" />
<p><span>Kratz</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kratz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '19, 19:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span></p>
</div>
</div>
<div id="comments-container-71250" class="comments-container">
&#10;</div>
<div id="comment-tools-71250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71250-form-container" class="comment-form-container">
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

<span id="71255"></span>

<div id="answer-container-71255" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71255-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Installing any routing software on your own server will require command-line access - you certainly won't be able to do it with just PHP.</p>
<p>You may find it easier to use a third-party provider. These include Graphhopper, Geofabrik, and Mapbox. Generally these will run OSRM, Graphhopper or Valhalla, which are all OSM-based routing engines. You can then simply call their API from your PHP script.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '19, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-71255" class="comments-container">
&#10;</div>
<div id="comment-tools-71255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71255-form-container" class="comment-form-container">
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

