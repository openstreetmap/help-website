+++
type = "question"
title = "Configure iD and openstreetmap-website to use local postgresql DB imported with osm2pgsql"
description = '''I would like to create my own local openstreetmap-website with iD editor and edit local postgres database which was imported with osm2pgsql. Here is the list of tables osm2pgsql made: gis=# &#92;dt  List of relations  Schema | Name | Type | Owner  --------+--------------------+-------+-------  public | ...'''
date = "2014-08-11T11:49:00Z"
lastmod = "2014-08-11T13:41:00Z"
weight = 35702
keywords = [ "local", "scheme", "postgresql", "osm2pgsql", "apidb" ]
aliases = [ "/questions/35702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Configure iD and openstreetmap-website to use local postgresql DB imported with osm2pgsql](/questions/35702/configure-id-and-openstreetmap-website-to-use-local-postgresql-db-imported-with-osm2pgsql)

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
<span id="post-35702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35702-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to create my own local openstreetmap-website with iD editor and edit local postgres database which was imported with osm2pgsql.</p>
<p>Here is the list of tables osm2pgsql made:</p>
<pre><code>gis=# \dt
              List of relations
 Schema |        Name        | Type  | Owner 
--------+--------------------+-------+-------
 public | planet_osm_line    | table | osm
 public | planet_osm_nodes   | table | osm
 public | planet_osm_point   | table | osm
 public | planet_osm_polygon | table | osm
 public | planet_osm_rels    | table | osm
 public | planet_osm_roads   | table | osm
 public | planet_osm_ways    | table | osm
 public | spatial_ref_sys    | table | osm</code></pre>
<p>openstreetmap-website DB scheme is quite different:</p>
<pre><code>current_relation_members
current_relation_tags
current_relations
current_way_nodes
current_way_tags
current_ways</code></pre>
<p>How should I correspond the osm2pgsql and openstreetmap-website DB schemes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-scheme" rel="tag" title="see questions tagged &#39;scheme&#39;">scheme</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '14, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/6567ad08ab94c655e25f2ae6a47a6d7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kayrus&#39;s gravatar image" />
<p><span>kayrus</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kayrus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '14, 12:58</strong> </span></p>
</div>
</div>
<div id="comments-container-35702" class="comments-container">
&#10;</div>
<div id="comment-tools-35702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35702-form-container" class="comment-form-container">
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

<span id="35705"></span>

<div id="answer-container-35705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35705-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not possible to run rendering and an OSM API from the same database. The OSM API needs an "APIDB" database that you create with Osmosis; it has history information and a full set of tags for every object, but no pre-computed geometries. Rendering, or other use cases that depend on osm2pgsql-imported data, depend on pre-computed geometries but do not need all tags and no history.</p>
<p>To update your rendering database, you will have to make a change dump from your APIDB database and import that into your rendering database with osm2pgsql (<code>--append</code> mode).</p>
<p>If this takes too long then you have to either run it on different machines or find other ways to improve your toolchain.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '14, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-35705" class="comments-container">
&#10;</div>
<div id="comment-tools-35705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35705-form-container" class="comment-form-container">
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

