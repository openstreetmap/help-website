+++
type = "question"
title = "Trac ticket dependencies"
description = '''How do I make one ticket (bug) depend on other and vice versa at trac.openstreetmap.org?'''
date = "2011-12-24T22:23:00Z"
lastmod = "2011-12-30T09:56:00Z"
weight = 9609
keywords = [ "ticket", "bug", "trac" ]
aliases = [ "/questions/9609" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Trac ticket dependencies](/questions/9609/trac-ticket-dependencies)

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
<span id="post-9609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9609-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I make one ticket (bug) depend on other and vice versa at <a href="http://trac.openstreetmap.org">trac.openstreetmap.org</a>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ticket" rel="tag" title="see questions tagged &#39;ticket&#39;">ticket</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-trac" rel="tag" title="see questions tagged &#39;trac&#39;">trac</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '11, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-9609" class="comments-container">
&#10;</div>
<div id="comment-tools-9609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9609-form-container" class="comment-form-container">
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

<span id="9630"></span>

<div id="answer-container-9630" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9630-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kozuch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't. Trac does not have the concept of ticket dependencies, like e.g. Bugzilla does. It's been discussed for a long time, but it's still not implemented. See <a href="http://trac.edgewall.org/ticket/31">http://trac.edgewall.org/ticket/31</a> .</p>
<p>That said, you can link to other tickets in the description or comments. Just put a '#' in front of the ticket number, and trac will auto-link it. E.g. "See ticket #33.".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '11, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-9630" class="comments-container">
<span id="9697"></span>
<div id="comment-9697" class="comment">
<div id="post-9697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While I accept your answer it seems like TRAC was a really bad choice for the project of this scale... dependencies are a must for larger projects.</p>
</div>
<div id="comment-9697-info" class="comment-info">
<span class="comment-age">(30 Dec '11, 09:56)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-9630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9630-form-container" class="comment-form-container">
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

