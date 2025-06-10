+++
type = "question"
title = "Nominatim import of data import results in Segmentation fault"
description = '''I have a VPS with 6 core, 60GB RAM and 1TB SSD space. I installed Nominatim on Ubuntu 18.04 following the official installation here Nominatim Installation I tried to import the openstreet planet pbf file located here Planet OpenStreetMap using the command below: ./utils/setup.php --osm-file planet-...'''
date = "2019-12-01T11:43:00Z"
lastmod = "2019-12-01T22:23:00Z"
weight = 71917
keywords = [ "openstreetmap", "nominatim" ]
aliases = [ "/questions/71917" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim import of data import results in Segmentation fault](/questions/71917/nominatim-import-of-data-import-results-in-segmentation-fault)

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
<span id="post-71917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a VPS with 6 core, 60GB RAM and 1TB SSD space.</p>
<p>I installed Nominatim on Ubuntu 18.04 following the official installation here <a href="http://nominatim.org/release-docs/latest/admin/Installation/">Nominatim Installation</a></p>
<p>I tried to import the openstreet planet pbf file located here <a href="https://planet.openstreetmap.org/">Planet OpenStreetMap</a> using the command below:</p>
<pre><code>./utils/setup.php --osm-file planet-latest.osm.pbf --all --osm2pgsql-cache 28000 2&gt;&amp;1 | tee setup.log</code></pre>
<p>After few hours I got the error Segmentation fault ERROR: No Data see below:</p>
<pre><code>&gt; 2019-11-30 16:50:55 == Setup DB Postgres version found: 10 Postgis
&gt; version found: 2.4  set_config
&gt; ------------
&gt; 
&gt; (1 row)
&gt; 
&gt; 2019-11-30 16:51:04 == Import data osm2pgsql version 1.2.0 (64 bit id
&gt; space)
&gt; 
&gt; Allocating memory for dense node cache Processing: Node(618450k
&gt; 2425.3k/s) Way(0k 0.00k/s) Relation(0 0.00/s) Allocating memory for sparse node cache Sharing dense sparse Node-cache: cache=28000MB,
&gt; maxblocks=448000*65536, allocation method=11 Mid: loading persistent
&gt; node cache from /srv/nominatim/flatnode/flatnode.file Mid: pgsql,
&gt; cache=28000 Setting up table: planet_osm_nodes Setting up table:
&gt; planet_osm_ways Setting up table: planet_osm_rels Processing:
&gt; Node(621390k 2427.3k/s) Way(0k 0.00k/s) Relation(0
&gt; 0.00/s)import-full.style&#39;. Using projection SRS 4326 (Latlong) NOTICE:  table &quot;place&quot; does not exist, skipping
&gt; 
&gt; Reading in file:
&gt; /srv/nominatim/Nominatim-3.4.0/build/planet-latest.osm.pbf Using PBF
&gt; parser. Processing: Node(5612922k 3148.0k/s) Way(437617k 33.05k/s)
&gt; Relation(0 0.00/s)Segmentation fault ERROR: No Data string(7) &quot;No
&gt; Data&quot;</code></pre>
<p>Any idea why I got this error please? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '19, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/689d86940d87df481c9144483c5479bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="okamal&#39;s gravatar image" />
<p><span>okamal</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="okamal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71917" class="comments-container">
<span id="71920"></span>
<div id="comment-71920" class="comment">
<div id="post-71920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is the date of the planet file that you downloaded, 191118 or 191125? If you don't remember then what is the exact size (in bytes) of your planet-latest.pbf?</p>
</div>
<div id="comment-71920-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 13:35)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="71921"></span>
<div id="comment-71921" class="comment">
<div id="post-71921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I went to the Planet OpenStreetMap link above and downloaded the Latest Weekly Planet PBF File from this link <a href="https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf.">https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf.</a> It is 45GB in size.</p>
</div>
<div id="comment-71921-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 13:48)</span> <span class="comment-user userinfo">okamal</span>
</div>
</div>
<span id="71924"></span>
<div id="comment-71924" class="comment">
<div id="post-71924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The newest planet is 48GB. So either you have a planet that is at least 2 months old or your download was incomplete. An incomplete pbf would also explain the segmentation fault.</p>
</div>
<div id="comment-71924-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 15:32)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="71925"></span>
<div id="comment-71925" class="comment">
<div id="post-71925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry I meant 48G not 45GB. My terminal shows it : -rw-rw-r-- 1 nominatim nominatim 49G Nov 28 14:49 planet-latest.osm.pbf and the file is the newest one, downloaded yesterday.</p>
</div>
<div id="comment-71925-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 15:48)</span> <span class="comment-user userinfo">okamal</span>
</div>
</div>
<span id="71931"></span>
<div id="comment-71931" class="comment">
<div id="post-71931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I imported the same file with Nominatim 2.4, osm2pgsql 1.2.0 two days ago and it finished fine. "Node(5612922k 6921.0k/s) Way(622516k 96.77k/s) Relation(7236370 1012.79/s)", the node count matches your output so I think the planet file and osm2pgsql version itself is alright.</p>
</div>
<div id="comment-71931-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 22:15)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-71917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71917-form-container" class="comment-form-container">
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

<span id="71932"></span>

<div id="answer-container-71932" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71932-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Actually I changed this --osm2pgsql-cache 28000 to this --osm2pgsql-cache 18000 and it worked. It is still importing data since 12 hours now. I'll comment again if all worked fine. Thanks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '19, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/689d86940d87df481c9144483c5479bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="okamal&#39;s gravatar image" />
<p><span>okamal</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="okamal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71932" class="comments-container">
&#10;</div>
<div id="comment-tools-71932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71932-form-container" class="comment-form-container">
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

