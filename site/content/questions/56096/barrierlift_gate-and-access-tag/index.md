+++
type = "question"
title = "barrier=lift_gate and access tag"
description = '''Hi, Since a barrier is supposed to restrict the traffic in some way, access tag is slightly confusing here. If a way is tagged with motorcycle=yes, motorcycles are free to ride here. What means barrier=lift_gate tagged motorcycle=yes? A motorcycle will pass through the barrier, but when? When the li...'''
date = "2017-05-09T15:29:00Z"
lastmod = "2017-05-09T20:45:00Z"
weight = 56096
keywords = [ "access", "barrier" ]
aliases = [ "/questions/56096" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [barrier=lift_gate and access tag](/questions/56096/barrierlift_gate-and-access-tag)

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
<span id="post-56096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56096-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Since a barrier is supposed to restrict the traffic in some way, <code>access</code> tag is slightly confusing here. If a way is tagged with <code>motorcycle=yes</code>, motorcycles are free to ride here. What means <code>barrier=lift_gate</code> tagged <code>motorcycle=yes</code>? A motorcycle will pass through the barrier, but when? When the lift gate is lowered or lifted? What about <code>motorcycle=no</code>? Motorcyclists will never pass, regardless of the position of the lift gate? Sorry but for me this is confusing. And JOSM is asking additional tags always when I add a lift gate.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '17, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d1495190e346c0c530fd7205883b55c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plamen&#39;s gravatar image" />
<p><span>Plamen</span><br />
<span class="score" title="151 reputation points">151</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plamen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56096" class="comments-container">
&#10;</div>
<div id="comment-tools-56096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56096-form-container" class="comment-form-container">
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

<span id="56098"></span>

<div id="answer-container-56098" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56098-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Plamen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general barriers imply access=no, they are there to shut someone out after all. For some barriers there are differing implicit access restrictions defined on their respective wiki pages. For barrier=lift_gate that is not the case, though (<a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dlift_gate">https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dlift_gate</a>).</p>
<p>So even if a road has a certain access restriction (yes or no) this does not mean that the barrier necessarily has to have the same restriction. Think of some bollards that split a road into two sections for example, although motor_vehicles might be allowed on both sections the passing of the bollard might only be allowed for pedestrians and bicycles.</p>
<p>But there are other values besides yes or no. The lift gate might be passable for customers (access=customers) or by permission of the owner (access=private) for example. See <a href="https://wiki.openstreetmap.org/wiki/Key:access#Access_tag_values">https://wiki.openstreetmap.org/wiki/Key:access#Access_tag_values</a> for the possibilities. Substitute access by motorcycle if appropriate but don't forget other modes of transport that might be generally allowed (eg. foot=yes).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '17, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-56098" class="comments-container">
<span id="56104"></span>
<div id="comment-56104" class="comment">
<div id="post-56104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The lift gate is mostly a moving boom and is not like the old railway boom covering the entire witdh of the way / street but only 2/3. There is a 1/3 gap, wide enough to allow pedestrians, bicycles or motorcycles to pass. So tag it accordingly the situation and traffic signs.</p>
</div>
<div id="comment-56104-info" class="comment-info">
<span class="comment-age">(09 May '17, 20:24)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="56106"></span>
<div id="comment-56106" class="comment">
<div id="post-56106-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Lift gates vary in width - it's pretty common to see ones that go all the away across the access that they control.</p>
</div>
<div id="comment-56106-info" class="comment-info">
<span class="comment-age">(09 May '17, 20:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56098-form-container" class="comment-form-container">
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

