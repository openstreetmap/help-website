+++
type = "question"
title = "How to clip / cut / filter / extract bounding box / radius around given point of gpx file WITHOUT altering the gpx file content otherwise?"
description = '''I want to extract and save an area around a given lat/lon of a gpx file and remove all the remaining points. I tried  gpsbabel -i gpx -f favorites.gpx -x radius,distance=500K,lat=64.9830,lon=-18.1074 -o gpx -F output.gpx  When I use gpsbabel for that, gpsbabel rewrites the whole file, changing the f...'''
date = "2023-08-14T19:09:00Z"
lastmod = "2023-08-15T07:26:00Z"
weight = 87676
keywords = [ "filter", "gpsbabel", "gpx", "polygon", "clip" ]
aliases = [ "/questions/87676" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to clip / cut / filter / extract bounding box / radius around given point of gpx file WITHOUT altering the gpx file content otherwise?](/questions/87676/how-to-clip-cut-filter-extract-bounding-box-radius-around-given-point-of-gpx-file-without-altering-the-gpx-file-content-otherwise)

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
<span id="post-87676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87676-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to extract and save an area around a given lat/lon of a gpx file and remove all the remaining points.</p>
<p>I tried</p>
<pre><code>gpsbabel -i gpx -f favorites.gpx -x radius,distance=500K,lat=64.9830,lon=-18.1074 -o gpx -F output.gpx</code></pre>
<p>When I use gpsbabel for that, gpsbabel rewrites the whole file, changing the format, inventing new tags etc. Is there any tool for just extracting, leaving the file untouched otherwise?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-gpsbabel" rel="tag" title="see questions tagged &#39;gpsbabel&#39;">gpsbabel</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-clip" rel="tag" title="see questions tagged &#39;clip&#39;">clip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '23, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-87676" class="comments-container">
&#10;</div>
<div id="comment-tools-87676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87676-form-container" class="comment-form-container">
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

<span id="87679"></span>

<div id="answer-container-87679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, You can GPSPrune does a lot of gpx manipulation, it might be able to suit your requirement. I use it to cut unwanted sections from gpx tracks. It's here:- <a href="https://activityworkshop.net/software/gpsprune/index.html">https://activityworkshop.net/software/gpsprune/index.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '23, 07:26</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-87679" class="comments-container">
&#10;</div>
<div id="comment-tools-87679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87679-form-container" class="comment-form-container">
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

