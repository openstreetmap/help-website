+++
type = "question"
title = "Performance Tuning Osm2pgsql / Postgresql for first time import"
description = '''As a new user I have multiple questions, I will try to break it up by topic. Part 1 I am a new user of OSM and started building a tool to locate customers and group them by criteria. I had made some great progress on my project and then came in last Monday to find the OSM tile server very slow. Not ...'''
date = "2018-08-07T18:46:00Z"
lastmod = "2018-08-07T18:46:00Z"
weight = 65197
keywords = [ "import", "postgresql", "osm2pgsql", "performance" ]
aliases = [ "/questions/65197" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Performance Tuning Osm2pgsql / Postgresql for first time import](/questions/65197/performance-tuning-osm2pgsql-postgresql-for-first-time-import)

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
<span id="post-65197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As a new user I have multiple questions, I will try to break it up by topic.</p>
<h2 id="part-1">Part 1</h2>
<p>I am a new user of OSM and started building a tool to locate customers and group them by criteria. I had made some great progress on my project and then came in last Monday to find the OSM tile server very slow. Not knowing how common this is I started putting together my own server. I stumbled across this thread: <a href="https://help.openstreetmap.org/questions/65043/osm-slowdown">https://help.openstreetmap.org/questions/65043/osm-slowdown</a> which initially gives me the impression it is an unusual situation, but either way I happen to have a decent server available that isn't doing anything at the moment and so figured I could set it up anyway.</p>
<p>Server Specs:</p>
<ol>
<li>Dell R620</li>
<li>Perc H700</li>
<li>Dual X5680 @ 3.33GHz (6 core / 12 thread per processor)</li>
<li>192GB DDR3 RAM</li>
<li>4X 146GB 10K drives for OS</li>
<li>1 256GB PCIe m.2 SSD for /var</li>
<li>100GB Fiber Internet</li>
</ol>
<p>I started setting it up last week and had an issue where it slowed way down which I discussed on StackOverflow here: <a href="https://stackoverflow.com/questions/51625815/osm2pgsql-extremely-slow-on-import-on-server-with-192gb-ram">https://stackoverflow.com/questions/51625815/osm2pgsql-extremely-slow-on-import-on-server-with-192gb-ram</a></p>
<p>The issue initially looked to be related to a HDD that went bad in a RAID setup and I swapped it out for the SSD and using the shell script you see there I was able to import Alabama in about 300 seconds at a rate of between 300-400k points/second during the first command, then running the second command to --append it slowed way down again to 1k points/second. So while I did have an issue with the HDD, it doesn't seem to be the only bottleneck.</p>
<p>Is it better for me to import all of North America using the --create vs --append multiple states? Is there supposed to be that dramatic of a difference between them?</p>
<p>I opened the database using a GUI (Navicat) and opened the planet_osm_nodes table which opened quickly with 1000 records. I then asked for the last page to get an idea how many records were in it. It took over a minute to pull back page 416,338. Using iotop I noticed something unusual, it was WRITING to the disk drive at a speed of around 120MB/sec to give me the last page. Is this because of how my GUI is requesting those pages The select statement would be of the type <code>SELECT * FROM "public"."planet_osm_nodes" LIMIT 1000 OFFSET 416337000</code>? It just seems very odd to have it writing during a select statement.</p>
<p>I was visiting with a DBA from Micron over the weekend and talking about the import process and the topic of disabling foreign keys and indexes came up as a way to speed up an import into an empty DB. Does the Osm2pgsql script already do this? He was talking about the Postgresql ROLLBACK feature that lets you reverse commits. While this is a great idea during updates, for an initial DB load, it isn't really important for Postgresql to be keeping track of how to rollback, is there options to disable that within the import script rather than tweaking the server config?</p>
<p>This is a brand new installation of Ubuntu 16.04 without any data anyone needs to worry about preserving. With that in mind, what is the fastest method we could devise of importing these records. What is the postgresql.conf file supposed to look like for a server with those stats? Here is what I came up with, but I am sure it could be much better:</p>
<pre><code>data_directory = &#39;/var/lib/postgresql/9.5/main&#39;
hba_file = &#39;/etc/postgresql/9.5/main/pg_hba.conf&#39;
ident_file = &#39;/etc/postgresql/9.5/main/pg_ident.conf&#39;
external_pid_file = &#39;/var/run/postgresql/9.5-main.pid&#39;
port = 5432
max_connections = 300
unix_socket_directories = &#39;/var/run/postgresql&#39;
ssl = true
ssl_cert_file = &#39;/etc/ssl/certs/ssl-cert-snakeoil.pem&#39;
ssl_key_file = &#39;/etc/ssl/private/ssl-cert-snakeoil.key&#39;
shared_buffers = 14GB
work_mem = 1GB
maintenance_work_mem = 8GB
temp_buffers = 8GB
dynamic_shared_memory_type = sysv
max_files_per_process = 1000
effective_io_concurrency = 500
max_worker_processes = 8
checkpoint_timeout = 1h
max_wal_size = 5GB
min_wal_size = 1GB
checkpoint_completion_target = 0.9
random_page_cost = 1.1          effective_cache_size = 25GB
log_line_prefix = &#39;%t [%p-%l] %q%u@%d &#39;
log_timezone = &#39;Navajo&#39;
stats_temp_directory = &#39;/var/run/postgresql/9.5-main.pg_stat_tmp&#39;
autovacuum = off
datestyle = &#39;iso, mdy&#39;
timezone = &#39;Navajo&#39;
lc_messages = &#39;en_US.UTF-8&#39;
lc_monetary = &#39;en_US.UTF-8&#39;
lc_numeric = &#39;en_US.UTF-8&#39;
lc_time = &#39;en_US.UTF-8&#39;
default_text_search_config = &#39;pg_catalog.english&#39;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '18, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/644620e74a312b0ce02a0a1bb1bae155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlanHalls&#39;s gravatar image" />
<p><span>AlanHalls</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlanHalls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65197" class="comments-container">
&#10;</div>
<div id="comment-tools-65197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65197-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

