+++
type = "question"
title = "SHAPE file for Indian Railway Stations"
description = '''Hi, Is there a link to download all Indian railway stations in SHAPE format? They could be either Points or Polygons, I could use them in either geometry?'''
date = "2016-06-03T08:09:00Z"
lastmod = "2016-06-03T12:32:00Z"
weight = 49981
keywords = [ "shapefile", "railway", "india", "railroad", "stations" ]
aliases = [ "/questions/49981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SHAPE file for Indian Railway Stations](/questions/49981/shape-file-for-indian-railway-stations)

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
<span id="post-49981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49981-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Is there a link to download all Indian railway stations in SHAPE format? They could be either Points or Polygons, I could use them in either geometry?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-india" rel="tag" title="see questions tagged &#39;india&#39;">india</span> <span class="post-tag tag-link-railroad" rel="tag" title="see questions tagged &#39;railroad&#39;">railroad</span> <span class="post-tag tag-link-stations" rel="tag" title="see questions tagged &#39;stations&#39;">stations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '16, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2c26e47b03e7178c1021d74ab35137e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="svenky1980&#39;s gravatar image" />
<p><span>svenky1980</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="svenky1980 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49981" class="comments-container">
&#10;</div>
<div id="comment-tools-49981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49981-form-container" class="comment-form-container">
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

<span id="49986"></span>

<div id="answer-container-49986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49986-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest way to do this is to save the data with a Overpass Query (such as this one) and use something like ogr2ogr to convert to a Shape file. (This particular query is small enough to return in Overpass-Turbo meaning that a geojson or KML file can be saved directly).</p>
<p>There are various additional parameters which can be added to the Overpass query which may help, see the documentation.</p>
<p>Alternatives are to download the ready built Shape files from Geofabrik or download a complete extract of india and pull out the stations using osmfilter (again you will need to convert from an OSM format to Shape).</p>
<p>For <em>ad hoc</em> conversions opensource GIS software such as QGIS may be more convenient than ogr2ogr or osm2shp.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '16, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-49986" class="comments-container">
&#10;</div>
<div id="comment-tools-49986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49986-form-container" class="comment-form-container">
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

