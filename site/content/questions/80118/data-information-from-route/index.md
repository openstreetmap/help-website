+++
type = "question"
title = "Data information from route"
description = '''I need to export data information (max speed limit, highway typology, surface typology) from a route selected.  The route would be exported from the navigator system, which would return the list of waypoints.  My idea is that all the waypoints would be connected and make the several ways of the rout...'''
date = "2021-05-11T11:54:00Z"
lastmod = "2021-05-11T14:53:00Z"
weight = 80118
keywords = [ "opendata", "highways", "route" ]
aliases = [ "/questions/80118" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Data information from route](/questions/80118/data-information-from-route)

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
<span id="post-80118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80118-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to export data information (max speed limit, highway typology, surface typology) from a route selected. The route would be exported from the navigator system, which would return the list of waypoints. My idea is that all the waypoints would be connected and make the several ways of the route. Then from the ways, I extract the information. But the problem is that I don't have any idea how to manage the problem. There's a web app, called brouter, that in general do what I would to obtain. I will appreciate every help.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span> <span class="post-tag tag-link-highways" rel="tag" title="see questions tagged &#39;highways&#39;">highways</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '21, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/78058cda447f983db7a442d3cbbdd456?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Francescogrillo&#39;s gravatar image" />
<p><span>Francescogrillo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Francescogrillo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80118" class="comments-container">
<span id="80122"></span>
<div id="comment-80122" class="comment">
<div id="post-80122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe to sort out the problem a bit. This is what I understood. Correct me if I am wrong.</p>
<ol>
<li>You have a route defined by waypoints.</li>
<li>Now you need to find the IDs of all the OSM ways the route is following.</li>
<li>You want to extract certain information (max speed limit, highway type, surface, ...) from those ways.</li>
</ol>
</div>
<div id="comment-80122-info" class="comment-info">
<span class="comment-age">(11 May '21, 13:28)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="80124"></span>
<div id="comment-80124" class="comment">
<div id="post-80124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is the idea. For example, this is what I'd obtain (see the Data section), obviously without this web interface. <a href="http://brouter.de/brouter-web/#map=10/45.1360/7.1205/standard,route-quality&amp;lonlats=7.017349,45.116177;7.330383,45.119084">http://brouter.de/brouter-web/#map=10/45.1360/7.1205/standard,route-quality&amp;lonlats=7.017349,45.116177;7.330383,45.119084</a></p>
</div>
<div id="comment-80124-info" class="comment-info">
<span class="comment-age">(11 May '21, 14:53)</span> <span class="comment-user userinfo">Francescogrillo</span>
</div>
</div>
</div>
<div id="comment-tools-80118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80118-form-container" class="comment-form-container">
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

<span id="80120"></span>

<div id="answer-container-80120" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, you should probably use <a href="https://overpass-turbo.eu/">overpass-turbo</a></p>
<p>If you want a CSV, try this with NNN = the ID of your route, and you can add in the first line any tag you want to see :</p>
<pre><code>[out:csv(::&quot;id&quot;, name, highway, maxspeed)];
relation(NNN);
way(r); out meta;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '21, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a588fbc312ece948db9faa4cc02b40de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zorglubu&#39;s gravatar image" />
<p><span>zorglubu</span><br />
<span class="score" title="324 reputation points">324</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zorglubu has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-80120" class="comments-container">
<span id="80121"></span>
<div id="comment-80121" class="comment">
<div id="post-80121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks, I'll try it. But the problem is that I don't know the ID of my route, I think.</p>
</div>
<div id="comment-80121-info" class="comment-info">
<span class="comment-age">(11 May '21, 12:20)</span> <span class="comment-user userinfo">Francescogrillo</span>
</div>
</div>
<span id="80123"></span>
<div id="comment-80123" class="comment">
<div id="post-80123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you post a link OSM with a road belonging to this route, and its name ?</p>
</div>
<div id="comment-80123-info" class="comment-info">
<span class="comment-age">(11 May '21, 14:02)</span> <span class="comment-user userinfo">zorglubu</span>
</div>
</div>
</div>
<div id="comment-tools-80120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80120-form-container" class="comment-form-container">
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

