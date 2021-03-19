+++
type = "question"
title = "SSL Decryption not working."
description = '''I perform decryption without issue regularly, and I did everything the same for this capture, but it&#x27;s not working. I disabled DHE, and the cipher being used is TLS_RSA_WITH_AES_128_CBC_SHA, as you can see in the log below. but the decryption doesn&#x27;t seem to work. I can&#x27;t find any relevant bugs. So ...'''
date = "2016-08-25T10:58:00Z"
lastmod = "2016-08-26T09:46:00Z"
weight = 55119
keywords = [ "ssl", "ssl_decrypt", "decryption" ]
aliases = [ "/questions/55119" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption not working.](/questions/55119/ssl-decryption-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55119-score" class="post-score" title="current number of votes">0</div><span id="post-55119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I perform decryption without issue regularly, and I did everything the same for this capture, but it's not working.</p><p>I disabled DHE, and the cipher being used is TLS_RSA_WITH_AES_128_CBC_SHA, as you can see in the log below. but the decryption doesn't seem to work. I can't find any relevant bugs. So I'm wondering what I'm missing here.</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.2.0rc1 (v2.2.0rc1-0-g438c022 from master-2.2)
GnuTLS version:    2.12.19
Libgcrypt version: 1.5.0

ssl_association_remove removing UDP 443 - handle 0x114cd4c10
KeyID[20]:
| fc 2f 23 ce 0f 39 52 24 c9 c5 27 3a 59 12 40 ed |./#..9R$..&#39;:[email protected]|
| 52 88 31 0a                                     |R.1.            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file /Users/e0170742/decrypt/&lt;redacted&gt;.key successfully loaded.
ssl_init port &#39;443&#39; filename &#39;/Users/e0170742/decrypt/&lt;redacted&gt;.key&#39; password(only for p12 file) &#39;&#39;
association_add ssl.port port 443 handle 0x114cd4c10

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 206
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 201
decrypt_ssl3_record: app_data len 201, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 197 bytes, remaining 206
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 1336
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 85
decrypt_ssl3_record: app_data len 85, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x002F TLS_RSA_WITH_AES_128_CBC_SHA -&gt; state 0x97
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #11 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 5753
decrypt_ssl3_record: app_data len 5753, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758
lookup(KeyID)[20]:
| fa c5 af a5 fd 33 09 87 bb 53 00 a6 12 33 f5 f0 |.....3...S...3..|
| 9f ad d2 e4                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0x0

dissect_ssl enter frame #11 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4
decrypt_ssl3_record: app_data len 4, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #13 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 206
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 201
decrypt_ssl3_record: app_data len 201, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 197 bytes, remaining 206
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 1336
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 85
decrypt_ssl3_record: app_data len 85, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x002F TLS_RSA_WITH_AES_128_CBC_SHA -&gt; state 0x97
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 5753
decrypt_ssl3_record: app_data len 5753, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758
lookup(KeyID)[20]:
| fa c5 af a5 fd 33 09 87 bb 53 00 a6 12 33 f5 f0 |.....3...S...3..|
| 9f ad d2 e4                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0x0

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4
decrypt_ssl3_record: app_data len 4, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #26 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 262
decrypt_ssl3_record: app_data len 262, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 278 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 174 offset 278 length 11298579 bytes, remaining 342

dissect_ssl enter frame #27 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 3 offset 11 length 10082429 bytes, remaining 75

dissect_ssl enter frame #33 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 262
decrypt_ssl3_record: app_data len 262, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 278 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 75 offset 278 length 12694995 bytes, remaining 342

dissect_ssl enter frame #34 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 235 offset 11 length 3290576 bytes, remaining 75

dissect_ssl enter frame #37 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b6d50, ssl_session = 0x1169ba250
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 512, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #42 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b66c0, ssl_session = 0x1169b7720
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 528, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #51 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 238
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 233
decrypt_ssl3_record: app_data len 233, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 229 bytes, remaining 238
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #52 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 1336
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 85
decrypt_ssl3_record: app_data len 85, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x002F TLS_RSA_WITH_AES_128_CBC_SHA -&gt; state 0x97
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #56 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 5753
decrypt_ssl3_record: app_data len 5753, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758
lookup(KeyID)[20]:
| fa c5 af a5 fd 33 09 87 bb 53 00 a6 12 33 f5 f0 |.....3...S...3..|
| 9f ad d2 e4                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0x0

dissect_ssl enter frame #56 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4
decrypt_ssl3_record: app_data len 4, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #62 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 262
decrypt_ssl3_record: app_data len 262, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 278 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 71 offset 278 length 9440866 bytes, remaining 342

dissect_ssl enter frame #63 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 44 offset 11 length 5362587 bytes, remaining 75

dissect_ssl enter frame #65 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x1169c0ec0
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 528, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #74 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 238
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 233
decrypt_ssl3_record: app_data len 233, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 229 bytes, remaining 238
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #75 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 1336
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 85
decrypt_ssl3_record: app_data len 85, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x002F TLS_RSA_WITH_AES_128_CBC_SHA -&gt; state 0x97
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #79 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 5753
decrypt_ssl3_record: app_data len 5753, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758
lookup(KeyID)[20]:
| fa c5 af a5 fd 33 09 87 bb 53 00 a6 12 33 f5 f0 |.....3...S...3..|
| 9f ad d2 e4                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0x0

dissect_ssl enter frame #79 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4
decrypt_ssl3_record: app_data len 4, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #85 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 262
decrypt_ssl3_record: app_data len 262, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 278 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 278 length 14831476 bytes, remaining 342

dissect_ssl enter frame #86 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 64
decrypt_ssl3_record: app_data len 64, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 151 offset 11 length 10999462 bytes, remaining 75

dissect_ssl enter frame #88 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1169c2d90, ssl_session = 0x1169c5a80
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 528, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #6 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 206
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 197 bytes, remaining 206

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 1336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #11 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758

dissect_ssl enter frame #11 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #13 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 206
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 197 bytes, remaining 206

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 1336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #26 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 174 offset 278 length 11298579 bytes, remaining 342

dissect_ssl enter frame #27 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 3 offset 11 length 10082429 bytes, remaining 75

dissect_ssl enter frame #33 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 75 offset 278 length 12694995 bytes, remaining 342

dissect_ssl enter frame #34 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 235 offset 11 length 3290576 bytes, remaining 75

dissect_ssl enter frame #37 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b6d50, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #42 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b66c0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #51 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 238
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 229 bytes, remaining 238

dissect_ssl enter frame #52 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 1336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #56 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758

dissect_ssl enter frame #56 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #62 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 71 offset 278 length 9440866 bytes, remaining 342

dissect_ssl enter frame #63 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 44 offset 11 length 5362587 bytes, remaining 75

dissect_ssl enter frame #65 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #74 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 238
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 229 bytes, remaining 238

dissect_ssl enter frame #75 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 1336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90
  record: offset = 90, reported_length_remaining = 1246
  need_desegmentation: offset = 90, reported_length_remaining = 1246

dissect_ssl enter frame #79 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 5758
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 5749 bytes, remaining 5758

dissect_ssl enter frame #79 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #85 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 342
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
  record: offset = 267, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 273, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 278 length 14831476 bytes, remaining 342

dissect_ssl enter frame #86 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 151 offset 11 length 10999462 bytes, remaining 75

dissect_ssl enter frame #88 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169c2d90, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #51 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x1169b9bc0, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 238
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 229 bytes, remaining 238</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '16, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/f1c01c97a368d12890afc86f646fce8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geewrd&#39;s gravatar image" /><p><span>geewrd</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geewrd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Aug '16, 04:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55119" class="comments-container"></div><div id="comment-tools-55119" class="comment-tools"></div><div class="clear"></div><div id="comment-55119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55128"></span>

<div id="answer-container-55128" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55128-score" class="post-score" title="current number of votes">0</div><span id="post-55128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Key ID (hash over the public key parameters) computes from your private key:</p><pre><code>KeyID[20]:
| fc 2f 23 ce 0f 39 52 24 c9 c5 27 3a 59 12 40 ed |./#..9R$..&#39;:[email protected]|
| 52 88 31 0a                                     |R.1.            |</code></pre><p>does not seem to match the public key from the certificate:</p><pre><code>lookup(KeyID)[20]:
| fa c5 af a5 fd 33 09 87 bb 53 00 a6 12 33 f5 f0 |.....3...S...3..|
| 9f ad d2 e4                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0x0</code></pre><p>Are you sure that the certificate matches your private key?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '16, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-55128" class="comments-container"></div><div id="comment-tools-55128" class="comment-tools"></div><div class="clear"></div><div id="comment-55128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

