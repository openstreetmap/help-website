+++
type = "question"
title = "Server does not send ACK"
description = '''hi my server is connected to several clients. there is an expected packet I want to get from one of the clients to my application on the server, but I don&#x27;t get it. when I use wireshark, I see that this packet came from the client but there no ACK on this packet from the server. then, the client ret...'''
date = "2012-02-08T02:35:00Z"
lastmod = "2012-02-10T13:34:00Z"
weight = 8890
keywords = [ "ack", "server" ]
aliases = [ "/questions/8890" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server does not send ACK](/questions/8890/server-does-not-send-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8890-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi</p><p>my server is connected to several clients. there is an expected packet I want to get from one of the clients to my application on the server, but I don't get it. when I use wireshark, I see that this packet came from the client but there no ACK on this packet from the server. then, the client retransmit this packet again and again, but there is no ACK. if the send window of the server is full - is there any indication on this in wireshark? or - what can be the root cause for the above issue?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">ack server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '12, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/5973b9fe3c7233493a0b258f0b263b4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gln&#39;s gravatar image" /><p>gln<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gln has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '12, 02:36</p></div></div><div id="comments-container-8890" class="comments-container"><span id="8894"></span><div id="comment-8894" class="comment"><div id="post-8894-score" class="comment-score"></div><div class="comment-text"><p>Does the handshake to the server work properly ? Is the packet from the client, that does not arrive at the server a fullsized segment ?</p></div><div id="comment-8894-info" class="comment-info"><span class="comment-age">(08 Feb '12, 04:32)</span> Landi</div></div><span id="8910"></span><div id="comment-8910" class="comment"><div id="post-8910-score" class="comment-score"></div><div class="comment-text"><p>yes, the handshake works properly. I don't understand the second question - can you please add details how can I see it?</p></div><div id="comment-8910-info" class="comment-info"><span class="comment-age">(08 Feb '12, 11:50)</span> gln</div></div><span id="8917"></span><div id="comment-8917" class="comment"><div id="post-8917-score" class="comment-score"></div><div class="comment-text"><p>how big are those packets, which the server does not ACK and is there any packet which is acked at all except during 3-way-handshake?</p></div><div id="comment-8917-info" class="comment-info"><span class="comment-age">(09 Feb '12, 01:12)</span> Landi</div></div><span id="8918"></span><div id="comment-8918" class="comment"><div id="post-8918-score" class="comment-score"></div><div class="comment-text"><p>those packet are 20 size.. there is an acks in this connection for several minutes, but then there is no ack somehow</p></div><div id="comment-8918-info" class="comment-info"><span class="comment-age">(09 Feb '12, 01:56)</span> gln</div></div><span id="8925"></span><div id="comment-8925" class="comment"><div id="post-8925-score" class="comment-score"></div><div class="comment-text"><p>sounds to me like a device in between that does not forward packets to the server after a certain event (firewall?). If you see the packets outgoing from the client but not incoming at the server I'd look at devices in the middle capable of traffic filtering</p></div><div id="comment-8925-info" class="comment-info"><span class="comment-age">(09 Feb '12, 04:20)</span> Landi</div></div></div><div id="comment-tools-8890" class="comment-tools"></div><div class="clear"></div><div id="comment-8890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8957"></span>

<div id="answer-container-8957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8957-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Run a capture at the server side to ensure that the packets are arriving.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/b119c1795a1d51f2d7d0aa7af9c54a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dixglata&#39;s gravatar image" /><p>dixglata<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dixglata has no accepted answers">0%</span></p></div></div><div id="comments-container-8957" class="comments-container"></div><div id="comment-tools-8957" class="comment-tools"></div><div class="clear"></div><div id="comment-8957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

