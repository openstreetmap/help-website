+++
type = "question"
title = "Certificate Verify Message"
description = '''Experts, The last message sent from a client in an SSL handshake with client certificate authentication is the Certificate Verify message.  Here are my questions. How is the Certificate Verify message constructed in an SSL Handshake?  How does a server validate the Certificate Verify message? The in...'''
date = "2015-06-29T09:30:00Z"
lastmod = "2015-06-29T09:58:00Z"
weight = 43671
keywords = [ "certificates", "ssl", "authentication" ]
aliases = [ "/questions/43671" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Certificate Verify Message](/questions/43671/certificate-verify-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43671-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Experts,</p><p>The last message sent from a client in an SSL handshake with client certificate authentication is the Certificate Verify message.</p><p>Here are my questions.</p><p><strong>How is the Certificate Verify message constructed in an SSL Handshake?</strong></p><p><strong>How does a server validate the Certificate Verify message?</strong></p><p>The information I have found is from the SSL 3.0 RFC.</p><p><a href="https://tools.ietf.org/html/rfc6101#section-5.6.8">https://tools.ietf.org/html/rfc6101#section-5.6.8</a></p><p>From my understanding, this is how the Certificate Verify is constructed and validated.</p><ol><li>2 seperate SHA1 and MD5 hashes are generated from Client Hello and Server Hello Messages.</li><li>A digest is generate with the hashed data and the Private Key associated with the client certificate sent to the server in previous messages.</li><li>The server validates the Certificate Verify by calculating a digest using the client certificate and a hash of the Client Hello and Server Hello messages.</li><li>If the verification is successful from the server's perspective, then the client is authenticated.</li></ol><p>If an SSL proxy exists between the client and the server, then this could break client certificate authentication. This is because the hashed data that is generated from the Client Hello and Server Hello would be different.</p><p>Any corrections on my understanding and guidance on client certificate authentication is appreciated.</p><p>Thanks for the help in advance.</p><p>Brooks</p></div><div id="question-tags" class="tags-container tags">certificates ssl authentication</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '15, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/422421655ff2e126be7341dcce9345e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brooks&#39;s gravatar image" /><p>Brooks<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brooks has no accepted answers">0%</span></p></div></div><div id="comments-container-43671" class="comments-container"><span id="43674"></span><div id="comment-43674" class="comment"><div id="post-43674-score" class="comment-score"></div><div class="comment-text"><p>Not really a Wireshark question, more a TLS\SSL one. You should ask your question in a more suitable forum.</p></div><div id="comment-43674-info" class="comment-info"><span class="comment-age">(29 Jun '15, 09:46)</span> grahamb ♦</div></div></div><div id="comment-tools-43671" class="comment-tools"></div><div class="clear"></div><div id="comment-43671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43676"></span>

<div id="answer-container-43676" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43676-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://tools.ietf.org/html/rfc7568">SSL 3.0 must not be used</a>, refer to <a href="https://tools.ietf.org/html/rfc5246.html#section-7.4.8">RFC 5246 (TLS 1.2) - 7.4.8. Certificate Verify</a> for a more up-to-date specification.</p><h2 id="how-is-the-certificate-verify-message-constructed-in-an-ssl-handshake">How is the Certificate Verify message constructed in an SSL Handshake?</h2><p>The Certificate Verify message is constructed by the client. It contains the signed hash of the handshake messages.</p><p><a href="https://tools.ietf.org/html/rfc5246.html#section-7.4.8">RFC 5246, section 7.4.8</a> about the handshake messages:</p><blockquote><p>handshake_messages refers to all handshake messages sent or received, starting at client hello and up to, but not including, this message, including the type and length fields of the handshake messages. This is the concatenation of all the Handshake structures (as defined in <a href="https://tools.ietf.org/html/rfc5246.html#section-7.4">Section 7.4</a>) exchanged thus far.</p></blockquote><p><a href="https://tools.ietf.org/html/rfc5246.html#section-4.7">RFC 5246, section 4.7</a> describes the digitally-signed attribute, <a href="https://tools.ietf.org/html/rfc5246.html#section-7.4.1.4.1">section 7.4.1.4.1</a> describes the available signature types. Basically you will have this form:</p><pre><code>    SignatureAndHashAlgorithm algorithm, consisting of:
        HashAlgorithm hash (4 for SHA-256 for example)
        SignatureAlgorithm signature (1 for RSA for example)
    Signature (a byte stream for a RSA signature for example)</code></pre><h2 id="how-does-a-server-validate-the-certificate-verify-message">How does a server validate the Certificate Verify message?</h2><p>The server will buffer the handshake messages and should then obtain the same hash as the one supplied by the client. In order to authenticate the hash, the server must validate the signature.</p><p>This can be done by using the public key from the certificate that was provided by the client in the <a href="https://tools.ietf.org/html/rfc5246.html#section-7.4.6">Client Certificate</a> handshake message.</p><p>A MitM SSL proxy can indeed not authenticate itself against the server since it does not posess the client key and therefore cannot sign the parameters exchanged in the handshake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-43676" class="comments-container"><span id="43678"></span><div id="comment-43678" class="comment"><div id="post-43678-score" class="comment-score"></div><div class="comment-text"><p><a href="https://tools.ietf.org/html/rfc7568">RFC 7568</a> deprecates SSL 3.0 and requires it to not be used.</p></div><div id="comment-43678-info" class="comment-info"><span class="comment-age">(29 Jun '15, 10:20)</span> grahamb ♦</div></div><span id="43679"></span><div id="comment-43679" class="comment"><div id="post-43679-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Right, SSL 3.0 is deprecated and RFC 7568 ("ssl3.0 die die die") forbids its use (the first sentence of this answer links to that).</p></div><div id="comment-43679-info" class="comment-info"><span class="comment-age">(29 Jun '15, 10:23)</span> Lekensteyn</div></div><span id="43684"></span><div id="comment-43684" class="comment"><div id="post-43684-score" class="comment-score"></div><div class="comment-text"><p>Ah, I missed that it was a link, hence my post.</p></div><div id="comment-43684-info" class="comment-info"><span class="comment-age">(29 Jun '15, 13:14)</span> grahamb ♦</div></div><span id="43802"></span><div id="comment-43802" class="comment"><div id="post-43802-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation!</p></div><div id="comment-43802-info" class="comment-info"><span class="comment-age">(01 Jul '15, 19:28)</span> Brooks</div></div></div><div id="comment-tools-43676" class="comment-tools"></div><div class="clear"></div><div id="comment-43676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

