+++
type = "question"
title = "Database scheme for API vs Rendering in Mapnik"
description = '''I want to create a clone of both http://openstreetmap.org and http://api.openstreetmap.org for testing purposes. The goal is to have JOSM work with my local installation, where I can edit / update and quickly render it. I followed the RailsPort guide for setting up my own API server. The rails db:mi...'''
date = "2012-11-03T11:35:00Z"
lastmod = "2012-11-04T10:25:00Z"
weight = 17441
keywords = [ "api", "mapnik", "osm2pgsql", "osmosis" ]
aliases = [ "/questions/17441" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Database scheme for API vs Rendering in Mapnik](/questions/17441/database-scheme-for-api-vs-rendering-in-mapnik)

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
<span id="post-17441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17441-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a clone of both <a href="http://openstreetmap.org">http://openstreetmap.org</a> and <a href="http://api.openstreetmap.org">http://api.openstreetmap.org</a> for testing purposes. The goal is to have JOSM work with my local installation, where I can edit / update and quickly render it.</p>
<p>I followed the RailsPort guide for setting up my own API server. The rails db:migrate automatically creates the database schema and it says to import data using <strong>osmosis</strong>.</p>
<p>The guide for Mapnik says it requires data to be imported from .osm files by using <strong>osm2pgsql</strong> which uses a different schema thank osmosis.</p>
<p>My question is, when updates are made using say <a href="http://api.localosmserver/api/">http://api.localosmserver/api/</a> how do I update the data for Mapnik? Are the two schema compatible with eachother?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '12, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/fce9c9c5dc42d98e71856d166e984e96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bibstha&#39;s gravatar image" />
<p><span>bibstha</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bibstha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17441" class="comments-container">
&#10;</div>
<div id="comment-tools-17441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17441-form-container" class="comment-form-container">
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

<span id="17446"></span>

<div id="answer-container-17446" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bibstha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to use osmosis to generate replication diffs from your local api-db. Next these replication diffs can be applied to your rendering-db using osm2pgsl. For details see:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis/Replication#Server-side_Replication">https://wiki.openstreetmap.org/wiki/Osmosis/Replication#Server-side_Replication</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '12, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-17446" class="comments-container">
<span id="17452"></span>
<div id="comment-17452" class="comment">
<div id="post-17452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understood the part where data needs to be migrated from apidb &gt; osmosis &gt; changesetfile &gt; osm2pgsql &gt; PostGIS schema.</p>
<p>However I can't figure out how to generate the changesetfile from osmosis on a regular basis. For example, I am working with a small area in OSM (oberbayern.osm) from geofabrik.de. Both ApiDB and PostGIS have data from the same .osm file with first import.</p>
<p>Now, I am able to upload new data from JOSM to ApiDB. This will happen on a daily basis. How do I keep track of those changes and put them to PostGIS?</p>
</div>
<div id="comment-17452-info" class="comment-info">
<span class="comment-age">(04 Nov '12, 10:25)</span> <span class="comment-user userinfo">bibstha</span>
</div>
</div>
</div>
<div id="comment-tools-17446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17446-form-container" class="comment-form-container">
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

