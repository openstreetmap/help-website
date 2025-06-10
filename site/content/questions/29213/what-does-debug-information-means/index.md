+++
type = "question"
title = "What does debug information means?"
description = '''I downloaded data from planet.osm.pbf into the database &quot;Nominatim&quot;. I have messages in console such as   Done 41901225 in 105214 @ 398.247620 per second - Rank 30 ETA (seconds): 97671.335938  What do this numbers mean: 41901225, 105214, 398.247620, 97671.335938 ? Can I predict the completion time o...'''
date = "2013-12-20T11:28:00Z"
lastmod = "2013-12-20T13:00:00Z"
weight = 29213
keywords = [ "download", "information", "nominatim" ]
aliases = [ "/questions/29213" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does debug information means?](/questions/29213/what-does-debug-information-means)

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
<span id="post-29213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29213-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded data from planet.osm.pbf into the database "Nominatim". I have messages in console such as</p>
<ul>
<li>Done 41901225 in 105214 @ 398.247620 per second - Rank 30 ETA (seconds): 97671.335938</li>
</ul>
<p>What do this numbers mean: 41901225, 105214, 398.247620, 97671.335938 ? Can I predict the completion time of loading data into the database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '13, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/aea8cdb05518a630ebad09bd7c777dc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amshegar&#39;s gravatar image" />
<p><span>amshegar</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amshegar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29213" class="comments-container">
&#10;</div>
<div id="comment-tools-29213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29213-form-container" class="comment-form-container">
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

<span id="29217"></span>

<div id="answer-container-29217" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29217-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The last number in that debug message gives you an estimate for completion time.</p>
<p>The line shows some statistics about how the address computation (or indexing) of objects is going for the current rank. There are 30 ranks in total, with rank 30 being the final one to be processed. The numbers mean:</p>
<pre><code>Done [1] in [2] @ [3] per second - Rank 30 ETA (seconds): [4]</code></pre>
<p>[1] number of objects already processed</p>
<p>[2] time (in seconds) already passed for indexing this rank</p>
<p>[3] number of objects that are processed per second</p>
<p>[4] estimated time (in seconds) to finish this rank</p>
<p>Rank 26 and 30 are the ones that take by far the longest. After rank 30 has finished, some additional database indexes need to be created. That takes a few hours more to complete.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '13, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-29217" class="comments-container">
&#10;</div>
<div id="comment-tools-29217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29217-form-container" class="comment-form-container">
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

