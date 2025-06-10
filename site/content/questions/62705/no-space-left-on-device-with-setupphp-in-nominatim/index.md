+++
type = "question"
title = "No space left on device with setup.php in Nominatim"
description = '''I&#x27;m trying to use the north-america-latest.osm.pbf file, around 40GB. I expect a total disk usage of 400(ish) GB. ./utils/setup.php --osm-file /3TB/nominatim/north-america-latest.osm.pbf --all --osm2pgsql-cache 24000 --threads 8 2&amp;gt;&amp;amp;1 | tee setup.log When running the setup, I get ./utils/setup...'''
date = "2018-03-16T21:34:00Z"
lastmod = "2018-04-11T23:08:00Z"
weight = 62705
keywords = [ "setup.php", "nominatim" ]
aliases = [ "/questions/62705" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [No space left on device with setup.php in Nominatim](/questions/62705/no-space-left-on-device-with-setupphp-in-nominatim)

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
<span id="post-62705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use the <code>north-america-latest.osm.pbf</code> file, around 40GB. I expect a total disk usage of 400(ish) GB.</p>
<p><code>./utils/setup.php --osm-file /3TB/nominatim/north-america-latest.osm.pbf --all --osm2pgsql-cache 24000 --threads 8 2&gt;&amp;1 | tee setup.log</code></p>
<p>When running the setup, I get</p>
<pre><code>./utils/setup.php   --osm-file /3TB/nominatim/north-america-latest.osm.pbf   --all --osm2pgsql-cache 24000 --threads 8 2&gt;&amp;1   | tee setup.log
2018-03-16 20:35:16 == Create DB
2018-03-16 20:35:17 == Setup DB
Postgres version found: 9.6
Postgis version found: 2.3
2018-03-16 20:35:19 == WARNING: external UK postcode table not found.
2018-03-16 20:35:20 == Import data
osm2pgsql version 0.93.0-dev (64 bit id space)
&#10;Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=24000MB, maxblocks=384000*65536, allocation method=11
Mid: pgsql, cache=24000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /3TB/nominatim/north-america-latest.osm.pbf
Using PBF parser.
Processing: Node(966941k 786.8k/s) Way(72862k 84.72k/s) Relation(0 0.00/s)COPY_END for COPY planet_osm_ways FROM STDIN;
 failed: ERROR:  could not extend file &quot;base/292375/295704.6&quot;: No space left on device
HINT:  Check free disk space.
CONTEXT:  COPY planet_osm_ways, line 15312860
&#10;Error occurred, cleaning up
ERROR: Error executing external command: /srv/nominatim/Nominatim-3.1.0/build/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore --number-processes 1 -C 24000 -P 5432 -d nominatim /3TB/nominatim/north-america-latest.osm.pbf
Error executing external command: /srv/nominatim/Nominatim-3.1.0/build/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore --number-processes 1 -C 24000 -P 5432 -d nominatim /3TB/nominatim/north-america-latest.osm.pbf</code></pre>
<p>I've already created a default tablesplace on the 3TB drive for PostGre, but somehow my (tiny) root partitions gets filled after 30ish minutes. How can I change this apparent tmp path?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup.php" rel="tag" title="see questions tagged &#39;setup.php&#39;">setup.php</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '18, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/5a3b2450568b2e986fe909dcb0f51f63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="otter-in-a-suit&#39;s gravatar image" />
<p><span>otter-in-a-suit</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="otter-in-a-suit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62705" class="comments-container">
&#10;</div>
<div id="comment-tools-62705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62705-form-container" class="comment-form-container">
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

<span id="62707"></span>

<div id="answer-container-62707" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62707-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="otter-in-a-suit has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like your default tablespace setting was ignored. You can tell Nominatim to explicitly move part or all of the database into a different tablespace through its configuration. To move all data, add something like that to your <code>settings/local/php</code>:</p>
<p><code>@define('CONST_Tablespace_Osm2pgsql_Data', 'bigTS'); @define('CONST_Tablespace_Osm2pgsql_Index', 'bigTS'); @define('CONST_Tablespace_Place_Data', 'bigTS'); @define('CONST_Tablespace_Place_Index', 'bigTS'); @define('CONST_Tablespace_Address_Data', 'bigTS'); @define('CONST_Tablespace_Address_Index', 'bigTS'); @define('CONST_Tablespace_Search_Data', 'bigTS'); @define('CONST_Tablespace_Search_Index', 'bigTS'); @define('CONST_Tablespace_Aux_Data', 'bigTS'); @define('CONST_Tablespace_Aux_Index', 'bigTS');</code></p>
<p>where <code>bigTS</code> should be replaced by the name of your tablespace. See <code>settings/defaults.php</code> for more information on these settings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '18, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-62707" class="comments-container">
<span id="62886"></span>
<div id="comment-62886" class="comment">
<div id="post-62886-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I'm running into the same problem. Did @Ionvia solution fix the issue? Thanks.</p>
</div>
<div id="comment-62886-info" class="comment-info">
<span class="comment-age">(02 Apr '18, 13:47)</span> <span class="comment-user userinfo">vipyoung</span>
</div>
</div>
<span id="62981"></span>
<div id="comment-62981" class="comment">
<div id="post-62981-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, this solved it. Thank you.</p>
</div>
<div id="comment-62981-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 23:08)</span> <span class="comment-user userinfo">otter-in-a-suit</span>
</div>
</div>
</div>
<div id="comment-tools-62707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62707-form-container" class="comment-form-container">
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

