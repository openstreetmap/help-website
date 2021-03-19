+++
type = "question"
title = "Listening to and decrypting SSL traffic with mitmproxy"
description = '''Hello, I have the following setup: An Android Emulator which uses mitmproxy on localhost:8080 and mitmproxy is intercepting the SSL traffic by providing a custom certificate. This works. That means I can follow and analyze the intercepted SSL traffic in the mitmproxy console. What I would like to do...'''
date = "2016-02-10T03:47:00Z"
lastmod = "2016-02-10T04:13:00Z"
weight = 50047
keywords = [ "mitmproxy", "mitm", "proxy", "wireshark" ]
aliases = [ "/questions/50047" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Listening to and decrypting SSL traffic with mitmproxy](/questions/50047/listening-to-and-decrypting-ssl-traffic-with-mitmproxy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50047-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have the following setup:</p><p>An Android Emulator which uses mitmproxy on localhost:8080 and mitmproxy is intercepting the SSL traffic by providing a custom certificate.</p><p>This works. That means I can follow and analyze the intercepted SSL traffic in the mitmproxy console.</p><p>What I would like to do now is to sniff the traffic between the Emulator and mitmproxy (which uses the spoof certificate) and then uses this certificate to decrypt the captured traffic.</p><p>The problem is that there are a couple of things I am uncertain of. For example how do I filter for that traffic? I tried <code>(ip.dst == 127.0.0.1 || ip.src == 127.0.0.1)</code> - but this does not contain any test requests via http but mostly small TCP packets.</p><p>The next question is: how do I have to configure the SSL Decrypt in Wireshark? (Edit / Preferences / Protocols / SSL / RSA keys list)</p><p>I am absolutely unsure as to what ...</p><ul><li>IP address</li><li>port</li><li>protocol</li><li>key file</li></ul><p>... to use.</p><p>In the mitmproxy certificates folder the following files are available:</p><ul><li>mitmproxy-ca-cert.cer</li><li>mitmproxy-ca-cert.p12</li><li>mitmproxy-ca-cert.pem</li><li>mitmproxy-ca.pem</li><li>mitmproxy-dhparam.pem</li></ul><hr /><p>I hope the question is not too long and confusing. I'll happily clarify if anything is unclear and am greatful for hints.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">mitmproxy mitm proxy wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '16, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/c44e61d34981ed01ab4bc25c3df52fc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raffael1984&#39;s gravatar image" /><p>Raffael1984<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raffael1984 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Feb '16, 03:47</p></div></div><div id="comments-container-50047" class="comments-container"></div><div id="comment-tools-50047" class="comment-tools"></div><div class="clear"></div><div id="comment-50047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50049"></span>

<div id="answer-container-50049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50049-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What I would like to do now is to sniff the traffic between the Emulator and mitmproxy (which uses the spoof certificate) and then uses this certificate to decrypt the captured traffic.</p><blockquote><p>For example how do I filter for that traffic [between the Emulator and mitmproxy]?</p></blockquote><p>You likely have to capture from the <a href="https://wiki.wireshark.org/CaptureSetup/Loopback">loopback interface</a>. Capturing from <code>127.0.0.1</code> on the LAN adapter is ineffective as packets never leave your machine via that interface.</p><blockquote><p>How do I have to configure the SSL Decrypt in Wireshark? (Edit / Preferences / Protocols / SSL / RSA keys list)</p></blockquote><p>See <a href="https://wiki.wireshark.org/SSL#SSL_dissection_in_Wireshark.">https://wiki.wireshark.org/SSL#SSL_dissection_in_Wireshark.</a> The IP, port and protocol fields are not that important. You could set for example <code>any</code>, <code>443</code> and <code>http</code> respectively.</p><p>According to the <a href="http://mitmproxy.org/doc/certinstall.html#docCertfiles">mitmproxy docs</a>, <code>mitmproxy-ca.pem</code> contains the private key for the CA, but these are only used to sign leaf certificates. The same page suggests that dummy certificates are generated on the fly. If these use the same key as the CA, then you can use the <code>mitmproxy-ca.pem</code> file as Key File.</p><p>It can be much easier though to configure SSL Key log files instead, see <a href="http://mitmproxy.org/doc/dev/sslkeylogfile.html">http://mitmproxy.org/doc/dev/sslkeylogfile.html</a> for instructions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '16, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-50049" class="comments-container"><span id="50053"></span><div id="comment-50053" class="comment"><div id="post-50053-score" class="comment-score"></div><div class="comment-text"><p>The loopback interface is not working. If I visit f.x. <a href="http://m.heise.de">http://m.heise.de</a> then (definitely) directly related packets are captured - but all of them are of type DNS and TCP handshakes. Otherwise I should be able to find HTML content by searching for text I see on the web site in the emulator (given that the communication is unencrypted in this example).</p></div><div id="comment-50053-info" class="comment-info"><span class="comment-age">(10 Feb '16, 07:23)</span> Raffael1984</div></div></div><div id="comment-tools-50049" class="comment-tools"></div><div class="clear"></div><div id="comment-50049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

