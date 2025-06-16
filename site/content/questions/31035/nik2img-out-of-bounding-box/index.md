+++
type = "question"
title = "[closed] nik2img out of bounding box"
description = '''Hi, Thanks to the help of some nice people on this forum I got nik2img working. Still the images go far over the bounding box values. nik2img.py mapnik.xml mercator1.png --srs 900913 --bbox 4 51 6 54 -d 1500 1500 -v nik2img.py mapnik.xml mercator2.png --srs 900913 --bbox 4 51 6 54 -d 500 500 -v The ...'''
date = "2014-02-25T22:42:00Z"
lastmod = "2014-02-26T12:19:00Z"
weight = 31035
keywords = [ "bbox", "nik2img" ]
aliases = [ "/questions/31035" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] nik2img out of bounding box](/questions/31035/nik2img-out-of-bounding-box)

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
<span id="post-31035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31035-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Thanks to the help of some nice people on this forum I got nik2img working.</p>
<p>Still the images go far over the bounding box values.</p>
<p>nik2img.py mapnik.xml mercator1.png --srs 900913 --bbox 4 51 6 54 -d 1500 1500 -v</p>
<p>nik2img.py mapnik.xml mercator2.png --srs 900913 --bbox 4 51 6 54 -d 500 500 -v</p>
<p>The images start at app 2 long and reach to appr 8 long. Bottom seems valid. Top to low. This makes navigation impossible. Is there a way to really fix these borders on bbox values? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-nik2img" rel="tag" title="see questions tagged &#39;nik2img&#39;">nik2img</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '14, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1a92bff5cdfa9e20e409daab589665ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wim%20de%20vries&#39;s gravatar image" />
<p><span>wim de vries</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wim de vries has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>26 Feb '14, 23:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31035" class="comments-container">
&#10;</div>
<div id="comment-tools-31035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31035-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, accepting own answer is not possible here. So... closing." by aseerel4c26 26 Feb '14, 23:12

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31044"></span>

<div id="answer-container-31044" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31044-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem arises because the dimensions of your image are square, while the projected dimensions of the bounding box are not (the rectangle you are asking to draw is more than twice as high than it is wide).</p>
<p>If you ask Mapnik (nik2img) to put a rectangle that is much higher than wide into a square output file, it will add stuff to the east and west that you haven't asked for. Actually nik2img should tell you the box it has decided to draw in <code>-v</code> mode. Read the output.</p>
<p>For a bbox of "4 51 6 54", you have to specify the dimensions "1500 3698" (or "500 1233") to get an image that exactly contains your bounding box.</p>
<p>See also the <code>--aspect-fix-mode</code> option of nik2img which allows you to control what happens when bounding box and image dimensions do not match.</p>
<p>If you want an output file that has the same aspect ration as the bounding box in degrees (e.g. you enter a box that is 2 degrees wide and 2 degrees high and you want a square output file) then you have to choose <code>--srs 4326</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '14, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '14, 07:20</strong> </span></p>
</div>
</div>
<div id="comments-container-31044" class="comments-container">
<span id="31050"></span>
<div id="comment-31050" class="comment">
<div id="post-31050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. I do see an output line:</p>
<p>Step: 11 // --&gt; Map long/lat bbox: Box2d(2.53474181678,51.0,7.46525818322,54.0)</p>
<p>I presume that is the notification of stretching it up.</p>
<p>I am still puzzled about the image sizes you mention. In the past I have used (downloaded) OSM maps (scale ~1:500000), but there the img height depends on which latitude you are on, while all x values having the same nr of pix size. This made navigation possible using the OSM equations (<a href="https://wiki.openstreetmap.org/wiki/Mercator).">https://wiki.openstreetmap.org/wiki/Mercator).</a></p>
<p>So, I want to say to nik2img: let one longitude be 795 pix; make a map like above (--bbox 4 51 6 54) with width 2x795 pix and height .... calculate it for I don't know.</p>
<p>Do you think this would be possible?</p>
</div>
<div id="comment-31050-info" class="comment-info">
<span class="comment-age">(26 Feb '14, 11:10)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
</div>
<div id="comment-tools-31044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31044-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31051"></span>

<div id="answer-container-31051" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31051-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is --aspect-fix-mode=GROW_CANVAS</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '14, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1a92bff5cdfa9e20e409daab589665ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wim%20de%20vries&#39;s gravatar image" />
<p><span>wim de vries</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wim de vries has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31051" class="comments-container">
&#10;</div>
<div id="comment-tools-31051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31051-form-container" class="comment-form-container">
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

