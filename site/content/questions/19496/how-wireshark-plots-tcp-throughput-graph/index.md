+++
type = "question"
title = "How Wireshark plots TCP throughput graph?"
description = '''Dear wireshark experts, could you help me to understand one thing? I did perfomance test with iperf. During test I collected dump on iperf client side. My question is: Which formula is used by Wireshark for creating TCP throughput graph?  According to wireshark, avarege RTT value of TCP stream is 0,...'''
date = "2013-03-14T05:18:00Z"
lastmod = "2013-03-21T06:39:00Z"
weight = 19496
keywords = [ "throughput", "tcp" ]
aliases = [ "/questions/19496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How Wireshark plots TCP throughput graph?](/questions/19496/how-wireshark-plots-tcp-throughput-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19496-score" class="post-score" title="current number of votes">1</div><span id="post-19496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear wireshark experts, could you help me to understand one thing? I did perfomance test with iperf. During test I collected dump on iperf client side. My question is: Which formula is used by Wireshark for creating TCP throughput graph? According to wireshark, avarege RTT value of TCP stream is 0,04 sec and TCP window (on server) is stable and equal 2048K bytes But in this case Bandwidth of TCP stream should be around 400 Mbps (TCPwindow / RTT). Real test bandwidth result (and Wireshark also shows this) is 61,2 Mbps</p><p>Thanks in advance, Alex.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/aa1b61765b73fc5b18abbacced95ed0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="p007229667&#39;s gravatar image" /><p><span>p007229667</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="p007229667 has no accepted answers">0%</span></p></div></div><div id="comments-container-19496" class="comments-container"></div><div id="comment-tools-19496" class="comment-tools"></div><div class="clear"></div><div id="comment-19496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19707"></span>

<div id="answer-container-19707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19707-score" class="post-score" title="current number of votes">0</div><span id="post-19707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Iperf client and server itself should tell you the throughput details.</p><p>Can you provide details of what MTU you used? what's your Window size ? and also tell me if you tried in single direction or bi-direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/2fd4419ad615504ce0ad00bcbc0a0cd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kaasi&#39;s gravatar image" /><p><span>Kaasi</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kaasi has no accepted answers">0%</span></p></div></div><div id="comments-container-19707" class="comments-container"></div><div id="comment-tools-19707" class="comment-tools"></div><div class="clear"></div><div id="comment-19707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

