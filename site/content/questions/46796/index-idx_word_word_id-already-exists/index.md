+++
type = "question"
title = "index &quot;idx_word_word_id&quot; already exists"
description = '''Hi guys.. I try to resume the process but after some log like: Starting rank 28  Done 0 in 0 @ 0.000000 per second - FINISHED  Starting rank 29  Done 0 in 0 @ 0.000000 per second - FINISHED  Starting rank 30  Done 0 in 0 @ 0.000000 per second - FINISHED  I got this error: ERRORE: la relazione &quot;idx_w...'''
date = "2015-11-23T16:02:00Z"
lastmod = "2015-11-24T18:08:00Z"
weight = 46796
keywords = [ "nominatim" ]
aliases = [ "/questions/46796" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [index "idx_word_word_id" already exists](/questions/46796/index-idx_word_word_id-already-exists)

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
<span id="post-46796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46796-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-46796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys.. I try to resume the process but after some log like:</p>
<pre><code>Starting rank 28
 Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 29
 Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 30
 Done 0 in 0 @ 0.000000 per second - FINISHED</code></pre>
<p>I got this error:</p>
<pre><code>ERRORE:  la relazione &quot;idx_word_word_id&quot; esiste già
ERROR: pgsql returned with error code (3)</code></pre>
<p>What can I do?? maybe change product? Thanks a lot</p>
<hr />
<p>I dropped that index and now I have similar error:</p>
<pre><code>ERRORE:  la relazione &quot;idx_search_name_nameaddress_vector&quot; esiste già
ERROR: pgsql returned with error code (3)</code></pre>
<p>It is the second index I found on sql folder (under nominatim path) inside file indices.src.sql. What I have to do?? I have to remove all index on that list??</p>
<p>Please I'am so close</p>
<p>Thanks anyway Giacomo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '15, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e1580c3bf447dab7c4a377186b60dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giacomo-keybiz&#39;s gravatar image" />
<p><span>giacomo-keybiz</span><br />
<span class="score" title="33 reputation points">33</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giacomo-keybiz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '15, 18:14</strong> </span></p>
</div>
</div>
<div id="comments-container-46796" class="comments-container">
&#10;</div>
<div id="comment-tools-46796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46796-form-container" class="comment-form-container">
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

<span id="46825"></span>

<div id="answer-container-46825" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46825-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Obviously half the indexes have already been created before your previous importing attempt failed. To finish creating the other indices run:</p>
<pre><code>./utils/setup.php --create-search-indices --ignore-errors</code></pre>
<p>and ignore the errors printed by postgres.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '15, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-46825" class="comments-container">
<span id="46826"></span>
<div id="comment-46826" class="comment">
<div id="post-46826-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot man.. Unfortunately I have read your post too late and I drop all index (already created) I found on <em>indices.src.sql</em>. I hope I'm not wrong..</p>
<p>Thanks again Giacomo</p>
</div>
<div id="comment-46826-info" class="comment-info">
<span class="comment-age">(24 Nov '15, 18:08)</span> <span class="comment-user userinfo">giacomo-keybiz</span>
</div>
</div>
</div>
<div id="comment-tools-46825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46825-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

