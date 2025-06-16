+++
type = "question"
title = "Trouble with Divided Intersections"
description = '''I have not figured out the correct way to map an intersection with divided lanes. For example, the intersection associated with node 195156704 ... The intersection has a major throughway which is divided, but the intersecting road is the tricky part: to the North is Ocean Road -- to the South is Lon...'''
date = "2016-12-01T02:15:00Z"
lastmod = "2017-01-21T18:11:00Z"
weight = 53185
keywords = [ "ways", "intersection", "routingerror", "routing" ]
aliases = [ "/questions/53185" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Trouble with Divided Intersections](/questions/53185/trouble-with-divided-intersections)

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
<span id="post-53185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53185-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have not figured out the correct way to map an intersection with divided lanes. For example, the intersection associated with node <a href="https://www.openstreetmap.org/node/195156704">195156704</a> ... The intersection has a major throughway which is divided, but the intersecting road is the tricky part: to the North is Ocean Road -- to the South is Longmeadow Road. What is the road called between the divided highway? My routing software OSMAnd told me to drive up the road and make a U-Turn, because it could not figure out how to jump over the Longmeadow Road area, to make a left onto Ocean Road. There must be a simple way to do this, but I cannot puzzle it out. Please help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '16, 02:15</strong></p>
<img src="https://secure.gravatar.com/avatar/cb68523a12e3580728c6bee495ae602e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtc&#39;s gravatar image" />
<p><span>mtc</span><br />
<span class="score" title="411 reputation points">411</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '17, 02:29</strong> </span></p>
</div>
</div>
<div id="comments-container-53185" class="comments-container">
&#10;</div>
<div id="comment-tools-53185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53185-form-container" class="comment-form-container">
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

<span id="53199"></span>

<div id="answer-container-53199" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53199-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mtc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In an odd edge case like this where the two side roads are so different, I'd put the middle portion as a <code>primary_link</code> with no name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '16, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-53199" class="comments-container">
<span id="53201"></span>
<div id="comment-53201" class="comment">
<div id="post-53201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Changing it to an unnamed, primary_link seems like the right choice. I would have tried that, if I had thought of it, before.</p>
</div>
<div id="comment-53201-info" class="comment-info">
<span class="comment-age">(01 Dec '16, 22:57)</span> <span class="comment-user userinfo">mtc</span>
</div>
</div>
<span id="53202"></span>
<div id="comment-53202" class="comment">
<div id="post-53202-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, I do not think this is an "odd edge case". There are many intersections with two names for a single intersecting street. Just for example, the next major intersection South on Lafayette is Breakfast Hill Rd turning into Washington Rd, and the next two North are Robert Rd turning into Heritage, then Elwyn Rd turning into Peverly Hill Rd.</p>
<p>It is a strange system for naming streets, though!</p>
</div>
<div id="comment-53202-info" class="comment-info">
<span class="comment-age">(01 Dec '16, 23:03)</span> <span class="comment-user userinfo">mtc</span>
</div>
</div>
</div>
<div id="comment-tools-53199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53199-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53190"></span>

<div id="answer-container-53190" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53190-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't understand why it does not like the left turn. The data seems to be OK. I recently had a similar case, but there the angle of the connection was pretty sharp. I ended up adding no-u-turn restrictions where the road joined again (Lafayette Road in your case). I haven't tested the updated situation though.</p>
<p>There is no established method for naming the part between Lafayette Road. I see the following possibilities</p>
<ul>
<li>Leave it unnamed</li>
<li><p>Split the part in 2 and name the parts</p></li>
<li><p>Ocean Road in the North, Longmeadow Road in the South. (Logical, OK on map, navigation will announce "wrong" name.</p></li>
<li>Ocean Road in the South, Longmeadow Road in the North. The navigation tool will then announce the correct name. But it will look weird on a map.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '16, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-53190" class="comments-container">
<span id="54229"></span>
<div id="comment-54229" class="comment">
<div id="post-54229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Routing seems ok to me now. Could to be the routers take a little time to catch up with edits.</p>
</div>
<div id="comment-54229-info" class="comment-info">
<span class="comment-age">(21 Jan '17, 18:11)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-53190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53190-form-container" class="comment-form-container">
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

