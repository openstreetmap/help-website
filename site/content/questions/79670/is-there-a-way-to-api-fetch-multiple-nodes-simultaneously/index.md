+++
type = "question"
title = "Is there a way to API fetch multiple nodes simultaneously?"
description = '''I have an array of nodes and am using https://api.openstreetmap.org/api/0.6/node/{node} to get the lng and lat of each node. Is their an easier way to fetch multiple nodes at the same time?'''
date = "2021-04-14T14:52:00Z"
lastmod = "2021-04-14T23:45:00Z"
weight = 79670
keywords = [ "api", "node", "nodes", "javascript", "nodejs" ]
aliases = [ "/questions/79670" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to API fetch multiple nodes simultaneously?](/questions/79670/is-there-a-way-to-api-fetch-multiple-nodes-simultaneously)

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
<span id="post-79670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79670-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an array of nodes and am using <a href="https://api.openstreetmap.org/api/0.6/node/%7Bnode%7D">https://api.openstreetmap.org/api/0.6/node/{node}</a> to get the lng and lat of each node. Is their an easier way to fetch multiple nodes at the same time?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-nodejs" rel="tag" title="see questions tagged &#39;nodejs&#39;">nodejs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '21, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/9e3a09c93f408b1f16f2daa7cae61821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zgivod&#39;s gravatar image" />
<p><span>zgivod</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zgivod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79670" class="comments-container">
&#10;</div>
<div id="comment-tools-79670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79670-form-container" class="comment-form-container">
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

<span id="79678"></span>

<div id="answer-container-79678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79678-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can ask for multiple nodes by ID like this:</p>
<p><a href="https://api.openstreetmap.org/api/0.6/nodes/?nodes=123456700,123456701,123456702">https://api.openstreetmap.org/api/0.6/nodes/?nodes=123456700,123456701,123456702</a></p>
<p>The same command works for just a single node ID as well:</p>
<p><a href="https://api.openstreetmap.org/api/0.6/nodes/?nodes=123456700">https://api.openstreetmap.org/api/0.6/nodes/?nodes=123456700</a></p>
<p>See the API documentation:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:_GET_.2Fapi.2F0.6.2F.5Bnodes.7Cways.7Crelations.5D.3F.23parameters">https://wiki.openstreetmap.org/wiki/API_v0.6#Multi fetch: GET /api/0.6/[nodes|ways|relations]?#parameters</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '21, 23:45</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '21, 01:02</strong> </span></p>
</div>
</div>
<div id="comments-container-79678" class="comments-container">
&#10;</div>
<div id="comment-tools-79678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79678-form-container" class="comment-form-container">
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

