+++
type = "question"
title = "Using one psql database for OSM psql database and tile server database"
description = '''I am currently setting up an osm stack on my macOS computer. I have set up the rails port for the OSM website and a map tiles server from this GitHub page: GitHub page. I followed the instructions for both installations and set up separate psql databases. Is it possible for the rails port OSM psql d...'''
date = "2022-04-18T03:27:00Z"
lastmod = "2022-04-19T00:21:00Z"
weight = 84198
keywords = [ "postgresql", "tileserver", "osm", "database" ]
aliases = [ "/questions/84198" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using one psql database for OSM psql database and tile server database](/questions/84198/using-one-psql-database-for-osm-psql-database-and-tile-server-database)

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
<span id="post-84198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently setting up an osm stack on my macOS computer. I have set up the rails port for the OSM website and a map tiles server from this GitHub page: <a href="https://github.com/Overv/openstreetmap-tile-server">GitHub page</a>. I followed the instructions for both installations and set up separate psql databases. Is it possible for the rails port OSM psql database to be the same as the tile server database (in a docker container)? There are instructions on the map tiles GitHub page: "to connect to the PostgreSQL database inside the docker container." Could the OSM server directly use the tile server database or vice versa? Thanks!</p>
<p>Edit: I am importing a .pbf file for the OSM psql database, and it seems to be way larger compared to the tile server docker database. How large is a country-sized psql database supposed to be?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '22, 03:27</strong></p>
<img src="https://secure.gravatar.com/avatar/8c989912c44afac7c436471c53946a06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nightilon&#39;s gravatar image" />
<p><span>Nightilon</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nightilon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '22, 07:05</strong> </span></p>
</div>
</div>
<div id="comments-container-84198" class="comments-container">
&#10;</div>
<div id="comment-tools-84198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84198-form-container" class="comment-form-container">
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

<span id="84201"></span>

<div id="answer-container-84201" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84201-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nightilon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, this is absolutely not possible. You need to export data from your rails database using e.g. the <code>planet_dump_ng</code> utility (<a href="https://github.com/zerebubuth/planet-dump-ng)">https://github.com/zerebubuth/planet-dump-ng)</a> and then import into a new database with <code>osm2pgsql</code> in order to use it for a tile server. (Both databases could be run on the same PostgreSQL instance / in the same container if you want but the data needs to be there twice.) The reason for this is that osm2pgsql builds geometry objects and indexes on import, which the original rails database has no need for. The tile server database is on a different abstraction level, for example when you have a building with four nodes, it is not interested in the individual nodes anymore, just the building object, whereas the rails database needs to record details about every single node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '22, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84201" class="comments-container">
<span id="84202"></span>
<div id="comment-84202" class="comment">
<div id="post-84202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I think I got it working now with your explanation. Is there a process that can automate the transition from the rails psql database to the tile server psql database?</p>
</div>
<div id="comment-84202-info" class="comment-info">
<span class="comment-age">(18 Apr '22, 16:33)</span> <span class="comment-user userinfo">Nightilon</span>
</div>
</div>
<span id="84205"></span>
<div id="comment-84205" class="comment">
<div id="post-84205-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to make changes to your rails database and have these replicated to the tile server, the process for that would be using <code>osmosis</code> (see <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Replication#Server-side_Replication)">https://wiki.openstreetmap.org/wiki/Osmosis/Replication#Server-side_Replication)</a> to create minutely diffs and then processing these with <code>osm2pgsql --append</code> to modify the tile server database. If your database is very small and edits happen infrequently then it is possible that making a full dump every time a change has been made and processing that with <code>osm2pgsql --create</code> is the simpler option though.</p>
</div>
<div id="comment-84205-info" class="comment-info">
<span class="comment-age">(19 Apr '22, 00:21)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84201-form-container" class="comment-form-container">
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

