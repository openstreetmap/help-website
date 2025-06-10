+++
type = "question"
title = "Calculate route and the list of places along the route"
description = '''Hi. First of All. I&#x27;m new to OSM. I ask this question in general form because I don&#x27;t know where to look for this kind of solution. I need the list of Cities and Villages that will be along the route from from point A (specified by lat,lon) to the point B (also specified by lat,lon). This list shoul...'''
date = "2011-12-13T12:56:00Z"
lastmod = "2011-12-17T17:53:00Z"
weight = 9495
keywords = [ "development", "cities", "routing", "places", "waypoints" ]
aliases = [ "/questions/9495" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Calculate route and the list of places along the route](/questions/9495/calculate-route-and-the-list-of-places-along-the-route)

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
<span id="post-9495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9495-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. First of All. I'm new to OSM.</p>
<p>I ask this question in general form because I don't know where to look for this kind of solution.</p>
<p>I need the list of Cities and Villages that will be along the route from from point A (specified by lat,lon) to the point B (also specified by lat,lon). This list should be in correct order from point A to B.</p>
<p>For now I have a database with all Cities, and Villages in Country with lat,lon coordinates for each entry. I don't have connections between those places in this database. Now I'm wondering how to add to this feature to show me the names of the places on the route from point A to point B (or from one place to other)</p>
<p>Can anybody give me some advice how to develop this kind of feature similar to routing. This feature will be developed for the website that is based on PHP and MySQL only.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-places" rel="tag" title="see questions tagged &#39;places&#39;">places</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '11, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e2bc1331dd17a1b2a2ad8e774766e3e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kapucha&#39;s gravatar image" />
<p><span>Kapucha</span><br />
<span class="score" title="45 reputation points">45</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kapucha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '13, 22:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-9495" class="comments-container">
<span id="9499"></span>
<div id="comment-9499" class="comment">
<div id="post-9499-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where is OSM in your question ? the places locations ? the path between them ? Or is it just a developer question about routing algorithmes ?</p>
</div>
<div id="comment-9499-info" class="comment-info">
<span class="comment-age">(13 Dec '11, 16:06)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="9501"></span>
<div id="comment-9501" class="comment">
<div id="post-9501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Several questions come up in my mind. First of all: do you need an exact route between the two places or just an "as the crow flies" straight line? What is the coverage of your app? Whole world or just a single country?</p>
</div>
<div id="comment-9501-info" class="comment-info">
<span class="comment-age">(13 Dec '11, 16:46)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
<span id="9503"></span>
<div id="comment-9503" class="comment">
<div id="post-9503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where did these cities, villages etc come from? OSM? If so, you need to also get the roads or tracks or rivers or railways or cycleways or whatever your route is using to then calculate the route.</p>
<p>Cities and villages are not a single lon-lat. They cover an area. if your route just passes the lon-lat for a village did it go through the edge of a big village or pass a small one by?</p>
</div>
<div id="comment-9503-info" class="comment-info">
<span class="comment-age">(13 Dec '11, 17:30)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="9505"></span>
<div id="comment-9505" class="comment">
<div id="post-9505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Breki</span> One Country. No straight line. along the public roads. Straight line with some kilometers tolerancy is simple for me. I see that I need to calculate the route along the public roads. Then in some way analyze this route and get the cities and villages near this route in correct order.</p>
</div>
<div id="comment-9505-info" class="comment-info">
<span class="comment-age">(13 Dec '11, 21:53)</span> <span class="comment-user userinfo">Kapucha</span>
</div>
</div>
<span id="9506"></span>
<div id="comment-9506" class="comment">
<div id="post-9506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@ChrisH</span> The data is not from OSM. I have database with all the cities and villages from one country but this is not from OSM. I don't have connections between those places in database. I need to get it from some place because without this I can't calculate the route I assume.</p>
</div>
<div id="comment-9506-info" class="comment-info">
<span class="comment-age">(13 Dec '11, 21:56)</span> <span class="comment-user userinfo">Kapucha</span>
</div>
</div>
</div>
<div id="comment-tools-9495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9495-form-container" class="comment-form-container">
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

<span id="9568"></span>

<div id="answer-container-9568" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9568-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kapucha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want details for each step, then this question should be broken into multiple questions. At a high level, here's the approach I would take.</p>
<ol>
<li>Route from Point A to Point B: See <a href="http://wiki.openstreetmap.org/wiki/Routing">http://wiki.openstreetmap.org/wiki/Routing</a></li>
<li>Convert the route into something that the database will understand. This is probably a Linestring in either WKT or WKB format.</li>
<li>Use the database's spatial functions to find cities/villages along the route. (Perhaps use the Buffer function to expand the LineString into a Polygon, then the Intersects function to find cities/villages -- note that I haven't checked if those are supported in MySQL).</li>
<li>Sort Cities / Villages so that they are in route-wise order. A simple approximate answer would be to sort them by distance from the starting point, under the assumption that most routes don't backtrack. A more robust approach might be to find the closest city/village to the starting point, then find the point on the route that is closest to that city/village, then repeat using that point as the new starting point and excluding cities that have already been visited.</li>
</ol>
<p>Items 3 and 4 may not be very practical to do with MySQL because its support for spatial data is very limited. If you could use any free, open source database for this, then PostgreSQL + PostGIS extension would be a much better choice. If you're locked into MySQL, then you'll probably need to do the spatial calculations externally to the database, and I'd look for a PHP wrapper of GEOS or JTS (Java Topology Suite).</p>
<p>I'd also recommend trying the <a href="http://gis.stackexchange.com/">GIS StackExchange</a> site for questions that aren't primarily about working with OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '11, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/343111beef816657beccdf3c601d600b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanHomerick&#39;s gravatar image" />
<p><span>DanHomerick</span><br />
<span class="score" title="156 reputation points">156</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanHomerick has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-9568" class="comments-container">
&#10;</div>
<div id="comment-tools-9568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9568-form-container" class="comment-form-container">
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

