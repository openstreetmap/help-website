+++
type = "question"
title = "osm2pgsql: Are the SQL statements documented, available?"
description = '''My osm2pgsql planet import chugged along for weeks and weeks and then the PostgreSQL backend crashed sometime after the creation of planet_osm_point_temp and planet_osm_roads_temp and during the creation of planet_osm_polygon_tmp as shown below. It seems I was ever so close to completing the process...'''
date = "2018-09-24T16:35:00Z"
lastmod = "2018-09-24T21:31:00Z"
weight = 66037
keywords = [ "osm2pgsql", "sql" ]
aliases = [ "/questions/66037" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql: Are the SQL statements documented, available?](/questions/66037/osm2pgsql-are-the-sql-statements-documented-available)

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
<span id="post-66037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66037-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My osm2pgsql planet import chugged along for weeks and weeks and then the PostgreSQL backend crashed sometime after the creation of planet_osm_point_temp and planet_osm_roads_temp and during the creation of planet_osm_polygon_tmp as shown below.</p>
<p>It seems I was ever so close to completing the process, and hoping I can pick up where it left off, but I cannot find the sql statements except that it seems they are generated in code.</p>
<p>I am wondering if there is a documented set of SQL statements that are carried out during the process. It looks like middle-pgsql.cpp and table.cpp, but I'm hoping there might exist a set of the statements. Thanks.</p>
<pre><code>STATEMENT:  CREATE TABLE planet_osm_polygon_tmp  AS
          SELECT * FROM planet_osm_polygon
            WHERE ST_IsValid(way)
            ORDER BY ST_GeoHash(ST_Transform(ST_Envelope(way),4326),10)
            COLLATE &quot;C&quot;
&#10;2018-09-23 10:42:48.391 PDT [15816] @osm FATAL:  connection to client lost</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '18, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/1524d0e025708854b20ad80271695e5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="middleforkgis&#39;s gravatar image" />
<p><span>middleforkgis</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="middleforkgis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66037" class="comments-container">
&#10;</div>
<div id="comment-tools-66037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66037-form-container" class="comment-form-container">
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

<span id="66041"></span>

<div id="answer-container-66041" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66041-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you SimonPoole,</p>
<p>Memory was all swapped out so I won't bore you with the performance issues.</p>
<p>Of course the answer to my original question - without regards to the wisdom or lack thereof - was to capture statements in the pg logfiles, after setting 'log_statement' in postgresql.conf to 'all' and running a new osm2pgsql build on a tiny data extract.</p>
<p>This gives the following (excerpt only - I won't post the whole thing but <a href="https://gist.github.com/middleforkgis/4db8e60dfda20fd3ac4a5c435beee197">here it is in a gist</a></p>
<pre><code>CREATE TABLE planet_osm_roads_tmp  AS; SELECT * FROM planet_osm_roads;  CREATE TABLE planet_osm_line_tmp  AS; SELECT * FROM planet_osm_line;  CREATE TABLE planet_osm_point_tmp  AS; SELECT
* FROM planet_osm_point;  CREATE TABLE planet_osm_polygon_tmp  AS; SELECT * FROM planet_osm_polygon;  DROP TABLE planet_osm_line;  DROP TABLE planet_osm_roads;  DROP TABLE planet_osm_polygon;  DROP TABLE planet_osm_point;  ALTER TABLE planet_osm_line_tmp RENAME TO planet_osm_line;  ALTER TABLE planet_osm_roads_tmp RENAME TO planet_osm_roads;  CREATE INDEX ON planet_osm_line USING GIST (way) WITH (FILLFACTOR=100);  CREATE INDEX ON planet_osm_roads USING GIST (way) WITH (FILLFACTOR=100);  ANALYZE planet_osm_roads;  ANALYZE planet_osm_line;  ALTER TABLE planet_osm_polygon_tmp RENAME TO planet_osm_polygon;  CREATE INDEX ON planet_osm_polygon USING GIST (way) WITH (FILLFACTOR=100);  ANALYZE planet_osm_polygon;  ALTER TABLE planet_osm_point_tmp RENAME TO planet_osm_point;  CREATE INDEX ON planet_osm_point USING GIST (way) WITH (FILLFACTOR=100);  ANALYZE planet_osm_point;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '18, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1524d0e025708854b20ad80271695e5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="middleforkgis&#39;s gravatar image" />
<p><span>middleforkgis</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="middleforkgis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66041" class="comments-container">
&#10;</div>
<div id="comment-tools-66041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66041-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66038"></span>

<div id="answer-container-66038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66038-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Given half adequate hardware a full planet import should complete in max 2 days (if you are talking about import in to the rendering schema).</p>
<p>Trying to fiddle around with SQL statements and rerunning parts of the import is likely going to take far longer than simply fixing the underlying issues (not to mention that a system that takes weeks to import will not be updatable without falling more and more behind).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '18, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66038" class="comments-container">
&#10;</div>
<div id="comment-tools-66038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66038-form-container" class="comment-form-container">
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

