+++
type = "question"
title = "Right Importer/Database Schema to store OSM road nodes and intersections (relations)?"
description = '''I&#x27;m looking to develop an application that requires a database of nodes and relations (intersections) of roads in an area. I don&#x27;t need to specifically pick out the roads within a map segment, however having the upcoming intersections in a road given GPS coordinates is a must. I&#x27;ve been looking into...'''
date = "2012-11-19T08:08:00Z"
lastmod = "2012-12-02T17:08:00Z"
weight = 17787
keywords = [ "intersections", "road", "database" ]
aliases = [ "/questions/17787" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Right Importer/Database Schema to store OSM road nodes and intersections (relations)?](/questions/17787/right-importerdatabase-schema-to-store-osm-road-nodes-and-intersections-relations)

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
<span id="post-17787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17787-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking to develop an application that requires a database of nodes and relations (intersections) of roads in an area. I don't need to specifically pick out the roads within a map segment, however having the upcoming intersections in a road given GPS coordinates is a must.</p>
<p>I've been looking into OSM and a few of its add-ons however I haven't been able to pinpoint the one that's right for me. Could anyone shed some light on which tool to use?</p>
<p>NOTE: I do not need to render maps graphically. It's a simple question of being given a point and knowing the locations of upcoming relations in the road.</p>
<p>I've looked into osmosis + osm2pgsql, however the latter doesn't seem to be ideal for routing purposes. I'm also looking into pgRouting, however once again I'm not entirely sure I'll be able to get the right info. If anyone with similar experience could push me in the right direction that would be awesome!</p>
<p>(Also, is there any preferred DBMS for OSM purposes? I'm usually a MSSQL guy, however I haven't heard of any particular benefits in using MySQL or any other system for this use. )</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '12, 08:08</strong></p>
<img src="https://secure.gravatar.com/avatar/afbf8ac71c39825569d7ba732a0c304c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JuZeeMan&#39;s gravatar image" />
<p><span>JuZeeMan</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JuZeeMan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17787" class="comments-container">
&#10;</div>
<div id="comment-tools-17787" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17787-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="17792"></span>

<div id="answer-container-17792" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17792-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A relatively simple way to achieve your goal could be downloading a suitable shape file from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> (provided there is one for your area), then take the roads layer and import it into a spatial database of your choice. Then use a couple SQL queries to determine intersections (i.e. anything where two road geometries intersect and neither has the bridge/tunnel flag), and take it from there. This means you'll unnecessarily reverse-engineer the intersections (the presence of which could have been detected from looking at the OSM raw data, where both roads would share the same node) but it works without any extra importing software - apart from some shapefile importer which any spatial database will come equipped with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '12, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17792" class="comments-container">
<span id="17969"></span>
<div id="comment-17969" class="comment">
<div id="post-17969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like a great and simple approach! I was going to try loading an osm file of my region into (PostGreSQL +)PostGIS to work with that but I'm not too sure what the difference in data would be tbh. Any specific differences you may know of?</p>
<p>So far, for the scope of this project, it seems that as long as I have road data then I should be safe, though I suppose having extra data might come in handy in the future.</p>
</div>
<div id="comment-17969-info" class="comment-info">
<span class="comment-age">(25 Nov '12, 15:21)</span> <span class="comment-user userinfo">JuZeeMan</span>
</div>
</div>
<span id="18152"></span>
<div id="comment-18152" class="comment">
<div id="post-18152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking further into this approach...though I can't really make heads or tails of the rows added to the DB.</p>
<p>In the meantime I've given NETCONVERT within the SUMO simulator a go, however, once again I'm not sure how to read this output into a DB. The problem here is that SUMO maps the coordinates onto a new map, resetting all the coordinates according to its own X and Y coordinates.</p>
<p>I have loaded the roads layer as you suggested, and indeed! I have managed to get a table of node ids (osm_id). Filtering out the intersections will be a tad trickier but I'll give that a shot. Thanks again!</p>
</div>
<div id="comment-18152-info" class="comment-info">
<span class="comment-age">(02 Dec '12, 17:08)</span> <span class="comment-user userinfo">JuZeeMan</span>
</div>
</div>
</div>
<div id="comment-tools-17792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17792-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17791"></span>

<div id="answer-container-17791" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17791-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Interesting project :-). However, I don't think there's existing software which does exactly that, so you'll need to roll your own. You can, however, use some infrastructure for parsing &amp; processing the data. <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> e.g. may help.</p>
<p>You will probably need to <a href="http://wiki.openstreetmap.org/wiki/Download">download the OSM data</a>, and then simplify it. You apparently only need roads, so you can filter out all the rest (boundaries, POIs etc.). Then you could do something like:</p>
<ul>
<li>input: GPS coordinates</li>
<li>find the nearest road (that's probably where you are)</li>
<li>find direction of movement/driving</li>
<li>move along the road in driving direction until you hit an intersection</li>
</ul>
<p>In OSM data, intersections are simply OSM nodes which are members of more than one road. Take care, however, that longer roads are usually split into multiple OSM ways, so it may be non-trivial to decide if something is an intersection. Also, you may want to discard crossing foot-paths etc...</p>
<blockquote>
<p>(Also, is there any preferred DBMS for OSM purposes? I'm usually a MSSQL guy, however I haven't heard of any particular benefits in using MySQL or any other system for this use. )</p>
</blockquote>
<p>Most OSM software uses PostGreSQL (specifically, PostGIS). But the best DB will depend on which software you use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '12, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-17791" class="comments-container">
&#10;</div>
<div id="comment-tools-17791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17791-form-container" class="comment-form-container">
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

