+++
type = "question"
title = "How to make &quot;unimportant&quot; markers that can be overlapped (mapnik)?"
description = '''When I make a marker layer, even with marker-allow-overlap: true, those markers cannot be overlapped by markers and text on higher layers. I&#x27;d like to make markers outside the collision tree, so labels and other markers could be drawn on top of them. Is there a way to do this with mapnik 2.2?'''
date = "2014-04-28T08:08:00Z"
lastmod = "2014-04-28T08:21:00Z"
weight = 32711
keywords = [ "tilemill", "mapnik" ]
aliases = [ "/questions/32711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make "unimportant" markers that can be overlapped (mapnik)?](/questions/32711/how-to-make-unimportant-markers-that-can-be-overlapped-mapnik)

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
<span id="post-32711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32711-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I make a marker layer, even with <code>marker-allow-overlap: true</code>, those markers cannot be overlapped by markers and text on higher layers. I'd like to make markers outside the collision tree, so labels and other markers could be drawn on top of them. Is there a way to do this with mapnik 2.2?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '14, 08:08</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-32711" class="comments-container">
&#10;</div>
<div id="comment-tools-32711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32711-form-container" class="comment-form-container">
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

<span id="32712"></span>

<div id="answer-container-32712" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32712-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-32712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>And immediately after asking this question I've found the answer: <code>marker-ignore-placement: true</code>. How did I not see that yesterday?..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '14, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-32712" class="comments-container">
&#10;</div>
<div id="comment-tools-32712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32712-form-container" class="comment-form-container">
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

