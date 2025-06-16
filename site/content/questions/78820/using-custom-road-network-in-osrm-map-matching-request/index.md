+++
type = "question"
title = "Using custom road network in OSRM map matching request"
description = '''For a project I&#x27;m using OSRM to map match a series of GPS measurements to a custom road network. My goal is to provide insight in where but more importantly how many times the vehicle has visited each road segment in the road network. My desired output is (1) an attribute table of the road network w...'''
date = "2021-02-12T15:32:00Z"
lastmod = "2021-02-16T15:51:00Z"
weight = 78820
keywords = [ "osrm", "osm", "matching", "ogr2osm", "map" ]
aliases = [ "/questions/78820" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using custom road network in OSRM map matching request](/questions/78820/using-custom-road-network-in-osrm-map-matching-request)

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
<span id="post-78820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78820-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For a project I'm using OSRM to map match a series of GPS measurements to a custom road network. My goal is to provide insight in where but more importantly how many times the vehicle has visited each road segment in the road network. My desired output is (1) an attribute table of the road network with an extra column that shows the number of times the vehicle drove through the street, (2) a map visualisation of the flow of traffic through the network, with the width of each line segment representing the amount of traffic (i.e. based on the visit frequency values in the attribute table). Something like this:</p>
<p><img src="/upfiles/Screen_Shot_2021-02-10_at_16.17.08.png" alt="alt text" /></p>
<p>I have been able to convert a custom road network in shapefile format to .osm data using ogr2osm and succesfully map match the GPS points to this network. Using the option "annotations=nodes" in the OSRM request I'm able to get all the node id pairs and geometry from the API response. This would allow me to tabulate and rank the most common segments, and display them visually, no joining to a PBF required. However, the original node id's from the shapefile appear to have lost after the conversion. Instead, new node id's have been chronologically numbered in the .osm file (see below). This makes it impossible to come to the desired output as described above. Does anyone have a solution to retain the original node id's from the original shapefile road network? Or does somebody havee a better solution for what I'm trying to achieve?</p>
<p><img src="/upfiles/Screen_Shot_2021-02-12_at_15.06.55.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span> <span class="post-tag tag-link-ogr2osm" rel="tag" title="see questions tagged &#39;ogr2osm&#39;">ogr2osm</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '21, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/152906fc74217eeefa79ad3b652b3380?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winecity&#39;s gravatar image" />
<p><span>winecity</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winecity has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '21, 15:36</strong> </span></p>
</div>
</div>
<div id="comments-container-78820" class="comments-container">
<span id="78827"></span>
<div id="comment-78827" class="comment">
<div id="post-78827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Slightly confused by this - what do you mean by "original node ids from the shapefile"? Shapefile linestring geometries don't have node ids.</p>
</div>
<div id="comment-78827-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 19:35)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="78862"></span>
<div id="comment-78862" class="comment">
<div id="post-78862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The attribute table of my shapefile has a column "source" and a column "target" to indicate the node id's. I was hoping these node id's would be recognized in the .osm file after the conversion, but apparently this is not the case. Do you know if there's another way?</p>
</div>
<div id="comment-78862-info" class="comment-info">
<span class="comment-age">(15 Feb '21, 13:15)</span> <span class="comment-user userinfo">winecity</span>
</div>
</div>
<span id="78883"></span>
<div id="comment-78883" class="comment">
<div id="post-78883-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Shapefiles aren't topological (i.e. they don't represent junctions between roads). Linestrings in shapefiles do not have individual attributes for each point, only for the linestring as a whole. For what you're trying to do, a shapefile seems a really bad fit. It would be better if you could get your software to output .osm directly.</p>
</div>
<div id="comment-78883-info" class="comment-info">
<span class="comment-age">(16 Feb '21, 15:51)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78820-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

