+++
type = "question"
title = "maxspeed:hazmat:forward or maxspeed:forward:hazmat"
description = '''Couldn&#x27;t find it in the Wiki. Can anyone tell me if it is maxspeed:hazmat:forward=30 or maxspeed:forward:hazmat=30. I looked it up for HGVs and hazmat in taginfo and found: 30x maxspeed:hgv:forward 12x maxspeed:forward:hgv  7x maxspeed:forward:hazmat  7x maxspeed:hazmat:forward  So it is not a stron...'''
date = "2014-04-26T13:06:00Z"
lastmod = "2014-04-26T16:29:00Z"
weight = 32657
keywords = [ "hgv", "hazmat", "maxspeed", "backward", "forward" ]
aliases = [ "/questions/32657" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [maxspeed:hazmat:forward or maxspeed:forward:hazmat](/questions/32657/maxspeedhazmatforward-or-maxspeedforwardhazmat)

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
<span id="post-32657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Couldn't find it in the Wiki. Can anyone tell me if it is <code>maxspeed:hazmat:forward=30</code> or <code>maxspeed:forward:hazmat=30</code>. I looked it up for HGVs and hazmat in taginfo and found:</p>
<pre><code>30x maxspeed:hgv:forward
12x maxspeed:forward:hgv
 7x maxspeed:forward:hazmat
 7x maxspeed:hazmat:forward</code></pre>
<p>So it is not a strong indicator. I'd prefer <code>maxspeed[:forward|:backward][:hgv|:hazmat]</code> but in the end it doesn't matter as long as it is consistent.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hgv" rel="tag" title="see questions tagged &#39;hgv&#39;">hgv</span> <span class="post-tag tag-link-hazmat" rel="tag" title="see questions tagged &#39;hazmat&#39;">hazmat</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-backward" rel="tag" title="see questions tagged &#39;backward&#39;">backward</span> <span class="post-tag tag-link-forward" rel="tag" title="see questions tagged &#39;forward&#39;">forward</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '14, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-32657" class="comments-container">
&#10;</div>
<div id="comment-tools-32657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32657-form-container" class="comment-form-container">
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

<span id="32673"></span>

<div id="answer-container-32673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32673-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">Conditional Restrictions</a> Wiki page <strong>hazmat</strong> should be treated as Condition, so my conclusion would be something like</p>
<pre><code>maxspeed:forward:conditional = 50 @ hazmat</code></pre>
<p>(50km/h for hazmat vehicles in direction of the way).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '14, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-32673" class="comments-container">
&#10;</div>
<div id="comment-tools-32673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32673-form-container" class="comment-form-container">
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

