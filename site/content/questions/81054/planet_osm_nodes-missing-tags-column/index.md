+++
type = "question"
title = "planet_osm_nodes missing &quot;tags&quot; column"
description = '''I&#x27;m trying to recreate a dataset produced by the SciGRID energy mapping project detailed here https://www.power.scigrid.de/. I used osm2pgsql to export German transmission line data to a postgreSQL database and I&#x27;m trying to run a Python script written by the SciGRID people that abstracts this data ...'''
date = "2021-07-21T23:19:00Z"
lastmod = "2021-07-23T00:26:00Z"
weight = 81054
keywords = [ "column", "flex", "nodes", "osm2pgsql", "tags" ]
aliases = [ "/questions/81054" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [planet_osm_nodes missing "tags" column](/questions/81054/planet_osm_nodes-missing-tags-column)

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
<span id="post-81054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81054-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to recreate a dataset produced by the SciGRID energy mapping project detailed here <a href="https://www.power.scigrid.de/.">https://www.power.scigrid.de/.</a> I used osm2pgsql to export German transmission line data to a postgreSQL database and I'm trying to run a Python script written by the SciGRID people that abstracts this data so that it can be turned into a .csv. Osm2pgsql creates a few tables with the prefix "planet_osm_".</p>
<p>The script requires the "planet_osm_nodes" table to have a "tags" column but it does not. I'm told this table used to have such a column but isn't meant for front end use so doesn't have it from osm2pgsql version 0.88 onwards. I cannot use "planet_osm_point" instead because it lacks all the "planet_osm_nodes" columns that I need (ie. "id", "lat", "lon"). Is there a way to bring the "tags" column back (perhaps with the style file or flex output?). Otherwise, are there any pre-built binaries of older versions of osm2pgsql, pre-0.88? I have no experience building from source.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-flex" rel="tag" title="see questions tagged &#39;flex&#39;">flex</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '21, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/5d841264facb40ff2d18a6317ddac0c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kev_7&#39;s gravatar image" />
<p><span>kev_7</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kev_7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81054" class="comments-container">
&#10;</div>
<div id="comment-tools-81054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81054-form-container" class="comment-form-container">
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

<span id="81055"></span>

<div id="answer-container-81055" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81055-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kev_7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your approach is deeply flawed, not your fault, likely the programmers of whatever software you are using did not know what they were doing. <code>planet_osm_point</code> has <code>osm_id</code> which is what <code>id</code> is in <code>planet_osm_nodes</code>, and lat and lon are contained in the <code>way</code> column. If you have used the <code>-l</code> flag (ell) on import, you can extract IDs and lat and lon like this:</p>
<pre><code>SELECT
   osm_id as id,
   st_x(way) as lon,
   st_y(way) as lat
FROM
   planet_osm_point;</code></pre>
<p>The <code>planet_osm_point</code> table will not contain all nodes, just those selected based on the style file you specify (or the default <code>osm2pgsql.style</code> if you do not specify any).</p>
<p>If you want to export all nodes, then the process involving osm2pgsql is unnecessary; you can use the command-line tool <code>osmium</code> to convert an .osm.pbf file to a text-based representation called the "opl" format, and that can be converted to CSV with a few trivial transformations.</p>
<p>Do not try to revive decades-old osm2pgsql versions, it's not worth the hassle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '21, 01:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '21, 08:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span></p>
</div>
</div>
<div id="comments-container-81055" class="comments-container">
<span id="81058"></span>
<div id="comment-81058" class="comment">
<div id="post-81058-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you! And is there a way to reveal the tags column for planet_osm_point? Currently this table only has "osm_id", "power", "cables", "voltage", "wires" and "way".</p>
</div>
<div id="comment-81058-info" class="comment-info">
<span class="comment-age">(22 Jul '21, 18:06)</span> <span class="comment-user userinfo">kev_7</span>
</div>
</div>
<span id="81059"></span>
<div id="comment-81059" class="comment">
<div id="post-81059-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes and no. If you <code>create extension hstore</code> in your postgres database and then use the <code>--hstore</code> flag on osm2pgsql, you will get a tags column. But it will be different from the tags column that used to be in planet_osm_nodes; the latter was a string array with 2 entries for every tag - first the key, then the value, then the next key, etc., whereas the the tags column in planet_osm_point will be "hstore" type column that represents a proper key-value map.</p>
</div>
<div id="comment-81059-info" class="comment-info">
<span class="comment-age">(23 Jul '21, 00:26)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81055-form-container" class="comment-form-container">
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

