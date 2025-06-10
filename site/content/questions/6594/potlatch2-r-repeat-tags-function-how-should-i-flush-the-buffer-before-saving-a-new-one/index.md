+++
type = "question"
title = "Potlatch2 &quot;R&quot; (repeat tags) function: how should I flush the buffer before saving a new one?"
description = '''I sometimes find that when I use the &quot;R&quot; function to copy tags it still as an older tag in the buffer which it uses, how should I flush this before saving a new one.'''
date = "2011-07-27T00:00:00Z"
lastmod = "2011-08-04T16:52:00Z"
weight = 6594
keywords = [ "function", "potlatch2", "repeat" ]
aliases = [ "/questions/6594" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Potlatch2 "R" (repeat tags) function: how should I flush the buffer before saving a new one?](/questions/6594/potlatch2-r-repeat-tags-function-how-should-i-flush-the-buffer-before-saving-a-new-one)

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
<span id="post-6594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6594-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I sometimes find that when I use the "R" function to copy tags it still as an older tag in the buffer which it uses, how should I flush this before saving a new one.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-repeat" rel="tag" title="see questions tagged &#39;repeat&#39;">repeat</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '11, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '17, 15:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-6594" class="comments-container">
&#10;</div>
<div id="comment-tools-6594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6594-form-container" class="comment-form-container">
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

<span id="6881"></span>

<div id="answer-container-6881" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6881-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andy mackey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two buffers, one for lines/areas, and one for nodes, if you select a line (click on it) or a node, this will set the "R" buffer to what you've clicked on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '11, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/f6827fbcbfc77428dfb7f8743ab775db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sundance&#39;s gravatar image" />
<p><span>Sundance</span><br />
<span class="score" title="467 reputation points">467</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sundance has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-6881" class="comments-container">
&#10;</div>
<div id="comment-tools-6881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6881-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6706"></span>

<div id="answer-container-6706" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6706-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have found that if I have tagged a street,a building a wall or lake the next line or polygon I draw can be tagged identically (while highlighted) with "r", you do not have to press "r" to save it first as I thought , it just remembers the last tag.which can be really useful.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '11, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '11, 09:40</strong> </span></p>
</div>
</div>
<div id="comments-container-6706" class="comments-container">
<span id="6707"></span>
<div id="comment-6707" class="comment">
<div id="post-6707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Andy, I don't understand..? Ways or areas when you 'r' repeat; but if you have a node, that repeats the last node instead - is that the issue?</p>
</div>
<div id="comment-6707-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 21:12)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
<span id="6708"></span>
<div id="comment-6708" class="comment">
<div id="post-6708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>actually, I do understand now... (o: yes, clearing the buffer is just done by selecting another item, which itself can then be repeated...</p>
</div>
<div id="comment-6708-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 21:14)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
</div>
<div id="comment-tools-6706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6706-form-container" class="comment-form-container">
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

