+++
type = "question"
title = "Convert a Polygon ( Close way ) to a node with its tags."
description = '''How can I convert a Building/Close way/Polygon to a node in the Center of the Object and hold the object tags (Using JOSM) ??'''
date = "2019-07-10T21:37:00Z"
lastmod = "2019-07-15T11:01:00Z"
weight = 69979
keywords = [ "building", "josm", "convert", "nodes", "tags" ]
aliases = [ "/questions/69979" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Convert a Polygon ( Close way ) to a node with its tags.](/questions/69979/convert-a-polygon-close-way-to-a-node-with-its-tags)

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
<span id="post-69979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69979-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I convert a Building/Close way/Polygon to a node in the Center of the Object and hold the object tags (Using JOSM) ??</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '19, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/8369dd4d51a9d62d4b2f840259fb542e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maher_elgammal&#39;s gravatar image" />
<p><span>maher_elgammal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maher_elgammal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69979" class="comments-container">
&#10;</div>
<div id="comment-tools-69979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69979-form-container" class="comment-form-container">
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

<span id="70081"></span>

<div id="answer-container-70081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70081-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do not understand why one would like to do such thing but there may be situations suggesting such a simplification.</p>
<p>That's not too difficult with JOSM:</p>
<ul>
<li>create an "empty" new node</li>
<li>select the "old" way</li>
<li>copy it with "Ctrl-c"</li>
<li>select the new node</li>
<li>paste the way's propertys into the node with "Shift-Ctrl-V"</li>
<li>add a friendly note Tag to the new node containing "way/nnnnn" with nnnn being the id of the old way. doing this you keep a hint to the history of this object in OSM. I think that is important.</li>
<li>now you may delete the "old" way. (perhaps also containing the id of it in the changeset comment)</li>
</ul>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '19, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/5886e9c0e6c8335f791223fe5cb32590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="village&#39;s gravatar image" />
<p><span>village</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="village has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70081" class="comments-container">
&#10;</div>
<div id="comment-tools-70081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70081-form-container" class="comment-form-container">
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

