+++
type = "question"
title = "Weak grid lines, why?"
description = '''On some places and at some zoom levels I can see weak horizontal and vertical (maybe) grid lines. Also, on some places these lines are oblique. Mostly over green areas (assume forests) like here: https://www.openstreetmap.org/#map=8/46.851/-83.790 Are these lines real or my W8 display system is wrong...'''
date = "2014-08-26T07:54:00Z"
lastmod = "2014-08-26T14:13:00Z"
weight = 36166
keywords = [ "grid", "forests" ]
aliases = [ "/questions/36166" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Weak grid lines, why?](/questions/36166/weak-grid-lines-why)

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
<span id="post-36166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36166-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On some places and at some zoom levels I can see weak horizontal and vertical (maybe) grid lines. Also, on some places these lines are oblique. Mostly over green areas (assume forests) like here: <a href="https://www.openstreetmap.org/#map=8/46.851/-83.790">https://www.openstreetmap.org/#map=8/46.851/-83.790</a> Are these lines real or my W8 display system is wrong? Can others see these lines too?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-grid" rel="tag" title="see questions tagged &#39;grid&#39;">grid</span> <span class="post-tag tag-link-forests" rel="tag" title="see questions tagged &#39;forests&#39;">forests</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '14, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-36166" class="comments-container">
&#10;</div>
<div id="comment-tools-36166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36166-form-container" class="comment-form-container">
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

<span id="36168"></span>

<div id="answer-container-36168" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36168-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>They are real and seem to be caused by the renderer / stylesheet using a slightly different color for area outlines. Looks ugly.</p>
<p>See this <a href="https://www.openstreetmap.org/node/2961467939">node</a> for example. It is part of four landuses and its position is exactly at the intersection of a horizontal and a vertical grid line.</p>
<p>There is already a <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/652">bug report for this issue</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '14, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '14, 14:16</strong> </span></p>
</div>
</div>
<div id="comments-container-36168" class="comments-container">
<span id="36199"></span>
<div id="comment-36199" class="comment">
<div id="post-36199-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That is a sub-optimally done import. See <span>way example</span>. The landuses are mapped as those rectangles. However, I it is a bit strange that the renderer draws a thin line in some zoom levels. It should not because the neighbouring lines are exactly on the same position, if I see correctly.</p>
</div>
<div id="comment-36199-info" class="comment-info">
<span class="comment-age">(26 Aug '14, 13:19)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="36204"></span>
<div id="comment-36204" class="comment">
<div id="post-36204-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, the import could have been improved. But the renderer should be able to handle adjacent landuses of the same type without creating ugly artifacts.</p>
</div>
<div id="comment-36204-info" class="comment-info">
<span class="comment-age">(26 Aug '14, 14:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36168-form-container" class="comment-form-container">
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

