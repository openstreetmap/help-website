+++
type = "question"
title = "Is it possible to change the whole nominatim data from one machine to another ?"
description = '''I installed nominatim in local machine, now i needs to install in server machine at the same time i dont want to again start installation process in that server machine. In steed i just wants to transfer the data from local to server, because it is faster. Is it possible, plz guide me right way.'''
date = "2014-02-12T06:13:00Z"
lastmod = "2014-02-12T11:09:00Z"
weight = 30667
keywords = [ "pgsql", "transfer", "nominatim", "osm" ]
aliases = [ "/questions/30667" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to change the whole nominatim data from one machine to another ?](/questions/30667/is-it-possible-to-change-the-whole-nominatim-data-from-one-machine-to-another)

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
<span id="post-30667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30667-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed nominatim in local machine, now i needs to install in server machine at the same time i dont want to again start installation process in that server machine.</p>
<p>In steed i just wants to transfer the data from local to server, because it is faster.</p>
<p>Is it possible, plz guide me right way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pgsql" rel="tag" title="see questions tagged &#39;pgsql&#39;">pgsql</span> <span class="post-tag tag-link-transfer" rel="tag" title="see questions tagged &#39;transfer&#39;">transfer</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '14, 06:13</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '14, 06:15</strong> </span></p>
</div>
</div>
<div id="comments-container-30667" class="comments-container">
&#10;</div>
<div id="comment-tools-30667" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30667-form-container" class="comment-form-container">
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

<span id="30669"></span>

<div id="answer-container-30669" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30669-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arun kmp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The fastest way to do this is to copy over the whole PostgreSQL data directory to the target machine. This only works if both machines have the same CPU architecture and the exact same versions of PostgreSQL, PostGIS and some related packages (GDAL and Proj come to mind).</p>
<p>The second-fastest way is likely to take a PostgreSQL database dump on the source and restore it on the target (pg_dump, pg_restore) but this requires rebuilding indexes on the target.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 07:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30669" class="comments-container">
<span id="30676"></span>
<div id="comment-30676" class="comment">
<div id="post-30676-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See <a href="http://www.postgresql.org/docs/current/static/backup.html">http://www.postgresql.org/docs/current/static/backup.html</a></p>
<p>Unless you want to get the disk space back in the old server, it might be a good idea to set <a href="http://www.postgresql.org/docs/current/static/warm-standby.html#STREAMING-REPLICATION">streaming replication</a> from the fast server to the slow one. It's not much more difficult than a filesystem-level copy, you gain resiliency in case the fast server has a problem, and you have an additional server to run read-only queries from to balance the load.</p>
</div>
<div id="comment-30676-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 11:09)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30669-form-container" class="comment-form-container">
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

