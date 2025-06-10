+++
type = "question"
title = "Why are layers numbered -1 and 1 and is there no other variation ?"
description = '''Is anyone able to explain the use of layers, further then bridge 1, 2, 3 and tunnel -1, -2 ? The rest of the situation is 0, but key nor value anywhere. A bridge over water gets 1, the surrounding area no value but the water lower then the surroundings none either. Whats the logic in this ? And how ...'''
date = "2012-08-11T11:42:00Z"
lastmod = "2012-08-12T09:30:00Z"
weight = 14961
keywords = [ "tunnel", "bridge", "layer", "culvert", "value" ]
aliases = [ "/questions/14961" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why are layers numbered -1 and 1 and is there no other variation ?](/questions/14961/why-are-layers-numbered-1-and-1-and-is-there-no-other-variation)

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
<span id="post-14961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14961-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is anyone able to explain the use of layers, further then bridge 1, 2, 3 and tunnel -1, -2 ? The rest of the situation is 0, but key nor value anywhere. A bridge over water gets 1, the surrounding area no value but the water lower then the surroundings none either. Whats the logic in this ? And how should a culvert beiing tagged, key layer _ value -1 ?</p>
<p>Greetz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-culvert" rel="tag" title="see questions tagged &#39;culvert&#39;">culvert</span> <span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '12, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-14961" class="comments-container">
&#10;</div>
<div id="comment-tools-14961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14961-form-container" class="comment-form-container">
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

<span id="14963"></span>

<div id="answer-container-14963" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14963-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-14963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>layer</strong> defines the <em>relative vertical position</em> of elements that intersect or overlap. In other words: Of two intersecting elements, the one with the larger layer value is above the other one.</p>
<p>This is the <em>only</em> purpose of layer. In particular, it does not define an absolute elevation. An element with layer=1 might very well higher than another element somewhere else that has layer=2, as long as they don't intersect.</p>
<p>So, with your example, it is perfectly ok that water lower than the surroundings is on the same layer as elements around it, as long as it is not <em>directly below</em> those elements - i.e. there is no overlap/intersection. A culvert, on the other hand, tends to run below something, e.g. a road, and will therefore usually need a layer=-1 tag to place it below that road (in addition to tunnel=culvert).</p>
<p>By convention, positive layer values are used for features above the ground, and negative layer values below the ground. It is also good practice to use the smallest (by absolute value) layer that describes the current situation - so even though tagging a "normal" bridge as layer=5 would still correctly place it above the ground-level road it crosses, this should be avoided. As a result, layers larger than 1 and lower than -1 are quite rare.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '12, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-14963" class="comments-container">
&#10;</div>
<div id="comment-tools-14963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14963-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14962"></span>

<div id="answer-container-14962" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14962-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Imagine 2 roads A and B that cross each other over a river and a third road C that is a tunnel under the river. The river would be at level/layer 0. The 2 aerial roads would have layers 1 for A and 2 (for the upper road B) and the tunnel C would have -1. The rendering would show that road B crosses over road A, over the river. And tunnel C would be rendered with dashed lines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '12, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1fb9da36bbe8817c461df33d395ee413?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerdami&#39;s gravatar image" />
<p><span>gerdami</span><br />
<span class="score" title="696 reputation points">696</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="46 badges"><span class="bronze">●</span><span class="badgecount">46</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerdami has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-14962" class="comments-container">
<span id="14969"></span>
<div id="comment-14969" class="comment">
<div id="post-14969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Guys, Ill have some work to do. I didnt tag all my bridges and culverts correctly. But intersections and subway systems could go deeper or higher then + or - 3.</p>
</div>
<div id="comment-14969-info" class="comment-info">
<span class="comment-age">(11 Aug '12, 22:01)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="14975"></span>
<div id="comment-14975" class="comment">
<div id="post-14975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Potlatch2 has a layer ruler that goes from - 5 to + 5</p>
</div>
<div id="comment-14975-info" class="comment-info">
<span class="comment-age">(12 Aug '12, 09:30)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
</div>
<div id="comment-tools-14962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14962-form-container" class="comment-form-container">
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

