+++
type = "question"
title = "Complete import job after disk out of space - indexes"
description = '''Hi,  I started the full planet import, and after a week of work the job was ALMOST done, failed during building indexes after the import was probably done, but the harddrive run out of space.  1) Is there a way how I can just rebuild the indexes without reimporting the whole set? By running commands...'''
date = "2021-02-08T13:32:00Z"
lastmod = "2021-02-15T07:57:00Z"
weight = 78728
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/78728" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Complete import job after disk out of space - indexes](/questions/78728/complete-import-job-after-disk-out-of-space-indexes)

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
<span id="post-78728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78728-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I started the full planet import, and after a week of work the job was ALMOST done, failed during building indexes after the import was probably done, but the harddrive run out of space.</p>
<p>1) Is there a way how I can just rebuild the indexes without reimporting the whole set? By running commands directly in PGSQL I guess? Where? How? (i know how to use command line sql tool, but not skilled in PGSQL, just MySQL)</p>
<p>2) I did the import with autovacuum=off. Is there any way I can run it now to save some additional space?</p>
<p>Here is the docker log.</p>
<pre><code>sudo -u renderer osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script /home/renderer/src/openstreetm                                                                                                                        ap-carto/openstreetmap-carto.lua --number-processes 8 -S /home/renderer/src/openstreetmap-carto/openstreetmap-carto.s                                                                                                                        tyle /data.osm.pbf -C 32000 --flat-nodes /nodes/flat_nodes.bin
2021-01-30 17:39:17  osm2pgsql version 1.4.0
2021-01-30 17:39:17  Database version: 12.5 (Ubuntu 12.5-1.pgdg18.04+1)
2021-01-30 17:39:17  PostGIS version: 3.0
2021-01-30 17:39:17  Node-cache: cache=32000MB, maxblocks=512000*65536, allocation method=11
2021-01-30 17:39:17  Setting up table &#39;planet_osm_point&#39;
2021-01-30 17:39:17  Setting up table &#39;planet_osm_line&#39;
2021-01-30 17:39:17  Setting up table &#39;planet_osm_polygon&#39;
2021-01-30 17:39:17  Setting up table &#39;planet_osm_roads&#39;
2021-02-07 22:53:59  Reading input files done in 710082s (197h 14m 42s).      4/s)
2021-02-07 22:53:59    Processed 6634698177 nodes in 5524s (1h 32m 4s) - 1201k/s
2021-02-07 22:53:59    Processed 733743019 ways in 303789s (84h 23m 9s) - 2k/s
2021-02-07 22:53:59    Processed 8593984 relations in 400769s (111h 19m 29s) - 21/s
2021-02-07 22:54:00  Clustering table &#39;planet_osm_polygon&#39; by geometry...
2021-02-07 22:54:00  Clustering table &#39;planet_osm_point&#39; by geometry...
2021-02-07 22:54:00  Clustering table &#39;planet_osm_line&#39; by geometry...
2021-02-07 22:54:00  Clustering table &#39;planet_osm_roads&#39; by geometry...
2021-02-07 22:54:01  Building index on table &#39;planet_osm_ways&#39;
2021-02-07 22:54:01  Building index on table &#39;planet_osm_rels&#39;
2021-02-08 05:14:21  node cache: stored: 3812666007(57.47%), storage efficiency: 90.90% (dense blocks: 472519, sparse nodes: 161717496), hit rate: 56.10%
2021-02-08 05:14:24  ERROR: Database error: ERROR:  could not extend file &quot;base/16385/5832519.8&quot;: No space left on device
HINT:  Check free disk space.</code></pre>
<p>Postgres log from within the docker:</p>
<pre><code>2021-01-30 17:39:17.177 UTC [75] postgres@gis STATEMENT:  CREATE EXTENSION hstore;
2021-02-08 01:45:40.776 UTC [161] renderer@gis ERROR:  could not extend file &quot;base/16385/5832515.2&quot;: No space left on device
2021-02-08 01:45:40.776 UTC [161] renderer@gis HINT:  Check free disk space.
2021-02-08 01:45:40.776 UTC [161] renderer@gis STATEMENT:  CREATE INDEX ON planet_osm_rels USING GIN (parts)  WITH (fastupdate = off) ;
&#10;2021-02-08 01:45:40.776 UTC [127] renderer@gis ERROR:  could not extend file &quot;base/16385/5832517&quot;: No space left on device
2021-02-08 01:45:40.776 UTC [127] renderer@gis HINT:  Check free disk space.
2021-02-08 01:45:40.776 UTC [127] renderer@gis STATEMENT:  CREATE TABLE &quot;planet_osm_roads_tmp&quot;  AS SELECT * FROM &quot;planet_osm_roads&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:40.776 UTC [124] renderer@gis ERROR:  could not extend file &quot;base/16385/5832519.8&quot;: No space left on device
2021-02-08 01:45:40.776 UTC [124] renderer@gis HINT:  Check free disk space.
2021-02-08 01:45:40.776 UTC [124] renderer@gis STATEMENT:  CREATE TABLE &quot;planet_osm_point_tmp&quot;  AS SELECT * FROM &quot;planet_osm_point&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:40.776 UTC [125] renderer@gis ERROR:  could not write to file &quot;base/pgsql_tmp/pgsql_tmp125.10&quot;: No space left on device
2021-02-08 01:45:40.776 UTC [125] renderer@gis STATEMENT:  CREATE TABLE &quot;planet_osm_line_tmp&quot;  AS SELECT * FROM &quot;planet_osm_line&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:41.541 UTC [167] FATAL:  terminating connection due to administrator command
2021-02-08 01:45:41.541 UTC [167] STATEMENT:  CREATE TABLE &quot;planet_osm_point_tmp&quot;  AS SELECT * FROM &quot;planet_osm_point&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:41.542 UTC [168] FATAL:  terminating connection due to administrator command
2021-02-08 01:45:41.542 UTC [168] STATEMENT:  CREATE TABLE &quot;planet_osm_roads_tmp&quot;  AS SELECT * FROM &quot;planet_osm_roads&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:41.570 UTC [165] FATAL:  terminating connection due to administrator command
2021-02-08 01:45:41.570 UTC [165] STATEMENT:  CREATE TABLE &quot;planet_osm_line_tmp&quot;  AS SELECT * FROM &quot;planet_osm_line&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:41.588 UTC [166] FATAL:  terminating connection due to administrator command
2021-02-08 01:45:41.588 UTC [166] STATEMENT:  CREATE TABLE &quot;planet_osm_point_tmp&quot;  AS SELECT * FROM &quot;planet_osm_point&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:41.589 UTC [164] FATAL:  terminating connection due to administrator command
2021-02-08 01:45:41.589 UTC [164] STATEMENT:  CREATE TABLE &quot;planet_osm_line_tmp&quot;  AS SELECT * FROM &quot;planet_osm_line&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 01:45:44.565 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 167) exited with exit code 1
2021-02-08 01:45:44.565 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 166) exited with exit code 1
2021-02-08 01:45:44.570 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 168) exited with exit code 1
2021-02-08 01:45:44.683 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 165) exited with exit code 1
2021-02-08 01:45:45.182 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 164) exited with exit code 1
2021-02-08 05:12:16.096 UTC [160] renderer@gis ERROR:  could not extend file &quot;base/16385/5832514.10&quot;: wrote only 4096 of 8192 bytes at block 1441264
2021-02-08 05:12:16.096 UTC [160] renderer@gis HINT:  Check free disk space.
2021-02-08 05:12:16.096 UTC [160] renderer@gis STATEMENT:  CREATE INDEX ON planet_osm_ways USING GIN (nodes)  WITH (fastupdate = off) ;
&#10;2021-02-08 05:14:15.671 UTC [126] renderer@gis ERROR:  could not write to file &quot;base/pgsql_tmp/pgsql_tmp126.30&quot;: No space left on device
2021-02-08 05:14:15.671 UTC [126] renderer@gis STATEMENT:  CREATE TABLE &quot;planet_osm_polygon_tmp&quot;  AS SELECT * FROM &quot;planet_osm_polygon&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 05:14:15.672 UTC [163] FATAL:  terminating connection due to administrator command
2021-02-08 05:14:15.672 UTC [163] STATEMENT:  CREATE TABLE &quot;planet_osm_polygon_tmp&quot;  AS SELECT * FROM &quot;planet_osm_polygon&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 05:14:15.699 UTC [162] ERROR:  could not write to file &quot;base/pgsql_tmp/pgsql_tmp162.29&quot;: No space left on device
2021-02-08 05:14:15.699 UTC [162] STATEMENT:  CREATE TABLE &quot;planet_osm_polygon_tmp&quot;  AS SELECT * FROM &quot;planet_osm_polygon&quot; WHERE ST_IsValid(way) ORDER BY way
2021-02-08 05:14:18.877 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 163) exited with exit code 1
2021-02-08 05:14:19.022 UTC [27] LOG:  background worker &quot;parallel worker&quot; (PID 162) exited with exit code 1</code></pre>
<p>Thank you! Radek</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '21, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/6ea6fb11ea43f247e60f7ad3d4c22733?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Palalet&#39;s gravatar image" />
<p><span>Palalet</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Palalet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78728" class="comments-container">
&#10;</div>
<div id="comment-tools-78728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78728-form-container" class="comment-form-container">
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

<span id="78729"></span>

<div id="answer-container-78729" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78729-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Palalet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A typical osm2pgsql 1.4 run would create these indexes:</p>
<p><code>CREATE INDEX planet_osm_line_osm_id_idx ON public.planet_osm_line USING btree (osm_id); CREATE INDEX planet_osm_line_way_idx ON public.planet_osm_line USING gist (way); CREATE INDEX planet_osm_point_osm_id_idx ON public.planet_osm_point USING btree (osm_id); CREATE INDEX planet_osm_point_way_idx ON public.planet_osm_point USING gist (way); CREATE INDEX planet_osm_polygon_osm_id_idx ON public.planet_osm_polygon USING btree (osm_id); CREATE INDEX planet_osm_polygon_way_idx ON public.planet_osm_polygon USING gist (way); CREATE INDEX planet_osm_rels_parts_idx ON public.planet_osm_rels USING gin (parts) WITH (fastupdate=off); CREATE INDEX planet_osm_roads_osm_id_idx ON public.planet_osm_roads USING btree (osm_id); CREATE INDEX planet_osm_roads_way_idx ON public.planet_osm_roads USING gist (way); CREATE INDEX planet_osm_ways_nodes_idx ON public.planet_osm_ways USING gin (nodes) WITH (fastupdate=off);</code></p>
<p>You can probably just run these commands and they will simply fail where the index already exists. After that your database should be good to go, but remember that many map styles will require the creation of additional indexes for performance.</p>
<p>You can switch on autovacuum before running the above commands if you want. It is unlikely to save space though. If you have a world-wide database, the planet_osm_ways_nodes index can easily use 200 GB of space. osm2pgsql 1.4 has a somewhat experimental feature where it allows you to reduce the size of that index at the cost of a little performance degradation during data updates (see option <code>--middle-way-node-index-id-shift</code>). Note that your database is likely going to grow by 30% within a few weeks if you run continuous updates due to database and index bloat, so be sure to have enough room.</p>
<p>Of course if you don't need data updates at all then you can save a lot of space by dropping the tables <code>planet_osm_ways</code> and <code>planet_osm_rels</code> and omitting their indexes from the list, and you can also omit the four "btree(osm_id)" indexes on the other tables and delete the flatnodes file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '21, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78729" class="comments-container">
<span id="78730"></span>
<div id="comment-78730" class="comment">
<div id="post-78730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, will run the indexes and see what happens :) I do not plan to update it way too often, I rather need some basic map data source for my other work, no need to be 100% up to date. Didnt expect this to grow up to some 600Gb during the work, and I do not want to loose one week of procesing :) This is too much new technologies for me, appreciate your help!</p>
</div>
<div id="comment-78730-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 14:12)</span> <span class="comment-user userinfo">Palalet</span>
</div>
</div>
<span id="78837"></span>
<div id="comment-78837" class="comment">
<div id="post-78837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well, I am unable to finish the task :( I did most of the indexes, but when I run the</p>
<p>CREATE INDEX planet_osm_ways_nodes_idx ON public.planet_osm_ways USING gin (nodes) WITH (fastupdate=off);</p>
<p>command, I get into trouble. The table is 160Gb, and running the index command takes up another 280Gb of space, before I had to kill it just before I run out of space again. Is this normal, that building the index takes x times more space than the original table? I tried to have them on separate tablespaces, one for data, one for index, but no help, it just eats up all available space :(</p>
</div>
<div id="comment-78837-info" class="comment-info">
<span class="comment-age">(13 Feb '21, 20:20)</span> <span class="comment-user userinfo">Palalet</span>
</div>
</div>
<span id="78843"></span>
<div id="comment-78843" class="comment">
<div id="post-78843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is normal. I suggest to do what I said above under "of course if you don't need..." - just drop the tables required for updates, and don't create the planet_osm_ways_nodes index at all. You'll be fine for rendering, and you can worry about loading new data later. Your disk is too small for running a continuously updated planet. (Unless, perhaps, you try the experimental osm2pgsql option also mentioned above, or maybe try a zfs compressed file system.)</p>
</div>
<div id="comment-78843-info" class="comment-info">
<span class="comment-age">(14 Feb '21, 11:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="78854"></span>
<div id="comment-78854" class="comment">
<div id="post-78854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, I will do it as you say, I cannot keep up with this space consumption :) - the table is 160Gb, while the complete index (yes, I made it after all) is 321Gb, which is utter nonsense :( so it would need some 800Gb+ to do the whole import</p>
</div>
<div id="comment-78854-info" class="comment-info">
<span class="comment-age">(15 Feb '21, 06:47)</span> <span class="comment-user userinfo">Palalet</span>
</div>
</div>
<span id="78855"></span>
<div id="comment-78855" class="comment">
<div id="post-78855-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw, is there a documentation which table contain what, what is their purpose? Where can I get the information which tables do I need just for the render and for the import? Also, not sure what role plays the flatnodes file, you mentioned I can delete it, so I guess is is some "temporary table" that is created during the transformation from the OSM file to final Postgres tables?</p>
</div>
<div id="comment-78855-info" class="comment-info">
<span class="comment-age">(15 Feb '21, 07:57)</span> <span class="comment-user userinfo">Palalet</span>
</div>
</div>
</div>
<div id="comment-tools-78729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78729-form-container" class="comment-form-container">
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

