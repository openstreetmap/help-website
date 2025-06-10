+++
type = "question"
title = "How can I get geometry of administrative boundaries from OSM data stored in postgreSQL/PostGIS database"
description = '''Hi, I have a PostGIS database which I filled with OSM data via osm2pgsql-Script.  Now I have the tables planet_osm_nodes, planet_osm_line and so on. The geometry-data is stored in the way-column. Everything fine. Is there a tutorial or something on how I can retrieve the geometry-data of a specific ...'''
date = "2013-04-23T11:58:00Z"
lastmod = "2017-07-01T23:19:00Z"
weight = 21758
keywords = [ "administrative", "boundary", "postgresql", "postgis" ]
aliases = [ "/questions/21758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get geometry of administrative boundaries from OSM data stored in postgreSQL/PostGIS database](/questions/21758/how-can-i-get-geometry-of-administrative-boundaries-from-osm-data-stored-in-postgresqlpostgis-database)

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
<span id="post-21758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21758-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have a PostGIS database which I filled with OSM data via osm2pgsql-Script. Now I have the tables <em>planet_osm_nodes</em>, <em>planet_osm_line</em> and so on. The geometry-data is stored in the way-column. Everything fine.</p>
<p>Is there a tutorial or something on how I can retrieve the geometry-data of a specific administrative boundary, like the national boundary of Germany or admin_level = 4 boundaries in the PostGIS database. I don't want to download them on a website, i need the data from the database, that I can do some quality analysis on this data and compare it to other geometry data.</p>
<p>When I try the following SQL-statement to get the geometry of a boundary-relation inside germany (relation id = 62611)</p>
<pre><code>SELECT osm_id, way
  FROM planet_osm_polygon
    where osm_id = -62611</code></pre>
<p>and view it in a GIS software or in C# (SharpMap), then it's not the boundary i expected. It's only some kind of rectangle and not the boundary of "Baden-Württemberg". Is that because I do something wrong or is my data incomplete?</p>
<p>Is there a proper way to get geometry data from PostGIS?</p>
<p>Thank you so far.</p>
<p>Thorsten</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '13, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c42286d4eeed3e34de09ef0cd2fca154?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="horstiborsti1337&#39;s gravatar image" />
<p><span>horstiborsti...</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="horstiborsti1337 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21758" class="comments-container">
<span id="21825"></span>
<div id="comment-21825" class="comment">
<div id="post-21825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, thanks for your answers so far. I played a bit around with the geometry column of "Baden-Württemberg" (Relation ID 62611) and as I already said, there are two "empty" geometry columns. However in fact they are not really empty. I tried the following statement:</p>
<pre><code>SELECT osm_id, way, ST_AsText(way), ST_IsValid(way), ST_IsEmpty(way)
   FROM planet_osm_polygon
      WHERE osm_id = -62611;</code></pre>
<p>The result looked like</p>
<p><img src="http://help.openstreetmap.org/upfiles/osm_missing_geometry01.png" alt="alt text" /></p>
<p>Is it possible to have a geometry column which is not empty but valid and has no WKT or WKB in the colums?</p>
<p>Thanks Thorsten</p>
</div>
<div id="comment-21825-info" class="comment-info">
<span class="comment-age">(25 Apr '13, 09:28)</span> <span class="comment-user userinfo">horstiborsti...</span>
</div>
</div>
<span id="21883"></span>
<div id="comment-21883" class="comment">
<div id="post-21883-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hey Thorsten, This site is more an FAQ site rather than a discussing forum for deeper database issues.</p>
<p>Come to the german speaking subforum at <a href="http://forum.osm.org">http://forum.osm.org</a> ...</p>
</div>
<div id="comment-21883-info" class="comment-info">
<span class="comment-age">(26 Apr '13, 13:43)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="56831"></span>
<div id="comment-56831" class="comment">
<div id="post-56831-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you managed to achieve your goal since then? if so, may you share your experience, please.</p>
</div>
<div id="comment-56831-info" class="comment-info">
<span class="comment-age">(01 Jul '17, 23:19)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
</div>
<div id="comment-tools-21758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21758-form-container" class="comment-form-container">
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

<span id="21759"></span>

<div id="answer-container-21759" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In principle what you are doing seems to be right. You should realize that in in the general case you will get multiple polygons back from your query (currently in the case of BW 4) that together represent the complete multi-polygon for the boundary.</p>
<p>You can generate a single object by for example doing:</p>
<p>select ST_Multi(ST_Collect(way)) from planet_osm_polygon where osm_id=-62611;</p>
<p>or on import request osm2pgsql to generate multi* geometries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '13, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</img>
</div>
</div>
<div id="comments-container-21759" class="comments-container">
<span id="21760"></span>
<div id="comment-21760" class="comment">
<div id="post-21760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thank you for the fast answer. I tried your statement on several geometries but the returned geometry was always NULL. Two of the four polygons for BW are NULL. When I try to suppress those emtpy polygons with</p>
<pre><code>SELECT way
   FROM planet_osm_polygon
     WHERE osm_id = -62611 AND way IS NOT NULL</code></pre>
<p>i still get all four lines.</p>
<p>Another statement was</p>
<pre><code> SELECT st_multi(st_collect(way)) 
    FROM planet_osm_roads
       WHERE admin_level = &#39;2&#39; AND &quot;name:en&quot; LIKE &#39;%Germany%&#39; 
           AND osm_id &gt; 0;</code></pre>
<p>but the return value for way column is again NULL</p>
</div>
<div id="comment-21760-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 12:39)</span> <span class="comment-user userinfo">horstiborsti...</span>
</div>
</div>
<span id="21761"></span>
<div id="comment-21761" class="comment">
<div id="post-21761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are a number of possible issues, you may have invalid geometeries (which is not the same as the column being null) or empty geometries, you can for example test for valid geometries with ST_IsValid. Maybe something did go wrong with your import, I'm not aware of osm2pgsql generating NULL values for geometries.</p>
</div>
<div id="comment-21761-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 12:48)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21759-form-container" class="comment-form-container">
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

