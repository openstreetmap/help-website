+++
type = "question"
title = "Given relation ID, get ways with role and nodes fields"
description = '''I have a relation, and need to get its ways along with role (inner/outer) and node IDs. If I make this query: [out:json]; rel(16357218); out geom; I get type, ref, role, geometry for each member (but no nodes IDs). If I make this query: [out:json]; rel(16357218); way(r); out geom; I get nodes for ea...'''
date = "2023-09-22T06:54:00Z"
lastmod = "2023-09-22T08:38:00Z"
weight = 87864
keywords = [ "ways", "nodes", "role", "json", "relations" ]
aliases = [ "/questions/87864" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Given relation ID, get ways with role and nodes fields](/questions/87864/given-relation-id-get-ways-with-role-and-nodes-fields)

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
<span id="post-87864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87864-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a relation, and need to get its ways along with role (inner/outer) and node IDs.</p>
<p>If I make this query:</p>
<p><code>[out:json]; rel(16357218); out geom;</code></p>
<p>I get <code>type</code>, <code>ref</code>, <code>role</code>, <code>geometry</code> for each member (but no nodes IDs).</p>
<p>If I make this query:</p>
<p><code>[out:json]; rel(16357218); way(r); out geom;</code></p>
<p>I get <code>nodes</code> for each way, but no <code>role</code>.</p>
<p>How can I get both fields for each way, given relation ID?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-role" rel="tag" title="see questions tagged &#39;role&#39;">role</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '23, 06:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c66ea5bac8eabd263857dc99dc190b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oleg%20V9&#39;s gravatar image" />
<p><span>Oleg V9</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oleg V9 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87864" class="comments-container">
&#10;</div>
<div id="comment-tools-87864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87864-form-container" class="comment-form-container">
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

<span id="87865"></span>

<div id="answer-container-87865" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87865-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved this issue with the following query:</p>
<p><code>[out:json]; rel(16357218); out; way(r); out geom;</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '23, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c66ea5bac8eabd263857dc99dc190b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oleg%20V9&#39;s gravatar image" />
<p><span>Oleg V9</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oleg V9 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87865" class="comments-container">
&#10;</div>
<div id="comment-tools-87865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87865-form-container" class="comment-form-container">
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

