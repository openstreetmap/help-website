+++
type = "question"
title = "How can I map an area described by metes and bounds?"
description = '''I have a complicated metes-and-bounds description of a boundary (start at this point, go foo feet at an angle of bar degrees, etc.). Is there any way to get this into OSM without calculating the latitude and longitude of each point individually?'''
date = "2010-08-07T19:04:00Z"
lastmod = "2010-08-09T07:59:00Z"
weight = 590
keywords = [ "metes", "bounds", "mapping" ]
aliases = [ "/questions/590" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I map an area described by metes and bounds?](/questions/590/how-can-i-map-an-area-described-by-metes-and-bounds)

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
<span id="post-590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-590-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a complicated metes-and-bounds description of a boundary (start at this point, go foo feet at an angle of bar degrees, etc.). Is there any way to get this into OSM without calculating the latitude and longitude of each point individually?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-metes" rel="tag" title="see questions tagged &#39;metes&#39;">metes</span> <span class="post-tag tag-link-bounds" rel="tag" title="see questions tagged &#39;bounds&#39;">bounds</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '10, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '10, 19:04</strong> </span></p>
</div>
</div>
<div id="comments-container-590" class="comments-container">
&#10;</div>
<div id="comment-tools-590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-590-form-container" class="comment-form-container">
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

<span id="594"></span>

<div id="answer-container-594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-594-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To represent this in a logical way in OSM you have to convert it to coordinates one way or another. If the dataset is big it might be worth the effort to make a script to do this for you.</p>
<p>For small datasets you could use JOSM. When drawing a way JOSM displays the distance and heading of the line segment in the lower part of the screen.</p>
<p>But remember that the accuracy might not be as you hope for the data. Distances are often measured in true distance, taking into account hills, while distance in OSM mostly does not take hills into account. The heading is often written in compass heading witch especially in high latitude situations might be different from the true north heading used in OSM. Old descriptions might also suffer from magnetic pole wobbling.</p>
<p>But not be warned off from importing the data into OSM as bad data is better then no data in many occasions. And a low accuracy import is a great help for mappers in the area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '10, 06:21</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-594" class="comments-container">
<span id="597"></span>
<div id="comment-597" class="comment">
<div id="post-597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"For small datasets you could use JOSM. When drawing a way JOSM displays the distance and heading of the line segment in the lower part of the screen." Yes, that's useful for one or two lines, but infeasible for 500 :)</p>
<p>"But remember that the accuracy..." This is from 1994 in flat swamp: <span></span></p>
</div>
<div id="comment-597-info" class="comment-info">
<span class="comment-age">(08 Aug '10, 12:28)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
<span id="605"></span>
<div id="comment-605" class="comment">
<div id="post-605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unless the surveyor is Doing It Wrong, distances are measured "flat earth" style; using true north. Coincidentally, I hate trying to chain something when there's a hill in the way...</p>
</div>
<div id="comment-605-info" class="comment-info">
<span class="comment-age">(09 Aug '10, 07:59)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-594-form-container" class="comment-form-container">
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

