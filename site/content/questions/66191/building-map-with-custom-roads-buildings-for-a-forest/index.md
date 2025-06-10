+++
type = "question"
title = "Building map with custom roads &amp; buildings for a forest?"
description = '''I have to create a navigation-system app for a local forest, where most of the &quot;streets&quot; aren&#x27;t registered by OpenStreetMap. How is it possible to extend existing maps with custom paths? (New streets, which can be navigated to) So at the end I want a map, which includes some new paths, that brings t...'''
date = "2018-10-06T15:23:00Z"
lastmod = "2018-10-07T13:13:00Z"
weight = 66191
keywords = [ "map", "mapserver", "osm", "tiles", "mapbox" ]
aliases = [ "/questions/66191" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Building map with custom roads & buildings for a forest?](/questions/66191/building-map-with-custom-roads-buildings-for-a-forest)

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
<span id="post-66191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66191-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have to create a navigation-system app for a local forest, where most of the "streets" aren't registered by OpenStreetMap.</p>
<p>How is it possible to extend existing maps with custom paths? (New streets, which can be navigated to)</p>
<p>So at the end I want a map, which includes some new paths, that brings the user to custom destinations. (e.g. "feeding boxes" for animals)</p>
<p>I already have the whole map-information already in a shape-format, but how can I extract it to osm? How can I create an OSM with this custom road-data? Should I host an own map server?</p>
<p>I am looking forward to your answers &amp; please help me!! :)</p>
<p>Marko</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '18, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/5c315e9f747d2adb03306ad33718d506?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markoo91&#39;s gravatar image" />
<p><span>markoo91</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markoo91 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66191" class="comments-container">
&#10;</div>
<div id="comment-tools-66191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66191-form-container" class="comment-form-container">
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

<span id="66198"></span>

<div id="answer-container-66198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66198-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There seem to be both technical and legal aspects to your question. In principle, adding paths or tracks to OpenStreetMap isn't an issue provided they actually exist on the ground and the source for your information is compatible with the <a href="https://wiki.osmfoundation.org/wiki/Licence">OpenStreetMap license</a>. I mention the license here because you say you have a shape file for the data, but don't mention the source. I know very little about the legal side of things, but I think the copyright holder would have to give express permission for the data to be included in OSM and published under OpenStreetMap's licensing terms. There are <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a> for this.</p>
<p>Adding streets to OpenStreetMap is fairly simple and many editors are available, the most popular being the in browser editors iD and Potlatch 2 (available on the main site) and JOSM (standalone download). Some of these have <a href="https://wiki.openstreetmap.org/wiki/Shapefiles#Obtaining_OSM_data_from_shapefiles">shapefile support</a> if you are sure you have proper permission to use it. As you put the word "streets" in quotation marks, I think it might help if you look at the <a href="https://wiki.openstreetmap.org/wiki/Key:highway">highway page</a> on the wiki as they might be better classified as a <em>track</em> or <em>path</em> in OSM terms.</p>
<p>Your "feeding boxes" sound like they might be either "<a href="https://wiki.openstreetmap.org/wiki/Tag:vending%3Danimal_feed">vending=animal_feed</a>", "<a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dfeeding_place">amenity=feeding_place</a>" or "<a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dgame_feeding">amenity=game_feeding</a>".</p>
<p>There are several starting points for creating apps depending on whether you are creating something for <a href="https://wiki.openstreetmap.org/wiki/Android#Libraries_for_developers">Android</a>, <a href="https://wiki.openstreetmap.org/wiki/Apple_iOS#Libraries_for_developers">iOS</a> or <a href="https://wiki.openstreetmap.org/wiki/Routing#Developers">the web</a>. Some keep all the map data on the device (probably sensible for something the size of <em>a</em> forest) and so may not need a tile-server or any internet connectivity at all while they are being used. Others rely much more heavily on a constant internet connection. There are also commercial providers of map tiles and back end services based on OSM that might work out cheaper than running your own server. I'm afraid I can't give any specific recommendations as I'm not a developer myself and am still a little unclear on your use case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '18, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-66198" class="comments-container">
&#10;</div>
<div id="comment-tools-66198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66198-form-container" class="comment-form-container">
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

