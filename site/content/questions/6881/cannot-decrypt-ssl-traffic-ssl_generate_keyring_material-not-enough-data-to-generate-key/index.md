+++
type = "question"
title = "Cannot Decrypt SSL Traffic - ssl_generate_keyring_material not enough data to generate key"
description = '''I am no longer able to decrypt traffic. I noticed the new ssl certificate are 2048bits. Does wireshark support this? I have setup the private key, ip where the traffic is terminated and in the ssl log file i see that it successfully loaded the keys but I still cannot decrypt traffic. I am on server ...'''
date = "2011-10-13T18:39:00Z"
lastmod = "2012-01-09T17:23:00Z"
weight = 6881
keywords = [ "ssl" ]
aliases = [ "/questions/6881" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot Decrypt SSL Traffic - ssl\_generate\_keyring\_material not enough data to generate key](/questions/6881/cannot-decrypt-ssl-traffic-ssl_generate_keyring_material-not-enough-data-to-generate-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6881-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am no longer able to decrypt traffic. I noticed the new ssl certificate are 2048bits. Does wireshark support this? I have setup the private key, ip where the traffic is terminated and in the ssl log file i see that it successfully loaded the keys but I still cannot decrypt traffic. I am on server side so have public and private keys.</p><p>The private key is in RSA format.</p><p>ssl_init keys string:</p><pre><code>64.186.189.125,6004,http,F:\HDM310_6003\weblogic92\server\lib\ssl\server\server-PRIVATE--RSA.key
ssl_init found host entry 64.186.189.125,6004,http,F:\HDM310_6003\weblogic92\server\lib\ssl\server\server-PRIVATE--RSA.key
ssl_init addr &#39;64.186.189.125&#39; port &#39;6004&#39; filename &#39;F:\HDM310_6003\weblogic92\server\lib\ssl\server\server-PRIVATE--RSA.key&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID 5D:C6:6A:C8:DF:2C:C8:9B:96:BA:03:E9:50:53:1D:D5:...
ssl_init private key file F:\HDM310_6003\weblogic92\server\lib\ssl\server\server-PRIVATE--RSA.key successfully loaded
association_add TCP port 6004 protocol http handle 040AD350

dissect_ssl enter frame #24 (first time)
ssl_session_init: initializing ptr 055025A8 size 564
association_find: TCP port 2059 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 64.186.189.125:6004
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 116
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 111 ssl, state 0x00
association_find: TCP port 2059 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 107 bytes, remaining 116 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #25 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 63, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 69, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 198 offset 74 length 11165230 bytes, remaining 106

dissect_ssl enter frame #27 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 2059 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 2059 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 43 offset 11 length 8390811 bytes, remaining 43

dissect_ssl enter frame #28 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #30 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 2880
  need_desegmentation: offset = 0, reported_length_remaining = 2880

dissect_ssl enter frame #31 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 3572
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 3567 ssl, state 0x17
association_find: TCP port 2059 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2059 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #33 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 229
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 224 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #34 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 524
  need_desegmentation: offset = 0, reported_length_remaining = 524

dissect_ssl enter frame #35 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 1048
  need_desegmentation: offset = 0, reported_length_remaining = 1048

dissect_ssl enter frame #36 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 1379
  need_desegmentation: offset = 0, reported_length_remaining = 1379

dissect_ssl enter frame #38 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 1562
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1534 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10
  record: offset = 1539, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #40 (first time)
  conversation = 055022D0, ssl_session = 055025A8
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 2059 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #45 (first time)
ssl_session_init: initializing ptr 055031D8 size 564
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 64.186.189.125:6004
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 116
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 111 ssl, state 0x00
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 107 bytes, remaining 116 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #46 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 63, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 69, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 82 offset 74 length 6702603 bytes, remaining 106

dissect_ssl enter frame #48 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 217 offset 11 length 3817121 bytes, remaining 43

dissect_ssl enter frame #49 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #51 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 2880
  need_desegmentation: offset = 0, reported_length_remaining = 2880

dissect_ssl enter frame #52 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 3615
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 3610 ssl, state 0x17
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2061 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #54 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 382
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 377 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #55 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 484
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 479 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #57 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 380
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 375 ssl, state 0x17
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2061 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #58 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 172
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 167 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #59 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 494
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 489 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #61 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #62 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 1759
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1754 ssl, state 0x17
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2061 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #64 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 178
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 173 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #66 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 2061 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #67 (first time)
  conversation = 05502F00, ssl_session = 055031D8
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #75 (first time)
ssl_session_init: initializing ptr 05504148 size 564
association_find: TCP port 2063 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 64.186.189.125:6004
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 116
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 111 ssl, state 0x00
association_find: TCP port 2063 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 107 bytes, remaining 116 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #76 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 63, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 69, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 178 offset 74 length 8692811 bytes, remaining 106

dissect_ssl enter frame #78 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 2063 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 2063 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 226 offset 11 length 14013770 bytes, remaining 43

dissect_ssl enter frame #79 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #81 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 2880
  need_desegmentation: offset = 0, reported_length_remaining = 2880

dissect_ssl enter frame #82 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 3562
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 3557 ssl, state 0x17
association_find: TCP port 2063 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2063 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #84 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 229
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 224 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #85 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 524
  need_desegmentation: offset = 0, reported_length_remaining = 524

dissect_ssl enter frame #86 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 1048
  need_desegmentation: offset = 0, reported_length_remaining = 1048

dissect_ssl enter frame #87 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 1379
  need_desegmentation: offset = 0, reported_length_remaining = 1379

dissect_ssl enter frame #89 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 1562
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1534 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10
  record: offset = 1539, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #91 (first time)
  conversation = 05503E70, ssl_session = 05504148
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 2063 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #96 (first time)
ssl_session_init: initializing ptr 05504D78 size 564
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 64.186.189.125:6004
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 116
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 111 ssl, state 0x00
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 107 bytes, remaining 116 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #97 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 63, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 69, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 31 offset 74 length 947347 bytes, remaining 106

dissect_ssl enter frame #99 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 127 offset 11 length 6273604 bytes, remaining 43

dissect_ssl enter frame #100 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #102 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 2880
  need_desegmentation: offset = 0, reported_length_remaining = 2880

dissect_ssl enter frame #104 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 3605
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 3600 ssl, state 0x17
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2065 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #106 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 382
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 377 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #107 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 484
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 479 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #109 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 380
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 375 ssl, state 0x17
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2065 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #111 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 178
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 173 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #113 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 2065 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #116 (first time)
  conversation = 05504AA0, ssl_session = 05504D78
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #142 (first time)
ssl_session_init: initializing ptr 05506558 size 564
association_find: TCP port 2067 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 64.186.189.125:6004
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 116
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 111 ssl, state 0x00
association_find: TCP port 2067 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 107 bytes, remaining 116 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #143 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 63, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 69, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 252 offset 74 length 15049992 bytes, remaining 106

dissect_ssl enter frame #145 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 2067 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 2067 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 204 offset 11 length 9798724 bytes, remaining 43

dissect_ssl enter frame #146 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #148 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 2880
  need_desegmentation: offset = 0, reported_length_remaining = 2880

dissect_ssl enter frame #150 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 3572
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 3567 ssl, state 0x17
association_find: TCP port 2067 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2067 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #151 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 229
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 224 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #152 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 524
  need_desegmentation: offset = 0, reported_length_remaining = 524

dissect_ssl enter frame #153 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 1048
  need_desegmentation: offset = 0, reported_length_remaining = 1048

dissect_ssl enter frame #154 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 1379
  need_desegmentation: offset = 0, reported_length_remaining = 1379

dissect_ssl enter frame #156 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 1562
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1534 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10
  record: offset = 1539, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #158 (first time)
  conversation = 05506280, ssl_session = 05506558
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 2067 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #163 (first time)
ssl_session_init: initializing ptr 05507188 size 564
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 64.186.189.125:6004
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 116
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 111 ssl, state 0x00
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 107 bytes, remaining 116 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #164 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 63, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 69, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 116 offset 74 length 13080417 bytes, remaining 106

dissect_ssl enter frame #166 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 173 offset 11 length 353274 bytes, remaining 43

dissect_ssl enter frame #167 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 1440
  need_desegmentation: offset = 0, reported_length_remaining = 1440

dissect_ssl enter frame #169 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 2880
  need_desegmentation: offset = 0, reported_length_remaining = 2880

dissect_ssl enter frame #170 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 3615
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 3610 ssl, state 0x17
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2069 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #172 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 382
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 377 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #173 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 484
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 479 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #175 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 380
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 375 ssl, state 0x17
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 2069 found 00000000
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #177 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 178
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 173 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 6004 found 061CEA10

dissect_ssl enter frame #179 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 2069 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #182 (first time)
  conversation = 05506EB0, ssl_session = 05507188
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 6004 found 061CEA10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '11, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/f3bee40b165c05eb9cac555a6f34040b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbhimji&#39;s gravatar image" /><p>mbhimji<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbhimji has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Oct '11, 00:07</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-6881" class="comments-container"></div><div id="comment-tools-6881" class="comment-tools"></div><div class="clear"></div><div id="comment-6881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8285"></span>

<div id="answer-container-8285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8285-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm wondering the same thing. If I switch our test site back to our old 1024 cert, I can decrypt just fine. However, when I move to the new 2048 certs, it fails with similar debug logs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '12, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/2e7337ea3a747674707604a9f44252ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbully&#39;s gravatar image" /><p>tbully<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbully has no accepted answers">0%</span></p></div></div><div id="comments-container-8285" class="comments-container"><span id="8292"></span><div id="comment-8292" class="comment"><div id="post-8292-score" class="comment-score"></div><div class="comment-text"><p>Yes, wireshark supports certificates with a 2048 bit key, that is not the issue.</p></div><div id="comment-8292-info" class="comment-info"><span class="comment-age">(09 Jan '12, 17:24)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-8285" class="comment-tools"></div><div class="clear"></div><div id="comment-8285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8291"></span>

<div id="answer-container-8291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8291-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the SSL session has been reused, so wireshark does not see the necessary key exchange. Close all browser windows and start capturing with wireshark <strong>before</strong> starting the browser, that should get you on the way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '12, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8291" class="comments-container"></div><div id="comment-tools-8291" class="comment-tools"></div><div class="clear"></div><div id="comment-8291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

