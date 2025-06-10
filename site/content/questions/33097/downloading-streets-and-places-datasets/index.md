+++
type = "question"
title = "Downloading Streets and Places datasets"
description = '''Hi there! I thank you all for doing massive work in educating and instructing us. I am a new user of this OSM and a big admirer of GIS. I am trying to mentor myself on GIS and I downloaded QGIS training manual only to find OSM used as a source of streets and places datasets. My question is, how do i...'''
date = "2014-05-12T08:09:00Z"
lastmod = "2014-05-12T11:04:00Z"
weight = 33097
keywords = [ "qgis", "roads" ]
aliases = [ "/questions/33097" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading Streets and Places datasets](/questions/33097/downloading-streets-and-places-datasets)

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
<span id="post-33097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33097-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there! I thank you all for doing massive work in educating and instructing us. I am a new user of this OSM and a big admirer of GIS. I am trying to mentor myself on GIS and I downloaded QGIS training manual only to find OSM used as a source of streets and places datasets. My question is, how do i download datasets of a specified place? Let say I want to download a place like Serengeti National Park in Tanzania.</p>
<p>I thank you in advance for your time and paying attention to my question.</p>
<p>Regards</p>
<p>Godfrey</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '14, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/de1f3767fa9a7599f45bfe284f2e4977?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GodfreyvOyema&#39;s gravatar image" />
<p><span>GodfreyvOyema</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GodfreyvOyema has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '14, 10:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-33097" class="comments-container">
&#10;</div>
<div id="comment-tools-33097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33097-form-container" class="comment-form-container">
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

<span id="33102"></span>

<div id="answer-container-33102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I never tried the tandem of QGIS and OSM before, but since QGIS 2.0 you have a <a href="http://wiki.openstreetmap.org/wiki/QGis">builtin OSM importer</a> that AFAIK allows you to filter for roadnetworks etc.</p>
<p>Other ways to get OSM data is to download <a href="http://wiki.openstreetmap.org/wiki/Planet">OSM extracts</a>, filter it using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> and import it as <a href="http://wiki.openstreetmap.org/wiki/Shapefile">shapefile</a>, geoJSON, ... . For first testing purpose you might be already happy by using the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> for getting small areas with the objects you are interested in. Or you get shapefile for example from Geofabrik.</p>
<p>BUT as you will find out the OSM model isn't designed for a specific purpose (rendering, queries, routing, geocoding, ...) but is an <strong>intermediate format</strong> that is build to allow easy modelling/tagging of all kind of real world features with geolocation.<br />
So you will need to transform the OSM representation of objects into a style that assists you on your workflow.</p>
<p>For your scenario this mean that you might merge OSM ways with same name into one roadnetwork and create an intelligent filter to unite places modelled as node with place=* tag and ones modelled as boundary relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '14, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-33102" class="comments-container">
&#10;</div>
<div id="comment-tools-33102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33102-form-container" class="comment-form-container">
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

