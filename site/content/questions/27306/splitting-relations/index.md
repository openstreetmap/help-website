+++
type = "question"
title = "Splitting relations?"
description = '''Firstly, I created a relation for a bus route, starting at a certain point. The bus route itself isn&#x27;t &#x27;circular&#x27; however it loops, in the sense that it&#x27;ll travel to its destination, and then turn around, either by a roundabout, or similar, or by making a loop (such as going through a series of road...'''
date = "2013-10-18T18:19:00Z"
lastmod = "2013-10-26T13:57:00Z"
weight = 27306
keywords = [ "bus", "route", "splitting", "relations" ]
aliases = [ "/questions/27306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Splitting relations?](/questions/27306/splitting-relations)

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
<span id="post-27306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27306-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Firstly, I created a relation for a bus route, starting at a certain point. The bus route itself isn't 'circular' however it loops, in the sense that it'll travel to its destination, and then turn around, either by a roundabout, or similar, or by making a loop (such as going through a series of roads eventually coming to a junction leading into a road it was previously on, and returning in the opposite direction).</p>
<p>Here's the relation for that route... <a href="https://www.openstreetmap.org/browse/relation/3277636">Route 410</a></p>
<p>Is this supposed to be one relation, or should it be one relation up to where it starts to return to the other destination? And if so, is there a way of splitting one relation into two, at a certain point?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '13, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/6035647123b433de9d9aaa4259d07e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheUltimateKoopa&#39;s gravatar image" />
<p><span>TheUltimateK...</span><br />
<span class="score" title="161 reputation points">161</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheUltimateKoopa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27306" class="comments-container">
&#10;</div>
<div id="comment-tools-27306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27306-form-container" class="comment-form-container">
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

<span id="27509"></span>

<div id="answer-container-27509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, I tried looking at that relation, but I just got a blank window. What you are describing sounds like a "spoon route". It's really a judgement call as to whether you treat it as one near-circular route, or as two separates. A third option is to have it as two routes, but with the looped section appearing once on each route-drection, so that one trip of the bus through the looped section will map to both relations!</p>
<p>What does the official timetable give as the official terminus (the most distant point (MDP), or the point where it rejoins its original point of divergence, OPOD) ?</p>
<p>Does the bus wait a significant time at the most distant point ?</p>
<p>Does the bus change its destination blind at any point during the loop ?</p>
<p>Are through tickets available, beyond the MDP to the OPOD ?</p>
<p>Do the bus stop timetables around the loop show the bus terminating somewhere other than the point-of-origin ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '13, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/033239e6e24e8bb673c3446836a5060c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwbg&#39;s gravatar image" />
<p><span>mwbg</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwbg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27509" class="comments-container">
&#10;</div>
<div id="comment-tools-27509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27509-form-container" class="comment-form-container">
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

