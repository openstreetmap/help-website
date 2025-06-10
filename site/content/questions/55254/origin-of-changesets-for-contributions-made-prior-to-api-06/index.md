+++
type = "question"
title = "Origin of changesets for contributions made prior to API 0.6"
description = '''Hi, I understand that the concept of changeset appeared with API 0.6 in April 2009. However, when querying the API, changesets exist prior to this date.   How did these changesets created? How did the information they contain retrieved?   Thanks'''
date = "2017-03-23T18:49:00Z"
lastmod = "2017-03-23T21:05:00Z"
weight = 55254
keywords = [ "changesets", "api", "database" ]
aliases = [ "/questions/55254" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Origin of changesets for contributions made prior to API 0.6](/questions/55254/origin-of-changesets-for-contributions-made-prior-to-api-06)

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
<span id="post-55254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55254-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I understand that the concept of changeset appeared with API 0.6 in April 2009. However, when querying the API, changesets exist prior to this date.</p>
<ul>
<li>How did these changesets created?</li>
<li>How did the information they contain retrieved?</li>
</ul>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '17, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55254" class="comments-container">
&#10;</div>
<div id="comment-tools-55254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55254-form-container" class="comment-form-container">
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

<span id="55256"></span>

<div id="answer-container-55256" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55256-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-55256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can read C++, the code that was carried out to "migrate" the database from its original form to one with changesets is at <a href="https://svn.openstreetmap.org/applications/utils/misc/api06_migrate/.">https://svn.openstreetmap.org/applications/utils/misc/api06_migrate/.</a> Specifically:</p>
<ul>
<li>the main logic is in <a href="https://svn.openstreetmap.org/applications/utils/misc/api06_migrate/changeset_synth.cpp">https://svn.openstreetmap.org/applications/utils/misc/api06_migrate/changeset_synth.cpp</a></li>
<li>the rules are explained in <a href="https://svn.openstreetmap.org/applications/utils/misc/api06_migrate/README.WARNING:">https://svn.openstreetmap.org/applications/utils/misc/api06_migrate/README.WARNING:</a> changesets were synthesised from existing edits with "idle time 1 hour, no changeset lasts longer than 24 hours, no changeset contains more than 50,000 changes"</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '17, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '17, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-55256" class="comments-container">
<span id="55258"></span>
<div id="comment-55258" class="comment">
<div id="post-55258-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks! I should be able to read the code. Anyway, the basic logic of applying changesets' capabilities on each users' edits is clever :-)</p>
</div>
<div id="comment-55258-info" class="comment-info">
<span class="comment-age">(23 Mar '17, 21:05)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-55256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55256-form-container" class="comment-form-container">
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

