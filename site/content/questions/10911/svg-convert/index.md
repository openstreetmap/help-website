+++
type = "question"
title = "svg convert"
description = '''how can I get the RAW uncompressed image format from a SVG map ? (RAW is uncompressed and unprocessed image data. once I saved the SVG as bitmap it would be already a compressed format and it is almost impossible to go back to RAW format that does not have any headers at all, just pure data.)'''
date = "2012-03-01T18:23:00Z"
lastmod = "2012-03-01T22:11:00Z"
weight = 10911
keywords = [ "svg" ]
aliases = [ "/questions/10911" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [svg convert](/questions/10911/svg-convert)

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
<span id="post-10911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10911-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how can I get the RAW uncompressed image format from a SVG map ?</p>
<p>(RAW is uncompressed and unprocessed image data. once I saved the SVG as bitmap it would be already a compressed format and it is almost impossible to go back to RAW format that does not have any headers at all, just pure data.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '12, 18:23</strong></p>
<img src="https://secure.gravatar.com/avatar/00bbccef092919170c720cae49be2403?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NullPointer&#39;s gravatar image" />
<p><span>NullPointer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NullPointer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '12, 19:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-10911" class="comments-container">
&#10;</div>
<div id="comment-tools-10911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10911-form-container" class="comment-form-container">
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

<span id="10913"></span>

<div id="answer-container-10913" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10913-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SVG is a vector graphics format but raster data can be embedded in SVG. If you export an SVG map with Mapnik, you will usually end up with exactl that - a vector map with some embedded raster icons.</p>
<p>You can convert that to PDF or a high-resoultion raster with tools like rsvg, Inkscape, Batik or others. The embedded raster bitmaps will always remain low-resolution unless you create your own rendering style that either uses high-resolution raster icons or vector icons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '12, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10913" class="comments-container">
<span id="10916"></span>
<div id="comment-10916" class="comment">
<div id="post-10916-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>ImageMagick is also a candidate (open source, license Apache 2.0)</p>
</div>
<div id="comment-10916-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 18:50)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="10918"></span>
<div id="comment-10918" class="comment">
<div id="post-10918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not care about quality too much, but Inkscape for example cannot Save As in the RAW format. Is any of the other tools capable of this?</p>
</div>
<div id="comment-10918-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 19:20)</span> <span class="comment-user userinfo">NullPointer</span>
</div>
</div>
<span id="10922"></span>
<div id="comment-10922" class="comment">
<div id="post-10922-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't see why anybody would want that. RAW files contain stuff like metadata about the camera sensor and so on, things that clearly do not exist when you make something from SVG. If you save as PNG from Inkscape then this uses a lossless compression. ImageMagick could then be used to convert PNG to a raw format, or you could try to convert SVG-&gt;RAW directly with ImageMagick. But you won't gain anything from that.</p>
</div>
<div id="comment-10922-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 19:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="10929"></span>
<div id="comment-10929" class="comment">
<div id="post-10929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well if I want to process the image in a programming language I need it in RAW format. I tried this in ImageMagick and I got this message:</p>
<p>$ convert map.svg map.raw convert: unrecognized color <code>7777777' @ warning/color.c/QueryMagickColorCompliance/2603. convert: unable to open image</code>#7777777': No such file or directory @ error/blob.c/OpenBlob/2614. convert: no decode delegate for this image format <code>#7777777' @ error/constitute.c/ReadImage/532. convert: non-conforming drawing primitive definition</code>fill' @ error/draw.c/DrawImage/3146.</p>
<p>what does it mean?</p>
</div>
<div id="comment-10929-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 21:11)</span> <span class="comment-user userinfo">NullPointer</span>
</div>
</div>
<span id="10930"></span>
<div id="comment-10930" class="comment not_top_scorer">
<div id="post-10930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>converting from a PNG to RAW worked though without any error messages but when I loaded the RAW into my imageLoader program it shows only colored noise. I have a sample RAW image in the program folder and I can load that one without any problem, so I am confused about all these conversions and why it's not working...</p>
</div>
<div id="comment-10930-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 21:12)</span> <span class="comment-user userinfo">NullPointer</span>
</div>
</div>
<span id="10932"></span>
<div id="comment-10932" class="comment">
<div id="post-10932-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Don't use the RAW format. Use a proper image reading library in your program, like libgd, and open the PNG file. The RAW format is not sufficiently standardized and you'll have changed your program to use a standard image format before you have found out how to exactly tune the output to have the exact same number, width, and arrangement of pixels that your other RAW file from a different source had.</p>
</div>
<div id="comment-10932-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 22:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10913" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-10913-form-container" class="comment-form-container">
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

