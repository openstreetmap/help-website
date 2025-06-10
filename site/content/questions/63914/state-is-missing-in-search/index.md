+++
type = "question"
title = "State is missing in search"
description = '''I installed a local nominatim database with North and Central America version 3.1.0 with tiger data. Most of my searches are working correctly, however, Quebec and Ontario are not being returned as states. Searching for them directly just shows a point with no boundaries. All other Canadian states a...'''
date = "2018-05-31T16:07:00Z"
lastmod = "2018-06-06T18:54:00Z"
weight = 63914
keywords = [ "state", "missing" ]
aliases = [ "/questions/63914" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [State is missing in search](/questions/63914/state-is-missing-in-search)

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
<span id="post-63914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63914-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed a local nominatim database with North and Central America version 3.1.0 with tiger data. Most of my searches are working correctly, however, Quebec and Ontario are not being returned as states. Searching for them directly just shows a point with no boundaries. All other Canadian states are working as expected. I found an older post that had directions to run the following script: ./utils/update.php --import-relation 61549 --index However this script returns an error. I feel its probably due to being outdated. Is there any other way to get the missing states into my database? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-state" rel="tag" title="see questions tagged &#39;state&#39;">state</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '18, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ab285a0245d5b262667b4eb333f7eea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="delongboy&#39;s gravatar image" />
<p><span>delongboy</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="delongboy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63914" class="comments-container">
&#10;</div>
<div id="comment-tools-63914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63914-form-container" class="comment-form-container">
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

<span id="64063"></span>

<div id="answer-container-64063" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64063-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So I found the fix for this. I edited the update.php and ran the script and it works properly now. Line 161 sets $sContentURLsModifyXMLstr which is never used, I changed it to $sContentURL which is used everywhere else and it works now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '18, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ab285a0245d5b262667b4eb333f7eea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="delongboy&#39;s gravatar image" />
<p><span>delongboy</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="delongboy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64063" class="comments-container">
&#10;</div>
<div id="comment-tools-64063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64063-form-container" class="comment-form-container">
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

