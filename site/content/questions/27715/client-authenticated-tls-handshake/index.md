+++
type = "question"
title = "Client-authenticated TLS handshake"
description = '''Hi guys, I am trying to connect to a public webservice, which requires from its clients to have their own certificate. The whole communication is secure. So I think we could talk about the Client-authenticated TLS handshake. The certificate is installed on the machine (Local Computer and User). It i...'''
date = "2013-12-03T07:37:00Z"
lastmod = "2013-12-04T03:44:00Z"
weight = 27715
keywords = [ "tlsv1", "handshake", "authentication" ]
aliases = [ "/questions/27715" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Client-authenticated TLS handshake](/questions/27715/client-authenticated-tls-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I am trying to connect to a public webservice, which requires from its clients to have their own certificate. The whole communication is secure. So I think we could talk about the Client-authenticated TLS handshake.</p><p>The certificate is installed on the machine (Local Computer and User). It is verified from a CA. But it seems to me, that the client does not send any client certificate, I have tried it in a browser and programatically:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_4.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tlsv1 handshake authentication</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/676f5760248f2e1bbe1f9e56d65ebf1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thespycry&#39;s gravatar image" /><p>thespycry<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thespycry has no accepted answers">0%</span></p></img></div></div><div id="comments-container-27715" class="comments-container"></div><div id="comment-tools-27715" class="comment-tools"></div><div class="clear"></div><div id="comment-27715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27755"></span>

<div id="answer-container-27755" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27755-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>OK the question is, why isn't the server requesting the certificate ? what reason could it have?</p></blockquote><p>The server <strong>does</strong> request a certificate, which you can see with a display filter (ssl.handshake.type == 13), in the Info column of the Server Hello (Certificate Request) or with OpenSSL.</p><pre><code>C:\tools\openssl\bin&gt;openssl s_client -connect awp.statistik.at:443 -state
Loading &#39;screen&#39; into random state - done
CONNECTED(0000074C)
SSL_connect:before/connect initialization
SSL_connect:SSLv2/v3 write client hello A
SSL_connect:SSLv3 read server hello A
depth=3 C = ZA, ST = Western Cape, L = Cape Town, O = Thawte Consulting cc, OU
 CA, emailAddress = [email protected]
verify error:num=19:self signed certificate in certificate chain
verify return:0
SSL_connect:SSLv3 read server certificate A
SSL_connect:SSLv3 read server certificate request A
SSL_connect:SSLv3 read server done A</code></pre><p><strong>HOWEVER</strong>: Your request is sent through a Proxy (CONNECT method used). If that is a 'simple' proxy, than it would be no problem to forward the client cert request to the browser. If you don't see the client cert request in the capture file (ssl.handshake.type == 13), then your proxy is (most certainly) intercepting SSL/TLS connections to scan the content, which is quite common in corporate environments. In that case it is impossible/hard to forward the client cert request to the client. The 'better' proxy products (means more expensive) do offer a workaround for this problem. On those devices you can store a client cert (plus key) and the proxy will answer the client cert request on behalf of the client, with the stored credentials.</p><p>Please ask your proxy admin:</p><ul><li>if SSL interception is turned on (I'm pretty sure, as the server sends a client cert request)</li><li>if it is possible to let the proxy answer the client cert request on behalf of the client</li></ul><p>If your proxy is not able to handle client cert requests, there are two workarounds</p><ul><li>Configure the proxy to <strong>not intercept</strong> connections to awp.statistik.at</li><li>Configure your client to <strong>not use</strong> the proxy for connections to awp.statistik.at. However, then you need a rule in your firewall, that allows the connection directly.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '13, 03:47</p></div></div><div id="comments-container-27755" class="comments-container"><span id="27758"></span><div id="comment-27758" class="comment"><div id="post-27758-score" class="comment-score"></div><div class="comment-text"><p>alright, so if I understand correctly, we see the cert request from server while using the openssl command, because we are on the one side of the ssl 'tunnel'. We do not see it with wireshark, because we are only intercepting a ssl connection. So, YES, the server always sends the client cert request, but it does not come through the proxy so it seems, like the server isn't asking.</p></div><div id="comment-27758-info" class="comment-info"><span class="comment-age">(04 Dec '13, 04:20)</span> thespycry</div></div><span id="27760"></span><div id="comment-27760" class="comment"><div id="post-27760-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>we see the cert request from server while using the openssl command,</p></blockquote><p>erm... no. <strong>I</strong> can see the client cert request, because I am accessing the target server via the internet, <strong>without proxy</strong>.</p><blockquote><p>We do not see it with wireshark, because we are only intercepting a ssl connection.</p></blockquote><p>Yes. And, if you would have used openssl in <strong>your environment</strong>, you would not see it due to the assumed proxy behavior.</p><blockquote><p>So, YES, the server always sends the client cert request,</p></blockquote><p>I don't know if it <strong>always</strong> sends the request, but it did in my tests.</p><blockquote><p>but it does not come through the proxy so it seems, like the server isn't asking.</p></blockquote><p>Yes.</p><p>If you check the certificate of the server in the browser. What do you see as issuer (Certificate Authority)? If you see something related to your corporate proxy, then you know the SSL traffic was intercepted. I'm pretty sure it is, as the Server Hello in your screenshot looks totally different than in my tests.</p></div><div id="comment-27760-info" class="comment-info"><span class="comment-age">(04 Dec '13, 05:30)</span> Kurt Knochner ♦</div></div><span id="27761"></span><div id="comment-27761" class="comment"><div id="post-27761-score" class="comment-score"></div><div class="comment-text"><p>Yes, you are right, in the Server Hello Message, there are 2 Certificates: one is asp.statistik.at and the other one is our organisation name. The issuer of the statistik.at is our organization. ! Man you are so much helpful.. Thank you really much !! :)</p></div><div id="comment-27761-info" class="comment-info"><span class="comment-age">(04 Dec '13, 05:42)</span> thespycry</div></div><span id="27762"></span><div id="comment-27762" class="comment"><div id="post-27762-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The issuer of the statistik.at is our organization. !</p></blockquote><p>there you have it! ;-)</p><blockquote><p>Man you are so much helpful.. Thank you really much !!</p></blockquote><p>you're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-27762-info" class="comment-info"><span class="comment-age">(04 Dec '13, 05:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27755" class="comment-tools"></div><div class="clear"></div><div id="comment-27755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27719"></span>

<div id="answer-container-27719" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27719-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see a "Certificate Request" sent by the server therfore the client doesn't send its certificate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-27719" class="comments-container"><span id="27745"></span><div id="comment-27745" class="comment"><div id="post-27745-score" class="comment-score"></div><div class="comment-text"><p>OK the question is, why isn't the server requesting the certificate ? what reason could it have?</p></div><div id="comment-27745-info" class="comment-info"><span class="comment-age">(04 Dec '13, 00:05)</span> thespycry</div></div></div><div id="comment-tools-27719" class="comment-tools"></div><div class="clear"></div><div id="comment-27719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

