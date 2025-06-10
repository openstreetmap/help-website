+++
type = "question"
title = "Why has my daily update stopped working?"
description = '''I have a daily cron job that updates the Great Britain extract in my PostGIS database using data from Geofabrik. The command is osmosis -q --read-replication-interval workingDirectory=$HOME/maps/replication --write-pgsql-change database=osm  and the configuration file is # -*- default-generic -*-  #...'''
date = "2017-02-15T20:33:00Z"
lastmod = "2017-02-15T21:47:00Z"
weight = 54657
keywords = [ "great-britain", "replication", "geofabrik", "osmosis" ]
aliases = [ "/questions/54657" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why has my daily update stopped working?](/questions/54657/why-has-my-daily-update-stopped-working)

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
<span id="post-54657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a daily cron job that updates the Great Britain extract in my PostGIS database using data from Geofabrik. The command is</p>
<pre><code>osmosis -q --read-replication-interval workingDirectory=$HOME/maps/replication --write-pgsql-change database=osm</code></pre>
<p>and the configuration file is</p>
<pre><code># -*- default-generic -*-
&#10;# The URL of the directory containing change files.
baseUrl=http://download.geofabrik.de/europe/great-britain-updates/
&#10;# Defines the maximum time interval in seconds to download in a single invocation.
# Setting to 0 disables this feature.
#maxInterval = 0
maxInterval = 86400</code></pre>
<p>(I had to set <code>maxInterval</code> early on, to take only one update at a time, but now even setting it to <code>100</code> isn't helping).</p>
<p>This has worked very nicely for the last few years, but recently it has started failing with</p>
<pre><code>org.springframework.dao.DuplicateKeyException: PreparedStatementCallback; SQL [INSERT INTO actions(data_type, action, id) VALUES(?, ?, ?)]; ERROR: duplicate key value violates unique constraint &quot;pk_actions&quot;
  Detail: Key (data_type, id)=(N, 469786539) already exists.; nested exception is org.postgresql.util.PSQLException: ERROR: duplicate key value violates unique constraint &quot;pk_actions&quot;
  Detail: Key (data_type, id)=(N, 469786539) already exists.</code></pre>
<p>It's as if items are being thrown into <code>actions</code> but without taking account of the version numbers or something. When I connect using the <code>psql</code> client, the <code>actions</code> table is empty, so it's not a matter of stale data causing the problem.</p>
<p>If it helps, my <code>state.txt</code> now has</p>
<pre><code>#Fri Feb 03 05:31:32 UTC 2017
sequenceNumber=1415
timestamp=2017-02-01T21\:21\:02Z</code></pre>
<p>How can I get my database updating again?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-great-britain" rel="tag" title="see questions tagged &#39;great-britain&#39;">great-britain</span> <span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '17, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8407ef33938bc29aeac67781527f8323?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tms13&#39;s gravatar image" />
<p><span>tms13</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tms13 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54657" class="comments-container">
&#10;</div>
<div id="comment-tools-54657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54657-form-container" class="comment-form-container">
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

<span id="54658"></span>

<div id="answer-container-54658" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54658-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tms13 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be a side effect of the switch to a new extract software at Geofabrik. The download dataset was re-synced with a current planet file at the time. This apparently led to some diff files containing some objects twice. This doesn't hurt osm2pgsql imports but trips up osmosis. Either re-initialize your database from a current data set, or use the --simplify-change flag in Osmosis to flatten the diff before applying to the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '17, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54658" class="comments-container">
<span id="54659"></span>
<div id="comment-54659" class="comment">
<div id="post-54659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect - I put <code>--simplify-change</code> immediately before <code>--write-pgsql-change</code> and it worked! I still need the <code>maxInterval</code>, else it fails with "Pipeline entities are not sorted", but I can probably live with that.</p>
</div>
<div id="comment-54659-info" class="comment-info">
<span class="comment-age">(15 Feb '17, 21:47)</span> <span class="comment-user userinfo">tms13</span>
</div>
</div>
</div>
<div id="comment-tools-54658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54658-form-container" class="comment-form-container">
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

