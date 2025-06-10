+++
type = "question"
title = "IS Pre-rendering tiles to a certain zoom level is a pre-requisite?"
description = '''Hi, I am planning to set up a map tile server and I was going through forum articles on improving tile rendering performance. Is pre-rendering tiles to a certain zoom level a prerequisite for tile rendering performance or using indexes and fine-tuning Postgres DB we can achieve the required performa...'''
date = "2020-11-09T08:05:00Z"
lastmod = "2020-11-09T08:57:00Z"
weight = 77454
keywords = [ "pre-rendering" ]
aliases = [ "/questions/77454" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IS Pre-rendering tiles to a certain zoom level is a pre-requisite?](/questions/77454/is-pre-rendering-tiles-to-a-certain-zoom-level-is-a-pre-requisite)

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
<span id="post-77454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77454-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am planning to set up a map tile server and I was going through forum articles on improving tile rendering performance. Is pre-rendering tiles to a certain zoom level a prerequisite for tile rendering performance or using indexes and fine-tuning Postgres DB we can achieve the required performance expectations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pre-rendering" rel="tag" title="see questions tagged &#39;pre-rendering&#39;">pre-rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '20, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0479ea402bfffeb70236946603798443?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jchrisprabu&#39;s gravatar image" />
<p><span>jchrisprabu</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jchrisprabu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77454" class="comments-container">
&#10;</div>
<div id="comment-tools-77454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77454-form-container" class="comment-form-container">
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

<span id="77459"></span>

<div id="answer-container-77459" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77459-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jchrisprabu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Rendering tiles on zoom levels &lt;= 8 will always be very slow, and several modifications are required to the osm-carto style if you want to render these "on the fly" with acceptable performance. Generally, pre-rendering the world on z0-12 is recommended when you set up a tile server. You can get away with less but you are very unlikely to get away without pre-rendering z0-8 at least.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '20, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77459" class="comments-container">
<span id="77461"></span>
<div id="comment-77461" class="comment">
<div id="post-77461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik</p>
</div>
<div id="comment-77461-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 08:57)</span> <span class="comment-user userinfo">jchrisprabu</span>
</div>
</div>
</div>
<div id="comment-tools-77459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77459-form-container" class="comment-form-container">
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

