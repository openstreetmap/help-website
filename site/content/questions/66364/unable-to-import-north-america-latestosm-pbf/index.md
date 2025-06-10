+++
type = "question"
title = "Unable to import north-america-latest.osm pbf"
description = '''We have a problem importing north-america-latest.osm to out map server VM which is 6 vCPU, 16 GB RAM and 550 GB storage. We tried to import Texas pbf, it works fine. And when we used these two different commands and in both case, the import failed with the coredump. osm2pgsql --slim -d gis -C 4000 /...'''
date = "2018-10-16T23:30:00Z"
lastmod = "2018-10-20T22:50:00Z"
weight = 66364
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/66364" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to import north-america-latest.osm pbf](/questions/66364/unable-to-import-north-america-latestosm-pbf)

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
<span id="post-66364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a problem importing north-america-latest.osm to out map server VM which is 6 vCPU, 16 GB RAM and 550 GB storage. We tried to import Texas pbf, it works fine. And when we used these two different commands and in both case, the import failed with the coredump.</p>
<pre><code>osm2pgsql --slim -d gis -C 4000 /mapdata/north-america-latest.osm.pbf
osm2pgsql --slim -d gis –C 1200 –number-processes 3 /tmp/north-america-latest.osm.pbf
&#10;HINT: In a moment you should be able to reconnect to the database and repeat your command.
terminate called after throwing an instance of &#39;std::runtime_error&#39;
what(): CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF) ;
failed: server closed the connection unexpectedly
This probably means the server terminated abnormally
before or while processing the request.
Aborted (core dumped)</code></pre>
<p>Then we tried to increase the "-C | --cache num" value to 12000 and 14000. Then in both cases, the import failed at the same step as below:</p>
<pre><code>bash-4.1$ osm2pgsql -d gis --slim -C 12000 /mapdata/north-america-latest.osm.pbf
osm2pgsql SVN version 0.88.2-dev (64 bit id space)
&#10;Using built-in tag processing pipeline
Using projection SRS 900913 (Spherical Mercator)
Setting up table: planet_osm_point
Setting up table: planet_osm_line
Setting up table: planet_osm_polygon
Setting up table: planet_osm_roads
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=12000MB, maxblocks=1536000*8192, allocation method=11
Mid: pgsql, scale=100 cache=12000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /mapdata/north-america-latest.osm.pbf
Processing: Node(870095k 259.3k/s) Way(61241k 14.44k/s) Relation(509320 68.81/s)
Standard exception processing relation id=6244046: TopologyException: side location conflict at -8427146.1899999995 5064220.8799999999
Processing: Node(870095k 259.3k/s) Way(61241k 14.44k/s) Relation(566160 71.63/s) parse time: 15501s
Node stats: total(870095450), max(4515939386) in 3356s
Way stats: total(61241977), max(455153763) in 4240s
Relation stats: total(566169), max(6729780) in 7905s
Committing transaction for planet_osm_point
Committing transaction for planet_osm_line
Committing transaction for planet_osm_polygon
Committing transaction for planet_osm_roads
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
Using built-in tag processing pipeline
&#10;Going over pending ways...
33693166 ways are pending
&#10;Using 1 helper-processes
Finished processing 33693166 ways in 20391 sec
&#10;33693166 Pending ways took 20391s at a rate of 1652.35/s
Committing transaction for planet_osm_point
Committing transaction for planet_osm_line
Committing transaction for planet_osm_polygon
Committing transaction for planet_osm_roads
&#10;Going over pending relations...
0 relations are pending
&#10;Using 1 helper-processes
Finished processing 0 relations in 0 sec
&#10;Committing transaction for planet_osm_point
WARNING: there is no transaction in progress
Committing transaction for planet_osm_line
WARNING: there is no transaction in progress
Committing transaction for planet_osm_polygon
WARNING: there is no transaction in progress
Committing transaction for planet_osm_roads
WARNING: there is no transaction in progress
Stopping table: planet_osm_nodes
Stopping table: planet_osm_ways
Building index on table: planet_osm_ways
Stopped table: planet_osm_nodes in 0s
Stopping table: planet_osm_rels
Building index on table: planet_osm_rels
Sorting data and creating indexes for planet_osm_polygon
Sorting data and creating indexes for planet_osm_point
Sorting data and creating indexes for planet_osm_line
Sorting data and creating indexes for planet_osm_roads
Stopped table: planet_osm_rels in 28s
Killed</code></pre>
<p>We checked the postgresql.conf, and we have the setting as below:</p>
<pre><code>shared_buffers = 256MB
work_mem = 512MB
maintenance_work_mem = 16GB
checkpoint_segments = 100
checkpoint_timeout = 10min
checkpoint_completion_target = 0.9
effective_cache_size = 24GB</code></pre>
<p>Any suggestion on how to fix this issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '18, 23:30</strong></p>
<img src="https://secure.gravatar.com/avatar/3b38e65d7347fe2ca02780c442a9e993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xming0819&#39;s gravatar image" />
<p><span>xming0819</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xming0819 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Oct '18, 07:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-66364" class="comments-container">
&#10;</div>
<div id="comment-tools-66364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66364-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="66367"></span>

<div id="answer-container-66367" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66367-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first message ("server closed the connection unexpectedly") means that your PostgreSQL server process has died. You might find more information in the postgresql.log or the kernel log ("dmesg" command). The second message ("Killed") likely points to an out-of-memory issue in osm2pgsql; the "dmesg" command might also shed some light on this.</p>
<p>Your VM does not have enough RAM. Increase the RAM if possible. If not, reduce <code>maintenance_work_mem</code> to 1 GB or even further. Set <code>--number-processes</code> to 1 since every parallel process consumes additional memory. Create a swap partition or swap file on your VM. All these steps will make the import much slower but at least you have a chance of it completing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '18, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66367" class="comments-container">
&#10;</div>
<div id="comment-tools-66367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66367-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66404"></span>

<div id="answer-container-66404" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66404-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your virtual machine is using SSD, then, as Frederik also recommended, simply increase your virtual machine's swap space by 16GB or so. It should hardly affect import speed with SSD.</p>
<p>I have successfully imported North America with that on a 16GB RAM laptop... just note you should leave out the -C cache option as well. Just leave osm2pgsql figure out its own optimal settings, it does an acceptable job.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '18, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '18, 22:52</strong> </span></p>
</div>
</div>
<div id="comments-container-66404" class="comments-container">
&#10;</div>
<div id="comment-tools-66404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66404-form-container" class="comment-form-container">
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

