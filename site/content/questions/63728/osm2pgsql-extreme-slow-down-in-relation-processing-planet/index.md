+++
type = "question"
title = "OSM2PGSQL - Extreme Slow Down in Relation Processing - Planet"
description = '''Hi - I am trying to load a planet file into Postgres on a very fast University Networked VM and the relation processing speed is extremely slow. But in comparison the Node &amp;amp; Way processing seems to be very fast (when comparing to the OSM2PGSQL benchmarks). My current estimates for the Relation p...'''
date = "2018-05-25T09:52:00Z"
lastmod = "2018-05-28T11:11:00Z"
weight = 63728
keywords = [ "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/63728" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM2PGSQL - Extreme Slow Down in Relation Processing - Planet](/questions/63728/osm2pgsql-extreme-slow-down-in-relation-processing-planet)

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
<span id="post-63728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63728-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - I am trying to load a planet file into Postgres on a very fast University Networked VM and the relation processing speed is extremely slow. But in comparison the Node &amp; Way processing seems to be very fast (when comparing to the OSM2PGSQL benchmarks). My current estimates for the Relation processing to finish is near enough 20 days + !!! I have tried about 20 different loads with different settings - but always the relations are slow.</p>
<p><strong>Processing: Node(4512083k 5086.9k/s) Way(494141k 137.53k/s) Relation(40080 2.16/s)</strong></p>
<p>Can anyone point to an obvious mistake or error? Or provide some advice? I'm using the latest OSM2PGSQL build - 0.96.0 64bit ( I have tried 0.94 - but this was even slower)</p>
<p><strong>HARDWARE</strong></p>
<pre><code>Ubuntu 16.04 VM / 96GB RAM / 8 CPU / 2TB SAN Network</code></pre>
<p><strong>COMMAND</strong></p>
<p>osm2pgsql -v -l --unlogged --create --slim -C 30000 --number-processes 8 --flat-nodes /var/data_2/planet.nodes -S /usr/local/share/osm2pgsql/default.style --tablespace-slim-index index_space --tablespace-main-index index_space --hstore -d osm_planet -U osm planet-latest.osm.pbf</p>
<p><strong>PostgreSQL Settings</strong> <strong>- Version 9.6.8 / PostGIS 2.3.3</strong></p>
<pre><code>shared_buffers = 14GB
work_mem = 1GB
max_connections = 300
maintenance_work_mem = 8GB
effective_cache_size = 25GB
fsync = off
synchronous_commit = off
checkpoint_timeout = 1h
max_wal_size = 8GB
min_wal_size = 4GB
checkpoint_completion_target = 0.95
full_page_writes = off
autovacuum = off</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '18, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/23c610c873fb12824008d2d9e17c915b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike_de_funk&#39;s gravatar image" />
<p><span>mike_de_funk</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike_de_funk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63728" class="comments-container">
&#10;</div>
<div id="comment-tools-63728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63728-form-container" class="comment-form-container">
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

<span id="63730"></span>

<div id="answer-container-63730" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63730-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>a) the relation is slow slow because any associated geometries need to be built from the constituent relation members (just as way processing was slower than node processing).</p>
<p>b) the processing speeds up as the older relations tend to have more large ones and the fast to process ones (turn restrictions etc) tend to have become popular later on (you should have seen a similar effect during way processing).</p>
<p>c) I wouldn't set number-processors to 8 if you have 8 cores, you will have an additional database process per osm2pgsql thread and you may be overwhelming available memory</p>
<p>d) check that you are not swapping/paging (one time out is ok, back in not) and that you are not limited by the SAN, these days fast imports tend to run directly to local SSDs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '18, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '18, 13:40</strong> </span></p>
</div>
</div>
<div id="comments-container-63730" class="comments-container">
<span id="63732"></span>
<div id="comment-63732" class="comment">
<div id="post-63732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Simon - thanks for the reply.</p>
<p>a) I know that Relations would be slower - just not this slow. I did a full planet import over a year ago on much less powerful infrastructure and was getting ~100/s. this led to a successful import in just under 3 days.</p>
<p>c) The machine actually has 16 cores, but I will try an import with maybe 6 processes to see if it makes any difference.</p>
<p>d) I created a 20GB swap partition on the VM prior to the load and the system never uses any swap memory</p>
<p>Do you have any comments on the Postgres settings? Anything there that might be limiting?</p>
</div>
<div id="comment-63732-info" class="comment-info">
<span class="comment-age">(25 May '18, 12:31)</span> <span class="comment-user userinfo">mike_de_funk</span>
</div>
</div>
<span id="63734"></span>
<div id="comment-63734" class="comment">
<div id="post-63734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you check that the --flat-nodes file is actually being populated (and IMHO that definitely should be local), though you would notice that processing ways too? Modern versions of osm2pgsql are far better in caching so the -C 30000 can be a lot smaller, but as you said you are not swapping so that is unlikely to have an effect.</p>
<p>In general I would consider anything over two days for a full planet import on a machine half up to the job is too long, so I agree with you there. But I haven't seen any thing in your config that would cause any such problems, so I would continue to suspect the SAN.</p>
</div>
<div id="comment-63734-info" class="comment-info">
<span class="comment-age">(25 May '18, 13:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="63783"></span>
<div id="comment-63783" class="comment">
<div id="post-63783-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Simon</p>
<p>I spoke to our infrastructure team at the University - they spun up another VM but this time with "direct access" to the SAN. I'm not an infrastructure specialist but they said it's using ceph rather than iscsi.</p>
<p>I kicked off a new planet load and the difference was huge. Full planet import in 16 hours :)</p>
<p>Processing: Node(4512083k 3689.4k/s) Way(494141k 114.12k/s) Relation(5827810 456.22/s)</p>
<p>Thanks for your help - but it just looks like it was a hardware issue.</p>
</div>
<div id="comment-63783-info" class="comment-info">
<span class="comment-age">(28 May '18, 11:11)</span> <span class="comment-user userinfo">mike_de_funk</span>
</div>
</div>
</div>
<div id="comment-tools-63730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63730-form-container" class="comment-form-container">
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

