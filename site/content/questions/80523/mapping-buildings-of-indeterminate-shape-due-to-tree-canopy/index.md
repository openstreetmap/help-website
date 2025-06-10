+++
type = "question"
title = "Mapping buildings of indeterminate shape due to tree canopy."
description = '''I&#x27;m trying to map an area that has many houses and significant, patchy tree coverage that prevents mapping them accurately as areas. I can verify that they&#x27;re there and check things like addresses and building types by looking from the street, but I&#x27;m not about to tromp across residents&#x27; yards to ve...'''
date = "2021-06-11T01:09:00Z"
lastmod = "2021-06-11T18:41:00Z"
weight = 80523
keywords = [ "buildings", "points", "survey", "areas" ]
aliases = [ "/questions/80523" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping buildings of indeterminate shape due to tree canopy.](/questions/80523/mapping-buildings-of-indeterminate-shape-due-to-tree-canopy)

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
<span id="post-80523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to map an area that has many houses and significant, patchy tree coverage that prevents mapping them accurately as areas.</p>
<p>I can verify that they're there and check things like addresses and building types by looking from the street, but I'm not about to tromp across residents' yards to verify their shape to make accurate areas.</p>
<p>What is the best way to deal with this situation: Map the buildings as points (honestly, I've already tried this as the wiki suggests it's a supported feature, but iD won't let me do it)? Map their shapes approximately? Leave it as an exercise for later or another mapper?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-survey" rel="tag" title="see questions tagged &#39;survey&#39;">survey</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '21, 01:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ebf202332a67e278a40e5d490a7c561f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tesla4D&#39;s gravatar image" />
<p><span>Tesla4D</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tesla4D has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80523" class="comments-container">
<span id="80526"></span>
<div id="comment-80526" class="comment">
<div id="post-80526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can also draw a <code>landuse=residential</code> for the area around them.</p>
</div>
<div id="comment-80526-info" class="comment-info">
<span class="comment-age">(11 Jun '21, 07:00)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-80523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80523-form-container" class="comment-form-container">
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

<span id="80524"></span>

<div id="answer-container-80524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80524-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-80524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sometimes the wiki and the iD editor's developers aren't entirely in agreement.</p>
<p>The "Address" preset can be found with iD's feature search and and added to a point. This gives a nice form for input. It is then possible to add the <code>building=house</code> tag manually in the Tags section near the bottom.</p>
<p>I think mapping outlines with poor or patchy imagery tends to be a bit of a personal judgement call and can even be case by case house by house. Ways can always be refined later so if you think you can make a good enough estimate to be helpful then you may consider them worth adding. If tree cover is bad enough that it is almost entirely guesswork then it might be worth leaving it until better imagery is available. It is also not unusual for a mapper on foot to prioritise getting address data available and following up with traces when time or patience permits.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '21, 04:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-80524" class="comments-container">
<span id="80533"></span>
<div id="comment-80533" class="comment">
<div id="post-80533-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's absolutely nothing wrong with mapping a building as a point (aka node). IMO it's appropriate to draw a building's shape if and only if there's sufficiently good imagery to make out the details reasonably well. Which is certainly not the case in many locations worldwide, due to problems like tree cover, outdated imagery, poor image resolution, or imagery missing altogether.</p>
<p>Note that the manual "Tags" section at the bottom of the left panel might need to expanded before you can use it, by clicking the blue arrow next to the word "Tags". You can then add building=house, or building=yes, or any other tag.</p>
<p>Also note that you don't need to add an address if you don't know it (and in fact you can simply select "Point" from iD's feature list instead and "Address".)</p>
</div>
<div id="comment-80533-info" class="comment-info">
<span class="comment-age">(11 Jun '21, 15:29)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="80534"></span>
<div id="comment-80534" class="comment">
<div id="post-80534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a> I probably should have made it more explicit that I do map buildings as points when I don't have imagery (or time) to add more detail.</p>
</div>
<div id="comment-80534-info" class="comment-info">
<span class="comment-age">(11 Jun '21, 18:41)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-80524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80524-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80527"></span>

<div id="answer-container-80527" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80527-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-80527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Tesla4D, estimate the volume for instance in a square and leave a note to make clear that the building is approximated and should be surveyed or imported later.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '21, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-80527" class="comments-container">
&#10;</div>
<div id="comment-tools-80527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80527-form-container" class="comment-form-container">
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

