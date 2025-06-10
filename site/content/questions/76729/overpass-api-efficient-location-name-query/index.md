+++
type = "question"
title = "Overpass API: Efficient location name query"
description = '''Hi, I&#x27;m looking for the most performant Overpass QL query to search for:  a part of a location name inside a given country with one of the tags &quot;place&quot;, &quot;natural&quot;  I tried (Country &quot;de&quot;, location &quot;Zugspitze&quot;): [out:json][timeout:30]; area[&quot;ISO3166-1&quot;=&quot;DE&quot;][admin_level=2]; node[&quot;name&quot;~&quot;Zugspitze&quot;]; o...'''
date = "2020-09-20T19:15:00Z"
lastmod = "2020-09-23T19:37:00Z"
weight = 76729
keywords = [ "overpass", "overpass-turbo", "location", "overpass-ql", "query" ]
aliases = [ "/questions/76729" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Efficient location name query](/questions/76729/overpass-api-efficient-location-name-query)

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
<span id="post-76729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76729-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm looking for the most performant Overpass QL query to search for:</p>
<ul>
<li>a part of a location name</li>
<li>inside a given country</li>
<li>with one of the tags "place", "natural"</li>
</ul>
<p>I tried (Country "de", location "Zugspitze"):</p>
<pre><code>[out:json][timeout:30];
area[&quot;ISO3166-1&quot;=&quot;DE&quot;][admin_level=2];
node[&quot;name&quot;~&quot;Zugspitze&quot;];
out;</code></pre>
<p>I noticed:</p>
<ul>
<li>part name queries like the one above or regular expression name queries are very slow</li>
<li>actually the fastest one is just to search for node["name"="Zugspitze"] without the area restriction</li>
<li>any restriction makes the query slower</li>
</ul>
<p>E.g. I tried to limit the results like this (to places and naturals):</p>
<pre><code>[out:json][timeout:30];
area[&quot;ISO3166-1&quot;=&quot;DE&quot;][admin_level=2];
node[&quot;name&quot;~&quot;Zugspitze&quot;][~&quot;(place|natural)&quot;~&quot;.&quot;];
out;</code></pre>
<p>My very simple use case: I want to give the user the possibility to search for a location and limit the results to certain place/natural types (like cities or mountains). It's a simple location search like we see on many mapping portals - and all of them are way faster than the above. How is this done with Overpass? Or is there a completely different way I'm missing?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '20, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/b3c6b0ce539881c7f94758a2f63c5541?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lukey78&#39;s gravatar image" />
<p><span>Lukey78</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lukey78 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76729" class="comments-container">
&#10;</div>
<div id="comment-tools-76729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76729-form-container" class="comment-form-container">
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

<span id="76733"></span>

<div id="answer-container-76733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76733-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass is a very generic query engine and it emphasizes flexibility over performance. Since everyone is using the same Overpass instance and people have vastly different requirements, optimizing towards one use case would often make a different use case slower.</p>
<p>You will get the best performance by importing OSM data into a PostGIS database and preprocessing/ indexing it according to your special use case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '20, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76733" class="comments-container">
<span id="76771"></span>
<div id="comment-76771" class="comment">
<div id="post-76771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, that makes sense. Thank you.</p>
<p>I created a location database with some additional tag info from a database I use for my map server (created with osm2pgsql) like this:</p>
<pre><code>CREATE TABLE location (&quot;osm_id&quot; BIGINT PRIMARY KEY, &quot;name&quot; TEXT, &quot;ele&quot; TEXT, &quot;lat&quot; FLOAT, &quot;lon&quot; FLOAT, &quot;way&quot; geometry(Point,3857), country_code VARCHAR(3), &quot;place&quot; TEXT, &quot;natural&quot; TEXT, &quot;tourism&quot; TEXT);
&#10;INSERT INTO location SELECT osm_id,name,ele,ST_Y(ST_Transform(way, 4326)) AS lat,ST_X(ST_Transform(way, 4326)) AS lon, way, null, &quot;place&quot;, &quot;natural&quot;, &quot;tourism&quot; FROM planet_osm_point WHERE name IS NOT NULL and (&quot;place&quot; OS NOT NULL or &quot;natural&quot; IS NOT NULL or &quot;tourism&quot; IS NOT NULL);
&#10;CREATE INDEX location_name_idx ON location (lower(name));</code></pre>
<p>Now I just need to find a way to insert the country_code.</p>
<p>I could use the Nominatim API of Overpass to query the ISO3166-1 code for all coordinates with an is_in query based on areas of admin_level=2.</p>
<p>Or is there a better way to do that on the SQL/Postgis level?</p>
</div>
<div id="comment-76771-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 20:26)</span> <span class="comment-user userinfo">Lukey78</span>
</div>
</div>
<span id="76775"></span>
<div id="comment-76775" class="comment">
<div id="post-76775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A standard osm2pgsql load without <code>--hstore</code> will not give you a country code column on the country boundaries. You'd either have to add that to the config, or use <code>--hstore</code> on import. Then, something like</p>
<pre><code>UPDATE location 
SET country_code = tags-&gt;&#39;ISO3166-1&#39; 
FROM planet_osm_polygon 
WHERE st_contains(planet_osm_polygon.way, location.way)
AND admin_level=&#39;2&#39; 
AND boundary=&#39;administrative&#39;;</code></pre>
<p>should add country codes to your <code>location</code> table.</p>
<p>There's a little thing I neglected to say in my initial reply; some POIs that you might be interested in could be mapped as an area, not as a point. You might want to repeat your <code>INSERT INTO...</code> query with <code>planet_osm_polygon</code> as the source, this time using <code>st_centroid(way)</code> instead of just <code>way</code> - this will then reduce the polygons to points and add them into your location table.</p>
</div>
<div id="comment-76775-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 22:16)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="76793"></span>
<div id="comment-76793" class="comment">
<div id="post-76793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is very helpful, thank you for the fast and comprehensive answer!</p>
</div>
<div id="comment-76793-info" class="comment-info">
<span class="comment-age">(23 Sep '20, 19:37)</span> <span class="comment-user userinfo">Lukey78</span>
</div>
</div>
</div>
<div id="comment-tools-76733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76733-form-container" class="comment-form-container">
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

