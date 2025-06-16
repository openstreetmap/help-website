+++
type = "question"
title = "How do I map a road that has traffic lights only in one direction?"
description = '''Sometimes I&#x27;ll see a road that has a set of traffic lights that only applies in one direction.  Typically this happens when the lights are staggered (i.e. there may be another set of lights some distance away that apply to the opposite lane) or when the lights control access to something like a temp...'''
date = "2010-07-12T16:59:00Z"
lastmod = "2011-01-07T16:16:00Z"
weight = 134
keywords = [ "traffic_signals", "tagging" ]
aliases = [ "/questions/134" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I map a road that has traffic lights only in one direction?](/questions/134/how-do-i-map-a-road-that-has-traffic-lights-only-in-one-direction)

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
<span id="post-134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-134-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sometimes I'll see a road that has a set of traffic lights that only applies in one direction.</p>
<p>Typically this happens when the lights are staggered (i.e. there may be another set of lights some distance away that apply to the opposite lane) or when the lights control access to something like a temporary road or bridge.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Traffic_signals">Tag:traffic___signals in the OSM Wiki</a> does not offer a solution to this and the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Set_of_Traffic_Signals">proposed Set of Traffic Signals</a> seems to have been abandoned.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '10, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-134" class="comments-container">
&#10;</div>
<div id="comment-tools-134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-134-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="173"></span>

<div id="answer-container-173" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-173-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your first example, where the lights in the opposite direction are some distance away, is simply an extreme case of an intersection with a divided highway, where the signals may be all at one of the two carriageways, but both crossing nodes are tagged highway=traffic_signals. I'd handle a "staggered" intersection the same way, since each intersection is fully controlled in all directions by traffic lights, even if not every approach to every individual subintersection has them physically present.</p>
<p>The second example, where a two-way road narrows to one lane and traffic lights control the segment in between, is a case of the highway agency putting traffic lights to a different use than their standard application at a fully-controlled intersection. The same thing happens at a drawbridge, and I don't believe we use highway=traffic_signals there. Perhaps the segment should simply be tagged lanes=1? I'm not sure whether not including a highway=traffic_signals node in this case is misleading; perhaps a "note=controlled by traffic signals" on the one-lane segment would be enough to allow changeover to a new tagging method in the future.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 02:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-173" class="comments-container">
&#10;</div>
<div id="comment-tools-173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-173-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="137"></span>

<div id="answer-container-137" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-137-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the lights only apply in one direction, perhaps the road should be tagged as two ways -- each with a <em>oneway=yes</em> (that is, the standard dual-carriageway tagging scheme) and the appropriate traffic lights node added to each way where appropriate. I've never seen traffic lights that only apply to one lane without the road having a hard separator along the middle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d59cb9321a7a2a3ea5e5790345279ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt%20Williams&#39;s gravatar image" />
<p><span>Matt Williams</span><br />
<span class="score" title="379 reputation points">379</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt Williams has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-137" class="comments-container">
<span id="164"></span>
<div id="comment-164" class="comment">
<div id="post-164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's an example (albeit not mapped with lights "yet") at <a href="http://osm.org/go/0EUggZ6Jp--">http://osm.org/go/0EUggZ6Jp--</a> -- in this case, the road turns single lane with alternating flow (controlled by traffic lights) for the curve where Morston Drift avoids the old line of the Puny Drain - about 100yds between the northbound and southbound sets of lights.</p>
</div>
<div id="comment-164-info" class="comment-info">
<span class="comment-age">(13 Jul '10, 12:54)</span> <span class="comment-user userinfo">Rowland</span>
</div>
</div>
<span id="174"></span>
<div id="comment-174" class="comment">
<div id="post-174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's an extreme example: the one-lane 2.5-mile Whittier Tunnel in Alaska, shared with the Alaska Railroad. The last tunnel photo on <span>shows the traffic signal on approach (which lacks a yellow ball).</span></p>
<p><span></span></p>
<p><span>By the way, this brings up a related issue: whenever a railway runs down the middle of a street, you have a railway crossing in only one direction at each end of the street running.</span></p>
</div>
<div id="comment-174-info" class="comment-info">
<span class="comment-age">(14 Jul '10, 02:46)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
</div>
<div id="comment-tools-137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-137-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2103"></span>

<div id="answer-container-2103" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2103-score" class="post-score" title="current number of votes">
-6
</div>
<span id="post-2103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have already found the wiki page for traffic signals, why don't you discuss there? You question will be read there by alle the persons who have ever edited the page because it is in their watchlist. That is maybe a more competend group than the readers of this newbie help forum ?!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/cb9e3487765b1e13e3fd6ebb00fdcac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartograefin&#39;s gravatar image" />
<p><span>Kartograefin</span><br />
<span class="score" title="592 reputation points">592</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartograefin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2103" class="comments-container">
&#10;</div>
<div id="comment-tools-2103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2103-form-container" class="comment-form-container">
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

