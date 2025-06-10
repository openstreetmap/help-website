+++
type = "question"
title = "A* routing algorithm on OpenStreetMap data"
description = '''Hi, I imported a large area from &quot;planet.osm&quot; file into a postgresql database using Osmosis. Now, I want to implement a routing algorithm based on two locations entered by a user.  Is not really clear for me where in my database structure I should search for this two points. For example if a user en...'''
date = "2013-06-13T08:50:00Z"
lastmod = "2022-05-19T08:26:00Z"
weight = 23306
keywords = [ "routing", "osmosis" ]
aliases = [ "/questions/23306" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [A\* routing algorithm on OpenStreetMap data](/questions/23306/a-routing-algorithm-on-openstreetmap-data)

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
<span id="post-23306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23306-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I imported a large area from "planet.osm" file into a postgresql database using Osmosis.<br />
Now, I want to implement a routing algorithm based on two locations entered by a user.<br />
</p>
<p>Is not really clear for me where in my database structure I should search for this two points. For example if a user enters as starting point "London, UK" and as end point "Paris, France" where should I search for this two locations so I can start implementing my routing algorithm.<br />
</p>
<p>My database structure as created by Osmosis contains the following tables: nodes, relation_members, relations, users, way_nodes and ways.<br />
</p>
<p>I need some clear information on how the database is structured because I can not figure out where to start building my graph so I can implement A* algorithm. This routing algorithm is a part of my thesis so I can not use an allready built service.</p>
<p>Thank you,<br />
Radu-Stefan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '13, 08:50</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-23306" class="comments-container">
<span id="84516"></span>
<div id="comment-84516" class="comment">
<div id="post-84516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a way to access the graph underlying OSM api?</p>
</div>
<div id="comment-84516-info" class="comment-info">
<span class="comment-age">(19 May '22, 01:32)</span> <span class="comment-user userinfo">PeterCullenB...</span>
</div>
</div>
<span id="84518"></span>
<div id="comment-84518" class="comment">
<div id="post-84518-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Pls create a new question and do not start new topics in comments.</p>
</div>
<div id="comment-84518-info" class="comment-info">
<span class="comment-age">(19 May '22, 08:26)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23306-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="23311"></span>

<div id="answer-container-23311" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23311-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="raduzugravu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Snapshot database structure populated by Osmosis is very unsuitable for routing, at least in part because geometry for ways might not exist or be unsuitable and there is no geometry for relations. You really need to transform the data into a more suitable format. This data is really for people who want a pretty much exact copy of current data from the planet database for an area.</p>
<p>I would start by reading the <a href="http://wiki.openstreetmap.org/wiki/Routing#Libraries.2FDevelopment-Tools">wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '13, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-23311" class="comments-container">
<span id="23322"></span>
<div id="comment-23322" class="comment">
<div id="post-23322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But how can I retrive my start and end locations from the list of nodes? Right now I do a search through the hsotore tags and compare name keys with the values introducted by the user. This is really slow. Is there a way to make a search through hstore keys faster? My database implementation uses Postgis functionality. My problem is in retrieving the start and end locations. Once I find my start and end points routing should be done easy using Postgis functions.</p>
</div>
<div id="comment-23322-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 11:45)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
<span id="23324"></span>
<div id="comment-23324" class="comment">
<div id="post-23324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then you probably need a nameserver like Nominatim, but I'm sceptical that you can use a raw snapshot schema. It's basically a Postgres schema not a PostGIS one (really only the nodes have location).</p>
</div>
<div id="comment-23324-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 12:14)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23311-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23337"></span>

<div id="answer-container-23337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23337-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap data can be converted into many database structures, for many different purposes. You should decide the database structure that you require first, and then import the data into your chosen structure.</p>
<p>By picking a schema without checking that it's suitable, then you're almost guaranteed to fail. It's like cementing bricks to one another, and then designing the house afterwards.</p>
<p>Of course, if you don't want to design the database structure, then you can use one that's already designed for routing, and already has an importer, like <a href="http://pgrouting.org/docs/tools/osm2pgrouting.html">osm2pgrouting</a> - but that might not be the point of the exercise.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '13, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span> </br></p>
</div>
</div>
<div id="comments-container-23337" class="comments-container">
&#10;</div>
<div id="comment-tools-23337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23337-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23366"></span>

<div id="answer-container-23366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23366-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no good way to do performant geocoding with a pgsnapshot database. If you do suitable partial indexes on (lower(tags -&gt; 'name')) (lower(tags -&gt; 'alt_name')) and similar tags you might be able to get some results, but writing a geocoder is a thesis in itself.</p>
<p>pgsnapshot is written to preserve full OSM data, which is <strong>not</strong> what you want for routing.</p>
<p>In any case, the three main tables are nodes, ways and relations. They contain the nodes, ways and relations imported into the DB with one row per object. Most of the columns for these are self-evident from the names, but tags is a <a href="http://www.postgresql.org/docs/9.1/static/hstore.html">hstore</a> with the object tags.</p>
<p>The table-specific columns are</p>
<ul>
<li>in nodes geom is the node location stored as a PostGIS POINT</li>
<li>in ways nodes is a bigint[] with a list of node IDs. Note that using this to find which ways are "parents" of a node is slow operation, even with a GIN index</li>
<li>The optional bbox and linestring columns on ways have the way bbox or linestring respectively. These probably won't help you with forming the graph as linestrings have no notion of connectivity.</li>
</ul>
<p>The way_nodes and relation_members store membership in ways and relations and allow you to find the "parent" ways or relations for a node or other object.</p>
<p>I suggest you decide if you're trying to write a geocoder or trying to write a routing engine. In either case, pgsnapshot is probably not the place to start.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '13, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23366" class="comments-container">
<span id="23369"></span>
<div id="comment-23369" class="comment">
<div id="post-23369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Thank you for your answer. What I am trying to write is a routing engine. I need to geocode start and end locations in order to know coordinates for locations introduced by the user. To obtain this coordinates I could make a request to nominatim.</p>
<p>Theoretically it should be possible to write an A* algorithm on this set of data after I get my start and end coordinates, right?</p>
</div>
<div id="comment-23369-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 11:09)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
<span id="23370"></span>
<div id="comment-23370" class="comment">
<div id="post-23370-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>yes but whether it will complete before heat-death of the universe is another matter</p>
</div>
<div id="comment-23370-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 11:22)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="23372"></span>
<div id="comment-23372" class="comment">
<div id="post-23372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Time is not that important. Of course it shouldn't take days to complete. I think somewhere under 1-2 minutes for locations not too far away one from another should be ok.</p>
<p>I have one more question. In order to write my routing algorithm my start and end nodes should be part of a way, right?</p>
</div>
<div id="comment-23372-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 11:32)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
<span id="23410"></span>
<div id="comment-23410" class="comment">
<div id="post-23410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mean if someone introduces as starting node a cultural objective (for example the name of a museum) which is not part of a way then I have to find the closest node to that starting node which is part of a way. That can be done using postgis geometry functions?</p>
</div>
<div id="comment-23410-info" class="comment-info">
<span class="comment-age">(16 Jun '13, 07:28)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
</div>
<div id="comment-tools-23366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23366-form-container" class="comment-form-container">
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

