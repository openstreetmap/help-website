+++
type = "question"
title = "extra space in returned xml (nominatim/reverse)"
description = '''Hi, I installed a local Nominatim server.  The reverse query returns an xml with the correct content but it starts with a space character.  Surprisingly, web browsers don&#x27;t handle it. Is there a way to remove this extra space? Thanks, Raz'''
date = "2014-01-06T09:38:00Z"
lastmod = "2014-01-06T11:45:00Z"
weight = 29606
keywords = [ "xml", "nominatim", "reverse" ]
aliases = [ "/questions/29606" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [extra space in returned xml (nominatim/reverse)](/questions/29606/extra-space-in-returned-xml-nominatimreverse)

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
<span id="post-29606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29606-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I installed a local Nominatim server.</p>
<p>The reverse query returns an xml with the correct content but it starts with a space character.</p>
<p>Surprisingly, web browsers don't handle it.</p>
<p>Is there a way to remove this extra space?</p>
<p>Thanks, Raz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '14, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/84ebb95a07dd884e34f0170b07b1d652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RazAlon&#39;s gravatar image" />
<p><span>RazAlon</span><br />
<span class="score" title="61 reputation points">61</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RazAlon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29606" class="comments-container">
&#10;</div>
<div id="comment-tools-29606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29606-form-container" class="comment-form-container">
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

<span id="29609"></span>

<div id="answer-container-29609" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29609-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-29609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely a whitespace issue in one of your PHP files. Make sure you did not add any whitespace before &lt;?php in settings/local.php or other php files edited.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '14, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-29609" class="comments-container">
<span id="29610"></span>
<div id="comment-29610" class="comment">
<div id="post-29610-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Bingo, it was indeed in local.php.</p>
<p>thanks a lot! Raz</p>
</div>
<div id="comment-29610-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 11:45)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
</div>
<div id="comment-tools-29609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29609-form-container" class="comment-form-container">
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

