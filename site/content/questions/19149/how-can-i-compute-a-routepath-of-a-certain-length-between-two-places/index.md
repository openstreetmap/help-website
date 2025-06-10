+++
type = "question"
title = "How can I compute a route/path of a certain length between two places?"
description = '''Given two places in a specific region, how can I compute a path that is of certain distance (the distance is given as a parameter) which connects the two places. The resulting path should ideally be composed of roads that are visited no more than once. I have learnt that this problem can be seen as ...'''
date = "2013-01-16T23:28:00Z"
lastmod = "2013-01-17T00:44:00Z"
weight = 19149
keywords = [ "path", "route", "map", "graph" ]
aliases = [ "/questions/19149" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I compute a route/path of a certain length between two places?](/questions/19149/how-can-i-compute-a-routepath-of-a-certain-length-between-two-places)

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
<span id="post-19149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19149-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given two places in a specific region, how can I compute a path that is of certain distance (the distance is given as a parameter) which connects the two places. The resulting path should ideally be composed of roads that are visited no more than once.</p>
<p>I have learnt that this problem can be seen as a graph problem where the roads in the map represent the edges of the graph and the intersection/junctions represent the nodes of the graph. From this we can simplify the problem to finding a path of certain length for any two nodes in the graph.</p>
<p>One of my approaches to this problem can be broken into two steps:</p>
<ul>
<li>Finding the shortest path between the two nodes (using A* or a similar algorithm).</li>
<li>Extending/Expanding the shortest path that is returned from A* so that it's long enough.</li>
</ul>
<p>Now, I am not exactly sure if this approach is worth pursuing or if a better approach exists? Also, I've not come across any methods that would allow me to expand the path - are there any specific techniques that can achieve this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '13, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/361e0b98020ca3f3d7db7baa2ec6c590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sadeer&#39;s gravatar image" />
<p><span>Sadeer</span><br />
<span class="score" title="176 reputation points">176</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sadeer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19149" class="comments-container">
&#10;</div>
<div id="comment-tools-19149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19149-form-container" class="comment-form-container">
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

<span id="19150"></span>

<div id="answer-container-19150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19150-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Routing#Developers">https://wiki.openstreetmap.org/wiki/Routing#Developers</a> may be of interest for you, if you did not know</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '13, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-19150" class="comments-container">
&#10;</div>
<div id="comment-tools-19150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19150-form-container" class="comment-form-container">
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

