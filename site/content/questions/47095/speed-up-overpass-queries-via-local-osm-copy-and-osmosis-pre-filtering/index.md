+++
type = "question"
title = "Speed up Overpass Queries via Local OSM Copy and Osmosis pre-filtering?"
description = '''I am using Overpass API (on overpass-api.de) to query for transport-related elements along a recorded GPS track/journey. Currently, I perform several &quot;around&quot;-queries for each track point of the journey to get the IDs of e.g. public transport routes and stops, roads, railway etc. within 50m. This ta...'''
date = "2015-12-11T13:35:00Z"
lastmod = "2015-12-13T11:20:00Z"
weight = 47095
keywords = [ "overpass", "optimization", "osmosis" ]
aliases = [ "/questions/47095" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Speed up Overpass Queries via Local OSM Copy and Osmosis pre-filtering?](/questions/47095/speed-up-overpass-queries-via-local-osm-copy-and-osmosis-pre-filtering)

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
<span id="post-47095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47095-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Overpass API (on overpass-api.de) to query for transport-related elements along a recorded GPS track/journey. Currently, I perform several "around"-queries for each track point of the journey to get the IDs of e.g. public transport routes and stops, roads, railway etc. within 50m. This takes a few seconds for each track point, and since each journey consists of about 100 track points, collecting all data takes minutes instead of desired &lt;10s.</p>
<p>I have the following idea for optimizing this:</p>
<ul>
<li>create a local copy of planet.osm <del>and Overpass API</del> on my own server. --&gt; no sharing of server-load</li>
<li>use Osmosis to pre-filter planet.osm for only the transport-related elements I am looking for --&gt; <del>Overpass</del> only has to search a smaller database.</li>
</ul>
<p>Since I am not experienced with OSM and this requires considerable effort:</p>
<ul>
<li><strong>Are my assumptions correct and do they make sense?</strong></li>
<li><strong>Can I expect a significant speed-up from this?</strong></li>
</ul>
<p>Thanks in advance!</p>
<p>Arik</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '15, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/382c1236163ab7156d672328538ba11e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arik&#39;s gravatar image" />
<p><span>Arik</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '15, 15:38</strong> </span></p>
</div>
</div>
<div id="comments-container-47095" class="comments-container">
<span id="47098"></span>
<div id="comment-47098" class="comment">
<div id="post-47098-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Is there any reason you particularly want to use Overpass locally? Simple PostGIS queries should be able to do this if you load OSM data into a spatial database using the standard tools.</p>
</div>
<div id="comment-47098-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 15:00)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="47099"></span>
<div id="comment-47099" class="comment">
<div id="post-47099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your comment! I was actually not aware of the fact that there is a different way to access the data. So, let's forget about Overpass in my question... I'll read about PostGIS to query a local database. Now, does the assumption with the prefiltering make sense?</p>
</div>
<div id="comment-47099-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 15:11)</span> <span class="comment-user userinfo">Arik</span>
</div>
</div>
<span id="47100"></span>
<div id="comment-47100" class="comment not_top_scorer">
<div id="post-47100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11756/arik">@Arik</a> Would it be possible to describe the sort of queries that you might want to do? Not in query language - just at the level of "I want to find houses near a road called X" or similar.</p>
</div>
<div id="comment-47100-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 15:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47101"></span>
<div id="comment-47101" class="comment">
<div id="post-47101-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure, for example: I want to know whether there is at least one road within 50m around given coordinates. Then replace "road" with several other elements like "bus stop", "train station", "subway route" and query again. For routes, the ID of the relation would be useful as well.</p>
<p>P.S.: more generally, my goal is to find out what means of transport could have been used while recording the GPS track</p>
</div>
<div id="comment-47101-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 15:34)</span> <span class="comment-user userinfo">Arik</span>
</div>
</div>
<span id="47106"></span>
<div id="comment-47106" class="comment not_top_scorer">
<div id="post-47106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you please post your original Overpass Query as overpass turbo link, so we can check if the issue persists with the latest beta version. Thanks.</p>
</div>
<div id="comment-47106-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 17:20)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47108"></span>
<div id="comment-47108" class="comment not_top_scorer">
<div id="post-47108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is not an issue with Overpass, I guess. Querying a lot of elements just takes its time. Instead, I will use PostGIS as suggested by Richard, I guess. The only remaining question is whether it makes sense to create a reduced dataset first which only includes all transport-related elements. I would strongly guess that the answer is yes and would be happy for a confirmation by an experienced user before I waste my time setting everything up.</p>
</div>
<div id="comment-47108-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 17:47)</span> <span class="comment-user userinfo">Arik</span>
</div>
</div>
<span id="47109"></span>
<div id="comment-47109" class="comment">
<div id="post-47109-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You mentioned a response time of several seconds. In the current beta, I would expect sub-second response time. I'm just asking to confirm that it's no longer an issue.</p>
<p>How much the savings of a reduced data set are in reality is hard to tell without running some tests. Biggest issue being: setting up a full planet db for comparison - that may easily take a few days. In any case I recommend to start out with some small extract (from download.geofabrik.de) and get familiar with the toolchain.</p>
</div>
<div id="comment-47109-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 17:50)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47110"></span>
<div id="comment-47110" class="comment not_top_scorer">
<div id="post-47110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, sure, so below you find the link to an example. I use the regex because I experienced it to be significantly faster than using the union of the queries of all the key-value pairs. And you're right, it takes about one second. I recently also tried to get all the nodes belonging to the elements (see the part that is commented out), which takes longer.</p>
<p><a href="http://overpass-turbo.eu/s/ddY">http://overpass-turbo.eu/s/ddY</a></p>
</div>
<div id="comment-47110-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 18:10)</span> <span class="comment-user userinfo">Arik</span>
</div>
</div>
<span id="47111"></span>
<div id="comment-47111" class="comment">
<div id="post-47111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>ok, thanks! On the dev instance I get 880ms response time for the official 0.7.52 version and about 550ms on the beta (running with <code>osm3s_query</code>, data in buffer cache). Response times on overpass-api.de are higher due to overall higher CPU utilization there. overpass-api.de only accepts one query at a time, but rambler.ru instance doesn't have that limit. If you set up your own instance, you can of course run as many queries in parallel as you wish (or your hardware can handle).</p>
</div>
<div id="comment-47111-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 18:28)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-47095" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-47095-form-container" class="comment-form-container">
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

<span id="47118"></span>

<div id="answer-container-47118" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47118-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A smaller database for Overpass API would indeed help to speed things up a bit:</p>
<p>Here's a small comparison I ran for your sample query <a href="http://overpass-turbo.eu/s/ddY">http://overpass-turbo.eu/s/ddY</a></p>
<ul>
<li>Full planet on v0.7.52 (official) - 880ms</li>
<li>Full Planet on <a href="https://github.com/mmd-osm/Overpass-API/wiki/Overpass-API-test754">v0.7.54_mmd (beta)</a> - 550ms</li>
</ul>
<p>Now comparing that with a smaller Berlin extract provided by Geofabrik and various database compression settings (lz4, gzip or no compression):</p>
<ul>
<li><a href="http://download.geofabrik.de/europe/germany/berlin.html">Berlin-only extract</a> on <a href="https://github.com/mmd-osm/Overpass-API/wiki/Overpass-API-test754">v0.7.54_mmd (beta)</a>, lz4 - 140ms (default for this branch)</li>
<li><a href="http://download.geofabrik.de/europe/germany/berlin.html">Berlin-only extract</a> on <a href="https://github.com/mmd-osm/Overpass-API/wiki/Overpass-API-test754">v0.7.54_mmd (beta)</a>, gzip - 250ms (also default in v0.7.52)</li>
<li><a href="http://download.geofabrik.de/europe/germany/berlin.html">Berlin-only extract</a> on <a href="https://github.com/mmd-osm/Overpass-API/wiki/Overpass-API-test754">v0.7.54_mmd (beta)</a>, no compression - 100ms (also default in v0.7.51)</li>
</ul>
<p>Database was populated using:</p>
<pre><code>osmconvert berlin-latest.osm.pbf --out-osm | ./update_database --db-dir=~/berlin --meta</code></pre>
<p>or with one of the following compression settings:</p>
<pre><code>    osmconvert berlin-latest.osm.pbf --out-osm | ./update_database --db-dir=~/berlin --meta --compression_method=gz
&#10;    osmconvert berlin-latest.osm.pbf --out-osm | ./update_database --db-dir=~/berlin --meta --compression_method=no</code></pre>
<p>Query was run using:</p>
<pre><code>./osm3s_query --db-dir=~/berlin &lt; query</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '15, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Dec '15, 13:12</strong> </span></p>
</div>
</div>
<div id="comments-container-47118" class="comments-container">
<span id="47127"></span>
<div id="comment-47127" class="comment">
<div id="post-47127-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the effort! It's great news that reducing the database to a certain region helps.</p>
<p>In my case, I want to reduce the database by only including the elements in my query (transport-related elements). I guess, this is possible with Osmosis and will speed it up as well. I'll test it with the Berlin-extract first, thanks for the idea :)</p>
</div>
<div id="comment-47127-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 11:20)</span> <span class="comment-user userinfo">Arik</span>
</div>
</div>
</div>
<div id="comment-tools-47118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47118-form-container" class="comment-form-container">
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

