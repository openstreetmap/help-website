+++
type = "question"
title = "How to add Nominatim custom tags?"
description = '''I have a working Nominatim install. Now i want to add in the nominatim database a custom tag column like for example an admin 20 level attribute, and i want to have it in my Nominatim requests. If i simply add it in the nominatim database, how can can I retrieve it with Nominatim.  So i just need to...'''
date = "2014-04-14T10:12:00Z"
lastmod = "2014-09-15T18:22:00Z"
weight = 32358
keywords = [ "nominatim", "data", "custom" ]
aliases = [ "/questions/32358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add Nominatim custom tags?](/questions/32358/how-to-add-nominatim-custom-tags)

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
<span id="post-32358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a working Nominatim install.</p>
<p>Now i want to add in the nominatim database a custom tag column like for example an admin 20 level attribute, and i want to have it in my Nominatim requests.</p>
<p>If i simply add it in the nominatim database, how can can I retrieve it with Nominatim. So i just need to geocode as usual, but get also that attribute, which is stored for every way.</p>
<p>Does this is feasible? Thank you advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '14, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/afa2913bd1ceace5a19edb7f80a43c24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mihai%20niculita&#39;s gravatar image" />
<p><span>mihai niculita</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mihai niculita has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '14, 10:30</strong> </span></p>
</div>
</div>
<div id="comments-container-32358" class="comments-container">
&#10;</div>
<div id="comment-tools-32358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32358-form-container" class="comment-form-container">
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

<span id="32395"></span>

<div id="answer-container-32395" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32395-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually, returning additional data is just a question of modifying the template snippet for the selected output format in <code>lib/templates</code>. This of course requires that the data is actually stored with the object.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '14, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32395" class="comments-container">
<span id="32398"></span>
<div id="comment-32398" class="comment">
<div id="post-32398-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, if I put the data in the placex table, I can modify the lib/templates and request those column in the query?</p>
</div>
<div id="comment-32398-info" class="comment-info">
<span class="comment-age">(17 Apr '14, 08:43)</span> <span class="comment-user userinfo">mihai niculita</span>
</div>
</div>
<span id="36850"></span>
<div id="comment-36850" class="comment">
<div id="post-36850-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you ever confirm this to work mihai?</p>
<p>I'm trying to do something similar myself, I'd like to create a custom key:value pair and be able to query the location using Nominatim</p>
</div>
<div id="comment-36850-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 18:22)</span> <span class="comment-user userinfo">olearytd12</span>
</div>
</div>
</div>
<div id="comment-tools-32395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32395-form-container" class="comment-form-container">
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

