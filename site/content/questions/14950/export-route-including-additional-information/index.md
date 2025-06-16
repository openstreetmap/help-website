+++
type = "question"
title = "Export route including additional information"
description = '''Hi, I would like to generate route data based on OSM that does not only consist of the GPS coordinates in a GPX file but also contains other information like street type and maximum speed. As an example, I would like to define start and endpoint for the route and than get a table in following form: ...'''
date = "2012-08-10T14:29:00Z"
lastmod = "2012-08-13T16:51:00Z"
weight = 14950
keywords = [ "route", "export" ]
aliases = [ "/questions/14950" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export route including additional information](/questions/14950/export-route-including-additional-information)

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
<span id="post-14950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14950-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to generate route data based on OSM that does not only consist of the GPS coordinates in a GPX file but also contains other information like street type and maximum speed. As an example, I would like to define start and endpoint for the route and than get a table in following form:</p>
<p>% node id, lat, lon, ele, way id, highway type, maxspeed,<br />
266572201, 52.4146423, 9.6425588, 98.7, 31140680, primary, 70 ....</p>
<p>What would be the general approach to get such data out of OpenStreetMap?</p>
<p>Thanks for the support, best regards, Maik</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '12, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/25565ea5464068f7d95f5c5dace080a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osmaik&#39;s gravatar image" />
<p><span>osmaik</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osmaik has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-14950" class="comments-container">
&#10;</div>
<div id="comment-tools-14950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14950-form-container" class="comment-form-container">
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

<span id="14952"></span>

<div id="answer-container-14952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14952-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> ... you can convert raw OSM data to CSV data. Define the columns that you need.</p>
<p>Or choose another approach like the numerous opensource solutions you can find in the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Routing">Routing</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '12, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-14952" class="comments-container">
<span id="15016"></span>
<div id="comment-15016" class="comment">
<div id="post-15016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, good hint. My problem is now that using osmconvert with the --all-to-nodes option, it will create a new node ID for each way that will than have a highway type and the maximum speed as properties. This is not what I wanted to have, because the connection between node and way is than lost.</p>
<p>I wanted to have all node properties, that are on my route, in that list and the properties of the street that the route is following should be printed in the line of the referenced node.</p>
<p>In other words, I need the reverse reference. To which way does the current node belong following the given node?</p>
<p>For the Routing topic: sometimes the route can be exported as a GPX file, while for me it would be much better to get the node IDs of my route. So is there a routing service existing that delivers the node IDs or is something like that possible via API?</p>
</div>
<div id="comment-15016-info" class="comment-info">
<span class="comment-age">(13 Aug '12, 12:24)</span> <span class="comment-user userinfo">osmaik</span>
</div>
</div>
<span id="15030"></span>
<div id="comment-15030" class="comment">
<div id="post-15030-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would ask that in one of the OS mailing lists about Developing or Routing ...</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">https://wiki.openstreetmap.org/wiki/Mailing_lists</a></p>
</div>
<div id="comment-15030-info" class="comment-info">
<span class="comment-age">(13 Aug '12, 16:51)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-14952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14952-form-container" class="comment-form-container">
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

