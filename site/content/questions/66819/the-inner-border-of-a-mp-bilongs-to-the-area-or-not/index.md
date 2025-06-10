+++
type = "question"
title = "The &quot;inner&quot; border of a MP bilongs to the area or not?"
description = '''In the digital world, when viewing/rendering objects, the smallest unit is a pixel. Consequently, the border lines of areas defined by MPs are one pixel thick lines. So, the decision whether this one pixel (inner) border line belongs to the area or not may have serious rendering and other functional...'''
date = "2018-11-17T10:23:00Z"
lastmod = "2018-11-30T09:27:00Z"
weight = 66819
keywords = [ "border", "inner", "multipolygon" ]
aliases = [ "/questions/66819" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The "inner" border of a MP bilongs to the area or not?](/questions/66819/the-inner-border-of-a-mp-bilongs-to-the-area-or-not)

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
<span id="post-66819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the digital world, when viewing/rendering objects, the smallest unit is a pixel. Consequently, the border lines of areas defined by MPs are one pixel thick lines. So, the decision whether this one pixel (inner) border line belongs to the area or not may have serious rendering and other functional consequences.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '18, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-66819" class="comments-container">
&#10;</div>
<div id="comment-tools-66819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66819-form-container" class="comment-form-container">
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

<span id="66820"></span>

<div id="answer-container-66820" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66820-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With vector graphics (or indeed map data) the pixel is not necessarily the smallest unit. While the data itself will have a limited precision, it doesn't necessarily have a resolution in the sense used in raster graphics.</p>
<p>While in many cases it is traditional to draw an outline separately on top of the border between e.g. inside and outside, this is not necessary for all rendering systems. The choice may be made to treat the line as having infinitesimal width and define the inside to be one colour and the outside another. If this then needs to rasterised for display then a variety of techniques may be used to determine the final rendered colour. This may be done very simply by, for example, determining whether the centre of each pixel is on one side of the line or the other and then colouring the entire pixel according to that determination, or it may be done by more sophisticated means whereby a determination is made as to how much of the area covered by the pixel is inside or out and choosing a colour for that pixel as being somewhere in between fully inside and fully outside.</p>
<p>When it comes to OpenStreetMap data, remember that there is no unified size of a pixel, this will depend on the renderer, zoom level etc. AFAIK OSM has no nominal width to outline features even though some objects recorded as centrelines <a href="https://wiki.openstreetmap.org/wiki/Key:width">can have explicitly defined widths</a>. To me, trying to make allowances for the dividing line itself potentially having a displayed width strays into "<del>tagging</del> <em>tracing</em> for the renderer".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '18, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-66820" class="comments-container">
<span id="66999"></span>
<div id="comment-66999" class="comment">
<div id="post-66999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Of course. The first lesson in vector/raster based imaging. However the question is much more serious than that. From the many "functional consequences" let us take this illustration. In OSM neighbouring holes in MPs are absolutely legal. If the "inner" border belongs to the area the common border section of the neighbouring holes is part of the area and the contrary. This dilemma has serious topological/connectivity consequences no matter whether you draw or not the area and which resolution (penn thickness) you assume.</p>
</div>
<div id="comment-66999-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 09:00)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="67000"></span>
<div id="comment-67000" class="comment">
<div id="post-67000-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To my mind, the edges of areas have zero with, if as in your example two inner polygons have share a line then the actual inner is the union of the two areas and there is no area between the two regions. To make your example more concrete: if a forest surrounds a grassy clearing and lake and the grassy area borders the lake, the grassy area and lake may both be listed as inner to the forest, but it would be wrong to assume that there is a thin line of forest separating the two entities.</p>
</div>
<div id="comment-67000-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 09:27)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-66820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66820-form-container" class="comment-form-container">
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

