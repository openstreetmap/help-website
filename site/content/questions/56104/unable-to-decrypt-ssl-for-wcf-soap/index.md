+++
type = "question"
title = "Unable to decrypt SSL for WCF SOAP."
description = '''I believe I have correctly configured Wireshark (SSL Protocol tab w/ RSA Keys list pointing to local .p12). I have attached an SSL debug log (with sensitive details removed); I&#x27;m hoping someone with an experienced eye can take a look. Thank you Wireshark SSL debug log  Wireshark version: 2.2.0 (v2.2...'''
date = "2016-10-03T11:12:00Z"
lastmod = "2016-10-03T11:12:00Z"
weight = 56104
keywords = [ "ssl" ]
aliases = [ "/questions/56104" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt SSL for WCF SOAP.](/questions/56104/unable-to-decrypt-ssl-for-wcf-soap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56104-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I believe I have correctly configured Wireshark (SSL Protocol tab w/ RSA Keys list pointing to local .p12).</p><p>I have attached an SSL debug log (with sensitive details removed); I'm hoping someone with an experienced eye can take a look.</p><p>Thank you</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.2.0 (v2.2.0-0-g5368c50 from master-2.2)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

3789 bytes read
PKCS#12 imported
Bag 0/0: Encrypted
Bag 0/0 decrypted: Certificate
Bag 0/1: Certificate
Bag 1/0: PKCS#8 Encrypted key
KeyID[20]:
| 00 3f ce b2 d8 20 e6 5f 62 47 ab 2c 9c 54 df 04 |.?... ._bG.,.T..|
| d2 31 b0 0b                                     |.1..            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file C:/removed.p12 successfully loaded.
ssl_init port &#39;0&#39; filename &#39;C:/removed.p12&#39; password(only for p12 file) &#39;removed&#39;
association_add ssl.port port 0 handle 0000026EFF16B130

dissect_ssl enter frame #12 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 184
decrypt_ssl3_record: app_data len 184, ssl state 0x00
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 1360
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 65
decrypt_ssl3_record: app_data len 65, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 61 bytes, remaining 70 
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0xC030 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 -&gt; state 0x97
  record: offset = 70, reported_length_remaining = 1290
  need_desegmentation: offset = 70, reported_length_remaining = 1290

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 4239
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4234
decrypt_ssl3_record: app_data len 4234, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 4230 bytes, remaining 4239 
lookup(KeyID)[20]:
| 12 06 0a d2 b1 8f d2 95 cc 47 cb dc 33 41 c2 a8 |.........G..3A..|
| 92 0e f4 bc                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0000000000000000

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 732
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 333
decrypt_ssl3_record: app_data len 333, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 5 length 329 bytes, remaining 338 
  record: offset = 338, reported_length_remaining = 394
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 343 389
decrypt_ssl3_record: app_data len 389, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 343 length 381 bytes, remaining 732 
dissect_ssl3_handshake iteration 0 type 14 offset 728 length 0 bytes, remaining 732

dissect_ssl enter frame #20 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 77
decrypt_ssl3_record: app_data len 77, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 82 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 66 bytes, remaining 82 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 82, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 88, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 93 40
decrypt_ssl3_record: app_data len 40, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 93 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 0 offset 97 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 45 offset 101 length 12227759 bytes, remaining 133

dissect_ssl enter frame #21 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 218
decrypt_ssl3_record: app_data len 218, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 214 bytes, remaining 223 
ssl_save_master_key not saving empty (pre-)master secret for Session Ticket!
  record: offset = 223, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x697
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 229, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 234 40
decrypt_ssl3_record: app_data len 40, ssl state 0x697
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 228 offset 234 length 13846850 bytes, remaining 274

dissect_ssl enter frame #22 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 313, ssl state 0x697
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #23 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 420
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 415, ssl state 0x697
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #24 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000026E84611010
  record: offset = 0, reported_length_remaining = 992
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 987, ssl state 0x697
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #12 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 61 bytes, remaining 70 
  record: offset = 70, reported_length_remaining = 1290
  need_desegmentation: offset = 70, reported_length_remaining = 1290

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4239
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 4230 bytes, remaining 4239

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 732
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 12 offset 5 length 329 bytes, remaining 338 
  record: offset = 338, reported_length_remaining = 394
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 13 offset 343 length 381 bytes, remaining 732 
dissect_ssl3_handshake iteration 0 type 14 offset 728 length 0 bytes, remaining 732

dissect_ssl enter frame #20 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 82 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 66 bytes, remaining 82 
  record: offset = 82, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 88, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 93 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 0 offset 97 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 45 offset 101 length 12227759 bytes, remaining 133

dissect_ssl enter frame #21 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 214 bytes, remaining 223 
  record: offset = 223, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 229, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 228 offset 234 length 13846850 bytes, remaining 274

dissect_ssl enter frame #22 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #23 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 420
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #24 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 992
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #22 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #22 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E846105C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #38 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 184
decrypt_ssl3_record: app_data len 184, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #40 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 1360
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 65
decrypt_ssl3_record: app_data len 65, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 61 bytes, remaining 70 
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0xC030 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 -&gt; state 0x97
  record: offset = 70, reported_length_remaining = 1290
  need_desegmentation: offset = 70, reported_length_remaining = 1290

dissect_ssl enter frame #44 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 4239
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4234
decrypt_ssl3_record: app_data len 4234, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 4230 bytes, remaining 4239 
lookup(KeyID)[20]:
| 12 06 0a d2 b1 8f d2 95 cc 47 cb dc 33 41 c2 a8 |.........G..3A..|
| 92 0e f4 bc                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0000000000000000

dissect_ssl enter frame #44 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 732
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 333
decrypt_ssl3_record: app_data len 333, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 5 length 329 bytes, remaining 338 
  record: offset = 338, reported_length_remaining = 394
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 343 389
decrypt_ssl3_record: app_data len 389, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 343 length 381 bytes, remaining 732 
dissect_ssl3_handshake iteration 0 type 14 offset 728 length 0 bytes, remaining 732

dissect_ssl enter frame #38 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189

dissect_ssl enter frame #40 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 61 bytes, remaining 70 
  record: offset = 70, reported_length_remaining = 1290
  need_desegmentation: offset = 70, reported_length_remaining = 1290

dissect_ssl enter frame #44 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4239
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 4230 bytes, remaining 4239

dissect_ssl enter frame #44 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 732
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 12 offset 5 length 329 bytes, remaining 338 
  record: offset = 338, reported_length_remaining = 394
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 13 offset 343 length 381 bytes, remaining 732 
dissect_ssl3_handshake iteration 0 type 14 offset 728 length 0 bytes, remaining 732

dissect_ssl enter frame #49 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 77
decrypt_ssl3_record: app_data len 77, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 82 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 66 bytes, remaining 82 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 82, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 88, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 93 40
decrypt_ssl3_record: app_data len 40, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 93 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 0 offset 97 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 142 offset 101 length 123382 bytes, remaining 133

dissect_ssl enter frame #53 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 218
decrypt_ssl3_record: app_data len 218, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 214 bytes, remaining 223 
ssl_save_master_key not saving empty (pre-)master secret for Session Ticket!
  record: offset = 223, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x697
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 229, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 234 40
decrypt_ssl3_record: app_data len 40, ssl state 0x697
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 240 offset 234 length 2088591 bytes, remaining 274

dissect_ssl enter frame #55 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 313, ssl state 0x697
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #57 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 420
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 415, ssl state 0x697
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #58 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000026E84608150
  record: offset = 0, reported_length_remaining = 992
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 987, ssl state 0x697
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #65 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 173
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 168
decrypt_ssl3_record: app_data len 168, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 164 bytes, remaining 173 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #68 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 1360
  need_desegmentation: offset = 0, reported_length_remaining = 1360

dissect_ssl enter frame #38 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189

dissect_ssl enter frame #49 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 82 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 66 bytes, remaining 82 
  record: offset = 82, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 88, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 93 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 0 offset 97 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 142 offset 101 length 123382 bytes, remaining 133

dissect_ssl enter frame #53 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 214 bytes, remaining 223 
  record: offset = 223, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 229, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 240 offset 234 length 2088591 bytes, remaining 274

dissect_ssl enter frame #55 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #57 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 420
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #58 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 992
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #65 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 173
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 164 bytes, remaining 173

dissect_ssl enter frame #71 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 3812
ssl_try_set_version found version 0x0301 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 3807
decrypt_ssl3_record: app_data len 3807, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 3812 
ssl_try_set_version found version 0x0301 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0xC014 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA -&gt; state 0x97
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 3383 bytes, remaining 3812 
lookup(KeyID)[20]:
| 22 b0 15 ac 97 7d 1b 79 cd 3f e6 30 cb 9e 45 ff |&quot;....}.y.?.0..E.|
| 62 e5 be 53                                     |b..S            |
ssl_find_private_key_by_pubkey: lookup result: 0000000000000000
dissect_ssl3_handshake iteration 0 type 12 offset 3477 length 327 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 14 offset 3808 length 0 bytes, remaining 3812

dissect_ssl enter frame #72 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 70
decrypt_ssl3_record: app_data len 70, ssl state 0x397
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 397
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x397
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 86 48
decrypt_ssl3_record: app_data len 48, ssl state 0x397
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 48 offset 86 length 4198931 bytes, remaining 134

dissect_ssl enter frame #74 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x397
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 48
decrypt_ssl3_record: app_data len 48, ssl state 0x397
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 5 offset 11 length 3892323 bytes, remaining 59

dissect_ssl enter frame #75 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 234
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x397
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
  record: offset = 37, reported_length_remaining = 197
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 192, ssl state 0x397
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #71 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 3812
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 3383 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 12 offset 3477 length 327 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 14 offset 3808 length 0 bytes, remaining 3812

dissect_ssl enter frame #72 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 48 offset 86 length 4198931 bytes, remaining 134

dissect_ssl enter frame #74 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 5 offset 11 length 3892323 bytes, remaining 59

dissect_ssl enter frame #75 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 234
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 197
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #38 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189

dissect_ssl enter frame #77 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x397
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
  record: offset = 37, reported_length_remaining = 1323
  need_desegmentation: offset = 37, reported_length_remaining = 1323

dissect_ssl enter frame #80 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 5141
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5136, ssl state 0x397
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #81 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x397
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x397
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #77 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 1323
  need_desegmentation: offset = 37, reported_length_remaining = 1323

dissect_ssl enter frame #80 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 5141
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #81 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #88 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000026E8460D250
  record: offset = 0, reported_length_remaining = 362
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x397
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 37, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 320, ssl state 0x397
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #88 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 362
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #77 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 1323
  need_desegmentation: offset = 37, reported_length_remaining = 1323

dissect_ssl enter frame #80 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 5141
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #81 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #88 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 362
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #81 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #80 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 5141
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #77 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 1323
  need_desegmentation: offset = 37, reported_length_remaining = 1323

dissect_ssl enter frame #75 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 234
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 197
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #74 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 5 offset 11 length 3892323 bytes, remaining 59

dissect_ssl enter frame #72 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 48 offset 86 length 4198931 bytes, remaining 134

dissect_ssl enter frame #71 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 3812
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 3383 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 12 offset 3477 length 327 bytes, remaining 3812 
dissect_ssl3_handshake iteration 0 type 14 offset 3808 length 0 bytes, remaining 3812

dissect_ssl enter frame #65 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84609470, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 173
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 164 bytes, remaining 173

dissect_ssl enter frame #58 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 992
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #57 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 420
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #55 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #53 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 214 bytes, remaining 223 
  record: offset = 223, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 229, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 240 offset 234 length 2088591 bytes, remaining 274

dissect_ssl enter frame #49 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 82 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 66 bytes, remaining 82 
  record: offset = 82, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 88, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 93 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 0 offset 97 length 0 bytes, remaining 133 
dissect_ssl3_handshake iteration 0 type 142 offset 101 length 123382 bytes, remaining 133

dissect_ssl enter frame #44 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4239
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 4230 bytes, remaining 4239

dissect_ssl enter frame #44 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 732
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 12 offset 5 length 329 bytes, remaining 338 
  record: offset = 338, reported_length_remaining = 394
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 13 offset 343 length 381 bytes, remaining 732 
dissect_ssl3_handshake iteration 0 type 14 offset 728 length 0 bytes, remaining 732

dissect_ssl enter frame #40 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1360
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 61 bytes, remaining 70 
  record: offset = 70, reported_length_remaining = 1290
  need_desegmentation: offset = 70, reported_length_remaining = 1290

dissect_ssl enter frame #38 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000026E84607780, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 189
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 180 bytes, remaining 189</code></pre></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '16, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/22f551bba3080eef8de3919ceeb574e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kindjames&#39;s gravatar image" /><p>kindjames<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kindjames has no accepted answers">0%</span></p></div></div><div id="comments-container-56104" class="comments-container"></div><div id="comment-tools-56104" class="comment-tools"></div><div class="clear"></div><div id="comment-56104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

