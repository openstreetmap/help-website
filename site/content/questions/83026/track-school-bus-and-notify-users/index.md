+++
type = "question"
title = "Track School Bus and notify users"
description = '''Hi, I am trying to build a small service for a community school. They have a couple of bus; but they are not punctual. Trying to build a service, where all the stops are mapped out and notify the next 2 stops (or parents that pick up or drop is imminent). Today, most of the time spent by the bus is ...'''
date = "2022-01-09T18:29:00Z"
lastmod = "2022-01-09T22:07:00Z"
weight = 83026
keywords = [ "openstreetmap", "mobile", "notification" ]
aliases = [ "/questions/83026" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Track School Bus and notify users](/questions/83026/track-school-bus-and-notify-users)

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
<span id="post-83026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83026-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to build a small service for a community school. They have a couple of bus; but they are not punctual. Trying to build a service, where all the stops are mapped out and notify the next 2 stops (or parents that pick up or drop is imminent).</p>
<p>Today, most of the time spent by the bus is waiting for the ward or the parent.</p>
<p>I am happy to build something in Java or use an existing tool. Do share your opinions and ideas.</p>
<p>Besides the tracking of the location and notification; is it possible to show the same map to all parents. Like real time tracking?</p>
<p>Summarising the ask:</p>
<ol>
<li><strong>Notify the parents that the bus is x stops away</strong></li>
<li><strong>Sharing the live map (with bus location) to parents</strong></li>
</ol>
<p>Regards, Aldrine</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-notification" rel="tag" title="see questions tagged &#39;notification&#39;">notification</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '22, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/dce34a87265cdeaaa9aefb98f9747a88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aldrine&#39;s gravatar image" />
<p><span>aldrine</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aldrine has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '22, 18:35</strong> </span></p>
</div>
</div>
<div id="comments-container-83026" class="comments-container">
&#10;</div>
<div id="comment-tools-83026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83026-form-container" class="comment-form-container">
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

<span id="83028"></span>

<div id="answer-container-83028" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83028-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is a geo database, what you are looking for is a fleet tracking app or gps tracking app. While there are surely fleet tracking or gps tracking apps (with live mode) that use OpenStreetMap data, this help board here is probably not the best place to find recommendations for those.</p>
<p>To get you started in your quest:</p>
<p>You would need gps trackers (either as hardware or mobile app with a mobile phone in each bus) in the buses that constantly (like every x seconds) transmit their position data to a server, there you would have to snap those position data to roads (osrm could do that) or define some geofencing algorithms to check if the bus is approaching the next stop or have some distance/duration calculations and then display this information on a map with the live data updates, etc.</p>
<p>Now this is a solved problem that is in use daily at companies around the world (taxi corporations, parcel services, food delivery etc.). So if you do start searching for gps tracking/fleet tracking apps, you may find it easier to use one of those solutions than building it all on your own.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '22, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83028" class="comments-container">
&#10;</div>
<div id="comment-tools-83028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83028-form-container" class="comment-form-container">
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

