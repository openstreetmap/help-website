+++
type = "question"
title = "Bridge on ground level"
description = '''A few questions... I have read that one should tag a bridge with layer=1 and a tunnel with layer=-1, always(?) A lot of times the road on the bridge is on ground level and the crossing road under has been lowered (with an area around the bridge). Then it would feel more natural to set the bridge to ...'''
date = "2011-01-30T12:42:00Z"
lastmod = "2011-07-26T12:19:00Z"
weight = 2559
keywords = [ "tunnel", "bridge", "layer", "ground" ]
aliases = [ "/questions/2559" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Bridge on ground level](/questions/2559/bridge-on-ground-level)

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
<span id="post-2559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2559-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A few questions... I have read that one should tag a bridge with layer=1 and a tunnel with layer=-1, always(?) A lot of times the road on the bridge is on ground level and the crossing road under has been lowered (with an area around the bridge). Then it would feel more natural to set the bridge to layer=0 and a segment of the road under as layer=-1. Is this totally wrong?</p>
<p>How would a bridge on ground level with tag layer=1 be rendered in a future 3D-map?? Or will you have to use elevation data only for that?</p>
<p>Another thing, if two ways join on the same bridge, how should I draw this? If I set a node at the start of the bridge on each way it will look like two seperate bridges, right?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-ground" rel="tag" title="see questions tagged &#39;ground&#39;">ground</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '11, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f71afeb7ab925cfcfd8a96fd2a9e0401?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Divvi&#39;s gravatar image" />
<p><span>Divvi</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Divvi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2559" class="comments-container">
&#10;</div>
<div id="comment-tools-2559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2559-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="2560"></span>

<div id="answer-container-2560" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2560-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-2560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Divvi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't worry. A level bridge at layer=0 with a road (or river) in a hollow underneath at layer=-1 it totally ok.</p>
<p>A future 3D map <strong>might</strong> choose to show a bridge with layer=1 as an arched structure. But that is a design choice of the rendering designer, not something you should worry (too much) about.</p>
<p>Unfortunately we don't have a good solution for the case of several ways sharing a bridge. You can add them to a single type=bridge relation but that is pretty much unused by data consumers today.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '11, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2560" class="comments-container">
&#10;</div>
<div id="comment-tools-2560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2560-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2561"></span>

<div id="answer-container-2561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2561-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-2561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Layer tags simply define the relative position of two or more things. Ground level is usually considered to be layer=0. If you feel that bridge is on layer 0 and the thing(s) below are lower numbers that is fine. Any object without a layer tag will be assumed to be layer=0, but it helps to add a layer=* tag to at least one object when one crosses another. Usually the way on the bridge will be layer=1, but it doesn't have to be.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '11, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-2561" class="comments-container">
&#10;</div>
<div id="comment-tools-2561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2561-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6560"></span>

<div id="answer-container-6560" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6560-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use any layer numbers you like. Layer numbers are only relevant when ways cross. Two consective segments of a way need not have the same layer number, even if those two segments constitute a billiard-table-flat section of road. You could legitimately have a bridge at layer 10 and the road underneath it at say layer 9. The actual layer number does not relate to height above ground; it is purely for determining what layer is above/below what.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '11, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/033239e6e24e8bb673c3446836a5060c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwbg&#39;s gravatar image" />
<p><span>mwbg</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwbg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6560" class="comments-container">
&#10;</div>
<div id="comment-tools-6560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6560-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2571"></span>

<div id="answer-container-2571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2571-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-2571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally speaking, it's not necessary to add a layer tag unless many objects pass over/under one another. See <a href="http://wiki.openstreetmap.org/wiki/Layer">Layer</a> in the OSM Wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '11, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-2571" class="comments-container">
&#10;</div>
<div id="comment-tools-2571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2571-form-container" class="comment-form-container">
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

