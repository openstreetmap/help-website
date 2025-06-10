+++
type = "question"
title = "Using .viking-maps files to generate an image file"
description = '''I&#x27;m using Viking and it buffers OSM tiles in ~/.viking-maps Does anyone know if, and how, to use this map data to render a (big) image file Viking itself is limited to image generation of 5000 * 5000 pixels, which is too small, the alternative is too stitch smaller images, which is tedious, and not ...'''
date = "2012-05-28T17:10:00Z"
lastmod = "2013-03-03T15:12:00Z"
weight = 13028
keywords = [ "viking", "tiles", "image", "render" ]
aliases = [ "/questions/13028" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using .viking-maps files to generate an image file](/questions/13028/using-viking-maps-files-to-generate-an-image-file)

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
<span id="post-13028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13028-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using Viking and it buffers OSM tiles in ~/.viking-maps</p>
<p>Does anyone know if, and how, to use this map data to render a (big) image file</p>
<p>Viking itself is limited to image generation of 5000 * 5000 pixels, which is too small, the alternative is too stitch smaller images, which is tedious, and not so accurate</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-viking" rel="tag" title="see questions tagged &#39;viking&#39;">viking</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '12, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/4479d39fc8e6a48ca8e5df063277ac83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnD&#39;s gravatar image" />
<p><span>JohnD</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13028" class="comments-container">
<span id="13202"></span>
<div id="comment-13202" class="comment">
<div id="post-13202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Currently there is no way for the end user to change this.</p>
<p>However if you can compile the source code then you can adjust the 5000 to the values you want in the code file vikwindow.c (see <a href="https://sourceforge.net/tracker/index.php?func=detail&amp;aid=2831256&amp;group_id=83870&amp;atid=570954)">https://sourceforge.net/tracker/index.php?func=detail&amp;aid=2831256&amp;group_id=83870&amp;atid=570954)</a></p>
<p>Note there is also some work to make this bounding box visible on the screen, configurable and save-able - see <a href="https://github.com/evanbattaglia/viking/tree/imageboxlayer">https://github.com/evanbattaglia/viking/tree/imageboxlayer</a></p>
<p>This may get reworked and included in the next version of Viking.</p>
</div>
<div id="comment-13202-info" class="comment-info">
<span class="comment-age">(01 Jun '12, 23:28)</span> <span class="comment-user userinfo">robbieonsea</span>
</div>
</div>
<span id="20463"></span>
<div id="comment-20463" class="comment">
<div id="post-20463-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Viking 1.4 has upped the limit to 50000x50000 pixels.</p>
<p>Although in practise (due the to the implementation) it is limited by (I think) the video cards display capability. So for instance I can only get it to work at 20000x20000 reliably, which takes several seconds to generate.</p>
</div>
<div id="comment-20463-info" class="comment-info">
<span class="comment-age">(03 Mar '13, 15:12)</span> <span class="comment-user userinfo">robbieonsea</span>
</div>
</div>
</div>
<div id="comment-tools-13028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13028-form-container" class="comment-form-container">
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

<span id="13133"></span>

<div id="answer-container-13133" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13133-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One hint I can give you is <a href="http://wiki.openstreetmap.org/wiki/Bigmap">Bigmap</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '12, 20:20</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-13133" class="comments-container">
&#10;</div>
<div id="comment-tools-13133" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13133-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13135"></span>

<div id="answer-container-13135" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13135-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Vikings max for 1 image files is 5000x5000. But you can also export a directory of images with a 10x10 matrix of 5000x5000 images. From there, you might be able to use GIMP to stitch them. Not sure if 50000 x 50000 is enough for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '12, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffdc5279fd70540799b762c14e66665?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwernerny&#39;s gravatar image" />
<p><span>jwernerny</span><br />
<span class="score" title="401 reputation points">401</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwernerny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13135" class="comments-container">
&#10;</div>
<div id="comment-tools-13135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13135-form-container" class="comment-form-container">
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

