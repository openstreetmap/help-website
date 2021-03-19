+++
type = "question"
title = "HTTP response not captured on a server capture even though received on the client"
description = '''I&#x27;m attempting to debug an issue where a iPhone client throws an error that seems to indicate the http response was not received when hitting my API. When comparing traffic of the bad case to the good ones I notice that even in the cases where this works for other clients my wireshark does not have ...'''
date = "2015-01-30T11:31:00Z"
lastmod = "2016-04-21T12:23:00Z"
weight = 39509
keywords = [ "misidentified", "http", "response", "missing" ]
aliases = [ "/questions/39509" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP response not captured on a server capture even though received on the client](/questions/39509/http-response-not-captured-on-a-server-capture-even-though-received-on-the-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39509-score" class="post-score" title="current number of votes">0</div><span id="post-39509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to debug an issue where a iPhone client throws an error that seems to indicate the http response was not received when hitting my API. When comparing traffic of the bad case to the good ones I notice that even in the cases where this works for other clients my wireshark does not have an HTTP response listed for the call in question and the request contains no "Response in Frame:" link. If I use the follow TCP stream I see the response. If I dig through the TCP entries I see a reassembled PDU with the HTTP 201 response and the appropriate JSON payload. But there is no HTTP capture entry showing the response. Again, this is a case in which the client was able to receive and process the response, but I wonder if it's pointing to some anomaly that could help explain the issue I'm seeing.</p><p>When I look at the logs from the failed test from the iPhone, the HTTP request entry contains a "Response in frame" link to an HTTP 204 No Content, which is not the correct response but is rather a response from a previous HTTP call in the same stream. This is reinforced by follow TCP stream feature which again properly shows the appropriate HTTP 201 response with the correct payload.</p><p>So my questions are these: 1) Is it normal for Wireshark to not log an HTTP response that was clearly sent? 2) Is it normal for Wireshark to misidentify the HTTP response in the "Reponse in frame" link? 3) Are these likely symptoms of my problem or simply artifacts of how http or wireshark works?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-misidentified" rel="tag" title="see questions tagged &#39;misidentified&#39;">misidentified</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/87099c1e52f00e197beb5d0911c0491e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bennoffsinger&#39;s gravatar image" /><p><span>bennoffsinger</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bennoffsinger has no accepted answers">0%</span></p></div></div><div id="comments-container-39509" class="comments-container"><span id="51845"></span><div id="comment-51845" class="comment"><div id="post-51845-score" class="comment-score"></div><div class="comment-text"><p>Did you ever get a response on this or figure out how to see the HTTP response code? I'm having the same problem, but I'm running over HTTPS so it becomes a little more complicated -- Wireshark isn't decoding the response packet, but it decoding the request packet.</p></div><div id="comment-51845-info" class="comment-info"><span class="comment-age">(21 Apr '16, 12:23)</span> <span class="comment-user userinfo">Hossy923</span></div></div></div><div id="comment-tools-39509" class="comment-tools"></div><div class="clear"></div><div id="comment-39509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

