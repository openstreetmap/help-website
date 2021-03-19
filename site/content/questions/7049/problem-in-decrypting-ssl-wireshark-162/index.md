+++
type = "question"
title = "Problem in decrypting SSL - Wireshark 1.6.2"
description = '''I am using the current newest version of Wireshark, 1.6.2. I wanted to decrypt an SSL connection. I entered the IP address, port, protocol and .key file in Preferences -&amp;gt; SSL correctly, but the packets are still not decrypted. I am using an Apache webserver, so the keys are all in .pem format. I ...'''
date = "2011-10-23T21:35:00Z"
lastmod = "2011-10-30T05:18:00Z"
weight = 7049
keywords = [ "ssl", "decrypt", "decryption" ]
aliases = [ "/questions/7049" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem in decrypting SSL - Wireshark 1.6.2](/questions/7049/problem-in-decrypting-ssl-wireshark-162)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7049-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the current newest version of Wireshark, 1.6.2. I wanted to decrypt an SSL connection. I entered the IP address, port, protocol and .key file in Preferences -&gt; SSL correctly, but the packets are still not decrypted. I am using an Apache webserver, so the keys are all in .pem format. I also tried converting the key and certificate to .pfx format and using it to decrypt, but to no avail. Here is the download link for the pcap capture file, server key, certificate and CSR (It's self-signed and it's only for private academic use so I'm fine sharing it): <a href="http://www.mediafire.com/?980y2vwedkf9r6r">http://www.mediafire.com/?980y2vwedkf9r6r</a> And I also started capturing packets in Wireshark even before I opened my web browser, so all the handshakes are captured (you can look at my pcap file)</p><p>Here is the debug file:</p><pre><code>ssl_association_remove removing TCP 443 - http handle 03454E58
ssl_parse: Can&#39;t load UAT string &quot;192.168.0.1&quot;,&quot;443&quot;,&quot;http&quot;,&quot;C:\server.key&quot;,&quot;&quot;: ssl_keys:1: File &#39;C:server.key&#39; does not exist or access is denied.
Private key imported: KeyID ef:d4:b1:da:f3:75:8d:a1:0f:37:87:7b:49:71:f8:2d:...
ssl_init IPv4 addr &#39;192.168.0.1&#39; (192.168.0.1) port &#39;443&#39; filename &#39;C:\server.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\server.key successfully loaded.
association_add TCP port 443 protocol http handle 03454E58
1717 bytes read
PKCS#12 imported
Bag 0/0: Encrypted
Bag 0/0 decrypted: Certificate
Certificate imported: Aldred Benedict &lt;[email protected]&gt;, KeyID efd4b1daf3758da10f37877b4971f82d1a99bd1f
Bag 1/0: PKCS#8 Encrypted key
Private key imported: KeyID ef:d4:b1:da:f3:75:8d:a1:0f:37:87:7b:49:71:f8:2d:...
ssl_init IPv4 addr &#39;192.168.0.1&#39; (192.168.0.1) port &#39;443&#39; filename &#39;C:\serverCert.pfx&#39; password(only for p12 file) &#39;caveman&#39;
ssl_init private key file C:\serverCert.pfx successfully loaded.
association_add TCP port 443 protocol http handle 03454E58

dissect_ssl enter frame #21 (first time)
ssl_session_init: initializing ptr 05072A5C size 588
  conversation = 050726F4, ssl_session = 05072A5C
  record: offset = 0, reported_length_remaining = 163
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 158, ssl state 0x00
association_find: TCP port 1076 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 154 bytes, remaining 163 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.1:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #22 (first time)
  conversation = 050726F4, ssl_session = 05072A5C
  record: offset = 0, reported_length_remaining = 1181
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 53, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0x88
  record: offset = 58, reported_length_remaining = 1123
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 707, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 703 bytes, remaining 770 
  record: offset = 770, reported_length_remaining = 411
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 397, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 775 length 393 bytes, remaining 1172 
  record: offset = 1172, reported_length_remaining = 9
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1177 length 0 bytes, remaining 1181

dissect_ssl enter frame #32 (first time)
ssl_session_init: initializing ptr 05073484 size 588
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 163
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 158, ssl state 0x00
association_find: TCP port 1077 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 154 bytes, remaining 163 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.1:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #33 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 1181
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 53, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0x88
  record: offset = 58, reported_length_remaining = 1123
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 707, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 703 bytes, remaining 770 
  record: offset = 770, reported_length_remaining = 411
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 397, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 775 length 393 bytes, remaining 1172 
  record: offset = 1172, reported_length_remaining = 9
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1177 length 0 bytes, remaining 1181

dissect_ssl enter frame #34 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 704
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 134, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
ssl_decrypt_pre_master_secret key exchange 0 different from KEX_RSA (16)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 139, reported_length_remaining = 565
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 559
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 148 offset 150 length 8824632 bytes, remaining 198 
  record: offset = 198, reported_length_remaining = 506
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1077 found 00000000
association_find: TCP port 443 found 0604A548
  record: offset = 235, reported_length_remaining = 469
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 464, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1077 found 00000000
association_find: TCP port 443 found 0604A548

dissect_ssl enter frame #35 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 266
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 202, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 198 bytes, remaining 207 
  record: offset = 207, reported_length_remaining = 59
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 213, reported_length_remaining = 53
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 251 offset 218 length 9643165 bytes, remaining 266

dissect_ssl enter frame #36 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 922
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 304, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0604A548
  record: offset = 309, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 608, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0604A548

dissect_ssl enter frame #40 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 634
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1077 found 00000000
association_find: TCP port 443 found 0604A548
  record: offset = 37, reported_length_remaining = 597
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 592, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1077 found 00000000
association_find: TCP port 443 found 0604A548

dissect_ssl enter frame #41 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 122
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1077 found 00000000
association_find: TCP port 443 found 0604A548
  record: offset = 37, reported_length_remaining = 85
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 80, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1077 found 00000000
association_find: TCP port 443 found 0604A548

dissect_ssl enter frame #43 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 362
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 304, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0604A548
  record: offset = 309, reported_length_remaining = 53
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 48, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0604A548

dissect_ssl enter frame #47 (first time)
  conversation = 0507311C, ssl_session = 05073484
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 32, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre></div><div id="question-tags" class="tags-container tags">ssl decrypt decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '11, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/3e9a0bc1ef1a8fb36c0d006a71179ad6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Caveman&#39;s gravatar image" /><p>Caveman<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Caveman has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '11, 21:41</p></div></div><div id="comments-container-7049" class="comments-container"></div><div id="comment-tools-7049" class="comment-tools"></div><div class="clear"></div><div id="comment-7049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7153"></span>

<div id="answer-container-7153" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7153-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I figured what's wrong. I used a Diffie-Hellman cipher. That's why the traffic cannot be decrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '11, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/3e9a0bc1ef1a8fb36c0d006a71179ad6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Caveman&#39;s gravatar image" /><p>Caveman<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Caveman has one accepted answer">50%</span></p></div></div><div id="comments-container-7153" class="comments-container"></div><div id="comment-tools-7153" class="comment-tools"></div><div class="clear"></div><div id="comment-7153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

