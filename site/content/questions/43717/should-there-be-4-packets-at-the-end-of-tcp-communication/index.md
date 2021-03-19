+++
type = "question"
title = "Should there be 4 packets at the end of TCP communication?"
description = '''Everywhere I look, people say/write that at the end of TCP communication there should be four packets. First the client send FIN-ACK, and it is ACKed by the other side, then the server sends its own FIN-ACK and it&#x27;s also ACKed by the client. But when I look at the packet flow in wireshark, I always ...'''
date = "2015-06-30T03:43:00Z"
lastmod = "2015-06-30T03:55:00Z"
weight = 43717
keywords = [ "packets" ]
aliases = [ "/questions/43717" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Should there be 4 packets at the end of TCP communication?](/questions/43717/should-there-be-4-packets-at-the-end-of-tcp-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Everywhere I look, people say/write that at the end of TCP communication there should be four packets. First the client send <code>FIN-ACK</code>, and it is <code>ACK</code>ed by the other side, then the server sends its own <code>FIN-ACK</code> and it's also <code>ACK</code>ed by the client. But when I look at the packet flow in wireshark, I always see only three packets: <code>FIN-ACK</code>, <code>FIN-ACK</code>, <code>ACK</code>. Take a look at the following image:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2015-06-30-12:39:22_Selection.png" alt="alt text" /></p><p>Something's missing? Should there be 4 packets or everything is just fine?</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/95d5949e0a326d0c91c81f6565cafd1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morfik&#39;s gravatar image" /><p>morfik<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morfik has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43717" class="comments-container"></div><div id="comment-tools-43717" class="comment-tools"></div><div class="clear"></div><div id="comment-43717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43723"></span>

<div id="answer-container-43723" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43723-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 4way closing: fin - ack - fin - ack can be shortened to: fin- fin, ack - ack</p><hr /><p>You can find detailed Information here: <a href="http://www.rfc-editor.org/rfc/rfc793.txt" title="RFC793">RFC 793</a> hint: <code>Figure 13</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jun '15, 05:25</p></div></div><div id="comments-container-43723" class="comments-container"><span id="43725"></span><div id="comment-43725" class="comment"><div id="post-43725-score" class="comment-score"></div><div class="comment-text"><p>Could you provide some link that can cast more light on this subject?</p></div><div id="comment-43725-info" class="comment-info"><span class="comment-age">(30 Jun '15, 04:16)</span> morfik</div></div><span id="43728"></span><div id="comment-43728" class="comment"><div id="post-43728-score" class="comment-score"></div><div class="comment-text"><p>See <a href="http://www.tcpipguide.com/free/t_TCPConnectionTermination.htm">TCP Connection Termination</a>.</p></div><div id="comment-43728-info" class="comment-info"><span class="comment-age">(30 Jun '15, 05:51)</span> Jaap ♦</div></div><span id="43742"></span><div id="comment-43742" class="comment"><div id="post-43742-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, in the link you gave, there's a normal closing and the simultaneous one. There's no info concerning the missing <code>ACK</code> packet.</p></div><div id="comment-43742-info" class="comment-info"><span class="comment-age">(30 Jun '15, 11:24)</span> morfik</div></div><span id="43744"></span><div id="comment-43744" class="comment"><div id="post-43744-score" class="comment-score"></div><div class="comment-text"><p>At the RFC Figure 13 it is included. Figure 12 is telling the theoretical function and figure 13 tells you the practical one.</p><pre><code>It is also possible to terminate the connection by a 3-way handshake, when host A sends a FIN and host B replies with a FIN &amp; ACK (merely combines 2 steps into one) and host A replies with an ACK.[12] This is perhaps the most common method.</code></pre><p>This sentence I had taken from here: <a href="https://en.wikipedia.org/wiki/Transmission_Control_Protocol">https://en.wikipedia.org/wiki/Transmission_Control_Protocol</a></p></div><div id="comment-43744-info" class="comment-info"><span class="comment-age">(30 Jun '15, 11:46)</span> Christian_R</div></div><span id="43781"></span><div id="comment-43781" class="comment"><div id="post-43781-score" class="comment-score"></div><div class="comment-text"><p>@Christian_R , now I get it!</p></div><div id="comment-43781-info" class="comment-info"><span class="comment-age">(01 Jul '15, 06:07)</span> morfik</div></div></div><div id="comment-tools-43723" class="comment-tools"></div><div class="clear"></div><div id="comment-43723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

