+++
type = "question"
title = "Use Osmosis PostGIS schema with QGIS"
description = '''If you try to use the simple PostGIS schema for Osmosis with QGIS, it complains about not having the right kind of index column in the schema. Is there a different schema for Osmosis that will work, or some hacking that you can do to make it work?'''
date = "2010-06-28T14:35:00Z"
lastmod = "2010-07-14T13:47:00Z"
weight = 2
keywords = [ "qgis", "osmosis", "postgis" ]
aliases = [ "/questions/2" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Use Osmosis PostGIS schema with QGIS](/questions/2/use-osmosis-postgis-schema-with-qgis)

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
<span id="post-2-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-2-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If you try to use the simple PostGIS schema for Osmosis with QGIS, it complains about not having the right kind of index column in the schema. Is there a different schema for Osmosis that will work, or some hacking that you can do to make it work?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '10, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-2" class="comments-container">
&#10;</div>
<div id="comment-tools-2" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="3"></span>

<div id="answer-container-3" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonathan Bennett has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From the hacking side of things, you can add a serial column.</p>
<pre><code>alter table planet_osm_line add column &quot;gid&quot; serial;
alter table planet_osm_point add column &quot;gid&quot; serial;
alter table planet_osm_polygon add column &quot;gid&quot; serial;</code></pre>
<p>There is the same problem with osm2pgsql database schema, where this hack needs to be repeated after every fresh import since the table is dropped. I don't know if it's the same with osmosis PostGIS schema</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '10, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-3" class="comments-container">
&#10;</div>
<div id="comment-tools-3" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="177"></span>

<div id="answer-container-177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-177-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>QGIS and other programs need a column with a unique 32 bit integer ("int" or "int4" in PostgreSQL) for every table they access. The Osmosis simple database schema uses larger integers ("bigint" or "int8" in PostgreSQL), so QGIS can't use them.</p>
<p>There are two ways to fix this: Either change the id columns from int8 to int4 in the simple database schema before importing or add an additional column to each table like this:</p>
<pre><code>ALTER TABLE nodes ADD COLUMN gid SERIAL;</code></pre>
<p>You might have to do this after every re-import of data if the table was dropped in between. Also you probably want to add an index to this column:</p>
<pre><code>CREATE UNIQUE INDEX nodes_gid_idx ON nodes (gid);</code></pre>
<p>Note that currently there are less than 2 billion nodes in the OSM database. This will change at some point. Then an int4 can't hold the id any more and we have to think about new solutions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-177" class="comments-container">
&#10;</div>
<div id="comment-tools-177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-177-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33"></span>

<div id="answer-container-33" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A similar problem occurs with GeoDjango.</p>
<p>The affected tables in the Osmosis simple schema are all tables without id:</p>
<ul>
<li>node_tags</li>
<li>relation_members</li>
<li>relation_tags</li>
<li>way_nodes</li>
<li>way_tags</li>
</ul>
<p>Adding a serial column as Andy Allan proposed helps, for example</p>
<p><code>alter table node_tags add column "gid" serial;</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '10, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5c9aa062fed08c7962c88bd21cc62f93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emka&#39;s gravatar image" />
<p><span>emka</span><br />
<span class="score" title="95 reputation points">95</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emka has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33" class="comments-container">
&#10;</div>
<div id="comment-tools-33" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33-form-container" class="comment-form-container">
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

