+++
type = "question"
title = "Clip part from map with a boundary polygon and adjust intersected polygons from boundary"
description = '''I want to extract (clip) a part of the map with a predefined boundary polygon. I have seen that I can do it with osmosis or osmconvert. But I get the problem, that polygons that intersects the predefined boundary polygon are no more polygons but only lines (because the polygon gets cropped). How can...'''
date = "2015-10-05T13:22:00Z"
lastmod = "2015-10-06T14:28:00Z"
weight = 45718
keywords = [ "boundaries", "intersection", "extract", "polygon", "multipolygon" ]
aliases = [ "/questions/45718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Clip part from map with a boundary polygon and adjust intersected polygons from boundary](/questions/45718/clip-part-from-map-with-a-boundary-polygon-and-adjust-intersected-polygons-from-boundary)

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
<span id="post-45718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to extract (clip) a part of the map with a predefined boundary polygon. I have seen that I can do it with <strong>osmosis</strong> or <strong>osmconvert</strong>. But I get the problem, that polygons that intersects the predefined boundary polygon are no more polygons but only lines (because the polygon gets cropped). How can I automatically adjust intersected polygons to the boundary polygon?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '15, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/fa82129a285be4619d5009aa2e2083a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phlegx&#39;s gravatar image" />
<p><span>phlegx</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phlegx has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '15, 13:22</strong> </span></p>
</div>
</div>
<div id="comments-container-45718" class="comments-container">
<span id="45719"></span>
<div id="comment-45719" class="comment">
<div id="post-45719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please explain what you want to do with the extract once created. This will make it easier for us to suggest something.</p>
</div>
<div id="comment-45719-info" class="comment-info">
<span class="comment-age">(05 Oct '15, 14:45)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45718-form-container" class="comment-form-container">
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

<span id="45751"></span>

<div id="answer-container-45751" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45751-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From your question I understand that you are aiming at clipping the map objects to/by an arbitrary polygon (CP, the Clipping Polygon). Especially, clipping areas defined by Multi-polygon relations. The subject is pretty complex and I don't think you will find open/public code doing that. At the same time area clipping is one of the essential functions of any modern vector map-making so, many of us (must) have it. Here are some hints to one possible solution.<br />
1. Pre-processing. Eliminate any replications (nodes, vectors...) and convert area objects into simple/primitive disjunctive objects (one outer and arbitrary inner border polygons). Strictly, this step is not necessary but soon or later these events may cause algorithm exceptions.<br />
2. Detect and handle trivial cases (the area is guaranteed outside/inside the CP, the CP is inside a hole, the CP is covered by the area and so on). In these cases polygons don't need to be really clipped.<br />
3. For any area border polygon P, that should be clipped, detect the inside-out and the consecutive outside-in crossings with the CP (note that if one of these crossings exist the other one must exist too). Replace the outside P segment between these crossing points with the corresponding CP segment providing the same orientation.<br />
4. Now, you have all polygons inside the CP (strictly inside or eventually with partly overlapping borders exactly on the CP). Make the area restructuring (detect the outer and the corresponding inner polygons). 5. Finally, if you really want a precise area clipping, remove the overlapping outer-inner polygon segments and reconnect the 2 complementary outer/inner segment.<br />
Note that while this is working fine, in practice we usually use another model. We detect all vector tails that are not outside the CP (e.g. country border, district border). This tile coverage provides a bit more than the first (more or less academic) option. Note also that there are many fine details missing in the hints. Most of them you may find in Polygon Algebra and Topology student books.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '15, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-45751" class="comments-container">
&#10;</div>
<div id="comment-tools-45751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45751-form-container" class="comment-form-container">
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

