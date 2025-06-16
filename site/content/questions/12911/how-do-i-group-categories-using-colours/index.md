+++
type = "question"
title = "How do I group categories using colours?"
description = '''Hi All, I am new to OpenStreetMap and was wondering if there is a recommended best practice to group categories with an identifiable colour or patterned system? For example, I am trying to identify different types of clay houses/buildings in Germany. Is there a form of best practice to categorize th...'''
date = "2012-05-23T19:37:00Z"
lastmod = "2012-05-24T13:48:00Z"
weight = 12911
keywords = [ "colour", "buildings", "mapping", "categories", "bestpractice" ]
aliases = [ "/questions/12911" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I group categories using colours?](/questions/12911/how-do-i-group-categories-using-colours)

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
<span id="post-12911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12911-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I am new to OpenStreetMap and was wondering if there is a recommended best practice to group categories with an identifiable colour or patterned system?</p>
<p>For example, I am trying to identify different types of clay houses/buildings in Germany. Is there a form of best practice to categorize the different types of houses via colouring or patterns?</p>
<p>Thanks</p>
<p>Vincent</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-colour" rel="tag" title="see questions tagged &#39;colour&#39;">colour</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-categories" rel="tag" title="see questions tagged &#39;categories&#39;">categories</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '12, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/97e2562cf3f05b0933c6b32e293f2ce8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincentm&#39;s gravatar image" />
<p><span>Vincentm</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincentm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12911" class="comments-container">
&#10;</div>
<div id="comment-tools-12911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12911-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="12918"></span>

<div id="answer-container-12918" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12918-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question seems to confuse two things, namely OpenStreetMap data and map styles. Mappers and rendering style designers have separate tasks:</p>
<ul>
<li>Mappers collect data about reality. For example, they add the information "here is a building made from clay" to the database.</li>
<li>Rendering style designers define what aspects influence the appearance of the map in which way. For example, they define "buildings made from clay should appear as a light brown shape".</li>
</ul>
<p>So if you want a new class of information to appear on the map, you also need to do two things:</p>
<ul>
<li>Check whether there is already a documented way of mapping this on the <a href="http://wiki.openstreetmap.org">wiki</a> or elsewhere. If there isn't, invent new tags to represent the information and use them on objects in the database (preferably after discussing your tagging ideas with other mappers).</li>
<li>Convince style designers to take this into account when rendering maps, or <a href="https://wiki.openstreetmap.org/wiki/Rendering">render</a> your own maps.</li>
</ul>
<p>This probably doesn't answer your question entirely, but I hope it helps you to understand what exactly it is that you want to do and to ask a more specific question that will result in better answers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '12, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-12918" class="comments-container">
&#10;</div>
<div id="comment-tools-12918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12918-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12916"></span>

<div id="answer-container-12916" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12916-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, the renderer and its stylesheet define what colors to use for which object (that is, <a href="https://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a> for the main page). If you want to change those colors, you have to <a href="https://wiki.openstreetmap.org/wiki/Rendering">render</a> your own maps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '12, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12916" class="comments-container">
&#10;</div>
<div id="comment-tools-12916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12916-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12930"></span>

<div id="answer-container-12930" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12930-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks all. I was told by my professor that the when rendering, the style sheets would automatically create the colours and patterns. But after reading your comments it sounds like the renderer (myself) can nominate the colours or patterns etc. I just hope that after allocating a colour and pattern to the different clay houses, that the map can merge the different combinations to show that an area of the map is mixed with different types of clay houses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '12, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/97e2562cf3f05b0933c6b32e293f2ce8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincentm&#39;s gravatar image" />
<p><span>Vincentm</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincentm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12930" class="comments-container">
&#10;</div>
<div id="comment-tools-12930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12930-form-container" class="comment-form-container">
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

