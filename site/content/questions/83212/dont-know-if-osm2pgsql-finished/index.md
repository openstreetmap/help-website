+++
type = "question"
title = "dont know if osm2pgsql finished"
description = '''Hello  is it finished processing? its been 9 hours since last line 2022-01-23 13:15:37 osm2pgsql version 1.5.1 2022-01-23 13:15:37 Database version: 13.5 (Debian 13.5-1.pgdg110+1) 2022-01-23 13:15:37 PostGIS version: 3.2 2022-01-23 13:15:38 Setting up table &#x27;planet_osm_point&#x27; 2022-01-23 13:15:38 Set...'''
date = "2022-01-26T09:37:00Z"
lastmod = "2022-01-26T12:18:00Z"
weight = 83212
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/83212" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dont know if osm2pgsql finished](/questions/83212/dont-know-if-osm2pgsql-finished)

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
<span id="post-83212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83212-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello is it finished processing? its been 9 hours since last line</p>
<pre><code>2022-01-23 13:15:37  osm2pgsql version 1.5.1
2022-01-23 13:15:37  Database version: 13.5 (Debian 13.5-1.pgdg110+1)
2022-01-23 13:15:37  PostGIS version: 3.2
2022-01-23 13:15:38  Setting up table &#39;planet_osm_point&#39;
2022-01-23 13:15:38  Setting up table &#39;planet_osm_line&#39;
2022-01-23 13:15:38  Setting up table &#39;planet_osm_polygon&#39;
2022-01-23 13:15:38  Setting up table &#39;planet_osm_roads&#39;
Processing: Node(3891800k 2915.2k/s) Way(0k 0.00k/s) Relation(0 0.0/s)sudo apt-get install iotop
&#10;Processing: Node(3980900k 2946.6k/s) Way(0k 0.00k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(12531k 3.62k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(68887k 3.65k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(72953k 3.71k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(100938k 4.09k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(105326k 4.15k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(507298k 7.02k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(648443k 7.55k/s) Relation(0 0.0/s)
Processing: Node(7445971k 3129.9k/s) Way(830127k 8.22k/s) Relation(238020 36.3/s)
Processing: Node(7445971k 3129.9k/s) Way(830127k 8.22k/s) Relation(587060 55.0/s)
Processing: Node(7445971k 3129.9k/s) Way(830127k 8.22k/s) Relation(1640510 86.9/s)
2022-01-25 07:18:42  Reading input files done in 151384s (42h 3m 4s).
2022-01-25 07:18:42    Processed 7445971967 nodes in 2379s (39m 39s) - 3130k/s
2022-01-25 07:18:42    Processed 830127741 ways in 100934s (28h 2m 14s) - 8k/s
2022-01-25 07:18:42    Processed 9578611 relations in 48071s (13h 21m 11s) - 199/s
2022-01-25 07:18:43  Dropping table &#39;planet_osm_nodes&#39;
2022-01-25 07:18:43  Done postprocessing on table &#39;planet_osm_nodes&#39; in 0s
2022-01-25 07:18:43  Dropping table &#39;planet_osm_ways&#39;
2022-01-25 07:18:45  Done postprocessing on table &#39;planet_osm_ways&#39; in 2s
2022-01-25 07:18:45  Dropping table &#39;planet_osm_rels&#39;
2022-01-25 07:18:45  Done postprocessing on table &#39;planet_osm_rels&#39; in 0s
2022-01-25 07:18:45  Done postprocessing on table &#39;planet_osm_nodes&#39; in 0s
2022-01-25 07:18:45  Done postprocessing on table &#39;planet_osm_ways&#39; in 0s
2022-01-25 07:18:45  Done postprocessing on table &#39;planet_osm_rels&#39; in 0s
2022-01-25 07:18:45  Clustering table &#39;planet_osm_point&#39; by geometry...
2022-01-25 07:18:45  Clustering table &#39;planet_osm_roads&#39; by geometry...
2022-01-25 07:18:45  Clustering table &#39;planet_osm_polygon&#39; by geometry...
2022-01-25 07:18:45  Clustering table &#39;planet_osm_line&#39; by geometry...
2022-01-25 09:04:10  Creating geometry index on table &#39;planet_osm_point&#39;...
2022-01-25 09:29:14  Creating geometry index on table &#39;planet_osm_roads&#39;...
2022-01-25 09:59:54  Analyzing table &#39;planet_osm_roads&#39;...
2022-01-25 11:20:04  Analyzing table &#39;planet_osm_point&#39;...
2022-01-25 11:27:19  All postprocessing on table &#39;planet_osm_point&#39; done in 14914s (4h 8m 34s).
2022-01-25 21:07:07  Creating geometry index on table &#39;planet_osm_polygon&#39;...
2022-01-25 21:27:05  Analyzing table &#39;planet_osm_line&#39;...
2022-01-25 21:27:16  All postprocessing on table &#39;planet_osm_line&#39; done in 50911s (14h 8m 31s).
2022-01-26 03:17:08  Analyzing table &#39;planet_osm_polygon&#39;...
2022-01-26 03:17:47  All postprocessing on table &#39;planet_osm_polygon&#39; done in 71942s (19h 59m 2s).
2022-01-26 03:17:47  All postprocessing on table &#39;planet_osm_roads&#39; done in 10092s (2h 48m 12s).
2022-01-26 03:17:48  osm2pgsql took 223331s (62h 2m 11s) overall.</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '22, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/8524afbaa2cb261296c620ea044952de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="do-d&#39;s gravatar image" />
<p><span>do-d</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="do-d has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83212" class="comments-container">
&#10;</div>
<div id="comment-tools-83212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83212-form-container" class="comment-form-container">
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

<span id="83214"></span>

<div id="answer-container-83214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83214-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it is finished. The <strong>"osm2pgsql took X (...) overall"</strong> message is the last one. You should now see the created tables fine in your database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '22, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-83214" class="comments-container">
&#10;</div>
<div id="comment-tools-83214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83214-form-container" class="comment-form-container">
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

