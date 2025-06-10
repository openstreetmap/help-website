+++
type = "question"
title = "Tile rendering queue limit?"
description = '''As you can see on http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_queue.html the rendering queue always peaks at 1k entries. Why is that and what happens with further submissions to the queue if it is already on limit?'''
date = "2011-03-19T13:56:00Z"
lastmod = "2011-03-25T11:36:00Z"
weight = 3909
keywords = [ "queue", "rendering", "tiles", "renderd" ]
aliases = [ "/questions/3909" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tile rendering queue limit?](/questions/3909/tile-rendering-queue-limit)

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
<span id="post-3909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3909-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As you can see on <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_queue.html">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/renderd_queue.html</a> the rendering queue always peaks at 1k entries. Why is that and what happens with further submissions to the queue if it is already on limit?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-queue" rel="tag" title="see questions tagged &#39;queue&#39;">queue</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '11, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/aa89e8e008c7920f96a759f481dd04a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bot47&#39;s gravatar image" />
<p><span>bot47</span><br />
<span class="score" title="236 reputation points">236</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bot47 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '11, 11:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-3909" class="comments-container">
&#10;</div>
<div id="comment-tools-3909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3909-form-container" class="comment-form-container">
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

<span id="3917"></span>

<div id="answer-container-3917" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3917-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bot47 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a compile-time limit built into renderd - the dirty queue has the 1k limit, and the request and priority-request queues have similar but much shorter limits.</p>
<p>The idea is that renderd can only render so many metatiles each second, and after a while the backlog can become so large that it's not really worth tracking any more tiles than are what is in the queue already.</p>
<p>If you request an old tile when the dirty queue is full, it's not added to the list that needs re-rendering. However, when the backlog is worked through and is no longer full, any further requests for the old tile triggers it being added to the queue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '11, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-3917" class="comments-container">
<span id="3934"></span>
<div id="comment-3934" class="comment">
<div id="post-3934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This means that if the queue is full some tiles will never get rendered?</p>
</div>
<div id="comment-3934-info" class="comment-info">
<span class="comment-age">(21 Mar '11, 08:15)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
<span id="3949"></span>
<div id="comment-3949" class="comment">
<div id="post-3949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"never" is the wrong word - if the queue is full it'll be added to the queue the next time it is viewed (so long as the queue isn't full at that point). That's what the last part of my answer says.</p>
</div>
<div id="comment-3949-info" class="comment-info">
<span class="comment-age">(21 Mar '11, 21:24)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="4067"></span>
<div id="comment-4067" class="comment">
<div id="post-4067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If it happens to you that I tile is not rendered properly, e.g. <a href="http://tile.openstreetmap.org/7/63/42.png">http://tile.openstreetmap.org/7/63/42.png</a> was, you can check its status by appending /status to the URI or /dirty to force rerendering. E.g. <a href="http://tile.openstreetmap.org/7/63/42.png/dirty">http://tile.openstreetmap.org/7/63/42.png/dirty</a></p>
</div>
<div id="comment-4067-info" class="comment-info">
<span class="comment-age">(25 Mar '11, 11:36)</span> <span class="comment-user userinfo">bot47</span>
</div>
</div>
</div>
<div id="comment-tools-3917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3917-form-container" class="comment-form-container">
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

