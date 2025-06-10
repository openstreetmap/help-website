+++
type = "question"
title = "Return segment of motorway derived from two latlng points"
description = '''Hey guys, For a few days I have been looking into the Overpass API but so far I have been unable to get the exact results I want. I want to get a segment of a motorway, from one point to the other (LatLng points). The point are within a 25m radius from the actual motorway, so fault tolerance is clos...'''
date = "2015-04-06T21:16:00Z"
lastmod = "2015-04-07T10:32:00Z"
weight = 42157
keywords = [ "motorway", "overpass", "section", "points" ]
aliases = [ "/questions/42157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Return segment of motorway derived from two latlng points](/questions/42157/return-segment-of-motorway-derived-from-two-latlng-points)

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
<span id="post-42157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42157-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys,</p>
<p>For a few days I have been looking into the Overpass API but so far I have been unable to get the exact results I want.</p>
<p>I want to get a segment of a motorway, from one point to the other (LatLng points). The point are within a 25m radius from the actual motorway, so fault tolerance is close to zero. So far, so good. However I also would like to get only the way that actually goes into the direction (which is derived from the start and end position). Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-section" rel="tag" title="see questions tagged &#39;section&#39;">section</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '15, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/40e18e19e518b85f3b3bd62a01faa9e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThAlmighty&#39;s gravatar image" />
<p><span>ThAlmighty</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThAlmighty has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '15, 21:17</strong> </span></p>
</div>
</div>
<div id="comments-container-42157" class="comments-container">
&#10;</div>
<div id="comment-tools-42157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42157-form-container" class="comment-form-container">
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

<span id="42166"></span>

<div id="answer-container-42166" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42166-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might think of using PostGIS after importing the data via OSM2PqSQL</p>
<p><a href="http://www.map.et">Alex</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '15, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42166" class="comments-container">
&#10;</div>
<div id="comment-tools-42166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42166-form-container" class="comment-form-container">
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

