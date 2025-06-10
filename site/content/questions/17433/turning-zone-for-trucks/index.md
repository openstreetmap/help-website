+++
type = "question"
title = "Turning zone for trucks"
description = '''Take a look at this. It&#x27;s a turn zone for trucks, and not a normal exit. The tertiary road still provides direct access to E65, but if a truck is driving the wrong way, they can handle it at this junction. highway=service does not seem the best way to tag it, and for a minute I considered a _link ta...'''
date = "2012-11-03T02:23:00Z"
lastmod = "2012-11-03T20:08:00Z"
weight = 17433
keywords = [ "trunk", "truck", "turnlanes" ]
aliases = [ "/questions/17433" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Turning zone for trucks](/questions/17433/turning-zone-for-trucks)

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
<span id="post-17433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17433-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Take a look at <a href="http://www.openstreetmap.org/?lat=55.500358&amp;lon=13.388487&amp;zoom=18&amp;layers=M">this</a>. It's a turn zone for trucks, and not a normal exit. The tertiary road still provides direct access to E65, but if a truck is driving the wrong way, they can handle it at this junction. highway=service does not seem the best way to tag it, and for a minute I considered a _link tag, but since it's not a normal junction that seems wrong.</p>
<p>Ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trunk" rel="tag" title="see questions tagged &#39;trunk&#39;">trunk</span> <span class="post-tag tag-link-truck" rel="tag" title="see questions tagged &#39;truck&#39;">truck</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '12, 02:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0210a545c865c5db5159bb059fe343d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grillo&#39;s gravatar image" />
<p><span>Grillo</span><br />
<span class="score" title="345 reputation points">345</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grillo has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-17433" class="comments-container">
&#10;</div>
<div id="comment-tools-17433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17433-form-container" class="comment-form-container">
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

<span id="17439"></span>

<div id="answer-container-17439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17439-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I've understood correctly then highway=service seems reasonable. I'd also consider adding other tags though. Is it only for trucks? If so then I'd <a href="http://wiki.openstreetmap.org/wiki/Key:access">access=no and hgv=yes</a>. Is it only for them to use as you describe, in which case do they need <a href="http://wiki.openstreetmap.org/wiki/Key:oneway">oneway</a> tags adding? And maybe <a href="http://wiki.openstreetmap.org/wiki/Relation:restriction">turn restriction</a> relations to make clear that they should only be used if going the wrong way (warning if you do - at some point validators may spot these strange turn restrictions so add a note tag too).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '12, 07:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17439" class="comments-container">
<span id="17449"></span>
<div id="comment-17449" class="comment">
<div id="post-17449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sounds wise. I'll look into the roads again, but I might have to go out there if there is no Bing coverage. Thanks for the answer!</p>
</div>
<div id="comment-17449-info" class="comment-info">
<span class="comment-age">(03 Nov '12, 20:08)</span> <span class="comment-user userinfo">Grillo</span>
</div>
</div>
</div>
<div id="comment-tools-17439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17439-form-container" class="comment-form-container">
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

