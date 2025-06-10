+++
type = "question"
title = "Drainage ditch end node connections"
description = '''Regarding this changeset:  I&#x27;ve created a drainage ditch that leads from Shull Road to Tinker Creek. In reality, the concrete making up the drainage ditch is part of the curb of the road, so one could say that the ditch and the road are &quot;connected&quot; (i.e. all water that runs down the road will go int...'''
date = "2020-08-21T03:33:00Z"
lastmod = "2020-08-21T09:49:00Z"
weight = 76248
keywords = [ "nodes", "ditch", "newbie", "waterway" ]
aliases = [ "/questions/76248" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Drainage ditch end node connections](/questions/76248/drainage-ditch-end-node-connections)

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
<span id="post-76248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76248-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Regarding <a href="https://www.openstreetmap.org/changeset/89712031">this changeset</a>:</p>
<ol>
<li>I've created a drainage ditch that leads from Shull Road to Tinker Creek. In reality, the concrete making up the drainage ditch is part of the curb of the road, so one could say that the ditch and the road are "connected" (i.e. all water that runs down the road will go into this ditch). Should I connect the nodes making up the top end of the ditch to the nodes on the road indicating the connection (they're made of the same concrete), even though the center of the ditch structure does not match up with the center of the road?</li>
<li>Should I connect the ending node of the ditch to the line making up the creek indicating the relationship that the water from the ditch flows into the creek, even though the concrete structure of the ditch does not extend into the center of the creek?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-ditch" rel="tag" title="see questions tagged &#39;ditch&#39;">ditch</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '20, 03:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb02a9b67a1b01840d744f6e83127c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winduptoy&#39;s gravatar image" />
<p><span>winduptoy</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winduptoy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Aug '20, 04:11</strong> </span></p>
</div>
</div>
<div id="comments-container-76248" class="comments-container">
&#10;</div>
<div id="comment-tools-76248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76248-form-container" class="comment-form-container">
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

<span id="76253"></span>

<div id="answer-container-76253" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76253-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="winduptoy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The central 'flow lines' of waterways should generally be connected to each other, see the illustration on <a href="https://wiki.openstreetmap.org/wiki/Rivers#River_junctions">the rivers page</a> in the wiki. In this case the lower end should definitely connect to the centreline of the creek. The upper end should also probably be connected to the road as it does drain it, even though roads aren't typically thought of as waterway features.</p>
<p>I should note that the wiki page for <a href="https://wiki.openstreetmap.org/wiki/Tag:waterway=ditch?uselang=en">ditch</a> indicates that it is not usually used for concrete lined waterways. You may find that <a href="https://wiki.openstreetmap.org/wiki/Tag:waterway%3Ddrain"><code>waterway=drain</code></a> is more consistent with the rest of OSM.</p>
<p>There appears to be a discrepancy between the (imported) location of the the creek and the position according to the available imagery (Including Virginia specific imagery). This should probably be investigated and the geometry corrected if the imagery appears to be accurately placed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '20, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76253" class="comments-container">
&#10;</div>
<div id="comment-tools-76253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76253-form-container" class="comment-form-container">
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

