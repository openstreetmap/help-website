+++
type = "question"
title = "osm2pgql - 7 days on &quot;Building index on table: planet_osm_ways&quot;"
description = '''Re-posted from stackoverflow: I&#x27;m importing the whole-planet OSM data set into PostgreSQL 9.6.2 on a Amazon EC2 i3.4xlarge (122 Gb mem, 16 CPUs) with the PostgreSQL data directory on a throughput-optimized 2TB volume. I have adjusted Postgres parameters like this (for the import):  shared_buffers = ...'''
date = "2017-05-01T14:35:00Z"
lastmod = "2017-05-11T14:52:00Z"
weight = 55971
keywords = [ "osm2pgsql", "planet_osm" ]
aliases = [ "/questions/55971" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgql - 7 days on "Building index on table: planet_osm_ways"](/questions/55971/osm2pgql-7-days-on-building-index-on-table-planet_osm_ways)

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
<span id="post-55971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55971-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Re-posted from stackoverflow:</p>
<p>I'm importing the whole-planet OSM data set into PostgreSQL 9.6.2 on a Amazon EC2 i3.4xlarge (122 Gb mem, 16 CPUs) with the PostgreSQL data directory on a throughput-optimized 2TB volume. I have adjusted Postgres parameters like this (for the import):</p>
<pre><code>shared_buffers = 4GB
work_mem = 100MB
fsync = off 
synchronous_commit = off
max_wal_size = 4GB
checkpoint_completion_target = 0.9</code></pre>
<p>I'm using <code>osm2pgsql</code> to execute the import. Here's the command:</p>
<p><code>osm2pgsql -c -d gis --number-processes 12 --slim -C 64000 --flat-nodes /data-cache/flat-node-cache/flat.nodes /data-postgres/planet-latest.osm.pbf</code></p>
<p>The initial steps of the import have gone extremely fast, but its been sitting at <code>Building index on table: planet_osm_ways</code> for days without change. <code>htop</code> indicates active Postgres processeses for <code>checkpoint process</code> and <code>CREATE INDEX</code>. When I log into Postgres and check <code>select * from pg_stat_activity;</code> I see an <code>active</code> state for <code>CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF) ;</code></p>
<p>Following the advice in this <a href="/questions/27587/data-import-stuck-at-create-index">post</a> I looked for the table <code>place</code>, but the response was <code>Did not find any relation named "place".</code></p>
<p>Does this sound normal? This is time-sensitive and having already been waiting the better part of a week, I am a little worried something has wrong. Are their other Postgres settings that could speed this part of the process?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '17, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/88d088c7b8b53519aa8026bd00ce121c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgwozdz&#39;s gravatar image" />
<p><span>rgwozdz</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgwozdz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55971" class="comments-container">
&#10;</div>
<div id="comment-tools-55971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55971-form-container" class="comment-form-container">
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

<span id="55976"></span>

<div id="answer-container-55976" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55976-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rgwozdz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How long did the rest of the import take? IMHO I would wait for the indexing to complete, it is a rather large part of the total time used, and will complete at some point in time.</p>
<p>Note: the reference to a place table is a red herring, that is used for imports in to the Nominatim schema, not the normal osm2pgsql tile rendering schema.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '17, 18:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '17, 20:23</strong> </span></p>
</div>
</div>
<div id="comments-container-55976" class="comments-container">
<span id="55977"></span>
<div id="comment-55977" class="comment">
<div id="post-55977-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> - the portion of the import prior to the phase it is currently on took about 24 hours.</p>
</div>
<div id="comment-55977-info" class="comment-info">
<span class="comment-age">(01 May '17, 18:37)</span> <span class="comment-user userinfo">rgwozdz</span>
</div>
</div>
<span id="56127"></span>
<div id="comment-56127" class="comment">
<div id="post-56127-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Eventually finished, took several more days. Failed on next step because max_connections were too low for that many processors. Success after increasing max_connections.</p>
</div>
<div id="comment-56127-info" class="comment-info">
<span class="comment-age">(11 May '17, 14:52)</span> <span class="comment-user userinfo">rgwozdz</span>
</div>
</div>
</div>
<div id="comment-tools-55976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55976-form-container" class="comment-form-container">
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

