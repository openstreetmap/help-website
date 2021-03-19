+++
type = "question"
title = "Get Packet Length"
description = '''I was able to retrieve my packet data as an unsigned char* with gCharArray = tvb_get_string(tvb, 0, length);  but I have no idea how to determine what &#x27;length&#x27; SHOULD be. My message type does not include any size information unfortunately. I want to grab the data from position 0 to the end of the da...'''
date = "2011-07-26T12:28:00Z"
lastmod = "2011-07-26T12:47:00Z"
weight = 5277
keywords = [ "char", "tvb_get_string", "length", "array", "packet" ]
aliases = [ "/questions/5277" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get Packet Length](/questions/5277/get-packet-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5277-score" class="post-score" title="current number of votes">0</div><span id="post-5277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was able to retrieve my packet data as an unsigned char* with<br />
</p><pre><code>gCharArray = tvb_get_string(tvb, 0, length);</code></pre><p>but I have no idea how to determine what 'length' SHOULD be. My message type does not include any size information unfortunately. I want to grab the data from position 0 to the end of the data. How can I accomplish this?<br />
<br />
Thank you for your time,<br />
Brandon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-char" rel="tag" title="see questions tagged &#39;char&#39;">char</span> <span class="post-tag tag-link-tvb_get_string" rel="tag" title="see questions tagged &#39;tvb_get_string&#39;">tvb_get_string</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-array" rel="tag" title="see questions tagged &#39;array&#39;">array</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p><span>officialhopsof</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-5277" class="comments-container"></div><div id="comment-tools-5277" class="comment-tools"></div><div class="clear"></div><div id="comment-5277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5278"></span>

<div id="answer-container-5278" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5278-score" class="post-score" title="current number of votes">1</div><span id="post-5278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="officialhopsof has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am going to answer my own question,<br />
</p><pre><code>length = tvb_length(tvb);</code></pre><p>Sorry about that!<br />
Brandon</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p><span>officialhopsof</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-5278" class="comments-container"></div><div id="comment-tools-5278" class="comment-tools"></div><div class="clear"></div><div id="comment-5278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

