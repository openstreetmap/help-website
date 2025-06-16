+++
type = "question"
title = "Can overpass produce neighbouring nodes in a single request?"
description = '''New here, and not so clear on how sets work yet.. I&#x27;m requesting a bunch of ways, and the nodes within these. For each node I&#x27;d like to find the other nodes which are connected via a way as kindly demonstrated here, https://help.openstreetmap.org/questions/71493 However, I was hoping for a way to ca...'''
date = "2021-07-13T20:54:00Z"
lastmod = "2021-07-13T20:54:00Z"
weight = 80948
keywords = [ "overpass", "nodes", "request", "nested" ]
aliases = [ "/questions/80948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can overpass produce neighbouring nodes in a single request?](/questions/80948/can-overpass-produce-neighbouring-nodes-in-a-single-request)

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
<span id="post-80948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>New here, and not so clear on how sets work yet..</p>
<p>I'm requesting a bunch of ways, and the nodes within these. For each node I'd like to find the other nodes which are connected via a way as kindly demonstrated here, <a href="/questions/71493">https://help.openstreetmap.org/questions/71493</a></p>
<p>However, I was hoping for a way to call this on multiple nodes, but having someway of knowing which nodes neighbour which, as opposed to receiving a large set of unordered nodes for the whole group.</p>
<p>Ultimately, in my application, I'm looking to create an array, neighbours[node], which contains a vector of reachable nodes from the said node.</p>
<p>Ideally this will also be filtered this so that it incorporates the oneway tag in regards which nodes are "reachable", i.e.</p>
<p><strong>neighbours[A] = BC</strong> while <strong>neighbours[C] = nil</strong> if nodes <strong>ABC</strong> make up a one way street or roundabout sequence of ways.</p>
<p>Is there any way to do this in a single request which will return some nested or ordered format containing nodes with their neighbours, or does it have to be done with an individual request for each node in order to fill out my array?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-nested" rel="tag" title="see questions tagged &#39;nested&#39;">nested</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '21, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b067c3ab521507c4200c82876330caa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mugwort&#39;s gravatar image" />
<p><span>mugwort</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mugwort has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80948" class="comments-container">
&#10;</div>
<div id="comment-tools-80948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80948-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

