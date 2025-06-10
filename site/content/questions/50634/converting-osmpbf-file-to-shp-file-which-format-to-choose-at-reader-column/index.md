+++
type = "question"
title = "Converting .osm.pbf file to .shp file - which format to choose at reader column?"
description = '''Hi, I am trying to convert a .osm.pbf file into .shp file so that it could opened in ArcGIS 10.1 for network analysis. I am following the steps as stated in openstreetmap wiki: http://wiki.openstreetmap.org/wiki/User:Bgirardot/How_To_Convert_osm_.pbf_files_to_Esri_Shapefiles I am at the second dot: ...'''
date = "2016-07-05T13:09:00Z"
lastmod = "2019-04-04T10:25:00Z"
weight = 50634
keywords = [ "openstreetmap", "shp", "pbf", "osm", "arcgis" ]
aliases = [ "/questions/50634" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Converting .osm.pbf file to .shp file - which format to choose at reader column?](/questions/50634/converting-osmpbf-file-to-shp-file-which-format-to-choose-at-reader-column)

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
<span id="post-50634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50634-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to convert a .osm.pbf file into .shp file so that it could opened in ArcGIS 10.1 for network analysis.</p>
<p>I am following the steps as stated in openstreetmap wiki: <a href="http://wiki.openstreetmap.org/wiki/User:Bgirardot/How_To_Convert_osm_.pbf_files_to_Esri_Shapefiles">http://wiki.openstreetmap.org/wiki/User:Bgirardot/How_To_Convert_osm_.pbf_files_to_Esri_Shapefiles</a></p>
<p>I am at the second dot: GDAL. I tried to put my file into the reader column of FME_Quick Translator (I was directed to here after downloaded GDAL 1.10), however there is no .osm.pbf format that I can choose. Do you have any idea which I should I put instead? Or some of my actions have gone wrong?</p>
<p>If I were to leave it blank ( letting the translator to read it automatically), then putting Esri Shapefile in the writer column and run it, error occurred: Value not specified for kDLG_ProjParmA1. Anyone has any idea what might be the reason?</p>
<p>Your help will be truly appreciated, thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-shp" rel="tag" title="see questions tagged &#39;shp&#39;">shp</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '16, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/8a52a5e439b0b8b57697355510ddf7f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rachel%20Hoo&#39;s gravatar image" />
<p><span>Rachel Hoo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rachel Hoo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50634" class="comments-container">
<span id="50635"></span>
<div id="comment-50635" class="comment">
<div id="post-50635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why are you trying to use FME Quick Tranlator? The instructions you link to are for GDAL, more specifically the command line utility ogr2ogr. Did you install that program? Can you run it from the command line as instructred?</p>
</div>
<div id="comment-50635-info" class="comment-info">
<span class="comment-age">(05 Jul '16, 15:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50634-form-container" class="comment-form-container">
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

<span id="68636"></span>

<div id="answer-container-68636" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68636-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We can use <a href="https://www.gdal.org/ogr2ogr.html"><code>ogr2ogr</code></a> to convert .osm.pbf to .shp file</p>
<p><code>ogr2ogr -f "ESRI Shapefile" -skip CGK.osm.shp CGK.osm.pbf</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '19, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/8d2ceff9c4f4168b7c08315273d27117?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="howtobeahacker&#39;s gravatar image" />
<p><span>howtobeahacker</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="howtobeahacker has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '19, 10:25</strong> </span></p>
</div>
</div>
<div id="comments-container-68636" class="comments-container">
&#10;</div>
<div id="comment-tools-68636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68636-form-container" class="comment-form-container">
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

