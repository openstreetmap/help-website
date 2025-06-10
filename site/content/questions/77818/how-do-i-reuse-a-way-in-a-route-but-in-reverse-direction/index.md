+++
type = "question"
title = "How do I reuse a way in a route, but in reverse direction?"
description = '''I am creating hiking routes for some of the trails in my area. Several of these trails include an &quot;entry&quot; way from the trailhead to a loop. After completing the loop, one walks back to the trailhead along the &quot;entry&quot; way in the opposite direction. I am not sure about the correct way to represent thi...'''
date = "2020-12-01T04:27:00Z"
lastmod = "2020-12-02T08:05:00Z"
weight = 77818
keywords = [ "route", "backward", "role", "hiking" ]
aliases = [ "/questions/77818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I reuse a way in a route, but in reverse direction?](/questions/77818/how-do-i-reuse-a-way-in-a-route-but-in-reverse-direction)

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
<span id="post-77818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am creating hiking routes for some of the trails in my area. Several of these trails include an "entry" way from the trailhead to a loop. After completing the loop, one walks back to the trailhead along the "entry" way in the opposite direction. I am not sure about the correct way to represent this in the route.</p>
<p>It seems like I should add the "entry" way twice, once at the beginning of the route and once at the end. JSOM gives me an warning when adding it twice, but lets me. Second time, the hike in in the opposite direction of the way, and seems like it would be appropriate to "reverse" the way for this (to keep the elevation plots/navigation correct). I tried applying the role "backward" and "reverse", but JSOM gives warnings for both. And "backward" appears to be defined to mean ONLY in the direction opposite the way (but I want to use the way in both directions). <a href="https://wiki.openstreetmap.org/wiki/Relation:route">https://wiki.openstreetmap.org/wiki/Relation:route</a></p>
<p>Here is a route where I used the role "backward" for the second pass along the "entry" way<br />
<a href="https://www.openstreetmap.org/relation/11965330">https://www.openstreetmap.org/relation/11965330</a></p>
<p>Here is a route where I reused the "entry" way without a role:<br />
<a href="https://www.openstreetmap.org/relation/11965331">https://www.openstreetmap.org/relation/11965331</a></p>
<p>Guidance for the best practice? (and any other suggestions for these routes)</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-backward" rel="tag" title="see questions tagged &#39;backward&#39;">backward</span> <span class="post-tag tag-link-role" rel="tag" title="see questions tagged &#39;role&#39;">role</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '20, 04:27</strong></p>
<img src="https://secure.gravatar.com/avatar/20665a395e42a468360d324028ebe02d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TroyH&#39;s gravatar image" />
<p><span>TroyH</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TroyH has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77818" class="comments-container">
<span id="77827"></span>
<div id="comment-77827" class="comment">
<div id="post-77827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM gives a prompt regardless when you add a member twice. This is about editing. It's less of a "warning" as validator ones.</p>
</div>
<div id="comment-77827-info" class="comment-info">
<span class="comment-age">(01 Dec '20, 20:50)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="77829"></span>
<div id="comment-77829" class="comment">
<div id="post-77829-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with Kovoschiz, I would see this warning as JOSM prompting you to check that you really did intend to add the member twice, rather than suggesting it is an error.</p>
<p>As far as I am aware, it is fine to add ways twice to hiking routes if that is how you would walk the route in reality. The "meaning" of the double appearance is implied by the order of the members. Here is a slightly different example where I mapped a short trail that requires one section in the middle of the route to be walked twice to reach a viewpoint and return: <a href="https://hiking.waymarkedtrails.org/#route?id=7157490&amp;map=18!36.725!-4.4078">https://hiking.waymarkedtrails.org/#route?id=7157490&amp;map=18!36.725!-4.4078</a> . It seems to work OK, e.g. waymarkedtrails correctly works out the mapped length counting this section twice.</p>
<p>If you feel the entry way is more like a way of getting to the "real" route rather than fully part of the route, then you could consider using the approach role as InsertUser mentioned. There is more on roles here: <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Recreational_route_relation_roles">https://wiki.openstreetmap.org/wiki/Proposed_features/Recreational_route_relation_roles</a> . These roles are relatively new. Possibly if I was mapping my above example now I would consider the "excursion" role for the repeated section.</p>
</div>
<div id="comment-77829-info" class="comment-info">
<span class="comment-age">(02 Dec '20, 08:05)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-77818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77818-form-container" class="comment-form-container">
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

<span id="77821"></span>

<div id="answer-container-77821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77821-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The pages for <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dhiking">hiking</a> and <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dfoot">foot</a> routes suggests that the <code>approach</code> role can be used for paths back to parking etc.</p>
<p>The <code>forward</code> and <code>backward</code> roles were once the generally accepted tagging for single direction parts of public transport routes (often a loop at the end) and would refer to the direction the bus/tram etc. travelled relative to the direction the way is drawn in OSM. In many areas the less ambiguous but more difficult to edit PTv2 is preferred and documentation of the older relation style is getting more difficult to find. The page you linked suggests that these roles may still be in use for cycle routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '20, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-77821" class="comments-container">
&#10;</div>
<div id="comment-tools-77821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77821-form-container" class="comment-form-container">
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

