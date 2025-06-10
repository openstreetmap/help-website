+++
type = "question"
title = "Map matching - optimal density of points"
description = '''Hi All, I need to determine the optimal density of points for map matching. I already played with the OSRM&#x27;s map matching API and it gives fine results, but in some cases I realized that the matching is incorrect and it was caused by sparse points. Now I want to find something like rules to get enou...'''
date = "2016-11-18T15:23:00Z"
lastmod = "2016-11-21T12:33:00Z"
weight = 53029
keywords = [ "osrm", "matching", "map" ]
aliases = [ "/questions/53029" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Map matching - optimal density of points](/questions/53029/map-matching-optimal-density-of-points)

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
<span id="post-53029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I need to determine the optimal density of points for map matching. I already played with the OSRM's map matching API and it gives fine results, but in some cases I realized that the matching is incorrect and it was caused by sparse points. Now I want to find something like rules to get enough points, I think about rules like: "You need at least one point every 100m in the buit-up areas" ... It's clear that this depends on many factors like the accuracy of GPS coordinates, the road network in the particular area, etc. and it's clear that the more points the better, but more points mean more data traffic, more storage ... are there any general rules which should be followed?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '16, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e7b6aab57b354bb4867304cd404610f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pksk88&#39;s gravatar image" />
<p><span>pksk88</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pksk88 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53029" class="comments-container">
<span id="53037"></span>
<div id="comment-53037" class="comment">
<div id="post-53037-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>a point every 100m ? that might work for straight roads in modern cities, but not for medieval towns or hiking paths.</p>
</div>
<div id="comment-53037-info" class="comment-info">
<span class="comment-age">(19 Nov '16, 15:44)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="53052"></span>
<div id="comment-53052" class="comment">
<div id="post-53052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for answer yes you'r probably right but did you tried that on real data or is it just a guess, if so what's the underlying assumption. I need to made this decision based on statics or theory :)</p>
</div>
<div id="comment-53052-info" class="comment-info">
<span class="comment-age">(21 Nov '16, 12:10)</span> <span class="comment-user userinfo">pksk88</span>
</div>
</div>
<span id="53053"></span>
<div id="comment-53053" class="comment">
<div id="post-53053-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Take a city of your choice. Generate random start and end points. Calculate a route between these points. Place a point every x meter along this route and see if your map matching algorithm returns the same route. Repeat for a different type of city.</p>
<p>Map matching in cities with a planned street layout (e.g. the US) will be easier than for cities where the street layout developed over a long time (e.g. in most other parts of the world).</p>
<p>Outside of towns you will need a much fewer point density of course.</p>
</div>
<div id="comment-53053-info" class="comment-info">
<span class="comment-age">(21 Nov '16, 12:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53054"></span>
<div id="comment-53054" class="comment">
<div id="post-53054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you scai, this was also one of my initial ideas, using some random sets of points connect them using routing and then just artificially play with different max time or distance to generate points, try to match them and see the error against the ground truth. I can also add some artificial noise to the GPS coordinates. In the simplest form this could be done easily but as you said, we need to consider the different density inside and outside towns, for different speed, etc. which should make this experiment a little bit complicated but anyway, this sounds as a methodologically correct solution.</p>
</div>
<div id="comment-53054-info" class="comment-info">
<span class="comment-age">(21 Nov '16, 12:33)</span> <span class="comment-user userinfo">pksk88</span>
</div>
</div>
</div>
<div id="comment-tools-53029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53029-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

