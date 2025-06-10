+++
type = "question"
title = "Missing buildings when comparing OSM.org to ArcGIS Pro OSM basemap"
description = '''Hi there, I&#x27;ve exported data from OSM.org (using Geofabrik) and extracted the building data using QGIS to create a polygon shapefile, but when I opened the shapefile in ArcGIS Pro I noticed that, for the same area, buildings are missing from the downloaded data, that are present in the OSM basemap i...'''
date = "2022-07-22T14:58:00Z"
lastmod = "2022-07-25T19:49:00Z"
weight = 85190
keywords = [ "buildings", "data", "exported", "missing" ]
aliases = [ "/questions/85190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing buildings when comparing OSM.org to ArcGIS Pro OSM basemap](/questions/85190/missing-buildings-when-comparing-osmorg-to-arcgis-pro-osm-basemap)

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
<span id="post-85190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85190-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I've exported data from OSM.org (using Geofabrik) and extracted the building data using QGIS to create a polygon shapefile, but when I opened the shapefile in ArcGIS Pro I noticed that, for the same area, buildings are missing from the downloaded data, that are present in the OSM basemap in ArcGIS Pro, and then I realized that those buildings are missing from the OSM.org map.</p>
<p>Does anyone know what's going on here? why would the OSM basemap in ArcGIS Pro have more buildings than the OSM.org map? and how can I get my hands on all of the buildings I'm seeing in the OSM basemap in ArcGIS Pro?</p>
<p><a href="https://photos.app.goo.gl/AdanyvadGh6yG9k77">ArcGIS Pro OSM basemap</a></p>
<p><a href="https://photos.app.goo.gl/znY4ZgYR9pz1dTuH7">OSM map</a></p>
<p>Thanks,</p>
<p>Tim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-exported" rel="tag" title="see questions tagged &#39;exported&#39;">exported</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '22, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/4695757c57cbe972f7baa50dd6c6b819?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Chevrier&#39;s gravatar image" />
<p><span>Tim Chevrier</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Chevrier has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '22, 16:59</strong> </span></p>
</div>
</div>
<div id="comments-container-85190" class="comments-container">
<span id="85191"></span>
<div id="comment-85191" class="comment">
<div id="post-85191-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you link to a view of the area on osm.org maybe?</p>
</div>
<div id="comment-85191-info" class="comment-info">
<span class="comment-age">(22 Jul '22, 15:03)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="85192"></span>
<div id="comment-85192" class="comment">
<div id="post-85192-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You've tried to link to images stored on your computer. You'll need to upload them somewhere online and then point to that location.</p>
</div>
<div id="comment-85192-info" class="comment-info">
<span class="comment-age">(22 Jul '22, 16:49)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="85193"></span>
<div id="comment-85193" class="comment">
<div id="post-85193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, thanks guys! I'll try with links.</p>
</div>
<div id="comment-85193-info" class="comment-info">
<span class="comment-age">(22 Jul '22, 16:54)</span> <span class="comment-user userinfo">Tim Chevrier</span>
</div>
</div>
<span id="85195"></span>
<div id="comment-85195" class="comment">
<div id="post-85195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was thinking more about <a href="https://www.openstreetmap.org/#map=19/45.56793/-73.64229">https://www.openstreetmap.org/#map=19/45.56793/-73.64229</a> so we know where it is, but found it now. My theory is they have been deleted at some point and ArcGIS Pro hasn't updated their data yet, but not sure how to check.</p>
</div>
<div id="comment-85195-info" class="comment-info">
<span class="comment-age">(22 Jul '22, 17:34)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="85196"></span>
<div id="comment-85196" class="comment not_top_scorer">
<div id="post-85196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Ed, sorry for the misunderstanding. I appreciate you looking into this, and finding (and adding) the link to the location in OSM. I'm not sure about your theory. Complete neighborhoods are missing (not only a few buildings).What would be the benefit for OSM to remove all this data? Here are some images of the neighborhood just north of the first images (brown buildings = OSM basemap, orange buildings = downloaded OSM data):<br />
<a href="https://photos.app.goo.gl/Zo3R9K9fKXUAs3Bp7">ArcGIS Pro OSM basemap</a><br />
<a href="https://photos.app.goo.gl/aV8YgaRoCX3pFN8cA">ArcGIS Pro Satellite basemap</a><br />
<a href="https://photos.app.goo.gl/WKMnXDqgnrLReVqcA">OSM map</a></p>
</div>
<div id="comment-85196-info" class="comment-info">
<span class="comment-age">(22 Jul '22, 18:26)</span> <span class="comment-user userinfo">Tim Chevrier</span>
</div>
</div>
<span id="85197"></span>
<div id="comment-85197" class="comment not_top_scorer">
<div id="post-85197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By comparing the ArcGIS Pro OSM map to the Standard rendering on osm.org, you can see a number of slight differences in the style. This leads me to believe that ArcGIS is rendering their own OSM-style map, and they could be incorporating non-OSM building data when they do so. The only way to know for sure would be to contact ArcGIS and ask if that's what they're doing.</p>
</div>
<div id="comment-85197-info" class="comment-info">
<span class="comment-age">(23 Jul '22, 00:20)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="85200"></span>
<div id="comment-85200" class="comment">
<div id="post-85200-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's what I thought as well - attribution when choosing OpenStreetMap basemap in Map Viewer Classic hints at that:</p>
<blockquote>
<p>Map data © OpenStreetMap contributors, Microsoft, Facebook, Inc. [...]</p>
</blockquote>
<p><a href="https://www.arcgis.com/home/webmap/viewer.html">https://www.arcgis.com/home/webmap/viewer.html</a></p>
<p>And at least this vector layer description confirms:</p>
<blockquote>
<p>Esri created this vector tile basemap from the Daylight map distribution of OSM data, which is supported by Facebook and supplemented with additional data from Microsoft.</p>
</blockquote>
<p><a href="https://www.arcgis.com/home/item.html?id=3e1a00aeae81496587988075fe529f71">https://www.arcgis.com/home/item.html?id=3e1a00aeae81496587988075fe529f71</a></p>
</div>
<div id="comment-85200-info" class="comment-info">
<span class="comment-age">(23 Jul '22, 08:56)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-85190" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-85190-form-container" class="comment-form-container">
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

<span id="85199"></span>

<div id="answer-container-85199" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85199-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It might be that Esri is including the buildings data produced by AI at Microsoft (see <a href="https://www.microsoft.com/en-us/maps/building-footprints">https://www.microsoft.com/en-us/maps/building-footprints</a> ) in combination with Esris communitymaps. See <a href="https://daylightmap.org/buildings.html">https://daylightmap.org/buildings.html</a> about thier collaboration.</p>
<p>Check the attribution on the ArcGIS Pro OSM basemap, does it include an attribution to Microsofts building footprints? (Ah, see the comment by Ikonor, they do attribute Microsoft.)</p>
<p>Microsofts data about buildings in Canada can be found here: <a href="https://github.com/Microsoft/CanadianBuildingFootprints">https://github.com/Microsoft/CanadianBuildingFootprints</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '22, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '22, 08:57</strong> </span></p>
</div>
</div>
<div id="comments-container-85199" class="comments-container">
<span id="85217"></span>
<div id="comment-85217" class="comment">
<div id="post-85217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you everyone! I was blindly assuming that the OSM basemap was OSM-only data without looking at the service layer credits. I was able to download and extract the building polygons from the github link (and using the JSON to Features tool) in ArcGIS Pro.</p>
</div>
<div id="comment-85217-info" class="comment-info">
<span class="comment-age">(25 Jul '22, 19:49)</span> <span class="comment-user userinfo">Tim Chevrier</span>
</div>
</div>
</div>
<div id="comment-tools-85199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85199-form-container" class="comment-form-container">
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

