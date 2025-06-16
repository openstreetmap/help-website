+++
type = "question"
title = "Strange size of svg files downloaded at different scales"
description = '''Hi, I&#x27;ve got a question when downloading svg files from openstreetmap. I was trying to download a map of an area in Marseille. The svg file I got was around 40MB when I set the scale at 1:20,000. But when I tried to download a map of a smaller scale, say 1:1,000,000, of the same area, I got an svg f...'''
date = "2013-03-01T09:12:00Z"
lastmod = "2013-03-04T09:10:00Z"
weight = 20409
keywords = [ "svg", "size" ]
aliases = [ "/questions/20409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange size of svg files downloaded at different scales](/questions/20409/strange-size-of-svg-files-downloaded-at-different-scales)

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
<span id="post-20409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20409-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've got a question when downloading svg files from openstreetmap. I was trying to download a map of an area in Marseille. The svg file I got was around 40MB when I set the scale at 1:20,000. But when I tried to download a map of a smaller scale, say 1:1,000,000, of the same area, I got an svg file of 120MB. I think that maps scaled smaller are more generalised, and the file size should be smaller as a result. Does anyone know why the file size actually increases when the scale is lowered? Any help is much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '13, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/9c5f128690365d629f9996c7c9c5109b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weeburn&#39;s gravatar image" />
<p><span>weeburn</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weeburn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20409" class="comments-container">
&#10;</div>
<div id="comment-tools-20409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20409-form-container" class="comment-form-container">
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

<span id="20411"></span>

<div id="answer-container-20411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20411-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The rendering engine behind the SVG export doesn't generalize or simplify geometries. It will drop some features - e.g. on a small scale map you won't see residential roads - but those features that you do see are drawn in full detail (even if that is not visible). Hence the large file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '13, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20411" class="comments-container">
<span id="20420"></span>
<div id="comment-20420" class="comment">
<div id="post-20420-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>AFAIK the text in OSM's SVG exports is converted to vector geometry, I think this is probably the biggest contributing factor in the size. If you need more compact SVGs, you can use <a href="http://maperitive.net/docs/Commands/ExportSvg.html">Maperitive's export function</a>.</p>
</div>
<div id="comment-20420-info" class="comment-info">
<span class="comment-age">(01 Mar '13, 12:31)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
<span id="20423"></span>
<div id="comment-20423" class="comment">
<div id="post-20423-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... or have a look at <a href="https://wiki.openstreetmap.org/wiki/SVG">https://wiki.openstreetmap.org/wiki/SVG</a> in general</p>
</div>
<div id="comment-20423-info" class="comment-info">
<span class="comment-age">(01 Mar '13, 18:58)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="20475"></span>
<div id="comment-20475" class="comment">
<div id="post-20475-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you all... But I am still confused why the size of the svg file downloaded under a smaller scales is larger, given a same area. At least, the sizes of svg files downloaded from different scales should be almost the same. For a same polygon, I got a svg file of 120MB for a map scaling at 1:500,000 but got a file of about 30MB for a map of the same polygon scaling at 1:50,000......</p>
</div>
<div id="comment-20475-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 09:10)</span> <span class="comment-user userinfo">weeburn</span>
</div>
</div>
</div>
<div id="comment-tools-20411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20411-form-container" class="comment-form-container">
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

