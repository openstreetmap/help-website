+++
type = "question"
title = "index error when import planet data, psycopg2.errors.TriggeredDataChangeViolation"
description = '''When I try to import planet osm data into my local nominatim service, I got a postgres error on the &quot;--index&quot; step:  2020-12-07 09:20:59 == Index ranks 0 - 4 &#x27;/data/www/nominatim/Nominatim-3.5.2/nominatim/nominatim.py&#x27; --database nominatim --port 5432 --threads 15 -v --maxrank 4WARNING: Starting ind...'''
date = "2020-12-07T02:13:00Z"
lastmod = "2020-12-07T02:16:00Z"
weight = 77863
keywords = [ "import", "nominatim", "index" ]
aliases = [ "/questions/77863" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [index error when import planet data, psycopg2.errors.TriggeredDataChangeViolation](/questions/77863/index-error-when-import-planet-data-psycopg2errorstriggereddatachangeviolation)

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
<span id="post-77863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I try to import planet osm data into my local nominatim service, I got a postgres error on the "--index" step:</p>
<blockquote>
<p>2020-12-07 09:20:59 == Index ranks 0 - 4 '/data/www/nominatim/Nominatim-3.5.2/nominatim/nominatim.py' --database nominatim --port 5432 --threads 15 -v --maxrank 4WARNING: Starting indexing rank (0 to 4) using 15 threads WARNING: Starting rank 0 WARNING: Done 0/0 in 0 @ 0.000 per second - FINISHED rank 0 WARNING: Starting rank 1 WARNING: Done 0/0 in 0 @ 0.000 per second - FINISHED rank 1 WARNING: Starting rank 2 WARNING: Done 0/0 in 0 @ 0.000 per second - FINISHED rank 2 WARNING: Starting rank 3 WARNING: Done 0/0 in 0 @ 0.000 per second - FINISHED rank 3 WARNING: Starting rank 4 INFO: Done 100 in 0 @ 109289.617 per second - rank 4 ETA (seconds): 0.00 Traceback (most recent call last): File "/data/www/nominatim/Nominatim-3.5.2/nominatim/nominatim.py", line 326, in &lt;module&gt; Indexer(options).run() File "/data/www/nominatim/Nominatim-3.5.2/nominatim/nominatim.py", line 206, in run self.index(RankRunner(self.maxrank), 20) File "/data/www/nominatim/Nominatim-3.5.2/nominatim/nominatim.py", line 243, in index t.wait() File "/data/www/nominatim/Nominatim-3.5.2/nominatim/nominatim.py", line 133, in wait wait_select(self.conn) File "/data/www/nominatim/.local/lib/python3.6/site-packages/psycopg2/extras.py", line 778, in wait_select state = conn.poll() <strong>psycopg2.errors.TriggeredDataChangeViolation: tuple to be updated was already modified by an operation triggered by the current command</strong> HINT: Consider using an AFTER trigger instead of a BEFORE trigger to propagate changes to other rows.</p>
</blockquote>
<p>My local nominatim version is 3.5.2, installed following the instructions on <a href="https://www.nominatim.org/release-docs/latest/api/Overview/">link text</a>. The imported data is complete OSM Data downloaded from the osm planet.</p>
<p>Has anyone got the same error? Thanks for all advice!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '20, 02:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ec4bbc3ec516217b8006ddec87c42db3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveLiu1225&#39;s gravatar image" />
<p><span>SteveLiu1225</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveLiu1225 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77863" class="comments-container">
&#10;</div>
<div id="comment-tools-77863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77863-form-container" class="comment-form-container">
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

<span id="77864"></span>

<div id="answer-container-77864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77864-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/osm-search/Nominatim/issues/2045#issuecomment-722649872">https://github.com/osm-search/Nominatim/issues/2045#issuecomment-722649872</a> mentions the same error with 3.5.2 and a patch.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '20, 02:16</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-77864" class="comments-container">
&#10;</div>
<div id="comment-tools-77864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77864-form-container" class="comment-form-container">
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

