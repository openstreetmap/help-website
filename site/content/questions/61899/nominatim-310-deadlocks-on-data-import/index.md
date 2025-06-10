+++
type = "question"
title = "Nominatim 3.1.0: Deadlocks on data import"
description = '''Hello, I started data import from a planet file into Nominatim 3.1.0 and Postgres log contains the lines that follow. There were no deadlocks like this for importing via 2.5.1 and also at the end of the import DB size for 2.5.1 is larger by a few tens of gigabytes. Import run as: sudo -u nominatim ....'''
date = "2018-01-30T12:48:00Z"
lastmod = "2018-01-30T13:23:00Z"
weight = 61899
keywords = [ "import", "data_import", "deadlock", "postgresql", "nominatim" ]
aliases = [ "/questions/61899" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim 3.1.0: Deadlocks on data import](/questions/61899/nominatim-310-deadlocks-on-data-import)

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
<span id="post-61899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61899-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I started data import from a planet file into Nominatim 3.1.0 and Postgres log contains the lines that follow. There were no deadlocks like this for importing via 2.5.1 and also at the end of the import DB size for 2.5.1 is larger by a few tens of gigabytes.</p>
<p>Import run as: sudo -u nominatim ./utils/setup.php --osm-file /mnt/ephemeral/planet-latest.osm.pbf --all --osm2pgsql-cache 28000</p>
<p>Also I can see there are multiple threads for import process (several postgress connections) that I'd assume cause the deadlocks. So my questions are:</p>
<ul>
<li>are the deadlocks handled properly by the import script and data is consistent?</li>
<li>why data size is larger for Nominatim 2.5.1 while the same planet file is in use?</li>
</ul>
<p>Postgres log:</p>
<pre><code>2018-01-29 22:27:21 UTC [15707-73] LOG:  checkpoints are occurring too frequently (29 seconds apart)
2018-01-29 22:27:21 UTC [15707-74] HINT:  Consider increasing the configuration parameter &quot;max_wal_size&quot;.
Interrupt requested
2018-01-29 22:30:02 UTC [18513-1] ERROR:  canceling autovacuum task
2018-01-29 22:30:02 UTC [18513-2] CONTEXT:  automatic analyze of table &quot;nominatim.public.placex&quot;
2018-01-29 23:04:13 UTC [18699-1] nominatim@nominatim ERROR:  deadlock detected
2018-01-29 23:04:13 UTC [18699-2] nominatim@nominatim DETAIL:  Process 18699 waits for ShareLock on transaction 185788759; blocked by process 18698.
        Process 18698 waits for ShareLock on transaction 185788763; blocked by process 18699.
        Process 18699: update placex set indexed_status = 0 where place_id = $1
        Process 18698: update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:13 UTC [18699-3] nominatim@nominatim HINT:  See server log for query details.
2018-01-29 23:04:13 UTC [18699-4] nominatim@nominatim CONTEXT:  while locking tuple (3588611,16) in relation &quot;placex&quot;
        SQL statement &quot;UPDATE placex SET linked_place_id = NEW.place_id WHERE place_id = linked_node_id&quot;
        PL/pgSQL function placex_update() line 142 at SQL statement
2018-01-29 23:04:13 UTC [18699-5] nominatim@nominatim STATEMENT:  update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:14 UTC [18702-1] nominatim@nominatim ERROR:  deadlock detected
2018-01-29 23:04:14 UTC [18702-2] nominatim@nominatim DETAIL:  Process 18702 waits for ShareLock on transaction 185788759; blocked by process 18698.
        Process 18698 waits for ShareLock on transaction 185788758; blocked by process 18702.
        Process 18702: update placex set indexed_status = 0 where place_id = $1
        Process 18698: update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:14 UTC [18702-3] nominatim@nominatim HINT:  See server log for query details.
2018-01-29 23:04:14 UTC [18702-4] nominatim@nominatim CONTEXT:  while locking tuple (3588611,16) in relation &quot;placex&quot;
        SQL statement &quot;UPDATE placex SET linked_place_id = NEW.place_id WHERE place_id = linked_node_id&quot;
        PL/pgSQL function placex_update() line 142 at SQL statement
2018-01-29 23:04:14 UTC [18702-5] nominatim@nominatim STATEMENT:  update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:23 UTC [18696-1] nominatim@nominatim ERROR:  deadlock detected
2018-01-29 23:04:23 UTC [18696-2] nominatim@nominatim DETAIL:  Process 18696 waits for ShareLock on transaction 185789325; blocked by process 18701.
        Process 18701 waits for ShareLock on transaction 185789329; blocked by process 18696.
        Process 18696: update placex set indexed_status = 0 where place_id = $1
        Process 18701: update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:23 UTC [18696-3] nominatim@nominatim HINT:  See server log for query details.
2018-01-29 23:04:23 UTC [18696-4] nominatim@nominatim CONTEXT:  while locking tuple (1561131,10) in relation &quot;placex&quot;
        SQL statement &quot;UPDATE placex SET linked_place_id = NEW.place_id WHERE place_id = linked_node_id&quot;
        PL/pgSQL function placex_update() line 142 at SQL statement
2018-01-29 23:04:23 UTC [18696-5] nominatim@nominatim STATEMENT:  update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:50 UTC [18697-1] nominatim@nominatim ERROR:  deadlock detected
2018-01-29 23:04:50 UTC [18697-2] nominatim@nominatim DETAIL:  Process 18697 waits for ShareLock on transaction 185794891; blocked by process 18701.
        Process 18701 waits for ShareLock on transaction 185794892; blocked by process 18697.
        Process 18697: update placex set indexed_status = 0 where place_id = $1
        Process 18701: update placex set indexed_status = 0 where place_id = $1
2018-01-29 23:04:50 UTC [18697-3] nominatim@nominatim HINT:  See server log for query details.
2018-01-29 23:04:50 UTC [18697-4] nominatim@nominatim CONTEXT:  while locking tuple (4485156,18) in relation &quot;placex&quot;
        SQL statement &quot;UPDATE placex SET linked_place_id = NEW.place_id WHERE place_id = linked_node_id&quot;
        PL/pgSQL function placex_update() line 142 at SQL statement</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-data_import" rel="tag" title="see questions tagged &#39;data_import&#39;">data_import</span> <span class="post-tag tag-link-deadlock" rel="tag" title="see questions tagged &#39;deadlock&#39;">deadlock</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '18, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/34a9ff282bda047810fdbb874b6671b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Taras%20O&#39;s gravatar image" />
<p><span>Taras O</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Taras O has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '18, 12:49</strong> </span></p>
</div>
</div>
<div id="comments-container-61899" class="comments-container">
&#10;</div>
<div id="comment-tools-61899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61899-form-container" class="comment-form-container">
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

<span id="61901"></span>

<div id="answer-container-61901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61901-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>During import Nominatim detects deadlocks (before it used to crash). It's possible the detection logic simply got better. If I remember correctly it does string matching.</p>
<p>Check <code>SELECT indexed_status,count(*) FROM placex GROUP BY indexed_status;</code> in the <code>nominatim</code> database after the import, all records should be <code>0</code> (zero).</p>
<p>Nominatim 3.1 puts postcodes in different tables. <a href="https://www.openstreetmap.org/user/lonvia/diary/43143">https://www.openstreetmap.org/user/lonvia/diary/43143</a> On a planet database 10GB is less than 5% difference and expected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '18, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '18, 13:24</strong> </span></p>
</div>
</div>
<div id="comments-container-61901" class="comments-container">
&#10;</div>
<div id="comment-tools-61901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61901-form-container" class="comment-form-container">
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

