+++
type = "question"
title = "How to find the neighbouring nodes of a node in postgresql and construct a graph?"
description = '''Here are the things I have done till now  I created a DB in PostgreSQL with PostGIS and HSTORE extension enabled. I used the osm2pgsql command-line tool to load the DB on to the PostgreSQL localhost server. In the command line I used --hstore flag and default.style file which came along with osm2pgs...'''
date = "2020-04-08T11:20:00Z"
lastmod = "2020-04-09T11:07:00Z"
weight = 74055
keywords = [ "qgis", "osm", "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/74055" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find the neighbouring nodes of a node in postgresql and construct a graph?](/questions/74055/how-to-find-the-neighbouring-nodes-of-a-node-in-postgresql-and-construct-a-graph)

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
<span id="post-74055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74055-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here are the things I have done till now</p>
<ol>
<li>I created a DB in PostgreSQL with PostGIS and HSTORE extension enabled.</li>
<li>I used the osm2pgsql command-line tool to load the DB on to the PostgreSQL localhost server.</li>
<li>In the command line I used --hstore flag and default.style file which came along with osm2pgsql package.</li>
</ol>
<p>So, I have a DB with 5 tables i.e. planet_osm_point, planet_osm_line, planet_osm_polygon, planet_osm_roads, and spatial_ref_sys.</p>
<p>I have identified the node of interest via following SQL queries. For 1st node, SELECT * FROM planet_osm_point WHERE name = 'bits pilani' and for second SELECT * FORM ppanet_osm_polygon WHERE tags::text like = '%Shamshabad Airport%'</p>
<p>The final aim of the project is to output the best possible route between these two nodes using an algorithm on a graph of nodes.</p>
<p>I want to know how to find the neighbouring nodes(4 or 5) of a node such that they are all connected via some highway, roads, street etc. How to query the DB for this? Please help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '20, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d43c95f3a08c8cb541561e6ba400ba3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ayush%20Porwal&#39;s gravatar image" />
<p><span>Ayush Porwal</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ayush Porwal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74055" class="comments-container">
&#10;</div>
<div id="comment-tools-74055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74055-form-container" class="comment-form-container">
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

<span id="74058"></span>

<div id="answer-container-74058" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74058-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ayush Porwal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql is designed for importing data for rendering, not for routing. It's a "lossy" import that doesn't preserve the topology required for routing. (Strictly speaking you could do this if you've imported in slim mode, but it's not the intention.)</p>
<p>For routing, you need to use an importer/pre-processor that will create a routable graph from the OSM data. Routing engines such as OSRM and Graphhopper will do this as part of their preparation process. If you want to write your own routing engine, but are looking for something that will create a graph for you, <a href="https://github.com/Tristramg/osm4routing2">https://github.com/Tristramg/osm4routing2</a> is probably the easiest tool to use.</p>
<p>(If you're determined to do it in Postgres, check out <a href="https://pgrouting.org/docs/tools/osm2pgrouting.html">https://pgrouting.org/docs/tools/osm2pgrouting.html</a> .)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '20, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '20, 12:27</strong> </span></p>
</div>
</div>
<div id="comments-container-74058" class="comments-container">
<span id="74061"></span>
<div id="comment-74061" class="comment">
<div id="post-74061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Richard</p>
<p>It looks like osm4routing tool will work for me. Can you please let me know how to convert .osm file to .pbf file and what is the command line to use in osm4routing to finally get the .csv file?</p>
<p>Edit: used osmconvert to convert .osm file to .pbf file via command osmconvert map.osm --out-pbf -o=map_01.pbf. I still need help with using osm4routing tool.</p>
</div>
<div id="comment-74061-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 15:34)</span> <span class="comment-user userinfo">Ayush Porwal</span>
</div>
</div>
<span id="74063"></span>
<div id="comment-74063" class="comment">
<div id="post-74063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>osm4routing path_to_your.osm.pbf</code></p>
<p>This will then output edges.csv and nodes.csv in the same directory. The .csv files have a header row, see the osm4routing2 source code if you want to know more.</p>
</div>
<div id="comment-74063-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 16:20)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="74072"></span>
<div id="comment-74072" class="comment">
<div id="post-74072-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ayush, this site is "help with OpenStreetMap" not "do people's homework for them". I'm guessing you've been given this assignment so that you understand how a path-finding algorithm works. If I were to tell you how to do it, you'd not learn anything. Just google A* algorithm, there are countless sites that explain it.</p>
</div>
<div id="comment-74072-info" class="comment-info">
<span class="comment-age">(09 Apr '20, 11:07)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74058-form-container" class="comment-form-container">
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

