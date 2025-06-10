+++
type = "question"
title = "How can I convert the land-polygons to a raster land mask?"
description = '''How can I use gdal_rasterize to produce a (GeoTiff) raster mask from the polygons found in: http://openstreetmapdata.com/data/land-polygons (WGS84 Shapefile split-polygons)? I have tried variations such as: gdal_rasterize -l land_polygons -init 0 -b 1 -burn 255 -of gtiff -ts 2000 1000 land_polygons....'''
date = "2015-11-13T19:59:00Z"
lastmod = "2015-11-16T17:38:00Z"
weight = 46571
keywords = [ "raster", "polygons", "land-mask" ]
aliases = [ "/questions/46571" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I convert the land-polygons to a raster land mask?](/questions/46571/how-can-i-convert-the-land-polygons-to-a-raster-land-mask)

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
<span id="post-46571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46571-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I use gdal_rasterize to produce a (GeoTiff) raster mask from the polygons found in: <a href="http://openstreetmapdata.com/data/land-polygons">http://openstreetmapdata.com/data/land-polygons</a> (WGS84 Shapefile split-polygons)?</p>
<p>I have tried variations such as:</p>
<pre><code>gdal_rasterize -l land_polygons -init 0 -b 1 -burn 255 -of gtiff -ts 2000 1000 land_polygons.shp land_polygons.tif</code></pre>
<p>... but all I get is a raster filled with 0.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-raster" rel="tag" title="see questions tagged &#39;raster&#39;">raster</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-land-mask" rel="tag" title="see questions tagged &#39;land-mask&#39;">land-mask</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '15, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a08659a77aaa993318279ee48ee2ca67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rosstrafford&#39;s gravatar image" />
<p><span>rosstrafford</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rosstrafford has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46571" class="comments-container">
&#10;</div>
<div id="comment-tools-46571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46571-form-container" class="comment-form-container">
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

<span id="46574"></span>

<div id="answer-container-46574" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46574-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ran this with the simplified_land_polygons shapefile (no need to go super detailed if your output file is just 2k x 1k pixels):</p>
<pre><code>gdal_rasterize -l simplified_land_polygons -burn 255 -of gtiff -ts 2000 1000 simplified_land_polygons.shp out.tiff</code></pre>
<p>and it worked nicely. Note the omission of your "-b 1" which gave an error message for me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46574" class="comments-container">
<span id="46583"></span>
<div id="comment-46583" class="comment">
<div id="post-46583-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Frederik, I'll give that a try shortly. Yes, I did have to get rid of the "-b 1" as well.</p>
<p>This should get me somewhere for now. However, I would like to do a bit better.</p>
<p>It's likely that the "simplified" polygons are considerably lower resolution (only 23 MB) than the ones I was trying to use. In the end, I want very detailed resolution - I will want to carve out tiles that are a few degrees wide, and ultimately want to get down below 100m resolution, so this dataset might not do the trick.</p>
<p>I also see that the simplified polygons are delivered in Mercator rather that WGS84 (lat/lon). I'd like to get as far north (and south) as I can, so the WGS84 sets would be preferable. Anyway, there are 3 other datasets I could try, so I'll cross my fingers.</p>
<p>I'll re-post back here to indicate which datasets work and don't work.</p>
</div>
<div id="comment-46583-info" class="comment-info">
<span class="comment-age">(14 Nov '15, 05:26)</span> <span class="comment-user userinfo">rosstrafford</span>
</div>
</div>
<span id="46597"></span>
<div id="comment-46597" class="comment">
<div id="post-46597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik.</p>
<p>Using the simplified polygons also does NOT work for me.</p>
<p>Maybe I should question my gdal/ogr library. I am using 1.11.1 built from source on SuSE 12.2. What version are you using?</p>
</div>
<div id="comment-46597-info" class="comment-info">
<span class="comment-age">(15 Nov '15, 15:34)</span> <span class="comment-user userinfo">rosstrafford</span>
</div>
</div>
<span id="46598"></span>
<div id="comment-46598" class="comment">
<div id="post-46598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1.10.1 on Ubuntu.</p>
</div>
<div id="comment-46598-info" class="comment-info">
<span class="comment-age">(15 Nov '15, 15:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46621"></span>
<div id="comment-46621" class="comment">
<div id="post-46621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have any other suggestions?</p>
<p>What I am really shooting for is to use it as a mask for DEM topography and bathymetry (to display one or the other in any given pixel). I need to get this big shapefile into 10 degree square tiles, and use these as a mask. Keeping it as vector, may actually be better (to get the resolution I need with raster would be immensely huge for the whole world), but I think that testing "inside vs outside" for each polygon will be seriously costly.</p>
</div>
<div id="comment-46621-info" class="comment-info">
<span class="comment-age">(16 Nov '15, 17:38)</span> <span class="comment-user userinfo">rosstrafford</span>
</div>
</div>
</div>
<div id="comment-tools-46574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46574-form-container" class="comment-form-container">
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

