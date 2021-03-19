+++
type = "question"
title = "HTTP requests/responses out of sequence"
description = '''Hi, I was recently looking at HTTP requests/responses made by the default web browser on an HTC Android smartphone and noticed some strange behaviour. When using Follow TCP Stream for HTTP traffic you normally see an HTTP request (e.g. GET) followed by the response repeated many times over. However ...'''
date = "2012-07-16T01:32:00Z"
lastmod = "2012-07-16T02:19:00Z"
weight = 12738
keywords = [ "follow", "http", "stream", "tcp", "sequence" ]
aliases = [ "/questions/12738" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [HTTP requests/responses out of sequence](/questions/12738/http-requestsresponses-out-of-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12738-score" class="post-score" title="current number of votes">0</div><span id="post-12738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was recently looking at HTTP requests/responses made by the default web browser on an HTC Android smartphone and noticed some strange behaviour. When using Follow TCP Stream for HTTP traffic you normally see an HTTP request (e.g. GET) followed by the response repeated many times over. However in this case I'm seeing 2 or 3 GETs together followed later by responses. I thought that HTTP communication on a given connection had to be sequential - a request followed by a response.</p><p>Is what I'm seeing a bug/feature of Wireshark attempting to assemble the TCP stream or is this genuinely happening? If it's real, how do responses get matched to the corresponding request?</p><p>Thanks in advance,</p><p>Colin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/ea47f0c4f9c42dbd902eb11880b99719?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ColinBaker&#39;s gravatar image" /><p><span>ColinBaker</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ColinBaker has no accepted answers">0%</span></p></div></div><div id="comments-container-12738" class="comments-container"></div><div id="comment-tools-12738" class="comment-tools"></div><div class="clear"></div><div id="comment-12738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12739"></span>

<div id="answer-container-12739" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12739-score" class="post-score" title="current number of votes">1</div><span id="post-12739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ColinBaker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your HTC is most likely usingHTTP pipelining, see <a href="http://en.wikipedia.org/wiki/HTTP_pipelining">http://en.wikipedia.org/wiki/HTTP_pipelining</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12739" class="comments-container"><span id="12740"></span><div id="comment-12740" class="comment"><div id="post-12740-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYN-bit, hadn't heard of that. Looks like the Android browser is one of the first to implement it.</p></div><div id="comment-12740-info" class="comment-info"><span class="comment-age">(16 Jul '12, 02:19)</span> <span class="comment-user userinfo">ColinBaker</span></div></div></div><div id="comment-tools-12739" class="comment-tools"></div><div class="clear"></div><div id="comment-12739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

