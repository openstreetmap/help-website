+++
type = "question"
title = "Download &amp; pre-cache images in JOSM"
description = '''If I load a imagery source into JOSM, it&#x27;ll download (and locally cache) all the images for the view I&#x27;m looking at now. However if I want to zoom in, it&#x27;ll have to download (and cache) the image for the new images, which can cause a user visible lag. Is it possible to, given an area in JOSM (e.g. t...'''
date = "2016-04-08T19:49:00Z"
lastmod = "2016-04-09T00:53:00Z"
weight = 49123
keywords = [ "josm", "imagery", "aerial", "aerial_imagery" ]
aliases = [ "/questions/49123" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download & pre-cache images in JOSM](/questions/49123/download-pre-cache-images-in-josm)

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
<span id="post-49123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49123-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I load a imagery source into JOSM, it'll download (and locally cache) all the images for the view I'm looking at now. However if I want to zoom in, it'll have to download (and cache) the image for the new images, which can cause a user visible lag.</p>
<p>Is it possible to, given an area in JOSM (e.g. the current view port), to download and pre-cache all the images for this and N levels of zoom deeper?</p>
<p>This would make it easier to edit an area, since you could download the OSM data for the area, then download the imagery for the area, and be able to pan around and edit without any network lag.</p>
<p><em>Although this would be helpful for Bing images, my current use case is for images from mapwarper and other community hosted, and open licenced, sources.</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-aerial" rel="tag" title="see questions tagged &#39;aerial&#39;">aerial</span> <span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '16, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-49123" class="comments-container">
&#10;</div>
<div id="comment-tools-49123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49123-form-container" class="comment-form-container">
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

<span id="49127"></span>

<div id="answer-container-49127" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49127-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="/questions/48466/how-to-configure-offline-imagery-for-josm">A similar question with some answers</a> and <a href="/questions/48585/significant-offset-between-josm-and-marble-for-mapwarper-imagery">don't miss the extra info in the followup.</a></p>
<p>For Mapwarper specifically, I think for many images that downloading the rectified image from the Export tab and opening it using the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/ImportImagePlugin">JOSM ImportImagePlugin</a> might be an easier solution (Obviously this will work with any service where the whole image is available).</p>
<p>I'm not sure how well JOSM will perform with larger images, but I'd be tempted to try using GDAL to extract the area of interest rather than mucking about with Marble to download tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '16, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '16, 01:01</strong> </span></p>
</div>
</div>
<div id="comments-container-49127" class="comments-container">
&#10;</div>
<div id="comment-tools-49127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49127-form-container" class="comment-form-container">
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

