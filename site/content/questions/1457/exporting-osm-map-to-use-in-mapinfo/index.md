+++
type = "question"
title = "Exporting OSM map to use in MapInfo"
description = '''Please let me know how I can export osm format maps to get them in SHP (ESRI), XLM or GML format? Do you have any converter which I can use? I used to work with maps with MapInfo and would like to keep it as a tool. Can anybody help?'''
date = "2010-11-05T08:56:00Z"
lastmod = "2012-09-19T20:14:00Z"
weight = 1457
keywords = [ "conversion" ]
aliases = [ "/questions/1457" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting OSM map to use in MapInfo](/questions/1457/exporting-osm-map-to-use-in-mapinfo)

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
<span id="post-1457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1457-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please let me know how I can export osm format maps to get them in SHP (ESRI), XLM or GML format? Do you have any converter which I can use? I used to work with maps with MapInfo and would like to keep it as a tool. Can anybody help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '10, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/dd6287312105b16537c142fb34e6af75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="korotie&#39;s gravatar image" />
<p><span>korotie</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="korotie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1457" class="comments-container">
&#10;</div>
<div id="comment-tools-1457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1457-form-container" class="comment-form-container">
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

<span id="1461"></span>

<div id="answer-container-1461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1461-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download ready-made SHP-format maps from <a href="http://download.geofabrik.de/osm/">Geofabrik</a> or <a href="http://downloads.cloudmade.com/">Cloudmade</a>.</p>
<p>I believe most people creating shapefiles (including the download services listed above) are doing so by putting OSM data into a PostGIS database, and then using the built in psql2shp function.</p>
<p>There are a few command-line tools to do a more direct conversion from osm to shapefiles. In fact it looks like there are two different tools called '<em>osm2shp</em>' under development (<a href="http://trac.openstreetmap.org/browser/applications/utils/export/osm2shp">one by Frederick</a> of geofabrik, <a href="http://code.google.com/p/osm2shp/">one by someone else</a>), and a ruby library called '<a href="http://osmlib.rubyforge.org/">OSMLib</a>'.</p>
<p>All the alternatives are listed on the <a href="http://wiki.openstreetmap.org/wiki/Shapefiles">Shapefiles</a> wiki page.</p>
<p>...and aside from shapefiles, you can actually convert or otherwise use OSM data more directly with MapInfo. See the <a href="http://wiki.openstreetmap.org/wiki/MapInfo">MapInfo</a> wiki page (although that information could do with some tidying up by a MapInfo expert)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '10, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '10, 12:51</strong> </span></p>
</div>
</div>
<div id="comments-container-1461" class="comments-container">
&#10;</div>
<div id="comment-tools-1461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16261"></span>

<div id="answer-container-16261" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16261-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also save as Raster from OSM - for example JPEG - and then create your own .TAB file for use with this Raster. The .TAB specifies rference points for conversion (Lon,Lat) -&gt; (pixel). Top Left is always pixel (0,0). Subtract -1 from the pixel count (since the numbering starts from pixel '0').</p>
<p>Example .TAB file below for Raster 2223 Wide by 1733 high:</p>
<p>!table !version 300 !charset WindowsLatin1</p>
<p>Definition Table File "MyRaster.jpg" Type "RASTER" (-87.407,39.076) (0,0) Label "TopLeft", (-86.708,39.076) (2222,0) Label "TopRight", (-87.407,38.652) (0,1732) Label "BottomLeft", (-86.708,38.652) (2222,1732) Label "BottomRight" CoordSys Earth Projection 1, 104 Units "degree" ReadOnly</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '12, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/89997183f2c7e6a4ec23da0e081141cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NeilS&#39;s gravatar image" />
<p><span>NeilS</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NeilS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16261" class="comments-container">
&#10;</div>
<div id="comment-tools-16261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16261-form-container" class="comment-form-container">
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

