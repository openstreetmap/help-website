+++
type = "question"
title = "[closed] what is wrong with this code? :("
description = '''if i have &quot;%turn1%=1&quot;, what is wrong? :1pcom1 set com1=%random% if %com1%&amp;gt;9 goto 1pcom1 if %com1%==%turn1% goto 1pcom1 goto 1pt2 Of course, i have &quot;1pt2&quot;...'''
date = "2012-05-21T12:38:00Z"
lastmod = "2012-05-21T12:55:00Z"
weight = 12841
keywords = [ "variable", "batch" ]
aliases = [ "/questions/12841" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] what is wrong with this code? :(](/questions/12841/what-is-wrong-with-this-code)

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
<span id="post-12841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12841-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-12841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>if i have "%turn1%=1", what is wrong?</p>
<p>:1pcom1</p>
<p>set com1=%random%</p>
<p>if %com1%&gt;9 goto 1pcom1</p>
<p>if %com1%==%turn1% goto 1pcom1</p>
<p>goto 1pt2</p>
<p>Of course, i have "1pt2"...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '12, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/aa84f224b2a82f15b2a76e4c49cf1c39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nadi106&#39;s gravatar image" />
<p><span>nadi106</span><br />
<span class="score" title="-1 reputation points">-1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nadi106 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>21 May '12, 14:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-12841" class="comments-container">
&#10;</div>
<div id="comment-tools-12841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12841-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not an OpenStreetMap question" by Richard 21 May '12, 14:17

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12843"></span>

<div id="answer-container-12843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>%random% returns a number from 1 to 32768, so it might have to run for a long time before it becomes between 2 and 9 - are you sure that is what you want?</p>
<p>If you try to explain what you want to happen it will be a lot easier to give you a good answer.</p>
<p>This might also not be the best place to ask, since it is not really OpenStreetMap related.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '12, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '12, 13:38</strong> </span></p>
</div>
</div>
<div id="comments-container-12843" class="comments-container">
&#10;</div>
<div id="comment-tools-12843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12843-form-container" class="comment-form-container">
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

