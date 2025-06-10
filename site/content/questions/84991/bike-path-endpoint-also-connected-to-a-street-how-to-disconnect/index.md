+++
type = "question"
title = "Bike path endpoint also connected to a street, how to disconnect"
description = '''I am trying to extend an existing cycle route to include a new section that was just added to extend the bike path. It appears that the endpoint is intersecting a road. When I try to drag the endpoint of the bike path, it moves the road.  How do I remove the endpoint of the path from being connected...'''
date = "2022-07-07T00:29:00Z"
lastmod = "2022-07-07T08:40:00Z"
weight = 84991
keywords = [ "line" ]
aliases = [ "/questions/84991" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bike path endpoint also connected to a street, how to disconnect](/questions/84991/bike-path-endpoint-also-connected-to-a-street-how-to-disconnect)

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
<span id="post-84991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84991-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to extend an existing cycle route to include a new section that was just added to extend the bike path. It appears that the endpoint is intersecting a road. When I try to drag the endpoint of the bike path, it moves the road.</p>
<p>How do I remove the endpoint of the path from being connected to the road?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '22, 00:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d3fe2be1da98e4fe3474459a55a6e86b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Zeeb&#39;s gravatar image" />
<p><span>Jim Zeeb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Zeeb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84991" class="comments-container">
&#10;</div>
<div id="comment-tools-84991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84991-form-container" class="comment-form-container">
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

<span id="84995"></span>

<div id="answer-container-84995" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84995-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, A link to the intersection point you're talking about would help? Editors differ in the way they do things so which editor would you be using?</p>
<p>An easy answer to the query would be to place a new node where the cycle route is to deviate, then delete the endpoint intersecting the road, (making sure you don't corrupt the road line). Then from your new end node continue to draw the extended cycle route.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '22, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-84995" class="comments-container">
<span id="84997"></span>
<div id="comment-84997" class="comment">
<div id="post-84997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another option is to add a node where you want the path to change. Then split the way at this node and simply delete the wrong part. This approach doesn't work if this part belongs to one or more relations, though.</p>
</div>
<div id="comment-84997-info" class="comment-info">
<span class="comment-age">(07 Jul '22, 08:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84995-form-container" class="comment-form-container">
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

