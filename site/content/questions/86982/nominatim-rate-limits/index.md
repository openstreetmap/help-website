+++
type = "question"
title = "Nominatim rate limits"
description = '''Hi! I&#x27;m looking to use Nominatim to rectify some addresses I have stored in my database. Problem is I have 66336 addresses to go through and don&#x27;t want to overload the API. The query doesn&#x27;t have to be fast, I plan to run it at midnight anyways, I&#x27;ve read stuff like &quot;No more than one request per sec...'''
date = "2023-03-24T19:58:00Z"
lastmod = "2023-07-10T18:53:00Z"
weight = 86982
keywords = [ "question", "api", "osm", "help", "nominatim" ]
aliases = [ "/questions/86982" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim rate limits](/questions/86982/nominatim-rate-limits)

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
<span id="post-86982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm looking to use Nominatim to rectify some addresses I have stored in my database. Problem is I have 66336 addresses to go through and don't want to overload the API. The query doesn't have to be fast, I plan to run it at midnight anyways, I've read stuff like "No more than one request per second." and "A maximum of 2,500 requests per day (this is a soft limit, but it's recommended to stay below it).". I'm fine with waiting more then a second per request but will I be ok to run through all my addresses? Edit: This process is a one off and won't need to happen again.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '23, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/1a5c982dc8825ee7594f38a8876576b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgeValleyeats&#39;s gravatar image" />
<p><span>GeorgeValley...</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgeValleyeats has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '23, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-86982" class="comments-container">
&#10;</div>
<div id="comment-tools-86982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86982-form-container" class="comment-form-container">
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

<span id="87468"></span>

<div id="answer-container-87468" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To answer my own question, yes it appears to be ok so long as you stay within those thresholds. I didn't do any testing with calls faster then one per second for an extended period but I did test whether 2,500 was a hard cap, it didn't appear to be so. I did choose to stay below that limit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '23, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/1a5c982dc8825ee7594f38a8876576b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgeValleyeats&#39;s gravatar image" />
<p><span>GeorgeValley...</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgeValleyeats has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87468" class="comments-container">
&#10;</div>
<div id="comment-tools-87468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87468-form-container" class="comment-form-container">
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

