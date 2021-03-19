+++
type = "question"
title = "HTTPS over TLS - encrypted type"
description = '''Hi, How does wireshark recognizes: Handshake protocol: Encrypted Handshake message. From the rfc, it doesn&#x27;t seem to have this type? how can we recognize it from the bytes? Diana &amp;amp; Shahar'''
date = "2015-03-18T06:33:00Z"
lastmod = "2015-03-19T06:26:00Z"
weight = 40656
keywords = [ "ssl", "https" ]
aliases = [ "/questions/40656" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [HTTPS over TLS - encrypted type](/questions/40656/https-over-tls-encrypted-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40656-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>How does wireshark recognizes: Handshake protocol: Encrypted Handshake message. From the rfc, it doesn't seem to have this type? how can we recognize it from the bytes?</p><p>Diana &amp; Shahar</p></div><div id="question-tags" class="tags-container tags">ssl https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '15, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p>Dianalab9<br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Mar '15, 03:42</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-40656" class="comments-container"></div><div id="comment-tools-40656" class="comment-tools"></div><div class="clear"></div><div id="comment-40656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40681"></span>

<div id="answer-container-40681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40681-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark lists this as an "Encrypted Handshake" message because:</p><ol><li>It sees from the SSL record that it is a handshake message</li><li>The communication is encrypted, as "ChangeCipherSpec" indicates that the negtiated session keys will from that point on be used to encrypt the communication.</li></ol><p>When you tell Wireshark to do SSL decryption (by using the private key of the server), the message would have been decrypted and you would see that it is indeed one of the listed handshake messages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40681" class="comments-container"><span id="40682"></span><div id="comment-40682" class="comment"><div id="post-40682-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot!</p></div><div id="comment-40682-info" class="comment-info"><span class="comment-age">(19 Mar '15, 03:15)</span> Dianalab9</div></div></div><div id="comment-tools-40681" class="comment-tools"></div><div class="clear"></div><div id="comment-40681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40685"></span>

<div id="answer-container-40685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40685-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Handshake messages are encrypted after ChangeCipherSpec message with appropriate preceding parameters.</p><p>From <a href="https://tools.ietf.org/html/rfc5246.html#section-7.4">RFC 5246 (TLS 1.2), section 7.4. Handshake protocol</a>:</p><blockquote><p>The TLS Handshake Protocol is one of the defined higher-level clients of the TLS Record Protocol. This protocol is used to negotiate the secure attributes of a session. <strong>Handshake messages</strong> are supplied to the TLS record layer, where they are encapsulated within one or more TLSPlaintext structures, which are <strong>processed and transmitted as specified by the current active session state</strong>.</p></blockquote><p>The current state is described in <a href="https://tools.ietf.org/html/rfc5246.html#section-6.1">section 6.1. Connection states</a>:</p><blockquote><p>The security parameters for the pending states can be set by the TLS Handshake Protocol, and <strong>the ChangeCipherSpec can selectively make either of the pending states current</strong>, in which case the appropriate current state is disposed of and replaced with the pending state; the pending state is then reinitialized to an empty state. It is illegal to make a state that has not been initialized with security parameters a current state. <strong>The initial current state always specifies that no encryption</strong>, compression, or MAC will be used.</p></blockquote><p>In practice, you will see unencrypted Client Hello, Server Hello, Certificate, Server Key Exchange, Certificate Request, Certificate Verify and Client Key Exchange messages. The Finished handshake message is encrypted since it occurs after the Change Cipher Spec message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-40685" class="comments-container"><span id="44309"></span><div id="comment-44309" class="comment"><div id="post-44309-score" class="comment-score"></div><div class="comment-text"><p>Thank you. The above helped but we have one more question: We have a single frame that the beginning of it's SSL Bytes are (Hex) 16 03 03 00 40 01 ..... 16 - is content type HANDSHAKE 03 03 - version 00 40 - length 01 - message type 'Client Hello'</p><p>For some reason wireshark recognizes it as Encrypted Handshake Message. We assume wireshark is right but we don't understand how it recognizes it as Encrypted Handshake Message instead of Client Hello.</p><p>Can you please explain?</p></div><div id="comment-44309-info" class="comment-info"><span class="comment-age">(20 Jul '15, 02:27)</span> Dianalab9</div></div><span id="44310"></span><div id="comment-44310" class="comment"><div id="post-44310-score" class="comment-score"></div><div class="comment-text"><p>Does it really dissect said part as encrypted handshake message? ContentType 16 (=22, Handshake) and HandshakeType 1 (ClientHello) can actually be dissected. Got a packet capture that you can share?</p></div><div id="comment-44310-info" class="comment-info"><span class="comment-age">(20 Jul '15, 03:41)</span> Lekensteyn</div></div><span id="44322"></span><div id="comment-44322" class="comment"><div id="post-44322-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/handshake.JPG" alt="alt text" /></p></div><div id="comment-44322-info" class="comment-info"><span class="comment-age">(21 Jul '15, 05:12)</span> Dianalab9</div></div><span id="44323"></span><div id="comment-44323" class="comment"><div id="post-44323-score" class="comment-score"></div><div class="comment-text"><p>I've published below partial screen shot; can you take a look?</p></div><div id="comment-44323-info" class="comment-info"><span class="comment-age">(21 Jul '15, 05:13)</span> Dianalab9</div></div><span id="44384"></span><div id="comment-44384" class="comment"><div id="post-44384-score" class="comment-score"></div><div class="comment-text"><p>@Dianalab9 that screenshot is not helpful, it contains no additional information. Can you reproduce it with a recent Wireshark stable version, say, the 1.12.z series?</p></div><div id="comment-44384-info" class="comment-info"><span class="comment-age">(22 Jul '15, 11:54)</span> Lekensteyn</div></div></div><div id="comment-tools-40685" class="comment-tools"></div><div class="clear"></div><div id="comment-40685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40659"></span>

<div id="answer-container-40659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40659-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are talking about HTTP over TLS, so you should look for SSL.</p><p><code>TLS 1.0 (0x0301) TLS 1.1 (0x0302) TLS 1.2 (0x0303)</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></img></div></div><div id="comments-container-40659" class="comments-container"><span id="40662"></span><div id="comment-40662" class="comment"><div id="post-40662-score" class="comment-score"></div><div class="comment-text"><p>We've looked at this but it only has the following: case hello_request: HelloRequest; case client_hello: ClientHello; case server_hello: ServerHello; case certificate: Certificate; case server_key_exchange: ServerKeyExchange; case certificate_request: CertificateRequest; case server_hello_done: ServerHelloDone; case certificate_verify: CertificateVerify; case client_key_exchange: ClientKeyExchange; case finished: Finished;</p><p>How do we recognize: "Handshake protocol: Encrypted Handshake message"</p></div><div id="comment-40662-info" class="comment-info"><span class="comment-age">(18 Mar '15, 08:19)</span> Dianalab9</div></div><span id="40670"></span><div id="comment-40670" class="comment"><div id="post-40670-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to achieve? Do you want to filter only for packets that contain "Encrypted Handshake message" or do you want to write some script/program and you want to know how to identify it?</p></div><div id="comment-40670-info" class="comment-info"><span class="comment-age">(18 Mar '15, 12:29)</span> Roland</div></div></div><div id="comment-tools-40659" class="comment-tools"></div><div class="clear"></div><div id="comment-40659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

