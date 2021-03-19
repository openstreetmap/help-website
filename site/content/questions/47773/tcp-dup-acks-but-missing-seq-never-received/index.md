+++
type = "question"
title = "TCP Dup Acks, but missing Seq never received"
description = '''Hi, I am connecting to the internet from a test laptop into a Layer 2 Epipe onto an internet facing router. For the most part, TCP application traffic is flowing correctly and all applications are working as expected - with one exception. When I attempt to download software updates from the internet...'''
date = "2015-11-19T11:46:00Z"
lastmod = "2015-11-19T11:56:00Z"
weight = 47773
keywords = [ "dup-ack" ]
aliases = [ "/questions/47773" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dup Acks, but missing Seq never received](/questions/47773/tcp-dup-acks-but-missing-seq-never-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47773-score" class="post-score" title="current number of votes">0</div><span id="post-47773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am connecting to the internet from a test laptop into a Layer 2 Epipe onto an internet facing router.</p><p>For the most part, TCP application traffic is flowing correctly and all applications are working as expected - with one exception.</p><p>When I attempt to download software updates from the internet (Microsoft, Adobe etc.), I can see the initial 3-way handshake complete and the download begins. However, part of the way through the download, a single random TCP sequence number is not received on the end host - although a wireshark on the internet facing router shows it is being sent towards the end host.</p><p>The end host sends multiple DUP ACKs requesting the missing sequence number, and the internet router shows it being retransmitted towards the end host several more times - but it never arrives and end host ultimately sends a TCP RST.</p><p>Is this as simple as the "missing" segment being dropped en route from the internet router towards the end host (via the L2 Epipe)? If so, any thoughts on why it would be so specific - why only when downloading updates, and why pick one specific segment to continually drop part way through the download? Scratching my head here......</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/25633f42be08818d87a6b956d0646a00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gtop81&#39;s gravatar image" /><p><span>gtop81</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gtop81 has no accepted answers">0%</span></p></div></div><div id="comments-container-47773" class="comments-container"></div><div id="comment-tools-47773" class="comment-tools"></div><div class="clear"></div><div id="comment-47773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47775"></span>

<div id="answer-container-47775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47775-score" class="post-score" title="current number of votes">0</div><span id="post-47775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this as simple as the "missing" segment being dropped en route from the internet router towards the end host (via the L2 Epipe)?</p></blockquote><p>according to your description, I would say: yes.</p><blockquote><p>why only when downloading updates, and why pick one specific segment to continually drop part way through the download? Scratching my head here......</p></blockquote><p>Maybe something in the downloader frame(s) triggers 'something' (security device) within the epipe infrastructure. Or it's a misconfigured QoS setting on a device in the epipe infrastructure that 'kills' the session (by dropping frames) because it reached a QoS limit.</p><p>Without insight, we can only guess.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47775" class="comments-container"></div><div id="comment-tools-47775" class="comment-tools"></div><div class="clear"></div><div id="comment-47775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

