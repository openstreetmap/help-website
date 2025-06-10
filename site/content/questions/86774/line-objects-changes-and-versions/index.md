+++
type = "question"
title = "line objects changes and versions"
description = '''Hello, i recently added a mountain path (highway=path), then i had to correct it by moving slightly some of its nodes (without adding new nodes to it), all this using the editor ID. Something surprises me: if i want to see the details about this &quot;highway&quot; object later on the map, i see only its &quot;ver...'''
date = "2023-02-22T12:30:00Z"
lastmod = "2023-02-24T11:42:00Z"
weight = 86774
keywords = [ "nodes", "version", "lines" ]
aliases = [ "/questions/86774" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [line objects changes and versions](/questions/86774/line-objects-changes-and-versions)

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
<span id="post-86774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86774-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i recently added a mountain path (highway=path), then i had to correct it by moving slightly some of its nodes (without adding new nodes to it), all this using the editor ID.</p>
<p>Something surprises me: if i want to see the details about this "highway" object later on the map, i see only its "version 1". Of course, in my history list of groups of changes, i can find what i did later, but only with a list of the displaced nodes (these nodes have a "version 2" in their history) without any mention of the path, despite when i made these changes, using ID editor, this clearly indicates "modified path" before i send my changes.</p>
<p>So i could change almost totally the appearance of a path, a track or a road (could be some of "my" objects or someone else's line object) and it would not be later very clear to see what happened to it as, when questionning this object from the map, it would only show the date of the previous version, as if nothing had been changed!!!</p>
<p>Of course, if i add only one node to the line, then there is a new version of this line object.</p>
<p>To resume it: ID tells me i modify a line, so why this line object doesn't show a new version for itself?</p>
<p>Thank you for your answers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '23, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/703cb55e76444760fd15e02ac0add178?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eric%20db&#39;s gravatar image" />
<p><span>eric db</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eric db has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86774" class="comments-container">
&#10;</div>
<div id="comment-tools-86774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86774-form-container" class="comment-form-container">
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

<span id="86775"></span>

<div id="answer-container-86775" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86775-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-86775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your observation is correct. Relations are built from ways and nodes; ways are built from nodes; and changing the properties of a member doesn't change the object itself. A way will only receive a new version if you change the list of nodes (by adding or removing nodes), or if you modify its properties (tags). It will not receive a new version if you move the nodes around.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '23, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86775" class="comments-container">
<span id="86799"></span>
<div id="comment-86799" class="comment">
<div id="post-86799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik, i understand this is how the different objects in OSM have been built and defined (even if it is not so intuitive: if i move all the nodes of a road, this road is not considered "modified" despite its aspect will be quite different!). Anyway, ID editor interface is still a bit confusing about this topic: if i edit my previous path by moving 3 nodes for example, ID will tell me "save 1" in the right upper button, and then the mention "Changes(1) Modified Path" on the bottom left before the final upload, and not "save 3" and mentionning 3 modified nodes. Made me think at first, of course, that the path object has been modified! Apart from the interface clarity, the main drawback i found was the difficulty to trace the real history of an object, a line in my case.</p>
</div>
<div id="comment-86799-info" class="comment-info">
<span class="comment-age">(24 Feb '23, 11:42)</span> <span class="comment-user userinfo">eric db</span>
</div>
</div>
</div>
<div id="comment-tools-86775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86775-form-container" class="comment-form-container">
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

