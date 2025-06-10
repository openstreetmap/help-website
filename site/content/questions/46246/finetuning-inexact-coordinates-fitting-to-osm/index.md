+++
type = "question"
title = "Finetuning inexact coordinates fitting to OSM"
description = '''Dear All, I scanned an old map and georeferenced it with Qgis (gdal).The result is ok - nearly. When I compare in QMapshack the grids UTM32 - printed grid on the scan and the QSM Grid - they are a little bit different, maybe 50 m in X Y. The geotiff is inexact - I checked it.  My question is if I ca...'''
date = "2015-10-30T16:27:00Z"
lastmod = "2015-10-31T09:18:00Z"
weight = 46246
keywords = [ "utm32", "coordinates", "gdal" ]
aliases = [ "/questions/46246" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Finetuning inexact coordinates fitting to OSM](/questions/46246/finetuning-inexact-coordinates-fitting-to-osm)

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
<span id="post-46246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46246-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear All,</p>
<p>I scanned an old map and georeferenced it with Qgis (gdal).The result is ok - nearly. When I compare in QMapshack the grids UTM32 - printed grid on the scan and the QSM Grid - they are a little bit different, maybe 50 m in X Y. The geotiff is inexact - I checked it. My question is if I can finetune the geotif coordinates so that the are exactly congruent to OSM-Grid ?</p>
<p>Here's the output from gdalinfo:</p>
<pre><code>gdalinfo wanderkarte_MK_54.tif 
Driver: GTiff/GeoTIFF
Files: wanderkarte_MK_54.tif
Size is 8630, 3774
Coordinate System is:
GEOGCS[&quot;WGS 84&quot;,
    DATUM[&quot;WGS_1984&quot;,
        SPHEROID[&quot;WGS 84&quot;,6378137,298.257223563,
            AUTHORITY[&quot;EPSG&quot;,&quot;7030&quot;]],
        AUTHORITY[&quot;EPSG&quot;,&quot;6326&quot;]],
    PRIMEM[&quot;Greenwich&quot;,0],
    UNIT[&quot;degree&quot;,0.0174532925199433],
    AUTHORITY[&quot;EPSG&quot;,&quot;4326&quot;]]
Origin = (7.611058772101766,51.326286037305387)
Pixel Size = (0.000040664445937,-0.000040664445937)
Metadata:
  AREA_OR_POINT=Area
Image Structure Metadata:
  INTERLEAVE=PIXEL
Corner Coordinates:
Upper Left  (   7.6110588,  51.3262860) (  7d36&#39;39.81&quot;E, 51d19&#39;34.63&quot;N)
Lower Left  (   7.6110588,  51.1728184) (  7d36&#39;39.81&quot;E, 51d10&#39;22.15&quot;N)
Upper Right (   7.9619929,  51.3262860) (  7d57&#39;43.17&quot;E, 51d19&#39;34.63&quot;N)
Lower Right (   7.9619929,  51.1728184) (  7d57&#39;43.17&quot;E, 51d10&#39;22.15&quot;N)
Center      (   7.7865259,  51.2495522) (  7d47&#39;11.49&quot;E, 51d14&#39;58.39&quot;N)
Band 1 Block=8630x1 Type=Byte, ColorInterp=Red
  Mask Flags: PER_DATASET ALPHA 
Band 2 Block=8630x1 Type=Byte, ColorInterp=Green
  Mask Flags: PER_DATASET ALPHA 
Band 3 Block=8630x1 Type=Byte, ColorInterp=Blue
  Mask Flags: PER_DATASET ALPHA 
Band 4 Block=8630x1 Type=Byte, ColorInterp=Alpha</code></pre>
<p>Kind regards</p>
<p>Rawbit</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-utm32" rel="tag" title="see questions tagged &#39;utm32&#39;">utm32</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-gdal" rel="tag" title="see questions tagged &#39;gdal&#39;">gdal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '15, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/dafc3603e66d984fc12fb51284858b78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rawbit&#39;s gravatar image" />
<p><span>Rawbit</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rawbit has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '15, 22:50</strong> </span></p>
</div>
</div>
<div id="comments-container-46246" class="comments-container">
<span id="46248"></span>
<div id="comment-46248" class="comment">
<div id="post-46248-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please explain what the "QSM Grid" and the "OSM-Grid" are.</p>
</div>
<div id="comment-46248-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 18:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46252"></span>
<div id="comment-46252" class="comment">
<div id="post-46252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I am referring to the grid for UMT which I can choose for an OSM map. In a second layer I use my scanned map which has a UMT grid as well. But the grid of my scanned map is not congruent and displaced a little bit.</p>
<p>Thank's a lot for your answer !</p>
<p>Kind regards</p>
<p>Rawbit</p>
</div>
<div id="comment-46252-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 22:38)</span> <span class="comment-user userinfo">Rawbit</span>
</div>
</div>
<span id="46254"></span>
<div id="comment-46254" class="comment">
<div id="post-46254-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And what is UMT?</p>
</div>
<div id="comment-46254-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 22:41)</span> <span class="comment-user userinfo">pnorman</span>
</div>
</div>
<span id="46255"></span>
<div id="comment-46255" class="comment">
<div id="post-46255-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi,</p>
<p>oh sorry I mean UTM not UMT ! Universal Transverse Mercator</p>
<p>Kind regards</p>
<p>Rawbit</p>
</div>
<div id="comment-46255-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 22:48)</span> <span class="comment-user userinfo">Rawbit</span>
</div>
</div>
<span id="46256"></span>
<div id="comment-46256" class="comment not_top_scorer">
<div id="post-46256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What tool/website/program are you using to display the OSM map with an UTM grid?</p>
</div>
<div id="comment-46256-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 22:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46257"></span>
<div id="comment-46257" class="comment">
<div id="post-46257-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I use Qmapshack with a .vrt file which is related to the mentioned raster geotiff.</p>
</div>
<div id="comment-46257-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 22:51)</span> <span class="comment-user userinfo">Rawbit</span>
</div>
</div>
</div>
<div id="comment-tools-46246" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46246-form-container" class="comment-form-container">
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

<span id="46260"></span>

<div id="answer-container-46260" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46260-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So if I understand you correctly, the problem is simply that the georeferencing didn't work as well as you would have expected. (This is not an OpenStreetMap specific question really and should have been asked in a more general GIS forum.) This is normal; the quality of the result depends on the quality of your scan, which algorithm you choose, how many GCPs you set, and how precise you are in setting them.</p>
<p>If you believe that simply shifting the GeoTIFF will help, then the easiest option is to use <a href="http://www.gdal.org/gdal_edit.html">gdal_edit.py</a> to override the geographic bounds of the image.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '15, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46260" class="comments-container">
<span id="46267"></span>
<div id="comment-46267" class="comment">
<div id="post-46267-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi,</p>
<p>thank you so much, gdal_edit is exactly what I'm looking for ! I used gdal_edit.py -a_ullr 7.610300 51.326280 7.961292 51.172818 testmod.tif</p>
<p>Kind regards</p>
<p>Rawbit</p>
</div>
<div id="comment-46267-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 09:18)</span> <span class="comment-user userinfo">Rawbit</span>
</div>
</div>
</div>
<div id="comment-tools-46260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46260-form-container" class="comment-form-container">
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

