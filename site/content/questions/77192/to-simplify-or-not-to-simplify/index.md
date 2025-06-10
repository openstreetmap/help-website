+++
type = "question"
title = "To simplify or not to simplify?"
description = '''In Sri Lanka where I do most of my mapping these days many ways look like this channel or that &quot;track&quot;: with a fantastic amount of redundant nodes that inflate the database and slow down rendering on my phone. I&#x27;m very tempted (and usually give in to this temptation) to press Y in JOSM when I&#x27;m maki...'''
date = "2020-10-22T06:34:00Z"
lastmod = "2023-04-20T20:18:00Z"
weight = 77192
keywords = [ "josm", "simplify_way" ]
aliases = [ "/questions/77192" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [To simplify or not to simplify?](/questions/77192/to-simplify-or-not-to-simplify)

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
<span id="post-77192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77192-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Sri Lanka where I do most of my mapping these days many ways look like <a href="https://www.openstreetmap.org/way/807538370/history#map=17/6.65278/80.35118">this channel</a> or <a href="https://www.openstreetmap.org/way/591930661/history">that "track"</a>: with a fantastic amount of redundant nodes that inflate the database and slow down rendering on my phone. I'm very tempted (and usually give in to this temptation) to press Y in JOSM when I'm making a change there and throw away the extra nodes. As there are rather few GPS tracks off the main roads I presume almost all of it is armchair mapped, so even where nodes are not in a straight line and thus objectively superfluous they suggest a precision that simply doesn't exist.</p>
<p>What with prominent mapper Kreuzschnabel giving people doing just this as one of the reasons for his "retirement", I've been thinking again. Do you think that's a fair assumption or should I just leave the nodes alone if they're already in the database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-simplify_way" rel="tag" title="see questions tagged &#39;simplify_way&#39;">simplify_way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '20, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d62eaa0c9cab6317d2887bfe6bd2163b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbethke&#39;s gravatar image" />
<p><span>mbethke</span><br />
<span class="score" title="381 reputation points">381</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbethke has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-77192" class="comments-container">
&#10;</div>
<div id="comment-tools-77192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77192-form-container" class="comment-form-container">
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

<span id="77193"></span>

<div id="answer-container-77193" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77193-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-77193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I seriously doubt if <em>"rendering on your phone is slowed down"</em> by this.</p>
<p>Most, or almost certainly all, navigation and map apps nowadays do not directly use OSM data, but do preprocessing on it to remove extraneous detail through automated simplification processes. E.g. all modern vector tile pipelines do this. If the app is still using raster tiles, there is even less reason why your phone would be slowed down, as raster tile size is ultimately limited by the size of the tiles in pixels.</p>
<p>So I think it is more likely your phone is either an older outdated model with limited capacity, or your mobile phone network a limiting factor.</p>
<p>Secondly, while the data may seem redundant for navigation apps, higher detail data may be of use for large(r) scale topographic maps (e.g. 1:10k to 1:25k), and as such useful for true cartographers. We're not just creating a "graph" for navigations apps to function, but a <em>map</em> as well!</p>
<p>That said, if a clearly straight side line of e.g. a soccer pitch is digitized with 100 vertices where it only needs 2 for begin and end point, I would totally agree its time for a clean up... So it all depends on the exact situation as well, and whether the extraneous detail is likely reliable or just pure fantasy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '20, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-77193" class="comments-container">
<span id="77197"></span>
<div id="comment-77197" class="comment">
<div id="post-77197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, OsmAnd feeling slower in those areas may well be my imagination, but if it was using raster tiles or online data that would have been obvious even to me ;) I totally agree with the map aspect, that was the only part of OSM I used for my first couple of editing years anyway. But yes, considering the best imagery here is at least an order of magnitude lower resolution than what's available in Germany, I think anything that pretends to have a precision of more than about 2m is in the realm of fantasy, especially if the same mapper consistently overlooks minor details like bridges or the difference between an irrigation canal and a tidal channel.</p>
</div>
<div id="comment-77197-info" class="comment-info">
<span class="comment-age">(22 Oct '20, 18:37)</span> <span class="comment-user userinfo">mbethke</span>
</div>
</div>
<span id="77199"></span>
<div id="comment-77199" class="comment">
<div id="post-77199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I compared the tidal channel to the Bing imagery for that area, and it seems to line up very well. While the exact positional accuracy of the way may be a bit off due to misaligned imagery, the positions of the nodes in relation to each other appears to be very good. While "this specific node is where it is in reality" might not be quite right, "this tidal channel that bends at these spots and is close to this spot" is correct and useful to data consumers.</p>
</div>
<div id="comment-77199-info" class="comment-info">
<span class="comment-age">(22 Oct '20, 19:43)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="80015"></span>
<div id="comment-80015" class="comment">
<div id="post-80015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a similar question. The objects I want to simplify aren't straight-line ways with multiple unnecessary nodes but lakes and streams containing thousands of nodes that after simplification with JOSN's Simplify Way plugin using a tiny 0.5-meter delta, will have its node count reduced by 50% or more.</p>
<p>These extra nodes are, IMO, simply wasted storage space and serve no purpose other than to bloat the OSM database. Nobody working with our satellite data can possibly believe that those points are both accurate and essential. And while they may not slow down your smartphone they add bulk to all other derivative applications.</p>
<p>Your thoughts?</p>
</div>
<div id="comment-80015-info" class="comment-info">
<span class="comment-age">(05 May '21, 21:53)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-77193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77193-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87150"></span>

<div id="answer-container-87150" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87150-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, I agree. It's like interpolating scanners that just invent extra pixels that are not coming from an image sensor. There's just no good reason for that. Of course you can guesstimate features—if I see a drain on one side of the road that continues on the other, I tend to assume there's a culvert there for instance. But not by adding more nodes than the imagery even has pixels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '23, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/d62eaa0c9cab6317d2887bfe6bd2163b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbethke&#39;s gravatar image" />
<p><span>mbethke</span><br />
<span class="score" title="381 reputation points">381</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbethke has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-87150" class="comments-container">
&#10;</div>
<div id="comment-tools-87150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87150-form-container" class="comment-form-container">
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

