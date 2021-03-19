+++
type = "question"
title = "is the decryption of TLS_RSA_WITH_AES_256_GCM_SHA384 cipher suite supported?"
description = '''I&#x27;m unable to decrypt any TLS 1.2 traffic if the cipher suite is TLS_RSA_WITH_AES_256_GCM_SHA384. I&#x27;m able to decrypt if I change the cipher suite. I&#x27;m using wireshark 2.2.6 Wireshark SSL debug log  Wireshark version: 2.2.6 (v2.2.6-0-g32dac6a) GnuTLS version: 3.2.15 Libgcrypt version: 1.6.2  KeyID[2...'''
date = "2017-05-10T13:26:00Z"
lastmod = "2017-05-12T08:41:00Z"
weight = 61343
keywords = [ "ciphersuite", "ssl", "openssl", "decryption", "ssl_decrypt" ]
aliases = [ "/questions/61343" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [is the decryption of TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384 cipher suite supported?](/questions/61343/is-the-decryption-of-tls_rsa_with_aes_256_gcm_sha384-cipher-suite-supported)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61343-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm unable to decrypt any TLS 1.2 traffic if the cipher suite is TLS_RSA_WITH_AES_256_GCM_SHA384. I'm able to decrypt if I change the cipher suite. I'm using wireshark 2.2.6</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.2.6 (v2.2.6-0-g32dac6a)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

KeyID[20]:
| 53 10 1d 8a 77 2e 73 37 e5 6d d9 1b c0 cf 10 dd |S...w.s7.m......|
| fe 13 ad ec                                     |....            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file E:/key.pem successfully loaded.
ssl_init port &#39;443&#39; filename &#39;E:/key.pem&#39; password(only for p12 file) &#39;&#39;
association_add ssl.port port 443 handle 0000000004B71BC0

dissect_ssl enter frame #4 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 221
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 216
decrypt_ssl3_record: app_data len 216, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 212 bytes, remaining 221 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 137
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 81
decrypt_ssl3_record: app_data len 81, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x009D TLS_RSA_WITH_AES_256_GCM_SHA384 -&gt; state 0x97
  record: offset = 86, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Session resumption using Session ID
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x97
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 97 40
decrypt_ssl3_record: app_data len 40, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 97 length 0 bytes, remaining 137 
dissect_ssl3_handshake iteration 0 type 0 offset 101 length 1 bytes, remaining 137 
dissect_ssl3_handshake iteration 0 type 252 offset 106 length 6788274 bytes, remaining 137

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x97
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 40
decrypt_ssl3_record: app_data len 40, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 11 length 0 bytes, remaining 51 
dissect_ssl3_handshake iteration 0 type 0 offset 15 length 0 bytes, remaining 51 
dissect_ssl3_handshake iteration 0 type 38 offset 19 length 789024 bytes, remaining 51

dissect_ssl enter frame #8 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1428
  need_desegmentation: offset = 0, reported_length_remaining = 1428

dissect_ssl enter frame #9 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1945
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1940, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #11 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1428
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 488, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 493, reported_length_remaining = 935
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 29, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 527, reported_length_remaining = 901
  need_desegmentation: offset = 527, reported_length_remaining = 901

dissect_ssl enter frame #12 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1463
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1458, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #12 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 26, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1428
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 29, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 34, reported_length_remaining = 1394
  need_desegmentation: offset = 34, reported_length_remaining = 1394

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 2667
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 2662, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 155
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 26, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 31, reported_length_remaining = 124
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 29, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 65, reported_length_remaining = 90
  need_desegmentation: offset = 65, reported_length_remaining = 90

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1261
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1256, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 257
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 26, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 31, reported_length_remaining = 226
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 28, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 64, reported_length_remaining = 193
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 175, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 244, reported_length_remaining = 13
  need_desegmentation: offset = 244, reported_length_remaining = 13

dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 26, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 34
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 29, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #21 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1428
  need_desegmentation: offset = 0, reported_length_remaining = 1428

dissect_ssl enter frame #22 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 00000000075920D0
  record: offset = 0, reported_length_remaining = 1945
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1940, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #4 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 221
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 212 bytes, remaining 221

dissect_ssl enter frame #5 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 137
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
  record: offset = 86, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 92, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 97 length 0 bytes, remaining 137 
dissect_ssl3_handshake iteration 0 type 0 offset 101 length 1 bytes, remaining 137 
dissect_ssl3_handshake iteration 0 type 252 offset 106 length 6788274 bytes, remaining 137

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 11 length 0 bytes, remaining 51 
dissect_ssl3_handshake iteration 0 type 0 offset 15 length 0 bytes, remaining 51 
dissect_ssl3_handshake iteration 0 type 38 offset 19 length 789024 bytes, remaining 51

dissect_ssl enter frame #9 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1945
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #11 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1428
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 493, reported_length_remaining = 935
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 527, reported_length_remaining = 901
  need_desegmentation: offset = 527, reported_length_remaining = 901

dissect_ssl enter frame #12 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1463
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #12 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1428
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 34, reported_length_remaining = 1394
  need_desegmentation: offset = 34, reported_length_remaining = 1394

dissect_ssl enter frame #16 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2667
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #16 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 155
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 31, reported_length_remaining = 124
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 65, reported_length_remaining = 90
  need_desegmentation: offset = 65, reported_length_remaining = 90

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1261
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 257
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 31, reported_length_remaining = 226
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 64, reported_length_remaining = 193
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 244, reported_length_remaining = 13
  need_desegmentation: offset = 244, reported_length_remaining = 13

dissect_ssl enter frame #19 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #19 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 34
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #22 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000007591700, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1945
dissect_ssl3_record: content_type 23 Application Data</code></pre></div><div id="question-tags" class="tags-container tags">ciphersuite ssl openssl decryption ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '17, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/fc4308015d9c1873c69e1e121587e2f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a5snc&#39;s gravatar image" /><p>a5snc<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a5snc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '17, 08:36</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61343" class="comments-container"></div><div id="comment-tools-61343" class="comment-tools"></div><div class="clear"></div><div id="comment-61343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61370"></span>

<div id="answer-container-61370" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61370-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not an expert but this item from the log:</p><pre><code>ssl_dissect_change_cipher_spec Session resumption using Session ID</code></pre><p>makes me think that the SSL session was resumed. As detailed in <a href="https://ask.wireshark.org/questions/43788/struggling-to-decrypt-ssl">this</a> question a resumed session can't be decrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '17, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61370" class="comments-container"></div><div id="comment-tools-61370" class="comment-tools"></div><div class="clear"></div><div id="comment-61370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

