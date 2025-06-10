+++
type = "question"
title = "Add variable pricing to toll booth"
description = '''I would like to add variable pricing, where my source would be Malaysia Highway Authority. Is it possible to add fee:car=2.10 on top of fee=yes? Furthermore, is this the standard way of adding toll booth amount data?'''
date = "2017-11-26T05:46:00Z"
lastmod = "2017-11-30T08:32:00Z"
weight = 60799
keywords = [ "toll" ]
aliases = [ "/questions/60799" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add variable pricing to toll booth](/questions/60799/add-variable-pricing-to-toll-booth)

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
<span id="post-60799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60799-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to add variable pricing, where my source would be <a href="http://kadartol.llm.gov.my/">Malaysia Highway Authority</a>. Is it possible to add fee:car=2.10 on top of fee=yes? Furthermore, is this the standard way of adding toll booth amount data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-toll" rel="tag" title="see questions tagged &#39;toll&#39;">toll</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '17, 05:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a86516628511fca8a0b8bd6c96144085?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MotionLogistics&#39;s gravatar image" />
<p><span>MotionLogistics</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MotionLogistics has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60799" class="comments-container">
&#10;</div>
<div id="comment-tools-60799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60799-form-container" class="comment-form-container">
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

<span id="60882"></span>

<div id="answer-container-60882" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60882-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Key:fee"><code>fee</code></a> is only used to tag <em>if</em> (<code>fee=yes</code>, <code>fee=no</code>) and <em>when</em> (<code>fee=&lt;interval&gt;</code>) there is a charge. The charge amount is specified via the <a href="https://wiki.openstreetmap.org/wiki/Key:charge"><code>charge</code></a> key.</p>
<p>These tages aren't widely in use so there is no "standard way" currently. You can check taginfo for <a href="https://taginfo.openstreetmap.org/keys/charge#values">typical values of the charge key</a>. You can see that many of them are just plain text values which cannot be parsed by a machine. Taginfo can also show <a href="https://taginfo.openstreetmap.org/keys/charge#similar">similar keys</a> which reveals that some people also started to use <code>charge:motorcar</code>, <code>charge:bus</code> to tag fees for specific types of transportation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '17, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60882" class="comments-container">
&#10;</div>
<div id="comment-tools-60882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60882-form-container" class="comment-form-container">
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

