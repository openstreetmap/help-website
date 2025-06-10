+++
type = "question"
title = "On what kind of node should we use the entrance tag?"
description = '''Hello, I&#x27;m trying to add entrance to building in order to be able to use the building as a destination in a routing program. I would thus like to link the surrounding street to the building entrance so that the routing using a dijkstra like algorithm can lead to the entrance immediately. Do you know...'''
date = "2012-10-18T12:30:00Z"
lastmod = "2012-10-18T15:11:00Z"
weight = 16995
keywords = [ "building", "entrance" ]
aliases = [ "/questions/16995" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [On what kind of node should we use the entrance tag?](/questions/16995/on-what-kind-of-node-should-we-use-the-entrance-tag)

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
<span id="post-16995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16995-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to add entrance to building in order to be able to use the building as a destination in a routing program. I would thus like to link the surrounding street to the building entrance so that the routing using a dijkstra like algorithm can lead to the entrance immediately. Do you know if i should add a small path from the road to the building or only add a node at the entrance? How should i set up the relations between the road and the building in order for them to be connected? How should i use the entrance tag in order to make this link?</p>
<p>Thank you for your help,</p>
<p>Matthieu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-entrance" rel="tag" title="see questions tagged &#39;entrance&#39;">entrance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '12, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/355d2bb4db49351bec602325fe7ce468?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mataymans&#39;s gravatar image" />
<p><span>mataymans</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mataymans has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16995" class="comments-container">
&#10;</div>
<div id="comment-tools-16995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16995-form-container" class="comment-form-container">
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

<span id="16996"></span>

<div id="answer-container-16996" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16996-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually, just inserting an entrance node (<a href="http://wiki.openstreetmap.org/wiki/Key:entrance">entrance=yes</a>, or entrance=main/service/... if there are multiple entrances) into the building outline is enough. Routing engines will lead you to the point on a street that is nearest to your target, even without a mapped direct connection. Usually, this produces the desired result.</p>
<p>If you want to work at a very high level of detail, you can also add a path between the street and the entrance (if such a path exists in reality). In that case, the entrance node should be a shared node of that path and the building outline.</p>
<p>There is no need to use any relations for mapping this situation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '12, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Oct '12, 15:16</strong> </span></p>
</div>
</div>
<div id="comments-container-16996" class="comments-container">
&#10;</div>
<div id="comment-tools-16996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16996-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16997"></span>

<div id="answer-container-16997" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Do you know if i should add a small path from the road to the building or only add a node at the entrance?</p>
</blockquote>
<p>You can do that if there really is a path from the road to the building. However, it should not be necessary for routing software. Routing SW will generally just find the road closest to your destination and guide you there, which will probably be enough. So for routing purposes, a node at the entrance is enough.</p>
<blockquote>
<p>How should i set up the relations between the road and the building in order for them to be connected?</p>
</blockquote>
<p>You just add <a href="http://wiki.openstreetmap.org/wiki/Key:addr">addr: tags</a> to the node, with the name of the street. The connection between road and building is then only implicit (by the name of the street). There is also a relation to make this explicit (<a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Street),">http://wiki.openstreetmap.org/wiki/Relations/Proposed/Street),</a> but it's not used frequently.</p>
<blockquote>
<p>How should i use the entrance tag in order to make this link?</p>
</blockquote>
<p>Just create a node which is part of the building, in the location where the entrance is. Then tag it with <code>entrance=yes</code> and with the address information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '12, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-16997" class="comments-container">
&#10;</div>
<div id="comment-tools-16997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16997-form-container" class="comment-form-container">
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

