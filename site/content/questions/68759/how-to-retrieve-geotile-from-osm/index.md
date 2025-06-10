+++
type = "question"
title = "How to retrieve geotile from OSM ?"
description = '''I am using Cesium, and I would like to make a 3d city representation. I would like to retrieve a .json of the current location I am from OpenStreetMap. I have the position and the altitude of where I am. The problem is that I do not understand/can&#x27;t find from which url source I can retrieve building...'''
date = "2019-04-11T10:03:00Z"
lastmod = "2020-09-20T16:36:00Z"
weight = 68759
keywords = [ "building", "tiles", "geocoding", "3d" ]
aliases = [ "/questions/68759" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve geotile from OSM ?](/questions/68759/how-to-retrieve-geotile-from-osm)

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
<span id="post-68759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Cesium, and I would like to make a 3d city representation.</p>
<p>I would like to retrieve a .json of the current location I am from OpenStreetMap. I have the position and the altitude of where I am.</p>
<p>The problem is that I do not understand/can't find from which url source I can retrieve buildings ID and their relative height for a defined tileset position in openstreetmap</p>
<p>I found a lot of exemple on internet and lib that do this, but I need to do it from source, and I do not quite know how.</p>
<p>Basically, how does for exemple this : <a href="https://osmbuildings.org/">https://osmbuildings.org/</a> get the data from</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f5b0c2461f5b2cabf3bc0708903e90e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Popolee&#39;s gravatar image" />
<p><span>Popolee</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Popolee has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '19, 10:25</strong> </span></p>
</div>
</div>
<div id="comments-container-68759" class="comments-container">
&#10;</div>
<div id="comment-tools-68759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68759-form-container" class="comment-form-container">
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

<span id="68782"></span>

<div id="answer-container-68782" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68782-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally speaking, openstreetmap.org itself only provides raw data. This is done as bulk downloads of the entire planet and as very small on demand extracts for editing purposes. There is some capacity for larger extracts on openstreetmap.org, but availability is <a href="https://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#Sources_of_OSM_Data">dependant on server load</a>. Regularly updated extracts for countries/cities are available <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">via other sites</a>. I believe, <a href="https://download.bbbike.org/osm/">bbbike.org</a>'s service supports geojson, if that is what you require.</p>
<p>Unfortunately, for the larger part of your question I can't offer much help. OpenStreetMap has it's own data format that stores what 3D information it has as tags on the relevant objects. The most common scheme for this seems to be <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_buildings">Simple 3D Buildings</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '19, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-68782" class="comments-container">
&#10;</div>
<div id="comment-tools-68782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68782-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76723"></span>

<div id="answer-container-76723" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(Copied from <a href="https://stackoverflow.com/a/55749711/1391631">my StackOverflow answer</a> to the same question.)</p>
<p>OSM has the data that's necessary to set up such a service, but the various providers use different formats as there's not really a clear standard yet (unlike with 2D raster and, arguably, vector maps). For use with Cesium, you probably want <a href="https://github.com/AnalyticalGraphicsInc/3d-tiles">Cesium 3D Tiles</a>.</p>
<p>Cesium is offering their own building layer based on OSM data, called <a href="https://cesium.com/content/cesium-osm-buildings/">Cesium OSM Buildings</a> (no relationship with OSM Buildings), on their Cesium Ion platform. It does not fully support the OSM data model at this point, but the Cesium integration is obviously well done.</p>
<p>I'm not sure what <a href="https://osmbuildings.org/">OSM Buildings</a> is currently using, but it does not seem to be the same as Cesium's 3D Tiles. <a href="https://github.com/OSMBuildings/OSMBuildings/blob/master/docs/server.md">Some older info on GitHub</a> mentions using GeoJSON, but looking at the network traffic, it now seems to be using <a href="https://docs.mapbox.com/vector-tiles/specification/">Mapbox Vector tiles</a>, which is not a format specialized for 3D data, but rather a general-purpose solution for transmitting OSM data (and other data sources) as tiled vector maps. On <a href="https://osmbuildings.org/data/">osmbuildings.org/data</a>, they mention that they are willing to provide data in other formats for commercial customers, though, if that's an option for you.</p>
<p>Finally, some people have experimented with providing OSM for Cesium using open source software (see e.g. the <a href="https://github.com/kiselev-dv/osm-cesium-3d-tiles">osm-cesium-3d-tiles</a> and <a href="https://github.com/stirringhalo/osm2cesium">osm2cesium</a> repos). This might be a starting point for setting up your own service if you're willing to go down that path, but it's definitely not a complete and polished solution at this point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '20, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-76723" class="comments-container">
&#10;</div>
<div id="comment-tools-76723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76723-form-container" class="comment-form-container">
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

