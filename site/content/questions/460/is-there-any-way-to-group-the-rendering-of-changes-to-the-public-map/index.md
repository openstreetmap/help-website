+++
type = "question"
title = "Is there any way to group the rendering of changes to the public map?"
description = '''When I look at the main public OSM map I often see patches where the map suddenly stops, where bits are missing or the ways don&#x27;t line up with each other between two tiles. This makes the map look pretty scrappy and unreliable - especially when demonstrating it to someone new to OSM. It is generally...'''
date = "2010-07-23T13:12:00Z"
lastmod = "2010-07-23T15:32:00Z"
weight = 460
keywords = [ "rendering" ]
aliases = [ "/questions/460" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there any way to group the rendering of changes to the public map?](/questions/460/is-there-any-way-to-group-the-rendering-of-changes-to-the-public-map)

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
<span id="post-460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-460-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I look at the main public OSM map I often see patches where the map suddenly stops, where bits are missing or the ways don't line up with each other between two tiles. This makes the map look pretty scrappy and unreliable - especially when demonstrating it to someone new to OSM.</p>
<p>It is generally caused when one tile has been re-rendered to show recent changes to the map, but a neighbouring tile has not yet been rendered and still shows the 'old' image.</p>
<p>It seems to me that map changes should be managed, so that a newly re-rendered tile is only ever published when each of its four adjacent tiles are either unchanged or have also been re-rendered and can be published to the tile server at the same time.</p>
<p>Has there ever been any attempt to coordinate changes to the rendered map like this? (or is there perhaps already a solution to this that I don't know about?)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '10, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '10, 13:25</strong> </span></p>
</div>
</div>
<div id="comments-container-460" class="comments-container">
&#10;</div>
<div id="comment-tools-460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-460-form-container" class="comment-form-container">
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

<span id="463"></span>

<div id="answer-container-463" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-463-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tiles are actually rendered on a 8x8 grid, so it's much rarer to have data changes noticeable in this way than it would be if the tiles were rendered individually. The more common problem is that your browser is caching individual tiles, and they expire at different times depending on when you first viewed them (along with other reasons that I won't go into here). So what you are seeing is a mixture of tiles of different ages, and a hard-refresh of your browser often cleans this up.</p>
<p>The larger 8x8 grids of tiles ("metatiles") are re-rendered when the data changes, so there is some implicit synchronisation between adjacent metatiles. When the tileserver is quiet all the rerendering can be completed within a few seconds, but at some times of the day the queue can grow long enough that adjacent metatiles are re-rendered at significantly different times (i.e. more than a few seconds apart). However, this has a much smaller effect than the browser-caching that I've previously described.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '10, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-463" class="comments-container">
&#10;</div>
<div id="comment-tools-463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-463-form-container" class="comment-form-container">
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

