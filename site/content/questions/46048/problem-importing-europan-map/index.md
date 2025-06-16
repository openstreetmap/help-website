+++
type = "question"
title = "Problem importing europan map"
description = '''Hi guys and thanks in advance. I have installed nominatim on my local (virtual) centOS 6.6 machine following the wiki guide there https://wiki.openstreetmap.org/wiki/Nominatim/Installation. I follow the instructions line to line and I manage to import a little map (monaco-latest.osm.pbf) and everythi...'''
date = "2015-10-22T11:37:00Z"
lastmod = "2015-10-22T11:37:00Z"
weight = 46048
keywords = [ "nominatim" ]
aliases = [ "/questions/46048" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem importing europan map](/questions/46048/problem-importing-europan-map)

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
<span id="post-46048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46048-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys and thanks in advance. I have installed nominatim on my local (virtual) centOS 6.6 machine following the wiki guide there <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation.">https://wiki.openstreetmap.org/wiki/Nominatim/Installation.</a> I follow the instructions line to line and I manage to import a little map (monaco-latest.osm.pbf) and everything goes fine. Now I tried to import the european map (15.8 gb), i follow the same procedure, I launch the command:</p>
<pre><code>nohup ./utils/setup.php --osm-file european.latest.osm.pbf --all --osm2pgsql-cache 18000 2&gt;&gt;err.log 1&gt;&gt;setup.log &amp;</code></pre>
<p>On a (virtual) machine with 500 gb disk space and 16 gb RAM. Now after 20 hours if I open the <em>setup.log</em> I can see some create table (9 exactly) and many insert; the file end with IMPORT command. If I open the <em>err.log</em> I can see something like this:</p>
<pre><code>NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse Node-cache: cache=2048MB, maxblocks=262144*8192, allocation method=11 Mid: pgsql, scale=10000000 cache=2048
Setting up table: planet_osm_nodes
NOTICE:  table &quot;planet_osm_nodes&quot; does not exist, skipping
Setting up table: planet_osm_ways
NOTICE:  table &quot;planet_osm_ways&quot; does not exist, skipping
Setting up table: planet_osm_rels
NOTICE:  table &quot;planet_osm_rels&quot; does not exist, skipping
Reading in file: /srv/mappe/europe-latest.osm.pbf
Processing: Node(10k 10.0k/s) Way(0k 0.00k/s) Relation(0 0.00/s)
Processing: Node(20k 20.0k/s) Way(0k 0.00k/s) Relation(0 0.00/s)
.....
.....</code></pre>
<p>This file ended <strong>exactly</strong> with this line and <strong>no error</strong>:</p>
<pre><code>Processing: Node(1561860k 141.1k/s) Way(6002k 0.04k/s) Relation(0 0.00/s)</code></pre>
<p>When I see this scenario the first time I kill the process, delete the database and reimport the map again. But is the THIRD TIME that the error.log ended exactly with that line, exactly at Node 1561860. The process is still present in <code>ps -aux</code> list and the postgresql data folder is still growing and if I launch the following command:</p>
<pre><code>psql -d postgres -c &quot;select * from pg_stat_activity where datname = &#39;nominatim&#39;&quot;</code></pre>
<p>I can see some log (but outdated). What damned is happening? Why the log stops exactly at that line? Why stops if there is no error? Maybe the map file is corrupted? Please help me I don't know what I have to do. Thanks Giacomo</p>
<p>Sorry for my stupidity... The process is not stucked, is working on node 1561860 and <em>way</em> growing very slowly... when I launch tail -f I didn't see that <em>Way(x,y)</em> parameter is growing.. I believed it was fixed to a specific value.</p>
<p>Sorry, I have to delete the entire post?? Just last question: the --osm2pgsql-cache value should be half of RAM memory?? How can I determine that??</p>
<p>Thanks Giacomo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '15, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e1580c3bf447dab7c4a377186b60dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giacomo-keybiz&#39;s gravatar image" />
<p><span>giacomo-keybiz</span><br />
<span class="score" title="33 reputation points">33</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giacomo-keybiz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '15, 12:06</strong> </span></p>
</div>
</div>
<div id="comments-container-46048" class="comments-container">
&#10;</div>
<div id="comment-tools-46048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46048-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

