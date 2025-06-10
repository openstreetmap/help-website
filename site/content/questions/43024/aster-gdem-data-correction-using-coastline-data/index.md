+++
type = "question"
title = "Aster GDEM data correction using coastline data?"
description = '''(Please excuse my poor English) Hi, I am a newbie for Open Street Map. Currently I&#x27;m doing a 3D map project using Aster 1 arcsecond GDEM data. However I found Aster GDEM data have some errors. Most significant error is that Aster GDEM data do not exclude water area(sea, river, lake) data sufficientl...'''
date = "2015-05-12T08:13:00Z"
lastmod = "2015-05-12T13:18:00Z"
weight = 43024
keywords = [ "gdem", "aster", "coastline", "dem" ]
aliases = [ "/questions/43024" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Aster GDEM data correction using coastline data?](/questions/43024/aster-gdem-data-correction-using-coastline-data)

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
<span id="post-43024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>(Please excuse my poor English)</p>
<p>Hi, I am a newbie for Open Street Map.</p>
<p>Currently I'm doing a 3D map project using Aster 1 arcsecond GDEM data. However I found Aster GDEM data have some errors. Most significant error is that Aster GDEM data do not exclude water area(sea, river, lake) data sufficiently.</p>
<p>To correct the error, I sought a land/water mask, but could not found sufficient one having sufficient resolution. So I want to make a land/water mask using OSM coastline data, having sufficient resolution matching for Aster GDEM. But I don't know how.</p>
<p>Would you please let me know how to get land/water mask using OSM coastline data, and how to include other water area(river, lake) data to the land/water mask? Of course, other ideas for correcting the Aster GDEM error will be welcomed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gdem" rel="tag" title="see questions tagged &#39;gdem&#39;">gdem</span> <span class="post-tag tag-link-aster" rel="tag" title="see questions tagged &#39;aster&#39;">aster</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span> <span class="post-tag tag-link-dem" rel="tag" title="see questions tagged &#39;dem&#39;">dem</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '15, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/73e73f735b43c333f11151785aa7e0cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pdh0710&#39;s gravatar image" />
<p><span>pdh0710</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pdh0710 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '15, 08:19</strong> </span></p>
</div>
</div>
<div id="comments-container-43024" class="comments-container">
&#10;</div>
<div id="comment-tools-43024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43024-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="43026"></span>

<div id="answer-container-43026" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43026-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the OSM-based shape files on <a href="http://www.openstreetmapdata.com/">http://www.openstreetmapdata.com/</a> - but note that using these files to correct your ASTER dataset will likely have license implications for your resulting data, i.e. it will likely be an OSM-derived database which you then have to license under ODbL 1.0.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '15, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-43026" class="comments-container">
&#10;</div>
<div id="comment-tools-43026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43026-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43027"></span>

<div id="answer-container-43027" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43027-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your reply. I found this.</p>
<blockquote>
<p><a href="http://openstreetmapdata.com/data/water-polygons">http://openstreetmapdata.com/data/water-polygons</a></p>
<p>.......</p>
<p>This dataset only contains bodies of water bordered by ways tagged natural=coastline, it does not contain lakes, reservoirs, etc. tagged with natural=water etc.</p>
</blockquote>
<p>Still I don't know below, cause I'm a newbie for OSM. Please let me know more detail.</p>
<ol>
<li>How I can get a shapefile tagged with natural=water from OSM map data. I want the shapefile includes lake and river data.</li>
<li>How I can get a land/water mask file from the shapefile. the mask file is normally black and white image file.</li>
<li>I will open and share the mask file and corrected Aster GDEM files. Is there any license problem?</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '15, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/73e73f735b43c333f11151785aa7e0cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pdh0710&#39;s gravatar image" />
<p><span>pdh0710</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pdh0710 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '15, 10:13</strong> </span></p>
</div>
</div>
<div id="comments-container-43027" class="comments-container">
&#10;</div>
<div id="comment-tools-43027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43027-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43031"></span>

<div id="answer-container-43031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer:the coastline you already found it at openstreetmapdata.com.</p>
<p>For lakes, you need openstreetmap data from planet.openstreetmap.org, then look on the wiki.openstreetmap.org for osmfilter.</p>
<p>The other tools you need are ogr2ogr to make shapefiles, and gdal to process the DEM and with resulting shapes, mainly <a href="http://www.gdal.org/gdal_rasterize.html.">http://www.gdal.org/gdal_rasterize.html.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '15, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-43031" class="comments-container">
&#10;</div>
<div id="comment-tools-43031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43031-form-container" class="comment-form-container">
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

