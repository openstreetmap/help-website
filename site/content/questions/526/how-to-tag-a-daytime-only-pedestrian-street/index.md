+++
type = "question"
title = "How to tag a daytime only pedestrian street?"
description = '''I have a street sign which says &amp;lt; No vehicles 10.00am to 6.00pm except for Permit Holders &amp;gt;. A few yards into the street are signs proclaiming it&#x27;s a Pedestrian Area. A local authority leaflet says cycles are allowed along with the Permit Holders. How should I tag this please?'''
date = "2010-07-31T19:22:00Z"
lastmod = "2011-03-10T16:56:00Z"
weight = 526
keywords = [ "access", "pedestrian", "tags" ]
aliases = [ "/questions/526" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a daytime only pedestrian street?](/questions/526/how-to-tag-a-daytime-only-pedestrian-street)

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
<span id="post-526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-526-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a street sign which says &lt; No vehicles 10.00am to 6.00pm except for Permit Holders &gt;. A few yards into the street are signs proclaiming it's a Pedestrian Area. A local authority leaflet says cycles are allowed along with the Permit Holders. How should I tag this please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '10, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/27ff85291b9bc05aabe35725f69d682b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Molescott&#39;s gravatar image" />
<p><span>Molescott</span><br />
<span class="score" title="265 reputation points">265</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Molescott has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-526" class="comments-container">
<span id="3693"></span>
<div id="comment-3693" class="comment">
<div id="post-3693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't forget to accept an answer (the round checkmark button).</p>
</div>
<div id="comment-3693-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 16:56)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-526-form-container" class="comment-form-container">
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

<span id="553"></span>

<div id="answer-container-553" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-553-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Molescott has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Let's first look for the basic tags. From 6.00pm to 10.00am, the situation can be described as</p>
<pre><code>highway = pedestrian
+ bicycle = yes (optional, because it is a subclass of vehicle)
+ vehicle = yes</code></pre>
<p>The rest of the time, we need a value for "permit holders only". I'll chose <em>=private for the rest of this answer. (A more precise value might be</em> =license as proposed by <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/License">"License" proposal</a>, but it isn't widely used and very similar to *=private for most applications.) The resulting tags would be</p>
<pre><code>highway = pedestrian
+ bicycle = yes
+ vehicle = private</code></pre>
<p>So what we need is a way to switch the vehicle key's value depending on the time. For this purpose, I recommend <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Extended_conditions_for_access_tags">Extended conditions for access tags</a>. Using this proposal's syntax, we end up with</p>
<pre><code>highway = pedestrian
+ bicycle = yes
+ vehicle = private
+ vehicle:(18:00-10:00) = yes</code></pre>
<p>The proposal's syntax is more powerful than <code>hour_on</code>/<code>hour_off</code>, can be used on a per-tag basis and is clearly defined: Using conditions, there's no doubt that the restrictions implied by highway=pedestrian are not affected, and neither is bicycle=yes.</p>
<p>Also note that</p>
<pre><code>...
+ vehicle = yes
+ vehicle:(10:00-18:00) = private</code></pre>
<p>would have the same meaning - however, a router ignoring the time-based restrictions will act differently depending on which one you choose.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '10, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '10, 18:07</strong> </span></p>
</div>
</div>
<div id="comments-container-553" class="comments-container">
<span id="558"></span>
<div id="comment-558" class="comment">
<div id="post-558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure vehicle=license is the right tag: 1) vehicle applies to all vehicles, motorized or not. 2) license isn't widely used, if it's used at all. Access by permit would be more akin to private access than anything.</p>
<p>Also, I'd be more inclined to use hour_on:motor_vehicle= and hour_off:motor_vehicle= to describe start and stop times, to fit with the modifiers used on oneway:mode_of_travel= and other similar tags already in use.</p>
</div>
<div id="comment-558-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 17:21)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="561"></span>
<div id="comment-561" class="comment">
<div id="post-561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@Paul: You're right about the value. As for the key, my answer assumes that the question's wording is precise. If the regulation refers to motor vehicles in reality, then motor_vehicle is, of course, the correct key.</p>
<p>I do not agree with your suggestion for the time-based tag, though. hour_on/off cannot handle multiple values for a key (e.g. different maxspeeds) or multiple time intervals (e.g. 7:00-9:00 and 16:00-18:00). It's a dead-end solution, and fixing a small subset of its shortcomings isn't worth the effort. If you want to discuss this further, I prefer a forum/list thread.</p>
</div>
<div id="comment-561-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 18:14)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-553-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="543"></span>

<div id="answer-container-543" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-543-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a <a href="https://wiki.openstreetmap.org/wiki/Access">wiki entry about access restrictions</a>, which also details time-based restrictions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '10, 07:41</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-543" class="comments-container">
<span id="547"></span>
<div id="comment-547" class="comment">
<div id="post-547-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Paul, Thanks for the link. I had seen the wiki and could probably put together the tags necessary but I stall at the Permit Holders only requirement. I was hoping to be pointed towards a similar example somewhere. The street concerned is a main road through town and I need to stop routing engines using it. Pete.</p>
</div>
<div id="comment-547-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 08:39)</span> <span class="comment-user userinfo">Molescott</span>
</div>
</div>
<span id="548"></span>
<div id="comment-548" class="comment">
<div id="post-548-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Use hour_on and hour_off to indicate when restrictions start and stop. Then something like motor_vehicle=no, foot=yes, bicycle=yes as applicable. If that doesn't do it, then it's a routing engine issue, not a data issue.</p>
</div>
<div id="comment-548-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 09:03)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-543-form-container" class="comment-form-container">
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

