+++
type = "question"
title = "Identifying Roads Uniquely and Traffic API"
description = '''I&#x27;m currently working on a project which involves tracing the path(GPS coordinates) taken by a vehicle (1) and measuring the traffic conditions(is it jammed and whats the speed during the time the vehicle was there) along the path in which the driver took (2). This is to judge whether the driver had...'''
date = "2015-06-03T12:14:00Z"
lastmod = "2015-06-08T13:24:00Z"
weight = 43370
keywords = [ "roads", "api", "traffic", "road" ]
aliases = [ "/questions/43370" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying Roads Uniquely and Traffic API](/questions/43370/identifying-roads-uniquely-and-traffic-api)

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
<span id="post-43370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43370-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently working on a project which involves tracing the path(GPS coordinates) taken by a vehicle (1) and measuring the traffic conditions(is it jammed and whats the speed during the time the vehicle was there) along the path in which the driver took (2). This is to judge whether the driver had made the appropriate actions to drive environmentally friendly and fuel efficiently during his time on route.</p>
<p>Therefore i need 2 things.</p>
<p>(1) A Way to Uniquely identify each road based on their direction it heads towards ( 2 or more for each road) I understand that there are OpenStreetMaps- WAY which provides me a set of nodes which will identify a road with a unique id however i am currently struggling to find the API service which can provide it to me.</p>
<p>(2) Any traffic APi reccomendation that can provide me with historical traffic data which i can use.</p>
<p>Cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '15, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/58bb60c363eb14f0cbbb9b37e75e4a6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DillyDallyKing&#39;s gravatar image" />
<p><span>DillyDallyKing</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DillyDallyKing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43370" class="comments-container">
<span id="43379"></span>
<div id="comment-43379" class="comment">
<div id="post-43379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>about (1): Maybe you need something like geocoding? then see <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a> ...</p>
<p>or about the most used OSM APIs: <a href="https://wiki.openstreetmap.org/wiki/Xapi">https://wiki.openstreetmap.org/wiki/Xapi</a></p>
<p>or (even better!): <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
</div>
<div id="comment-43379-info" class="comment-info">
<span class="comment-age">(03 Jun '15, 16:41)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-43370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43370-form-container" class="comment-form-container">
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

<span id="43429"></span>

<div id="answer-container-43429" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43429-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For this task I suggest to use the <a href="https://github.com/graphhopper/map-matching">map matching project</a> (where I'm the author of)</p>
<p>With this project you can easily associate arbitrary GPS coordinates to edge IDs of GraphHopper. An edge is the connection between two junctions. And then you can use this to influence the routing of GraphHopper itself. I've blogged about the map matching <a href="https://karussell.wordpress.com/2015/05/26/map-matching-use-cases-or-why-an-open-source-and-open-data-alternative-is-superior-to-the-google-maps-roads-api/">here</a> and also about the traffic influenced routing <a href="https://karussell.wordpress.com/2015/04/08/visualize-and-handle-traffic-information-with-graphhopper-in-real-time-for-cologne-germany-koln/">here</a>. The problem you'll encounter is that you can get the edge IDs but not the OSM IDs and you'll have to take care when you re-import the data with fresh OSM data where the edge IDs will change. But as I've already done this several times I can say there are ways to make it working ;)</p>
<p>For the second part of your question I only have a partial answer. We've started to collect some open/free data sources <a href="https://github.com/graphhopper/open-traffic-collection">here</a> where often e.g. only the traffic counts is available (not the flow or speed of the vehicles). Feel free to add your known sources and maybe make this more popular so that more people add their sources ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '15, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '15, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-43429" class="comments-container">
&#10;</div>
<div id="comment-tools-43429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43453"></span>

<div id="answer-container-43453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43453-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is currently an open project well underway to define both an API and a matching algorithm based on OSM data here: <a href="https://github.com/opentraffic">https://github.com/opentraffic</a> they use an approach based on osm ID and way start/end coordinates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '15, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-43453" class="comments-container">
&#10;</div>
<div id="comment-tools-43453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43453-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43465"></span>

<div id="answer-container-43465" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43465-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For (1) (identifying roads), it depends on how you want to process the data. if you were to import OSM data into a PostGIS database with osm2pgsql, then you can look at the <code>osm_id</code> column to determine the OSM id of the underlying way object. However, OSM can, and does, split ways when a tag changes, so "one street"/"one road" can be represented as many different ways in OSM.</p>
<p>It's also possible for an OSM object to be deleted and replaced by a mapper, meaning the old id would no longer be valid and there'd be a new id.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '15, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43465" class="comments-container">
&#10;</div>
<div id="comment-tools-43465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43465-form-container" class="comment-form-container">
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

