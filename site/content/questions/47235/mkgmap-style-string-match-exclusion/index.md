+++
type = "question"
title = "mkgmap style string match exclusion"
description = '''In the style files for Mkgmap how do i add an exclusion based on a partial string match, I know if i want to find tags with &quot;Lane&quot; in them it is  name ~ &#x27;.*[Ll]ane&#x27; but how do i find a match for names that do not have Lane in them I have tried  name !~ &#x27;.*[Ll]ane&#x27; and name != ~&#x27;.*[Ll]ane&#x27; but they c...'''
date = "2015-12-19T11:33:00Z"
lastmod = "2015-12-19T11:58:00Z"
weight = 47235
keywords = [ "mkgmap", "partial", "string", "match" ]
aliases = [ "/questions/47235" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mkgmap style string match exclusion](/questions/47235/mkgmap-style-string-match-exclusion)

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
<span id="post-47235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47235-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the style files for Mkgmap how do i add an exclusion based on a partial string match,</p>
<p>I know if i want to find tags with "Lane" in them it is</p>
<p>name ~ '.*[Ll]ane'</p>
<p>but how do i find a match for names that do not have Lane in them</p>
<p>I have tried</p>
<p>name !~ '.*[Ll]ane'</p>
<p>and</p>
<p>name != ~'.*[Ll]ane'</p>
<p>but they crash the compiler.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-partial" rel="tag" title="see questions tagged &#39;partial&#39;">partial</span> <span class="post-tag tag-link-string" rel="tag" title="see questions tagged &#39;string&#39;">string</span> <span class="post-tag tag-link-match" rel="tag" title="see questions tagged &#39;match&#39;">match</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '15, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '15, 11:45</strong> </span></p>
</div>
</div>
<div id="comments-container-47235" class="comments-container">
&#10;</div>
<div id="comment-tools-47235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47235-form-container" class="comment-form-container">
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

<span id="47236"></span>

<div id="answer-container-47236" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47236-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>found the answer,</p>
<p>name! (~ '.*[Ll]ane')</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '15, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-47236" class="comments-container">
&#10;</div>
<div id="comment-tools-47236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47236-form-container" class="comment-form-container">
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

