+++
type = "question"
title = "How do I best edit &quot;shared nodes&quot; in Potlatch (e.g. between two polygons)"
description = '''I have some city border polygons that seemingly randomly share some of the points along their edges. Given two polygons that share points, what are the best ways to edit them in Potlatch? The needed operations to clean up such a situation are:  Split: given a shared node, split it into two independe...'''
date = "2011-08-31T06:10:00Z"
lastmod = "2011-08-31T11:54:00Z"
weight = 7465
keywords = [ "potlatch", "nodes", "multipolygon", "josm", "shared" ]
aliases = [ "/questions/7465" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I best edit "shared nodes" in Potlatch (e.g. between two polygons)](/questions/7465/how-do-i-best-edit-shared-nodes-in-potlatch-eg-between-two-polygons)

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
<span id="post-7465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7465-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some city border polygons that seemingly randomly share some of the points along their edges. Given two polygons that share points, what are the best ways to edit them in Potlatch? The needed operations to clean up such a situation are:</p>
<ol>
<li><strong>Split</strong>: given a shared node, split it into two independent nodes.</li>
<li><strong>Merge</strong>: drag a node onto another and have it stick, merging the nodes.</li>
<li><strong>Co-locate</strong>: (<em>rare, mentioned only for symmetry</em>) move two nodes to the exact same spot.</li>
</ol>
<p>I find myself doing a lot of splitting of ways in order to manage (or even to remove) such shared points. I split the way, draw a new segment to connect, then delete the extra nodes so created. Is there a better way? A more obvious way? A way that introduces less un-needed churn?</p>
<p>In JOSM the tools are called disconnect, unglue and join, in the Tools menu.</p>
<p>Note I'm not asking about the wisdom of sharing points: simply the tools question.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-shared" rel="tag" title="see questions tagged &#39;shared&#39;">shared</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '11, 06:10</strong></p>
<img src="https://secure.gravatar.com/avatar/372fabe5d3962d54b0c9474e35a05359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bryce%20C%20Nesbitt&#39;s gravatar image" />
<p><span>Bryce C Nesbitt</span><br />
<span class="score" title="345 reputation points">345</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bryce C Nesbitt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '14, 00:23</strong> </span></p>
</div>
</div>
<div id="comments-container-7465" class="comments-container">
&#10;</div>
<div id="comment-tools-7465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7465-form-container" class="comment-form-container">
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

<span id="7471"></span>

<div id="answer-container-7471" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7471-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bryce C Nesbitt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To join a node to another one underneath it, press J. To unjoin a node, press shift-J. There is no "co-locate" function.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '11, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-7471" class="comments-container">
&#10;</div>
<div id="comment-tools-7471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7471-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7470"></span>

<div id="answer-container-7470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7470-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potlatch has the "Follow" tool (press F) which is useful when you want to draw way/polygon that shares some nodes with another.</p>
<p>While drawing a way you can click on one node of another way, then an adjacent one to indicate direction, and after that each press of F adds a new shared node to your way. (This is probably easier to try than explain!)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '11, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-7470" class="comments-container">
&#10;</div>
<div id="comment-tools-7470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7470-form-container" class="comment-form-container">
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

