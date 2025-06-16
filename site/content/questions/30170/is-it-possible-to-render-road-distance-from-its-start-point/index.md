+++
type = "question"
title = "Is it possible to render road distance from its start point ?"
description = '''Is it possible to render marks with current distance from a road start to map tiles in Mapnik ? We are looking for some way how to configure, or add rendering of a distance from road start point near to roads in some sensible frequency and only for higher zoom levels in kilometers. Here is an exampl...'''
date = "2014-01-24T09:20:00Z"
lastmod = "2014-01-26T16:00:00Z"
weight = 30170
keywords = [ "openstreetmap", "distance", "switch2osm", "road", "mapnik" ]
aliases = [ "/questions/30170" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to render road distance from its start point ?](/questions/30170/is-it-possible-to-render-road-distance-from-its-start-point)

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
<span id="post-30170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to render marks with current distance from a road start to map tiles in Mapnik ? We are looking for some way how to configure, or add rendering of a distance from road start point near to roads in some sensible frequency and only for higher zoom levels in kilometers. Here is an example of what we would like to prerender on our tiles (of course, it would be enough to show just a number of kilometers in some uniquely looking mark):</p>
<p><img src="/upfiles/RoadDistance.png" alt="alt text" /></p>
<p>These values are "statical", so it would be great to have them prerendered on our tiles. We're using Mapnik renderer as part of the Switch2osm server.</p>
<p>Is that even possible ? If so, did we miss an existing settings or do we need to write some plugin for this feature ?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '14, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d6b3f1a4100f56e3e3c0874c82141ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TLama&#39;s gravatar image" />
<p><span>TLama</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TLama has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '14, 10:11</strong> </span></p>
</div>
</div>
<div id="comments-container-30170" class="comments-container">
&#10;</div>
<div id="comment-tools-30170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30170-form-container" class="comment-form-container">
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

<span id="30174"></span>

<div id="answer-container-30174" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30174-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TLama has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is certainly possible but OSM does not necessarily know where the "starting point" of a certain road is, and the road will consist of many many pieces in OSM, so first you have to puzzle together the pieces and know where to count from, then you could go about measuring the length. It's not somthing that can simply be "configured", it will require programming.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '14, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30174" class="comments-container">
<span id="30176"></span>
<div id="comment-30176" class="comment">
<div id="post-30176-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Most likely the creation of an SQL function, which returns points with the distances as attributes. But I don't fancy trying to write the string-together-linestrings-sort-merge-and-handle-dual-carriageways query!</p>
</div>
<div id="comment-30176-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 10:58)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="30194"></span>
<div id="comment-30194" class="comment">
<div id="post-30194-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are dealing with the US, the national and state routes have all been put into relations which will help you "puzzle together the bits and know where to count from". My understanding is that there route relations are frowned upon in other parts of the world, so they may not be available where you need it.</p>
</div>
<div id="comment-30194-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 20:38)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="30238"></span>
<div id="comment-30238" class="comment">
<div id="post-30238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Andy Allan</span> is quite right transforming OSM data to be able to calculate this distance markers is horrendous. Creating lots of routes using a routing engine, transforming them into linestrings &amp; chopping them up might work. (more or less what <span>@Richard</span> says below)</p>
</div>
<div id="comment-30238-info" class="comment-info">
<span class="comment-age">(26 Jan '14, 16:00)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30174-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30190"></span>

<div id="answer-container-30190" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30190-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's certainly possible, but far from trivial.</p>
<p>First, you need to create linestrings for the roads where you want to show these mileages, chainages or whatever modern measurement system you may be using ;) .</p>
<p>It's possible to do this algorithmically from the raw data in OSM. Andy has mentioned in his comment above one way of doing it; I've also done it by downloading the data for an OSM route relation, then processing it in Ruby to order it correctly and smooth out the little hiccups along the way. But don't underestimate the complexity of this, especially where dual carriageways are concerned.</p>
<p>Instead, if you're dealing with a manageable dataset (say, "all the autoroutes in France" rather than "all the trunk roads in the world"), I would suggest that you manually create these linestrings with a routing program. In particular, <a href="http://project-osrm.org/">OSRM</a> makes it easy to plan a route and export it as an easily parseable GPX file. Do this for all the motorways you need. Motorways don't move very often so it should be a one-time task!</p>
<p>You can then load these linestrings into your PostGIS database. PostGIS and Mapnik ninjas will doubtless be able to write a query that automatically generates shields with the correct value every 1km. I'd personally prefer to precompute the kilometre points into a separate table. Whatever, you probably want to loop using <a href="http://postgis.net/docs/manual-2.0/ST_LocateAlong.html">ST_LocateAlong</a> to find the point at each kilometre. Finally, add rendering rules for this in your Mapnik stylesheet.</p>
<p>Footnote: I've done something related, but using user-generated routes and rendering the mile/kilometre points dynamically in Leaflet rather than Mapnik. Have a look at <a href="http://cycle.travel/map">cycle.travel/map</a> - plan a route and see the yellow dots along the way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '14, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-30190" class="comments-container">
&#10;</div>
<div id="comment-tools-30190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30190-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30171"></span>

<div id="answer-container-30171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30171-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi and welcome to the world of OSM :)</p>
<p>As I understand your question, you want to do a distance (here: by traveltime) anaylsis and visualize it on top of the default mapnik map style?</p>
<p>This is something that <a href="http://neis-one.org/2010/09/osm-fur-die-feuerwehr-2-0/">Pascal neis realized</a> some time ago to do analysis for the coverage of firefighters. Unfortunatly the OpenLS service is still down, so you might migrate the idea <a href="https://wiki.openstreetmap.org/wiki/OpenRouteService#What_can_you_do_on_ORS.3F">to OpenRouteServe AAS</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '14, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-30171" class="comments-container">
<span id="30173"></span>
<div id="comment-30173" class="comment">
<div id="post-30173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I'm not sure if I explained our needs well (I've added an example image). The information we'd like to render are quite "statical", so I'm not so sure if routing services are the best for us (we were hoping for some style settings, but maybe your suggestion is the way to go). Basically, on tiles we would like to show that you're looking e.g. on 115th km of the road (from its starting point).</p>
</div>
<div id="comment-30173-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 10:12)</span> <span class="comment-user userinfo">TLama</span>
</div>
</div>
<span id="30177"></span>
<div id="comment-30177" class="comment">
<div id="post-30177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the update. Obviously I had a misunderstanding on your request. Sorry!</p>
</div>
<div id="comment-30177-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 11:11)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-30171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30171-form-container" class="comment-form-container">
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

