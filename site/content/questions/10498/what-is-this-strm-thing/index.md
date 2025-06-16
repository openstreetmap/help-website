+++
type = "question"
title = "What is this STRM thing?"
description = '''I keep seeing references to SRTM, such as in the Elevation Maps question. What is a good summary of what is SRTM, what are the alternatives and how do I start with using it?'''
date = "2012-02-08T17:53:00Z"
lastmod = "2012-02-09T00:42:00Z"
weight = 10498
keywords = [ "elevation", "srtm" ]
aliases = [ "/questions/10498" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is this STRM thing?](/questions/10498/what-is-this-strm-thing)

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
<span id="post-10498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10498-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-10498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I keep seeing references to SRTM, such as in the <a href="/questions/3069/elevation-maps">Elevation Maps question</a>. What is a good summary of what is SRTM, what are the alternatives and how do I start with using it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-srtm" rel="tag" title="see questions tagged &#39;srtm&#39;">srtm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '12, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-10498" class="comments-container">
&#10;</div>
<div id="comment-tools-10498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10498-form-container" class="comment-form-container">
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

<span id="10499"></span>

<div id="answer-container-10499" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10499-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-10499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Richard Weait has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://www2.jpl.nasa.gov/srtm/"><strong>S</strong>huttle <strong>R</strong>adar <strong>T</strong>opography <strong>M</strong>ission</a> was a mission that flew in February 2000 on board the space shuttle Endeavour. The result of this mission is a digital elevation map that covers from 56° S to 60° N in 30m accuracy. All this data is avalable on a <a href="http://dds.cr.usgs.gov/srtm/">USGS server</a> in PD.</p>
<p>The licence is fully compatible with any other licence including CC-BY-SA and ODbL and it is possible to use SRTM data and OSM data together. However you should <strong>not import SRTM to OSM</strong>. OSM is not a place to save raster data. SRTM is often used to make <a href="https://wiki.openstreetmap.org/wiki/Contours">contours</a> or <a href="https://wiki.openstreetmap.org/wiki/Relief_maps">reliefs</a> to maps, altitude profiles or to help in routing.</p>
<p>More information about the data format and tools to work with it can be found at the <a href="https://wiki.openstreetmap.org/wiki/SRTM">wiki</a></p>
<p>Other options for DEM data are <a href="http://www.ersdac.or.jp/GDEM/E/1.html">ASTER</a> or <a href="http://www.viewfinderpanoramas.org">www.viewfinderpanoramas.org</a>.</p>
<p>ASTER have more coverage then SRTM but have a "research" licence that is not compatible with a comercial licence like OSM have. You are however allowed to use it in research or in humanitarian aid if you seperate the datasets, or if you claim necessity.</p>
<p><a href="http://www.viewfinderpanoramas.org">www.viewfinderpanoramas.org</a> have coverage in the areas where SRTM does not have good enough data. It claims to be PD, however it is based on many data sources including russian maps with unknown copyright status. Care should be taken when using theese maps as you could get sued if someone with a legitimate claim to theese maps wishes to do so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '12, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-10499" class="comments-container">
&#10;</div>
<div id="comment-tools-10499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10499-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10501"></span>

<div id="answer-container-10501" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10501-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some other sources of elevation data for specific countries, available under a free licence, which may be more useful than SRTM. This includes:</p>
<ul>
<li><p>Great Britain - <a href="http://www.ordnancesurvey.co.uk/oswebsite/products/land-form-panorama/">OS Landform Panorama</a>. 50m resolution. This is available under the OS OpenData Licence, which just requires attribution, so can be used with OSM data.</p></li>
<li><p>United States - <a href="http://ned.usgs.gov/Ned/">USGS National Elevation Dataset (NED)</a>. Mostly 10m resolution, public domain licence.</p></li>
<li><p>Canada - <a href="http://www.geobase.ca/geobase/en/data/cded/">GeoBase Canadian Digital Elevation Data</a>. Under the GeoBase Unrestricted Use Licence Agreement</p></li>
</ul>
<p>This data is provided in a variety of formats, so would need to be converted into something suitable for using with OSM data. There might be some tutorials for how to do this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '12, 00:42</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-10501" class="comments-container">
&#10;</div>
<div id="comment-tools-10501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10501-form-container" class="comment-form-container">
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

