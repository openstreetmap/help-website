+++
type = "question"
title = "Discrepancy at zoomlevel / routingerror"
description = '''https://www.openstreetmap.org/changeset/92992522 I made the changeset above primarily to correct a routing issue- the map shows a dogleg of Hillside that doesn&#x27;t exist, so routing leads to a dead end.  At some zoom levels (20m, 30m, 100m+) the changes I made appear correctly, but at others (50m+) th...'''
date = "2020-10-25T17:31:00Z"
lastmod = "2020-10-29T12:38:00Z"
weight = 77227
keywords = [ "zoomlevel", "routingerror" ]
aliases = [ "/questions/77227" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Discrepancy at zoomlevel / routingerror](/questions/77227/discrepancy-at-zoomlevel-routingerror)

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
<span id="post-77227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77227-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://www.openstreetmap.org/changeset/92992522">https://www.openstreetmap.org/changeset/92992522</a></p>
<p>I made the changeset above primarily to correct a routing issue- the map shows a dogleg of Hillside that doesn't exist, so routing leads to a dead end.</p>
<p>At some zoom levels (20m, 30m, 100m+) the changes I made appear correctly, but at others (50m+) they do not appear at all. Also (consequently?) the routing has not changed for affected addresses- they are routed to a nonexistent road section.</p>
<p>Is this just a matter of propagation time, or is there something else I need to do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '20, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1f37e66b7464718a5b408eeaeea1a86e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="loopgru&#39;s gravatar image" />
<p><span>loopgru</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="loopgru has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '20, 20:17</strong> </span></p>
</div>
</div>
<div id="comments-container-77227" class="comments-container">
&#10;</div>
<div id="comment-tools-77227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77227-form-container" class="comment-form-container">
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

<span id="77228"></span>

<div id="answer-container-77228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77228-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tiles take a while to re-render. They are generally rendered on request unless they have been rendered recently. See <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#Tile_rendering">here</a> for more information. You may also have some tiles cached, in which case you won't be making fresh requests.</p>
<p>Routing updates less frequently, there's usually quite a bit of pre-computation to do.</p>
<p>The tile issue may resolve itself if you clear your cache or use another browser. For the routers, all you can really do is wait (unless you want to try running your own).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '20, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-77228" class="comments-container">
<span id="77238"></span>
<div id="comment-77238" class="comment">
<div id="post-77238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In my experience routing services have taken a few days to use my edits</p>
</div>
<div id="comment-77238-info" class="comment-info">
<span class="comment-age">(26 Oct '20, 10:11)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="77239"></span>
<div id="comment-77239" class="comment">
<div id="post-77239-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Current routing <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=45.49930%2C-122.71917%3B45.49940%2C-122.71814">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=45.49930%2C-122.71917%3B45.49940%2C-122.71814</a></p>
</div>
<div id="comment-77239-info" class="comment-info">
<span class="comment-age">(26 Oct '20, 10:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="77249"></span>
<div id="comment-77249" class="comment">
<div id="post-77249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Confirmed on the cache side- it renders correctly at all zoom levels after a clear. Thank you!</p>
<p>I'll keep an eye on the routing over the next few days to see if/when it is resolved there. Thanks all for the feedback!</p>
</div>
<div id="comment-77249-info" class="comment-info">
<span class="comment-age">(26 Oct '20, 14:31)</span> <span class="comment-user userinfo">loopgru</span>
</div>
</div>
<span id="77266"></span>
<div id="comment-77266" class="comment">
<div id="post-77266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=45.49898%2C-122.72025%3B45.49943%2C-122.71820">https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=45.49898%2C-122.72025%3B45.49943%2C-122.71820</a></p>
</div>
<div id="comment-77266-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 11:50)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="77267"></span>
<div id="comment-77267" class="comment">
<div id="post-77267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Routing seems to working on foot, but not car, at least not a few minutes ago.</p>
</div>
<div id="comment-77267-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 12:00)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="77307"></span>
<div id="comment-77307" class="comment not_top_scorer">
<div id="post-77307-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Car routing is now working using Graphopper five days since your edit. I didn't check yesterday so it may have been working in fours days. see <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=45.49930%2C-122.71917%3B45.49940%2C-122.71814">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=45.49930%2C-122.71917%3B45.49940%2C-122.71814</a></p>
</div>
<div id="comment-77307-info" class="comment-info">
<span class="comment-age">(29 Oct '20, 12:38)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-77228" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-77228-form-container" class="comment-form-container">
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

