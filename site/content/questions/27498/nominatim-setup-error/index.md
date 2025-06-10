+++
type = "question"
title = "Nominatim Setup Error"
description = '''I&#x27;m getting through some of the setup process but I suddenly receive an error and it quits. I&#x27;m just testing on a small data set and should have plenty of resources for it. Using projection SRS 4326 (Latlong) NOTICE: table &quot;place&quot; does not exist, skipping NOTICE: type &quot;keyvalue&quot; does not exist, skip...'''
date = "2013-10-25T20:54:00Z"
lastmod = "2013-10-28T14:07:00Z"
weight = 27498
keywords = [ "setup", "nominatim" ]
aliases = [ "/questions/27498" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim Setup Error](/questions/27498/nominatim-setup-error)

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
<span id="post-27498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm getting through some of the setup process but I suddenly receive an error and it quits. I'm just testing on a small data set and should have plenty of resources for it.</p>
<pre><code>Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=977MB, maxblocks=125056*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=977
Setting up table: planet_osm_nodes
NOTICE:  table &quot;planet_osm_nodes&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_nodes_pkey&quot; for table &quot;planet_osm_nodes&quot;
Setting up table: planet_osm_ways
NOTICE:  table &quot;planet_osm_ways&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_ways_pkey&quot; for table &quot;planet_osm_ways&quot;
Setting up table: planet_osm_rels
NOTICE:  table &quot;planet_osm_rels&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_rels_pkey&quot; for table &quot;planet_osm_rels&quot;
&#10;Reading in file: /home/spbryfczynski/Documents/geocode/Nominatim/greenland-latest.osm.pbf
Processing: Node(1169k 292.4k/s) Way(35k 4.45k/s) Relation(380 47.50/s)  parse time: 20s
&#10;Node stats: total(1169737), max(2506472169) in 4s
Way stats: total(35562), max(243229034) in 8s
Relation stats: total(384), max(3274904) in 8s
node cache: stored: 1169737(100.00%), storage efficiency: 58.49% (dense blocks: 875, sparse nodes: 551964), hit rate: 100.00%
Stopping table: planet_osm_nodes
Stopped table: planet_osm_nodes in 0s
Stopping table: planet_osm_ways
Building index on table: planet_osm_ways (fastupdate=off)
Stopping table: planet_osm_rels
Building index on table: planet_osm_rels (fastupdate=off)
Stopped table: planet_osm_rels in 0s
Stopped table: planet_osm_ways in 225s
&#10;Osm2pgsql took 245s overall
Functions
ERROR: nominatim module not built
nominatim module not built</code></pre>
<p>Any advice would be greatly appreciated. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '13, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/cedcf7f648595f10a2eff219e1b94922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbryfcz&#39;s gravatar image" />
<p><span>sbryfcz</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbryfcz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27498" class="comments-container">
&#10;</div>
<div id="comment-tools-27498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27498-form-container" class="comment-form-container">
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

<span id="27516"></span>

<div id="answer-container-27516" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27516-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sbryfcz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to build the software first.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Compiling_the_Required_Software">http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Compiling_the_Required_Software</a></p>
<pre><code> cd Nominatim
 ./autogen.sh
 ./configure
 make</code></pre>
<p>It is possible that something failed (and you should check any messages output) but I suspect you missed this step.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '13, 01:55</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27516" class="comments-container">
<span id="27577"></span>
<div id="comment-27577" class="comment">
<div id="post-27577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well I feel dumb. I could have sworn that I had built it. Thanks</p>
</div>
<div id="comment-27577-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 14:07)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
</div>
<div id="comment-tools-27516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27516-form-container" class="comment-form-container">
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

