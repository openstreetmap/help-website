+++
type = "question"
title = "Draw route"
description = '''Hi, I will be getting a set of lat, longs from the client. I need to connect those points using a free line. I used the polyline feature in the leaflet library. I only get a straight line. I want to draw a line that highlights the road. Thank you.'''
date = "2020-02-10T03:27:00Z"
lastmod = "2020-02-10T11:49:00Z"
weight = 72964
keywords = [ "leaflet" ]
aliases = [ "/questions/72964" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Draw route](/questions/72964/draw-route)

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
<span id="post-72964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I will be getting a set of lat, longs from the client. I need to connect those points using a free line. I used the polyline feature in the leaflet library. I only get a straight line. I want to draw a line that highlights the road.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '20, 03:27</strong></p>
<img src="https://secure.gravatar.com/avatar/01322bb35fae18ef30b3bcff70ab9f5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Poojitha&#39;s gravatar image" />
<p><span>Poojitha</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Poojitha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72964" class="comments-container">
&#10;</div>
<div id="comment-tools-72964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72964-form-container" class="comment-form-container">
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

<span id="72970"></span>

<div id="answer-container-72970" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72970-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get a route following roads between points, you need to use a routing engine.</p>
<p>There are several such engines available that you can query for free for light use. For more intensive use, you will typically need to pay.</p>
<p>Engines you could consider include Graphhopper and OSRM (the best free service for the latter is at <a href="https://routing.openstreetmap.de/about.html">https://routing.openstreetmap.de/about.html</a> ). Typically you will send an AJAX/fetch request to the routing engine server with your lat/lons, and it will return a polyline which you can draw with Leaflet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '20, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72970" class="comments-container">
&#10;</div>
<div id="comment-tools-72970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72970-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72973"></span>

<div id="answer-container-72973" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72973-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the leaflet plugin list, you'll find a <a href="https://leafletjs.com/plugins.html#routing">Routing</a> section.</p>
<p>All these plugins relies on external services for the calculation, but integration with your map should be easy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '20, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-72973" class="comments-container">
&#10;</div>
<div id="comment-tools-72973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72973-form-container" class="comment-form-container">
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

