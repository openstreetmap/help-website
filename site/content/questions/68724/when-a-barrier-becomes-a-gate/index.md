+++
type = "question"
title = "When a Barrier becomes a Gate!"
description = '''Fairly new to mapping. I wanted to map locked security gates installed in a side alley previously on a cycle route which are only accessible by key holders.  Initially I mapped a barrier defined as a gate. But I noticed if you move the barrier symbol off and onto the surface of the road, it changed ...'''
date = "2019-04-09T13:43:00Z"
lastmod = "2019-04-09T20:53:00Z"
weight = 68724
keywords = [ "gate", "barrier" ]
aliases = [ "/questions/68724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [When a Barrier becomes a Gate!](/questions/68724/when-a-barrier-becomes-a-gate)

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
<span id="post-68724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68724-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Fairly new to mapping. I wanted to map locked security gates installed in a side alley previously on a cycle route which are only accessible by key holders. Initially I mapped a barrier defined as a gate. But I noticed if you move the barrier symbol off and onto the surface of the road, it changed into a gate symbol which is much more appropriate. I defined access as permissive. Hopefully that will prevent routing access. I welcome any comments? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '19, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/18914f7d5d4b03adbe658877970b77d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Craftycockney&#39;s gravatar image" />
<p><span>Craftycockney</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Craftycockney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68724" class="comments-container">
&#10;</div>
<div id="comment-tools-68724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68724-form-container" class="comment-form-container">
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

<span id="68726"></span>

<div id="answer-container-68726" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68726-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the barrier restricts access to the road its node should always be placed onto the road (so that the symbol changes to a gate). Otherwise a router wouldn't know that the gate belongs on that route.</p>
<p>Additionally, the road behind (between) the gates could also get an access tag (not all routers evaluate the barrier). Make sure to split the way first if the barrier only cuts off part of it.</p>
<p>Please also keep in mind the <a href="https://wiki.openstreetmap.org/wiki/Key:access#Land-based_transportation">access hierarchy</a>. Access=no/private/... locks out everything and everyone. If the road is for example only closed for vehicles but not pedestrians use vehicle=no/private/...</p>
<p>Access=permissive means someone owns the road who could restrict the access if they wanted to but have chosen to leave access open for time being. So a router would probably route over that barrier/road. If you need a key as you described I would tag it as access=private.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '19, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-68726" class="comments-container">
<span id="68737"></span>
<div id="comment-68737" class="comment">
<div id="post-68737-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As far i know permissive means users are permitted. footpath=permissive, bridleway=permissive or residents=permissiveso in this case permissive=key_holders</p>
</div>
<div id="comment-68737-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 20:50)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="68738"></span>
<div id="comment-68738" class="comment">
<div id="post-68738-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If the gate is a barrier to the side route it should on the side route NOT on the road. Otherwise it blocks the road.</p>
</div>
<div id="comment-68738-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 20:53)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-68726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68726-form-container" class="comment-form-container">
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

