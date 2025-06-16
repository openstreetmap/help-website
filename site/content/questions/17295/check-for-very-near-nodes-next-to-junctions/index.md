+++
type = "question"
title = "Check for very near nodes next to junctions"
description = '''Is there something that verifies/validates/checks/tests for very near nodes next to junctions? For example, the picture below. See that we have a node that could be removed (or merged) to the node that is already being used at the junction. Visually it is very difficult to see those unnecessary node...'''
date = "2012-10-30T13:39:00Z"
lastmod = "2012-10-30T17:17:00Z"
weight = 17295
keywords = [ "test", "nodes", "validation", "junction", "check" ]
aliases = [ "/questions/17295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Check for very near nodes next to junctions](/questions/17295/check-for-very-near-nodes-next-to-junctions)

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
<span id="post-17295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there something that verifies/validates/checks/tests for very near nodes next to junctions?</p>
<p>For example, the picture below. See that we have a node that could be removed (or merged) to the node that is already being used at the junction. Visually it is very difficult to see those unnecessary nodes that could be removed.</p>
<p>Are there any tools available that could warn us about this?</p>
<p><img src="http://i.imgur.com/bRyCV.png" alt="http://i.imgur.com/bRyCV.png" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-test" rel="tag" title="see questions tagged &#39;test&#39;">test</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '12, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c605758904cf00f577053e4e130f89a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naoliv&#39;s gravatar image" />
<p><span>naoliv</span><br />
<span class="score" title="600 reputation points">600</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naoliv has 3 accepted answers">37%</span></p>
</img>
</div>
</div>
<div id="comments-container-17295" class="comments-container">
&#10;</div>
<div id="comment-tools-17295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17295-form-container" class="comment-form-container">
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

<span id="17299"></span>

<div id="answer-container-17299" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17299-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The extra node there isn't causing any massive problem, so I guess the first thing to say is, this problem is low priority compared to some other problems we detect with automated checks.</p>
<p>In particular "connectivity problems" are more severe. I mean for example if the way on the right hand side there actually stopped short of the junction at the extra node. Such problems are identified by <a href="https://wiki.openstreetmap.org/wiki/Keep_Right">Keep Right</a>, and also shown as fixable little tasks in the awesome new <a href="https://oegeo.wordpress.com/2012/10/29/new-maproulette-challenge-connectivity-bugs/">MapRoulette challenge</a>.</p>
<p>But if this is just a case of one too many nodes, I don't think we have a tool to detect that. It's a problem we see a bit in the TIGER data. It's not just at junctions. We also see too many nodes forming fiddly bits on boundary ways (a larger class of problems where we might say we just need to do some 'simplifying' algorithm) In a way I suppose it's a somewhat subjective choice, whether this node is unnecessary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-17299" class="comments-container">
<span id="17301"></span>
<div id="comment-17301" class="comment">
<div id="post-17301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not that rare to find a way that has useless nodes (it's not specific to crossroads). Not worth hunting them down systematically, but fixing them as we go (like useless tags for example) is usefull. So checking that in the editor's before-upload validator may be the way to go ? Alas, everybody will have a different opinion on which treshold is "correct".</p>
</div>
<div id="comment-17301-info" class="comment-info">
<span class="comment-age">(30 Oct '12, 15:37)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="17304"></span>
<div id="comment-17304" class="comment">
<div id="post-17304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@vincent</span>-de-phily exactly this. Suppose I am editing an area and I would like to also fix some low hanging fruits. It would be good to have a validator to point me where there are such very near nodes that could be merged/fixed.</p>
</div>
<div id="comment-17304-info" class="comment-info">
<span class="comment-age">(30 Oct '12, 16:46)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
<span id="17308"></span>
<div id="comment-17308" class="comment">
<div id="post-17308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>turning off backgound image can help sometimes so set background to none.</p>
</div>
<div id="comment-17308-info" class="comment-info">
<span class="comment-age">(30 Oct '12, 17:08)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="17309"></span>
<div id="comment-17309" class="comment">
<div id="post-17309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it helps, but still not on higher density cities or with a far zoom.</p>
</div>
<div id="comment-17309-info" class="comment-info">
<span class="comment-age">(30 Oct '12, 17:17)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
</div>
<div id="comment-tools-17299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17299-form-container" class="comment-form-container">
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

