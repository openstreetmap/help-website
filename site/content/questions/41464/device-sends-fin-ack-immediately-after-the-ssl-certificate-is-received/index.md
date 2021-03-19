+++
type = "question"
title = "Device sends FIN, ACK immediately after the SSL certificate is received"
description = '''I am trying to establish an SSL Tunnel over TCP using a Lantronix Xport Pro network module. The trouble is that certain websites are no allowing the connection for some reason. If i simply try to open a a secure session against, say Paypal or Google, it works fine and I can send data via a serial st...'''
date = "2015-04-15T11:01:00Z"
lastmod = "2015-04-16T12:54:00Z"
weight = 41464
keywords = [ "reset", "ssl", "tunnel", "fin", "certificate" ]
aliases = [ "/questions/41464" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Device sends FIN, ACK immediately after the SSL certificate is received](/questions/41464/device-sends-fin-ack-immediately-after-the-ssl-certificate-is-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41464-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to establish an SSL Tunnel over TCP using a Lantronix Xport Pro network module.</p><p>The trouble is that certain websites are no allowing the connection for some reason. If i simply try to open a a secure session against, say Paypal or Google, it works fine and I can send data via a serial stream through the tunnel. (Note we do not have a web server).</p><p>The trouble comes when trying to connect to our servers which are based on the Microsoft Azure platform. We have a VIP address to use and it all looks fine and dandy, except i get the following sequence on wireshark:</p><p>---&gt; Server Hello, Certificate, Server Hello Done</p><p>---&gt; 42572→443 [FIN, ACK] Seq=65 Ack=716 Win=64240 Len=0</p><p>---&gt; 443→42572 [RST, ACK] Seq=716 Ack=66 Win=0 Len=0</p><p>It looks like the server is sending our local module a certificate and it immediately closes the tunnel before it even attempts a key exchange. We then receive a reset.</p><p>I cant visually see anything wrong with the certificate that the server has sent, and we have disabled the certificate validation for now.</p><p>Anyone have any idea what could be happening here? I am not in my area of expertise and have run out of ideas.</p></div><div id="question-tags" class="tags-container tags">reset ssl tunnel fin certificate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '15, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/a449a85a3ae4dd0722f9d8e4123ffdee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jihenderson&#39;s gravatar image" /><p>jihenderson<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jihenderson has no accepted answers">0%</span></p></div></div><div id="comments-container-41464" class="comments-container"></div><div id="comment-tools-41464" class="comment-tools"></div><div class="clear"></div><div id="comment-41464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41499"></span>

<div id="answer-container-41499" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41499-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Anyone have any idea what could be happening here?</p></blockquote><p>There are "typical" reasons why a client would reject a server certificate</p><ol><li>The client is unable to verify the whole cert chain, meaning it does not know the root CA cert and/or any of the intermediate CA certs</li><li>The client does not accept the cert, because the cert lifetime is invalid from the clients point of view. Possible reason: The date/time on the client is totally wrong (off by several months or years).</li><li>The client does access the server via <a href="https://x.x.x.x">https://x.x.x.x</a> (an IP address), but the common name of the cert contains a host name</li><li>The client is unable to process the cert, because the public key is too large (4096 or even 8192 bit)</li><li>The cert contains an X.509 extension that the client is unable to understand/process</li></ol><blockquote><p>and we have disabled the certificate validation for now.</p></blockquote><p>If this means, that the connection works after you've disabled cert validation, then I would rule out 4. and 5. The other items are still good troublemaker candidates.</p><p>Without a capture file AND more detailed information about the client system (date/time, cert store, ssl stack, etc.) it's impossible to predict which of the items is causing the problems.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '15, 12:55</p></div></div><div id="comments-container-41499" class="comments-container"><span id="41618"></span><div id="comment-41618" class="comment"><div id="post-41618-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for the reply. Very useful.</p><p>Certainly on the current certificate (1) is true, although I imagine it might have ok with a previous one as we were trying different things. What happens if the chain is incomplete?</p><p>(2) I don’t think this is a problem because there are other websites which are connecting properly which are out of date by several years – unless both ends are out of date by the same amount?! This i will check.</p><p>(3) Not sure about this. We are activating a tunnel directly with an IP address. The system has not yet resolved the http(s) part so I'm not sure it is relevant.</p><p>However I have seen in a few places that the common name in the certificate should not be related to the domain in any way. Not really sure why this is as the explanations I have seen don’t seem to make a whole load of sense as it is quite well defined in the certificate structure and would imagine it would be hard to confuse.</p><p>(4) Don’t think this is it. Seems to be RSA2048 which is not too unusual and i have other websites that this seems to be ok with.</p><p>(5) Now this is a good point. Our module client is a bit (very) picky when we have to upload a cert onto the module and the only thing that seems to work is a .PEM format. It didn’t like any of the .cer, .crt, .der formats. Could the module not understand a cert if in the wrong format for the server end? Sounds stupid as it means that it simply won’t connect to many common https sites?</p><p>If disabling cert checking rules out 4&amp;5, functionally that may be true, but I also think that it is not beyond belief that the module would at least try to read it, and if it cant…</p></div><div id="comment-41618-info" class="comment-info"><span class="comment-age">(21 Apr '15, 01:04)</span> jihenderson</div></div><span id="41626"></span><div id="comment-41626" class="comment"><div id="post-41626-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to attach a wireshark log on this forum?</p></div><div id="comment-41626-info" class="comment-info"><span class="comment-age">(21 Apr '15, 05:47)</span> jihenderson</div></div><span id="41627"></span><div id="comment-41627" class="comment"><div id="post-41627-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>A capture can be shared from a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc. and posting a link as a comment, or by editing your question.</p></div><div id="comment-41627-info" class="comment-info"><span class="comment-age">(21 Apr '15, 06:09)</span> grahamb ♦</div></div><span id="41649"></span><div id="comment-41649" class="comment"><div id="post-41649-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(1) What happens if the chain is incomplete?</p></blockquote><p>That depends on you SSL stack and it's configuration. I can't tell you, as I don't know the SSL stack and configuration of you Lantronix device!</p><blockquote><p>(3) We are activating a tunnel directly with an IP address. The system has not yet resolved the http(s) part so <strong>I'm not sure it is relevant</strong>.</p></blockquote><p>sounds relevant to me, because a web server cert usually does not have the IP address in it's common name. But again: If this is a problem or not depends solely on the SSL stack and it's configuration in the Lantronix device. Only the vendor will be able to help you with this.</p><blockquote><p>(4) Don’t think this is it. Seems to be RSA2048 which is not too unusual and i have other websites that this seems to be ok with.</p></blockquote><p>seems to be O.K. or are you sure it's O.K.??? ;-)</p><blockquote><p>(5) Could the module not understand a cert if in the wrong format for the server end?</p></blockquote><p>No, that's totally unrelated. After the cert is loaded into the server software, no matter in which format, it will send the same information, which is (basically) the signed public key with information to whom it belongs (common name) and how long it is valid. This information is called the cert ;-)</p><blockquote><p>but I also think that it is not beyond belief that the module would at least try to read it, and if it cant…</p></blockquote><p>I don't know. Only the vendor of that device will be able to answer that question.</p></div><div id="comment-41649-info" class="comment-info"><span class="comment-age">(21 Apr '15, 14:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-41499" class="comment-tools"></div><div class="clear"></div><div id="comment-41499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

