+++
type = "question"
title = "Matching HTTP traffic to TCP"
description = '''I&#x27;ve a hunt for an answer to this question but can&#x27;t find it... I&#x27;ve got a pcap for a webpage loading and I want to match the HTTP requests to TCP conversations The HTTP requests have a cookie that&#x27;s larger than the TCP segment size and I want to check whether the client is waiting for an ACK before...'''
date = "2012-11-16T08:16:00Z"
lastmod = "2012-11-16T08:16:00Z"
weight = 15969
keywords = [ "http", "tcp" ]
aliases = [ "/questions/15969" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Matching HTTP traffic to TCP](/questions/15969/matching-http-traffic-to-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15969-score" class="post-score" title="current number of votes">0</div><span id="post-15969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've a hunt for an answer to this question but can't find it...</p><p>I've got a pcap for a webpage loading and I want to match the HTTP requests to TCP conversations</p><p>The HTTP requests have a cookie that's larger than the TCP segment size and I want to check whether the client is waiting for an ACK before sending the rest of the HTTP request.</p><p>Can anyone advise how I do this or point me at a tutorial for it?</p><p><strong>EDIT</strong></p><p>OK made some progress, by finding the tcp.stream and filtering on it I can see all the packets on that stream.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '12, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/e3a42e29e189a1d4b1aade7c42dbb1e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Davies&#39;s gravatar image" /><p><span>Andy Davies</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Davies has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Nov '12, 08:33</strong> </span></p></div></div><div id="comments-container-15969" class="comments-container"></div><div id="comment-tools-15969" class="comment-tools"></div><div class="clear"></div><div id="comment-15969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

