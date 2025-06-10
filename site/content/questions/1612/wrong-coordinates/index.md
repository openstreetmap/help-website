+++
type = "question"
title = "[closed] Wrong coordinates"
description = '''I have exported a part of the Map from www.openstreetmap.org as .jpg. As I opend it in ArcGIS and defined it in WGS 1984, it didn’t correspond with my other layers. It was too big and it was in the wrong place. My other layers are all defined in Gauss Krüger, but thqat shouldn’t be a problem since A...'''
date = "2010-11-24T08:39:00Z"
lastmod = "2012-05-14T23:00:00Z"
weight = 1612
keywords = [ "arcgis", "corrdinates" ]
aliases = [ "/questions/1612" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Wrong coordinates](/questions/1612/wrong-coordinates)

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
<span id="post-1612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1612-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have exported a part of the Map from <a href="http://www.openstreetmap.org">www.openstreetmap.org</a> as .jpg. As I opend it in ArcGIS and defined it in WGS 1984, it didn’t correspond with my other layers. It was too big and it was in the wrong place. My other layers are all defined in Gauss Krüger, but thqat shouldn’t be a problem since ArcGIS kann show bothe at the same time. What do I have to do that the OpenSteetMap shows at the right coordinates?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-corrdinates" rel="tag" title="see questions tagged &#39;corrdinates&#39;">corrdinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '10, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/97da164e9733a5f5549c3f808b1e9c13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariem&#39;s gravatar image" />
<p><span>mariem</span><br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>15 May '12, 07:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-1612" class="comments-container">
&#10;</div>
<div id="comment-tools-1612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by Frederik Ramm 15 May '12, 07:38

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1613"></span>

<div id="answer-container-1613" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1613-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly any image that you have exported is not in WGS-84 but rather will have been projected to spherical mercator (EPSG-3857, sometimes nicknamed EPSG-900913 as it's the same system used by GOOGLE).</p>
<p>Your main problem however is that JPEG files do not have a system to store the geographical information in maps. And I think only TIFF is the only raster file type have that ability (which you can't export <em>hint to developers</em>).</p>
<p>ArcGIS is therefore making up the geographical information when importing JPEG files, probably from the current view. There is probably some way of changing the layer (scaling, moving, rotating) so that it matches the other layers.</p>
<p>You can use OSM as a <a href="http://www.arcgis.com/home/item.html?id=b834a68d7a484c5fb473d4ba90d35e71">basemap</a> in ArcGis or you can import an osm file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '10, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '10, 09:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1613" class="comments-container">
<span id="1614"></span>
<div id="comment-1614" class="comment">
<div id="post-1614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-1614-info" class="comment-info">
<span class="comment-age">(24 Nov '10, 10:55)</span> <span class="comment-user userinfo">mariem</span>
</div>
</div>
</div>
<div id="comment-tools-1613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1613-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12735"></span>

<div id="answer-container-12735" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12735-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have the same problem with osm converted to shape in QGIS, ir won't re-project to the projection set by the other layers, as it should, at least in ArcGIS.</p>
<p>I wondered if you might know what was going on as I tell it to take the projection of the other layers, maybe QGIS doesn't handle this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 23:00</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9f7befbf40ef9e944dd83ba2cef0a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lewis_pusey&#39;s gravatar image" />
<p><span>lewis_pusey</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lewis_pusey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12735" class="comments-container">
&#10;</div>
<div id="comment-tools-12735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12735-form-container" class="comment-form-container">
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

