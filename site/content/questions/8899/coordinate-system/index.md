+++
type = "question"
title = "Coordinate system?"
description = '''Hallo, I have exported a couple of sections of the OSM Map using the export tab and saving as a Mapnik image. I would now like to use these images in ArcGIS. In ArcGIS I have created a point layer showing the map sections corner points (in WSG84). To my surprise the map sections didn&#x27;t correspond wi...'''
date = "2011-11-10T08:22:00Z"
lastmod = "2012-05-14T22:55:00Z"
weight = 8899
keywords = [ "arcgis", "projection", "coordinates" ]
aliases = [ "/questions/8899" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Coordinate system?](/questions/8899/coordinate-system)

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
<span id="post-8899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8899-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo,</p>
<p>I have exported a couple of sections of the OSM Map using the export tab and saving as a Mapnik image. I would now like to use these images in ArcGIS. In ArcGIS I have created a point layer showing the map sections corner points (in WSG84). To my surprise the map sections didn't correspond with my corner points. The map sections have the form of a square, the corner poitns on the other hand a rectangle. In both cases I used the exactly same coordinates. Does anybody have an idea what the solution could be?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '11, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/97da164e9733a5f5549c3f808b1e9c13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariem&#39;s gravatar image" />
<p><span>mariem</span><br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '11, 17:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-8899" class="comments-container">
&#10;</div>
<div id="comment-tools-8899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8899-form-container" class="comment-form-container">
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

<span id="9029"></span>

<div id="answer-container-9029" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9029-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Mapnik image is generated using the Spherical Mercator projection. You have to set your ArcGIS to use that, not WGS84. The projection uses the codes EPSG:3857, sometimes also EPSG:900913. In older ArcGIS systems you might have to use ESRI:102100.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '11, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9029" class="comments-container">
&#10;</div>
<div id="comment-tools-9029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9029-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12734"></span>

<div id="answer-container-12734" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12734-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ESRI should handle conversions on the fly, why does it not reproject the osm data to the projection of the project I had set the layer to convert to?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9f7befbf40ef9e944dd83ba2cef0a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lewis_pusey&#39;s gravatar image" />
<p><span>lewis_pusey</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lewis_pusey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12734" class="comments-container">
&#10;</div>
<div id="comment-tools-12734" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12734-form-container" class="comment-form-container">
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

