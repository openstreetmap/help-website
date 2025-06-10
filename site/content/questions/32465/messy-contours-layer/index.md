+++
type = "question"
title = "[closed] Messy contours layer"
description = '''When I make contours layer (with gdal_contour) for my area (near 60°N), the result is quite messy and not usable. See the image below for an example. Can I fix this, and how? Sorry that this question does not relate to OSM directly, but such artifats are visible on most OSM tiles that use SRTM data,...'''
date = "2014-04-19T21:44:00Z"
lastmod = "2014-04-21T21:08:00Z"
weight = 32465
keywords = [ "contours", "srtm" ]
aliases = [ "/questions/32465" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Messy contours layer](/questions/32465/messy-contours-layer)

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
<span id="post-32465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32465-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I make contours layer (with gdal_contour) for my area (near 60°N), the result is quite messy and not usable. See the image below for an example. Can I fix this, and how?</p>
<p>Sorry that this question does not relate to OSM directly, but such artifats are visible on most OSM tiles that use SRTM data, such as CycleMap.</p>
<p><img src="http://not.textual.ru/zverik/2/4/contours-alot.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span> <span class="post-tag tag-link-srtm" rel="tag" title="see questions tagged &#39;srtm&#39;">srtm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '14, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>21 Apr '14, 21:10</strong> </span></p>
</div>
</div>
<div id="comments-container-32465" class="comments-container">
&#10;</div>
<div id="comment-tools-32465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32465-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by Zverik 21 Apr '14, 21:10

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32468"></span>

<div id="answer-container-32468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32468-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like this area is rather flat. A few things can help:</p>
<p>Render the contour lines with a less proeminent style: lighter, thinner. Contour lines are arbitrary and artificial, so they will look strange if they are as visible as the other map features.</p>
<p>Decrease resolution of the DEM raster, or smooth them with a median filter 3x3 or 5x5 (very useful for Aster). You loose accuracy, but the map is more readable.</p>
<p>Smooth the contour lines with Bezier curves (mapnik smooth parameter).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '14, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-32468" class="comments-container">
&#10;</div>
<div id="comment-tools-32468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32468-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32497"></span>

<div id="answer-container-32497" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32497-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Solved this by downloading <a href="http://topotools.cr.usgs.gov/gmted_viewer/">GMTED2010</a> dataset and applying "Grid → Gaussian Filter" <a href="http://sourceforge.net/apps/trac/saga-gis/wiki/grid_filter">with SAGA</a> (radius 2). Applying "Simple Filter" with radius 8 on SRTM also worked, though GMTED has better coverage in northern regions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '14, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '14, 21:09</strong> </span></p>
</div>
</div>
<div id="comments-container-32497" class="comments-container">
&#10;</div>
<div id="comment-tools-32497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32497-form-container" class="comment-form-container">
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

