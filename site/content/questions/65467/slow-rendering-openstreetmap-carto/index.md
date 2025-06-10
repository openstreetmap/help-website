+++
type = "question"
title = "Slow rendering (openstreetmap-carto)"
description = '''Hello, I just set up a planet DB on my server, following the switch2osm tutorial (https://switch2osm.org/manually-building-a-tile-server-18-04-lts). I&#x27;m using the default openstreetmap-carto style. Tiles rendering is way too slow to be usable: I plan to pre-render up to zoom 12, and generating a sin...'''
date = "2018-08-20T17:15:00Z"
lastmod = "2018-08-22T22:43:00Z"
weight = 65467
keywords = [ "rendering", "slow", "postgresql" ]
aliases = [ "/questions/65467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow rendering (openstreetmap-carto)](/questions/65467/slow-rendering-openstreetmap-carto)

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
<span id="post-65467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65467-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I just set up a planet DB on my server, following the switch2osm tutorial (<a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts).">https://switch2osm.org/manually-building-a-tile-server-18-04-lts).</a> I'm using the default openstreetmap-carto style. Tiles rendering is way too slow to be usable: I plan to pre-render up to zoom 12, and generating a single metatile at zoom 13 takes 20 seconds. It still takes 6 seconds at zoom 16.</p>
<p>Here's what I've done so far to speed things up:</p>
<ul>
<li>put my DB on my server's SSD</li>
<li>execute the indexes.sql script (<a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/indexes.sql">https://github.com/gravitystorm/openstreetmap-carto/blob/master/indexes.sql</a> )</li>
<li>fine tune my PostgreSQL config and set my cpufreq-set to performance as recommended here: <a href="https://wiki.openstreetmap.org/wiki/User:Species/PostGIS_Tuning">https://wiki.openstreetmap.org/wiki/User:Species/PostGIS_Tuning</a></li>
</ul>
<p>What more should I do? I added below more information about my setup. Interestingly rendering durations with render_list seems fine (see below).</p>
<hr />
<p>Here's my server's config:</p>
<ul>
<li>Intel Core i7-8700 Hexa-Core (12 threads)</li>
<li>64 GB of RAM</li>
<li>2 TB SSD (for the DB)</li>
<li>2 * 6 TB HDD (set up in RAID 1, for the OS &amp; the tile cache)</li>
</ul>
<p>I imported the planet.pbf file using this command:</p>
<pre><code>time osm2pgsql -d gis --create --slim
-G --hstore -C 48000 --number-processes 6 \
     --tag-transform-script ~/src/map-styles/openstreetmap-carto/openstreetmap-carto.lua \
     --style ~/src/map-styles/openstreetmap-carto/openstreetmap-carto.style \
    planet-latest.osm.pbf</code></pre>
<p>It took 36 hours to complete, creating a DB of around 900 GB.</p>
<p>Here's what I added to my postgresql.conf:</p>
<pre><code>synchronous_commit = off
fsync = off
random_page_cost = 1.1
wal_buffers = 16MB
effective_cache_size = 48GB
maintenance_work_mem = 4GB
shared_buffers = 8MB
work_mem = 128MB
autovacuum = on
effective_io_concurrency = 200
max_connections = 300
checkpoint_completion_target = 0.7
default_statistics_target = 100
min_wal_size = 1GB
max_wal_size = 2GB
max_worker_processes = 12
max_parallel_workers_per_gather = 6
max_parallel_workers = 12</code></pre>
<p>I also changed my cpufreq-set with the following command:</p>
<pre><code>sudo cpufreq-set -g performance</code></pre>
<p>Here are some rendering durations I got with render_list. They seem fine to me:</p>
<ul>
<li>zooms 0 -&gt; 4: 13mn</li>
<li>zooms 5 -&gt; 6: 15mn</li>
<li>zooms 7: 13mn</li>
</ul>
<p>What more can I do? Are we supposed to create other indexes than the ones listed in the indexes.sql script?</p>
<p>I was expecting rendering performance to be something like 1-5 secs on that server (depending on the zoom level). Is that realistic?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '18, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a711e0129f307399a857a6f9b4bfd0e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timautin&#39;s gravatar image" />
<p><span>timautin</span><br />
<span class="score" title="151 reputation points">151</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timautin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '18, 19:34</strong> </span></p>
</div>
</div>
<div id="comments-container-65467" class="comments-container">
<span id="65468"></span>
<div id="comment-65468" class="comment">
<div id="post-65468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you add indexes to your database?</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/indexes.sql">https://github.com/gravitystorm/openstreetmap-carto/blob/master/indexes.sql</a></p>
<p>Low zoom tiles are slow to render anyway because of reading a lot of data, but that's probably too long.</p>
</div>
<div id="comment-65468-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 17:29)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65469"></span>
<div id="comment-65469" class="comment">
<div id="post-65469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your comment. As said in my question yes, I executed the indexes.sql script (it was taking half an hour before doing so). Yes it seems too slow to me. It should take less than a second at zoom 16, right?</p>
</div>
<div id="comment-65469-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 17:30)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="65470"></span>
<div id="comment-65470" class="comment">
<div id="post-65470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry TL;DR...</p>
<p>It's hard to say for me, because my render_speedtest numbers were taken with just one country in the database:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/1287#issuecomment-383266123">https://github.com/gravitystorm/openstreetmap-carto/issues/1287#issuecomment-383266123</a></p>
</div>
<div id="comment-65470-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 18:11)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65471"></span>
<div id="comment-65471" class="comment">
<div id="post-65471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'm running the test. Stuck at zoom 0 at the moment -_- ... It was very fast for a small extract (I did test with Azerbaidjan &amp; Corsica extracts, I was under the second all the time). I'm wondering if everything is indeed on the SSD, maybe some indexes are on the default partition, I need to find a way to check that.</p>
</div>
<div id="comment-65471-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 18:18)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="65472"></span>
<div id="comment-65472" class="comment">
<div id="post-65472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that without whole planet loaded it's kind of dry run test, because probably it renders empty places most of the time. But it's just a wild guess. Anyway, even dry run data can be usable in a limited way.</p>
</div>
<div id="comment-65472-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 18:59)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65474"></span>
<div id="comment-65474" class="comment not_top_scorer">
<div id="post-65474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well it's still stuck at zoom 0, I gave up. But the numbers you got seems good, I'd like to get the same. I moved the whole DB on the SSD (previously I was only using a table space), it didn't change anything.</p>
</div>
<div id="comment-65474-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 19:06)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="65475"></span>
<div id="comment-65475" class="comment not_top_scorer">
<div id="post-65475-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Might be worth noting that my cores are never at 100% (5-20%), and my RAM usage is always low (10GB out of my 64GB).</p>
</div>
<div id="comment-65475-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 19:18)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="65521"></span>
<div id="comment-65521" class="comment not_top_scorer">
<div id="post-65521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have an oldish import of Europe and I also experience big slowdowns. Importing does not take so long; last time it was a ~16TiB .pfb file that loaded in a couple of days (256TiB consumer grade SSD, 16GiB of RAM, not much tweaking on the PG side).</p>
<p>I do think that any performance test should be done with a big import, otherwise the penalties for continent/world levels aren't really felt. Current planet is at 41GiB, Europe 18GiB, N.America/Asia 7GiB, maybe something at least 1GiB?</p>
</div>
<div id="comment-65521-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 22:43)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
</div>
<div id="comment-tools-65467" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65467-form-container" class="comment-form-container">
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

<span id="65520"></span>

<div id="answer-container-65520" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have an oldish import of Europe and I also experience big slowdowns. Importing does not take so long; last time it was a ~16TiB .pfb file that loaded in a couple of days (256TiB consumer grade SSD, 16GiB of RAM, not much tweaking on the PG side).</p>
<p>I do think that any performance test should be done with a big import, otherwise the penalties for continent/world levels aren't really felt. Current planet is at 41GiB, Europe 18GiB, N.America/Asia 7GiB, maybe something at least 1GiB?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '18, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65520" class="comments-container">
&#10;</div>
<div id="comment-tools-65520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65520-form-container" class="comment-form-container">
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

