+++
type = "question"
title = "Missing lake on Cuba when download shp file via BBBike.org or Geofabrik.de"
description = '''Hi Guys, I&#x27;ve downloaded shp file for a part of Cuba (Artemisa Province) through BBBike.org. I&#x27;ve notice one of the biggest lake/water is missing (coord: -82.875 , 22.925). It is not on any of the different shp. So I tried with another download source, Geofabrik.de, and it is the same, the lake is m...'''
date = "2013-08-29T15:15:00Z"
lastmod = "2013-08-30T12:24:00Z"
weight = 25934
keywords = [ "lake", "missing" ]
aliases = [ "/questions/25934" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing lake on Cuba when download shp file via BBBike.org or Geofabrik.de](/questions/25934/missing-lake-on-cuba-when-download-shp-file-via-bbbikeorg-or-geofabrikde)

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
<span id="post-25934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25934-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>I've downloaded shp file for a part of Cuba (Artemisa Province) through BBBike.org. I've notice one of the biggest lake/water is missing (coord: -82.875 , 22.925). It is not on any of the different shp. So I tried with another download source, Geofabrik.de, and it is the same, the lake is missing. However the lake appear on OSM.org. So I tried to edit it on OSM.org and I could see the polygone with tag "water". Could you please advise me on that matter? How is it possible? Is there a way to download it?</p>
<p>Kind Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '13, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0fb849ee5915f2c1ac0196ab3866acb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cedric_uk&#39;s gravatar image" />
<p><span>Cedric_uk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cedric_uk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25934" class="comments-container">
<span id="25935"></span>
<div id="comment-25935" class="comment">
<div id="post-25935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've investigate a bit more. It seems it's a multipolygone, Is this could be the problem? If yes, what the solution of the problem? Should I edit it by creating a simple polygone?</p>
</div>
<div id="comment-25935-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 15:23)</span> <span class="comment-user userinfo">Cedric_uk</span>
</div>
</div>
<span id="25936"></span>
<div id="comment-25936" class="comment">
<div id="post-25936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>not sure the exact issue. might be related to the fact that it's a multipolygon relation: <a href="https://www.openstreetmap.org/browse/relation/2582516">https://www.openstreetmap.org/browse/relation/2582516</a></p>
</div>
<div id="comment-25936-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 15:27)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-25934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25934-form-container" class="comment-form-container">
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

<span id="25937"></span>

<div id="answer-container-25937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25937-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One possibility: the upper way of the multipolygon is a recent edit, so it has the higher (64-bit) IDs. Some tools/software haven't been rewritten to handle these yet (right now, QGIS is the major one), so it could be related to that? More info on this issue at the <a href="https://wiki.openstreetmap.org/wiki/64-bit_Identifiers">64-bit</a> wiki page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '13, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-25937" class="comments-container">
<span id="25938"></span>
<div id="comment-25938" class="comment">
<div id="post-25938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx for your interest!!! I didn't use Qgis for the download but bbbike.org and geofabrik.de. And for them I don't know how they extract the data from OSM. I've just send an email to them to know a bit more about it.</p>
</div>
<div id="comment-25938-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 15:58)</span> <span class="comment-user userinfo">Cedric_uk</span>
</div>
</div>
<span id="25939"></span>
<div id="comment-25939" class="comment">
<div id="post-25939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How are you viewing the shapefiles?</p>
</div>
<div id="comment-25939-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 16:03)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="25940"></span>
<div id="comment-25940" class="comment">
<div id="post-25940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I've got more info. I downloaded through them as "free download" they don't do multipolygones. So I think I got the answer of my question. Thx neuhausr for your help.</p>
</div>
<div id="comment-25940-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 16:10)</span> <span class="comment-user userinfo">Cedric_uk</span>
</div>
</div>
<span id="25942"></span>
<div id="comment-25942" class="comment">
<div id="post-25942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I feel stupid to not have understand what you wanted to say.... I used Qgis and MAPublisher 8 on Adobe Illustrator CS4....</p>
</div>
<div id="comment-25942-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 16:32)</span> <span class="comment-user userinfo">Cedric_uk</span>
</div>
</div>
<span id="25943"></span>
<div id="comment-25943" class="comment not_top_scorer">
<div id="post-25943-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you know/recommend a free software on which I could check the shapefile?</p>
</div>
<div id="comment-25943-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 16:35)</span> <span class="comment-user userinfo">Cedric_uk</span>
</div>
</div>
<span id="25946"></span>
<div id="comment-25946" class="comment">
<div id="post-25946-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FYI, you can also download the data in OSM format in other ways, like via osm.org (Map Layers &gt; Map Data &gt; Retrieve this area from the API), or via XAPI/Overpass (ie - see <a href="http://harrywood.co.uk/maps/uixapi/xapi.html).">http://harrywood.co.uk/maps/uixapi/xapi.html).</a> There are ways to convert OSM to SHP, for example with ogr2ogr <a href="http://www.gdal.org/ogr2ogr.html">http://www.gdal.org/ogr2ogr.html</a> I recently used a command like this: ogr2ogr -where "OGR_GEOMETRY='LineString' -lco SHPT=ARC outfile.shp infile.osm. More options here: <a href="https://wiki.openstreetmap.org/wiki/Shapefile">https://wiki.openstreetmap.org/wiki/Shapefile</a></p>
</div>
<div id="comment-25946-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 16:45)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="25961"></span>
<div id="comment-25961" class="comment not_top_scorer">
<div id="post-25961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thank you very much for your help. BTW I had an answer from Geofabrik.de and they said they don't do multipolygon on the free download. For the 64bits ID's they say there is no problem.</p>
</div>
<div id="comment-25961-info" class="comment-info">
<span class="comment-age">(30 Aug '13, 12:24)</span> <span class="comment-user userinfo">Cedric_uk</span>
</div>
</div>
</div>
<div id="comment-tools-25937" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-25937-form-container" class="comment-form-container">
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

