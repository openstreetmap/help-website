+++
type = "question"
title = "osm2pgsql restart data import after crash"
description = '''If osm2pgsql import fails for some reason (server rebooting), can you simply kick the process of again, or do you need to clear out the database first? This is on ubuntu.'''
date = "2013-06-26T01:29:00Z"
lastmod = "2013-06-26T08:54:00Z"
weight = 23713
keywords = [ "osm2pgsql", "ubuntu" ]
aliases = [ "/questions/23713" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql restart data import after crash](/questions/23713/osm2pgsql-restart-data-import-after-crash)

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
<span id="post-23713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If osm2pgsql import fails for some reason (server rebooting), can you simply kick the process of again, or do you need to clear out the database first?</p>
<p>This is on ubuntu.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '13, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d0323e670bafa590ec131e5d08f1b85e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tangotonyb&#39;s gravatar image" />
<p><span>Tangotonyb</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tangotonyb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23713" class="comments-container">
&#10;</div>
<div id="comment-tools-23713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23713-form-container" class="comment-form-container">
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

<span id="23721"></span>

<div id="answer-container-23721" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23721-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tangotonyb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just start it again and it will clear the tables by itself (assuming you're running in create, not append, mode). It is not possible to continue where you left off though, it will start from scratch.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '13, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23721" class="comments-container">
&#10;</div>
<div id="comment-tools-23721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23721-form-container" class="comment-form-container">
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

