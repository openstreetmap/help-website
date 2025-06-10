+++
type = "question"
title = "get residential street closest to gps coordinates"
description = '''I&#x27;m trying to get a residential road using the reversegeocoding with nominatim. This is what I have constructed https://nominatim.openstreetmap.org/reverse.php?format=html&amp;amp;lat=47.5&amp;amp;lon=-122&amp;amp;zoom=16&amp;amp;highway=residential but the road returned is not residential, instead it&#x27;s classified ...'''
date = "2018-08-03T14:27:00Z"
lastmod = "2018-08-06T11:24:00Z"
weight = 65105
keywords = [ "nominatim", "reversegeolocation", "reversegeocoding", "coordinates", "gps" ]
aliases = [ "/questions/65105" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [get residential street closest to gps coordinates](/questions/65105/get-residential-street-closest-to-gps-coordinates)

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
<span id="post-65105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get a residential road using the reversegeocoding with nominatim. This is what I have constructed</p>
<p><a href="https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=47.5&amp;lon=-122&amp;zoom=16&amp;highway=residential">https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=47.5&amp;lon=-122&amp;zoom=16&amp;highway=residential</a></p>
<p>but the road returned is not residential, instead it's classified as "highway:track" how can I get the closest residential road when given gps coordinates?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reversegeolocation" rel="tag" title="see questions tagged &#39;reversegeolocation&#39;">reversegeolocation</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '18, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/4f6e295d4a3e0e24268e948e79eae3fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave4784&#39;s gravatar image" />
<p><span>Dave4784</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave4784 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65105" class="comments-container">
&#10;</div>
<div id="comment-tools-65105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65105-form-container" class="comment-form-container">
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

<span id="65155"></span>

<div id="answer-container-65155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65155-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim can't do it. It understands a couple of special phrases <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases</a> for points-of-interest type searches, but not road types. <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> might work for your use case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '18, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65155" class="comments-container">
&#10;</div>
<div id="comment-tools-65155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65155-form-container" class="comment-form-container">
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

