+++
type = "question"
title = "Tagging a commercial area outside a village as hamlet?"
description = '''When looking at the area surrounding the Leipzig/Halle airport, I noticed that the commercial area outside of Zwochau is tagged with place=hamlet and name=Gewerbegebiet Zwochau (see here). However, although it lies outside the village, it appears to be the only commercial or industrial area within 5...'''
date = "2015-10-05T12:49:00Z"
lastmod = "2015-10-07T00:28:00Z"
weight = 45717
keywords = [ "commercial", "tagging", "hamlet" ]
aliases = [ "/questions/45717" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging a commercial area outside a village as hamlet?](/questions/45717/tagging-a-commercial-area-outside-a-village-as-hamlet)

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
<span id="post-45717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45717-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When looking at the area surrounding the Leipzig/Halle airport, I noticed that the commercial area outside of Zwochau is tagged with <code>place=hamlet</code> and <code>name=Gewerbegebiet Zwochau</code> (<a href="http://www.openstreetmap.org/#map=16/51.4621/12.2540">see here</a>). However, although it lies outside the village, it appears to be the only commercial or industrial area within 5 miles around the airport tagged in such a way. Is this a generally acceptable tagging scheme, or should it be done differently? If yes, how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-commercial" rel="tag" title="see questions tagged &#39;commercial&#39;">commercial</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-hamlet" rel="tag" title="see questions tagged &#39;hamlet&#39;">hamlet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '15, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b65e058cd0b8b0a32bc2f0bd6a954470?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LEJ-TD%20Praktikant&#39;s gravatar image" />
<p><span>LEJ-TD Prakt...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LEJ-TD Praktikant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45717" class="comments-container">
&#10;</div>
<div id="comment-tools-45717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45717-form-container" class="comment-form-container">
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

<span id="45770"></span>

<div id="answer-container-45770" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45770-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LEJ-TD Praktikant has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>hamlet</code> implies a settlement, that means some people would live there. This is not the case for the industrial landuse. The name <code>Gewerbegebiet</code> on the landuse is incorrect as well, this is just a description.</p>
<p>You should transfer the full name <code>Gewerbegebiet Zwochau</code> to the landuse polygon and remove the hamlet node.</p>
<p>There is also no need for a <code>layer</code> tag on the landuse, that can be removed as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '15, 00:28</strong></p>
<img src="https://secure.gravatar.com/avatar/2d01b00413bb205c1735dde9a3b32c4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="P24&#39;s gravatar image" />
<p><span>P24</span><br />
<span class="score" title="154 reputation points">154</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="P24 has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '15, 00:31</strong> </span></p>
</div>
</div>
<div id="comments-container-45770" class="comments-container">
&#10;</div>
<div id="comment-tools-45770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45770-form-container" class="comment-form-container">
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

