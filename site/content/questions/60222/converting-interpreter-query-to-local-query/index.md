+++
type = "question"
title = "Converting interpreter query to local query."
description = '''I&#x27;m planning on writing a small phone application which will show the users the current street and speed limit, I found that this information is easily accessible on the following link: http://overpass-api.de/api/interpreter?data=[out:json];way(around:10,53.6788398,-1.4992124)[maxspeed];out; But sin...'''
date = "2017-10-22T23:26:00Z"
lastmod = "2017-10-23T14:01:00Z"
weight = 60222
keywords = [ "overpass", "osm3s", "server" ]
aliases = [ "/questions/60222" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Converting interpreter query to local query.](/questions/60222/converting-interpreter-query-to-local-query)

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
<span id="post-60222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60222-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm planning on writing a small phone application which will show the users the current street and speed limit, I found that this information is easily accessible on the following link:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;way(around:10,53.6788398,-1.4992124)%5Bmaxspeed%5D;out;">http://overpass-api.de/api/interpreter?data=[out:json];way(around:10,53.6788398,-1.4992124)[maxspeed];out;</a></p>
<p>But since this will be a real time app and each user will probably ping the server at every 5 seconds, I have concluded that it will be against the current server fair usage limit so I have deployed a local copy to my own server, however I do not want to use the interpreter with Apache I will like to use my own php script which calls osm3s_query but I couldn't find a way to translate above query to work from the command line.</p>
<p>I have read the documentation found here: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#.22around.22_-_finding_something_near_something_else">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#.22around.22_-_finding_something_near_something_else</a> about the around, but it doesn't give any explanation about how to use it with lat/long and creating a bounding box for this feels like an overkill to me.</p>
<p>As question number 2, is there any way to reduce the deployed osm data? I only need street names and speed limits, I do not need everything else, but I need this for the whole globe, and I need to updated it on daily or weekly basis. Again having a full OSM synced to my server fills a huge overkill.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osm3s" rel="tag" title="see questions tagged &#39;osm3s&#39;">osm3s</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '17, 23:26</strong></p>
<img src="https://secure.gravatar.com/avatar/8498a3434038d28b988bae45693a86ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Borconi&#39;s gravatar image" />
<p><span>Borconi</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Borconi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '17, 23:31</strong> </span></p>
</div>
</div>
<div id="comments-container-60222" class="comments-container">
&#10;</div>
<div id="comment-tools-60222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60222-form-container" class="comment-form-container">
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

<span id="60242"></span>

<div id="answer-container-60242" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Never mind, I found the solution here: <a href="/questions/60210/get-around-ways-more-data">https://help.openstreetmap.org/questions/60210/get-around-ways-more-data</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '17, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/8498a3434038d28b988bae45693a86ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Borconi&#39;s gravatar image" />
<p><span>Borconi</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Borconi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60242" class="comments-container">
&#10;</div>
<div id="comment-tools-60242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60242-form-container" class="comment-form-container">
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

