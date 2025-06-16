+++
type = "question"
title = "how to cut out data within a defined polygon with osmosis"
description = '''With the current document, osmosis only support extracting a subset from a large downloaded file by define a polygon. But whether there’s a solution to cut out data within a defined polygon.  I have file europe.pbf, what I want to do is cutting out &#x27;Russia&#x27; data, keep other country,  but I can&#x27;t fin...'''
date = "2017-05-24T08:06:00Z"
lastmod = "2017-05-24T09:26:00Z"
weight = 56269
keywords = [ "osmosis" ]
aliases = [ "/questions/56269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to cut out data within a defined polygon with osmosis](/questions/56269/how-to-cut-out-data-within-a-defined-polygon-with-osmosis)

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
<span id="post-56269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56269-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With the current document, osmosis only support extracting a subset from a large downloaded file by define a polygon.</p>
<p>But whether there’s a solution to cut out data within a defined polygon.</p>
<p>I have file europe.pbf, what I want to do is cutting out 'Russia' data, keep other country, but I can't find a way which can help me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '17, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e39e790f95aa9576807573229ea9d7e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="webertao&#39;s gravatar image" />
<p><span>webertao</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="webertao has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56269" class="comments-container">
&#10;</div>
<div id="comment-tools-56269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56269-form-container" class="comment-form-container">
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

<span id="56270"></span>

<div id="answer-container-56270" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56270-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check the example on <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format</a> - what you want is a file with two polygons, the first being a large rectangle around Europe (or a rectangle that covers the whole planet), the second should be a polygon describing Russia, and it needs to be introduced with an exclamation mark which means it is a "hole" in the polygon before.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '17, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56270" class="comments-container">
<span id="56272"></span>
<div id="comment-56272" class="comment">
<div id="post-56272-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for the rectangle that covers the whole planet, whether it could be '90,180', '90,-180', '-90,-180', '-90, 180'?</p>
</div>
<div id="comment-56272-info" class="comment-info">
<span class="comment-age">(24 May '17, 09:20)</span> <span class="comment-user userinfo">webertao</span>
</div>
</div>
<span id="56273"></span>
<div id="comment-56273" class="comment">
<div id="post-56273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, that'll work.</p>
</div>
<div id="comment-56273-info" class="comment-info">
<span class="comment-age">(24 May '17, 09:26)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56270-form-container" class="comment-form-container">
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

