+++
type = "question"
title = "how to keep osm2pgsql from using swap"
description = '''Hello, I have successfully imported a planet file (Mar 04 2016) into postgres (9.4) using osm2pgsql (0.91.0-dev).  I have the following system: MOBO = SuperMicro DAL-i-O CPU = dual Xeon E5-2620V3 (24 cores total) RAM = 8x16G DDR4 ECC RDIMM (128 gig total) OS = Ubuntu 15.04 (I&#x27;m about to upgrade to 1...'''
date = "2016-05-06T08:18:00Z"
lastmod = "2018-08-08T07:16:00Z"
weight = 49588
keywords = [ "import", "osm2pgsql", "memory" ]
aliases = [ "/questions/49588" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to keep osm2pgsql from using swap](/questions/49588/how-to-keep-osm2pgsql-from-using-swap)

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
<span id="post-49588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49588-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have successfully imported a planet file (Mar 04 2016) into postgres (9.4) using osm2pgsql (0.91.0-dev).</p>
<p>I have the following system:</p>
<pre><code>MOBO = SuperMicro DAL-i-O
CPU = dual Xeon E5-2620V3 (24 cores total)
RAM = 8x16G DDR4 ECC RDIMM (128 gig total)
OS = Ubuntu 15.04 (I&#39;m about to upgrade to 16.04 so don&#39;t hate)</code></pre>
<p>The OS (as well as postgres database) lives on a 500GB (Samsung EVO) SSD (This drive has a 16GB swap partition.) The pbf planet file lives on a separate HDD. I also have a 1TB (Samsumg PRO) SSD where main_data, main_idx, slim_data, and slim_idx tablespaces are stored. Each tablespace is on its own partition which comes in handy when profiling with df and dstat (You really get a good picture of what is happening during the import.)</p>
<p>My postgresql.conf settings are all set to defaults except for:</p>
<pre><code>max_connections = 200
shared_buffers = 32GB
work_mem = 100MB
maintenance_work_mem = 48GB
effective_io_concurrency = 2
fsync = off
synchronous_commit = off
full_page_writes = off
wal_buffers = 1MB
checkpoint_segments = 1024
checkpoint_timeout = 1h
checkpoint_completion_target = 0.9
random_page_cost = 2.5
effective_cache_size = 60GB
autovacuum = off</code></pre>
<p>Note that the above settings are for IMPORT ONLY.</p>
<p>Here is a summary of the results:</p>
<pre><code>osm2pgsql -c -d gis -U maddoxw --number-processes 16 --slim -C 30000 --flat-nodes /var/lib/mod_tile/planet.cache --tablespace-main-data main_data --tablespace-main-index main_idx --tablespace-slim-data slim_data --tablespace-slim-index slim_idx /media/Borg_LS/terrain/osm/pbf/planet-latest.osm.pbf
osm2pgsql version 0.91.0-dev (64 bit id space)
&#10;Using built-in tag processing pipeline
Using projection SRS 3857 (Spherical Mercator)
Setting up table: planet_osm_point
Setting up table: planet_osm_line
Setting up table: planet_osm_polygon
Setting up table: planet_osm_roads
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=30000MB, maxblocks=480000*65536, allocation method=11
Mid: loading persistent node cache from /var/lib/mod_tile/planet.cache
Allocated space for persistent node cache file
Maximum node in persistent node cache: 0
Mid: pgsql, scale=100 cache=30000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /media/Borg_LS/terrain/osm/pbf/planet-latest.osm.pbf
Using PBF parser.
Processing: Node(3333342k 2100.4k/s) Way(344218k 62.62k/s) Relation(4175840 263.11/s)  parse time: 22955s
Node stats: total(3333342858), max(4145675901) in 1587s
Way stats: total(344218973), max(413214616) in 5497s
Relation stats: total(4175849), max(6168030) in 15871s
Maximum node in persistent node cache: 4146069503
&#10;Going over pending ways...
    231812682 ways are pending
&#10;Using 16 helper-processes
Finished processing 231812682 ways in 5223 s
&#10;231812682 Pending ways took 5223s at a rate of 44383.05/s
&#10;Going over pending relations...
    0 relations are pending
&#10;Using 16 helper-processes
Finished processing 0 relations in 0 s
&#10;All indexes on planet_osm_roads created in 592s
All indexes on planet_osm_point created in 3441s
All indexes on planet_osm_line created in 6995s
All indexes on planet_osm_polygon created in 11933s
Stopped table: planet_osm_nodes in 0s
Stopped table: planet_osm_ways in 16613s
Stopped table: planet_osm_rels in 119s
Maximum node in persistent node cache: 4146069503
node cache: stored: 3303017669(99.09%), storage efficiency: 84.00% (dense blocks: 449090, sparse nodes: 126610290), hit rate: 99.10%
&#10;Osm2pgsql took 56882s overall</code></pre>
<p>I monitored the whole install process with dstat and a homebrew script to record the results of df (and du) calls. I noticed that about 5 minutes into the "going over pending ways" section, my swap usage started climbing steadily. By the time I hit the "Building index on table: planet_osm_ways" section, the swap usage was 12GB and then 2 minutes into building the planet_osm_ways indexes the swap was completely full and stayed that way for the remainder of the import.</p>
<p>My postgresql memory settings (shared buffs, work mem, maintenance work mem, effective cache size) as well as the osm2pgsql cache setting were all calculated based on the wikis and the numerous forums and blog posts I've found. However, most of the suggestions I've seen are 2+ years old and none of them give good settings for systems with large SSDs and large amounts of RAM (I think 32GB is the largest system I've seen someone benchmark.) I've been experimenting with OSM imports for about 2 months now and have tried various combinations of the above settings, but have only recently (today) noticed that my swap is being used heavily.</p>
<p>Does anyone have any advice on how to best calculate the values of each of the memory settings such that osm2pgsql does not eat into the swap? For you experienced guys, do any of my settings look too high (or too low)?</p>
<p>Thanks,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '16, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/487645f035e9b2f095acf7510b32ce89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="placebo10&#39;s gravatar image" />
<p><span>placebo10</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="placebo10 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '16, 08:20</strong> </span></p>
</div>
</div>
<div id="comments-container-49588" class="comments-container">
<span id="65207"></span>
<div id="comment-65207" class="comment">
<div id="post-65207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am also wondering the best tuning settings for resource heavy databases. I have a lot of ram (50G) and IOPS available, and I wonder what the best settings area.</p>
</div>
<div id="comment-65207-info" class="comment-info">
<span class="comment-age">(08 Aug '18, 07:16)</span> <span class="comment-user userinfo">sprutner</span>
</div>
</div>
</div>
<div id="comment-tools-49588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49588-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

