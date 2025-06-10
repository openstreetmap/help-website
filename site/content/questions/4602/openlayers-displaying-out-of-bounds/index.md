+++
type = "question"
title = "OpenLayers Displaying out of bounds"
description = '''I have a map displaying a feature overlaying the islands to the west of Alaska and when I extend the bounds, it is zooming way out to world view and repeating part of the feature on the other side of the map - I guess because it is so close to the border. How do I prevent this? (I am thinking either...'''
date = "2011-04-18T18:16:00Z"
lastmod = "2011-04-24T09:31:00Z"
weight = 4602
keywords = [ "openlayers", "bounds", "extent" ]
aliases = [ "/questions/4602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLayers Displaying out of bounds](/questions/4602/openlayers-displaying-out-of-bounds)

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
<span id="post-4602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a map displaying a feature overlaying the islands to the west of Alaska and when I extend the bounds, it is zooming way out to world view and repeating part of the feature on the other side of the map - I guess because it is so close to the border.</p>
<p>How do I prevent this? (I am thinking either by setting the max bounds or by shifting the IDL but I have no success withe either).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-bounds" rel="tag" title="see questions tagged &#39;bounds&#39;">bounds</span> <span class="post-tag tag-link-extent" rel="tag" title="see questions tagged &#39;extent&#39;">extent</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '11, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/4aeae01ed45c0aaf2bf91b968bb5f980?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Denn&#39;s gravatar image" />
<p><span>Denn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Denn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4602" class="comments-container">
&#10;</div>
<div id="comment-tools-4602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4602-form-container" class="comment-form-container">
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

<span id="4761"></span>

<div id="answer-container-4761" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For all I can tell that is a bug in the rather simple way Openlayers calculates the bounding box. The best chances to get help with this is probably the <a href="http://lists.osgeo.org/mailman/listinfo/openlayers-users">openlayers mailinglist</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '11, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4761" class="comments-container">
&#10;</div>
<div id="comment-tools-4761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4761-form-container" class="comment-form-container">
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

