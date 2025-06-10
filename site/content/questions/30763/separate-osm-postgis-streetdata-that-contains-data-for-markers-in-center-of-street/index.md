+++
type = "question"
title = "Separate OSM postgis streetdata that contains data for markers in center of street"
description = '''I&#x27;m kinda new to Django and OSM but after hours of googling I didn&#x27;t find my answer. I have set up my own OSM tileserver which runs on a postgis database (psql). The tile server runs fine. Now I want to do the following. I want to add markers in the center of each street in a specific area. I want a...'''
date = "2014-02-16T08:26:00Z"
lastmod = "2014-06-11T23:24:00Z"
weight = 30763
keywords = [ "openstreetmap", "geocoding", "geodjango", "postgresql", "postgis" ]
aliases = [ "/questions/30763" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Separate OSM postgis streetdata that contains data for markers in center of street](/questions/30763/separate-osm-postgis-streetdata-that-contains-data-for-markers-in-center-of-street)

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
<span id="post-30763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30763-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm kinda new to Django and OSM but after hours of googling I didn't find my answer. I have set up my own OSM tileserver which runs on a postgis database (psql). The tile server runs fine. Now I want to do the following. I want to add markers in the center of each street in a specific area. I want add all these markers in the database on forehand, because the data is already there (nodes,lines,way etc.) and I want to give streets additional values. This means that i have to add all the streets to my database. In my head these tables must at least contain:</p>
<p>Name of street, City, Country, Lon, lat (of the center of the street)</p>
<p>This way I can call-up the markers and values from the database. Is this the right way of thinking, and how do I get this street data from my postgis db to this new table with the right relations and coordinates?</p>
<p>I hope someone could help me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-geodjango" rel="tag" title="see questions tagged &#39;geodjango&#39;">geodjango</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '14, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/fa5ed42b72e2ff1afe4ecb54768e2171?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lengo&#39;s gravatar image" />
<p><span>Lengo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lengo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30763" class="comments-container">
&#10;</div>
<div id="comment-tools-30763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30763-form-container" class="comment-form-container">
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

<span id="30828"></span>

<div id="answer-container-30828" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30828-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lengo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several issues that make this difficult. One is that the database you are using does not have the concept of "a street" - it just has "ways" as they were mapped in OSM. You can easily create a database of all ways and their centre point but where a street consists of five ways in OSM, your database will then have five points.</p>
<p>You'd create your basic table like this:</p>
<pre><code>SELECT name, highway, st_line_interpolate_point(way, 0.5) as geom
INTO my_new_table
FROM planet_osm_line
WHERE highway is not null;</code></pre>
<p>The <code>st_interpolate_point</code> gives you a point halfway along the street which is what I suspect you want when you say "center of the street".</p>
<p>The other non-triviality is that you would like to have city and country information which means you would have to run additional queries that use st_contains or similar functions to check which of the relevant boundary polygons from planet_osm_polygon actually contains your street, for example:</p>
<pre><code>ALTER TABLE my_new_table 
ADD COLUMN country VARCHAR(64);
UPDATE my_new_table 
SET country = (
   SELECT name from planet_osm_polygon 
   WHERE boundary=&#39;administrative&#39;
   AND admin_level=&#39;2&#39;
   AND st_contains(planet_osm_polygon.way, my_new_table.geom)
);</code></pre>
<p>Similar coding can be added for cities. These queries can run for a long time, and it is a good idea to first run them on a subset (e.g. use a WHERE clause to only run them on every 100th my_new_table object or so) to get an idea of how long they take. Adding a specialized index to planet_osm_polygon can help, e.g.</p>
<pre><code>CREATE INDEX my_country_index 
ON planet_osm_polygon 
USING gist(way) 
WHERE boundary=&#39;administrative&#39;
AND admin_level=&#39;2&#39;;</code></pre>
<p>Note that it is possible for streets to cross country or city borders but if you're just working on the centre point then the results should be clear. <em>Updating</em> this mapping (other than simply re-running the queries) could be achieved by adding some kind of dirty flag to the boundaries when they change, and re-run the matching only for those that have changed. But if you implement all that then you already have half a Nominatim installation, and it may be easier for you to look into how Nominatim solves these problems and base your solution on that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '14, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '14, 18:57</strong> </span></p>
</div>
</div>
<div id="comments-container-30828" class="comments-container">
<span id="33893"></span>
<div id="comment-33893" class="comment">
<div id="post-33893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And what to do if I just want ALL road and street name list with ANY lon/lat point on it??? Could you please advice on the query?</p>
</div>
<div id="comment-33893-info" class="comment-info">
<span class="comment-age">(11 Jun '14, 23:24)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-30828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30828-form-container" class="comment-form-container">
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

