+++
type = "question"
title = "Error: DB error: insufficient permissions"
description = '''Hi Last week managed to set up Nominatim successfully following the instructions provided by OSM. However there was one problem where the gb_postcode database was not created. I think it was because it was using deprecated functions so I have replaced them with the newer alternatives. I have my post...'''
date = "2013-01-28T01:19:00Z"
lastmod = "2013-01-28T16:43:00Z"
weight = 19383
keywords = [ "osm", "nominatim", "postgresql", "postgis" ]
aliases = [ "/questions/19383" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error: DB error: insufficient permissions](/questions/19383/error-db-error-insufficient-permissions)

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
<span id="post-19383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19383-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Last week managed to set up Nominatim successfully following the instructions provided by OSM. However there was one problem where the gb_postcode database was not created. I think it was because it was using deprecated functions so I have replaced them with the newer alternatives.</p>
<p>I have my postgres user set up as the same user of the computer just as the instructions mention.</p>
<p>I run the following command: ./Nominatim-2.0.0/utils/setup.php --osm-file osmfile.osm.pbf --all</p>
<p>But I get a permissions error as follows:</p>
<pre><code>Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in block sized chunks
Node-cache: cache=1169MB, maxblocks=0*149633, allocation method=8192
Mid: pgsql, scale=10000000 cache=1169
Setting up table: planet_osm_nodes
NOTICE:  table &quot;planet_osm_nodes&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_nodes_pkey&quot; for table &quot;planet_osm_nodes&quot;
Setting up table: planet_osm_ways
NOTICE:  table &quot;planet_osm_ways&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_ways_pkey&quot; for table &quot;planet_osm_ways&quot;
Setting up table: planet_osm_rels
NOTICE:  table &quot;planet_osm_rels&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_rels_pkey&quot; for table &quot;planet_osm_rels&quot;
&#10;Reading in file: /home/sam/src/nominatim/Edinburgh.osm.pbf
Processing: Node(460k 153.3k/s) Way(66k 11.02k/s) Relation(820 820.00/s)  parse time: 9s
&#10;Node stats: total(460001), max(1955784257) in 3s
Way stats: total(66118), max(184992843) in 6s
Relation stats: total(827), max(2454531) in 0s
node cache: stored: 460001(100.00%), storage efficiency: 2.44% (dense blocks: 18381, sparse nodes: 0), hit rate: 0.00%
Stopping table: planet_osm_nodes
Stopping table: planet_osm_ways
Stopped table: planet_osm_nodes in 0s
Stopping table: planet_osm_rels
Building index on table: planet_osm_rels (fastupdate=off)
Building index on table: planet_osm_ways (fastupdate=off)
Stopped table: planet_osm_rels in 0s
Stopped table: planet_osm_ways in 4s
&#10;Osm2pgsql took 17s overall
osm2pgsql SVN version 0.81.0 (32bit id space)
&#10;ERROR: DB Error: insufficient permissions
DB Error: insufficient permissions</code></pre>
<p>I have ran the chmod +x command on all the directories mentioned in the instructions.</p>
<p>I don't understand why this error occurs. I managed to run the command last week but I can't think of what has changed.</p>
<p>Can anyone help?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '13, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19383" class="comments-container">
&#10;</div>
<div id="comment-tools-19383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19383-form-container" class="comment-form-container">
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

<span id="19404"></span>

<div id="answer-container-19404" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19404-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I manged to fix this. Turns out I was using the wrong username in the local.php file. Not sure how this worked before.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '13, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19404" class="comments-container">
&#10;</div>
<div id="comment-tools-19404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19404-form-container" class="comment-form-container">
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

