+++
type = "question"
title = "tcp flow control"
description = '''How can I see tcp slow-start flow control in the wireshark.. I transfer a file (100 M) between two computers on filezilla client/server to see how the window size increase but I didn&#x27;t see it .. what should I do ??'''
date = "2013-02-20T04:38:00Z"
lastmod = "2013-02-20T04:57:00Z"
weight = 18768
keywords = [ "tcp" ]
aliases = [ "/questions/18768" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp flow control](/questions/18768/tcp-flow-control)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18768-score" class="post-score" title="current number of votes">0</div><span id="post-18768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I see tcp slow-start flow control in the wireshark.. I transfer a file (100 M) between two computers on filezilla client/server to see how the window size increase but I didn't see it .. what should I do ??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/688380b09dfaccd7370d2840dd8727f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maher%20Moualla&#39;s gravatar image" /><p><span>Maher Moualla</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maher Moualla has no accepted answers">0%</span></p></div></div><div id="comments-container-18768" class="comments-container"></div><div id="comment-tools-18768" class="comment-tools"></div><div class="clear"></div><div id="comment-18768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18769"></span>

<div id="answer-container-18769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18769-score" class="post-score" title="current number of votes">0</div><span id="post-18769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Slow-start is not negotiated or explicitly exchanged between hosts. It is a host-internal back-off mechanism to not saturate the bandwidth.</p><p>The congestion window is therefor only known to the host and not transmitted over the network. The only way to "see" the slow-start control is by looking at the tcptrace Time Sequence graph (Statistics -&gt; TCP StreamGraph -&gt; Time-Sequence Graph tcptrace). It should have an exponential shape at first and then turn into a linear line (assuming no packet loss and constant RTT).</p><p>You can also see the mechanism by looking at the bytes_in_flight field. It will stay low at first and will exponentially increase for a while.</p><p>See also: <a href="http://en.wikipedia.org/wiki/Slow-start">http://en.wikipedia.org/wiki/Slow-start</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '13, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18769" class="comments-container"></div><div id="comment-tools-18769" class="comment-tools"></div><div class="clear"></div><div id="comment-18769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

