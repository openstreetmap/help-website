+++
type = "question"
title = "Is the Nominatim Request Limit Done Automatically?"
description = '''Sorry for the noob question but apparently there is a limit of 1 request per second when using Nominatim. I&#x27;m using this through PHP. Would I have to manually limit requests to 1 per second or is this done automatically when sending a request through to the API? Thanks!'''
date = "2017-06-08T14:37:00Z"
lastmod = "2017-06-08T15:39:00Z"
weight = 56533
keywords = [ "api", "limit", "nominatim", "request", "php" ]
aliases = [ "/questions/56533" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is the Nominatim Request Limit Done Automatically?](/questions/56533/is-the-nominatim-request-limit-done-automatically)

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
<span id="post-56533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56533-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sorry for the noob question but apparently there is a limit of 1 request per second when using Nominatim. I'm using this through PHP. Would I have to manually limit requests to 1 per second or is this done automatically when sending a request through to the API?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '17, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/3445398f13d7704cdc6e8616794f30e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OJSS&#39;s gravatar image" />
<p><span>OJSS</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OJSS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56533" class="comments-container">
&#10;</div>
<div id="comment-tools-56533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56533-form-container" class="comment-form-container">
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

<span id="56534"></span>

<div id="answer-container-56534" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56534-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OJSS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to do that on your end. A simple <code>sleep(1);</code> in PHP after each API request already helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-56534" class="comments-container">
&#10;</div>
<div id="comment-tools-56534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56534-form-container" class="comment-form-container">
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

