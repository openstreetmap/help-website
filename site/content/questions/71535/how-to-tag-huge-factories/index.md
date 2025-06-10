+++
type = "question"
title = "How to tag huge factories?"
description = '''Lets say we have a super big factory that is bigger than an entire neighborhood. Thousands work there, but it is still one company. I know that landuse=industrial needs to be added under it, but how should naming happen? Should I separate it from other industrial landuses and name that big lot or ad...'''
date = "2019-11-08T07:30:00Z"
lastmod = "2019-11-09T07:24:00Z"
weight = 71535
keywords = [ "industrial", "landuse", "factory", "tagging" ]
aliases = [ "/questions/71535" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag huge factories?](/questions/71535/how-to-tag-huge-factories)

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
<span id="post-71535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71535-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Lets say we have a super big factory that is bigger than an entire neighborhood. Thousands work there, but it is still one company. I know that <code>landuse=industrial</code> needs to be added under it, but how should naming happen? Should I separate it from other industrial landuses and name that big lot or add a new area with <code>man_made=works</code> and add the name for that? Should I even add that in the first place when the landuse already has the <code>industrial=factory</code> tag?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-industrial" rel="tag" title="see questions tagged &#39;industrial&#39;">industrial</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-factory" rel="tag" title="see questions tagged &#39;factory&#39;">factory</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '19, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a9715d60e31c91a442c2dacefdc1dae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UntaggedWay&#39;s gravatar image" />
<p><span>UntaggedWay</span><br />
<span class="score" title="576 reputation points">576</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UntaggedWay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71535" class="comments-container">
&#10;</div>
<div id="comment-tools-71535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71535-form-container" class="comment-form-container">
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

<span id="71539"></span>

<div id="answer-container-71539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71539-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>man_made=works</code> seems to me to be more commonly used to map the actual factory. I would do as you suggest: Draw a polyline around the perimeter of the factory and give it a <code>name=XYZ</code> tag. I see the <code>landuse=industrial</code> to also include the adjacent roads, neighboring factories, the small fast food stall across the street etc., while the <code>man_made=works</code> is drawn around the company's property. The <code>industrial=factory</code> only makes sense if the <code>landuse=industrial</code> is used instead of the <code>man_made=works</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '19, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-71539" class="comments-container">
<span id="71540"></span>
<div id="comment-71540" class="comment">
<div id="post-71540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is my point. The whole facility is just manufacturing plants, parking and roads. Everything is the company's property so the <code>landuse=industrial</code> and <code>man_made=works</code> would cover the same area. Or is <code>man_made=works</code> only for the actual production buildings?</p>
</div>
<div id="comment-71540-info" class="comment-info">
<span class="comment-age">(08 Nov '19, 15:03)</span> <span class="comment-user userinfo">UntaggedWay</span>
</div>
</div>
<span id="71554"></span>
<div id="comment-71554" class="comment">
<div id="post-71554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Buildings are <code>building=industrial</code>.</p>
</div>
<div id="comment-71554-info" class="comment-info">
<span class="comment-age">(09 Nov '19, 05:34)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="71559"></span>
<div id="comment-71559" class="comment">
<div id="post-71559-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The factory and the landuse could cover the same area in special cases. Generally, landuse is larger. Do you have a link to the place?</p>
</div>
<div id="comment-71559-info" class="comment-info">
<span class="comment-age">(09 Nov '19, 07:24)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71539-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71542"></span>

<div id="answer-container-71542" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71542-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To Add to TZorn's answer. I would map the service roads and any footpaths into to area. I would also map. if i knew the various, good inwards bays dispatch points and entries for staff and visitors plus various car parks, all these can be useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '19, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '19, 15:47</strong> </span></p>
</div>
</div>
<div id="comments-container-71542" class="comments-container">
&#10;</div>
<div id="comment-tools-71542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71542-form-container" class="comment-form-container">
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

