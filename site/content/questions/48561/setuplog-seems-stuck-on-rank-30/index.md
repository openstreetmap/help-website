+++
type = "question"
title = "setup.log seems stuck on rank 30.."
description = '''Hi guys and thanks in advance. I have a 8 gb RAM centos 6.6 machine. I&#x27;m trying to install nominatim and indexing european map.. I follow the simple instructions oon wiki guide and, until yesterday, everything seems going fine.. But yesterday when I do tail -f on log file I saw: Done 54357951 in 141...'''
date = "2016-03-08T10:13:00Z"
lastmod = "2016-03-08T14:20:00Z"
weight = 48561
keywords = [ "europe", "nominatim" ]
aliases = [ "/questions/48561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [setup.log seems stuck on rank 30..](/questions/48561/setuplog-seems-stuck-on-rank-30)

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
<span id="post-48561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48561-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys and thanks in advance. I have a 8 gb RAM centos 6.6 machine. I'm trying to install nominatim and indexing european map.. I follow the simple instructions oon wiki guide and, until yesterday, everything seems going fine..</p>
<p>But yesterday when I do <code>tail -f</code> on log file I saw:</p>
<pre><code>Done 54357951 in 1416077 @ 38.386295 per second - Rank 30 ETA (seconds): 136114.046875
Done 54358077 in 1416078 @ 38.386356 per second - Rank 30 ETA (seconds): 136110.546875
Done 54358206 in 1416078 @ 38.386448 per second - Rank 30 ETA (seconds): 136106.859375</code></pre>
<p>After some hours (and after a day) I repeat the <code>tail -f</code> and same output appear, last row is the same:</p>
<pre><code>Done 54358206 in 1416078 @ 38.386448 per second - Rank 30 ETA (seconds): 136106.859375</code></pre>
<p>and no progress is been done..</p>
<p>In the other log file (I redirected the output to two file) I can see:</p>
<pre><code>.....................................................................................
Reanalysing database...
ANALYZE
Please download osmosis.
If it is already installed, check the path in your local settings (settings/local.php) file.
ANALYZE
ANALYZE</code></pre>
<p>What does it mean?? Please say me thats everything goes fine... I started this indexing process approx a month ago..</p>
<hr />
<p>Are you sure?? because the log show the line below:</p>
<pre><code>Done 54358206 in 1416078 @ 38.386448 per second - Rank 30 ETA (seconds): 136106.859375</code></pre>
<p>as last line from 3 days...</p>
<p>If I launch the <code>ps auxw|grep postgres</code> I can see some postgres process (for example vacuum, write ecc..) but if I launch <code>ps -aux | more</code> I can't see no process about nominatim or about the original map import command <code>nohup ./utils/setup.php --osm-file &lt;planet file&gt; --all --osm2pgsql-cache 18000 2&gt;&gt;err.log 1&gt;&gt;setup.log &amp;</code></p>
<p>The output of <code>select * from pg_stat_activity</code> is:</p>
<pre><code>postgres=# select * from pg_stat_activity;
datid | datname  |  pid  | usesysid | usename  | application_name | client_addr
| client_hostname | client_port |         backend_start         |          xact
_start           |          query_start          |         state_change
| waiting | state  | backend_xid | backend_xmin |              query
&#10;-------+----------+-------+----------+----------+------------------+------------
-+-----------------+-------------+-------------------------------+--------------
-----------------+-------------------------------+------------------------------
-+---------+--------+-------------+--------------+------------------------------
---
13003 | postgres | 14967 |       10 | postgres | psql             |
|                 |          -1 | 2016-03-09 12:25:49.719568+01 | 2016-03-09 12
:26:01.184549+01 | 2016-03-09 12:26:01.184549+01 | 2016-03-09 12:26:01.184556+01
| f       | active |             |     80287794 | select * from pg_stat_activit
y;
(1 row)</code></pre>
<p>Do you really think is everything ok??</p>
<p>Thanks a lot Mark</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-europe" rel="tag" title="see questions tagged &#39;europe&#39;">europe</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '16, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/8b8afc2fa4a72009fdf51409cd072c87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbies&#39;s gravatar image" />
<p><span>newbies</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbies has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '16, 11:29</strong> </span></p>
</div>
</div>
<div id="comments-container-48561" class="comments-container">
&#10;</div>
<div id="comment-tools-48561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48561-form-container" class="comment-form-container">
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

<span id="48571"></span>

<div id="answer-container-48571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48571-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Everything is fine. The database still needs to create some indexes most likely (ps auxw|grep postgres will show a couple busy PostgreSQL processes).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48571" class="comments-container">
<span id="48573"></span>
<div id="comment-48573" class="comment">
<div id="post-48573-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Still having the same last line with the same ETA after a day seems strange, doesn't it?</p>
</div>
<div id="comment-48573-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 14:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48571-form-container" class="comment-form-container">
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

