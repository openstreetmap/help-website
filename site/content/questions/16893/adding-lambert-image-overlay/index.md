+++
type = "question"
title = "Adding Lambert Image Overlay"
description = '''I would like to add an image overlay to OpenStreetMap. Initial image is of 760*760 pixels and it is referred in Lambert Conic Conformal coordinates with a center grid point in 40N, 3W. The isometric latitudes of lambert projection are in 33.5N and 46.5N. To be well overlayed, it is necessary to conv...'''
date = "2012-10-15T08:34:00Z"
lastmod = "2012-10-15T08:58:00Z"
weight = 16893
keywords = [ "lambert", "image", "overlay" ]
aliases = [ "/questions/16893" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding Lambert Image Overlay](/questions/16893/adding-lambert-image-overlay)

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
<span id="post-16893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16893-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to add an image overlay to OpenStreetMap. Initial image is of 760*760 pixels and it is referred in Lambert Conic Conformal coordinates with a center grid point in 40N, 3W. The isometric latitudes of lambert projection are in 33.5N and 46.5N. To be well overlayed, it is necessary to convert Lambert projection to WGS84 and then to Mercator EPSG:900013, right? Do you know a tool or any easy way to do it?</p>
<p>Thank you very much</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lambert" rel="tag" title="see questions tagged &#39;lambert&#39;">lambert</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '12, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/2e35f44e6f48fe28e434998df5bf28a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmsole&#39;s gravatar image" />
<p><span>jmsole</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmsole has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16893" class="comments-container">
&#10;</div>
<div id="comment-tools-16893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16893-form-container" class="comment-form-container">
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

<span id="16894"></span>

<div id="answer-container-16894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16894-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can reproject raster images with the "gdalwarp" command line utility from the GDAL suite of programs (many Linux distributions have that as "gdal-bin" package). You could also use control points instead of mathematics and bring the image into shape with the MapWarper web site (<a href="http://mapwarper.net/).">http://mapwarper.net/).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '12, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16894" class="comments-container">
&#10;</div>
<div id="comment-tools-16894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16894-form-container" class="comment-form-container">
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

