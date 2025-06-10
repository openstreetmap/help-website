+++
type = "question"
title = "Problems with relation"
description = '''Hi all, anybody knows why this island is not rendered? The relation seems to be correct. http://www.openstreetmap.org/way/268014778 Thanks René'''
date = "2015-01-29T21:48:00Z"
lastmod = "2015-01-30T21:18:00Z"
weight = 40704
keywords = [ "outer", "inner", "relations" ]
aliases = [ "/questions/40704" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problems with relation](/questions/40704/problems-with-relation)

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
<span id="post-40704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>anybody knows why this island is not rendered? The relation seems to be correct.</p>
<p><a href="http://www.openstreetmap.org/way/268014778">http://www.openstreetmap.org/way/268014778</a></p>
<p>Thanks René</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-outer" rel="tag" title="see questions tagged &#39;outer&#39;">outer</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '15, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a6e2839b04b99e35e45d64fe66b9a500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rene78&#39;s gravatar image" />
<p><span>rene78</span><br />
<span class="score" title="700 reputation points">700</span><span title="29 badges"><span class="badge1">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rene78 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40704" class="comments-container">
&#10;</div>
<div id="comment-tools-40704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40704-form-container" class="comment-form-container">
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

<span id="40705"></span>

<div id="answer-container-40705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My guessing: you should delete natural=water from the outer ring (<a href="http://www.openstreetmap.org/way/313399158),">http://www.openstreetmap.org/way/313399158),</a> it is a redundancy of the riverbank relation (one feature, one element); right now, it's like having two objects overlapping: a riverbank with some islands inside, and a sort of lake covering them all. Also, those ways should have "inner" role: <a href="http://www.openstreetmap.org/way/313647459">http://www.openstreetmap.org/way/313647459</a> and <a href="http://www.openstreetmap.org/way/313647754">http://www.openstreetmap.org/way/313647754</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '15, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/b75c397321b010a8a70f44ab78e7bb44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alecs01&#39;s gravatar image" />
<p><span>Alecs01</span><br />
<span class="score" title="1371 reputation points"><span>1.4k</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alecs01 has 6 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-40705" class="comments-container">
<span id="40723"></span>
<div id="comment-40723" class="comment">
<div id="post-40723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. Even after doing what you recommended the problem persisted. After redoing the relation it worked though. There was one inner element too much, maybe that caused problems.</p>
<p>Thanks anyway!</p>
</div>
<div id="comment-40723-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 21:18)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
</div>
<div id="comment-tools-40705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40705-form-container" class="comment-form-container">
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

