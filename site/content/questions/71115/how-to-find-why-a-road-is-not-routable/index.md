+++
type = "question"
title = "How to find why a road is not routable"
description = '''Using iD editor. Reference point: 48.510500, -113.307546 While on a trip recently I ran into a situation where OsmAnd (based on OSM) would not find a route to a National Park campground that I was trying to reach. However, it did find a route if I changed the mode from driving to walking or biking. ...'''
date = "2019-10-11T19:12:00Z"
lastmod = "2019-10-16T14:31:00Z"
weight = 71115
keywords = [ "problem", "routing", "barrier" ]
aliases = [ "/questions/71115" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to find why a road is not routable](/questions/71115/how-to-find-why-a-road-is-not-routable)

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
<span id="post-71115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71115-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using iD editor. Reference point: 48.510500, -113.307546</p>
<p>While on a trip recently I ran into a situation where OsmAnd (based on OSM) would not find a route to a National Park campground that I was trying to reach. However, it did find a route if I changed the mode from driving to walking or biking. In order to find the problem I set the destination just a short ways down the road that I needed to take and gradually kept moving the destination farther down the road until it would no longer find a route. Then I examined the area near where it broke and found that there was a barrier=gate there. Evidently, gates do not allow motor traffic to pass even though it was tagged Access=All. I changed it to barrier=cattle-grid (because there really is a cattle grid there) and now it will route.</p>
<p>My question is: how do we find these types of issues with routing. Gradually moving the destination until it breaks is a very tedious process. When I highlighted the road segment it did not report any issues related to barriers. I am very new to OSM editing but there has to be an easier way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '19, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/6b3646ffa8b999016fb03694b7b94a54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dremelts&#39;s gravatar image" />
<p><span>dremelts</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dremelts has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71115" class="comments-container">
&#10;</div>
<div id="comment-tools-71115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71115-form-container" class="comment-form-container">
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

<span id="71139"></span>

<div id="answer-container-71139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71139-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-71139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you are being misled by the iD editor's way of presenting the data. The original gate <a href="https://www.openstreetmap.org/node/960037163/history">has never had an access tag</a>. You've changed it from gate to toll booth to cattle grid but access was never changed. iD shows indeed access all=yes but it is grayed out. I would think so, and I think you did too, that iD thinks access=yes would be the default for the gate. In reality most routers would assume the default for a barrier, at least for a gate, to be access=no or vehicle=no. And actually, the <a href="https://wiki.openstreetmap.org/wiki/Barriers#Routing">wiki page on barriers</a> prescribes that default, too.</p>
<p>I suggest you add access=yes or access=permissive to both the gate and the cattle grid to make the situation clear. The motor_vehicle=permissive still leaves all non motorized traffic (including pedestrians) at the default which is access=no if in doubt.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '19, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-71139" class="comments-container">
<span id="71172"></span>
<div id="comment-71172" class="comment">
<div id="post-71172-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>TZorn, thank you for the help. Yes, that is VERY confusing the way the iD editor presents the access tags. But I see now that if I scroll down a little it will show the tags that are actually applied to the object. So, I have changed the gate from motor_vehicle=permissive to access=permissive and I added access=yes to the cattle_grid.</p>
</div>
<div id="comment-71172-info" class="comment-info">
<span class="comment-age">(14 Oct '19, 16:57)</span> <span class="comment-user userinfo">dremelts</span>
</div>
</div>
<span id="71188"></span>
<div id="comment-71188" class="comment">
<div id="post-71188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>most routers would assume the default for a barrier, at least for a gate, to be access=no or vehicle=no</p>
</blockquote>
<p>I don't think that's true. The defaults for OSRM and Graphhopper both presume a gate to be passable (which is surely right - the whole point of a gate is that you can open it). Unfortunately the barrier default documentation on the wiki is notoriously broken.</p>
</div>
<div id="comment-71188-info" class="comment-info">
<span class="comment-age">(16 Oct '19, 00:36)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="71191"></span>
<div id="comment-71191" class="comment">
<div id="post-71191-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Richard, maybe "most routers" is exaggerating. But as we see above at least OSMand is treating a gate as access=no and I can see why. Other barriers can be opened (e.g. bollards, swing gates) and OSRM <a href="https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua#L54">does not treat them as access yes</a>. What I take away is that we should always tag the access restrictions to avoid (wrong) guess work by the routers.</p>
</div>
<div id="comment-71191-info" class="comment-info">
<span class="comment-age">(16 Oct '19, 08:26)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71139-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71116"></span>

<div id="answer-container-71116" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71116-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think I have seen <code>access=all</code>. The usual tag if all traffic is legally permitted is <a href="https://wiki.openstreetmap.org/wiki/Key:access"><code>access=yes</code></a> and if it is just generally allowed by the owner then <code>access=permissive</code>.</p>
<p>If there is actually a gate there then the gate tagging should remain. I'm not sure if there are established tags for mixed type barriers, but if the grid is on one side then this could be sidestepped by using two nodes.</p>
<p>OsmAnd will route cars through <code>access=permissive</code>, although for completeness I should mention that it's generally considered poor practice to tag because a specific application doesn't behave or <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">render something</a> correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '19, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '19, 21:57</strong> </span></p>
</div>
</div>
<div id="comments-container-71116" class="comments-container">
<span id="71117"></span>
<div id="comment-71117" class="comment">
<div id="post-71117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll add another node back in for the gate (they are separated by several feet). And you are correct; it did say access=yes (I was going from memory).</p>
</div>
<div id="comment-71117-info" class="comment-info">
<span class="comment-age">(11 Oct '19, 22:33)</span> <span class="comment-user userinfo">dremelts</span>
</div>
</div>
<span id="71120"></span>
<div id="comment-71120" class="comment">
<div id="post-71120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I have added the gate node back in so now there are two barriers in succession: cattle grid and gate. The gate access is set to all=yes, motor vehicles=permissive. Permissive seems appropriate because over the span of 5 days while we were there I never saw the gate closed. So, it appears to meet the criteria: Access allowed until such time as the owner revokes the permission.</p>
</div>
<div id="comment-71120-info" class="comment-info">
<span class="comment-age">(12 Oct '19, 13:22)</span> <span class="comment-user userinfo">dremelts</span>
</div>
</div>
</div>
<div id="comment-tools-71116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71116-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71203"></span>

<div id="answer-container-71203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71203-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A more general answer to "How to find why a road is not routable " is to test the ways with the map page routers By shuffling the Start (green) and End Flags (red), it is easy to narrow down the problem. Only when you have narrowed it down is it worth opening the editor. Don't forget recent edits may not be used by the routers for a few days. Third party apps will, almost certainly, be using older data so check the dates on their downloads as the problem may be there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '19, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-71203" class="comments-container">
&#10;</div>
<div id="comment-tools-71203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71203-form-container" class="comment-form-container">
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

