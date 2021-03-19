+++
type = "question"
title = "SSL decryption help?"
description = '''I&#x27;m having problems making SSL decryption work. I&#x27;m running wireshark 1.6.2 Compiled (64-bit) with GTK+ 2.24.6, with GLib 2.29.92, with libpcap 1.1.1, with libz 1.2.3.4, with POSIX capabilities (Linux), without libpcre, with SMI 0.4.8, with c-ares 1.7.4, with Lua 5.1, without Python, with GnuTLS 2.1...'''
date = "2012-07-02T03:41:00Z"
lastmod = "2012-07-02T05:55:00Z"
weight = 12365
keywords = [ "ssl" ]
aliases = [ "/questions/12365" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decryption help?](/questions/12365/ssl-decryption-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12365-score" class="post-score" title="current number of votes">0</div><span id="post-12365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having problems making SSL decryption work.</p><p>I'm running wireshark 1.6.2</p><pre><code>Compiled (64-bit) with GTK+ 2.24.6, with GLib 2.29.92, with libpcap 1.1.1, with
libz 1.2.3.4, with POSIX capabilities (Linux), without libpcre, with SMI 0.4.8,
with c-ares 1.7.4, with Lua 5.1, without Python, with GnuTLS 2.10.5, with Gcrypt
1.5.0, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Jul 27
2011 11:52:20), without AirPcap.
Running on Linux 3.0.0-20-generic, with libpcap version 1.1.1, with libz
1.2.3.4, GnuTLS 2.10.5, Gcrypt 1.5.0.</code></pre><p>I have a self signed certificate generated with java keytool. I have extracted and converted the private key with the help of <a href="http://rubenlaguna.com/wp/2007/06/29/inspecting-tomcat-https-connection-with-wireshark/index.html/">http://rubenlaguna.com/wp/2007/06/29/inspecting-tomcat-https-connection-with-wireshark/index.html/</a></p><p>I have updated wireshark preferences so I have:</p><pre><code>ssl.desegment_ssl_records: TRUE
ssl.desegment_ssl_application_data: TRUE
ssl.keys_list: 127.0.0.1,8443,http,/tmp/cert.rsa.key
ssl.debug_file: /tmp/ssl.log</code></pre><p>When starting the ssl.log file says:</p><pre><code>Private key imported: KeyID 96:8b:93:2b:cb:26:7e:d1:b1:1f:18:d0:22:ba:13:6b:...
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;8443&#39; filename &#39;/tmp/cert.rsa.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /tmp/cert.rsa.key successfully loaded.
association_add TCP port 8443 protocol http handle 0x7fa335b09560</code></pre><p>So it looks like the configuration is all OK</p><p>I capture a simple HTTP GET request, but it cannot decode the data. It recognises SSL as the protocol and offers "Follow SSL Stream", but all I get is 0 bytes in the resulting dialog.</p><p>Below is the rest of the ssl.log:</p><pre><code>dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0x7fa321c13d90 size 680
  conversation = 0x7fa321c13880, ssl_session = 0x7fa321c13d90
  record: offset = 0, reported_length_remaining = 180
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 175, ssl state 0x00
association_find: TCP port 41462 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 171 bytes, remaining 180
packet_from_server: is from server - FALSE
ssl_find_private_key server 127.0.0.1:8443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
  conversation = 0x7fa321c13880, ssl_session = 0x7fa321c13d90
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0xC011

dissect_ssl enter frame #8 (first time)
  conversation = 0x7fa321c13880, ssl_session = 0x7fa321c13d90
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
dissect_ssl enter frame #10 (first time)
  conversation = 0x7fa321c13880, ssl_session = 0x7fa321c13d90
  record: offset = 0, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 36, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 112 offset 5 length 12449696 bytes, remaining 41

dissect_ssl enter frame #12 (first time)
  conversation = 0x7fa321c13880, ssl_session = 0x7fa321c13d90
  record: offset = 0, reported_length_remaining = 47
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 36, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 172 offset 11 length 2369652 bytes, remaining 47

dissect_ssl enter frame #13 (first time)
  conversation = 0x7fa321c13880, ssl_session = 0x7fa321c13d90
  record: offset = 0, reported_length_remaining = 407
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 402, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 41462 found (nil)
association_find: TCP port 8443 found 0x7fa336522040</code></pre><p>I'm not sure why it says no decoder available?</p><p>What else am I missing???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '12, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/9986909d140083165a11b82070ca51b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregory_j_wilkins&#39;s gravatar image" /><p><span>gregory_j_wi...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregory_j_wilkins has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jul '12, 03:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-12365" class="comments-container"></div><div id="comment-tools-12365" class="comment-tools"></div><div class="clear"></div><div id="comment-12365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12366"></span>

<div id="answer-container-12366" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12366-score" class="post-score" title="current number of votes">1</div><span id="post-12366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gregory_j_wilkins has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>dissect_ssl3_hnd_srv_hello can't find cipher suite 0xC011</p></blockquote><p>Cipher suite 0xC011 (TLS_ECDHE_RSA_WITH_RC4_128_SHA) uses DH (Diffie Hellman) to generate the session key. Unfortunately, you cannot decrpyt that with Wireshark. Please configure your SSL client to use only cipher suites without DH.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '12, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12366" class="comments-container"><span id="12369"></span><div id="comment-12369" class="comment"><div id="post-12369-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt - that was it. I went to about:config, searched for SSL and then disabled anything with "DH" in the cipher name.</p></div><div id="comment-12369-info" class="comment-info"><span class="comment-age">(02 Jul '12, 05:55)</span> <span class="comment-user userinfo">gregory_j_wi...</span></div></div></div><div id="comment-tools-12366" class="comment-tools"></div><div class="clear"></div><div id="comment-12366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

