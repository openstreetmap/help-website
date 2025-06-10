+++
type = "question"
title = "How can I pick areas in the data overlay that are hidden by other areas"
description = '''If e.g go to http://www.openstreetmap.org/?lat=48.135583&amp;amp;lon=11.614641&amp;amp;zoom=18&amp;amp;layers=M and activate the data overlay it is not possible to pick the parking lot in the middle as it is hidden by another area. The same problem exists for a lot of other ways. How can I pick it anyway? Using...'''
date = "2010-11-01T20:52:00Z"
lastmod = "2010-11-02T10:41:00Z"
weight = 1406
keywords = [ "picking", "data", "overlay" ]
aliases = [ "/questions/1406" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I pick areas in the data overlay that are hidden by other areas](/questions/1406/how-can-i-pick-areas-in-the-data-overlay-that-are-hidden-by-other-areas)

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
<span id="post-1406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1406-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If e.g go to <a href="http://www.openstreetmap.org/?lat=48.135583&amp;lon=11.614641&amp;zoom=18&amp;layers=M">http://www.openstreetmap.org/?lat=48.135583&amp;lon=11.614641&amp;zoom=18&amp;layers=M</a> and activate the data overlay it is not possible to pick the parking lot in the middle as it is hidden by another area. The same problem exists for a lot of other ways. How can I pick it anyway? Using the object list is IMO too time consuming as one needs to try all 'way' entries.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-picking" rel="tag" title="see questions tagged &#39;picking&#39;">picking</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '10, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/7fdd2a23ef2c61ebed9eec7f3aa54ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grungelborz&#39;s gravatar image" />
<p><span>grungelborz</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grungelborz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1406" class="comments-container">
&#10;</div>
<div id="comment-tools-1406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1406-form-container" class="comment-form-container">
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

<span id="1421"></span>

<div id="answer-container-1421" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1421-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="grungelborz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a problem with <a href="http://openlayers.org">OpenLayers</a> (see <a href="http://trac.openstreetmap.org/ticket/2760">this bug report</a>) and the ordering of polygons by size. We need to wait until either it's fixed in the OpenLayers project, or we find some other way around it.</p>
<p>The practical way around this problem is to click "manually select a different area" and draw a small box around the feature you are interested in. If this still causes problems, find a corner of the area and draw the box around that - it will find the node in the corner and load up the rest of the way too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '10, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-1421" class="comments-container">
&#10;</div>
<div id="comment-tools-1421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1421-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1408"></span>

<div id="answer-container-1408" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1408-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't. <a href="http://trac.openstreetmap.org/ticket/2760">It has been reported</a></p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '10, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>01 Nov '10, 21:11</strong> </span></p>
</div>
</div>
<div id="comments-container-1408" class="comments-container">
&#10;</div>
<div id="comment-tools-1408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1408-form-container" class="comment-form-container">
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

