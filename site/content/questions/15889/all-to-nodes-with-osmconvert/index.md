+++
type = "question"
title = "All to nodes with OSMConvert?"
description = '''I am using osmconvert to filter OSM data and convert all the ways to nodes using the --all-to-nodes parameter. When creating a new node from a way it adds 10^15 to the id of the way to make the new node&#x27;s id. For what I want to use the data, I will never need to handle any ways and so was wondering ...'''
date = "2012-09-07T15:41:00Z"
lastmod = "2012-09-07T15:50:00Z"
weight = 15889
keywords = [ "to", "osmconvert", "nodes", "all" ]
aliases = [ "/questions/15889" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [All to nodes with OSMConvert?](/questions/15889/all-to-nodes-with-osmconvert)

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
<span id="post-15889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15889-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using osmconvert to filter OSM data and convert all the ways to nodes using the --all-to-nodes parameter. When creating a new node from a way it adds 10^15 to the id of the way to make the new node's id. For what I want to use the data, I will never need to handle any ways and so was wondering wether there was a way of making the id of the new node the same as the way it was converted from? I tried to set the offset of the id by using --object-type-offset= and setting it to 0 (thinking that this would add 0 to the id and result in the same id) but this resulted in it defaulting to 10^15 once more. Does anyone know how I can solve this? Thanks, Adam</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-all" rel="tag" title="see questions tagged &#39;all&#39;">all</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '12, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3de18384de812d5ab4814c0d0c7e133d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adsized&#39;s gravatar image" />
<p><span>adsized</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adsized has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15889" class="comments-container">
&#10;</div>
<div id="comment-tools-15889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15889-form-container" class="comment-form-container">
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

<span id="15890"></span>

<div id="answer-container-15890" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15890-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adsized has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nodes, ways and relations use overlapping id spaces, and ids are only unique for a given element type. In other words, it is possible that data contains both a node with the node id 4242 and a completely unrelated way with the way id 4242.</p>
<p>For this reason, it is not a good idea to make the node's id the same as the way it was converted from - there might already be a node using this id.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '12, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '12, 15:51</strong> </span></p>
</div>
</div>
<div id="comments-container-15890" class="comments-container">
&#10;</div>
<div id="comment-tools-15890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15890-form-container" class="comment-form-container">
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

