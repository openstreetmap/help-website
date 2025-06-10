+++
type = "question"
title = "Which co-ordinate system?"
description = '''Hi, Hopefully a simple question, but if you were building something completely new, how would you record the data? Specifically if you wanted to use OSM, would you store the co-ordinates in EPSG:3857 or EPSG:4326? Of course if you need to exchange data with other systems EPSG:4326 might be more usef...'''
date = "2013-07-22T09:06:00Z"
lastmod = "2013-07-22T12:53:00Z"
weight = 24424
keywords = [ "coordinates" ]
aliases = [ "/questions/24424" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Which co-ordinate system?](/questions/24424/which-co-ordinate-system)

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
<span id="post-24424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24424-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Hopefully a simple question, but if you were building something completely new, how would you record the data? Specifically if you wanted to use OSM, would you store the co-ordinates in EPSG:3857 or EPSG:4326? Of course if you need to exchange data with other systems EPSG:4326 might be more useful as users are fairly familiar with the idea of latitude/longitude, however given this would be the exception rather than the rule, is there any merit in storing the data in EPSG:3857 and converting to EPSG:4326 when needed? Would this be any faster with less conversions going on to plot the data on a map? If this is sensible is there an easy way to convert EPSG:3857 to tile names like there is for EPSG:4326?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '13, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b46466f8e6ef72cc352e347c1c34794f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott07&#39;s gravatar image" />
<p><span>Scott07</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott07 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24424" class="comments-container">
&#10;</div>
<div id="comment-tools-24424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24424-form-container" class="comment-form-container">
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

<span id="24428"></span>

<div id="answer-container-24428" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24428-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Scott07 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Storing coordinates in EPSG:3857 could mean a slight performance advantage when drawing but it would also mean that you cannot capture information around the poles since that projection only goes up to 85°N (or down to 85°S).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '13, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24428" class="comments-container">
<span id="24452"></span>
<div id="comment-24452" class="comment">
<div id="post-24452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that, the 85 degree constraint wont be a problem for the intended use. How would you work out a map tile for a EPSG:3857 co-ordinate?</p>
<p>Thanks</p>
<p>Scott</p>
</div>
<div id="comment-24452-info" class="comment-info">
<span class="comment-age">(22 Jul '13, 12:53)</span> <span class="comment-user userinfo">Scott07</span>
</div>
</div>
</div>
<div id="comment-tools-24428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24428-form-container" class="comment-form-container">
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

