+++
type = "question"
title = "Connecting linear highway=footway with area:highway=footway containing it?"
description = '''In my local area, there are a lot of sidewalks or pedestrian footways mapped as areas (area:highway=footway) that contain linear paths marked as highway=footway running along the centerline, as recommended on the wiki. The linear paths are not connected to the areas, and the iD editor displays valid...'''
date = "2020-10-04T16:49:00Z"
lastmod = "2020-10-04T21:10:00Z"
weight = 76942
keywords = [ "connection", "footway", "highway", "area" ]
aliases = [ "/questions/76942" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Connecting linear highway=footway with area:highway=footway containing it?](/questions/76942/connecting-linear-highwayfootway-with-areahighwayfootway-containing-it)

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
<span id="post-76942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76942-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my local area, there are a lot of sidewalks or pedestrian footways mapped as areas (<code>area:highway=footway</code>) that contain linear paths marked as <code>highway=footway</code> running along the centerline, as recommended on the wiki. The linear paths are not connected to the areas, and the iD editor displays validation issues due to that. Should they be connected, or is this a non-issue that should be reported to iD?</p>
<p>Here is such an example: <a href="https://www.openstreetmap.org/#map=21/52.46101/16.90936">https://www.openstreetmap.org/#map=21/52.46101/16.90936</a> (sorry about the full link, I cannot find how to get permanent IDs of nodes from the iD editor)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '20, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/296432870fed506ff81bedbb7243d1c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pie3636&#39;s gravatar image" />
<p><span>pie3636</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pie3636 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76942" class="comments-container">
&#10;</div>
<div id="comment-tools-76942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76942-form-container" class="comment-form-container">
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

<span id="76947"></span>

<div id="answer-container-76947" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76947-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pie3636 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would place a shared node where the central ways intersect area:highway polygons.</p>
<p>However, I don't think iD actually has such validation rules in place for area <code>area:highway=*</code>. Instead, I suspect that the iD errors may be caused by a the fact that your <code>area:highway=*</code> areas are additionally tagged with <code>highway=*</code>, which is not really the intended usage of these tags. So iD will treat them like any other <code>highway=*</code>, and flag missing connections as a result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '20, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-76947" class="comments-container">
<span id="76951"></span>
<div id="comment-76951" class="comment">
<div id="post-76951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think your diagnosis is right, because the validation rule seems to be treating the <code>area:highway=*</code> as vehicular roads - the validation error is "Sidewalk crosses Road Area". Since removing all the <code>highway=*</code> tags seems like a bad idea (thousands of tags to change and possibly breaking local consensus, although I found nothing about this on the Polish wiki), I think I will go with the shared nodes.</p>
</div>
<div id="comment-76951-info" class="comment-info">
<span class="comment-age">(04 Oct '20, 21:10)</span> <span class="comment-user userinfo">pie3636</span>
</div>
</div>
</div>
<div id="comment-tools-76947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76947-form-container" class="comment-form-container">
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

