+++
type = "question"
title = "A* algorithm with OSM"
description = '''I want to implement an A* Search Algorithm with OSM, but how can I get the coordinates just from the streets, not from the houses etc? And how can I get the neighbor&#x27;s coordinates from this specific street coordinate? How can I identify crossroads? Does someone have an idea? I need this to trace a r...'''
date = "2013-07-21T03:02:00Z"
lastmod = "2013-07-25T04:57:00Z"
weight = 24397
keywords = [ "api", "xapi" ]
aliases = [ "/questions/24397" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [A\* algorithm with OSM](/questions/24397/a-algorithm-with-osm)

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
<span id="post-24397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24397-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to implement an A* Search Algorithm with OSM, but how can I get the coordinates just from the streets, not from the houses etc? And how can I get the neighbor's coordinates from this specific street coordinate? How can I identify crossroads? Does someone have an idea? I need this to trace a route, but using my own algorithm *Coordinates= Latitude,Longitude</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '13, 03:02</strong></p>
<img src="https://secure.gravatar.com/avatar/fc2465c602afc28e2b926c36282d17c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user&#39;s gravatar image" />
<p><span>user</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '13, 01:24</strong> </span></p>
</div>
</div>
<div id="comments-container-24397" class="comments-container">
&#10;</div>
<div id="comment-tools-24397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24397-form-container" class="comment-form-container">
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

<span id="24407"></span>

<div id="answer-container-24407" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24407-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to read up on the basics of the OSM data model, e.g. <a href="http://wiki.openstreetmap.org/wiki/Data_model">on the Wiki</a>. This will give you an idea of how to identify what is a street. You will then be able to process an OSM data set and export streets only, or identify crossroads. Finding neighbour's coordinates is a simple geometric problem. Many people will have "an idea" about this but the space here is too short to explain it all! It is possible that importing OSM data into a spatial database (e.g. imposm, osm2pgsql - read other answers about these in this help system) will help you, since you can then query the database for geometries or things like nearest neighbours.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '13, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24407" class="comments-container">
<span id="24458"></span>
<div id="comment-24458" class="comment">
<div id="post-24458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how can I get the neighbor's coordinates from a specific street coordinate?</p>
</div>
<div id="comment-24458-info" class="comment-info">
<span class="comment-age">(22 Jul '13, 18:20)</span> <span class="comment-user userinfo">user</span>
</div>
</div>
<span id="24468"></span>
<div id="comment-24468" class="comment">
<div id="post-24468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to download the spatial database? I can't do this using HTTP request?</p>
</div>
<div id="comment-24468-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 03:58)</span> <span class="comment-user userinfo">user</span>
</div>
</div>
<span id="24474"></span>
<div id="comment-24474" class="comment">
<div id="post-24474-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>To do anything directly with the OSM data (such as routing) you'll almost certainly want to download an extract of the data (such as from one of the links <a href="http://wiki.openstreetmap.org/wiki/Extract">here</a>) first.</p>
</div>
<div id="comment-24474-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 09:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24475"></span>
<div id="comment-24475" class="comment">
<div id="post-24475-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You have to download the data and prepare it in a suitable fashion. You cannot use an API for what you want to do because you need access to much more data than you can download from the API, and your algorithm would be terribly slow. Getting the neighbour's coordinate is a geometric problem that e.g. a PostGIS database would solve for you (search the web for "nearest point postgis" or so).</p>
</div>
<div id="comment-24475-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 09:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="24548"></span>
<div id="comment-24548" class="comment">
<div id="post-24548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, I'm using PostGis with Osm2pgsql schema now, but it's not the nearest point, I need of all points around. look this image <a href="http://www.policyalmanac.org/games/aStarT3.jpg">Here</a>, the green square is my current location and the red square is the destination, so, How can I represent these squares on osm2pgsql schema? line, point, polygon or roads? and the main question is: how to get the squares around of my current location?</p>
</div>
<div id="comment-24548-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 04:57)</span> <span class="comment-user userinfo">user</span>
</div>
</div>
</div>
<div id="comment-tools-24407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24407-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24461"></span>

<div id="answer-container-24461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24461-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe there are some hints from opensource solutions from <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '13, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-24461" class="comments-container">
<span id="24467"></span>
<div id="comment-24467" class="comment">
<div id="post-24467-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It was helpful thanks, but I didn't find anything that solved my problem.</p>
</div>
<div id="comment-24467-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 03:55)</span> <span class="comment-user userinfo">user</span>
</div>
</div>
</div>
<div id="comment-tools-24461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24461-form-container" class="comment-form-container">
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

