+++
type = "question"
title = "coordinate format LatLon vs LonLat"
description = '''Hi, I am trying to write a small tool but I am more and more confused. What is the correct (or the best) way to present the result coordinates? LatLon or LonLat? Seems every application decides for itself. OSM GPS Planet -&amp;gt;latlon Polygon File (*.poly) -&amp;gt;lonlat Garmin CSV -&amp;gt;lonlat OGR (csv) ...'''
date = "2012-04-30T10:41:00Z"
lastmod = "2012-04-30T10:58:00Z"
weight = 12450
keywords = [ "latlon", "lonlat", "coordinates" ]
aliases = [ "/questions/12450" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [coordinate format LatLon vs LonLat](/questions/12450/coordinate-format-latlon-vs-lonlat)

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
<span id="post-12450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to write a small tool but I am more and more confused. What is the correct (or the best) way to present the result coordinates? LatLon or LonLat? Seems every application decides for itself.</p>
<p>OSM GPS Planet -&gt;latlon</p>
<p>Polygon File (*.poly) -&gt;lonlat</p>
<p>Garmin CSV -&gt;lonlat</p>
<p>OGR (csv) -&gt;LatLon</p>
<p>KML -&gt;LonLat</p>
<p>ISO 6709 -&gt;LatLon</p>
<p>Basic coordinate system (xy) -&gt;lonlat</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latlon" rel="tag" title="see questions tagged &#39;latlon&#39;">latlon</span> <span class="post-tag tag-link-lonlat" rel="tag" title="see questions tagged &#39;lonlat&#39;">lonlat</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '12, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0d6b8ca226cd8b7f08b8974f297dfd64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SunCobalt&#39;s gravatar image" />
<p><span>SunCobalt</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SunCobalt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12450" class="comments-container">
&#10;</div>
<div id="comment-tools-12450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12450-form-container" class="comment-form-container">
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

<span id="12452"></span>

<div id="answer-container-12452" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12452-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Stuff that deals with latitude and longitude exclusively tends to list latitude first, then longitude.</p>
<p>Stuff that deals with some abstract sort of coordinates, which <em>might</em> be latitude and longitude but could also be any kind of projected x/y, tends to list longitude first, then latitude.</p>
<p>For specifying bounding boxes, most programs use the sequence west-south-east-north, or minlon-minlat-maxlon-maxlat but even that is not always the same.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '12, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12452" class="comments-container">
&#10;</div>
<div id="comment-tools-12452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12452-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12453"></span>

<div id="answer-container-12453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12453-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The only thing worse then no standard is two standards that is indistinguishable. Just be sure that you document what way you use. I prefer latlon because it is an iso standard and the tools I use tend to use that format, but there are no real advantages to using one over the other.</p>
<p>If you are writing a tool that is taking input from or output to programs with unknown order make sure to add an option to swap the coordinates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '12, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12453" class="comments-container">
&#10;</div>
<div id="comment-tools-12453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12453-form-container" class="comment-form-container">
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

