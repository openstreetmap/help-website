+++
type = "question"
title = "TCP out of sequence on HTTP POST"
description = '''Hi, I am having an intermittent issue where sometimes an HTTP POST to my proxy server results in a 405, Invalid Method response. After capturing both a successful and unsuccessful POST I have noted the following. Both captures start with a normal 3-way handshake. After this they diverge.  The succes...'''
date = "2015-10-27T21:42:00Z"
lastmod = "2015-10-27T23:00:00Z"
weight = 47003
keywords = [ "post", "http", "tcp" ]
aliases = [ "/questions/47003" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP out of sequence on HTTP POST](/questions/47003/tcp-out-of-sequence-on-http-post)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47003-score" class="post-score" title="current number of votes">0</div><span id="post-47003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am having an intermittent issue where sometimes an HTTP POST to my proxy server results in a 405, Invalid Method response. After capturing both a successful and unsuccessful POST I have noted the following.</p><p>Both captures start with a normal 3-way handshake. After this they diverge.</p><p>The successful one is as follows:</p><ol><li>Sequence number 1, Segment Length 1380, Next Sequence Number 1381 Flags ACK - This packet contains the HTTP POST request method</li><li>Sequence Number 1381, Segment Length 134, Next Sequence Number 1515, Flags PSH,ACK</li><li>Sequence Number 1515, Segment Length 1380, Next Sequence Number 2895, Flags ACK</li><li>Sequence Number 2895, Segment Length 357, Next Sequence Number 3252, Flags PSH, ACK</li></ol><p>The stream which results in the 405 has these same three frames with the sequence order reversed. i.e:</p><ol><li>Sequence number 1, Segment Length 1380, Next Sequence Number 1381, Flags ACK</li><li>Sequence Number 1381, Segment Length 357, Next Sequence Number 1738, Flags PSH,ACK</li><li>Sequence number 1738, Segment Length 1380, Next Sequence Number 3118 Flags ACK - This packet contains the HTTP POST</li><li>Sequence number 3118, Segment Length 134, Next Sequence Number 3252, Flash PSH, ACK</li></ol><p>So it would seem to me that the TCP segments are being passed down out of order. Am I interpreting this correctly? It seems suspicious that there are two segments of exactly the same size (1380) with an ACK flag which are followed by the a second segment with a PSH flag. Each pair is correct, but the order of the pairs is wrong.</p><p>Why would this be happening?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '15, 21:42</strong></p><img src="https://secure.gravatar.com/avatar/7377b9ec854c402be011d3f806fef5b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeremy%20Hagan&#39;s gravatar image" /><p><span>Jeremy Hagan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeremy Hagan has no accepted answers">0%</span></p></div></div><div id="comments-container-47003" class="comments-container"><span id="47005"></span><div id="comment-47005" class="comment"><div id="post-47005-score" class="comment-score"></div><div class="comment-text"><p>Could You provide us a trace on a public accessible place?</p></div><div id="comment-47005-info" class="comment-info"><span class="comment-age">(27 Oct '15, 23:00)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-47003" class="comment-tools"></div><div class="clear"></div><div id="comment-47003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

