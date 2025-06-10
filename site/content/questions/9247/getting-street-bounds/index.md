+++
type = "question"
title = "Getting street bounds"
description = '''Hello everyone. Can I get using OSM Api the location and bounds of street by lat lon ( the point is near or on the street) and draw a curve on it? Should I use some geo services or route DB(like geoserver.org)?'''
date = "2011-11-27T21:46:00Z"
lastmod = "2011-11-28T12:37:00Z"
weight = 9247
keywords = [ "geolocation" ]
aliases = [ "/questions/9247" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting street bounds](/questions/9247/getting-street-bounds)

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
<span id="post-9247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9247-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>Can I get using OSM Api the location and bounds of street by lat lon ( the point is near or on the street) and draw a curve on it? Should I use some geo services or route DB(like <a href="http://geoserver.org">geoserver.org</a>)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '11, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/04a50c0f1ba0dbf4a36e948646b8f47d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zzzzteph&#39;s gravatar image" />
<p><span>zzzzteph</span><br />
<span class="score" title="30 reputation points">30</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zzzzteph has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9247" class="comments-container">
&#10;</div>
<div id="comment-tools-9247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9247-form-container" class="comment-form-container">
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

<span id="9259"></span>

<div id="answer-container-9259" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9259-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the API to request a "way", which is a line/polygon feature. You can then calculate its bounds fairly easily by requesting its components with the /full call (or requesting each individually). From there you can do simple math on the nodes to see the way's bounds.</p>
<p>As for the second part of your question "The point is near or on the street"- if the point in mention is an existing node in OSM, then you can request if the node is a component of the way.</p>
<p>Since streets in OSM are stored as lines and not areas, unless your point has the exact same location as an existing node, then it would be a bit of a guess (even if it's an extrapolated one) whether it's on a street.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '11, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-9259" class="comments-container">
&#10;</div>
<div id="comment-tools-9259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9259-form-container" class="comment-form-container">
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

