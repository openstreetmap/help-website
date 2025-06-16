+++
type = "question"
title = "Slow pre-rendering with generate_tiles_multiprocess.py"
description = '''I have successfully imported europe-latest.osm.pbf in postgresql 10. Now I am using generate_tiles_multiprocess.py (NUM_THREADS=10) to prerender tiles. I have prerendered europe zoom 0-7. That went fine (but that are not that many tiles). Now I am trying to prerender individual countries (zoom 8-17)...'''
date = "2019-09-13T16:55:00Z"
lastmod = "2019-09-16T21:58:00Z"
weight = 70763
keywords = [ "generate_tiles", "postgresql", "mapnik" ]
aliases = [ "/questions/70763" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow pre-rendering with generate_tiles_multiprocess.py](/questions/70763/slow-pre-rendering-with-generate_tiles_multiprocesspy)

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
<span id="post-70763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70763-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have successfully imported europe-latest.osm.pbf in postgresql 10.</p>
<p>Now I am using generate_tiles_multiprocess.py (NUM_THREADS=10) to prerender tiles. I have prerendered europe zoom 0-7. That went fine (but that are not that many tiles).</p>
<p>Now I am trying to prerender individual countries (zoom 8-17) (Netherlands for example) but even such a small country takes very long. I have it running now for 6 hours and it has generated 6000 tiles which comes down to 3 seconds per tile (30s per tile per core). At this rate Netherlands will take weeks to finish.</p>
<p>The specs of my machine are:</p>
<p>i9-7900X CPU @ 3.30GHz 3.31 GHz (10 cores)</p>
<p>64 GB RAM</p>
<p>2 TB SSD</p>
<p>I have previously rendered a single province of the Netherlands on my 8 year old laptop (with that province being the only data in my postgresql db)(NUM_THREADS=4) and that went fine (effective 1 tile per 0.25s - 1s per tile per core). This leaves me to believe that postgresql is my bottleneck as my current machine is much faster but it has a lot more data to query.</p>
<p>I found a lot of information about how to tune postgresql when importing osm data, but little to nothing about best settings for rendering. Are there any settings that make a world of difference?</p>
<p>I have the following postgresql settings:</p>
<ul>
<li>work_mem 16MB</li>
<li>shared_buffers 128MB</li>
<li>effective_cache_size 4GB</li>
<li>maintenance_work_mem 265MB</li>
<li>autovacuum on</li>
</ul>
<p>What other settings are relevant? Which of these should I alter?</p>
<p>I also found some information about tuning the stylesheet queries but I am using the commonly used style openstreetmap-carto and was hoping that a greater mind than me had already optimized it.</p>
<p>Or are there any specific db indexes that I should create for this particular stylesheet that would speed things up?</p>
<p>When I look at top I see 16 postgres processes (not 10) that use between 45% en 65% cpu and use between 0,1% and 0,3% mem. It looks like it is not using much memory:</p>
<p>free -m:</p>
<pre><code>     total        used        free      shared  buff/cache   available</code></pre>
<p>Mem: 49739 6821 1836 528 41082 41791</p>
<p>Swap: 0 0 0</p>
<p>Does anyone know what my bottleneck is?</p>
<p>Last and I hope it is not too relevant. I am running Docker containers in VirtualBox (gave it 50GB RAM).</p>
<p>p.s. I read <a href="/questions/65115/solved-slow-pre-rendering-with-generate_tiles_multiprocesspy">https://help.openstreetmap.org/questions/65115/solved-slow-pre-rendering-with-generate_tiles_multiprocesspy</a> but I already imported without the -l option.</p>
<p>p.p.s. Here someone also prerenders europe: <a href="/questions/54560/slow-generation-of-tiles-for-whole-europe">https://help.openstreetmap.org/questions/54560/slow-generation-of-tiles-for-whole-europe</a> and he claims to generate half a million tiles over a night. That is 100 times faster than what I am seeing. This leaves me to believe that with better tuning I can gain a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '19, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/31cbcef9e1dd2923f15c35ab8cf690b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mg218&#39;s gravatar image" />
<p><span>mg218</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mg218 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '19, 10:09</strong> </span></p>
</div>
</div>
<div id="comments-container-70763" class="comments-container">
&#10;</div>
<div id="comment-tools-70763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70763-form-container" class="comment-form-container">
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

<span id="70764"></span>

<div id="answer-container-70764" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70764-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>3 seconds a tile for zooms 8-12 sound roughly what I'd expect. These involve huge numbers of not very selective SQL queries and therefore take a long time to run. Tiles for lower tiles should be a little faster as the queries will be more selective, but they produce more data. For these reasons most sites only pre-render low-zoom tiles periodically and the higher zoom tiles (metatiles) are only rendered on demand.</p>
<p>The latter case is because: a) doing them all takes a lot of time; b) it's a lot of tiles; and c) most of them will never be looked at.</p>
<p>If you log SQL queries on your postgres instance you may be able to see exactly how many queries are run per tile (or do a single tile render as per switch2osm). You can also grab the SQL and see if the actual query plan is not what you'd expect, but consider that individual queries are retrieving the highway network, railway network, water features, natural &amp; landuse, airports, place names, boundaries, some POIs etc. For low zoom metatiles covering much of NL this may mean table scans are used rather than indexes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '19, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70764" class="comments-container">
<span id="70765"></span>
<div id="comment-70765" class="comment">
<div id="post-70765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Effectively 1 tile is generated per 3 seconds, but it also means that 10 cores are busy and each takes 30s to generate 1 tile. Then it doesn't sound so fast anymore. Maybe that is a better way to look at it?</p>
</div>
<div id="comment-70765-info" class="comment-info">
<span class="comment-age">(13 Sep '19, 17:28)</span> <span class="comment-user userinfo">mg218</span>
</div>
</div>
<span id="70787"></span>
<div id="comment-70787" class="comment">
<div id="post-70787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here someone also prerenders europe: <a href="/questions/54560/slow-generation-of-tiles-for-whole-europe">https://help.openstreetmap.org/questions/54560/slow-generation-of-tiles-for-whole-europe</a> and he claims to generate half a million tiles over a night. That is 100 times faster than what I am seeing. This leaves me to believe that with better tuning I can gain a lot.</p>
</div>
<div id="comment-70787-info" class="comment-info">
<span class="comment-age">(15 Sep '19, 10:09)</span> <span class="comment-user userinfo">mg218</span>
</div>
</div>
<span id="70790"></span>
<div id="comment-70790" class="comment">
<div id="post-70790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I cant do your PostgreSQL DB optimisation for you. You need to do some standard DBA work. Get some query plans, see how much memory is allocated to each process (default is 4MB IIRC), look at other things like checkpoint interval etc.</p>
</div>
<div id="comment-70790-info" class="comment-info">
<span class="comment-age">(15 Sep '19, 15:31)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="70808"></span>
<div id="comment-70808" class="comment">
<div id="post-70808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I changed the 4 MB work_mem to 64 MB (did not see an improvement). I was hoping that as more people are tiling europe with the same openstreetmap-carto stylesheet, with data imported with osm2pgsql and a CPU with 10+ cores (all more or less standard) that good settings for postgresql would be well known and hopefully documented. But I find tons of info about good settings for importing but not so for tiling. And yes, I have very little know-how about database tuning so I fear that I don't know what I would be looking at. Until now I had never heard about checkpoint intervals to give you an idea how little I know about this aspect of IT.</p>
</div>
<div id="comment-70808-info" class="comment-info">
<span class="comment-age">(16 Sep '19, 21:58)</span> <span class="comment-user userinfo">mg218</span>
</div>
</div>
</div>
<div id="comment-tools-70764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70764-form-container" class="comment-form-container">
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

