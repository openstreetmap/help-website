+++
type = "question"
title = "TLSv1 Decryption Problem"
description = '''Hello, I&#x27;m having problems decrypting HTTPS TLSv1 traffic. I&#x27;ve set up a Windows Server 2012 VM with IIS and I&#x27;ve only allowed RSA cipher suites. I start the capture, open the browser and the page and then stop the capture. Then I configure the private key on Wireshark but the traffic does not get d...'''
date = "2015-10-17T10:06:00Z"
lastmod = "2015-10-18T02:26:00Z"
weight = 46641
keywords = [ "tlsv1", "decryption" ]
aliases = [ "/questions/46641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLSv1 Decryption Problem](/questions/46641/tlsv1-decryption-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm having problems decrypting HTTPS TLSv1 traffic. I've set up a Windows Server 2012 VM with IIS and I've only allowed RSA cipher suites.</p><p>I start the capture, open the browser and the page and then stop the capture.</p><p>Then I configure the private key on Wireshark but the traffic does not get decrypted.</p><p>I found an error regarding the Pre Master Secret but I'm sure that this is the correct private key and certificate.</p><p>At the end of the post you'll find the contents of the SSL log file.</p><p>Regards,</p><p>Chris</p><p>Wireshark SSL debug log</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0000000004453240
Private key imported: KeyID 75:a5:a6:2c:01:a5:7c:34:a5:4a:a0:e9:c3:74:4f:18:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;192.168.0.9&#39; (192.168.0.9) port &#39;443&#39; filename &#39;C:\Users\chris_000\Desktop\key.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\Users\chris_000\Desktop\key.pem successfully loaded.
association_add TCP port 443 protocol http handle 0000000004453240

dissect_ssl enter frame #8 (first time)
ssl_session_init: initializing ptr 000000000A5D1790 size 712
association_find: TCP port 60866 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000005771098, ssl_session = 000000000A5D1790
  record: offset = 0, reported_length_remaining = 223
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 218, ssl state 0x00
association_find: TCP port 60866 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 214 bytes, remaining 223 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.9:443
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #13 (first time)
ssl_session_init: initializing ptr 000000000A5D2280 size 712
association_find: TCP port 60867 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 175
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 170, ssl state 0x00
association_find: TCP port 60867 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 166 bytes, remaining 175 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.0.9:443
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 965
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 960, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 965 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 871 bytes, remaining 965 
dissect_ssl3_handshake iteration 0 type 14 offset 961 length 0 bytes, remaining 965

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 314
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
pre master encrypted[256]:
| 07 6a 72 cb 03 09 9c 0e 23 c6 23 7f 2c 3d 85 6b |.jr.....#.#.,=.k|
| 67 cf 4b eb 2a 4d 9d 06 2a 7c 75 b5 d5 bf fc 47 |g.K.*M..*|u....G|
| 5e d0 5b cd 86 0e 77 03 58 1d 49 a7 a5 fb 22 a7 |^.[...w.X.I...&quot;.|
| e0 b0 1d 3b 90 7d cb 61 35 24 9a f2 3d 3d 14 49 |...;.}.a5$..==.I|
| 25 8a 05 2e da 0c ee f7 01 8d 9c 1f 63 75 49 ba |%...........cuI.|
| b7 ea 43 1e b7 75 53 a7 40 6b d7 45 d9 65 4a ef |..C..uS.@k.E.eJ.|
| 2c b8 7a a5 88 b6 21 ce f9 3e a2 c1 70 b4 2a a1 |,.z...!..&gt;..p.*.|
| e5 38 59 52 88 48 ee 0f e6 8a 60 65 37 d9 76 3b |.8YR.H....`e7.v;|
| fb e6 f0 5d c0 5b 93 e7 8d 27 dd d0 7c 6c 4b 99 |...].[...&#39;..|lK.|
| 0e 3f e2 fd da ba d4 1d c7 87 19 28 30 40 24 c2 |.?.........([email protected]$.|
| 00 e3 96 13 68 20 8c 85 9d ab 9e 61 7b b8 f1 15 |....h .....a{...|
| 5b e5 cd a5 d0 19 bf 4b f9 56 3f 80 a6 a2 f6 37 |[......K.V?....7|
| 69 14 b6 e2 28 97 2c 6b fc 16 19 0e 67 75 eb b2 |i...(.,k....gu..|
| f3 85 3e 06 bd 76 10 73 95 e7 bf bf 73 f3 c7 57 |..&gt;..v.s....s..W|
| 35 09 d9 e0 34 59 97 b6 40 af fd 64 5e dd e2 7a |[email protected]^..z|
| cd 81 7f 7b e0 8a 51 3c cc a9 93 9e ef 0b 64 5a |...{..Q&lt;......dZ|
ssl_decrypt_pre_master_secret:RSA_private_decrypt
decrypted_unstrip_pre_master[256]:
| 07 f9 03 9c 86 87 14 37 b8 47 54 e2 b4 d8 45 04 |.......7.GT...E.|
| 73 28 ca b0 c0 14 7e 48 6b fb c1 01 9f 2e 4d ac |s(....~Hk.....M.|
| 16 b8 a0 b5 22 8b 47 9a f9 4f 81 b6 fb c6 c8 c6 |....&quot;.G..O......|
| ab af 11 8d c8 4c 6b 74 96 2c 9c f0 ef bb cf 3e |.....Lkt.,.....&gt;|
| fd 3d 65 67 87 c9 ed 63 9d 1e 69 df 0f 48 86 47 |.=eg...c..i..H.G|
| f5 d7 9f ad 2e c4 46 39 68 b3 cf a8 83 8b 1f 6e |......F9h......n|
| f9 23 9b 7a f9 10 ff f2 0f 84 63 6c a9 25 0a 1f |.#.z......cl.%..|
| 48 7b 63 55 7b ab 3e 66 85 fd b7 71 9e eb 4f 8f |H{cU{.&gt;f...q..O.|
| b9 af 94 13 98 75 52 1e 85 67 fc bd ba e5 f0 05 |.....uR..g......|
| 28 7d da e3 06 38 21 4b f1 7d 50 c3 9d 86 bd 83 |(}...8!K.}P.....|
| 3c 03 10 38 5a cf 3e 9d d8 73 b7 aa b5 f2 48 4b |&lt;..8Z.&gt;..s....HK|
| 74 af 39 4a fb e5 ce 33 27 e6 a6 08 a9 99 71 d1 |t.9J...3&#39;.....q.|
| 80 a7 44 89 7e f4 9c 43 ac 57 2a ad fd ca 02 18 |..D.~..C.W*.....|
| 2a a4 a7 3c 5d d8 32 dc fa e6 1e 30 14 53 7a a8 |*..&lt;].2....0.Sz.|
| bb 5c f0 75 18 52 74 6e 3c 86 40 7d b4 af 2b 08 |.\.u.Rtn&lt;[email protected]}..+.|
| d9 5f 75 cf 87 59 b8 88 6e dd a3 4f 27 ff ff ff |._u..Y..n..O&#39;...|
pcry_private_decrypt: stripping 0 bytes, decr_len 256
ssl_decrypt_pre_master_secret wrong pre_master_secret length (256, expected 48)
ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret
trying to use SSL keylog in c:\sslkeylogfile.log
failed to open SSL keylog
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 32 offset 278 length 3561692 bytes, remaining 314

dissect_ssl enter frame #17 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
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
dissect_ssl3_handshake iteration 1 type 84 offset 11 length 1500765 bytes, remaining 47

dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 313, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 60867 found 0000000000000000
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #20 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 948
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 943, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #22 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 393
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 388, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 60867 found 0000000000000000
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #23 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #35 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 16409
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 16404, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #35 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 1111
  need_desegmentation: offset = 0, reported_length_remaining = 1111

dissect_ssl enter frame #47 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 16409
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 16404, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #47 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 762
  need_desegmentation: offset = 0, reported_length_remaining = 762

dissect_ssl enter frame #59 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 16409
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 16404, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #59 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 413
  need_desegmentation: offset = 0, reported_length_remaining = 413

dissect_ssl enter frame #71 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 16409
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 16404, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #71 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 64
  need_desegmentation: offset = 0, reported_length_remaining = 64

dissect_ssl enter frame #72 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 250
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 245, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #74 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #85 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 16409
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 16404, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #85 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 1111
  need_desegmentation: offset = 0, reported_length_remaining = 1111

dissect_ssl enter frame #97 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 16409
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 16404, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #97 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 762
  need_desegmentation: offset = 0, reported_length_remaining = 762

dissect_ssl enter frame #98 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 000000000A5D2280
  record: offset = 0, reported_length_remaining = 1431
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1426, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #8 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771098, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 223
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 214 bytes, remaining 223

dissect_ssl enter frame #13 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 175
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 166 bytes, remaining 175

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 965
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 965 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 871 bytes, remaining 965 
dissect_ssl3_handshake iteration 0 type 14 offset 961 length 0 bytes, remaining 965

dissect_ssl enter frame #16 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 314
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
  record: offset = 267, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 273, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 32 offset 278 length 3561692 bytes, remaining 314

dissect_ssl enter frame #17 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 84 offset 11 length 1500765 bytes, remaining 47

dissect_ssl enter frame #19 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 318
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 60867 found 0000000000000000
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #20 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 948
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #22 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 393
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 60867 found 0000000000000000
association_find: TCP port 443 found 0000000004D24240

dissect_ssl enter frame #13 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 175
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 166 bytes, remaining 175

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 965
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 965 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 871 bytes, remaining 965 
dissect_ssl3_handshake iteration 0 type 14 offset 961 length 0 bytes, remaining 965

dissect_ssl enter frame #16 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000005771240, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 314
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
  record: offset = 267, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 273, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 32 offset 278 length 3561692 bytes, remaining 314</code></pre></div><div id="question-tags" class="tags-container tags">tlsv1 decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '15, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/d9ee5622062195b1b9c37f37bd0cddae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CPolydorou&#39;s gravatar image" /><p>CPolydorou<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CPolydorou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '15, 14:22</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46641" class="comments-container"></div><div id="comment-tools-46641" class="comment-tools"></div><div class="clear"></div><div id="comment-46641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46648"></span>

<div id="answer-container-46648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46648-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try first to use the snakeoil2 sample capture. <a href="https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=snakeoil2_070531.tgz">https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=snakeoil2_070531.tgz</a></p><p>Are you able to decrypt it ?</p><p>If you can, please upload the key.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '15, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Oct '15, 05:51</p></div></div><div id="comments-container-46648" class="comments-container"><span id="46649"></span><div id="comment-46649" class="comment"><div id="post-46649-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I tried to open the file in the tar archive but there are not packets. The private key is missing also.</p><p>I'm using Wireshark 1.12.8 on Windows.</p></div><div id="comment-46649-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:27)</span> CPolydorou</div></div><span id="46650"></span><div id="comment-46650" class="comment"><div id="post-46650-score" class="comment-score"></div><div class="comment-text"><p>there is a .cap file and the private key inside:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/capture.jpg" alt="alt text" /></p></div><div id="comment-46650-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:36)</span> adasko</div></div><span id="46651"></span><div id="comment-46651" class="comment"><div id="post-46651-score" class="comment-score"></div><div class="comment-text"><p>Never mind, the extension of the file in the archive is missing, that confused me a little bit.</p><p>I can decrypt the sample traffic.</p><p>I run the browser on another VM, where Wireshark is installed.</p><p>Thanks</p></div><div id="comment-46651-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:37)</span> CPolydorou</div></div><span id="46652"></span><div id="comment-46652" class="comment"><div id="post-46652-score" class="comment-score"></div><div class="comment-text"><p>The Private Key uploaded to Wireshark is the one from the VM running IIS, right ?</p></div><div id="comment-46652-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:38)</span> adasko</div></div><span id="46653"></span><div id="comment-46653" class="comment"><div id="post-46653-score" class="comment-score"></div><div class="comment-text"><p>Yes. I've uploaded the files <a href="http://1drv.ms/1GMP3oL">here</a></p></div><div id="comment-46653-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:42)</span> CPolydorou</div></div><span id="46654"></span><div id="comment-46654" class="comment not_top_scorer"><div id="post-46654-score" class="comment-score"></div><div class="comment-text"><p>the .pfx is password protected, can you send it as a pm it to me ?</p></div><div id="comment-46654-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:50)</span> adasko</div></div><span id="46655"></span><div id="comment-46655" class="comment not_top_scorer"><div id="post-46655-score" class="comment-score"></div><div class="comment-text"><p>The password is PasswordForCertificate.</p><p>Sorry, I forgot that.</p><p>I've also updated the file with the certificate in PEM format converted using openssl.</p></div><div id="comment-46655-info" class="comment-info"><span class="comment-age">(18 Oct '15, 03:56)</span> CPolydorou</div></div><span id="46656"></span><div id="comment-46656" class="comment not_top_scorer"><div id="post-46656-score" class="comment-score"></div><div class="comment-text"><p>did you select any other other options beside the default ones ? <img src="https://osqa-ask.wireshark.org/upfiles/option.jpg" alt="alt text" /></p></div><div id="comment-46656-info" class="comment-info"><span class="comment-age">(18 Oct '15, 04:32)</span> adasko</div></div><span id="46657"></span><div id="comment-46657" class="comment not_top_scorer"><div id="post-46657-score" class="comment-score"></div><div class="comment-text"><p>Yes the first and the last ones.</p></div><div id="comment-46657-info" class="comment-info"><span class="comment-age">(18 Oct '15, 04:56)</span> CPolydorou</div></div><span id="46658"></span><div id="comment-46658" class="comment not_top_scorer"><div id="post-46658-score" class="comment-score"></div><div class="comment-text"><p>try to export it the same options selected as on my screenshot. next convert the private key file in PKCS12 format to PEM format:</p><p>openssl pkcs12 -nodes -in your.pfx -out key.pem -nocerts -nodes</p><p>c:\OpenSSL-Win32\bin&gt; openssl rsa -in key.pem -out keyout.pem</p><p>let me know if that works</p></div><div id="comment-46658-info" class="comment-info"><span class="comment-age">(18 Oct '15, 05:02)</span> adasko</div></div><span id="46659"></span><div id="comment-46659" class="comment not_top_scorer"><div id="post-46659-score" class="comment-score"></div><div class="comment-text"><p>I didn't work...</p></div><div id="comment-46659-info" class="comment-info"><span class="comment-age">(18 Oct '15, 05:14)</span> CPolydorou</div></div><span id="46660"></span><div id="comment-46660" class="comment not_top_scorer"><div id="post-46660-score" class="comment-score"></div><div class="comment-text"><p>can you please upload the new files...</p></div><div id="comment-46660-info" class="comment-info"><span class="comment-age">(18 Oct '15, 05:16)</span> adasko</div></div><span id="46663"></span><div id="comment-46663" class="comment not_top_scorer"><div id="post-46663-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to post the link but I get invalid captcha...</p><p>I can't post it here because of SPAM filtering.</p></div><div id="comment-46663-info" class="comment-info"><span class="comment-age">(18 Oct '15, 05:35)</span> CPolydorou</div></div><span id="46664"></span><div id="comment-46664" class="comment not_top_scorer"><div id="post-46664-score" class="comment-score"></div><div class="comment-text"><p>when you open the "keyout.pem" do you see it in the following format:</p><p>-----BEGIN RSA PRIVATE KEY-----</p><p>blablalablablalbalalbalbalbb blablalblalblablalbblblalba..</p><p>-----END RSA PRIVATE KEY-----</p></div><div id="comment-46664-info" class="comment-info"><span class="comment-age">(18 Oct '15, 05:36)</span> adasko</div></div><span id="46665"></span><div id="comment-46665" class="comment not_top_scorer"><div id="post-46665-score" class="comment-score"></div><div class="comment-text"><p>Yes. I've updated the contents of the first file I've shared with the new files.</p><p>Have you tested these files?</p></div><div id="comment-46665-info" class="comment-info"><span class="comment-age">(18 Oct '15, 05:39)</span> CPolydorou</div></div><span id="46668"></span><div id="comment-46668" class="comment not_top_scorer"><div id="post-46668-score" class="comment-score"></div><div class="comment-text"><p>well, I'm still not able to decrypt it. Just to double check, you did the export on the server NOT the client, right ? and you are sure that it's the correct one ?</p></div><div id="comment-46668-info" class="comment-info"><span class="comment-age">(18 Oct '15, 07:36)</span> adasko</div></div><span id="46669"></span><div id="comment-46669" class="comment not_top_scorer"><div id="post-46669-score" class="comment-score"></div><div class="comment-text"><p>Yes. I do not have any other certificates on the server. I also tried with other cipher suites without any luck.</p></div><div id="comment-46669-info" class="comment-info"><span class="comment-age">(18 Oct '15, 08:47)</span> CPolydorou</div></div><span id="46670"></span><div id="comment-46670" class="comment not_top_scorer"><div id="post-46670-score" class="comment-score"></div><div class="comment-text"><p>From <a href="https://wiki.wireshark.org/SSL">https://wiki.wireshark.org/SSL</a></p><p>"The RSA key file can either be a PEM format private key or a PKCS#12 keystore. If the file is a PKCS#12 keystore (typically a file with a .pfx or .p12 extension), the password for the keystore must be specified in the Password field."</p><p>Tried with the .pfx you provided, still no luck. I'm puzzled.</p><p>Will try to reproduce it tomorrow.</p></div><div id="comment-46670-info" class="comment-info"><span class="comment-age">(18 Oct '15, 09:13)</span> adasko</div></div><span id="46671"></span><div id="comment-46671" class="comment not_top_scorer"><div id="post-46671-score" class="comment-score"></div><div class="comment-text"><p>I've tried that also.</p><p>Just tried with Wireshark 2.0.0.rc1 with the same results.</p></div><div id="comment-46671-info" class="comment-info"><span class="comment-age">(18 Oct '15, 09:15)</span> CPolydorou</div></div><span id="46673"></span><div id="comment-46673" class="comment not_top_scorer"><div id="post-46673-score" class="comment-score"></div><div class="comment-text"><p>one note, the certificate and Private Key match (it was mentioned in other posts that a mismatch can cause issues) but this is not the case ... <img src="https://osqa-ask.wireshark.org/upfiles/Capture.JPG.jpg" alt="alt text" /></p></div><div id="comment-46673-info" class="comment-info"><span class="comment-age">(18 Oct '15, 10:04)</span> adasko</div></div><span id="46676"></span><div id="comment-46676" class="comment not_top_scorer"><div id="post-46676-score" class="comment-score"></div><div class="comment-text"><p>guys, please post comments as comments not "answers". I've just spent several minutes of my spare time cleaning up your "answers".</p><p>Please read the FAQ for more information.</p></div><div id="comment-46676-info" class="comment-info"><span class="comment-age">(18 Oct '15, 14:28)</span> grahamb ♦</div></div></div><div id="comment-tools-46648" class="comment-tools"><span class="comments-showing"> showing 5 of 21 </span> <a href="#" class="show-all-comments-link">show 16 more comments</a></div><div class="clear"></div><div id="comment-46648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

