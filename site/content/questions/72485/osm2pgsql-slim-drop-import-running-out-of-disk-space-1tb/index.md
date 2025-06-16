+++
type = "question"
title = "osm2pgsql --slim --drop import running out of disk space ( 1TB)"
description = '''Hi all, Unfortunately planet.osm.pbf osm2pgsql import crashed because of disk space lack (1TB available). What I don&#x27;t understand is that I used --slim --drop options and, after osm2pgsql crash, only 30% of disk space is used (259GB). So I guess the unecessary tables were already dropped when osm2pg...'''
date = "2020-01-13T12:14:00Z"
lastmod = "2020-01-22T14:07:00Z"
weight = 72485
keywords = [ "planet", "import", "postgresql", "osm2pgsql", "disk_usage" ]
aliases = [ "/questions/72485" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql --slim --drop import running out of disk space ( 1TB)](/questions/72485/osm2pgsql-slim-drop-import-running-out-of-disk-space-1tb)

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
<span id="post-72485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72485-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Unfortunately <code>planet.osm.pbf</code> osm2pgsql import crashed because of disk space lack (1TB available).</p>
<p>What I don't understand is that I used <strong>--slim --drop</strong> options and, after osm2pgsql crash, only 30% of disk space is used (259GB). So I guess the unecessary tables were already dropped when osm2pgsql went out of disk space. I don't think osm2pgsql need more than 700GB, even temporary, to build indexes.</p>
<p>I would like to relaunch the import, do you have any advice to use less disk space ? maybe</p>
<ul>
<li>use <code>--flat-nodes</code> osm2pgsql option ? if yes: do you think 1TB will be sufficent for node file + database ? or I should try to host node file on another 500GB disk ? Can you confirm that <code>--drop</code> osm2pgsql option will drop the node file at the end of the process ?</li>
<li>turn on <code>autovaccum</code> as suggested here <a href="/questions/52672/osm2pgsql-import-disk-space-running-out-during-index-creation">osm2pgsql import - disk space running out during index creation</a> ?</li>
</ul>
<p>In fact I got 916GB available, minus planet.osm.pbf file (50GB), so I got ~865GB. If it's confirmed that it is not sufficient for a full planet import, I'll add the information to this post ( <a href="/questions/64405/tile-server-hardware-requirements">Tile server hardware requirements</a> ).</p>
<p>Below are more informations, thanks in advance for your help !</p>
<p>Augustin</p>
<h3 id="osm2pgsql-command">osm2pgsql command</h3>
<p><code>osm2pgsql --username $DBPG_USER --database $DBPG_DB \ --hstore \ --style $WORKING_DIR/openstreetmap-carto/openstreetmap-carto.style \ --tag-transform-script $WORKING_DIR/openstreetmap-carto/openstreetmap-carto.lua \ --slim --drop \ --cache 18800 \ --number-processes 4 \ --multi-geometry 20200102_planet.osm.pbf</code></p>
<h3 id="system">system</h3>
<p><code>OS Debian 9 Stretch Architecture x86_64 Processor model: Intel(R) Core(TM) i5-6500 CPU @ 3.20GHz 4 cores (1 thread per core) 32GB RAM/32GB swap disk space: 1To SSD</code></p>
<h3 id="postgresql.conf-extract-postgresql-version-10">postgresql.conf extract (PostgreSQL version: 10)</h3>
<p><code>shared_buffers = 8GB work_mem = 50MB maintenance_work_mem = 1GB min_wal_size = 1G max_wal_size = 2GB effective_cache_size = 20GB</code></p>
<h3 id="osm2pgsql-logs-extract-vs.-disk-space-usage">osm2pgsql logs extract vs. disk space usage</h3>
<p>On january 9th at 6pm, osm2pgsql was still processing relations</p>
<p><code>Processing: Node(5682827k 291.6k/s) Way(630406k 5.06k/s) Relation(3798620 120.78/s)</code></p>
<p>and 78% of disk space was used:</p>
<p><code>Filesystem Size Used Avail Use% Mounted on /dev/sda1 916G 670G 200G 78% /var/lib/postgresql/data</code></p>
<p>On january 10th at 8pm osm2pgsql crashed because of lack of disk space (logs below) whereas only 30% disk space is used</p>
<p><code>Filesystem Size Used Avail Use% Mounted on /dev/sda1 916G 259G 612G 30% /data</code></p>
<p>here are osm2pgsql logs with the crash:</p>
<p><code>Using PBF parser. Processing: Node(5682827k 291.6k/s) Way(630406k 5.06k/s) Relation(5590480 140.30/s) Standard exception processing relation id=8346358: TopologyException: side location conflict at 721638.68999999994 1016915.5699999999 Processing: Node(5682827k 291.6k/s) Way(630406k 5.06k/s) Relation(7379160 155.86/s) parse time: 191305s Node stats: total(5682827154), max(7094416299) in 19487s Way stats: total(630406201), max(759474335) in 124474s Relation stats: total(7379167), max(10509928) in 47344s Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction for planet_osm_polygon Committing transaction for planet_osm_roads Setting up table: planet_osm_nodes Setting up table: planet_osm_ways Setting up table: planet_osm_rels Using lua based tag processing pipeline with script /docker_mounted_volumes/working_dir/openstreetmap-carto/openstreetmap-carto.lua Setting up table: planet_osm_nodes Setting up table: planet_osm_ways Setting up table: planet_osm_rels Using lua based tag processing pipeline with script /docker_mounted_volumes/working_dir/openstreetmap-carto/openstreetmap-carto.lua Setting up table: planet_osm_nodes Setting up table: planet_osm_ways Setting up table: planet_osm_rels Using lua based tag processing pipeline with script /docker_mounted_volumes/working_dir/openstreetmap-carto/openstreetmap-carto.lua Setting up table: planet_osm_nodes Setting up table: planet_osm_ways Setting up table: planet_osm_rels Using lua based tag processing pipeline with script /docker_mounted_volumes/working_dir/openstreetmap-carto/openstreetmap-carto.lua Going over pending ways... 434307049 ways are pending Using 4 helper-processes Finished processing 434307049 ways in 71654 s 434307049 Pending ways took 71654s at a rate of 6061.17/s Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction for planet_osm_polygon Committing transaction for planet_osm_roads Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction for planet_osm_polygon Committing transaction for planet_osm_roads Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction for planet_osm_polygon Committing transaction for planet_osm_roads Committing transaction for planet_osm_point Committing transaction for planet_osm_line Committing transaction for planet_osm_polygon Committing transaction for planet_osm_roads Going over pending relations... 0 relations are pending Using 4 helper-processes Finished processing 0 relations in 0 s Committing transaction for planet_osm_point WARNING: there is no transaction in progress Committing transaction for planet_osm_line WARNING: there is no transaction in progress Committing transaction for planet_osm_polygon WARNING: there is no transaction in progress Committing transaction for planet_osm_roads WARNING: there is no transaction in progress Committing transaction for planet_osm_point WARNING: there is no transaction in progress Committing transaction for planet_osm_line WARNING: there is no transaction in progress Committing transaction for planet_osm_polygon WARNING: there is no transaction in progress Committing transaction for planet_osm_roads WARNING: there is no transaction in progress Committing transaction for planet_osm_point WARNING: there is no transaction in progress Committing transaction for planet_osm_line WARNING: there is no transaction in progress Committing transaction for planet_osm_polygon WARNING: there is no transaction in progress Committing transaction for planet_osm_roads WARNING: there is no transaction in progress Committing transaction for planet_osm_point WARNING: there is no transaction in progress Committing transaction for planet_osm_line WARNING: there is no transaction in progress Committing transaction for planet_osm_polygon WARNING: there is no transaction in progress Committing transaction for planet_osm_roads WARNING: there is no transaction in progress Sorting data and creating indexes for planet_osm_point Sorting data and creating indexes for planet_osm_line Sorting data and creating indexes for planet_osm_polygon Stopping table: planet_osm_nodes Sorting data and creating indexes for planet_osm_roads Stopping table: planet_osm_ways Stopping table: planet_osm_rels Stopped table: planet_osm_rels in 0s Stopped table: planet_osm_nodes in 1s Stopped table: planet_osm_ways in 1s Copying planet_osm_roads to cluster by geometry finished Creating geometry index on planet_osm_roads Creating indexes on planet_osm_roads finished All indexes on planet_osm_roads created in 2661s Completed planet_osm_roads node cache: stored: 2266194517(39.88%), storage efficiency: 91.97% (dense blocks: 275092, sparse nodes: 105299977), hit rate: 38.95% Osm2pgsql failed due to ERROR: CREATE TABLE planet_osm_point_tmp AS SELECT * FROM planet_osm_point ORDER BY ST_GeoHash(ST_Transform(ST_Envelope(way),4326),10) COLLATE "C" failed: ERROR: could not extend file "base/16385/4462032.9": wrote only 4096 of 8192 bytes at block 1292910 HINT: Check free disk space.</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '20, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-72485" class="comments-container">
&#10;</div>
<div id="comment-tools-72485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72485-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="72486"></span>

<div id="answer-container-72486" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72486-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="augustind has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>865 GB is imho not enough anymore, but I'm not using --drop. I would strongly adise to keep the planet.osm.pbf somewhere else as well as using --flat-nodes (about 50 GB in size) and keeping the flat-nodes bin somewhere else (extra drive).</p>
<p>I recently did an import with 1.1 TB free space (used for postgresql db + flat-node file), the planet.osm.pbf was on another drive) and that worked (and probably won't work anymore in 2021).</p>
<p>You could as well look into the fs you are using. ZFS offers compression and would help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '20, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '20, 12:30</strong> </span></p>
</div>
</div>
<div id="comments-container-72486" class="comments-container">
<span id="72487"></span>
<div id="comment-72487" class="comment">
<div id="post-72487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot Spiekerooger for your quick answer. I'll try to relaunch the import with your advices:</p>
<ul>
<li>use <code>--flat-nodes</code> and host the node file on the system disk (500GB)</li>
<li>host the <code>planet.osm.pbf</code> on the system disk also</li>
<li>keep hosting the database on the extra disk (1TB)</li>
</ul>
<p>I'll come back here to report what happened !</p>
</div>
<div id="comment-72487-info" class="comment-info">
<span class="comment-age">(13 Jan '20, 12:53)</span> <span class="comment-user userinfo">augustind</span>
</div>
</div>
<span id="72490"></span>
<div id="comment-72490" class="comment">
<div id="post-72490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just had a look in my statistics: with a ZFS filesystem and ZFS compression turned on I maxed at 692 GB incl. the flat-nodes file during import (index building I think) on a recent import (without the --drop option and with autovacuum on).</p>
<p>Right now the db plus flat-nodes file takes up about 530GB after the import and after some --append updates.</p>
<p>With ext4 and about ~ 900GB free space for db + flat-node file I ran into the same probs you have on a first import (but again, I'm not using the --drop option).</p>
</div>
<div id="comment-72490-info" class="comment-info">
<span class="comment-age">(13 Jan '20, 14:24)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72498"></span>
<div id="comment-72498" class="comment">
<div id="post-72498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for these benchmarks.</p>
<p>So let's go for ZFS. Following <a href="http://www.paulnorman.ca/blog/2014/11/zfs-settings-for-osm2pgsql/">Paul’s Blog - ZFS Settings for Osm2pgsql</a> recommendations, I would like to use ZFS to convert my 1TB disk (currently ext4, mounted on /data) with lz4 compression enabled and a 8Kb recordsize.</p>
<p>As I'm not very familiar with filesystems and don't know zf4, does somebody could confirm that below approach is approximately correct (source: <a href="https://wiki.debian.org/ZFS)">https://wiki.debian.org/ZFS)</a> ?</p>
<ul>
<li>Umount current ext4 disk</li>
</ul>
<p><code>umount /data rm -r /data</code></p>
<ul>
<li>Debian ZF4 installation</li>
</ul>
<p><code>apt update apt install linux-headers-`uname -r` apt install -t buster-backports dkms spl-dkms apt install -t buster-backports zfs-dkms zfsutils-linux</code></p>
<ul>
<li>Creating a single disk stripe pool</li>
</ul>
<p><code>zpool create ashift=8 tank /dev/sda</code></p>
<ul>
<li>Provisioning file systems or volume</li>
</ul>
<p><code>mkdir -p /data zfs create -o mountpoint=/data tank/data</code></p>
<ul>
<li>Enable lz4 compression</li>
</ul>
<p><code>zfs set compression=lz4 tank</code></p>
</div>
<div id="comment-72498-info" class="comment-info">
<span class="comment-age">(14 Jan '20, 11:37)</span> <span class="comment-user userinfo">augustind</span>
</div>
</div>
<span id="72499"></span>
<div id="comment-72499" class="comment">
<div id="post-72499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the /dev/sda (are you sure about that, especially the sda?) is the extra 1TB drive where you plan to keep the db, this sounds about ok. You may have to format the drive before using zpool. Personally I wouldn't even create an exta filesystem under the zfs pool but just create the pool directly as "data".</p>
<p>so I would just:</p>
<ul>
<li>zpool create ashift=8 data /dev/sda</li>
<li>zfs set compression=lz4 data</li>
</ul>
<p>(without the extra zfs create in between).</p>
<p>By that, the pool should be mounted under /data directly.</p>
<p>But I don't know what else you are planing for that drive, so you may go ahead with your plan.</p>
</div>
<div id="comment-72499-info" class="comment-info">
<span class="comment-age">(14 Jan '20, 12:34)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="72612"></span>
<div id="comment-72612" class="comment">
<div id="post-72612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Finally it has worked like below for ZFS compression. For the whole conclusion, see answer at the bottom of the ticket. Thanks.</p>
<p>Be careful: <code>ashift</code> option evoked above is not the good one to set <code>recordsize</code>.</p>
<p><code>bash sudo su - cat &lt;&lt;'EOF' &gt; /etc/apt/sources.list.d/backports.list \# Backports repository deb </code><a href="http://deb.debian.org/debian"><code>http://deb.debian.org/debian</code></a><code> stretch-backports main contrib non-free # disponible après la publication de buster EOF apt update apt install linux-headers-`uname -r` apt install -t stretch-backports dkms spl-dkms apt install -t stretch-backports zfs-dkms zfsutils-linux</code></p>
<ul>
<li>Erase disk first 100M (<code>lsblk</code> to find name)</li>
</ul>
<p><code>bash dd if=/dev/zero of=/dev/sda bs=1M count=100</code></p>
<ul>
<li>Then</li>
</ul>
<p><code>bash zpool create data $disk_id \# use legacy mode is not required zfs set mountpoint=legacy data mount -t zfs /dev/sda1 /data/ df -khT /data/ \# check zfs list \# set compression and recordsize zfs set compression=lz4 data zfs set recordsize=8k data \# check zfs get recordsize /data zfs get compression /data</code></p>
</div>
<div id="comment-72612-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 14:03)</span> <span class="comment-user userinfo">augustind</span>
</div>
</div>
<span id="72613"></span>
<div id="comment-72613" class="comment not_top_scorer">
<div id="post-72613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ups, yes, actually I'm using set recordsize as well and not ashift.</p>
<p>Glad you got it running.</p>
</div>
<div id="comment-72613-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 14:07)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-72486" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-72486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72491"></span>

<div id="answer-container-72491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72491-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-72491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Run your import with <code>--disable-parallel-indexing</code> to save disk space.</p>
<p>Why? You ran out of disk space in the final stage of osm2pgsql where tables are sorted and indexes are created. In order to sort the tables, Postgresql needs to make a complete copy of the table. So you temporarily need twice the size of the table on disk. To speed things up, osm2pgsql runs parallel threads that do the sorting and indexing. At the worst case it therefore sorts all tables in parallel, so that you need twice the disk space you would actually need in the end. <code>--disable-parallel-indexing</code> ensures that sorting and index creation is done sequentially. It will take longer and you still need some additional space for the sorting but your current disk should be enough.</p>
<p>Regarding the <code>--drop</code> option: when enabled, tables that are only needed for updates get dropped early and some indexes are not even created in the first place. Therefore a lot less space is needed. Note though that this is only true for newer versions of osm2pgsql. The 0.92 version that ships with stretch is still badly optimised in this regard.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '20, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-72491" class="comments-container">
<span id="72497"></span>
<div id="comment-72497" class="comment">
<div id="post-72497-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/2921/lonvia">@lonvia</a> for your answer! It's pretty interesting. I've upgraded osm2pgsql from 0.92 to 1.2.0. Regarding <code>--disable-parallel-indexing</code> I keep it in mind as a fallback solution: I'd like to not give up speed aspect.</p>
</div>
<div id="comment-72497-info" class="comment-info">
<span class="comment-age">(14 Jan '20, 11:30)</span> <span class="comment-user userinfo">augustind</span>
</div>
</div>
</div>
<div id="comment-tools-72491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72491-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72611"></span>

<div id="answer-container-72611" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72611-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Thanks everybody for your help, the import was successful :) What has been changed for this second import:</p>
<ul>
<li>use <code>--flat-nodes</code> and host the nodes.cache file on another disk</li>
<li>move <code>planet.osm.pbf</code> to another disk too</li>
<li>upgrade from osm2pgsql 0.92 to 1.2.0</li>
<li>use a ZFS filesystem with <code>lz4</code> compression and <code>recordsize=8k</code></li>
</ul>
<p>Benchmark details here: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks#Desktop_Debian_9.2C_4_cores_i5-6500_CPU_.40_3.20GHz.2F32GB_RAM.2C_1TB.2B500GB_SSD_.28hstore_slim_drop_flat-nodes_and_ZFS_filesystem.29">Wiki OSM / Osm2pgsql Benchmarks / Desktop Debian 9, 4 cores i5-6500 CPU @ 3.20GHz/32GB RAM, 1TB+500GB SSD (hstore slim drop flat-nodes and ZFS filesystem)</a></p>
<p>About PostgreSQL/PostGIS OSM database (on ZFS filesystem): peak usage 460 GB, end size: 185 GB.</p>
<p>The source code of the related project has been just released on Github: <a href="https://github.com/Magellium/osmtilemaker">osmtilemaker</a> (generate your OSM tiles (one shot, no updates).)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '20, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-72611" class="comments-container">
&#10;</div>
<div id="comment-tools-72611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72611-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72488"></span>

<div id="answer-container-72488" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72488-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After <a href="https://help.openstreetmap.org/users/17439/spiekerooger">@Spiekerooger</a> answer, it could be nice if somebody else could provide some explanations about <strong>how the <code>--drop</code> option impact the disk usage over the osm2pgsql import time ?</strong> Particularly:</p>
<ul>
<li>does it impact the disk space peak usage ?</li>
<li>or it's just impacting the final disk space usage ?</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '20, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-72488" class="comments-container">
&#10;</div>
<div id="comment-tools-72488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72488-form-container" class="comment-form-container">
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

