+++
type = "question"
title = "Are holes in water objects rendered?"
description = '''When rendering the main map the holes (islands with no specific content) in river and lake water objects are displayed in the land/light-grey colour. Are these holes rendered or we just see the background through the holes?'''
date = "2016-07-03T21:09:00Z"
lastmod = "2016-07-12T13:30:00Z"
weight = 50591
keywords = [ "rendering", "river", "holes", "lake" ]
aliases = [ "/questions/50591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Are holes in water objects rendered?](/questions/50591/are-holes-in-water-objects-rendered)

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
<span id="post-50591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50591-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When rendering the main map the holes (islands with no specific content) in river and lake water objects are displayed in the land/light-grey colour. Are these holes rendered or we just see the background through the holes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-holes" rel="tag" title="see questions tagged &#39;holes&#39;">holes</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '16, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-50591" class="comments-container">
<span id="50602"></span>
<div id="comment-50602" class="comment">
<div id="post-50602-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I guess this depends on the renderer and/or rendering setup. Some might choose to display water as background, some others might choose to display land by default.</p>
</div>
<div id="comment-50602-info" class="comment-info">
<span class="comment-age">(04 Jul '16, 07:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50591-form-container" class="comment-form-container">
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

<span id="50873"></span>

<div id="answer-container-50873" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50873-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>if the water object is a multipolygon and the "islands" are set as inner objects, they will render. Note at higher zooms(12,13) it takes a lot longer to refresh on the main OSM map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '16, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/55b745b283e8f1a78cd942c72b6021f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LogicalViolinist&#39;s gravatar image" />
<p><span>LogicalVioli...</span><br />
<span class="score" title="246 reputation points">246</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LogicalViolinist has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-50873" class="comments-container">
&#10;</div>
<div id="comment-tools-50873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50873-form-container" class="comment-form-container">
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

