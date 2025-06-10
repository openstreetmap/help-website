+++
type = "question"
title = "How to export UTM Coordinates into map.osm file instead lat/long?"
description = '''Hello, I want to export the UTM coordinates into map.osm instead of lat/long coordinates from Open street map. Is there any way I can do that? I can&#x27;t find anywhere option to change the lat/long coordinates into UTM coordinates. https://www.openstreetmap.org/export#map=17/39.22130/-77.27298 Work: I ...'''
date = "2022-05-31T22:22:00Z"
lastmod = "2022-06-01T10:57:00Z"
weight = 84643
keywords = [ "osm", "utm" ]
aliases = [ "/questions/84643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to export UTM Coordinates into map.osm file instead lat/long?](/questions/84643/how-to-export-utm-coordinates-into-maposm-file-instead-latlong)

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
<span id="post-84643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84643-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to export the UTM coordinates into map.osm instead of lat/long coordinates from Open street map. Is there any way I can do that? I can't find anywhere option to change the lat/long coordinates into UTM coordinates.</p>
<p><a href="https://www.openstreetmap.org/export#map=17/39.22130/-77.27298">https://www.openstreetmap.org/export#map=17/39.22130/-77.27298</a></p>
<p>Work: I require my road networks from osm file in UTM coordinates. So, I it can be converted into opendrive(.xodr) format later and I can view those map in carmaker simulation in UTM coordinates.</p>
<p>Can anyone please specify any other alternatives, if we can't export UTM coordinates from osm into map.osm file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-utm" rel="tag" title="see questions tagged &#39;utm&#39;">utm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '22, 22:22</strong></p>
<img src="https://secure.gravatar.com/avatar/84886a0ce5366c29f1ba5d60760c79d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nagarjun&#39;s gravatar image" />
<p><span>Nagarjun</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nagarjun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84643" class="comments-container">
&#10;</div>
<div id="comment-tools-84643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84643-form-container" class="comment-form-container">
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

<span id="84649"></span>

<div id="answer-container-84649" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are no tools to transform the coordinates in an OSM file because the OSM XML file format only supports lat/lon coordinates. There isn't any software that would process an OSM file with coordinates in a different coordinate system.</p>
<p>If there is already a conversion program that converts OSM data to the XODR format then it would make sense to modify that program - potentially using the "proj4" library to do the coordinate transformation.</p>
<p>Another potential avenue is using the osm2pgsql software to load the data into a PostGIS database. osm2pgsql can transform OSM data into a number of projections on import (using the <code>-E</code> commandline option). Then you would have to find a way to generate XODR data from the PostGIS tables (or perhaps export the PostGIS tables to Shape Files first with pgsql2shp and take it from there).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '22, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84649" class="comments-container">
&#10;</div>
<div id="comment-tools-84649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84649-form-container" class="comment-form-container">
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

