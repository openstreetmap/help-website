+++
type = "question"
title = "Change speed limit of part of a road"
description = '''I&#x27;ve been using osmAnd~ for navigation in Sweden and found that a road with a speed limit of 90km/h has a section of several kilometers that allow 100km/h. What steps do I have to do in the default web-based OSM editor to change the speed limit of a part of the road?  Neither wiki:Speed limits, wiki...'''
date = "2016-08-27T16:17:00Z"
lastmod = "2023-08-22T02:40:00Z"
weight = 51755
keywords = [ "speedlimit" ]
aliases = [ "/questions/51755" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Change speed limit of part of a road](/questions/51755/change-speed-limit-of-part-of-a-road)

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
<span id="post-51755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51755-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been using <a href="https://en.wikipedia.org/wiki/OsmAnd">osmAnd~</a> for navigation in Sweden and found that a road with a speed limit of 90km/h has a section of several kilometers that allow 100km/h.</p>
<p>What steps do I have to do in the default web-based OSM editor to change the speed limit of a part of the road?</p>
<p>Neither <a href="http://wiki.openstreetmap.org/wiki/Speed_limits">wiki:Speed limits</a>, <a href="http://wiki.openstreetmap.org/wiki/Key:maxspeed">wiki:maxspeed</a> nor <a href="https://help.openstreetmap.org/questions/1330/speed-limits-map-correction">Speed Limits map correction</a> give any help on this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '16, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/9e263681488308e5e5d5e548b2f9bc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cweiske&#39;s gravatar image" />
<p><span>cweiske</span><br />
<span class="score" title="156 reputation points">156</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cweiske has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51755" class="comments-container">
&#10;</div>
<div id="comment-tools-51755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51755-form-container" class="comment-form-container">
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

<span id="51757"></span>

<div id="answer-container-51757" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51757-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You must "split" the road at both points where the speed limit changes in order to isolate that section. Once the 100 kph section is separate, tag it with maxspeed=100</p>
<p>In Potlatch add a node where the limit goes to 100 kph, then type "x" or use the scissors in the toolkit to split the way at that point. Do the same thing when the limit changes back again. Now select that section of highway and apply the new maxspeed tag to it.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '16, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-51757" class="comments-container">
&#10;</div>
<div id="comment-tools-51757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51757-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51756"></span>

<div id="answer-container-51756" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51756-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Go to beginning of speed limit change</li>
<li>Select node (or double-click line to create node at this location)</li>
<li>In the popup, click the scissors icon to split the line</li>
<li>Go to the end of the speed limit change</li>
<li>Select the node</li>
<li>In the popup, click the scissors icon to split the line</li>
<li>Change the speed limit of the line that has been split</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '16, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/9e263681488308e5e5d5e548b2f9bc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cweiske&#39;s gravatar image" />
<p><span>cweiske</span><br />
<span class="score" title="156 reputation points">156</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cweiske has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51756" class="comments-container">
<span id="87730"></span>
<div id="comment-87730" class="comment">
<div id="post-87730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for this!!!</p>
</div>
<div id="comment-87730-info" class="comment-info">
<span class="comment-age">(21 Aug '23, 23:42)</span> <span class="comment-user userinfo">352Guy</span>
</div>
</div>
<span id="87731"></span>
<div id="comment-87731" class="comment">
<div id="post-87731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that at least one response here considers Potlatch to be the default editor. This hasn't been the case since the end of Flash player. You may need to seek out instructions for the iD editor instead.</p>
</div>
<div id="comment-87731-info" class="comment-info">
<span class="comment-age">(22 Aug '23, 02:40)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-51756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51756-form-container" class="comment-form-container">
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

