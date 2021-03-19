+++
type = "question"
title = "Display few http responses with TCP information"
description = '''Hi, I have a trace file in which there are many HTTP requests and responses. All these requests and responses are in the same TCP connection. Of these different requests and responses I want to filter out a specific set of requests which has the string advert in the HTTP request. This can be done us...'''
date = "2014-07-04T04:56:00Z"
lastmod = "2014-07-07T00:23:00Z"
weight = 34406
keywords = [ "filter" ]
aliases = [ "/questions/34406" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display few http responses with TCP information](/questions/34406/display-few-http-responses-with-tcp-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34406-score" class="post-score" title="current number of votes">1</div><span id="post-34406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a trace file in which there are many HTTP requests and responses. All these requests and responses are in the same TCP connection. Of these different requests and responses I want to filter out a specific set of requests which has the string <em>advert</em> in the HTTP request. This can be done using <em>http.request.uri.contains</em> filter, but I want to visualize the entire TCP conversation only for these requests. Since it is the same stream as all other requests <em>tcp stream</em> filter doesn't do the job here. Is there another way to get this done?</p><p>Thanks, much appreciated!</p><p>/venky</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '14, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/51b8b3a1451c6552dc91862b68590758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="venky&#39;s gravatar image" /><p><span>venky</span><br />
<span class="score" title="24 reputation points">24</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="venky has no accepted answers">0%</span></p></div></div><div id="comments-container-34406" class="comments-container"><span id="34409"></span><div id="comment-34409" class="comment"><div id="post-34409-score" class="comment-score"></div><div class="comment-text"><p>Are you looking for a way to extract requests together with their responses?</p></div><div id="comment-34409-info" class="comment-info"><span class="comment-age">(04 Jul '14, 05:40)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="34414"></span><div id="comment-34414" class="comment"><div id="post-34414-score" class="comment-score"></div><div class="comment-text"><p>Yes, exactly, with the entire response stream for the requests which match.</p></div><div id="comment-34414-info" class="comment-info"><span class="comment-age">(04 Jul '14, 07:11)</span> <span class="comment-user userinfo">venky</span></div></div><span id="34425"></span><div id="comment-34425" class="comment"><div id="post-34425-score" class="comment-score"></div><div class="comment-text"><p>Duplicate of <a href="https://ask.wireshark.org/questions/30972/filter-the-response-to-a-matched-http-request">https://ask.wireshark.org/questions/30972/filter-the-response-to-a-matched-http-request</a></p></div><div id="comment-34425-info" class="comment-info"><span class="comment-age">(04 Jul '14, 14:59)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-34406" class="comment-tools"></div><div class="clear"></div><div id="comment-34406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34446"></span>

<div id="answer-container-34446" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34446-score" class="post-score" title="current number of votes">0</div><span id="post-34446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the answer. I came up with a different fix for the problem. I am just using packet numbers to create a filtered stream together with other filters which will filter the conversation between the host and the server. Of course the first few TCP segments from the client to server will contain acks for previous responses. Just looking at the sequence number of the request I can remove the unnecessary packets and voila...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '14, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/51b8b3a1451c6552dc91862b68590758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="venky&#39;s gravatar image" /><p><span>venky</span><br />
<span class="score" title="24 reputation points">24</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="venky has no accepted answers">0%</span></p></div></div><div id="comments-container-34446" class="comments-container"></div><div id="comment-tools-34446" class="comment-tools"></div><div class="clear"></div><div id="comment-34446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

