+++
type = "question"
title = "Disk space needed for loading the latest planet with osm2pgsql"
description = '''Hi! Could anybody please recommend the volume of free disk space required to import the latest planet PBF via osm2pgsql? E.g., one of crucially important characteristics is the resulting size of the directory PostgreSQL/{version}/data/base after the whole loading in the slim mode with flat-nodes wit...'''
date = "2019-01-15T13:10:00Z"
lastmod = "2019-01-27T04:05:00Z"
weight = 67591
keywords = [ "planet", "disk_usage", "osm2pgsql" ]
aliases = [ "/questions/67591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disk space needed for loading the latest planet with osm2pgsql](/questions/67591/disk-space-needed-for-loading-the-latest-planet-with-osm2pgsql)

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
<span id="post-67591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67591-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! Could anybody please recommend the volume of free disk space required to import the latest planet PBF via osm2pgsql?</p>
<p>E.g., one of crucially important characteristics is the resulting size of the directory</p>
<p>PostgreSQL/{version}/data/base</p>
<p>after the whole loading in the slim mode with flat-nodes with hstore. What size did you get in this mode?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '19, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/7e8e1b07b427abdbd7ba5e9403f87e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="molokanov&#39;s gravatar image" />
<p><span>molokanov</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="molokanov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67591" class="comments-container">
&#10;</div>
<div id="comment-tools-67591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67591-form-container" class="comment-form-container">
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

<span id="67748"></span>

<div id="answer-container-67748" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67748-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the whole Europe (19.1 GB in PBF) PostgreSQL 10 database takes about 450 GB, so I assume it would be about 1 TB for the whole planet (43 GB in PBF).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '19, 04:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-67748" class="comments-container">
&#10;</div>
<div id="comment-tools-67748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67748-form-container" class="comment-form-container">
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

