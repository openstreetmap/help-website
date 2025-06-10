+++
type = "question"
title = "How to change a county line?"
description = '''I am new to editing and can&#x27;t seem to figure out how to change an incorrect county line.'''
date = "2014-09-04T19:37:00Z"
lastmod = "2017-12-12T13:47:00Z"
weight = 36614
keywords = [ "county" ]
aliases = [ "/questions/36614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to change a county line?](/questions/36614/how-to-change-a-county-line)

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
<span id="post-36614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36614-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to editing and can't seem to figure out how to change an incorrect county line.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-county" rel="tag" title="see questions tagged &#39;county&#39;">county</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '14, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c1f07facb4475c0e2104c4cb3485c8ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cauthenn&#39;s gravatar image" />
<p><span>cauthenn</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cauthenn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36614" class="comments-container">
<span id="36621"></span>
<div id="comment-36621" class="comment">
<div id="post-36621-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You should provide a reference to the object/location in question (this can be as simply as providing a link from the main map page with the locatio ncentered) and indicate which editor you are using.</p>
</div>
<div id="comment-36621-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 21:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="61148"></span>
<div id="comment-61148" class="comment">
<div id="post-61148-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same question. Here is a link to an example:<a href="https://www.openstreetmap.org/export#map=16/35.3102/-97.6709">https://www.openstreetmap.org/export#map=16/35.3102/-97.6709</a></p>
<p>The county line is actually on the road called "County Line Road", but it is showing up ~500' to the west. When I go into iD or Potlatch, the line disappears and thus can't be edited.</p>
</div>
<div id="comment-61148-info" class="comment-info">
<span class="comment-age">(11 Dec '17, 21:25)</span> <span class="comment-user userinfo">Dulahey</span>
</div>
</div>
</div>
<div id="comment-tools-36614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36614-form-container" class="comment-form-container">
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

<span id="61152"></span>

<div id="answer-container-61152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61152-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using Dulahey's example.</p>
<p>If you zoom in and select the <code>?</code> tool from the button bar at the right and click near the rendered county line, the query returns 3 "Nearby features". Two of the them are the overall representations of the counties and the third is an "administrative boundary", the geometry that represents that part of the county line. Clicking it brings up <a href="https://www.openstreetmap.org/way/135361436">https://www.openstreetmap.org/way/135361436</a>.</p>
<p>On that page there is a list of all the points that are in the line, 6 in this case. The small number of points is why the feature is hidden in the editors, they don't download the line when there is no point in the current view. To adjust the county line, visit each of those points and adjust the location of it.</p>
<p>Do take care on the corners like <a href="https://www.openstreetmap.org/node/263663965">https://www.openstreetmap.org/node/263663965</a> where the node location impacts several different counties.</p>
<p>If you plan to adjust many borders, it may be worth adopting a workflow like is discussed at <a href="http://ksmapper.blogspot.com/2014/02/workflow-for-fixing-county-borders.html">http://ksmapper.blogspot.com/2014/02/workflow-for-fixing-county-borders.html</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '17, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-61152" class="comments-container">
<span id="61159"></span>
<div id="comment-61159" class="comment">
<div id="post-61159-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Beautiful. Thank you!</p>
</div>
<div id="comment-61159-info" class="comment-info">
<span class="comment-age">(12 Dec '17, 13:47)</span> <span class="comment-user userinfo">Dulahey</span>
</div>
</div>
</div>
<div id="comment-tools-61152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61152-form-container" class="comment-form-container">
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

