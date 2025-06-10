+++
type = "question"
title = "How to map a no U turn restriction on an undivided road crossing a divided road?"
description = '''I am still on the subject of u turns :) A two-way undivided Street A crosses a two-way divided Street B. This creates two intersection nodes. Street A has a no u turn sign at the intersection. I am thinking I should add a no_u_turn restriction on the farther of the two intersection points, where Str...'''
date = "2011-03-07T19:41:00Z"
lastmod = "2011-03-16T19:02:00Z"
weight = 3622
keywords = [ "turn_restrictions", "no_u_turn", "routing", "cloudmade" ]
aliases = [ "/questions/3622" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to map a no U turn restriction on an undivided road crossing a divided road?](/questions/3622/how-to-map-a-no-u-turn-restriction-on-an-undivided-road-crossing-a-divided-road)

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
<span id="post-3622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3622-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-3622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am still on the subject of u turns :)</p>
<p>A two-way undivided Street A crosses a two-way divided Street B. This creates two intersection nodes. Street A has a no u turn sign at the intersection. I am thinking I should add a no_u_turn restriction on the farther of the two intersection points, where Street A would make a left turn onto Street B. It does not seem plausible that a routing algorithm, if it was looking for a U turn, would plot a U turn at the first intersection, where it would momentarily take the driver against the traffic. Yet, during the moments when I am feeling particularly distrustful of routing algorithms, I tend to add a this second no_u_turn restriction "just in case". But I don't feel good doing it.</p>
<p>Is it safe to only add one turn restriction as described earlier? Has this configuration been tested on CloudMade? I can't come up with a way to click on their map to test such routing scenario (unlike the case of two divided roads intersecting, which is tested easily.)</p>
<p><a href="http://www.openstreetmap.org/?lat=33.58591&amp;lon=-117.725175&amp;zoom=18&amp;layers=M">Here</a> is a sample intersection. Columbia at Aliso Viejo Pkwy</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-no_u_turn" rel="tag" title="see questions tagged &#39;no_u_turn&#39;">no_u_turn</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-cloudmade" rel="tag" title="see questions tagged &#39;cloudmade&#39;">cloudmade</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '11, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3622" class="comments-container">
<span id="3623"></span>
<div id="comment-3623" class="comment">
<div id="post-3623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good question, I was wondering this myself, considering that no-U-turn is the default turn restriction at all intersections in Oregon.</p>
</div>
<div id="comment-3623-info" class="comment-info">
<span class="comment-age">(07 Mar '11, 20:44)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3858"></span>
<div id="comment-3858" class="comment">
<div id="post-3858-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like to bump up this question since I did not receive an answer despite Nic's try below.</p>
</div>
<div id="comment-3858-info" class="comment-info">
<span class="comment-age">(16 Mar '11, 19:02)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3622-form-container" class="comment-form-container">
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

<span id="3628"></span>

<div id="answer-container-3628" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3628-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not going to speculate about Cloudmade. Not only is it closed source, but they have published very little (Only a couple of bug admissions to the talk list in 2009). At least Garmin has some code that can be reverse engineered.</p>
<p>If street A (Columbia) is undivided, routing algorithms should not consider a u-turn at any intersection. We could introduce a new tag to allow for the extremely rare case where it is advantageous and legal to make a u-turn at a mini roundabout. For example, if you are <a href="http://osmu.org/demo/?lat=-25.78512&amp;lon=28.30018&amp;zoom=16&amp;markers=!-25.7853,28.3048!-25.78417,28.3036&amp;v=motorcar&amp;fast=1&amp;layers=B000FTFT">westbound on Atterbury</a> and you want to stop at the hairdresser, the <a href="http://Osm.org">Osm.org</a> Routing Demo "Recommended" route is to turn right into Manitoba, left at the service road, right into Quebec, right into Glenwood, right into Manitoba, left into Atterbury and then left into the service way. It will be slightly shorter if you make a u-turn at the mini roundabout, but perhaps illegal.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '11, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-3628" class="comments-container">
<span id="3630"></span>
<div id="comment-3630" class="comment">
<div id="post-3630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nic, perhaps you could tell me what other programs/sites/devices/services provide routing over OSM. I could try testing using their online inetrfaces, if any. I assumed CloudMade was the main routing user of OSM, as many end-user apps use their routes on back end.</p>
<p>I am not sure I got your answer. You may have made an assumption I did not intend. Perhaps, U-turns are never legal on undivided roads. But routing algorithms don't know whether the road is physically undivided, or is just drawn as a single two-way way for lack of time or need for detalization. Comment continues...</p>
</div>
<div id="comment-3630-info" class="comment-info">
<span class="comment-age">(07 Mar '11, 21:40)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3631"></span>
<div id="comment-3631" class="comment">
<div id="post-3631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Columbia physically is undivided, which is why, I am guessing, there is a no U turn sign. However, the routing algorithms I have seen - well, CloudMade - make no such assumption and have no trouble recommending a U-turn on a single way - provided it's two-way and there is no turn restriction. And in most cases (that is to say, when the road is only undivided in OSM, but divided in real life), this would be perfectly legal.</p>
</div>
<div id="comment-3631-info" class="comment-info">
<span class="comment-age">(07 Mar '11, 21:42)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3632"></span>
<div id="comment-3632" class="comment">
<div id="post-3632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Example <a href="http://osm.org/go/TPVwP9kJb--">http://osm.org/go/TPVwP9kJb--</a> Routing algorithm would not see the difference between Eastwing and Aliso Creek Rd, both of which are drawn as a single way. U turns are prohibited on Eastwing but allowed on Aliso Creek. I believe routing algorithms would recommend U-turns on either road if there were no turn restrictions created for Eastwing.</p>
</div>
<div id="comment-3632-info" class="comment-info">
<span class="comment-age">(07 Mar '11, 21:56)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3634"></span>
<div id="comment-3634" class="comment">
<div id="post-3634-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could try <a href="http://yournavigation.org/"></a><a href="http://yournavigation.org"></a><a href="http://yournavigation.org">yournavigation.org</a>. It appears before cloudmade in most searches for "routing" and uses the same open source routing engine (Gosmore) as the <a href="http://wiki.openstreetmap.org/wiki/Osm.org_Routing_Demo"></a><a href="http://Osm.org"></a><a href="http://Osm.org">Osm.org</a> Routing Demo. They are both a couple of months out of date (Obtaining sponsorship for them has not been easy).</p>
<p>In 2008, no one, not even Cloudmade generated uturns back onto the same road. Surely we can't just abandon such a long standing convention. Furthermore, think of the vast number of additional turn restriction required.</p>
</div>
<div id="comment-3634-info" class="comment-info">
<span class="comment-age">(07 Mar '11, 22:36)</span> <span class="comment-user userinfo">Nic Roets</span>
</div>
</div>
<span id="3636"></span>
<div id="comment-3636" class="comment">
<div id="post-3636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In reviewing skobbler bugs created by real world users, I see that CloudMade (which skobbler reportedly uses) recommend U turns back onto the same street left and right (no pun whatsoever intended). This is also consistent with our real world experience: you miss a turn, you come to an intersection, you check for signs, you make a u turn onto the same road. Yes, it does require a lot of turn restrictions, which is one thing that skobbler bug tracker (<a href="http://MapDust.com">MapDust.com</a>) helps with. If the app recommends an illegal U-turn, the user drops a bug, and OSM editors fix it by adding the proper restriction.</p>
</div>
<div id="comment-3636-info" class="comment-info">
<span class="comment-age">(07 Mar '11, 22:51)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3628-form-container" class="comment-form-container">
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

