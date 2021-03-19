+++
type = "question"
title = "Decrypt Lync TLS SIP"
description = '''Hi, I&#x27;m running Wireshark 1.8 and I try to decrypt a SIP communication on a Lync server (Microsft voip server). Lync use TLS v1 to crypt sip flows but I can&#x27;t decrypt with wireshark. Somebody can maybe help me, this is the logs, thank&#x27;s : ssl_load_key: can&#x27;t import pem data  dissect_ssl enter frame ...'''
date = "2012-07-13T14:10:00Z"
lastmod = "2012-07-13T16:01:00Z"
weight = 12707
keywords = [ "tls", "ssl", "sip", "decrypt", "lync" ]
aliases = [ "/questions/12707" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt Lync TLS SIP](/questions/12707/decrypt-lync-tls-sip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12707-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm running Wireshark 1.8 and I try to decrypt a SIP communication on a Lync server (Microsft voip server). Lync use TLS v1 to crypt sip flows but I can't decrypt with wireshark. Somebody can maybe help me, this is the logs, thank's :</p><pre><code>ssl_load_key: can&#39;t import pem data

dissect_ssl enter frame #39 (first time)
ssl_session_init: initializing ptr 0528416C size 588
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 70
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 65, ssl state 0x00
association_find: TCP port 1264 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 61 bytes, remaining 70 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:5061
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #40 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #41 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2444
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2439, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 2444 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 13 offset 1473 length 963 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 14 offset 2440 length 0 bytes, remaining 2444 

dissect_ssl enter frame #89 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 321
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 269, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 274 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 258 bytes, remaining 274 
trying to use SSL keylog in C:\Documents and Settings\Jerome.LYNC.001\Bureau\MasterSecretlog.txt
  record: offset = 274, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 280, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 62 offset 285 length 7005420 bytes, remaining 321 

dissect_ssl enter frame #90 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 231 offset 11 length 12244221 bytes, remaining 47 

dissect_ssl enter frame #91 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 320, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #92 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 361
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 356, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #93 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 792
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 787, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #94 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 690
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 685, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #95 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1043
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1038, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #96 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #97 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #99 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 3831
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 3826, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #101 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #102 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #103 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2934
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 2929, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #105 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 599
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 594, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #106 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1026
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1021, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #107 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 966
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 961, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #108 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 604
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 599, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #109 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 470
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 465, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #110 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 288, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #111 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 511
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 506, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #112 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 666
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 393, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0
  record: offset = 398, reported_length_remaining = 268
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 263, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #113 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1090, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1095, reported_length_remaining = 365
  need_desegmentation: offset = 1095, reported_length_remaining = 365

dissect_ssl enter frame #114 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 969
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 964, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #116 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #117 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2920
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 2313, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 2318, reported_length_remaining = 602
  need_desegmentation: offset = 2318, reported_length_remaining = 602

dissect_ssl enter frame #119 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2062
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1445, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1450, reported_length_remaining = 612
  need_desegmentation: offset = 1450, reported_length_remaining = 612

dissect_ssl enter frame #121 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2072
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 742, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 747, reported_length_remaining = 1325
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 196, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 948, reported_length_remaining = 1124
  need_desegmentation: offset = 948, reported_length_remaining = 1124

dissect_ssl enter frame #122 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2584
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1165, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1170, reported_length_remaining = 1414
  need_desegmentation: offset = 1170, reported_length_remaining = 1414

dissect_ssl enter frame #124 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2232
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1736, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1741, reported_length_remaining = 491
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 486, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #125 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 358
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 353, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #126 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1103
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1098, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #130 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 982
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 977, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #131 (first time)
ssl_session_init: initializing ptr 0528ADBC size 588
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 78
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
client random len: 16 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #132 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #133 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1477
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1472, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1477 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 14 offset 1473 length 0 bytes, remaining 1477 

dissect_ssl enter frame #135 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 260, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
trying to use SSL keylog in C:\Documents and Settings\Jerome.LYNC.001\Bureau\MasterSecretlog.txt
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #136 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 220 offset 11 length 11369201 bytes, remaining 71 

dissect_ssl enter frame #137 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #138 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 170
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 165, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #139 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2031
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1581, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1586, reported_length_remaining = 445
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 440, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #140 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #142 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 2331
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1870, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1875, reported_length_remaining = 456
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 451, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #143 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 432
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 427, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #144 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #145 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #146 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #148 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 5469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5464, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #150 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #151 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #153 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #154 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 5622
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5617, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #156 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 428, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #157 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #158 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #160 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #161 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 4976
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4971, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #166 (first time)
ssl_session_init: initializing ptr 0528D960 size 588
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 102
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 97, ssl state 0x00
association_find: TCP port 1270 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 93 bytes, remaining 102 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #167 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 150
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 85, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 222 offset 90 length 14924092 bytes, remaining 150 

dissect_ssl enter frame #168 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 222 offset 11 length 11467023 bytes, remaining 71 

dissect_ssl enter frame #169 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 428, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #170 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #172 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #174 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #175 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 5197
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5192, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #177 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #178 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1797
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1792, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #180 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 479
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 474, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #181 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #182 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #183 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 4242
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4237, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #185 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 1065
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1060, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #186 (first time)
  conversation = 0528A7DC, ssl_session = 0528ADBC
  record: offset = 0, reported_length_remaining = 820
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 815, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #187 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 411
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 406, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #188 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #189 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #191 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 4270
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4265, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #193 (first time)
  conversation = 0528D494, ssl_session = 0528D960
  record: offset = 0, reported_length_remaining = 743
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 738, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #195 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1210
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1205, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #198 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 750
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 745, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #200 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 253
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 248, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #201 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1059
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1054, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #203 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 265
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 260, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #205 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 642
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 637, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #251 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 161
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 156, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #252 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 649
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 644, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #253 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #254 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1581
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1576, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #256 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 297
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 292, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #258 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 426
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 181, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 186, reported_length_remaining = 240
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 235, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #266 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 178
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 173, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #271 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 949
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 944, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #274 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 348
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 343, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #278 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 136
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 131, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #281 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 536
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 531, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #285 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 131
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 126, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #290 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 242
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 237, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #293 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 120
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 115, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #295 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 222
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 217, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #296 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 110
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 105, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #298 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 608
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 603, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #299 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1403, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1408, reported_length_remaining = 52
  need_desegmentation: offset = 1408, reported_length_remaining = 52

dissect_ssl enter frame #300 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 69, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #302 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1413, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1418, reported_length_remaining = 42
  need_desegmentation: offset = 1418, reported_length_remaining = 42

dissect_ssl enter frame #303 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 103
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 98, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #305 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 689
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 684, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #338 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 176
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 171, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #340 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 280
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 275, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #343 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 204
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 199, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #344 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 797
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 792, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #345 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1321, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1326, reported_length_remaining = 134
  need_desegmentation: offset = 1326, reported_length_remaining = 134

dissect_ssl enter frame #347 (first time)
  conversation = 05283BD8, ssl_session = 0528416C
  record: offset = 0, reported_length_remaining = 543
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 538, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #39 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 70
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 61 bytes, remaining 70 

dissect_ssl enter frame #41 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2444
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 13 offset 1473 length 963 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 14 offset 2440 length 0 bytes, remaining 2444 

dissect_ssl enter frame #89 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 321
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 274 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 258 bytes, remaining 274 
  record: offset = 274, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 280, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 62 offset 285 length 7005420 bytes, remaining 321 

dissect_ssl enter frame #90 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 231 offset 11 length 12244221 bytes, remaining 47 

dissect_ssl enter frame #91 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #92 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 361
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #93 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 792
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #94 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 690
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #95 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1043
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #99 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 3831
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #103 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2934
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #105 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 599
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #106 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1026
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #107 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 966
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #108 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 604
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #109 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 470
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #110 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #111 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 511
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #112 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 666
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0
  record: offset = 398, reported_length_remaining = 268
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #113 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1095, reported_length_remaining = 365
  need_desegmentation: offset = 1095, reported_length_remaining = 365

dissect_ssl enter frame #114 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 969
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #117 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2920
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 2318, reported_length_remaining = 602
  need_desegmentation: offset = 2318, reported_length_remaining = 602

dissect_ssl enter frame #119 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2062
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1450, reported_length_remaining = 612
  need_desegmentation: offset = 1450, reported_length_remaining = 612

dissect_ssl enter frame #121 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2072
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 747, reported_length_remaining = 1325
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 948, reported_length_remaining = 1124
  need_desegmentation: offset = 948, reported_length_remaining = 1124

dissect_ssl enter frame #122 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2584
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1170, reported_length_remaining = 1414
  need_desegmentation: offset = 1170, reported_length_remaining = 1414

dissect_ssl enter frame #124 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2232
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1741, reported_length_remaining = 491
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #125 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 358
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #126 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1103
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #130 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 982
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #131 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 78

dissect_ssl enter frame #133 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1477
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 14 offset 1473 length 0 bytes, remaining 1477 

dissect_ssl enter frame #135 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #136 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 220 offset 11 length 11369201 bytes, remaining 71 

dissect_ssl enter frame #138 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 170
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #139 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2031
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1586, reported_length_remaining = 445
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #142 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2331
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1875, reported_length_remaining = 456
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #143 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 432
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #148 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #154 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5622
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #156 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #161 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 4976
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #166 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 102
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 93 bytes, remaining 102 

dissect_ssl enter frame #167 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 150
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 85, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 222 offset 90 length 14924092 bytes, remaining 150 

dissect_ssl enter frame #168 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 222 offset 11 length 11467023 bytes, remaining 71 

dissect_ssl enter frame #169 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #175 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5197
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #178 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1797
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #180 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 479
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #183 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 4242
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #185 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1065
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #186 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 820
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #187 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 411
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #191 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 4270
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #193 (already visited)
  conversation = 0528D494, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 743
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #195 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1210
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #198 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 750
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #200 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 253
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #201 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1059
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #203 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 265
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #205 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 642
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #251 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 161
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #252 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 649
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #254 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1581
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #256 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 297
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #258 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 426
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 186, reported_length_remaining = 240
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #266 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 178
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #271 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 949
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #274 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 348
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #278 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 136
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #281 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 536
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #285 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 131
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #290 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 242
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #293 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 120
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #295 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 222
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #296 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 110
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #298 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 608
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #299 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1408, reported_length_remaining = 52
  need_desegmentation: offset = 1408, reported_length_remaining = 52

dissect_ssl enter frame #300 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #302 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1418, reported_length_remaining = 42
  need_desegmentation: offset = 1418, reported_length_remaining = 42

dissect_ssl enter frame #303 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 103
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #305 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 689
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #338 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 176
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #340 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 280
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #343 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 204
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #344 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 797
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #345 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0
  record: offset = 1326, reported_length_remaining = 134
  need_desegmentation: offset = 1326, reported_length_remaining = 134

dissect_ssl enter frame #347 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 543
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #39 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 70
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 61 bytes, remaining 70 

dissect_ssl enter frame #41 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2444
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 13 offset 1473 length 963 bytes, remaining 2444 
dissect_ssl3_handshake iteration 0 type 14 offset 2440 length 0 bytes, remaining 2444 

dissect_ssl enter frame #89 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 321
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 274 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 258 bytes, remaining 274 
  record: offset = 274, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 280, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 62 offset 285 length 7005420 bytes, remaining 321 

dissect_ssl enter frame #90 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 231 offset 11 length 12244221 bytes, remaining 47 

dissect_ssl enter frame #91 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #92 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 361
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #93 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 792
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #94 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 690
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #95 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1043
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #135 (already visited)
  conversation = 0528A7DC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #99 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 3831
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #103 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 2934
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #105 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 599
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #106 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1026
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #107 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 966
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #108 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 604
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1264 found 00000000
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #109 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 470
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 049BF9C0

dissect_ssl enter frame #39 (already visited)
  conversation = 05283BD8, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 70
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 61 bytes, remaining 70 

dissect_ssl enter frame #131 (first time)
ssl_session_init: initializing ptr 0528A824 size 588
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 78
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
client random len: 16 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #132 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #133 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1477
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1472, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1477 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 14 offset 1473 length 0 bytes, remaining 1477 

dissect_ssl enter frame #135 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 260, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
trying to use SSL keylog in C:\Documents and Settings\Jerome.LYNC.001\Bureau\MasterSecretlog.txt
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #136 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 220 offset 11 length 11369201 bytes, remaining 71 

dissect_ssl enter frame #143 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 432
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 427, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #144 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #145 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #146 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #148 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 5469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5464, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #150 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #151 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #153 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #154 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 5622
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5617, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #156 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 428, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #157 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #158 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #160 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #161 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4976
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4971, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #166 (first time)
ssl_session_init: initializing ptr 0528D348 size 588
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 102
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 97, ssl state 0x00
association_find: TCP port 1270 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 93 bytes, remaining 102 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #167 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 150
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 85, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 222 offset 90 length 14924092 bytes, remaining 150 

dissect_ssl enter frame #168 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 222 offset 11 length 11467023 bytes, remaining 71 

dissect_ssl enter frame #169 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 428, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #170 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #172 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #174 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #175 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 5197
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5192, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #177 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #178 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1797
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1792, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #180 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 479
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 474, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #181 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #182 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #183 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4242
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4237, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #185 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 1065
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1060, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #186 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 820
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 815, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #187 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 411
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 406, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #188 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #189 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #191 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 4270
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4265, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #193 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 743
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 738, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #131 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 78

dissect_ssl enter frame #133 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1477
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 14 offset 1473 length 0 bytes, remaining 1477 

dissect_ssl enter frame #135 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #136 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 220 offset 11 length 11369201 bytes, remaining 71 

dissect_ssl enter frame #143 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 432
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #148 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #154 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5622
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #156 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #131 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 78

dissect_ssl enter frame #131 (first time)
ssl_session_init: initializing ptr 0528A824 size 588
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 78
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
client random len: 16 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #132 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #133 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1477
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1472, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1477 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 14 offset 1473 length 0 bytes, remaining 1477 

dissect_ssl enter frame #135 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 260, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
trying to use SSL keylog in C:\Documents and Settings\Jerome.LYNC.001\Bureau\MasterSecretlog.txt
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #136 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 220 offset 11 length 11369201 bytes, remaining 71 

dissect_ssl enter frame #143 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 432
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 427, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #144 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #145 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #146 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #148 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 5469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5464, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #150 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #151 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #153 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #154 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 5622
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5617, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #156 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 428, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #157 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #158 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #160 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #161 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4976
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4971, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #166 (first time)
ssl_session_init: initializing ptr 0528D348 size 588
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 102
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 97, ssl state 0x00
association_find: TCP port 1270 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 93 bytes, remaining 102 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.141:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #167 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 150
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 85, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 222 offset 90 length 14924092 bytes, remaining 150 

dissect_ssl enter frame #168 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 222 offset 11 length 11467023 bytes, remaining 71 

dissect_ssl enter frame #169 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 428, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #170 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #172 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #174 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #175 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 5197
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5192, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #177 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #178 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1797
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1792, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #180 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 479
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 474, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #181 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #182 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #183 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 4242
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4237, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #185 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 1065
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1060, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #186 (first time)
  conversation = 0528A244, ssl_session = 0528A824
  record: offset = 0, reported_length_remaining = 820
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 815, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #187 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 411
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 406, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #188 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #189 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #191 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 4270
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4265, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1270 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #193 (first time)
  conversation = 0528CE7C, ssl_session = 0528D348
  record: offset = 0, reported_length_remaining = 743
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 738, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #131 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 78

dissect_ssl enter frame #133 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 1477
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1390 bytes, remaining 1477 
dissect_ssl3_handshake iteration 0 type 14 offset 1473 length 0 bytes, remaining 1477 

dissect_ssl enter frame #135 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 336
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 256 bytes, remaining 265 
  record: offset = 265, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 271, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 237 offset 276 length 12255752 bytes, remaining 336 

dissect_ssl enter frame #136 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 71
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 65
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 220 offset 11 length 11369201 bytes, remaining 71 

dissect_ssl enter frame #143 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 432
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #148 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #154 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 5622
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #156 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 433
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 1269 found 00000000
association_find: TCP port 443 found 04973120

dissect_ssl enter frame #131 (already visited)
  conversation = 0528A244, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 78
</code></pre></div><div id="question-tags" class="tags-container tags">tls ssl sip decrypt lync</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '12, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/f575fc1fd76c7c1763fb1f3f6076479f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jerome&#39;s gravatar image" /><p>Jerome<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jerome has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jul '12, 15:29</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-12707" class="comments-container"><span id="22629"></span><div id="comment-22629" class="comment"><div id="post-22629-score" class="comment-score"></div><div class="comment-text"><p>Hi ,</p><p>Was your problem resolved ? If yes ..can you please help me know how you could resolve the issue..i have a similar problem</p><p>I have lync.cer file and lync.pem file ..but wireshark does not show the sip messages decrypted ..any idea how i can get this done ?</p><p>Thanks in advance, SL.</p></div><div id="comment-22629-info" class="comment-info"><span class="comment-age">(03 Jul '13, 22:37)</span> Srinivas Lolla</div></div><span id="22638"></span><div id="comment-22638" class="comment"><div id="post-22638-score" class="comment-score"></div><div class="comment-text"><p>Yes we had found the solution, if my memory is good, in your pem file you have got an encrypted private key, you have to uncrypt your key. We had used openssl and after you should have the RSA private key in clear who should be understandable by Wireshark.</p></div><div id="comment-22638-info" class="comment-info"><span class="comment-age">(04 Jul '13, 02:18)</span> Jerome</div></div></div><div id="comment-tools-12707" class="comment-tools"></div><div class="clear"></div><div id="comment-12707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12709"></span>

<div id="answer-container-12709" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12709-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You seem to have configured both a private key (which could not be read properly by Wireshark) and a SSL session key logfile (in C:\Documents and Settings\Jerome.LYNC.001\Bureau\<a href="http://MasterSecretlog.txt">MasterSecretlog.txt</a>). Please share your current SSL preferences for further analysis.</p><p>Could you also explain how you got hold of the SSL session keys?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '12, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12709" class="comments-container"><span id="12716"></span><div id="comment-12716" class="comment"><div id="post-12716-score" class="comment-score"></div><div class="comment-text"><p>Hi, These private key come from my Lync server. I work on virtual machines for a university project on interoperability between some voip solutions. Lync use TLS v1 to crypt sip communications with its softphone cients. I try to decrypt a communication between two clients to compare standard SIP packets and Lync SIP packets. Lync server : 192.168.0.141 Lync client 1 : 192.168.0.143 I have export the certificat with private key and used OpenSSL to extract the key in a .pem file, but I dont understand why Wireshark can't use it. I have check my Mastersecretlog file but the file is empty... Thank's,</p></div><div id="comment-12716-info" class="comment-info"><span class="comment-age">(14 Jul '12, 05:02)</span> Jerome</div></div><span id="12717"></span><div id="comment-12717" class="comment"><div id="post-12717-score" class="comment-score"></div><div class="comment-text"><p>Your key file should not have a passphrase if it is in pem format.</p><p>And you should use something like "192.168.0.141,5061,sip,&lt;path-to-keyfile&gt;" in your SSL settings. The field for the master secret log should be empty, this is for reading known session keys from earlier decryption or from debug logging.</p></div><div id="comment-12717-info" class="comment-info"><span class="comment-age">(14 Jul '12, 05:57)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-12709" class="comment-tools"></div><div class="clear"></div><div id="comment-12709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

