+++
type = "question"
title = "Nominatim Index Creation Stuck"
description = '''I am running a Nominatim install on an EC2 instance with 1TB SSD, 6 processors and 64GB memory for the planet. The process has been running for about a week now. After rank creation, which finished about two days back, the install is stuck at index creation. When I queried pg_stat_activity, I see be...'''
date = "2019-12-31T17:58:00Z"
lastmod = "2020-01-01T16:58:00Z"
weight = 72303
keywords = [ "nominatim", "osm", "osm2pgsql" ]
aliases = [ "/questions/72303" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Index Creation Stuck](/questions/72303/nominatim-index-creation-stuck)

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
<span id="post-72303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running a Nominatim install on an EC2 instance with 1TB SSD, 6 processors and 64GB memory for the planet. The process has been running for about a week now. After rank creation, which finished about two days back, the install is stuck at index creation. When I queried pg_stat_activity, I see below as the currently active query:</p>
<pre><code>CREATE INDEX CONCURRENTLY idx_placex_rank_address ON placex USING BTREE (rank_address);</code></pre>
<p>This has started two days ago and still active. On the list of indexes that are created here: <a href="https://github.com/openstreetmap/Nominatim/blob/3b4ffea690fdbc84623916f968bee2ba15ee681b/sql/indices.src.sql">https://github.com/openstreetmap/Nominatim/blob/3b4ffea690fdbc84623916f968bee2ba15ee681b/sql/indices.src.sql</a>, this particular index is creation appears before some other spatial indexes. Does that suggest the install will go on for another week or so?</p>
<p>Strangely, I don't see the cpu or the ram being utilised by Postgres. CPU is at about 1% usage and memory below 1GB in usage. Do you think the installation is stuk for some reason? When I queried place and placex tables I see some indexes there but not all in indices.src.sql; if for some reason, the process is stuck, can I stop the process and build the remaining indexes manually according to indices.src.sql?</p>
<p><strong>Update</strong></p>
<p>When I checked pg_stat_activity after 8 hours, I saw now the active query is to create a different index from <a href="https://github.com/openstreetmap/Nominatim/blob/3b4ffea690fdbc84623916f968bee2ba15ee681b/sql/indices_search.src.sql">here</a>. Both the linked sql files have a comment mentioning, <strong><em>These indices are created only after the indexing process is done</em></strong>. Does this mean if I don't care for forward geocoding or search (I am only interested in reverse geo look ups), if I stop the process now I should be fine?</p>
<p><strong>Update</strong></p>
<p>Finally the entire process finished in 8 days opposed to the 2 days that is given in the official installation instructions</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Dec '19, 17:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3fa98831cef96f8b9fb7530160338da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="picmate&#39;s gravatar image" />
<p><span>picmate</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="picmate has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jan '20, 16:20</strong> </span></p>
</div>
</div>
<div id="comments-container-72303" class="comments-container">
<span id="72304"></span>
<div id="comment-72304" class="comment">
<div id="post-72304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How much OSM data are you using? Is it a small extract, a country, or the whole planet? The answer may not help with whether the process is stuck or not, but it could explain how long the process is expected to take.</p>
</div>
<div id="comment-72304-info" class="comment-info">
<span class="comment-age">(31 Dec '19, 18:18)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="72305"></span>
<div id="comment-72305" class="comment">
<div id="post-72305-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is the planet. Thanks</p>
</div>
<div id="comment-72305-info" class="comment-info">
<span class="comment-age">(31 Dec '19, 20:06)</span> <span class="comment-user userinfo">picmate</span>
</div>
</div>
</div>
<div id="comment-tools-72303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72303-form-container" class="comment-form-container">
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

<span id="72306"></span>

<div id="answer-container-72306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sounds much like <a href="https://github.com/openstreetmap/Nominatim/issues/1476">https://github.com/openstreetmap/Nominatim/issues/1476</a> If that's the case you need to watch the progress and possibly kill the autovacuum several time. After the installation run <a href="https://github.com/openstreetmap/Nominatim/blob/master/utils/check_import_finished.php">https://github.com/openstreetmap/Nominatim/blob/master/utils/check_import_finished.php</a> to make sure all required indices got created.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '19, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72306" class="comments-container">
<span id="72309"></span>
<div id="comment-72309" class="comment">
<div id="post-72309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, could you take a look at the update I added to the question?</p>
</div>
<div id="comment-72309-info" class="comment-info">
<span class="comment-age">(01 Jan '20, 03:09)</span> <span class="comment-user userinfo">picmate</span>
</div>
</div>
<span id="72315"></span>
<div id="comment-72315" class="comment">
<div id="post-72315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The setup.php supports a --reverse-only parameter (<a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/).">http://nominatim.org/release-docs/latest/admin/Import-and-Update/).</a> If you look into <a href="https://github.com/openstreetmap/Nominatim/blob/master/lib/setup/SetupClass.php">https://github.com/openstreetmap/Nominatim/blob/master/lib/setup/SetupClass.php</a> you'll see a couple of indices (those in /sql/indices_search.src.sql) are skipped. The one you mentioned in the original question, idx_placex_rank_address, is needed for reverse.</p>
</div>
<div id="comment-72315-info" class="comment-info">
<span class="comment-age">(01 Jan '20, 12:35)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="72317"></span>
<div id="comment-72317" class="comment">
<div id="post-72317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It finished after 8 days. Thanks for the info</p>
</div>
<div id="comment-72317-info" class="comment-info">
<span class="comment-age">(01 Jan '20, 16:58)</span> <span class="comment-user userinfo">picmate</span>
</div>
</div>
</div>
<div id="comment-tools-72306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72306-form-container" class="comment-form-container">
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

