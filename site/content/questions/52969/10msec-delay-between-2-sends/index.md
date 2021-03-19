+++
type = "question"
title = "10msec delay between 2 sends"
description = '''We have a latency sensitive app wherein the receiver is waiting for two messages from the sender. Each Message size is ~500bytes and the application sends it within 1msec interval. The problem is that the receiver application sees these two messages 10msec apart which results in delays in our applic...'''
date = "2016-05-26T10:50:00Z"
lastmod = "2016-05-31T01:25:00Z"
weight = 52969
keywords = [ "tcp_nodelay", "nagle" ]
aliases = [ "/questions/52969" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [10msec delay between 2 sends](/questions/52969/10msec-delay-between-2-sends)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a latency sensitive app wherein the receiver is waiting for two messages from the sender. Each Message size is ~500bytes and the application sends it within 1msec interval. The problem is that the receiver application sees these two messages 10msec apart which results in delays in our application.</p><p>Digging further into the wireshark traces we see that on the sender side, the 2nd send message is not actually sent until the tcp.ack for the 1st message arrives (10msec later) which seems to be the root cause of the problem. Question is why would tcp wait for this ack and not send out the 2nd message immediately? We have set the “TCPNoDelay” option on the socket (and hence Nagle turned off) which seems like an obvious culprit, but it did not help.</p><p>This is the pattern we are trying to understand: Send, &lt;10msec&gt;, Ack, Send</p><p>I would think that with “TCPNoDelay” option set (and hence Nagle turned off) on the socket, assuming 10msec delayed Ack timer, the behavior should be:</p><p>Send, Send, &lt;10msec&gt;, Ack</p><p>Any ideas whats going on? Platform: Windows Server 2012 R2</p><p><a href="https://www.dropbox.com/s/ia33nml95njvtoe/bad_sender.pcapng?dl=0">WireSharkSendTraces</a></p><p><a href="https://www.dropbox.com/s/9a33qwyiju75h99/bad_receiver.pcapng?dl=0">WireSharkReceiverTraces</a></p></div><div id="question-tags" class="tags-container tags">tcp_nodelay nagle</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '16, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/ea02c3d8b6b5d3e83a7298001fa426d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shahankur11&#39;s gravatar image" /><p>shahankur11<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shahankur11 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 May '16, 11:00</p></div></div><div id="comments-container-52969" class="comments-container"></div><div id="comment-tools-52969" class="comment-tools"></div><div class="clear"></div><div id="comment-52969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="53038"></span>

<div id="answer-container-53038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53038-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In every packet the sender sends the Push bit is set, so the Application is saying I'm finished, I have no more data to send the receiver ACKs the packet and the sequence starts over. the result of this is that there is never more than 309 bytes in flight I.E one packets worth of data, if you deploy this application over a WAN then performance will be dismal to say the least. If the Application had more data to send the Push bit would not/should not be set. This is not a case of the sender waiting for the ACK to the first packet, it's the cause of the Push bit being sent in every packet indicating the application has flushed the buffer and has no more data to send at that point.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '16, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/6d1650215a2d36670ba82fb893f72c6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_F&#39;s gravatar image" /><p>Mike_F<br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_F has no accepted answers">0%</span></p></div></div><div id="comments-container-53038" class="comments-container"></div><div id="comment-tools-53038" class="comment-tools"></div><div class="clear"></div><div id="comment-53038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53049"></span>

<div id="answer-container-53049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53049-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure I agree with the answer of @Mike_F. Setting the PUSH flag when sending shouldn't make the senders' application or tcp stack wait for an ack before sending any more data, that depends on the window size.</p><p><a href="https://tools.ietf.org/html/rfc793">RFC 793</a> and the amplification in <a href="https://tools.ietf.org/html/rfc1122#page-82">RFC 1122</a> state that the PUSH flag informs a senders' tcp stack to send all buffered data immediately.</p><p>At the receiver, the PSH bit forces the TCP stack to immediately send data to the application and not wait for the application buffer to be filled before doing so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '16, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '16, 14:02</p></div></div><div id="comments-container-53049" class="comments-container"><span id="53053"></span><div id="comment-53053" class="comment"><div id="post-53053-score" class="comment-score"></div><div class="comment-text"><p>+1 to grahamb. The application is doing 2 sends, back-to-back without waiting for even the completions to fire. Each after each send the application calls flush buffer which probably sets the PSH flag. TCP Stack should not be waiting for Ack to come for the first send before sending the 2nd send out.</p></div><div id="comment-53053-info" class="comment-info"><span class="comment-age">(30 May '16, 10:38)</span> shahankur11</div></div><span id="53056"></span><div id="comment-53056" class="comment"><div id="post-53056-score" class="comment-score"></div><div class="comment-text"><p>Well the ACK of the data is delayed by 10 ms. But the next DATA packet after the ACK is received are delayed sometimes by around 80ms at client side. So this 80ms are part of your problem, too.</p><p>So it could be application related, too. Seems to be an interesting apllication sends data all the time but never gets back an ack at application level. So why do you wait between two data packets?</p><p>But nevertheless, here I found some links around nagle: <a href="http://www.speedguide.net/articles/windows-8-10-2012-server-tcpip-tweaks-5077">http://www.speedguide.net/articles/windows-8-10-2012-server-tcpip-tweaks-5077</a></p><p><a href="http://kb.globalscape.com/KnowledgebaseArticle10438.aspx">http://kb.globalscape.com/KnowledgebaseArticle10438.aspx</a></p></div><div id="comment-53056-info" class="comment-info"><span class="comment-age">(30 May '16, 12:16)</span> Christian_R</div></div><span id="53057"></span><div id="comment-53057" class="comment"><div id="post-53057-score" class="comment-score"></div><div class="comment-text"><p>Can you confirm that you don't run the server application on a virtual server?</p></div><div id="comment-53057-info" class="comment-info"><span class="comment-age">(30 May '16, 13:07)</span> sindy</div></div></div><div id="comment-tools-53049" class="comment-tools"></div><div class="clear"></div><div id="comment-53049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53063"></span>

<div id="answer-container-53063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53063-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is it due to slow start for TCP connection?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '16, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p>srinu_bel<br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div></div><div id="comments-container-53063" class="comments-container"></div><div id="comment-tools-53063" class="comment-tools"></div><div class="clear"></div><div id="comment-53063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

