+++
type = "question"
title = "Wireshark cannot decrypt https traffic"
description = '''Hi all, I&#x27;m using Wireshark 1.12.3, I can decode https traffic before (a few weeks ago) but now I cannot anymore. This is debug log file : debug.txt I tried to search google and this site, I find some stuffs but they didn&#x27;t work, some topic said: Wireshark is only able to decrypt SSL when the full f...'''
date = "2015-02-09T19:48:00Z"
lastmod = "2015-02-10T00:12:00Z"
weight = 39735
keywords = [ "https" ]
aliases = [ "/questions/39735" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark cannot decrypt https traffic](/questions/39735/wireshark-cannot-decrypt-https-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39735-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm using Wireshark 1.12.3, I can decode https traffic before (a few weeks ago) but now I cannot anymore. This is debug log file : <a href="http://textuploader.com/64k4">debug.txt</a></p><p>I tried to search google and this site, I find some stuffs but they didn't work, some topic said:</p><pre><code>Wireshark is only able to decrypt SSL when the full first SSL handshake is available (&quot;Client Hello&quot; with Session-ID = 0) --&gt; How to check ?
The Key-Exchange should be RSA (not DHE or ECDHE) --&gt; How to check ?
SSL: &quot;Reassemble SSL records spanning multiple TCP segments&quot; should be enabled --&gt; yes
TCP: &quot;Allow subdissectors to reassemble TCP streams&quot; should also be enabled --&gt; yes</code></pre><p>the full SSL handshake needs to be present in the trace so that the proper keys can be extracted. A reused SSL session (with a short handshake) does not provide the keying material and can therefor only be decrypted when the original full handshake is also present in the tracefile. --&gt; how to check ?</p><p>Then, as Jaap mentioned, when a DH cipher is used, the keying material is exchanged using the Diffie Hellman protocol which uses dynamically created keypairs instead of the server's public and private key. Therefor Wireshark is not able to decrypt these sessions. --&gt; how to check ?</p><p>My webserver : Centos 6.4 64 bit. I tried to capture by wireshark on Windows client or tcpdump on server and many way but it still not works. Please let me know if you need more information.</p></div><div id="question-tags" class="tags-container tags">https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '15, 19:48</strong></p><img src="https://secure.gravatar.com/avatar/b54edb144a2f152c6b3fe8e69caa0d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack%20Chuong&#39;s gravatar image" /><p>Jack Chuong<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack Chuong has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Feb '15, 20:01</p></div></div><div id="comments-container-39735" class="comments-container"></div><div id="comment-tools-39735" class="comment-tools"></div><div class="clear"></div><div id="comment-39735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39740"></span>

<div id="answer-container-39740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39740-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From your SSL debug log:</p><pre><code>ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt</code></pre><p>So, your session is using a DH cipher. You can see that for yourself when you look at the ServerHello message and then look at the cipher that was chosen. You can also determine this by seeing a "ServerKeyExchange" in the SSL session setup, you won't see a ServerKeyExchange in a RSA key negotiation.</p><p>If you want to know if your session is using a full SSL handshake, check whether there is a "Certificate" and "ClientKeyExchange" handshake message in the SSL session that you are looking at. If not, it's using a cached session. You can then check the SSL Session ID in the ServerHello message to see which session it was and look for other sessions in the tracefile with the same session ID. If one of these (the first one) does have a "Certificate" and "ClientKeyExchange" handshake message, then wireshark is able to decrypt all sessions with this session ID, if not, you're out of luck as the full SSL handshake was not captured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39740" class="comments-container"><span id="39750"></span><div id="comment-39750" class="comment"><div id="post-39750-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit, thank you for your reply.</p><p>I looked into SeverHello message and find out that Cipher Suite : TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xc013).</p><p>How can I remove cached session and make my server and client to establish a full SSL handshake with RSA key negotiation ?</p></div><div id="comment-39750-info" class="comment-info"><span class="comment-age">(10 Feb '15, 02:35)</span> Jack Chuong</div></div><span id="40778"></span><div id="comment-40778" class="comment"><div id="post-40778-score" class="comment-score"></div><div class="comment-text"><p>I made it work. As SYN-bit said, the reason because my server and client use DH cipher to exchange key, I should config my server to use RSA cipher to exchange key. with Apache : SSLCipherSuite RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS Now I can decrypt https traffic.</p></div><div id="comment-40778-info" class="comment-info"><span class="comment-age">(23 Mar '15, 02:28)</span> Jack Chuong</div></div></div><div id="comment-tools-39740" class="comment-tools"></div><div class="clear"></div><div id="comment-39740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

