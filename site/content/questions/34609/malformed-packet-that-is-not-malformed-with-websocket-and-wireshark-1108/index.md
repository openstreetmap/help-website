+++
type = "question"
title = "Malformed packet (that is NOT malformed) with Websocket and Wireshark 1.10.8"
description = '''Hi there, I am working with a Webocket client that, via MQTT, sends a large payload (exactly 124,000 bytes) to an Active MQ 5.10.0 server. I am capturing the packets between the client and the MQTT server. The Pcap shows the following error client -&amp;gt; server when one attempts to unmask the Websock...'''
date = "2014-07-11T17:25:00Z"
lastmod = "2014-07-11T19:56:00Z"
weight = 34609
keywords = [ "malformedpacket", "websocket", "expertinfo" ]
aliases = [ "/questions/34609" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed packet (that is NOT malformed) with Websocket and Wireshark 1.10.8](/questions/34609/malformed-packet-that-is-not-malformed-with-websocket-and-wireshark-1108)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34609-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I am working with a Webocket client that, via MQTT, sends a large payload (exactly 124,000 bytes) to an Active MQ 5.10.0 server. I am capturing the packets between the client and the MQTT server.</p><p>The Pcap shows the following error client -&gt; server when one attempts to unmask the Websocket frame payload:</p><p>[Malformed Packet: WebSocket] Expert Info (Error/Malformed): Malformed Packet (Exception occurred) [Message: Malformed Packet (Exception occurred)] [Severity level: Error] [Group: Malformed]</p><p>However, the entire message successfully reaches the server. As I am testing publish/subscribe, and the client is also subscribed, the server echoes back the entire message and I can see all of the Websocket frames coming back. Further, the client reassembles the message, completely intact.</p><p>I have the zipped up Pcap (317Kb) as well as the zipped up test payload (1K).</p><p>Is there a place to upload those? The forum guidelines say attaching files &gt; 100K is not accepted.</p><p>Thank you in advance. Dan Smith Kaazing Global Support [email protected]</p></div><div id="question-tags" class="tags-container tags">malformedpacket websocket expertinfo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '14, 17:25</strong></p><img src="https://secure.gravatar.com/avatar/ed608b5f5de778509c6270ba6af695b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daniel_smith_kaazing&#39;s gravatar image" /><p>daniel_smith...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daniel_smith_kaazing has no accepted answers">0%</span></p></div></div><div id="comments-container-34609" class="comments-container"></div><div id="comment-tools-34609" class="comment-tools"></div><div class="clear"></div><div id="comment-34609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34610"></span>

<div id="answer-container-34610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34610-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please fill a bug report to <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> and attach your sample capture here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '14, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34610" class="comments-container"></div><div id="comment-tools-34610" class="comment-tools"></div><div class="clear"></div><div id="comment-34610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

