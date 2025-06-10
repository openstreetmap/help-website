+++
type = "question"
title = "Notes API: Maximum size of a bbox?"
description = '''Hello, I want to write a small script using the Notes API. I want to limit the size of a Bounding Box that a user can choose. So if I try big requests OSM Servers are repsonding: [400] The maximum bbox size is 25, and your request was too large. Either request a smaller area, or use planet.osm  What...'''
date = "2014-08-11T15:47:00Z"
lastmod = "2014-08-11T16:27:00Z"
weight = 35706
keywords = [ "notes-api", "notes" ]
aliases = [ "/questions/35706" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Notes API: Maximum size of a bbox?](/questions/35706/notes-api-maximum-size-of-a-bbox)

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
<span id="post-35706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35706-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to write a small script using the Notes API. I want to limit the size of a Bounding Box that a user can choose. So if I try big requests OSM Servers are repsonding:</p>
<pre><code>[400] The maximum bbox size is 25, and your request was too large. Either request a smaller area, or use planet.osm</code></pre>
<p>What does 25 mean? 25 square kilometers?</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notes-api" rel="tag" title="see questions tagged &#39;notes-api&#39;">notes-api</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '14, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/7ec5c174de466f97a699757f71dc398b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerosin&#39;s gravatar image" />
<p><span>kerosin</span><br />
<span class="score" title="411 reputation points">411</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerosin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35706" class="comments-container">
&#10;</div>
<div id="comment-tools-35706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35706-form-container" class="comment-form-container">
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

<span id="35707"></span>

<div id="answer-container-35707" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35707-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kerosin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the comments in the <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/config/example.application.yml#L30">example configuration</a>, 25 square degrees</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '14, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-35707" class="comments-container">
&#10;</div>
<div id="comment-tools-35707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35707-form-container" class="comment-form-container">
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

