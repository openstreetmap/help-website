+++
type = "question"
title = "Is it possible to recover from a failed osm2pgsql import?"
description = '''After a week of importing, I hit an error due to an unrelated db issue. Is it in any way possible to pick up and continue the last ~3 hours of the relations import? Reading in file: /osm/data/planet-220516.osm.pbf Using PBF parser. Processing: Node(7685383k 248.6k/s) Way(858972k 2.10k/s) Relation(95...'''
date = "2022-05-31T09:33:00Z"
lastmod = "2022-06-02T10:30:00Z"
weight = 84635
keywords = [ "osm2pgsql", "recovery" ]
aliases = [ "/questions/84635" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to recover from a failed osm2pgsql import?](/questions/84635/is-it-possible-to-recover-from-a-failed-osm2pgsql-import)

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
<span id="post-84635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After a week of importing, I hit an error due to an unrelated db issue. Is it in any way possible to pick up and continue the last ~3 hours of the relations import?</p>
<pre><code>Reading in file: /osm/data/planet-220516.osm.pbf
Using PBF parser.
Processing: Node(7685383k 248.6k/s) Way(858972k 2.10k/s) Relation(9501590 59.22/s)WARNING:  terminating connection because of crash of another server process
DETAIL:  The postmaster has commanded this server process to roll back the current transaction and exit, because another server process exited abnormally and possibly corrupted shared memory.
HINT:  In a moment you should be able to reconnect to the database and repeat your command.
WARNING:  terminating connection because of crash of another server process
DETAIL:  The postmaster has commanded this server process to roll back the current transaction and exit, because another server process exited abnormally and possibly corrupted shared memory.
HINT:  In a moment you should be able to reconnect to the database and repeat your command.
terminate called after throwing an instance of &#39;std::runtime_error&#39;
  what():  result COPY_END for planet_osm_polygon failed: SSL SYSCALL error: EOF detected</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-recovery" rel="tag" title="see questions tagged &#39;recovery&#39;">recovery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '22, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/4f56517242a58c6e37c6421d4b874893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesPep&#39;s gravatar image" />
<p><span>JamesPep</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesPep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84635" class="comments-container">
&#10;</div>
<div id="comment-tools-84635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84635-form-container" class="comment-form-container">
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

<span id="84645"></span>

<div id="answer-container-84645" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JamesPep has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, unfortunately it is not possible to pick up where the import crashed.</p>
<p>Note that one week for the import seems to be on the long side. Have you read the chapters on tuning the database in the manual? <a href="https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server">https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '22, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-84645" class="comments-container">
<span id="84674"></span>
<div id="comment-84674" class="comment">
<div id="post-84674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's painfully slow, but it's on one of those new AWS RDS Aurora-Postgreql "serverless" instance, so I'm not sure how to tune it.</p>
</div>
<div id="comment-84674-info" class="comment-info">
<span class="comment-age">(02 Jun '22, 10:30)</span> <span class="comment-user userinfo">JamesPep</span>
</div>
</div>
</div>
<div id="comment-tools-84645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84645-form-container" class="comment-form-container">
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

