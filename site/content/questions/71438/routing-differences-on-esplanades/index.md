+++
type = "question"
title = "Routing differences on esplanades"
description = '''I wonder why this routing along an esplanade (highway=pedestrian, area=yes) goes all the way around the edges of the area, while this routing along another esplanade (highway=pedestrian, area=yes) doesn&#x27;t do so. What I&#x27;m really trying to achieve is to improve the first mentioned routing (in the wors...'''
date = "2019-11-03T20:52:00Z"
lastmod = "2019-11-04T19:12:00Z"
weight = 71438
keywords = [ "routing", "area" ]
aliases = [ "/questions/71438" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Routing differences on esplanades](/questions/71438/routing-differences-on-esplanades)

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
<span id="post-71438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wonder why <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=59.31228%2C18.10198%3B59.31238%2C18.10180#map=18/59.31302/18.10295">this routing</a> along an esplanade (<em>highway=pedestrian, area=yes</em>) goes all the way around the edges of the area, while <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=43.69434%2C7.25981%3B43.69427%2C7.26033#map=19/43.69437/7.26004">this routing</a> along another esplanade (<em>highway=pedestrian, area=yes</em>) doesn't do so.</p>
<p>What I'm really trying to achieve is to improve the first mentioned routing (in the worst case it routes a 5 m walk into a 1.82 km walk around the edges of the area), while sticking to best mapping practices (I'm aware of the difficulties associated with routing through open areas).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '19, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/9e27711b40b77771caa643f74d9a1d5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henrik&#39;s gravatar image" />
<p><span>Henrik</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henrik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Nov '19, 21:04</strong> </span></p>
</div>
</div>
<div id="comments-container-71438" class="comments-container">
&#10;</div>
<div id="comment-tools-71438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71438-form-container" class="comment-form-container">
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

<span id="71444"></span>

<div id="answer-container-71444" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71444-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Henrik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My guess for an explanation:</p>
<p>In the first case the pedestrian area is mapped as a polygon (highway=pedestrian + area=yes) and this is understood by the routers as a routable way. Since they cannot route over an area they take the edges instead as an approximation.</p>
<p>In the second case the pedestrian area is mapped as a multipolygon and the routers don't accept that as a routable way and completely ignore it. Instead they route over the adjacent cycleway. It's <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=43.69160%2C7.24875%3B43.69156%2C7.24917#map=19/43.69143/7.24944">better visible a bit to the west</a>.</p>
<p>You cannot do much about the problem in the first case. Routers would have to introduce routing over areas. Some mappers map virtual paths over such area but this is generally frowned upon and would require a lot of virtual paths here connecting all the entering paths.</p>
<p>But the problem is a bit academic. A more realistic routing question would be <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=59.31191%2C18.10117%3B59.31375%2C18.10404">solved quite ok</a> in my opinion. Of course the turn-by-turn instructions don't really fit to the situation on the ground.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '19, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-71444" class="comments-container">
<span id="71449"></span>
<div id="comment-71449" class="comment">
<div id="post-71449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I think that you're probably right! Not sure that I agree that the problem is academic though. For example, my use case is to determine the which location (out of a given set of locations) that is closest (walking distance) to a user. If the user's location is on an unfortunate side of the pedestrian area polygon, this calculation becomes very wrong.</p>
</div>
<div id="comment-71449-info" class="comment-info">
<span class="comment-age">(04 Nov '19, 14:40)</span> <span class="comment-user userinfo">Henrik</span>
</div>
</div>
<span id="71453"></span>
<div id="comment-71453" class="comment">
<div id="post-71453-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would setting the area to pedestrian=yes instead of having it unset which i believe these both are. give the routers a chance work.</p>
</div>
<div id="comment-71453-info" class="comment-info">
<span class="comment-age">(04 Nov '19, 19:12)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-71444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71444-form-container" class="comment-form-container">
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

