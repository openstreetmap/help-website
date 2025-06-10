+++
type = "question"
title = "How to find out coordinates of route/road?"
description = '''I want to know that if it is possible to find out the coordinates of route between two positions. eg. if i have starting and ending position and osm suggests a path, but also provide the gps coordinates of route/waypoint.'''
date = "2019-09-25T13:13:00Z"
lastmod = "2019-10-03T07:47:00Z"
weight = 70914
keywords = [ "python", "osmapi_python", "osmpythontools", "coordinates" ]
aliases = [ "/questions/70914" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find out coordinates of route/road?](/questions/70914/how-to-find-out-coordinates-of-routeroad)

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
<span id="post-70914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70914-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to know that if it is possible to find out the coordinates of route between two positions. eg. if i have starting and ending position and osm suggests a path, but also provide the gps coordinates of route/waypoint.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-osmpythontools" rel="tag" title="see questions tagged &#39;osmpythontools&#39;">osmpythontools</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '19, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/45c1cced3ea049e72e23496b4715be45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsaadnet&#39;s gravatar image" />
<p><span>vsaadnet</span><br />
<span class="score" title="45 reputation points">45</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsaadnet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70914" class="comments-container">
&#10;</div>
<div id="comment-tools-70914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70914-form-container" class="comment-form-container">
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

<span id="70915"></span>

<div id="answer-container-70915" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70915-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vsaadnet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you want is a routing engine. That's a server to which you send a start and end location, and get back a - textual or geometric - route description. There is free software to do that, e.g. "graphhopper" and "OSRM", so you can set up a server yourself. If you just need a few, and not thousands, of routes, you can use at graphhopper.com or routing.openstreetmap.de. Note that there are many possible routes between two points, and these servers will usually try to find the fastest but can also be parameterised differently.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '19, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70915" class="comments-container">
<span id="70925"></span>
<div id="comment-70925" class="comment">
<div id="post-70925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was able to use graphhopper and extract path coordinates, but can you guide me about how i can use these points to plot a path on google maps or any other engine using Python</p>
</div>
<div id="comment-70925-info" class="comment-info">
<span class="comment-age">(26 Sep '19, 05:56)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
<span id="70926"></span>
<div id="comment-70926" class="comment">
<div id="post-70926-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could save the coordinates as a GeoJSON file and upload it to umap.openstreetmap.fr to make it visible.</p>
</div>
<div id="comment-70926-info" class="comment-info">
<span class="comment-age">(26 Sep '19, 07:26)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="71020"></span>
<div id="comment-71020" class="comment">
<div id="post-71020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you for your guidance, I just checked out how OSRM is actually working, One issue I am still facing is an updated and reliable source to follow, on how to setup my own server in ubuntu, can you help me with that?</p>
</div>
<div id="comment-71020-info" class="comment-info">
<span class="comment-age">(03 Oct '19, 07:47)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
</div>
<div id="comment-tools-70915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70915-form-container" class="comment-form-container">
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

