+++
type = "question"
title = "Cambridge Bay and Rankin Inlet zones have errors"
description = '''Hi all, Using timezone-boundary-builder ( https://github.com/evansiroky/timezone-boundary-builder ) which downloads zone files using overpass and builds its own database from the polygons. Cambridge Bay and Rankin Inlet zones have errors as shown below. I had to remove these zones from the timezone-...'''
date = "2019-04-19T17:24:00Z"
lastmod = "2019-04-19T20:40:00Z"
weight = 68853
keywords = [ "timezone", "cambridge_bay", "rankin_inlet", "coordinates", "polygons" ]
aliases = [ "/questions/68853" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cambridge Bay and Rankin Inlet zones have errors](/questions/68853/cambridge-bay-and-rankin-inlet-zones-have-errors)

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
<span id="post-68853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68853-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Using timezone-boundary-builder ( <a href="https://github.com/evansiroky/timezone-boundary-builder">https://github.com/evansiroky/timezone-boundary-builder</a> ) which downloads zone files using overpass and builds its own database from the polygons. Cambridge Bay and Rankin Inlet zones have errors as shown below.</p>
<p>I had to remove these zones from the timezone-boundary-builder boundary and timezone json files to complete the building of the shape files, but then when trying to find the zone using lat/long of either zone, ZoneDetect comes up empty, so no coverage for these zones which may impact my usage.</p>
<p>Is someone able to fix these or do I have to do this myself? How could I fix this myself without going down a rabbit hole (visualizing the actual boundaries, fixing the coordinates and then exporting back out to whatever format is on the server, uploading to the server.. how is all this done?)</p>
<p>Here is the error output for both zones; I removed Cambridge Bay first to be able to continue to see the problem with Rankin Inlet. Many thanks in advance.</p>
<p>getting data for Cambridge Bay-tz; Downloading progress: 14.3% done - 0.0 seconds left downloading from overpass waiting 4 seconds Success, decreasing overpass request gap combining border Invalid geojson received in Overpass Result Overpass query: [out:json][timeout:60];(relation["timezone"="America/Cambridge_Bay"];);out body;&gt;;out meta qt; saved problem file to Cambridge Bay-tz_convert_to_geom_error.json To read more about this error, please visit <a href="https://git.io/vxKQq">https://git.io/vxKQq</a> done error! [ { message: 'the first and last positions in a LinearRing of coordinates must be the same', line: 5 }, { message: 'the first and last positions in a LinearRing of coordinates must be the same', line: 10973 }, { message: 'the first and last positions in a LinearRing of coordinates must be the same', line: 28797 }, { message: 'the first and last positions in a LinearRing of coordinates must be the same', line: 29045 } ]</p>
<hr />
<p>getting data for Rankin Inlet-tz; Downloading progress: 70.2% done - 0.0 seconds left downloading from overpass waiting 4 seconds Success, decreasing overpass request gap combining border Invalid geojson received in Overpass Result Overpass query: [out:json][timeout:60];(relation["timezone"="America/Rankin_Inlet"];);out body;&gt;;out meta qt; saved problem file to Rankin Inlet-tz_convert_to_geom_error.json To read more about this error, please visit <a href="https://git.io/vxKQq">https://git.io/vxKQq</a> done error! [ { message: 'the first and last positions in a LinearRing of coordinates must be the same', line: 4 } ]</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-timezone" rel="tag" title="see questions tagged &#39;timezone&#39;">timezone</span> <span class="post-tag tag-link-cambridge_bay" rel="tag" title="see questions tagged &#39;cambridge_bay&#39;">cambridge_bay</span> <span class="post-tag tag-link-rankin_inlet" rel="tag" title="see questions tagged &#39;rankin_inlet&#39;">rankin_inlet</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '19, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8fb260c6f11edf427f0e01250db11a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="speppercorn&#39;s gravatar image" />
<p><span>speppercorn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="speppercorn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68853" class="comments-container">
&#10;</div>
<div id="comment-tools-68853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68853-form-container" class="comment-form-container">
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

<span id="68856"></span>

<div id="answer-container-68856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can analyse relations such as this using Relation Analyzer. The map view shows where the problem is with Rankin Inlet timezone: <a href="http://ra.osmsurround.org/analyzeMap?relationId=6446189.">http://ra.osmsurround.org/analyzeMap?relationId=6446189.</a> OSM is a wiki, if this data is important to you, then I'd advise learning how to repair it: to most OSM contributors (and I expect editor maintainers) these are rather obscure items which may be easily damaged. Either way references to OSM elements are far more useful for getting help of this sort than output from your workflow tools.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '19, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-68856" class="comments-container">
&#10;</div>
<div id="comment-tools-68856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68856-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

