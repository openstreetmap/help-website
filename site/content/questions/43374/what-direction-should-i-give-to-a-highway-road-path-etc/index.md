+++
type = "question"
title = "What direction should I give to a highway, road, path, etc.?"
description = '''When I plot a highway, road, street or path, what direction should I draw it in, or assign to it? Are there any conventions? For waterways the documented convention is the direction is the direction of the water flow, i.e. downhill to the sea. Also, it would make sense that on divided highways the d...'''
date = "2015-06-03T14:51:00Z"
lastmod = "2015-06-05T15:35:00Z"
weight = 43374
keywords = [ "traffic-flow", "residential", "direction", "highway", "path" ]
aliases = [ "/questions/43374" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What direction should I give to a highway, road, path, etc.?](/questions/43374/what-direction-should-i-give-to-a-highway-road-path-etc)

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
<span id="post-43374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43374-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I plot a highway, road, street or path, what direction should I draw it in, or assign to it? Are there any conventions? For waterways the documented convention is the direction is the direction of the water flow, i.e. downhill to the sea. Also, it would make sense that on divided highways the direction of each way is the same as the direction of the traffic flow, but I cannot see where that has been documented anywhere. My real problem is when it comes to two way streets where there is a single way representing travel in both directions. What is the way direction? Should I draw the way from the end of a street to a junction, or between two junctions on two other streets, the way acquires its direction from the direction it has been drawn in. But should the way direction be changed to follow the property numbering on the street, and be in an increasing property number direction? Or should the direction point towards, or away from, the centre of town, or other destination? What about other ways, like foot and cycle paths, should the direction be uphill, downhill, or is there some other convention or rule?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-traffic-flow" rel="tag" title="see questions tagged &#39;traffic-flow&#39;">traffic-flow</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-direction" rel="tag" title="see questions tagged &#39;direction&#39;">direction</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '15, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/1a623cf4b5df74bee1b91d0c21736921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Huttite&#39;s gravatar image" />
<p><span>Huttite</span><br />
<span class="score" title="560 reputation points">560</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Huttite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43374" class="comments-container">
&#10;</div>
<div id="comment-tools-43374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43374-form-container" class="comment-form-container">
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

<span id="43375"></span>

<div id="answer-container-43375" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43375-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-43375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oneway roads are tagged with <a href="http://wiki.openstreetmap.org/wiki/Oneway">oneway=yes</a>, so the way direction matters. Other way whose direction matter include waterways, coastlines, cliffs, embankments, any way tagged with "*:forward/backward/left/right" keys, etc.</p>
<p>In other cases, the way direction does not matter, so use whatever direction is easyer to draw.</p>
<p>Your editor should know about most of those cases, so that if you reverse the way's direction ('r' in JOSM or 'v' in iD) it'll update the tag and/or warn you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '15, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-43375" class="comments-container">
<span id="43387"></span>
<div id="comment-43387" class="comment">
<div id="post-43387-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Roundabouts (highway=roundabout) are the only exception to the general rule I believe, you should follow the direction of traffic flow (oneway is implicit by tagging conventions, if not specified).</p>
</div>
<div id="comment-43387-info" class="comment-info">
<span class="comment-age">(03 Jun '15, 19:48)</span> <span class="comment-user userinfo">Alecs01</span>
</div>
</div>
<span id="43419"></span>
<div id="comment-43419" class="comment">
<div id="post-43419-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have worked out how I can choose and change the way direction in the editor, that is not my problem.</p>
<p>In the real world, the thing that a way represents will often have a direction. Or the way will need a direction so I can use the tags of forward, left, backwards, right, etc. In my case I have a no exit way with a single line that crosses a single lane bridge from the junction with a main road. Traffic turning off the main road onto the bridge has right of way over traffic coming the other way. Exiting the bridge, after crossing the river there is a sharp left turn with a cutting in the bank on the driver's right and an embankment (river bank) on the left. Of course the driver exiting the street has to give way to traffic turning off the main road, but they have to stop in a passing area, before turning onto the bridge. I want to represent all these features on the same way at the same time, so I need to determine the direction of the way. What is the rule? What is the principle, logic, or convention for choosing a particular direction, if any?</p>
</div>
<div id="comment-43419-info" class="comment-info">
<span class="comment-age">(05 Jun '15, 14:30)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
<span id="43422"></span>
<div id="comment-43422" class="comment">
<div id="post-43422-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Pretty much all tags that depend on the osm way's direction have a "reversed" value (in order to support various combinaisons on a single object). Because of that, the direction of the actual osm way rarely matters, it's just personal style. The exceptions (waterways, cliffs, coastlines...) are rare and documented on the tag's wiki page.</p>
</div>
<div id="comment-43422-info" class="comment-info">
<span class="comment-age">(05 Jun '15, 15:35)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43375-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43376"></span>

<div id="answer-container-43376" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43376-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is a two way street then it does not matter which direction it is entered. The direction of the way only becomes important when you add a oneway tag. Likewise for foot trails and cycle paths.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '15, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-43376" class="comments-container">
<span id="43420"></span>
<div id="comment-43420" class="comment">
<div id="post-43420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My street is two way but with only one lane, so is only wide enough to travel one way at a time. In some places it is wide enough to pass, in other places, particularly the bridges, it is one way at a time only. But it is not a one way street, so the oneway tag is not appropriate, although the tag lanes=1 is. Pedestrians and cyclists also use the street as a footpath, or cycle path, as it has no sidewalks.</p>
<p>So the direction is important. But what is the rule that should be applied to determine the direction that should be recorded?</p>
</div>
<div id="comment-43420-info" class="comment-info">
<span class="comment-age">(05 Jun '15, 14:50)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
</div>
<div id="comment-tools-43376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43376-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43377"></span>

<div id="answer-container-43377" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43377-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree that on a one way street that the way direction should be in the direction of the traffic flow. But on a ONE LANE TWO WAY street the way direction could become very important, because the direction could indicate which direction should give way. For example: on a hill - down hill traffic should give way to up hill traffic, or on a single lane bridge one direction often has right of way over the other direction. In rural areas, some property numbering schemes rely on the distance from the start of the road. This suggests highways should be directional. However, I can't find any convention saying what direction they should be given.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '15, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1a623cf4b5df74bee1b91d0c21736921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Huttite&#39;s gravatar image" />
<p><span>Huttite</span><br />
<span class="score" title="560 reputation points">560</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Huttite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43377" class="comments-container">
<span id="43378"></span>
<div id="comment-43378" class="comment">
<div id="post-43378-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I haven't seen any tagging regarding which way traffic should yield on a two way one lane road, so I can't comment on that. In the western United States the one lane bridges I can remember have a stop sign on both ends and there are no conventions as two which direction has priority.</p>
<p>With respect to addressing, the best case scenario is that each actual address is represented as a point or area so the direction of the near by road is irrelevant. If you are doing address ranges, then that is a separate vector parallel to the road, it is not tagged on the road.</p>
</div>
<div id="comment-43378-info" class="comment-info">
<span class="comment-age">(03 Jun '15, 16:19)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="43418"></span>
<div id="comment-43418" class="comment">
<div id="post-43418-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I came across this wiki article for the <a href="http://wiki.openstreetmap.org/wiki/Key:priority">Key:priority</a> which seems to express just what I want to show on the map. However, it requires the way to have a specific direction. What I want to know is how do I determine the best direction, or is there no rule, standard or convention?</p>
</div>
<div id="comment-43418-info" class="comment-info">
<span class="comment-age">(05 Jun '15, 14:03)</span> <span class="comment-user userinfo">Huttite</span>
</div>
</div>
</div>
<div id="comment-tools-43377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43377-form-container" class="comment-form-container">
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

