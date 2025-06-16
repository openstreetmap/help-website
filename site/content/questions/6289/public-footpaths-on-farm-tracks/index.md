+++
type = "question"
title = "Public footpaths on farm tracks"
description = '''What is the correct way to tag a farm road which has a public right-of-way footpath on it, but otherwise is private? How about highway=service,access=private,foot=yes,designation=public_footpath? In this case, what would be the difference between access=private and access=no? I&#x27;ve assumed that highw...'''
date = "2011-07-12T18:09:00Z"
lastmod = "2011-07-19T19:37:00Z"
weight = 6289
keywords = [ "track", "footpath", "service", "highway", "public" ]
aliases = [ "/questions/6289" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Public footpaths on farm tracks](/questions/6289/public-footpaths-on-farm-tracks)

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
<span id="post-6289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6289-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the correct way to tag a farm road which has a public right-of-way footpath on it, but otherwise is private? How about highway=service,access=private,foot=yes,designation=public_footpath? In this case, what would be the difference between access=private and access=no?</p>
<p>I've assumed that highway=service is appropriate for a track that joins a farm to a main road, but if the purpose of the track is to provide access internally within the farm boundary, then highway=track is more appropriate. Is this correct?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-service" rel="tag" title="see questions tagged &#39;service&#39;">service</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '11, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/660363689cead9b16bfce059d49fe7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceperman&#39;s gravatar image" />
<p><span>ceperman</span><br />
<span class="score" title="291 reputation points">291</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceperman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6289" class="comments-container">
&#10;</div>
<div id="comment-tools-6289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6289-form-container" class="comment-form-container">
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

<span id="6436"></span>

<div id="answer-container-6436" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6436-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Having read the wisdom posted here, and studied the documentation and guidelines for using these tags, I've drawn the following conclusions about the semantics of access:</p>
<ol>
<li>The access tag defines a restriction (it's part of the Restrictions group). By default there is no restriction on access, although some types of highway may imply one. For example, highway=service for me implies access=destination.</li>
<li>The access restriction applies to all modes of transport unless specifically mentioned. This includes snowmobiles, pogo sticks, elephants, whatever. If I actually know that snowmobiles are not allowed, I would add snowmobile=no</li>
<li>It's not clear to me what snowmobile=yes would mean in this case: either that snowmobiles are definitely allowed within the restriction, so just restating what's already known, or it overrides the restriction and says that they are always allowed. Since there isn't much point in the first, I'd say it means the second.</li>
<li>I'm not sure about access=yes, since access is a restriction, so what does this mean?</li>
<li>"designated" has a different meaning depending where it's used. foot=designated implies a ROW, but the equivalent for access= is "offical". access=designated means something different. This is confusing.</li>
</ol>
<p>Anyhow, following on from this, in my example I've concluded that the best way to express what I want is simply highway=service,foot=designated; access=destination is implied (or I could add it explicitly), but importantly, foot=designated overrides the access restriction. Foot transport is always allowed, and it's actually a ROW.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '11, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/660363689cead9b16bfce059d49fe7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceperman&#39;s gravatar image" />
<p><span>ceperman</span><br />
<span class="score" title="291 reputation points">291</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceperman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6436" class="comments-container">
<span id="6441"></span>
<div id="comment-6441" class="comment">
<div id="post-6441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Whilst I'd tend to expect routing software to "prefer" a proper road over a service road, I don't think any access restriction is actually implied from highway=service</p>
<p>In practice, I don't think the difference between access=destination and access=yes is particularly relevant in the case where the way does not connect to any other usable ways, as routing software won't be including it unless it is the destination simply for reason of the topography... it becomes much more relevant if it is connected at both ends, such that routing software might decide it looks like a convenient short-cut.</p>
</div>
<div id="comment-6441-info" class="comment-info">
<span class="comment-age">(19 Jul '11, 15:10)</span> <span class="comment-user userinfo">banoffee</span>
</div>
</div>
<span id="6442"></span>
<div id="comment-6442" class="comment">
<div id="post-6442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ceperman, I think that's a good summary. =designated is IMHO an unnecessary tag and one I would never use.</p>
</div>
<div id="comment-6442-info" class="comment-info">
<span class="comment-age">(19 Jul '11, 15:39)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="6448"></span>
<div id="comment-6448" class="comment">
<div id="post-6448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>banoffee: My opinion was based on the observation that services roads are typically on private property and so you should have a "business" reason to be on it or you're probably trespassing. So if that's the normal case then it would make sense for the default access to be destination. But since I don't actually know, and also because I don't make the rules, I accept what you say!</p>
</div>
<div id="comment-6448-info" class="comment-info">
<span class="comment-age">(19 Jul '11, 18:30)</span> <span class="comment-user userinfo">ceperman</span>
</div>
</div>
<span id="6450"></span>
<div id="comment-6450" class="comment">
<div id="post-6450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>...also my perspective is on just getting things onto the map correctly, particularly footpaths, and not from a routing software one.</p>
</div>
<div id="comment-6450-info" class="comment-info">
<span class="comment-age">(19 Jul '11, 19:37)</span> <span class="comment-user userinfo">ceperman</span>
</div>
</div>
</div>
<div id="comment-tools-6436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6436-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6291"></span>

<div id="answer-container-6291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6291-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd assume something like:</p>
<ul>
<li>highway=X (where X is the best description of the actual form of the road - may be service, track, or something else)</li>
<li>access=private (or =destination if people who are visiting the farm would have an implicit right to use it - what if the farmer had ordered pizza? would the delivery boy bring a motorbike up that farm road? Would the postman drive his van up there to deliver a parcel?)</li>
<li>foot=designated (or =yes - I don't think the distinction is particularly relevant when there's a designation tag to make the legal right of way explicit)</li>
<li>designation=public_footpath</li>
</ul>
<p>So, its legal designation is as a public footpath, routing software will only normally allow foot traffic over it, and the physical form would be drawn on a map as a service road, track, or whatever else it looks like.</p>
<p>(Still mainly 'theory' rather than 'practice' for me so far as I've primarily been "duck-tagging", and will need to go back and record legal designations where appropriate/known...)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '11, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/b95e1b5cb818be577b5561688a50368c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banoffee&#39;s gravatar image" />
<p><span>banoffee</span><br />
<span class="score" title="884 reputation points">884</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="banoffee has 3 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6291" class="comments-container">
<span id="6400"></span>
<div id="comment-6400" class="comment">
<div id="post-6400-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've tended to avoid using access= in cases where there are different restrictions for different classes of vehicle, instead preferring to distinguish them e.g in this instance using foot=designated, horse=private, motorcar=private, motorcycle=private, bicycle=private.</p>
<p>Where there is a private track with no access rights, e.g. to a farm, I've been using access=private as a short cut to saying that all vehicles can use it in practice, but shouldn't (because it is private). I've based this assumption on the fact that if the postman or pizza delivery were to use it, they would be authorised</p>
</div>
<div id="comment-6400-info" class="comment-info">
<span class="comment-age">(18 Jul '11, 14:09)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
<span id="6402"></span>
<div id="comment-6402" class="comment">
<div id="post-6402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>...cont.. to use the private access.</p>
<p>The problem really, is what does access= actually mean, in cases where you might have a foot access but not a vehicular one? And is it helpful to record in these cases?</p>
</div>
<div id="comment-6402-info" class="comment-info">
<span class="comment-age">(18 Jul '11, 14:11)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
<span id="6407"></span>
<div id="comment-6407" class="comment">
<div id="post-6407-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@c2r</span>: in the specific list you've given, this would appear to leave access for several classes of vehicle undefined. The relevant hierarchy would appear to be shown on the wiki at <a href="https://wiki.openstreetmap.org/wiki/Access">https://wiki.openstreetmap.org/wiki/Access</a></p>
<p>If it's been snowing a lot, and someone decides to try out their snowmobile... you've not specified an access restriction for snowmobiles, so when they ask the routing software for routes where snowmobiles are allowed, how would it know about any restriction?</p>
<p>I think it reduces potential routing errors by using access= to specify the default access, and tagging exceptions.</p>
</div>
<div id="comment-6407-info" class="comment-info">
<span class="comment-age">(18 Jul '11, 14:41)</span> <span class="comment-user userinfo">banoffee</span>
</div>
</div>
<span id="6443"></span>
<div id="comment-6443" class="comment">
<div id="post-6443-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It may be more useful to tag it as motor_vehicle=private (or motor_vehicle=no). Then this will include cars, motorbikes etc, as well as your snowmobile.</p>
<p>Though this will depend on local access laws. If you are somewhere within a general lack of access rights (eg England), then perhaps access=private makes sense.</p>
</div>
<div id="comment-6443-info" class="comment-info">
<span class="comment-age">(19 Jul '11, 16:02)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-6291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6291-form-container" class="comment-form-container">
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

