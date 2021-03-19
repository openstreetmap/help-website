+++
type = "question"
title = "HTTP/2 traffic decryption without SSLKEYLOGFILE"
description = '''So I found a lot of information about decrypting HTTP/2 traffic in Chrome and Firefox via the sslkeylogfile, which works fine. But what if I want to decrypt traffic in other browsers like Safari, Edge, Opera or browsers on mobile phones? Is there a way to do it? Do they have an sslkeylogfile or anyt...'''
date = "2016-08-04T04:32:00Z"
lastmod = "2016-08-05T06:27:00Z"
weight = 54575
keywords = [ "http2.0" ]
aliases = [ "/questions/54575" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP/2 traffic decryption without SSLKEYLOGFILE](/questions/54575/http2-traffic-decryption-without-sslkeylogfile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54575-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I found a lot of information about decrypting HTTP/2 traffic in Chrome and Firefox via the sslkeylogfile, which works fine.</p><p>But what if I want to decrypt traffic in other browsers like Safari, Edge, Opera or browsers on mobile phones? Is there a way to do it? Do they have an sslkeylogfile or anything similar?</p><p>For testing purposes I set up my own (apache) webserver, that means I have the server's certificate and the private key available.</p><p>When I try to decrypt traffic with wireshark using the private key it won't work. I found out it has to do with the diffie hellman key exchange.</p><p>From my understanding there is no way to use encrypted HTTP/2 without diffie hellman key exchange (please correct me if I'm wrong). At least when I disabled the diffie hellman ciphers in the apache ssl.conf, the server would only communicate via HTTP/1.1 but not HTTP/2</p><p>I'm not really experienced with ssl encryption, diffie hellman and it's vulnerabilities. Might a man in the middle attack be an option?</p><p>Since it is a webserver that is only used for testing with no connection to the internet, security concerns are not really an issue.</p><p>I just want to use wireshark to analyse HTTP/2 traffic of as many different browsers as possible.</p><p>So any help is highly appreciated.</p></div><div id="question-tags" class="tags-container tags">http2.0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '16, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/8906e209d9348c4b01e9126bc7317e24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Megastaine&#39;s gravatar image" /><p>Megastaine<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Megastaine has no accepted answers">0%</span></p></div></div><div id="comments-container-54575" class="comments-container"></div><div id="comment-tools-54575" class="comment-tools"></div><div class="clear"></div><div id="comment-54575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54613"></span>

<div id="answer-container-54613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54613-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Recent versions of Opera are based on Chromium and are supposed to work with the SSL keylog file too. Edge and Safari probably do not work with it. Not to mention smartphones where it is even more difficult to get the keys from.</p><p>In theory a MITM proxy should be possible, but these are often specific for HTTP as application data protocol. An example of a generic, protocol-agnostic "proxy" is <a href="http://www.dest-unreach.org/socat/doc/socat.html#ADDRESS_OPENSSL_CONNECT">socat</a> which you can start with:</p><pre><code>socat OPENSSL-LISTEN:443,fork,certificate=some.crt,key=some.key OPENSSL:your.host:port</code></pre><p>Combined with a <a href="http://security.stackexchange.com/q/80158/2630">utility to extract keys from OpenSSL applications</a>, this allows you to create a SSL keylog file. There are probably other tools that can do the same, but this shows the basic idea, proxy and dump keys.</p><p>Since you control the webserver you have more flexibility since security is not a concern:</p><ul><li>Change the <a href="https://httpd.apache.org/docs/current/mod/mod_ssl.html#sslciphersuite">SSLCipherSuite</a> directive in Apache to use non-DH ciphers. For example, you can specify <code>AES128-SHA</code>. This way, you can actually use the RSA private key file in Wireshark.</li><li>Use a debugger to extract keys from OpenSSL in Apache into a SSL keylog file. (See the utility mentioned above.)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-54613" class="comments-container"></div><div id="comment-tools-54613" class="comment-tools"></div><div class="clear"></div><div id="comment-54613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

