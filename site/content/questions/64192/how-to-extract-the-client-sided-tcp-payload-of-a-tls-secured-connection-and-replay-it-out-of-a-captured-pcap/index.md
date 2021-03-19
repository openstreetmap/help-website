+++
type = "question"
title = "How to extract the client-sided TCP-Payload of a TLS secured connection and replay it out of a captured pcap?"
description = '''Hello guys, I&#x27;m not much of an expert and I&#x27;m stuck. What I wanna do is:  I have a captured TCP stream in pcap I wanna separate Client and Server connection Extract the payload/Application Data (Not decrypt or stuff like that) And replay the extracted payload. For example with Packet Sender which is...'''
date = "2017-10-25T08:37:00Z"
lastmod = "2017-10-26T13:56:00Z"
weight = 64192
keywords = [ "pcap", "payload", "tcp" ]
aliases = [ "/questions/64192" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract the client-sided TCP-Payload of a TLS secured connection and replay it out of a captured pcap?](/questions/64192/how-to-extract-the-client-sided-tcp-payload-of-a-tls-secured-connection-and-replay-it-out-of-a-captured-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64192-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>I'm not much of an expert and I'm stuck. What I wanna do is:</p><ul><li>I have a captured TCP stream in pcap</li><li>I wanna separate Client and Server connection</li><li>Extract the payload/Application Data (<strong>Not decrypt or stuff like that</strong>)</li><li>And replay the extracted payload. For example with <strong>Packet Sender</strong> which is taking care of the connection sequence</li><li><em>If possible automatically, because there usually over 150 packets</em></li></ul><p>I don't wanna change the IP-Address necessarily.</p><p>I tried <code>tcpprep</code> to split the packets and <code>tcpwrite</code> create a new pcap file. But it didn't work out. The background behind all this, it is a research for my study program and I need to perform a replay attack.</p><p>If you could help me, it would be very sweet. Thx in advance....</p></div><div id="question-tags" class="tags-container tags">pcap payload tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '17, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/678a38555b4d90a481e3d2eb0849f0ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UserWire&#39;s gravatar image" /><p>UserWire<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UserWire has no accepted answers">0%</span></p></div></div><div id="comments-container-64192" class="comments-container"><span id="64244"></span><div id="comment-64244" class="comment"><div id="post-64244-score" class="comment-score"></div><div class="comment-text"><p>No one or is it too trivial??!</p></div><div id="comment-64244-info" class="comment-info"><span class="comment-age">(26 Oct '17, 09:56)</span> UserWire</div></div><span id="64248"></span><div id="comment-64248" class="comment"><div id="post-64248-score" class="comment-score"></div><div class="comment-text"><p>I don't understand when you say you want to extract the payload but not decrypt for replay. If you extract the encrypted payload you won't be able to replay that as the TLS handshake will fail.</p></div><div id="comment-64248-info" class="comment-info"><span class="comment-age">(26 Oct '17, 12:05)</span> grahamb ♦</div></div></div><div id="comment-tools-64192" class="comment-tools"></div><div class="clear"></div><div id="comment-64192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64257"></span>

<div id="answer-container-64257" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64257-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Handshake will be taken care of by the tool <em>Packet Sender</em>. It will manage the connection. I just need to fill the packets with the encrypted payload. Thats the big advantage of replay-attacks, unless there aren't any replay-countermeasures like sessionID or timestamps. You don't need any decryption, just the bitstream.</p><p><strong>Or am I wrong?!</strong> I presented this idea my Prof. and he didn't oppose to that, so I am a lil confused right now.</p><p>Thanks for your reply.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/678a38555b4d90a481e3d2eb0849f0ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UserWire&#39;s gravatar image" /><p>UserWire<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UserWire has no accepted answers">0%</span></p></div></div><div id="comments-container-64257" class="comments-container"></div><div id="comment-tools-64257" class="comment-tools"></div><div class="clear"></div><div id="comment-64257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

