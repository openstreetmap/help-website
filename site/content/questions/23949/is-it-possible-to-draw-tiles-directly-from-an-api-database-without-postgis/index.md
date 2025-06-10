+++
type = "question"
title = "[closed] Is it possible to draw tiles directly from an API database (without PostGIS)?"
description = '''After having installed PostgreSQL, and successfully imported the full planet to an local API DB, and having successfully setup the replication process to keep it updated using the hourly diffs, I would like to start drawing my own tiles from this database. I made a short experiment before and had to...'''
date = "2013-07-04T01:43:00Z"
lastmod = "2013-07-04T07:49:00Z"
weight = 23949
keywords = [ "tiles", "apidb", "postgresql", "mapnik", "postgis" ]
aliases = [ "/questions/23949" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Is it possible to draw tiles directly from an API database (without PostGIS)?](/questions/23949/is-it-possible-to-draw-tiles-directly-from-an-api-database-without-postgis)

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
<span id="post-23949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23949-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After having installed PostgreSQL, and successfully imported the full planet to an local API DB, and having successfully setup the replication process to keep it updated using the hourly diffs, I would like to start drawing my own tiles from this database.</p>
<p>I made a short experiment before and had to export and import the API DB to a PostGIS database, and was able to draw tiles from this PostGIS database (after encountering a LOT of trouble setting up Mapnik on Windows...). However, in this experiment, I used just a very small extract from the main database, and not the full planet.</p>
<p>Knowing that it would take a very long time (and a lot of memory and CPU resources) to export the full planet to a PostGIS database (my API DB has 1.5 TB as of today after a VACUUM ANALYZE... and growing!), I would like to know if it is possible to somehow draw tiles directly from the local API DB without the intermediate PostGIS database.</p>
<p>Surely, the performance would be quite lower than the "standard" way of doing things, but it would save me a lot of time and resources.</p>
<p>Thanks in advance!</p>
<p>P.S.: Working with a subset or extract of the full planet does NOT interest me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '13, 01:43</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>19 Sep '13, 21:52</strong> </span></p>
</div>
</div>
<div id="comments-container-23949" class="comments-container">
&#10;</div>
<div id="comment-tools-23949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23949-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by MCPicoli 19 Sep '13, 21:52

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23954"></span>

<div id="answer-container-23954" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23954-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think anyone has done this before and it would be terribly, terribly slow (to the point of being totally unusable). But if you are hell-bent on trying, you could probably write a set of function-based views that emulate the geometry tables produced by osm2pgsql, and therefore enable rendering from an APIDB schema database.</p>
<p>Another possible option is using Mapnik's OSM backend instead of the PostGIS backend - i.e. to render a map for a specific area, run an Osmosis task that extracts that area from your database and then use Mapnik's OSM backend to read that data. Since the data structure is different from a standard osm2pgsql database in this case, you will have to use a different map style than the standard Mapnik style.</p>
<p>All these options are however quite painful in one way or another, and if you want proper rendering without waiting forever, you will need database tables with pre-made geometries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '13, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23954" class="comments-container">
&#10;</div>
<div id="comment-tools-23954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23954-form-container" class="comment-form-container">
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

