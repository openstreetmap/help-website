+++
type = "question"
title = "How can I query polyline data for a road?"
description = '''I want to write a web app, which needs to know the exact path of a certain road, e.g. the german Autobahn A7. The minimum requirement for the data is a list of locations, forming a polyline, which approximates the road with an accuracy of 10 - 15 meters. Optionally extra data like junctions, exits, ...'''
date = "2012-05-25T23:23:00Z"
lastmod = "2012-05-26T01:16:00Z"
weight = 12960
keywords = [ "polyline", "road" ]
aliases = [ "/questions/12960" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I query polyline data for a road?](/questions/12960/how-can-i-query-polyline-data-for-a-road)

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
<span id="post-12960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12960-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to write a web app, which needs to know the exact path of a certain road, e.g. the german Autobahn A7.<br />
The minimum requirement for the data is a list of locations, forming a polyline, which approximates the road with an accuracy of 10 - 15 meters.</p>
<p>Optionally extra data like junctions, exits, tunnels, bridges and road km would be fine. Altitude would be great.</p>
<p>So, the questions are:</p>
<ul>
<li>Is it possible? (It really should be)</li>
<li>which data source is preferable:</li>
<li><a href="http://xapi.openstreetmap.org/api/0.6/">http://xapi.openstreetmap.org/api/0.6/</a></li>
<li><a href="http://open.mapquestapi.com/xapi/api/0.6">http://open.mapquestapi.com/xapi/api/0.6</a></li>
<li><a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a></li>
<li>others?</li>
</ul>
<p>What would the query look like?</p>
<p>Addition: it is not required that the data is queried live from the app - it would be perfectly ok that the query is done beforehand and formatted and stored in a database</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-polyline" rel="tag" title="see questions tagged &#39;polyline&#39;">polyline</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '12, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/cc305f70bb760f8993f58be1d02be55d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gisela&#39;s gravatar image" />
<p><span>Gisela</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gisela has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '12, 00:17</strong> </span></p>
</div>
</div>
<div id="comments-container-12960" class="comments-container">
&#10;</div>
<div id="comment-tools-12960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12960-form-container" class="comment-form-container">
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

<span id="12961"></span>

<div id="answer-container-12961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12961-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible, but only if you set up a suitable server yourself. You will want to import data into a PostGIS database e.g. with imposm or osm2pgsql, and then write some code (e.g. in PHP or another scripting language) that lets the client request something and it replies with a geometry.</p>
<p>The existing services - most notably Overpass API but also the XAPI instances you mentioned - will be able to answer simple queries like "give me all objects have ref=A7 in this bounding box" or "give me all members of a route relation called ref=A7", and this might be sufficient to build a prototype, but you won't be able to build a proper application with that for a number of reasons:</p>
<ul>
<li>in some cases you might have to do different searches to find the object you want and it will be too time consuming to run all that from within the browser</li>
<li>since these services don't reply with a complete geometry but instead with a series of nodes and ways, you'll have to parse and process that in the browser which might be time consuming as well</li>
<li>especially if you are "zoomed out", these services will return the full, detailed geometry of the object having tens of thousands of nodes and consisting of many parts, when it would be much easier for you to have an assembled and simplified geometry</li>
<li>if your application has more than the occasional visitor, you might be unduly placing load on the volunteer-operated XAPI/Overpass services.</li>
</ul>
<p>In addition to what has already been discussed, there's also the routing engine at project-osrm.org which already has some neat features e.g. producing a simplified geometry, but with that engine you can only acces the fastest route between to points and not something arbitrary like "Autobahn x" or so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '12, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12961" class="comments-container">
<span id="12963"></span>
<div id="comment-12963" class="comment">
<div id="post-12963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, my plan is to use a server which will provide the path data (forgot to mention that, I've updated my question)<br />
The simplified geometry from project-osrm.org sounds promising, I will check this.</p>
<p>I just wonder: road information seems to me a very basic part of a project called OpenStreetMap; the information I want is very fundamental for the map rendering and for navigation applications - so why it is a non trivial task to get this kind of data?</p>
<p>If I get it right, using the services mentioned I have to</p>
<ol>
<li>get information about the road, using a number of region searches, then</li>
<li>dig deeper, using the results of the first queries the get more information</li>
<li>filter out duplicate, and unnecessary data</li>
<li>assemble my own Autobahn Object, and store it in my database, suitable for a web page</li>
</ol>
<p>This is quite a bit.</p>
</div>
<div id="comment-12963-info" class="comment-info">
<span class="comment-age">(26 May '12, 00:17)</span> <span class="comment-user userinfo">Gisela</span>
</div>
</div>
<span id="12965"></span>
<div id="comment-12965" class="comment">
<div id="post-12965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The information you want is there in the database, but the database is not organised in a way that would easily serve your particular query. That's why you have to do this organising yourself. Everyone who does rendering or navigation will pre-process OSM data into the strucuture that best serves the use case. If you are interested in a "I think OSM should be offering X" type of discussion, then the talk mailinglist would be a good place for that.</p>
</div>
<div id="comment-12965-info" class="comment-info">
<span class="comment-age">(26 May '12, 00:58)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="12966"></span>
<div id="comment-12966" class="comment">
<div id="post-12966-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answers and the insights, I know that I have to go deeper into the docs - and surely will (it's my first day here).</p>
</div>
<div id="comment-12966-info" class="comment-info">
<span class="comment-age">(26 May '12, 01:16)</span> <span class="comment-user userinfo">Gisela</span>
</div>
</div>
</div>
<div id="comment-tools-12961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12961-form-container" class="comment-form-container">
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

