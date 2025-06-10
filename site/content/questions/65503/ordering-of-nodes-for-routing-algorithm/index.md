+++
type = "question"
title = "Ordering of nodes for routing algorithm"
description = '''Hi guys, I&#x27;ve been writing a little Overpass QL script that grabs the way data base on a route of nodes. I&#x27;m doing this by comparing the ways a node is part of with those of the previous node. This means it&#x27;s vital that my foreach loop iterates over the nodes in the way that I&#x27;m providing them. At t...'''
date = "2018-08-22T18:05:00Z"
lastmod = "2018-08-22T18:05:00Z"
weight = 65503
keywords = [ "ordering", "routing", "foreach" ]
aliases = [ "/questions/65503" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ordering of nodes for routing algorithm](/questions/65503/ordering-of-nodes-for-routing-algorithm)

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
<span id="post-65503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I've been writing a little Overpass QL script that grabs the way data base on a route of nodes. I'm doing this by comparing the ways a node is part of with those of the previous node. This means it's vital that my foreach loop iterates over the nodes in the way that I'm providing them. At the moment it's automatically reordering all nodes by if before starting the loop. Any way you guys can see around this? Any help would be greatly appreciated!</p>
<p>/ <em>run to see input nodes node(id:360043069,2864527555,360043065); out;</em> /</p>
<p>node(id:2864527555,360043065) -&gt; .nodes; node(id:360043069); way<a href="bn">highway</a> -&gt; .lastnodeways;</p>
<p>foreach .nodes -&gt; .thisnode ( way<a href="bn.thisnode">highway</a> -&gt; .thisnodeways; ( way.thisnodeways.lastnodeways; .confirmedways; ) -&gt; .confirmedways; .thisnodeways -&gt; .lastnodeways; );</p>
<p>.confirmedways out geom;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ordering" rel="tag" title="see questions tagged &#39;ordering&#39;">ordering</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-foreach" rel="tag" title="see questions tagged &#39;foreach&#39;">foreach</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '18, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/079e3a6cce1a2115c3a107820ee7e132?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gillesgerlo&#39;s gravatar image" />
<p><span>gillesgerlo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gillesgerlo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65503" class="comments-container">
&#10;</div>
<div id="comment-tools-65503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65503-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

