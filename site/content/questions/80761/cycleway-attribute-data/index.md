+++
type = "question"
title = "Cycleway attribute data"
description = '''I downloaded the cycleway layer from Geofabrik as a shapefile and was using it in ArcGIS.  On OSM I can see attributes like width, pavement type, etc. However, in ArcGIS attribute data table I see none of this.  How can I access that attribute data for the cycleway layer?'''
date = "2021-06-28T15:12:00Z"
lastmod = "2021-12-10T22:40:00Z"
weight = 80761
keywords = [ "shapefile", "arcgis", "attributes", "geofabrik", "cycleway" ]
aliases = [ "/questions/80761" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cycleway attribute data](/questions/80761/cycleway-attribute-data)

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
<span id="post-80761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded the cycleway layer from Geofabrik as a shapefile and was using it in ArcGIS.</p>
<p>On OSM I can see attributes like width, pavement type, etc.</p>
<p>However, in ArcGIS attribute data table I see none of this.</p>
<p>How can I access that attribute data for the cycleway layer?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '21, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a06fb5e6e6895e4ebb15a9ebfdf5d3b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juradoN&#39;s gravatar image" />
<p><span>juradoN</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juradoN has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80761" class="comments-container">
<span id="80765"></span>
<div id="comment-80765" class="comment">
<div id="post-80765-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you clarify exactly what you downloaded and from where? As far as I know, the data extracts from Geofabrik are arranged by geographic region and contain all of the OSM data for that region with all tags included. I can't find a cycling-specific extract on their site.</p>
</div>
<div id="comment-80765-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 17:42)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="80766"></span>
<div id="comment-80766" class="comment">
<div id="post-80766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded washington-latest-free.shp.zip from Geofabrik (<a href="https://download.geofabrik.de/north-america/us/washington.html).">https://download.geofabrik.de/north-america/us/washington.html).</a> This is for the entire Washington State in U.S. And yes, I did get what looks to be all of the OSM data for that region. However, the roads layer that was within that file has different attributes than the fields/attributes you see when editing within OSM. For example, I can add a width in OSM when editing a cycleway. But in the shapefile attribute table in ArcGIS, I see no 'width' field. So I'm curious, OSM obviously has attributes for certain cycleways (ex. width) but I can't see it in ArcGIS even after downloading the entire dataset. So where would I access these attributes?</p>
</div>
<div id="comment-80766-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 18:06)</span> <span class="comment-user userinfo">juradoN</span>
</div>
</div>
<span id="82808"></span>
<div id="comment-82808" class="comment">
<div id="post-82808-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Geofabrik shape files only contain a very small set of attributes present in OSM (at least in part because they sell services around more detailed extracts). You will find more details by using an OSM download (Pbf file for the area, and extracting the relevant details yourself) or through querying data via Overpass(-turbo).</p>
</div>
<div id="comment-82808-info" class="comment-info">
<span class="comment-age">(10 Dec '21, 22:40)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80761-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

