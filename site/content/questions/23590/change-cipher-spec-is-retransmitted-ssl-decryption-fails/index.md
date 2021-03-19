+++
type = "question"
title = "Change Cipher Spec is retransmitted. SSL Decryption fails."
description = '''Hello, I have the following case: I am trying to decrypt the communication between a client and a web server. I have the private key and I have setup wireshark correctly since I an able to decrypt most of the traffic. However for I face the following issue: Messages from client to server are not dec...'''
date = "2013-08-06T06:24:00Z"
lastmod = "2015-10-12T03:51:00Z"
weight = 23590
keywords = [ "ssl" ]
aliases = [ "/questions/23590" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Change Cipher Spec is retransmitted. SSL Decryption fails.](/questions/23590/change-cipher-spec-is-retransmitted-ssl-decryption-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23590-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have the following case: I am trying to decrypt the communication between a client and a web server. I have the private key and I have setup wireshark correctly since I an able to decrypt most of the traffic. However for I face the following issue: Messages from client to server are not decrypted while messages from server to clients are decrypted correctly. I observed the following: When the client sends the Change Cipher Spec message to the server, initially this message reports as finished. Immediately this message is retransmitted and reports Encrypted Handshake Message.</p><pre><code>&quot;18749&quot;,&quot;11:58:13.246703000&quot;,&quot;170.186.153.151&quot;,&quot;167.16.161.16&quot;,&quot;TLSv1&quot;,&quot;163&quot;,&quot;Client Hello&quot;
&quot;18750&quot;,&quot;11:58:13.246718000&quot;,&quot;170.186.153.151&quot;,&quot;167.16.161.16&quot;,&quot;TLSv1&quot;,&quot;163&quot;,&quot;[TCP Retransmission] Client Hello&quot;
&quot;18758&quot;,&quot;11:58:13.247513000&quot;,&quot;167.16.161.16&quot;,&quot;170.186.153.151&quot;,&quot;TLSv1&quot;,&quot;187&quot;,&quot;Server Hello, Change Cipher Spec, Finished&quot;
&quot;18759&quot;,&quot;11:58:13.248696000&quot;,&quot;170.186.153.151&quot;,&quot;167.16.161.16&quot;,&quot;TLSv1&quot;,&quot;101&quot;,&quot;Change Cipher Spec, Finished&quot;
&quot;18760&quot;,&quot;11:58:13.248707000&quot;,&quot;170.186.153.151&quot;,&quot;167.16.161.16&quot;,&quot;TLSv1&quot;,&quot;101&quot;,&quot;[TCP Retransmission] Change Cipher Spec, Encrypted Handshake Message&quot;
&quot;18762&quot;,&quot;11:58:13.252905000&quot;,&quot;170.186.153.151&quot;,&quot;167.16.161.16&quot;,&quot;TLSv1&quot;,&quot;622&quot;,&quot;Application Data&quot;
&quot;18763&quot;,&quot;11:58:13.252952000&quot;,&quot;170.186.153.151&quot;,&quot;167.16.161.16&quot;,&quot;TLSv1&quot;,&quot;622&quot;,&quot;[TCP Retransmission] Application Data&quot;
&quot;18766&quot;,&quot;11:58:13.253584000&quot;,&quot;167.16.161.16&quot;,&quot;170.186.153.151&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;https &gt; 60406 [ACK] Seq=1784558668 Ack=207907348 Win=64245 Len=0&quot;
&quot;18777&quot;,&quot;11:58:13.259411000&quot;,&quot;167.16.161.16&quot;,&quot;170.186.153.151&quot;,&quot;TCP&quot;,&quot;1434&quot;,&quot;[TCP segment of a reassembled PDU]&quot;
&quot;18778&quot;,&quot;11:58:13.259473000&quot;,&quot;167.16.161.16&quot;,&quot;170.186.153.151&quot;,&quot;HTTP&quot;,&quot;820&quot;,&quot;HTTP/1.1 200 OK  (GIF89a) (GIF89a) (image/gif)&quot;</code></pre><p>I think that this may cause my problems. Can you please provide some assistance?</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '13, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/4abc84b62f59c17f8252adc9dc9ff144?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="it_trb&#39;s gravatar image" /><p>it_trb<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="it_trb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '13, 08:59</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23590" class="comments-container"></div><div id="comment-tools-23590" class="comment-tools"></div><div class="clear"></div><div id="comment-23590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23593"></span>

<div id="answer-container-23593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like all outbound packets are captured twice causing wireshark to interpret them as 'retransmissions'. You need to look at the ip.id to see if it is a real retransmit or a duplicte packet. Telling from the delta time I assume it's the latter.</p><p>I suggest to run <code>editcap -d infile outfile'</code> and see if the retransmissions disapper.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '13, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-23593" class="comments-container"></div><div id="comment-tools-23593" class="comment-tools"></div><div class="clear"></div><div id="comment-23593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46466"></span>

<div id="answer-container-46466" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46466-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I experienced the same issue. A retransmitted "Change Cipher Spec" message (from server to client) causes the wrong decryption of all the TLS messages received at the client side. By ignoring the retransmitted CCS (Right Click -&gt; Ignore Packet (toggle) ) the decryption works fine for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '15, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/eca830854093757dbe9847c9d44241b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theo66&#39;s gravatar image" /><p>theo66<br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theo66 has one accepted answer">50%</span></p></div></div><div id="comments-container-46466" class="comments-container"><span id="46468"></span><div id="comment-46468" class="comment"><div id="post-46468-score" class="comment-score"></div><div class="comment-text"><p>That sounds like a bug. Could you raise a bug report at the <a href="https://bugs.wireshark.org">Wireshark bugzilla</a>, and attach a capture illustrating the problem so it can be fixed?</p></div><div id="comment-46468-info" class="comment-info"><span class="comment-age">(12 Oct '15, 09:23)</span> grahamb ♦</div></div><span id="46489"></span><div id="comment-46489" class="comment"><div id="post-46489-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately I can't attach my capture traces, however I don't think it's a bug. I discovered that by enabling the TCP option "Do not call subdissector for error packets" the TLS sessions are correctly decripted without the "hack" I mention before.</p></div><div id="comment-46489-info" class="comment-info"><span class="comment-age">(12 Oct '15, 23:32)</span> theo66</div></div></div><div id="comment-tools-46466" class="comment-tools"></div><div class="clear"></div><div id="comment-46466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

