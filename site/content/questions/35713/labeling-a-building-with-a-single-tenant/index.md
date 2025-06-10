+++
type = "question"
title = "Labeling a building with a single tenant"
description = '''I&#x27;m trying to label the office building I currently work in. My company is the sole tenant of the building. Generally, do OSM guidelines dictate that I name the building after the company, or attach a separate point to the building with the company name? The former feels more semantically correct (b...'''
date = "2014-08-11T19:15:00Z"
lastmod = "2014-08-12T09:42:00Z"
weight = 35713
keywords = [ "office", "tagging" ]
aliases = [ "/questions/35713" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Labeling a building with a single tenant](/questions/35713/labeling-a-building-with-a-single-tenant)

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
<span id="post-35713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35713-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to label the office building I currently work in. My company is the sole tenant of the building.</p>
<p>Generally, do OSM guidelines dictate that I name the building after the company, or attach a separate point to the building with the company name? The former feels more semantically correct (by the nature of rental, the company is merely an itinerant occupant of the building), but the latter feels redundant, attaching a separate commercial office node to a commercial office building. Thoughts?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-office" rel="tag" title="see questions tagged &#39;office&#39;">office</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '14, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1ee81188404d89b7c8eb73a6bc4f6659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pagibson&#39;s gravatar image" />
<p><span>pagibson</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pagibson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35713" class="comments-container">
&#10;</div>
<div id="comment-tools-35713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35713-form-container" class="comment-form-container">
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

<span id="35742"></span>

<div id="answer-container-35742" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35742-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-35742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pagibson has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM maps what's visible on the ground. Whether your company owns the building, or is just the sole tenant, will often be indistinguishable from the outside, so I would not worry about making that distinction in the map. I would assign <code>building=yes</code>, any appropriate <code>addr:*</code> tags (using <code>addr:housename</code> only where postally relevant), and then <code>name</code> and likely <code>office</code> tags describing your business.</p>
<p>If the building does have a name that you wish to record in addition to the name of your business, then use <code>name</code> on the building and place a separate node for the business.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '14, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '14, 09:45</strong> </span></p>
</div>
</div>
<div id="comments-container-35742" class="comments-container">
&#10;</div>
<div id="comment-tools-35742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35742-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35717"></span>

<div id="answer-container-35717" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35717-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-35717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would put the company name in the name value and the building name in the addr:housename address tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '14, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-35717" class="comments-container">
<span id="35735"></span>
<div id="comment-35735" class="comment">
<div id="post-35735-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>addr:housename is intended for cases where the name of the building is part of its postal address (e.g. Buckingham Palace, which doesn't have a numerical street address). If you can mail something to the address and use something like 123 Main Street, then addr:housename likely shouldn't be used.</p>
<p>If there's a single tenant of a named building, it's probably best to use the name tag on the building to record its name, and tag the business on a separate node.</p>
</div>
<div id="comment-35735-info" class="comment-info">
<span class="comment-age">(12 Aug '14, 00:30)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-35717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35717-form-container" class="comment-form-container">
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

