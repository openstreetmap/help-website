+++
type = "question"
title = "Driving car distance between two coordinates"
description = '''Hi Please help me making a query towards Overpass API. As input I&#x27;d like to give two coordinates and as output I&#x27;d like to get driving distance. cURL example would be much appreciated, but anything goes.'''
date = "2021-08-14T11:48:00Z"
lastmod = "2021-08-14T13:40:00Z"
weight = 81302
keywords = [ "overpass" ]
aliases = [ "/questions/81302" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Driving car distance between two coordinates](/questions/81302/driving-car-distance-between-two-coordinates)

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
<span id="post-81302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81302-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>Please help me making a query towards Overpass API. As input I'd like to give two coordinates and as output I'd like to get driving distance.</p>
<p>cURL example would be much appreciated, but anything goes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '21, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/adf865b143665c371f9f850fc232dfab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ehitajah2rra&#39;s gravatar image" />
<p><span>Ehitajah2rra</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ehitajah2rra has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81302" class="comments-container">
&#10;</div>
<div id="comment-tools-81302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81302-form-container" class="comment-form-container">
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

<span id="81303"></span>

<div id="answer-container-81303" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81303-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ehitajah2rra has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass cannot do that. You need a routing engine like Graphhopper or OSRM. You can install these programs on your own server(s) if you need to make a lot of requests, but if you're just making a few you can use the free public instances. For OSRM, see <a href="http://project-osrm.org/docs/v5.24.0/api/#">http://project-osrm.org/docs/v5.24.0/api/#</a> which has working curl examples. For Graphhopper, see <a href="https://graphhopper.com/">https://graphhopper.com/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '21, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-81303" class="comments-container">
<span id="81304"></span>
<div id="comment-81304" class="comment">
<div id="post-81304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank You so much!</p>
</div>
<div id="comment-81304-info" class="comment-info">
<span class="comment-age">(14 Aug '21, 13:40)</span> <span class="comment-user userinfo">Ehitajah2rra</span>
</div>
</div>
</div>
<div id="comment-tools-81303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81303-form-container" class="comment-form-container">
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

