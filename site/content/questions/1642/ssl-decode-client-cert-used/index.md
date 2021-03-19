+++
type = "question"
title = "ssl decode - client cert used?"
description = '''Hi. Today I was asked to verify that particular ssl transaction did NOT include the sending of a Client Cert. So I captured packets on the client and fed them into wireshark. The SSL decode showed Client Hello, Server Hello, Certificate (from the server), Server Hello Done, Client Key Exchange, Chan...'''
date = "2011-01-05T18:27:00Z"
lastmod = "2011-01-05T22:22:00Z"
weight = 1642
keywords = [ "ssl" ]
aliases = [ "/questions/1642" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ssl decode - client cert used?](/questions/1642/ssl-decode-client-cert-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. Today I was asked to verify that particular ssl transaction did NOT include the sending of a Client Cert. So I captured packets on the client and fed them into wireshark. The SSL decode showed Client Hello, Server Hello, Certificate (from the server), Server Hello Done, Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message and Application Data It did NOT show a Certificate sent by the Client (nor any dropped packets).<br />
</p><p>Am I correct in concluding that if a Client Cert was sent, Wireshark would have decoded it and displayed it as such??</p><p>Thx!</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '11, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span> </br></p></div></div><div id="comments-container-1642" class="comments-container"></div><div id="comment-tools-1642" class="comment-tools"></div><div class="clear"></div><div id="comment-1642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1644"></span>

<div id="answer-container-1644" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1644-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the server needs to ask for a client certificate with a "CertificateRequest" and then the client will have to answer with a "Certificate" message on its own.</p><p>But beware, this "Certificate" message from the client can also contain 0 certificates, which means the client does not have a certificate. When this happens, the server will reject the connection if it is configured to "Require" a certificate and accept the connection when the clientcertificate was "Optional".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '11, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1644" class="comments-container"><span id="1650"></span><div id="comment-1650" class="comment"><div id="post-1650-score" class="comment-score"></div><div class="comment-text"><p>Perfect! That makes sense, and I can now confidently assert that a Client Cert was neither requested nor sent.</p><p>thx!</p></div><div id="comment-1650-info" class="comment-info"><span class="comment-age">(06 Jan '11, 07:43)</span> feenyman99</div></div></div><div id="comment-tools-1644" class="comment-tools"></div><div class="clear"></div><div id="comment-1644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

