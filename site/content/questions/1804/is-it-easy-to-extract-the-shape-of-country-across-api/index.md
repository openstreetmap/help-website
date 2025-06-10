+++
type = "question"
title = "Is it easy to extract the shape of country across API?"
description = '''I read the API documentation for to extract the points (not all of course ;) ) of that make the shape of a country. For example, I have a website with a map. The map is displayed with OpenLayers and the connection is OpenStreeMap. I want to show the shape of Spain for paint with vector polygon.'''
date = "2010-12-13T20:30:00Z"
lastmod = "2010-12-13T20:36:00Z"
weight = 1804
keywords = [ "country", "shape", "api", "openlayers" ]
aliases = [ "/questions/1804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it easy to extract the shape of country across API?](/questions/1804/is-it-easy-to-extract-the-shape-of-country-across-api)

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
<span id="post-1804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1804-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I read the API documentation for to extract the points (not all of course ;) ) of that make the shape of a country.</p>
<p>For example, I have a website with a map. The map is displayed with OpenLayers and the connection is OpenStreeMap. I want to show the shape of Spain for paint with vector polygon.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-shape" rel="tag" title="see questions tagged &#39;shape&#39;">shape</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '10, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/7599b25221cf81f7ec06b4280f8c21d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguel&#39;s gravatar image" />
<p><span>Miguel</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '10, 09:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-1804" class="comments-container">
&#10;</div>
<div id="comment-tools-1804" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1804-form-container" class="comment-form-container">
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

<span id="1805"></span>

<div id="answer-container-1805" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1805-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-1805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap data is very detailed. If you extract the border of Spain from OSM, you will have a polygon with many thousand points, and that will be very slow to draw on OpenLayers. It is better to take such polygons from generalised datasets, for example from the public domain resource <a href="http://naturalearthdata.com">Natural Earth Data</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '10, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-1805" class="comments-container">
&#10;</div>
<div id="comment-tools-1805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1805-form-container" class="comment-form-container">
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

