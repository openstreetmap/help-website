+++
type = "question"
title = "Using OSM for application having high request rate."
description = '''I have included OSM in my application using leaflet. I have used it similar to how the code snippet is written on leaflet&#x27;s home page https://leafletjs.com/. Map is loading great. My application has high request rate of around 40k requests per day. I want to know does the OSM put any restrictions on...'''
date = "2019-01-07T20:14:00Z"
lastmod = "2019-01-07T20:34:00Z"
weight = 67494
keywords = [ "usage" ]
aliases = [ "/questions/67494" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using OSM for application having high request rate.](/questions/67494/using-osm-for-application-having-high-request-rate)

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
<span id="post-67494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67494-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have included OSM in my application using leaflet. I have used it similar to how the code snippet is written on leaflet's home page <a href="https://leafletjs.com/">https://leafletjs.com/</a>. Map is loading great.</p>
<p>My application has high request rate of around 40k requests per day. I want to know does the OSM put any restrictions on how much requests its server can receive. If I launch OSM maps for my application will it work fine given the requests the application will make to load OSM map tiles. If there are any issues in this way, then how can I use OSM for my application.</p>
<p>I don't want to run into an issue where maps fail to load in my application due to some sort of throttling or requests exceeding the threshold (not sure whether that can happen). That's why need to confirm on the same.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '19, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ffa6330d1a05769b6a64a7c13f0e8182?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Amit_&#39;s gravatar image" />
<p><span>_Amit_</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Amit_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67494" class="comments-container">
&#10;</div>
<div id="comment-tools-67494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67494-form-container" class="comment-form-container">
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

<span id="67496"></span>

<div id="answer-container-67496" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67496-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-67496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM's data is free for you to use, but OSM's tile servers are not. See <a href="https://operations.osmfoundation.org/policies/tiles/">this policy</a> for details. If you want to render your own tiles, you can follow <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">these instructions</a>. Lots of companies also offer OSM-based tile layers; you might find it more cost effective to buy something from them.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '19, 20:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67496" class="comments-container">
&#10;</div>
<div id="comment-tools-67496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67496-form-container" class="comment-form-container">
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

