+++
type = "question"
title = "Remote decryption TLS in wireshark"
description = '''I want to know if it is possible to do remote decryption with wireshark ? A more structured approach to what I want to do is this - Setup: 2 computers (comp A and comp B) with one computer acting as a network gateway. That is all traffic from comp A goes to comp B. Any firewall rules set on comp B a...'''
date = "2016-11-01T11:02:00Z"
lastmod = "2016-11-01T13:05:00Z"
weight = 56910
keywords = [ "tls", "decryption", "ssl_decrypt", "remote", "ssl" ]
aliases = [ "/questions/56910" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Remote decryption TLS in wireshark](/questions/56910/remote-decryption-tls-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56910-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know if it is possible to do remote decryption with wireshark ?</p><p>A more structured approach to what I want to do is this -</p><p>Setup: 2 computers (comp A and comp B) with one computer acting as a network gateway. That is all traffic from comp A goes to comp B. Any firewall rules set on comp B applies to comp A.</p><p>Objective: Generate the TLS secrets on a local PC (comp A) and then send the secrets to comp B (via file transer/ssh/nc). Comp B should be able to decrypt encrypted traffic given the TLS secret information (the actual 6 keys generated from master secret).</p><p>Current Approach - Print out the TLS secrets/ SSLdecoder variable in a file using a modified version of wireshark. Send this file to comp B via netcat/ssh. On comp B, use a modified version of wireshark to read these secrets and decrypt data.</p><p>Problems: There is a delay in sending the secrets from comp A to comp B. As a result the decryption code on wireshark runs before the secrets are sent by comp A. That is the packets are already captured and dissected by wireshark on comp B as when I browse a website on comp A. There is a manual delay for sending TLS secrets to comp B</p><p>Question: Is there a way to solve this problem without tweaking anything at comp A side (one tweak is adding delay in sending packets at network level to comp B)</p><p>Why this problem: I am trying to study security for fine grained proxies. Here comp A is a local PC and comp B is a proxy. Instead of using certificates, now only specific TLS sessions can be decrypted by the proxy with some secrets</p></div><div id="question-tags" class="tags-container tags">tls decryption ssl_decrypt remote ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '16, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/c28011fe6d6c690149158e45cf811175?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mac9393&#39;s gravatar image" /><p>mac9393<br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mac9393 has no accepted answers">0%</span></p></div></div><div id="comments-container-56910" class="comments-container"></div><div id="comment-tools-56910" class="comment-tools"></div><div class="clear"></div><div id="comment-56910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56916"></span>

<div id="answer-container-56916" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56916-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is your "modified version" of Wireshark? Wireshark already supports linking session secrets to a SSL/TLS session using the "(Pre-)master secrets keylog file" approach (see <a href="https://wiki.wireshark.org/SSL#Using_the_.28Pre.29-Master-Secret">Wireshark wiki - SSL</a>). This method will also suffer from the same problem though. When the keylog file entry is added after the Client Key Exchange message has been dissected, there will be no more attempts to load the secrets.</p><p>A possible idea is to delay dissection of the Client Key Exchange record type until the keylog file has gained a session secret for the Random value from the Client Hello. This requires either modification to the SSL dissector or a custom dissector that is invoked before the SSL dissector (and interprets the record layer first).</p><p>Sketch of the approach:</p><ul><li>Use <code>ssl_get_session()</code> to obtain the SSL session.</li><li>If <code>session-&gt;state &amp; SSL_CLIENT_RANDOM</code>, then assume that the Client Hello handshake record (used for identification purposes) is found.</li><li>If <code>SSL_CLIENT_RANDOM</code> was set, but neither <code>SSL_HAVE_SESSION_KEY</code> nor <code>SSL_MASTER_SECRET</code> are set, then try to locate the session secret in the keylog file (in the <code>ssl_crandom_hash</code> hash table). If it was not found, then:</li><li>Try to dissect the current <code>tvb</code> yourself and see if it is is a Change Cipher Spec message. If it is, keep polling the key log file (possibly up to some maximum time) until the Client Random is found.</li><li>Invoke the normal SSL dissection code (hopefully it will succeed now in loading the key).</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56916" class="comments-container"></div><div id="comment-tools-56916" class="comment-tools"></div><div class="clear"></div><div id="comment-56916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56913"></span>

<div id="answer-container-56913" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56913-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you want to consider a different approach. <a href="http://www.ieeelcn.org/lcn41demos/Erlacher.pdf">This</a> is an interesting article about the subject. <a href="http://www.telerik.com/fiddler">Fiddler</a> is a well known tool, as is <a href="https://mitmproxy.org">MitM Proxy</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56913" class="comments-container"><span id="56914"></span><div id="comment-56914" class="comment"><div id="post-56914-score" class="comment-score"></div><div class="comment-text"><p>The article is really related to this project. However, I would like to use TLS encryption keys instead of the master secret/certificate to decrypt info by the proxies.</p></div><div id="comment-56914-info" class="comment-info"><span class="comment-age">(01 Nov '16, 12:50)</span> mac9393</div></div></div><div id="comment-tools-56913" class="comment-tools"></div><div class="clear"></div><div id="comment-56913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

