+++
type = "question"
title = "Intersecting divided roads: braids or four corners?"
description = '''If a divided roads crosses another divided road I tend to draw four lines with four intersecting points. If a divided road crosses an undivided road, I draw two and one line respectively with two intersecting points. I have noticed that other mappers in my area went an alternative way. They bring al...'''
date = "2011-02-19T15:52:00Z"
lastmod = "2015-10-01T03:43:00Z"
weight = 3194
keywords = [ "divided", "street", "braiding", "intersection" ]
aliases = [ "/questions/3194" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Intersecting divided roads: braids or four corners?](/questions/3194/intersecting-divided-roads-braids-or-four-corners)

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
<span id="post-3194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3194-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-3194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If a divided roads crosses another divided road I tend to draw four lines with four intersecting points. If a divided road crosses an undivided road, I draw two and one line respectively with two intersecting points. I have noticed that other mappers in my area went an alternative way. They bring all lines to a point in the middle of the intersection, creating a braided look. It's not the same braiding problem that had to be fixed from TIGER where the direction was wrong on every other segment. The directions are correct and the routing should work fine. It just looks wrong. After all, when driving, you don't make a sudden lurch to the left at every intersection followed by a lurch to the right.</p>
<p>One benefit of the braiding approach is that you only have to map one traffic light and if there are "No U-turn" signs, they are easier to map. When I create four corners and have "No U-turn" signs to map I always have to think where they go and what the restriction is. I also end up creating separate way in between two intersection points. So I end up with three ways (for the sake of mapping U-turn restrictions) where a "braider" has one. But to me this benefit does not trump the goofy look. Well, almost.</p>
<p>Is there an accepted solution for intersecting divided streets? Should I unbraid the streets others have made or leave them alone?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-divided" rel="tag" title="see questions tagged &#39;divided&#39;">divided</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-braiding" rel="tag" title="see questions tagged &#39;braiding&#39;">braiding</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '11, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3194" class="comments-container">
<span id="3206"></span>
<div id="comment-3206" class="comment">
<div id="post-3206-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You say routing works when the intersection has been braided. But is the directions still correct ? For example if you are in a right hand traffic country (US/EU) and the route is to drive straight across the intersection and the road changes from "A street" to B Street" at the intersection, wouldn't a router say "Make a slight right into B street" ? That would be wrong.</p>
</div>
<div id="comment-3206-info" class="comment-info">
<span class="comment-age">(19 Feb '11, 20:37)</span> <span class="comment-user userinfo">Nic Roets</span>
</div>
</div>
<span id="3211"></span>
<div id="comment-3211" class="comment">
<div id="post-3211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I only meant that the routing algorithm should get you from point A to point B without getting confused about traffic direction or available intersections. I make no guarantees that there won't be some suspect turn instructions in between. But that happens now with most routers that tell you to "merge" from Street A to Street A if there is a new segment on the map, even if it has the same name.</p>
</div>
<div id="comment-3211-info" class="comment-info">
<span class="comment-age">(20 Feb '11, 07:37)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3558"></span>
<div id="comment-3558" class="comment">
<div id="post-3558-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I have now used OSM-based navigator skobbler and I can confirm that when two sides of a divided street come to a point in the middle of the intersection, the app advises the driver (who's going straight through intersection) to make a right turn. The directions come from CloudMade. Confusing if you are navigating an unfamiliar route!</p>
</div>
<div id="comment-3558-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 09:39)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3194-form-container" class="comment-form-container">
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

<span id="3217"></span>

<div id="answer-container-3217" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3217-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-3217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my opinion intersections between dual carriageways should be done using individual intersection, without a central crossing point. Interestingly enough I can't find that in the wiki (but in all the mapped data in the region near me). Traffic lights are mapped separately for every direction plus the pedestrian crossings anyway (can you tell I'm from Germany? <em>g</em>). I'm not sure however if you should unbraid intersections that where mapped by others. That is a question that should be answered by your local community.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '11, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-3217" class="comments-container">
<span id="45680"></span>
<div id="comment-45680" class="comment">
<div id="post-45680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking at Google maps, this is the approach they take. It makes sense.</p>
</div>
<div id="comment-45680-info" class="comment-info">
<span class="comment-age">(01 Oct '15, 03:43)</span> <span class="comment-user userinfo">Jem</span>
</div>
</div>
</div>
<div id="comment-tools-3217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3217-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11450"></span>

<div id="answer-container-11450" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Follow-up Question - Is the decision to choose one junction configuration versus another on the basis of what is best for a particular navigation aid a mild example of "<a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>"?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '12, 00:38</strong></p>
<img src="https://secure.gravatar.com/avatar/925be477b8f486f93b030b27e03bbf5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceyockey&#39;s gravatar image" />
<p><span>ceyockey</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceyockey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11450" class="comments-container">
&#10;</div>
<div id="comment-tools-11450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11450-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35552"></span>

<div id="answer-container-35552" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>how is navigation software to know if a side road connects only to one direction of the divided road,</p>
</blockquote>
<p>For that I add turn restrictions to the intersecting node; as far as I know, navit understands them. In most situations using turn restrictions seems me more elegant than doubling the road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '14, 20:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ec13bb694d2871b12a3c8d686ab05aab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oleg&#39;s gravatar image" />
<p><span>Oleg</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oleg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35552" class="comments-container">
&#10;</div>
<div id="comment-tools-35552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35552-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35453"></span>

<div id="answer-container-35453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35453-score" class="post-score" title="current number of votes">
-6
</div>
<span id="post-35453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Navigating programs (navit in my case) may indeed create confusion -- dangerous when driving. The easiest (but incomplete) fix would be just to introduce property "divided=yes" to the road, and not to draw two roads instead of one whenever possible. In addition I would introduce a new object: group of intersecting points. For example, when two divided roads intersect, their four intersecting nodes would be grouped. A map renderer or a navigator could handle this easily. When such an intersection is controlled by traffic lights, a map renderer could draw one large traffic light symbol instead of four.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '14, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ec13bb694d2871b12a3c8d686ab05aab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oleg&#39;s gravatar image" />
<p><span>Oleg</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oleg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35453" class="comments-container">
<span id="35551"></span>
<div id="comment-35551" class="comment">
<div id="post-35551-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't see how this improves anything. One purpose behind drawing a divided road as two separate lines is so that side roads which only connect to one direction of the divided road can be easily mapped. If you have a single line for a divided road, then how is navigation software to know if a side road connects only to one direction of the divided road, or if there is a break in the median to allow vehicles to go to/from the side road from either direction on the main road?</p>
</div>
<div id="comment-35551-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 19:50)</span> <span class="comment-user userinfo">Jack the Ripper</span>
</div>
</div>
<span id="35553"></span>
<div id="comment-35553" class="comment">
<div id="post-35553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>how is navigation software to know if a side road connects only to one direction of the divided road,</p>
</blockquote>
<p>For that I add turn restrictions to the intersecting node; as far as I know, navit understands them. In most situations using turn restrictions seems me more elegant than doubling the road.</p>
</div>
<div id="comment-35553-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 20:13)</span> <span class="comment-user userinfo">Oleg</span>
</div>
</div>
</div>
<div id="comment-tools-35453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35453-form-container" class="comment-form-container">
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

