+++
type = "question"
title = "problem decoding SIP TLS - only one side decoded"
description = '''Hi, I&#x27;m having problem with decoding captured SIP TLS connection. I have the server private key. However, after configuring wireshark to decode packets I can see only one side of the connection (for example I can see REGISTER packet) but I can not see the response - it&#x27;s ciphered. Can any one help m...'''
date = "2012-08-14T07:02:00Z"
lastmod = "2012-08-15T00:53:00Z"
weight = 13610
keywords = [ "tlsv1", "sip", "ssl" ]
aliases = [ "/questions/13610" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [problem decoding SIP TLS - only one side decoded](/questions/13610/problem-decoding-sip-tls-only-one-side-decoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13610-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm having problem with decoding captured SIP TLS connection. I have the server private key. However, after configuring wireshark to decode packets I can see only one side of the connection (for example I can see REGISTER packet) but I can not see the response - it's ciphered. Can any one help me?</p><p>Here is a debug of such connection</p><pre><code>Private key imported: KeyID 77:2e:3c:63:01:24:eb:29:8d:ad:35:e5:6d:35:db:a5:...
ssl_init IPv4 addr &#39;10.0.4.63&#39; (10.0.4.63) port &#39;5061&#39; filename &#39;D:\asterisk.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file D:\asterisk.key successfully loaded.
association_add TCP port 5061 protocol sip handle 0000000005B16760

dissect_ssl enter frame #5 (first time)
ssl_session_init: initializing ptr 0000000007071FB8 size 680
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 98
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 93, ssl state 0x00
association_find: TCP port 8003 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 89 bytes, remaining 98 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.0.4.63:5061
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #8 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #9 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x17
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #10 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 2125
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2111, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2107 bytes, remaining 2116 
  record: offset = 2116, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 2121 length 0 bytes, remaining 2125

dissect_ssl enter frame #14 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
pre master encrypted[128]:
5d e9 aa 35 6e e1 12 6c 06 ef 2b c3 03 44 0f 7a 
f4 ed 00 f3 9d 95 93 98 a4 94 3a 35 51 ab 38 ff 
9b a3 69 4e 46 51 c6 5f 53 ef 34 75 c5 fa 99 ef 
4d 4a 7e dc ab 4d b7 80 3e a0 55 cb e3 f2 c0 04 
ff da 57 d6 35 bb 3d 63 aa 4d e0 87 2b 29 58 50 
d4 c0 45 04 f3 2a 6d 06 da c3 e3 6a f9 cd 4b 9e 
03 a0 7b 0f 60 cf dc 9d 9f 29 c7 40 a7 20 f7 5c 
f6 c8 0c 0a 3c d0 7f a5 4f e0 19 2f 47 41 2d 7e 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 79 bytes, decr_len 127
decrypted_unstrip_pre_master[127]:
02 bc 5b 1e a2 bd 1c 4d 26 2c 12 31 af 1b ac 10 
07 e8 a1 f8 93 ea 18 95 8b 9e 64 7f a4 1b 08 52 
a8 34 53 c1 58 f7 be 06 6e eb d3 6d 32 61 e0 d8 
ba f7 62 b8 b0 1e 1a 4d ea 97 ff 05 f9 42 d5 f7 
d4 a6 4c 9f c1 ed e4 94 91 5c 1f 74 d2 5d 00 03 
01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 d2 
24 55 85 48 4b 89 46 23 19 9c 3a 2f e6 a9 79 8f 
47 50 51 1c d1 4d 0e d1 a6 e1 fe 69 7f 32 c8 
pre master secret[48]:
03 01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 
d2 24 55 85 48 4b 89 46 23 19 9c 3a 2f e6 a9 79 
8f 47 50 51 1c d1 4d 0e d1 a6 e1 fe 69 7f 32 c8 
ssl_generate_keyring_material:PRF(pre_master_secret)
pre master secret[48]:
03 01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 
d2 24 55 85 48 4b 89 46 23 19 9c 3a 2f e6 a9 79 
8f 47 50 51 1c d1 4d 0e d1 a6 e1 fe 69 7f 32 c8 
client random[32]:
4e ca e6 1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 
54 53 c5 9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 
server random[32]:
50 2a 58 c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 
1b db 6d bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
03 01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 
d2 24 55 85 48 4b 89 46 
tls_hash: hash seed[77]:
6d 61 73 74 65 72 20 73 65 63 72 65 74 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 
hash out[48]:
df b8 de 0f a1 50 08 a3 0c 78 f5 10 67 e0 d4 ed 
6c 53 89 99 1b 76 f7 62 a6 55 c8 da b6 bf e7 5b 
09 6f 8e ff 90 8c 45 5e 72 96 d0 d4 9e fe a2 e0 
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
23 19 9c 3a 2f e6 a9 79 8f 47 50 51 1c d1 4d 0e 
d1 a6 e1 fe 69 7f 32 c8 
tls_hash: hash seed[77]:
6d 61 73 74 65 72 20 73 65 63 72 65 74 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 
hash out[48]:
8a 99 cc a8 29 36 9e 06 4c 95 0c f3 b2 a0 16 19 
96 5d 60 d2 f8 2d 46 bb 48 10 f8 4b 4f 93 63 4c 
d6 3b fd 72 a7 2a 1f 45 82 7c aa 40 4c ce 69 98 
PRF out[48]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 ee 45 30 91 f9 2c 84 17 
df 54 73 8d 37 a6 5a 1b f0 ea 7a 94 d2 30 cb 78 
master secret[48]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 ee 45 30 91 f9 2c 84 17 
df 54 73 8d 37 a6 5a 1b f0 ea 7a 94 d2 30 cb 78 
ssl_generate_keyring_material sess key generation
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 
tls_hash: hash seed[77]:
6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 
hash out[64]:
85 19 05 4d 00 32 38 02 fd a7 18 7b 63 b6 72 58 
4b 86 4c 98 28 c3 6b d6 f5 61 a1 92 46 b8 a8 65 
34 44 10 96 e2 c5 6c b5 a2 f4 61 5e 68 f0 e6 5e 
e1 6f f4 18 4a 08 9a 48 34 11 78 21 f4 6f eb 62 
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
ee 45 30 91 f9 2c 84 17 df 54 73 8d 37 a6 5a 1b 
f0 ea 7a 94 d2 30 cb 78 
tls_hash: hash seed[77]:
6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 
hash out[64]:
a1 3e f6 ca 12 2e 1d 17 fe d0 8e 89 3a 75 17 24 
6a 9b 50 8c 4d 54 d4 26 0c 58 32 a2 27 65 15 b1 
17 a4 de cc f8 ac fb a0 e6 c1 0a ce 37 33 8a e1 
ec 01 18 90 05 d1 4e 4e 15 76 9e a8 8b b3 0b 56 
PRF out[64]:
24 27 f3 87 12 1c 25 15 03 77 96 f2 59 c3 65 7c 
21 1d 1c 14 65 97 bf f0 f9 39 93 30 61 dd bd d4 
23 e0 ce 5a 1a 69 97 15 44 35 6b 90 5f c3 6c bf 
0d 6e ec 88 4f d9 d4 06 21 67 e6 89 7f dc e0 34 
key expansion[64]:
24 27 f3 87 12 1c 25 15 03 77 96 f2 59 c3 65 7c 
21 1d 1c 14 65 97 bf f0 f9 39 93 30 61 dd bd d4 
23 e0 ce 5a 1a 69 97 15 44 35 6b 90 5f c3 6c bf 
0d 6e ec 88 4f d9 d4 06 21 67 e6 89 7f dc e0 34 
Client MAC key[16]:
24 27 f3 87 12 1c 25 15 03 77 96 f2 59 c3 65 7c 
Server MAC key[16]:
21 1d 1c 14 65 97 bf f0 f9 39 93 30 61 dd bd d4 
Client Write key[16]:
23 e0 ce 5a 1a 69 97 15 44 35 6b 90 5f c3 6c bf 
Server Write key[16]:
0d 6e ec 88 4f d9 d4 06 21 67 e6 89 7f dc e0 34 
Client Write IV[8]:
00 00 00 00 00 00 00 00 
Server Write IV[8]:
c0 d0 27 00 00 00 00 00 
ssl_generate_keyring_material ssl_create_decoder(client)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material ssl_create_decoder(server)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material: client seq 0, server seq 0
ssl_save_session stored session id[32]:
af dd 5f fb 98 29 74 f7 1c 0d 91 37 94 cd 95 8b 
ed 2e f0 b4 ea e0 5a 79 94 31 00 0e a0 e8 b0 89 
ssl_save_session stored master secret[48]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 ee 45 30 91 f9 2c 84 17 
df 54 73 8d 37 a6 5a 1b f0 ea 7a 94 d2 30 cb 78 
dissect_ssl3_handshake session keys successfully generated
  record: offset = 139, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
f3 cc a1 1f 1c 04 c3 04 43 19 84 42 33 8e 0d d4 
77 46 27 74 1a 9c 53 7d 86 cb 79 f9 c5 7d 61 2d 
Plaintext[32]:
14 00 00 0c 07 14 6d 39 0a ad 54 2f af 9e f9 f8 
9a c9 2a 7c 36 69 7d cd 29 bf c8 c0 b0 e5 43 23 
checking mac (len 16, version 301, ct 22 seq 0)
tls_check_mac mac type:MD5 md 1
Mac[16]:
9a c9 2a 7c 36 69 7d cd 29 bf c8 c0 b0 e5 43 23 
ssl_decrypt_record: mac ok
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #15 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
9c 2e 94 9e 40 17 8f 0c 32 d6 28 49 ee 0b b9 86 
f7 f0 a3 d8 30 50 f2 50 3b 55 f0 1d d4 0d 25 8d 
Plaintext[32]:
14 00 00 0c 70 f7 4f f8 13 a2 cc 62 1e 14 d6 ad 
84 9b 01 62 07 02 e7 a0 59 4f fe e2 7a 1a d3 8c 
checking mac (len 16, version 301, ct 22 seq 0)
tls_check_mac mac type:MD5 md 1
Mac[16]:
84 9b 01 62 07 02 e7 a0 59 4f fe e2 7a 1a d3 8c 
ssl_decrypt_record: mac ok
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #16 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 156 offset 11 length 3052702 bytes, remaining 43

dissect_ssl enter frame #18 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 513
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 508, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 508
Ciphertext[508]:
f0 22 9a 0b ec 67 48 1e e9 45 85 8f 17 0c 40 6e 
d1 a6 58 9b 02 98 22 ba 76 d1 a7 b1 80 48 96 a5 
0c 77 78 2c 62 74 20 40 80 ec 3a 6f d9 d5 02 20 
35 8b eb 26 42 8a 6b 17 2d ae 55 59 61 83 48 6f 
f4 6d 45 9f d2 ab 1b e9 ca 90 86 3c d7 8c 04 45 
1a 5b db d0 ec 3d a9 99 37 d9 d0 f0 6a 0e 3b e0 
dc 2d a8 9f 43 31 a5 5f 16 90 68 17 82 c3 56 b4 
fb cf 83 88 55 4e b0 15 ce c8 8b 26 97 b9 bc 3c 
6a 1b e3 9d 3c 84 3d 39 ac 61 72 19 1e 69 1e 01 
44 81 a1 b0 78 a5 4b b0 cb af 98 e6 da f9 4c f5 
07 58 73 10 1e ca ff 9c 52 b9 04 91 0c d9 84 f5 
94 e6 76 fd b3 19 19 ca b8 cd 79 92 8c 4d 60 6a 
da 03 66 d4 7f 80 73 45 45 f7 c1 52 4b 27 9e 8b 
51 f4 0d 9c a3 e0 b2 49 81 0d 4e b0 16 d3 5f 2e 
e5 e9 7f 3a 2e a7 5f 5b 9b 52 08 96 9d 45 f0 73 
70 4c 27 04 cd cc 61 9d 1d a0 e9 c3 59 09 d6 02 
b0 7b f7 64 6c 98 77 f0 ec 2d 7b 1a b6 15 d2 b9 
d3 47 ca 49 6a b7 11 f2 c9 14 93 ee 25 21 5d 06 
37 fb b0 b0 72 36 2a 50 bb d3 42 9b 5c 60 91 20 
16 92 3c 80 df 2e 53 a8 d4 ea 67 ac f2 f2 18 fe 
90 0a fa f6 82 66 3d a3 68 0d 1f 8c 6c f9 1b c0 
78 7f 1b db 9d 1b 9b 0f 67 a2 a8 ba 03 ac fe b7 
3d 75 a4 46 fd d2 96 d0 2f c4 3a 5a 0e 13 a3 2a 
30 a8 91 f9 b5 74 cf b4 62 5f f4 5f 19 46 d6 5a 
17 fd 7b d6 83 08 69 d1 92 49 fd 83 f1 14 60 b6 
cd e1 aa 4c 20 83 04 39 4a 23 db d0 ca 3b b6 8b 
94 4d 9f 48 7c 60 18 f2 31 07 f1 9a cf 08 76 d0 
73 ac 9c d6 f3 ac 26 67 62 6c 7d 12 6b 09 28 28 
99 28 c0 5b 4d 13 a8 ad be fb 43 24 70 4f 1c 48 
c5 91 b3 35 3b 74 fb 6b 98 fb df 0f ef 91 af 24 
e9 22 a2 7a 1b 16 88 ac 9d 9a 85 f8 f3 23 d2 c7 
18 f4 bd 31 e9 7f 02 6a d7 1a 18 9b 
ssl_decrypt_record: allocating 540 bytes for decrypt data (old len 32)
Plaintext[508]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 36 33 33 32 32 31 36 33 30 0d 0a 46 
72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 
31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
3e 3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 36 
0d 0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 30 
30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 
31 3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 30 
35 33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 37 
32 0d 0a 43 53 65 71 3a 20 31 20 52 45 47 49 53 
54 45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 73 
69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 2e 
30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 73 
70 6f 72 74 3d 54 4c 53 3e 0d 0a 41 6c 6c 6f 77 
3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 4f 2c 20 
50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 59 45 2c 
20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 4f 4e 53 
2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 49 53 54 
45 52 2c 20 53 55 42 53 43 52 49 42 45 2c 20 52 
45 46 45 52 2c 20 50 55 42 4c 49 53 48 2c 20 55 
50 44 41 54 45 2c 20 4d 45 53 53 41 47 45 0d 0a 
4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 20 37 30 
0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 59 65 
61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 50 20 32 
2e 36 31 2e 30 2e 37 30 0d 0a 45 78 70 69 72 65 
73 3a 20 36 30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 
65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 8c 2f bf 4e 
df 16 d6 8f 3e b0 cb 65 72 52 e5 28 
checking mac (len 492, version 301, ct 23 seq 1)
tls_check_mac mac type:MD5 md 1
Mac[16]:
8c 2f bf 4e df 16 d6 8f 3e b0 cb 65 72 52 e5 28 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 492, seq = 0, nxtseq = 492
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 492
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK633221630

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #19 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 518, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #20 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 518, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #22 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 677
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 672, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 672
Ciphertext[672]:
6e 67 b7 b4 af ed f2 e2 8e b7 f3 d2 f0 d6 2c 72 
7f c8 06 23 e4 44 98 d0 5c d4 61 9d 8f 80 a5 9b 
ec d8 b0 65 f6 f6 67 8e 1b e0 87 d5 f7 ea eb 78 
dd 3a d8 e1 e5 2d b3 df ed df 09 af 99 ab 5a be 
c7 d0 e9 6e 63 d5 cd 91 ef 30 9e 9d ce 2c d5 56 
19 e2 98 a1 6e 15 0b ce 5f 40 ab dc 1b 48 8d 18 
94 f6 6c 60 ea 1d fa 27 8b 89 e4 7f ed c2 3b 8c 
c3 3a 18 e5 88 7a ee 75 cf 7e cb 64 b4 73 a0 d5 
11 a3 6a 4c 37 56 d3 04 a2 46 33 1e d0 b2 32 e3 
e6 bc 47 be c1 39 bb ff d2 a0 d5 5c 02 f0 dd 97 
c2 bc b6 ff 75 df 15 1d 8d 3b aa ab 43 e3 2e 20 
44 4a 65 99 53 33 75 ce 6f 00 8c 8a 79 01 26 3f 
59 f3 56 ce c7 a1 39 d5 8c 64 f0 c9 5f f3 55 29 
ad be 1a 32 76 e5 da d8 d3 db 03 b5 17 de 9c e4 
80 dc 17 8c 68 89 73 28 13 b0 92 48 4b e1 7d 91 
23 24 c8 be 3e 4c c6 93 59 ff 8a 57 b4 54 66 3e 
a6 bd 93 c4 7d d8 60 1c 59 bb 24 f6 25 da 46 39 
51 2f b7 cb 59 fe 85 76 6c 9a 14 b5 b4 ce 38 2e 
f1 33 99 e1 d0 5a eb 2d 7f cd a4 44 c4 20 de 7b 
c5 19 96 3f 35 94 22 9e 1c e3 b2 fc 36 86 08 95 
a9 cf 07 d0 75 9a 7b f0 ee a8 f7 8f 47 a1 17 e3 
50 46 21 04 56 a8 cb 04 e3 c5 a9 d2 f6 8c 0c e8 
db 08 b8 d0 2d 4f fd ed 61 4a 5e 92 b1 ab 8d fc 
4e 86 c5 94 95 36 13 59 e8 f6 5a c2 bd c2 20 c6 
f5 74 e6 34 26 b1 fc 69 da 48 72 f2 23 4c 71 fc 
c0 af 12 f9 4a e6 dd c6 e8 a8 7f 67 90 52 c1 1e 
a2 bb 78 00 a8 44 36 4a c5 8b d7 97 50 ea f1 10 
30 ac 88 99 4c a6 6d 0a 34 59 99 c8 cf 3e ff a0 
e2 3f ea be 0a f9 05 fc c6 24 91 89 1a b1 a9 23 
8e af 84 0c de 92 67 41 2c c6 86 05 bf 52 46 69 
45 7e 63 61 0a 8c 3b c6 ed a2 40 b3 74 2e 34 ce 
4f d0 41 84 49 29 2b 3a 63 1a 7e 38 40 04 f8 62 
1a ea c5 08 e6 8a 2e 0b 0c 9a 10 f2 1a ff d6 52 
5a 10 22 b8 40 18 cd 66 93 3e 42 f4 d6 43 d1 6a 
9a 86 7f 93 f8 f1 f2 90 3f cc 92 a1 a5 ff 58 7d 
1f 43 90 de 7f 32 bb 2d 3a bf 77 71 32 e3 63 46 
ef 9e a6 99 d2 de 00 74 b8 f3 32 3e 57 af 1d b0 
41 aa 70 fc b0 df e9 54 fc c9 a4 95 73 40 4f d9 
2d ef c8 8b a9 f3 a0 d0 68 13 d6 f0 1d 26 bb 0a 
3e e5 ed 82 40 b1 a4 95 db 2d 47 9e 5c 36 de 71 
ef 2f 56 9a 95 a6 65 aa 6b ab c7 3e b1 35 5d fe 
77 e0 6c 68 c7 87 64 82 4b a7 24 17 5a af 64 2d 
ssl_decrypt_record: allocating 704 bytes for decrypt data (old len 540)
Plaintext[672]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 31 38 34 37 32 38 33 38 38 30 0d 0a 
46 72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 
30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 
31 3e 3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 
36 0d 0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 
30 30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 
36 31 3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 
30 35 33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 
37 32 0d 0a 43 53 65 71 3a 20 32 20 52 45 47 49 
53 54 45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 
73 69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 
2e 30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 
73 70 6f 72 74 3d 54 4c 53 3e 0d 0a 41 75 74 68 
6f 72 69 7a 61 74 69 6f 6e 3a 20 44 69 67 65 73 
74 20 75 73 65 72 6e 61 6d 65 3d 22 74 65 73 74 
30 30 31 22 2c 20 72 65 61 6c 6d 3d 22 43 61 6c 
6c 2d 65 58 22 2c 20 6e 6f 6e 63 65 3d 22 31 33 
35 36 61 37 37 62 22 2c 20 75 72 69 3d 22 73 69 
70 3a 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
22 2c 20 72 65 73 70 6f 6e 73 65 3d 22 37 31 31 
38 65 39 32 32 38 62 65 62 32 37 31 33 34 35 61 
30 66 65 32 62 63 38 61 64 32 33 33 32 22 2c 20 
61 6c 67 6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 41 
6c 6c 6f 77 3a 20 49 4e 56 49 54 45 2c 20 49 4e 
46 4f 2c 20 50 52 41 43 4b 2c 20 41 43 4b 2c 20 
42 59 45 2c 20 43 41 4e 43 45 4c 2c 20 4f 50 54 
49 4f 4e 53 2c 20 4e 4f 54 49 46 59 2c 20 52 45 
47 49 53 54 45 52 2c 20 53 55 42 53 43 52 49 42 
45 2c 20 52 45 46 45 52 2c 20 50 55 42 4c 49 53 
48 2c 20 55 50 44 41 54 45 2c 20 4d 45 53 53 41 
47 45 0d 0a 4d 61 78 2d 46 6f 72 77 61 72 64 73 
3a 20 37 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 
3a 20 59 65 61 6c 69 6e 6b 20 53 49 50 2d 54 32 
38 50 20 32 2e 36 31 2e 30 2e 37 30 0d 0a 45 78 
70 69 72 65 73 3a 20 36 30 0d 0a 43 6f 6e 74 65 
6e 74 2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 
0a 53 eb b7 50 8b 49 11 01 51 1b f2 75 b5 2a 2f 
checking mac (len 656, version 301, ct 23 seq 2)
tls_check_mac mac type:MD5 md 1
Mac[16]:
0a 53 eb b7 50 8b 49 11 01 51 1b f2 75 b5 2a 2f 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 656, seq = 492, nxtseq = 1148
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 656
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1847283880

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #23 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 549, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #24 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 549, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #26 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 904
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 899, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 899
Ciphertext[899]:
2a c5 1c f1 2e d6 04 fc e9 c3 2b b0 a1 ee 76 bf 
48 d3 84 a0 8f 32 e4 bb 5e 66 93 20 eb c8 78 3a 
68 95 45 77 20 66 5c b0 c3 2c 33 fb a9 a1 18 18 
60 8d cd ee 47 8d 5d 4e 98 c7 9f 56 cb f9 63 06 
fb 99 b2 28 60 bc ee 7f 58 ee bd 0a f9 7b 0c ef 
06 77 b3 94 f1 dd 68 2d 96 9f 37 b3 d5 6d 13 5e 
3b 47 8e ab 40 e5 da 71 27 d1 05 90 70 fb e4 4a 
04 0b 35 4c 40 f2 32 89 9b ef 98 2c d3 5b 52 5d 
5d 7f 2b b2 8c 45 cb 5c 29 28 e7 21 0e 76 13 18 
90 18 ba 0e af 21 52 eb 3c f0 c2 1f ec 90 4e 9d 
8f c6 e9 58 05 3a 17 30 0d d4 a3 32 74 15 78 f2 
18 19 dc 96 8b 51 97 8f b0 ab c9 4d 31 1f 7e 82 
9a d5 a8 ac 49 e6 2e 97 e6 14 43 ec 6b 58 ba ab 
82 ff 7a 65 f6 3a 1d 33 bd ee be cb dc 04 46 97 
92 2a 33 c7 40 78 db a8 6e 14 ba b5 20 dd 84 c8 
61 cc 59 7d 47 f8 6e 35 50 c5 8a ff fa cd 0e 24 
e4 6e ca f8 b5 fb 05 7f 01 22 c1 7d 8c 11 4b b2 
b5 06 60 03 05 78 7a 3b 29 be 94 dc b8 c9 58 fd 
28 cb 31 0e 73 63 d7 85 da a2 59 e5 a0 6c 04 fc 
a9 77 ee 41 11 f3 df ad ae c0 3c 06 54 3c 0d 91 
94 a3 12 06 53 81 a4 c0 82 c8 6d f4 4f eb 5d 6a 
e3 cf fd 7b 27 1c 8b bc ea 5a 74 ae b8 17 21 5d 
a7 10 5c 25 cc 74 fb ad 44 bb 3c e5 0e 79 fd f9 
4e 38 0f 38 b1 79 be 33 4d fe 91 ab 2b e2 0a f1 
d0 ac 02 84 f7 9d 51 40 09 b6 51 17 f0 82 1c 74 
75 02 27 f8 84 b0 7e 11 2d 50 02 10 a3 ce 03 73 
63 c4 6d 12 2a d9 c5 a4 6f 4c 08 f4 63 f9 04 82 
26 af 11 e4 14 dc 47 e4 be 99 9c eb 56 59 97 c5 
70 d2 cd 0b 62 9d 15 5b 71 52 67 2f 76 2f b3 52 
1e 40 80 5a 7f 00 f5 b5 c9 7a 9f 31 f3 ca 58 62 
ca 31 34 93 5d 82 e7 2b 7e 9f 21 57 56 5c bc 2f 
0a 09 a8 5b bf 5a c3 c8 f4 ad eb d5 87 fa c3 3e 
36 82 65 43 30 99 51 43 60 44 62 7d 21 5c 0c 0a 
8b 62 84 20 7c 01 af 3d 57 55 8d d0 d9 09 e5 78 
03 2f 1d 73 c3 df 44 69 b9 29 72 a2 e0 44 d5 a9 
44 30 3d d8 2b 64 30 c8 07 f3 11 63 50 49 b8 76 
5a 97 19 42 a4 fe d7 e1 f4 09 67 20 cb 87 67 03 
f3 f6 61 24 40 34 46 78 17 7a a8 53 97 35 9b ef 
35 93 cd 89 f1 7b 94 c4 68 01 87 d4 f8 81 95 af 
c0 0d 42 d2 c6 8e e7 23 e7 96 99 29 dc 86 27 1e 
c6 3e 37 e1 f7 02 39 d3 22 a8 08 30 11 03 c0 91 
1e 12 4d ff 1f eb 8b ad 46 11 ac e0 f6 08 b4 e1 
cb f9 e4 71 1e b9 7b 1e 8e 57 7e 64 af 8a dc e4 
69 58 c8 70 43 46 ae bc 6f d1 6e 83 39 61 a1 7b 
47 f2 7c 76 0e 23 06 b9 3c 6c 37 fa 55 fe cc ae 
cc 89 f3 48 be 61 18 53 0a 5c 01 86 9b 1e f1 f4 
60 fb 66 84 75 df 2e 37 9a 13 af 8f 26 87 91 38 
79 36 18 8a f4 2d 0d 0a 9e 1f 6f 96 6f 14 ca f0 
64 3e 02 0b b5 73 41 3d 50 38 60 ba 0d df a6 fe 
a1 88 ca 99 a6 22 6a 34 64 0d 43 c4 b9 7b c3 f8 
5f 31 a3 35 2b 95 81 ce f5 b3 a4 af 43 9c c8 48 
6a 88 ec dd 4c 98 01 89 43 53 34 69 b3 33 ad 1f 
d4 02 7a 95 ed c5 84 77 a0 67 f1 61 4d 32 d9 13 
e5 52 aa e2 b4 74 6b 62 44 3c 89 4b 59 8b f7 28 
0b 67 d8 ea d9 0a 30 67 c7 02 69 64 18 80 4a 54 
06 e3 49 b4 3b 15 24 92 fd 51 f0 67 14 5c 2b ac 
c8 ba 3a 
ssl_decrypt_record: allocating 931 bytes for decrypt data (old len 704)
Plaintext[899]:
49 4e 56 49 54 45 20 73 69 70 3a 31 32 40 31 30 
2e 30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 
2f 32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 
2e 30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 
32 3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 
68 47 34 62 4b 31 39 39 35 33 39 37 39 38 30 0d 
0a 46 72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 
30 30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 
36 31 3e 3b 74 61 67 3d 36 30 37 34 39 31 33 32 
39 0d 0a 54 6f 3a 20 3c 73 69 70 3a 31 32 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 0d 0a 
43 61 6c 6c 2d 49 44 3a 20 31 30 37 31 31 32 39 
39 35 31 40 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 
43 53 65 71 3a 20 31 20 49 4e 56 49 54 45 0d 0a 
43 6f 6e 74 61 63 74 3a 20 3c 73 69 70 3a 74 65 
73 74 30 30 31 40 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 74 72 61 6e 73 70 6f 72 74 3d 
54 4c 53 3e 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 
70 65 3a 20 61 70 70 6c 69 63 61 74 69 6f 6e 2f 
73 64 70 0d 0a 41 6c 6c 6f 77 3a 20 49 4e 56 49 
54 45 2c 20 49 4e 46 4f 2c 20 50 52 41 43 4b 2c 
20 41 43 4b 2c 20 42 59 45 2c 20 43 41 4e 43 45 
4c 2c 20 4f 50 54 49 4f 4e 53 2c 20 4e 4f 54 49 
46 59 2c 20 52 45 47 49 53 54 45 52 2c 20 53 55 
42 53 43 52 49 42 45 2c 20 52 45 46 45 52 2c 20 
50 55 42 4c 49 53 48 2c 20 55 50 44 41 54 45 2c 
20 4d 45 53 53 41 47 45 0d 0a 4d 61 78 2d 46 6f 
72 77 61 72 64 73 3a 20 37 30 0d 0a 55 73 65 72 
2d 41 67 65 6e 74 3a 20 59 65 61 6c 69 6e 6b 20 
53 49 50 2d 54 32 38 50 20 32 2e 36 31 2e 30 2e 
37 30 0d 0a 53 75 70 70 6f 72 74 65 64 3a 20 72 
65 70 6c 61 63 65 73 0d 0a 41 6c 6c 6f 77 2d 45 
76 65 6e 74 73 3a 20 74 61 6c 6b 2c 68 6f 6c 64 
2c 63 6f 6e 66 65 72 65 6e 63 65 2c 72 65 66 65 
72 2c 63 68 65 63 6b 2d 73 79 6e 63 0d 0a 43 6f 
6e 74 65 6e 74 2d 4c 65 6e 67 74 68 3a 20 33 30 
32 0d 0a 0d 0a 76 3d 30 0d 0a 6f 3d 2d 20 32 30 
30 30 30 20 32 30 30 30 30 20 49 4e 20 49 50 34 
20 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 73 3d 53 
44 50 20 64 61 74 61 0d 0a 63 3d 49 4e 20 49 50 
34 20 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 74 3d 
30 20 30 0d 0a 6d 3d 61 75 64 69 6f 20 31 31 37 
38 30 20 52 54 50 2f 41 56 50 20 30 20 38 20 31 
38 20 39 20 31 30 31 0d 0a 61 3d 72 74 70 6d 61 
70 3a 30 20 50 43 4d 55 2f 38 30 30 30 0d 0a 61 
3d 72 74 70 6d 61 70 3a 38 20 50 43 4d 41 2f 38 
30 30 30 0d 0a 61 3d 72 74 70 6d 61 70 3a 31 38 
20 47 37 32 39 2f 38 30 30 30 0d 0a 61 3d 66 6d 
74 70 3a 31 38 20 61 6e 6e 65 78 62 3d 6e 6f 0d 
0a 61 3d 72 74 70 6d 61 70 3a 39 20 47 37 32 32 
2f 38 30 30 30 0d 0a 61 3d 66 6d 74 70 3a 31 30 
31 20 30 2d 31 35 0d 0a 61 3d 72 74 70 6d 61 70 
3a 31 30 31 20 74 65 6c 65 70 68 6f 6e 65 2d 65 
76 65 6e 74 2f 38 30 30 30 0d 0a 61 3d 70 74 69 
6d 65 3a 32 30 0d 0a 61 3d 73 65 6e 64 72 65 63 
76 0d 0a 10 69 30 60 1b 65 e5 22 93 1f ce 8f 46 
28 01 a0 
checking mac (len 883, version 301, ct 23 seq 3)
tls_check_mac mac type:MD5 md 1
Mac[16]:
10 69 30 60 1b 65 e5 22 93 1f ce 8f 46 28 01 a0 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 883, seq = 1148, nxtseq = 2031
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 883
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #27 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 512, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #28 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 512, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #30 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 275
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 270, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 270
Ciphertext[270]:
13 9f d1 a9 be bb c9 d3 40 1b ab 82 25 09 19 5c 
a4 18 2f c4 26 f3 44 5c b2 32 50 9c 52 67 9d c9 
a5 19 41 4e dd b5 05 ec 55 da ba 7f 84 b6 17 a7 
87 03 12 5e f8 13 a4 c4 fa 61 f4 91 14 f7 74 e8 
22 00 7f 5c 93 d5 a7 a7 15 fc 0b 00 6e 68 1d 59 
f7 e0 a2 26 78 05 15 d9 5e 26 62 67 1d b2 73 82 
88 4d 4f c6 59 a3 32 c0 6a 80 31 b9 af 92 1d da 
29 b4 4e ad f8 bc 8a 31 f6 3a 12 05 6f 2d a3 4e 
a2 38 f1 83 9d 8c f8 01 a0 40 cd e2 53 af 8f 44 
57 e3 9e 24 bb 72 68 ac 6d 95 41 18 c4 a7 70 d0 
32 98 af 49 97 42 08 d2 ea d7 95 81 1a 6f c1 76 
f3 47 a4 77 11 b6 99 9c aa 90 2d f6 03 99 8c 4b 
29 a7 df c6 1e fb e6 85 09 7d 0f 42 55 2a 0e 16 
bd fd b6 fa eb 06 77 bc e9 5c ed 2b ca 50 9b 10 
dc 83 02 b7 30 a8 96 d9 08 f8 45 83 09 5d 75 a4 
ce 42 6e 8b 5f 99 60 40 5e 78 94 df 09 6f e5 08 
e7 30 92 f0 dc 92 dc 48 c8 8d ba 1e b4 53 
Plaintext[270]:
41 43 4b 20 73 69 70 3a 31 32 40 31 30 2e 30 2e 
34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 32 2e 
30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 30 2f 
54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 3a 35 
30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 47 34 
62 4b 31 39 39 35 33 39 37 39 38 30 0d 0a 46 72 
6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 31 
40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 
3b 74 61 67 3d 36 30 37 34 39 31 33 32 39 0d 0a 
54 6f 3a 20 3c 73 69 70 3a 31 32 40 31 30 2e 30 
2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 3d 
61 73 35 38 31 38 30 32 35 63 0d 0a 43 61 6c 6c 
2d 49 44 3a 20 31 30 37 31 31 32 39 39 35 31 40 
31 30 2e 30 2e 30 2e 31 37 32 0d 0a 43 53 65 71 
3a 20 31 20 41 43 4b 0d 0a 43 6f 6e 74 65 6e 74 
2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a e9 24 
cb 24 90 ab ce 06 e4 77 f9 01 3e 49 59 02 
checking mac (len 254, version 301, ct 23 seq 4)
tls_check_mac mac type:MD5 md 1
Mac[16]:
e9 24 cb 24 90 ab ce 06 e4 77 f9 01 3e 49 59 02 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 254, seq = 2031, nxtseq = 2285
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 254
decrypted app data fragment: ACK sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as5818025c

Call-ID: [email protected]

CSeq: 1 ACK

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #33 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 1070
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1065, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 1065
Ciphertext[1065]:
af ec ba 53 3b a6 5c 51 6d b5 35 6b 35 14 cc a2 
c9 04 ab 47 2c 34 73 d5 eb 71 d6 56 bb 40 df ca 
72 26 fa 13 ce cd 33 e7 b2 a0 81 ad bc df 88 43 
82 06 5a 05 d7 1d 01 cc 5c bc de 42 43 2c 66 53 
fd b1 69 36 db d4 f6 c8 6d fe 28 fb d6 a2 6e 4a 
92 c1 f7 28 f0 4a 73 5a 26 85 51 af 1c 94 0a 1f 
1c b1 e5 98 c0 d8 f7 79 0c 4e 05 5b 39 a9 08 b4 
ed 22 94 47 70 d7 ea 8c 22 c9 92 26 f5 af b6 1f 
db 1a 6f 90 28 1a db 97 43 fb de f5 df 66 02 5d 
d0 ae 99 e2 32 8c 60 57 b9 41 f3 56 f8 db cc 17 
cb 48 3d cc 18 40 c8 11 57 8d 71 ca 21 08 ef eb 
da 7b ea 32 a2 8b c3 bd be 2b 79 f2 55 4a 34 e9 
ee 8a ca 95 32 32 96 d6 c9 4d 5d 88 cb 59 f7 95 
68 5c fa 0c f1 1d fb 95 46 8c 7e b3 43 9e 25 27 
c0 7b 4e 6b 82 96 07 7c 76 b5 a2 49 41 66 f6 e0 
04 ca 88 6b 36 78 15 89 cb 00 14 a3 ec e1 b6 80 
89 9a dd 65 37 9f e0 41 b9 6c 00 e5 76 65 d1 ae 
78 9b dd 36 93 7a c5 6f ad 96 f9 fa 54 98 3d 4a 
a0 57 b7 d1 93 28 b6 b1 50 ea 67 87 56 70 f0 9f 
36 c2 44 fe 94 e8 b4 69 a9 70 f0 14 6f 03 8a 9a 
37 29 24 17 04 a6 83 bf ee 37 89 ca 64 f3 b6 ea 
8d aa 4e 28 ba d4 7b 98 0f 95 1b d8 3c ae aa 7c 
b4 20 b4 b8 96 c1 a8 84 c7 85 2b 48 6b e2 3a fa 
d6 3b e0 7d ef f7 e9 79 ca 7c 31 c6 09 5a db 80 
01 8c da 6c 10 cd 40 e6 8c 18 fe d1 42 8a 91 7c 
c7 8c 70 68 5b f9 2f e9 81 5a 75 78 c8 14 0a ed 
be a4 16 da 68 8b 52 1b 37 83 d1 ba 28 f5 82 f7 
ee 01 d5 41 2e a6 15 ae 67 cf 17 ca ec 78 73 c9 
3f 7e 3c 25 bc 60 1a 28 0e e1 9c 3d 53 05 aa b3 
7e 17 c1 f9 c5 f9 62 cf bc bd 9a e8 81 21 10 e2 
2e 22 80 67 da bb 71 10 05 c0 a4 cc 3b 52 86 6b 
85 40 d7 44 9f 1c eb a2 aa 03 b6 98 44 6b 42 29 
fe 85 9c 77 22 06 ff 81 1d 5a b8 ac 0f 9a 65 39 
1f 01 02 54 0f f1 eb 83 a1 d6 47 d8 77 59 a6 ff 
38 ec 4b 55 87 58 0f ac d9 af 33 cf 0a a0 d7 07 
68 2d 69 e1 84 96 41 ed 38 34 a9 4d 20 32 d3 cd 
39 09 7d bd 67 87 c4 4a d7 d9 79 0f f2 22 ba 06 
dd e3 00 fa f7 9c cd 3a 31 36 5d c0 e2 e4 ce d2 
5d 10 f3 08 a9 8b 11 78 ee a7 92 85 27 e3 c8 db 
00 f3 b6 a7 9c 07 d4 cd b0 ef 31 19 bc 50 32 18 
fe d6 9b 4e 9d e3 c0 90 15 ba 30 05 8c 93 8f 38 
01 96 a8 ca aa 3d d0 5b c0 91 69 24 c8 9c 58 8c 
47 b5 f6 4a af d2 f4 bd b1 b1 1f 59 52 7b e0 bd 
e4 a0 75 a6 15 6f 3c 8a b3 2b 8f 52 38 f1 be 0c 
35 3d 92 29 93 4d 69 be 7b e8 dc c8 1e b4 e4 b8 
23 dd 2c a3 85 99 16 d1 4c be 88 fe 4c 95 db 92 
00 ae 57 7a f6 49 b2 cb 5f f4 0d ca 35 10 d5 71 
dc ca 24 98 7a 01 8f 6f 19 54 54 34 e1 b2 14 d7 
6a 7b 90 cd 1d b2 9a fd 48 bd 36 93 53 56 9b 2a 
38 ea 37 52 ab 82 87 17 15 4a 52 eb 69 80 ae 7c 
30 68 c8 20 c7 76 43 a6 e1 c9 bb 6e 38 11 23 63 
fb 6b 22 24 3f 63 97 31 d2 fe a4 07 4d 68 d8 96 
d7 38 60 f4 65 b0 c6 5c 91 23 22 04 39 d8 f7 dc 
3f a0 28 65 ce d8 f7 41 90 02 2d 99 5c 6f 29 71 
cd fb a9 d5 73 13 c8 32 6f 8f dc 74 ec e3 ff 1c 
8f 70 f5 3a 86 4d 9f bd 6e 05 9e da 52 0b b0 7d 
bc 96 5f 29 2c 7f 04 ad 61 2e 17 59 5f ff 7f fc 
3f 42 94 49 f7 d5 71 84 10 46 43 ed 8a e9 3c e9 
d7 a9 61 67 97 e5 0a 3e b6 02 44 3f 7f 1b 91 5a 
af 1a e1 3f 16 08 51 7c e2 70 48 67 6d f5 4d d5 
2d 60 07 2c bd 75 ff 06 e3 f0 df bd 22 0d 48 14 
fb d5 a3 c3 d2 9b 05 f8 db 2a f7 51 48 ad 2c d3 
a9 aa 2a 06 16 3c d6 0a 76 02 93 f0 57 05 6f eb 
4c ce 3e dc 11 50 c3 ea f1 e2 e4 35 94 29 97 22 
06 e8 aa 82 27 43 de e2 4c 9a 41 8e e5 23 cd 31 
e6 cf b9 a1 dc 30 92 d9 95 4a b6 e8 05 fd 0a 4a 
c2 43 62 c6 b6 bf 2c f1 df 
ssl_decrypt_record: allocating 1097 bytes for decrypt data (old len 931)
Plaintext[1065]:
49 4e 56 49 54 45 20 73 69 70 3a 31 32 40 31 30 
2e 30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 
2f 32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 
2e 30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 
32 3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 
68 47 34 62 4b 31 38 31 31 34 35 38 35 35 38 0d 
0a 46 72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 
30 30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 
36 31 3e 3b 74 61 67 3d 36 30 37 34 39 31 33 32 
39 0d 0a 54 6f 3a 20 3c 73 69 70 3a 31 32 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 0d 0a 
43 61 6c 6c 2d 49 44 3a 20 31 30 37 31 31 32 39 
39 35 31 40 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 
43 53 65 71 3a 20 32 20 49 4e 56 49 54 45 0d 0a 
43 6f 6e 74 61 63 74 3a 20 3c 73 69 70 3a 74 65 
73 74 30 30 31 40 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 74 72 61 6e 73 70 6f 72 74 3d 
54 4c 53 3e 0d 0a 41 75 74 68 6f 72 69 7a 61 74 
69 6f 6e 3a 20 44 69 67 65 73 74 20 75 73 65 72 
6e 61 6d 65 3d 22 74 65 73 74 30 30 31 22 2c 20 
72 65 61 6c 6d 3d 22 43 61 6c 6c 2d 65 58 22 2c 
20 6e 6f 6e 63 65 3d 22 35 33 61 34 61 36 34 39 
22 2c 20 75 72 69 3d 22 73 69 70 3a 31 32 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 22 2c 20 
72 65 73 70 6f 6e 73 65 3d 22 34 35 38 61 31 32 
38 63 31 30 30 63 32 61 31 34 36 37 65 37 61 36 
35 63 34 66 30 62 66 63 35 62 22 2c 20 61 6c 67 
6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 43 6f 6e 74 
65 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 
61 74 69 6f 6e 2f 73 64 70 0d 0a 41 6c 6c 6f 77 
3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 4f 2c 20 
50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 59 45 2c 
20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 4f 4e 53 
2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 49 53 54 
45 52 2c 20 53 55 42 53 43 52 49 42 45 2c 20 52 
45 46 45 52 2c 20 50 55 42 4c 49 53 48 2c 20 55 
50 44 41 54 45 2c 20 4d 45 53 53 41 47 45 0d 0a 
4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 20 37 30 
0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 59 65 
61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 50 20 32 
2e 36 31 2e 30 2e 37 30 0d 0a 53 75 70 70 6f 72 
74 65 64 3a 20 72 65 70 6c 61 63 65 73 0d 0a 41 
6c 6c 6f 77 2d 45 76 65 6e 74 73 3a 20 74 61 6c 
6b 2c 68 6f 6c 64 2c 63 6f 6e 66 65 72 65 6e 63 
65 2c 72 65 66 65 72 2c 63 68 65 63 6b 2d 73 79 
6e 63 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65 6e 67 
74 68 3a 20 33 30 32 0d 0a 0d 0a 76 3d 30 0d 0a 
6f 3d 2d 20 32 30 30 30 30 20 32 30 30 30 30 20 
49 4e 20 49 50 34 20 31 30 2e 30 2e 30 2e 31 37 
32 0d 0a 73 3d 53 44 50 20 64 61 74 61 0d 0a 63 
3d 49 4e 20 49 50 34 20 31 30 2e 30 2e 30 2e 31 
37 32 0d 0a 74 3d 30 20 30 0d 0a 6d 3d 61 75 64 
69 6f 20 31 31 37 38 30 20 52 54 50 2f 41 56 50 
20 30 20 38 20 31 38 20 39 20 31 30 31 0d 0a 61 
3d 72 74 70 6d 61 70 3a 30 20 50 43 4d 55 2f 38 
30 30 30 0d 0a 61 3d 72 74 70 6d 61 70 3a 38 20 
50 43 4d 41 2f 38 30 30 30 0d 0a 61 3d 72 74 70 
6d 61 70 3a 31 38 20 47 37 32 39 2f 38 30 30 30 
0d 0a 61 3d 66 6d 74 70 3a 31 38 20 61 6e 6e 65 
78 62 3d 6e 6f 0d 0a 61 3d 72 74 70 6d 61 70 3a 
39 20 47 37 32 32 2f 38 30 30 30 0d 0a 61 3d 66 
6d 74 70 3a 31 30 31 20 30 2d 31 35 0d 0a 61 3d 
72 74 70 6d 61 70 3a 31 30 31 20 74 65 6c 65 70 
68 6f 6e 65 2d 65 76 65 6e 74 2f 38 30 30 30 0d 
0a 61 3d 70 74 69 6d 65 3a 32 30 0d 0a 61 3d 73 
65 6e 64 72 65 63 76 0d 0a a9 eb bd 38 80 79 97 
4f a3 d5 9c 57 e3 df 03 9a 
checking mac (len 1049, version 301, ct 23 seq 5)
tls_check_mac mac type:MD5 md 1
Mac[16]:
a9 eb bd 38 80 79 97 4f a3 d5 9c 57 e3 df 03 9a 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 1049, seq = 2285, nxtseq = 3334
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 1049
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1811458558

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;53a4a649&quot;, uri=&quot;sip:[email protected]:5061&quot;, response=&quot;458a128c100c2a1467e7a65c4f0bfc5b&quot;, algorithm=MD5

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #36 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 464, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #37 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 464, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #39 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 485
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 480, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #40 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 485
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 480, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #42 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 675
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 670, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 670
Ciphertext[670]:
5f f9 62 c0 eb c7 e4 26 bc 27 bf 3b c4 7d 72 97 
ab 31 07 46 56 fb 67 db 5e 1d 90 1c ab 70 b1 5a 
ba 79 8b 74 02 39 69 81 87 f5 96 e9 3b 18 1c 1c 
ca cd db fc ea 7d 0d c2 e3 08 23 2c 17 0b b2 34 
02 95 d0 f0 38 4e 54 f6 2d 9c 8e c5 f7 78 e7 51 
ca 44 24 ef 68 4a 34 8d b2 3b 26 d5 b2 72 71 9c 
40 a0 2b 17 28 1a bd 5c 9f 91 d8 03 4c 73 d7 eb 
75 1e 52 14 bc af 6b 45 67 41 d4 a5 df 54 67 de 
f2 8f 86 6f dc b5 50 8a c9 b2 aa 8d 88 b5 79 21 
57 91 a9 58 1d 29 8e 2a a1 92 34 10 b4 a8 b3 7e 
b6 89 bf 06 69 0d b1 1e ec 9a e0 00 a0 a4 fd 25 
a1 a5 48 8b 7b 03 a6 5f 5a f3 40 52 e5 04 82 0f 
5d e3 61 af 45 17 95 5b 03 0d 31 29 1d 42 7e 41 
33 ed 5a 34 68 c0 1d 02 c1 80 b5 73 04 1c 71 d0 
a7 c3 ab 8b a9 c4 56 67 2b 6c 25 6c dc 2c 23 fa 
8d 69 17 e8 75 fe 0f c0 a0 8c fb a2 88 de d8 1f 
63 2a 7f 73 87 5a 14 ab 5f cd f0 53 1c cd 35 fb 
d1 c9 1d 15 59 26 b1 7d c3 ce 8d ef a5 5b 7e f2 
1b e8 77 31 58 41 c0 37 e8 37 b2 cc ac d3 92 e6 
ec 18 df df b0 53 bc 2d d3 a2 2c 0f c1 25 32 25 
ff 83 a6 f5 54 0a ca b7 9f 0e fe 2d 68 fa be 33 
b9 37 09 0c 40 00 c2 b3 9d f3 19 c9 3b cd 7c 17 
0b af c8 69 e0 eb 5f 9e ad e7 31 4b 1c d7 24 31 
64 22 20 08 5c 83 f0 aa f1 a1 94 25 03 9c 29 20 
9d 1e cd c4 ea 85 38 a6 f8 91 e8 3e c6 60 fa 7c 
04 88 6c d2 d4 db 65 ed 8c bc c2 d3 e4 db 8a ba 
c6 b2 a8 3b 74 2c 03 d5 f5 f5 c6 a7 04 de ef a7 
82 41 45 53 ec 4f 73 55 e1 ab 9e aa c6 86 68 8f 
1a 0f 6e 81 09 f1 41 d4 f1 54 39 93 63 76 2f b8 
6f ae 6f d0 79 53 8c 83 f6 0d 66 b0 ef 25 b0 3d 
f3 67 46 ed 3e 49 36 dc 05 e8 05 7c 08 6a 04 6d 
e0 74 72 7c 54 15 d5 cf 8c a4 25 4b 6e 24 c9 13 
15 c2 3e 73 c3 39 51 c0 58 35 8a 28 8f c8 68 ce 
35 9d 36 20 53 1b ed f9 1d ae 20 32 f8 ee 70 51 
b2 74 db ac 0c f0 ae db 64 9d cd 67 e9 56 f4 97 
65 38 4d 30 30 31 67 9f 96 d9 d0 92 2a 2d 25 03 
a3 87 dc 74 80 2d 7d 3f 98 f8 6e c8 e4 3f 01 de 
8a ce 84 8a 45 c6 77 53 04 92 bc 7b 84 08 82 c2 
2a ab 83 cf f1 a3 67 87 54 2f 2d 50 37 fb ad 46 
20 6f 60 ad 2c b9 2a 97 a9 5a 61 8f 7b ff 37 76 
f3 1f 7c ce 10 e6 91 52 9e 28 73 b4 3d 49 4f f9 
2f 49 af 4d 34 40 e6 c6 64 d5 3f ac b3 69 
Plaintext[670]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 38 34 36 38 31 39 33 34 0d 0a 46 72 
6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 31 
40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 
3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 36 0d 
0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 
31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 30 35 
33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 37 32 
0d 0a 43 53 65 71 3a 20 33 20 52 45 47 49 53 54 
45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 73 69 
70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 2e 30 
2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 73 70 
6f 72 74 3d 54 4c 53 3e 0d 0a 41 75 74 68 6f 72 
69 7a 61 74 69 6f 6e 3a 20 44 69 67 65 73 74 20 
75 73 65 72 6e 61 6d 65 3d 22 74 65 73 74 30 30 
31 22 2c 20 72 65 61 6c 6d 3d 22 43 61 6c 6c 2d 
65 58 22 2c 20 6e 6f 6e 63 65 3d 22 31 33 35 36 
61 37 37 62 22 2c 20 75 72 69 3d 22 73 69 70 3a 
31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 22 2c 
20 72 65 73 70 6f 6e 73 65 3d 22 37 31 31 38 65 
39 32 32 38 62 65 62 32 37 31 33 34 35 61 30 66 
65 32 62 63 38 61 64 32 33 33 32 22 2c 20 61 6c 
67 6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 41 6c 6c 
6f 77 3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 4f 
2c 20 50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 59 
45 2c 20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 4f 
4e 53 2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 49 
53 54 45 52 2c 20 53 55 42 53 43 52 49 42 45 2c 
20 52 45 46 45 52 2c 20 50 55 42 4c 49 53 48 2c 
20 55 50 44 41 54 45 2c 20 4d 45 53 53 41 47 45 
0d 0a 4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 20 
37 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 
59 65 61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 50 
20 32 2e 36 31 2e 30 2e 37 30 0d 0a 45 78 70 69 
72 65 73 3a 20 36 30 0d 0a 43 6f 6e 74 65 6e 74 
2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 25 cd 
a4 2f 59 43 78 84 74 8c 2f 76 2f 93 74 85 
checking mac (len 654, version 301, ct 23 seq 6)
tls_check_mac mac type:MD5 md 1
Mac[16]:
25 cd a4 2f 59 43 78 84 74 8c 2f 76 2f 93 74 85 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 654, seq = 3334, nxtseq = 3988
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 654
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK84681934

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 3 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #43 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 534
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 529, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #44 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 534
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 529, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #46 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 676
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 671, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 671
Ciphertext[671]:
83 9d d3 77 35 8e 56 17 f6 7a 30 e7 fb d9 34 23 
5b 71 9d 28 aa d8 ed 8f ab a9 13 e4 37 e9 f4 03 
fb a1 72 11 94 36 d3 64 7d 51 42 a7 16 1d 2e 83 
4e fd 86 b6 5f de f2 7c 56 fd 0d 8a 41 36 10 d5 
fd 32 39 8a 81 bc 18 d9 57 13 57 15 78 68 68 19 
9b 82 45 1d 2f 1e f7 1e 70 33 5b 4e ea 28 40 68 
3b af 53 3d f6 cc 47 97 c0 3c 63 ea e4 55 6b d3 
a6 15 f4 46 bb e9 7d 53 0d 19 ea ee 09 1c e7 74 
35 75 6c 0e f8 f8 d6 a4 01 81 60 cf 1f b3 f9 bc 
27 f9 12 c7 3a fc 04 dd 98 43 e3 2d 56 c9 27 12 
75 c9 0f f8 2e 48 c6 a7 8d 0d 7a 79 c3 8a 4d 3c 
8c 06 7d 96 76 2b 3f e1 f1 07 60 fc a9 ba e7 d1 
ea f1 43 a6 4a a0 cd e8 b0 0c f0 a4 9d 2e 3b 3c 
19 52 da 42 c1 c2 a7 4c 32 4a 58 b7 aa 37 cd 9f 
e3 80 ca fe 9a 9e 1b 55 70 d3 9e 7f 76 8c ab 63 
44 8b 1a 9b fc 02 6f df 62 b9 47 1b b9 74 16 15 
a4 14 79 4f 13 ef 2d 3f 8c 27 24 d9 60 fd 8c 46 
d5 ad a3 a5 a3 d1 dd 3f 16 02 8f 3d de 8d 63 7a 
63 66 ae 2e 01 99 63 ca 18 1b 54 05 5d 9e 0d 67 
67 60 f5 d6 4e 58 1b 5a 0a 3e ad 53 4f b7 30 59 
4a 36 2f 66 20 c3 f0 bf bf 6b 8e 2d 90 39 55 fd 
7c 7a 96 7a 8b 7c 53 d3 bb dc ee ba 55 1b cf 69 
8a df 1a b9 56 b8 c4 b0 26 40 1a 09 6a c4 b5 5b 
c4 ed 2e d8 d4 0c 09 6a dd 1e d7 6f 29 63 b9 19 
9c 0d 5e f6 1e 91 43 0d a6 c8 ba 5b 32 a3 7c df 
78 c3 9b 2a d9 77 a1 2f aa 01 37 14 5d 96 da 4c 
7e 73 1a c5 30 f6 f5 5a 0b 09 0f a9 ae fd 8a e2 
75 c2 7b b4 c5 78 3c 22 60 22 cb 44 62 28 80 d8 
15 17 6b e4 f8 02 76 9a a7 4f b6 3b 94 20 b1 18 
44 9f e4 0f 3c 8a c5 1a 06 a5 4d e6 58 49 ee d3 
8d 24 d6 f7 65 55 27 67 89 4b e5 70 3d d9 75 3a 
f7 eb cb 07 cb 6c c7 41 7e 18 24 42 3b 8a 78 45 
79 b6 6f ee 14 0c 03 85 b3 c1 72 1b f0 85 af 01 
61 27 54 1b e7 08 37 0d c6 5d 97 ed 48 05 2c a1 
ff 50 ef 0e f2 28 86 2d 3b b1 1c cf 35 1f b2 9f 
7b d1 e8 85 40 aa d1 c0 b5 fe 6e 8d 91 ae d6 e3 
d1 70 ce 3c 19 80 05 09 61 8d 1f 51 70 2c 43 bb 
81 ae a3 29 e8 aa 04 16 81 49 22 86 5b 32 1d 5e 
9c 7b 50 d8 ea 36 96 09 e9 95 05 b8 aa f3 ea 3a 
3b 4a 49 f5 73 47 9a 7f 38 18 00 c7 06 24 3a cb 
83 56 97 d0 0c f0 9c 38 09 5e f3 96 c0 30 88 f0 
c4 8b 39 34 6d f8 f3 c6 4e c0 22 35 56 ba 11 
Plaintext[671]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 39 36 32 35 34 33 37 31 34 0d 0a 46 
72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 
31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
3e 3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 36 
0d 0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 30 
30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 
31 3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 30 
35 33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 37 
32 0d 0a 43 53 65 71 3a 20 34 20 52 45 47 49 53 
54 45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 73 
69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 2e 
30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 73 
70 6f 72 74 3d 54 4c 53 3e 0d 0a 41 75 74 68 6f 
72 69 7a 61 74 69 6f 6e 3a 20 44 69 67 65 73 74 
20 75 73 65 72 6e 61 6d 65 3d 22 74 65 73 74 30 
30 31 22 2c 20 72 65 61 6c 6d 3d 22 43 61 6c 6c 
2d 65 58 22 2c 20 6e 6f 6e 63 65 3d 22 30 34 61 
38 62 32 33 33 22 2c 20 75 72 69 3d 22 73 69 70 
3a 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 22 
2c 20 72 65 73 70 6f 6e 73 65 3d 22 34 64 39 66 
36 30 30 31 36 64 32 37 63 38 38 31 64 30 62 34 
32 35 34 63 35 34 63 61 38 64 38 30 22 2c 20 61 
6c 67 6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 41 6c 
6c 6f 77 3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 
4f 2c 20 50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 
59 45 2c 20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 
4f 4e 53 2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 
49 53 54 45 52 2c 20 53 55 42 53 43 52 49 42 45 
2c 20 52 45 46 45 52 2c 20 50 55 42 4c 49 53 48 
2c 20 55 50 44 41 54 45 2c 20 4d 45 53 53 41 47 
45 0d 0a 4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 
20 37 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 
20 59 65 61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 
50 20 32 2e 36 31 2e 30 2e 37 30 0d 0a 45 78 70 
69 72 65 73 3a 20 36 30 0d 0a 43 6f 6e 74 65 6e 
74 2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 9d 
dd fb ba 35 9a b3 b4 32 82 63 85 9d 8a 96 11 
checking mac (len 655, version 301, ct 23 seq 7)
tls_check_mac mac type:MD5 md 1
Mac[16]:
9d dd fb ba 35 9a b3 b4 32 82 63 85 9d 8a 96 11 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 655, seq = 3988, nxtseq = 4643
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 655
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK962543714

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 4 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;04a8b233&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;4d9f60016d27c881d0b4254c54ca8d80&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #47 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 553
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 548, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #48 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 553
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 548, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #50 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 784
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 779, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #51 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 784
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 779, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #55 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 401
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 396, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 396
Ciphertext[396]:
d1 df 6e 63 67 3d 5e b1 2b ec b0 f8 50 af eb 6d 
6f 90 59 18 2f b3 e7 70 b8 1f 67 db 5b 87 11 c7 
d9 c1 28 54 2f 25 c6 a5 d0 ef b1 ac bf 71 f7 b5 
ed bc 65 d1 58 05 1e 2b bc ac e7 09 ff 09 78 c0 
17 9d b4 32 c8 4b c7 f6 f7 94 40 fe d6 af 54 6c 
ca 4d b5 ec 4d 44 85 9d 1a 3a 0e 0d a5 56 99 5d 
7e 21 86 ed 12 a1 33 47 a1 b8 83 29 8d e9 8f 3a 
01 10 62 d1 99 77 65 b6 d7 8a e9 e6 b9 a8 ef 3e 
db 88 6b 91 91 87 8f ce ba 4e df 1b ad 18 4f d4 
65 b3 91 86 22 2f 5f 27 83 68 07 2e 42 ff 7c 70 
a0 7f 9a 2d 90 2f 07 3c b9 b0 54 66 d1 53 d7 c7 
18 48 8d 48 b2 91 2f 2d 2e 51 ac 04 2b ef e1 ac 
98 66 3a 49 ea 67 a6 f9 d8 e3 8f 70 fe 50 1d b9 
1c 1f 84 8e bb 60 ac 40 8e b5 bb 50 36 12 bd 86 
99 06 a0 ca e6 29 93 4e 33 03 0d f5 27 a6 6e 50 
49 b6 14 75 e5 8c ee f4 ee 65 5b 94 56 2c 65 c8 
ec 5e aa e6 b3 96 56 db a5 81 25 57 d7 91 be 37 
90 e2 c3 24 18 e8 91 af da 52 bd cd f4 02 6e bd 
78 d9 68 07 fc 69 99 f8 a3 ba 36 54 59 32 ce 9e 
28 4f fd b6 cc e9 cd f2 9a ef 55 01 2d a3 b4 21 
81 3b 33 ca db d9 45 4d 53 d2 05 a0 d0 d8 0e ee 
1b 8a a1 08 4a 42 64 3a f5 84 85 9a bf 61 de 6c 
60 f4 67 36 b7 a8 fb d4 50 27 4f 0b d8 46 b4 cf 
0e 4a 7e 00 6e 5f 2b 48 28 29 bd 32 62 ce f0 50 
a5 ed b1 74 20 1f 1c c2 59 19 7a 7e 
Plaintext[396]:
41 43 4b 20 73 69 70 3a 31 32 40 31 30 2e 30 2e 
34 2e 36 33 3a 35 30 36 31 3b 74 72 61 6e 73 70 
6f 72 74 3d 54 4c 53 20 53 49 50 2f 32 2e 30 0d 
0a 56 69 61 3a 20 53 49 50 2f 32 2e 30 2f 54 4c 
53 20 31 30 2e 30 2e 30 2e 31 37 32 3a 35 30 36 
32 3b 62 72 61 6e 63 68 3d 7a 39 68 47 34 62 4b 
31 39 36 37 33 37 39 36 39 35 0d 0a 46 72 6f 6d 
3a 20 3c 73 69 70 3a 74 65 73 74 30 30 31 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 
61 67 3d 36 30 37 34 39 31 33 32 39 0d 0a 54 6f 
3a 20 3c 73 69 70 3a 31 32 40 31 30 2e 30 2e 34 
2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 3d 61 73 
33 34 33 35 39 36 37 62 0d 0a 43 61 6c 6c 2d 49 
44 3a 20 31 30 37 31 31 32 39 39 35 31 40 31 30 
2e 30 2e 30 2e 31 37 32 0d 0a 43 53 65 71 3a 20 
32 20 41 43 4b 0d 0a 43 6f 6e 74 61 63 74 3a 20 
3c 73 69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 
30 2e 30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 
6e 73 70 6f 72 74 3d 54 4c 53 3e 0d 0a 4d 61 78 
2d 46 6f 72 77 61 72 64 73 3a 20 37 30 0d 0a 55 
73 65 72 2d 41 67 65 6e 74 3a 20 59 65 61 6c 69 
6e 6b 20 53 49 50 2d 54 32 38 50 20 32 2e 36 31 
2e 30 2e 37 30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 
65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 9e cd b7 a4 
64 c7 80 6b c9 d1 69 66 d0 2e d1 53 
checking mac (len 380, version 301, ct 23 seq 8)
tls_check_mac mac type:MD5 md 1
Mac[16]:
9e cd b7 a4 64 c7 80 6b c9 d1 69 66 d0 2e d1 53 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 380, seq = 4643, nxtseq = 5023
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 380
decrypted app data fragment: ACK sip:[email protected]:5061;transport=TLS SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1967379695

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as3435967b

Call-ID: [email protected]

CSeq: 2 ACK

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #610 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 583
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 578, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #611 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 583
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 578, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #613 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 301
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 296, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 296
Ciphertext[296]:
4d 95 c3 9d ee 7d 71 1a 38 3f d9 4c b0 82 68 5d 
c7 b6 d9 68 c3 dc c0 c8 33 ec e5 85 22 90 09 d8 
68 cb f9 de cf a7 06 30 6d 7f 84 25 dc fb 25 97 
d3 a4 ec 6a a3 a2 47 07 6c b7 1f 7e 01 c3 5a 1c 
da e7 6d a0 09 5f 70 95 fc d5 a7 1c 23 1e 58 fd 
78 84 85 00 ab d7 98 49 9b 72 d5 4b ea bb 05 77 
e8 a1 64 03 3a 16 a4 95 6a 13 83 98 c6 65 a6 14 
e2 c8 33 d9 05 2b 6e 62 8f 39 7a 51 9b 86 83 b9 
d9 65 2c a0 b3 c2 8a 56 05 a1 6e 6e d0 f6 9f 11 
dc 7c 98 c6 c7 30 4e 8b 95 6f 88 4c 99 c4 98 89 
b8 d9 d3 59 81 e9 a1 ba 6f b3 37 20 9f 49 74 b6 
a6 7a 74 13 49 11 92 ba b2 97 38 4b d6 6d 60 d6 
8c 67 6a 15 a8 55 48 33 f7 2f 3f 22 d7 6f 95 54 
da 3f 24 3c c8 57 0e b0 ca f5 51 62 3e 59 2c 4e 
a3 62 a7 1d c5 07 38 ce fa f7 00 45 4f bf b2 a9 
fd b3 51 5d 74 8a ef 85 5f 60 c8 95 88 1b 11 e5 
9b 93 cf 68 47 18 f9 f1 db a1 05 22 84 1e c6 2b 
aa 9f ff 75 ce 80 ef 74 3b e5 3e dc 74 e4 a3 bb 
a3 15 e3 ba 9f 69 87 0d 
Plaintext[296]:
53 49 50 2f 32 2e 30 20 32 30 30 20 4f 4b 0d 0a 
56 69 61 3a 20 53 49 50 2f 32 2e 30 2f 54 4c 53 
20 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3b 
62 72 61 6e 63 68 3d 7a 39 68 47 34 62 4b 34 65 
38 31 30 63 38 33 3b 72 70 6f 72 74 0d 0a 46 72 
6f 6d 3a 20 3c 73 69 70 3a 31 32 40 31 30 2e 30 
2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 3d 
61 73 33 34 33 35 39 36 37 62 0d 0a 54 6f 3a 20 
3c 73 69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 
3d 36 30 37 34 39 31 33 32 39 0d 0a 43 61 6c 6c 
2d 49 44 3a 20 31 30 37 31 31 32 39 39 35 31 40 
31 30 2e 30 2e 30 2e 31 37 32 0d 0a 43 53 65 71 
3a 20 31 30 32 20 42 59 45 0d 0a 55 73 65 72 2d 
41 67 65 6e 74 3a 20 59 65 61 6c 69 6e 6b 20 53 
49 50 2d 54 32 38 50 20 32 2e 36 31 2e 30 2e 37 
30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65 6e 67 74 
68 3a 20 30 0d 0a 0d 0a 80 2f f9 7a 89 bd b3 21 
44 82 c5 17 55 fe 0d ac 
checking mac (len 280, version 301, ct 23 seq 9)
tls_check_mac mac type:MD5 md 1
Mac[16]:
80 2f f9 7a 89 bd b3 21 44 82 c5 17 55 fe 0d ac 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 280, seq = 5023, nxtseq = 5303
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 280
decrypted app data fragment: SIP/2.0 200 OK

Via: SIP/2.0/TLS 10.0.4.63:5061;branch=z9hG4bK4e810c83;rport

From: &lt;sip:[email protected]:5061&gt;;tag=as3435967b

To: &lt;sip:[email protected]:5061&gt;;tag=607491329

Call-ID: [email protected]

CSeq: 102 BYE

User-Agent: Yealink SIP-T28P 2.61.0.70

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #5 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 98
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 89 bytes, remaining 98

dissect_ssl enter frame #8 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #9 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #10 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2125
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2107 bytes, remaining 2116 
  record: offset = 2116, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 2121 length 0 bytes, remaining 2125

dissect_ssl enter frame #14 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
  record: offset = 139, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 145, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #15 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #16 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 156 offset 11 length 3052702 bytes, remaining 43

dissect_ssl enter frame #18 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 513
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 492
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK633221630

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #19 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #20 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #22 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 677
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 656
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1847283880

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #23 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #24 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #26 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 904
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 883
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #27 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #28 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #30 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 275
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 254
decrypted app data fragment: ACK sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as5818025c

Call-ID: [email protected]

CSeq: 1 ACK

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #33 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1070
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 1049
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1811458558

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;53a4a649&quot;, uri=&quot;sip:[email protected]:5061&quot;, response=&quot;458a128c100c2a1467e7a65c4f0bfc5b&quot;, algorithm=MD5

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #36 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #37 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100
association_find: TCP port 5061 found 0000000006322100
association_find: TCP port 5061 found 0000000006322100
ssl_association_remove removing TCP 5061 - sip handle 0000000005B16760
association_add TCP port 5061 protocol sip.tcp handle 0000000005B16790

dissect_ssl enter frame #5 (first time)
ssl_session_init: initializing ptr 0000000007071FB8 size 680
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 98
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 93, ssl state 0x00
association_find: TCP port 8003 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 89 bytes, remaining 98 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.0.4.63:5061
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #8 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #9 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x17
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #10 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 2125
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2111, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2107 bytes, remaining 2116 
  record: offset = 2116, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 2121 length 0 bytes, remaining 2125

dissect_ssl enter frame #14 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
pre master encrypted[128]:
5d e9 aa 35 6e e1 12 6c 06 ef 2b c3 03 44 0f 7a 
f4 ed 00 f3 9d 95 93 98 a4 94 3a 35 51 ab 38 ff 
9b a3 69 4e 46 51 c6 5f 53 ef 34 75 c5 fa 99 ef 
4d 4a 7e dc ab 4d b7 80 3e a0 55 cb e3 f2 c0 04 
ff da 57 d6 35 bb 3d 63 aa 4d e0 87 2b 29 58 50 
d4 c0 45 04 f3 2a 6d 06 da c3 e3 6a f9 cd 4b 9e 
03 a0 7b 0f 60 cf dc 9d 9f 29 c7 40 a7 20 f7 5c 
f6 c8 0c 0a 3c d0 7f a5 4f e0 19 2f 47 41 2d 7e 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 79 bytes, decr_len 127
decrypted_unstrip_pre_master[127]:
02 bc 5b 1e a2 bd 1c 4d 26 2c 12 31 af 1b ac 10 
07 e8 a1 f8 93 ea 18 95 8b 9e 64 7f a4 1b 08 52 
a8 34 53 c1 58 f7 be 06 6e eb d3 6d 32 61 e0 d8 
ba f7 62 b8 b0 1e 1a 4d ea 97 ff 05 f9 42 d5 f7 
d4 a6 4c 9f c1 ed e4 94 91 5c 1f 74 d2 5d 00 03 
01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 d2 
24 55 85 48 4b 89 46 23 19 9c 3a 2f e6 a9 79 8f 
47 50 51 1c d1 4d 0e d1 a6 e1 fe 69 7f 32 c8 
pre master secret[48]:
03 01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 
d2 24 55 85 48 4b 89 46 23 19 9c 3a 2f e6 a9 79 
8f 47 50 51 1c d1 4d 0e d1 a6 e1 fe 69 7f 32 c8 
ssl_generate_keyring_material:PRF(pre_master_secret)
pre master secret[48]:
03 01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 
d2 24 55 85 48 4b 89 46 23 19 9c 3a 2f e6 a9 79 
8f 47 50 51 1c d1 4d 0e d1 a6 e1 fe 69 7f 32 c8 
client random[32]:
4e ca e6 1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 
54 53 c5 9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 
server random[32]:
50 2a 58 c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 
1b db 6d bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
03 01 51 f4 b5 f8 c8 cf e7 8f db 96 d3 1a b5 b2 
d2 24 55 85 48 4b 89 46 
tls_hash: hash seed[77]:
6d 61 73 74 65 72 20 73 65 63 72 65 74 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 
hash out[48]:
df b8 de 0f a1 50 08 a3 0c 78 f5 10 67 e0 d4 ed 
6c 53 89 99 1b 76 f7 62 a6 55 c8 da b6 bf e7 5b 
09 6f 8e ff 90 8c 45 5e 72 96 d0 d4 9e fe a2 e0 
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
23 19 9c 3a 2f e6 a9 79 8f 47 50 51 1c d1 4d 0e 
d1 a6 e1 fe 69 7f 32 c8 
tls_hash: hash seed[77]:
6d 61 73 74 65 72 20 73 65 63 72 65 74 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 
hash out[48]:
8a 99 cc a8 29 36 9e 06 4c 95 0c f3 b2 a0 16 19 
96 5d 60 d2 f8 2d 46 bb 48 10 f8 4b 4f 93 63 4c 
d6 3b fd 72 a7 2a 1f 45 82 7c aa 40 4c ce 69 98 
PRF out[48]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 ee 45 30 91 f9 2c 84 17 
df 54 73 8d 37 a6 5a 1b f0 ea 7a 94 d2 30 cb 78 
master secret[48]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 ee 45 30 91 f9 2c 84 17 
df 54 73 8d 37 a6 5a 1b f0 ea 7a 94 d2 30 cb 78 
ssl_generate_keyring_material sess key generation
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 
tls_hash: hash seed[77]:
6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 
hash out[64]:
85 19 05 4d 00 32 38 02 fd a7 18 7b 63 b6 72 58 
4b 86 4c 98 28 c3 6b d6 f5 61 a1 92 46 b8 a8 65 
34 44 10 96 e2 c5 6c b5 a2 f4 61 5e 68 f0 e6 5e 
e1 6f f4 18 4a 08 9a 48 34 11 78 21 f4 6f eb 62 
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
ee 45 30 91 f9 2c 84 17 df 54 73 8d 37 a6 5a 1b 
f0 ea 7a 94 d2 30 cb 78 
tls_hash: hash seed[77]:
6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 50 2a 58 
c7 b7 e2 66 00 8c b1 66 68 e3 c6 5f b6 1b db 6d 
bc 83 4b 4e 6f ca 39 d2 cc b0 24 81 c4 4e ca e6 
1c 90 58 cf 50 c9 45 fb b7 f9 fc 34 36 54 53 c5 
9c 54 36 c8 c4 a4 bd 61 05 fe 5e f5 77 
hash out[64]:
a1 3e f6 ca 12 2e 1d 17 fe d0 8e 89 3a 75 17 24 
6a 9b 50 8c 4d 54 d4 26 0c 58 32 a2 27 65 15 b1 
17 a4 de cc f8 ac fb a0 e6 c1 0a ce 37 33 8a e1 
ec 01 18 90 05 d1 4e 4e 15 76 9e a8 8b b3 0b 56 
PRF out[64]:
24 27 f3 87 12 1c 25 15 03 77 96 f2 59 c3 65 7c 
21 1d 1c 14 65 97 bf f0 f9 39 93 30 61 dd bd d4 
23 e0 ce 5a 1a 69 97 15 44 35 6b 90 5f c3 6c bf 
0d 6e ec 88 4f d9 d4 06 21 67 e6 89 7f dc e0 34 
key expansion[64]:
24 27 f3 87 12 1c 25 15 03 77 96 f2 59 c3 65 7c 
21 1d 1c 14 65 97 bf f0 f9 39 93 30 61 dd bd d4 
23 e0 ce 5a 1a 69 97 15 44 35 6b 90 5f c3 6c bf 
0d 6e ec 88 4f d9 d4 06 21 67 e6 89 7f dc e0 34 
Client MAC key[16]:
24 27 f3 87 12 1c 25 15 03 77 96 f2 59 c3 65 7c 
Server MAC key[16]:
21 1d 1c 14 65 97 bf f0 f9 39 93 30 61 dd bd d4 
Client Write key[16]:
23 e0 ce 5a 1a 69 97 15 44 35 6b 90 5f c3 6c bf 
Server Write key[16]:
0d 6e ec 88 4f d9 d4 06 21 67 e6 89 7f dc e0 34 
Client Write IV[8]:
00 00 00 00 00 00 00 00 
Server Write IV[8]:
f0 c4 27 00 00 00 00 00 
ssl_generate_keyring_material ssl_create_decoder(client)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material ssl_create_decoder(server)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material: client seq 0, server seq 0
ssl_save_session stored session id[32]:
af dd 5f fb 98 29 74 f7 1c 0d 91 37 94 cd 95 8b 
ed 2e f0 b4 ea e0 5a 79 94 31 00 0e a0 e8 b0 89 
ssl_save_session stored master secret[48]:
55 21 12 a7 88 66 96 a5 40 ed f9 e3 d5 40 c2 f4 
fa 0e e9 4b e3 5b b1 d9 ee 45 30 91 f9 2c 84 17 
df 54 73 8d 37 a6 5a 1b f0 ea 7a 94 d2 30 cb 78 
dissect_ssl3_handshake session keys successfully generated
  record: offset = 139, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
f3 cc a1 1f 1c 04 c3 04 43 19 84 42 33 8e 0d d4 
77 46 27 74 1a 9c 53 7d 86 cb 79 f9 c5 7d 61 2d 
Plaintext[32]:
14 00 00 0c 07 14 6d 39 0a ad 54 2f af 9e f9 f8 
9a c9 2a 7c 36 69 7d cd 29 bf c8 c0 b0 e5 43 23 
checking mac (len 16, version 301, ct 22 seq 0)
tls_check_mac mac type:MD5 md 1
Mac[16]:
9a c9 2a 7c 36 69 7d cd 29 bf c8 c0 b0 e5 43 23 
ssl_decrypt_record: mac ok
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #15 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
9c 2e 94 9e 40 17 8f 0c 32 d6 28 49 ee 0b b9 86 
f7 f0 a3 d8 30 50 f2 50 3b 55 f0 1d d4 0d 25 8d 
Plaintext[32]:
14 00 00 0c 70 f7 4f f8 13 a2 cc 62 1e 14 d6 ad 
84 9b 01 62 07 02 e7 a0 59 4f fe e2 7a 1a d3 8c 
checking mac (len 16, version 301, ct 22 seq 0)
tls_check_mac mac type:MD5 md 1
Mac[16]:
84 9b 01 62 07 02 e7 a0 59 4f fe e2 7a 1a d3 8c 
ssl_decrypt_record: mac ok
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #16 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 156 offset 11 length 3052702 bytes, remaining 43

dissect_ssl enter frame #18 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 513
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 508, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 508
Ciphertext[508]:
f0 22 9a 0b ec 67 48 1e e9 45 85 8f 17 0c 40 6e 
d1 a6 58 9b 02 98 22 ba 76 d1 a7 b1 80 48 96 a5 
0c 77 78 2c 62 74 20 40 80 ec 3a 6f d9 d5 02 20 
35 8b eb 26 42 8a 6b 17 2d ae 55 59 61 83 48 6f 
f4 6d 45 9f d2 ab 1b e9 ca 90 86 3c d7 8c 04 45 
1a 5b db d0 ec 3d a9 99 37 d9 d0 f0 6a 0e 3b e0 
dc 2d a8 9f 43 31 a5 5f 16 90 68 17 82 c3 56 b4 
fb cf 83 88 55 4e b0 15 ce c8 8b 26 97 b9 bc 3c 
6a 1b e3 9d 3c 84 3d 39 ac 61 72 19 1e 69 1e 01 
44 81 a1 b0 78 a5 4b b0 cb af 98 e6 da f9 4c f5 
07 58 73 10 1e ca ff 9c 52 b9 04 91 0c d9 84 f5 
94 e6 76 fd b3 19 19 ca b8 cd 79 92 8c 4d 60 6a 
da 03 66 d4 7f 80 73 45 45 f7 c1 52 4b 27 9e 8b 
51 f4 0d 9c a3 e0 b2 49 81 0d 4e b0 16 d3 5f 2e 
e5 e9 7f 3a 2e a7 5f 5b 9b 52 08 96 9d 45 f0 73 
70 4c 27 04 cd cc 61 9d 1d a0 e9 c3 59 09 d6 02 
b0 7b f7 64 6c 98 77 f0 ec 2d 7b 1a b6 15 d2 b9 
d3 47 ca 49 6a b7 11 f2 c9 14 93 ee 25 21 5d 06 
37 fb b0 b0 72 36 2a 50 bb d3 42 9b 5c 60 91 20 
16 92 3c 80 df 2e 53 a8 d4 ea 67 ac f2 f2 18 fe 
90 0a fa f6 82 66 3d a3 68 0d 1f 8c 6c f9 1b c0 
78 7f 1b db 9d 1b 9b 0f 67 a2 a8 ba 03 ac fe b7 
3d 75 a4 46 fd d2 96 d0 2f c4 3a 5a 0e 13 a3 2a 
30 a8 91 f9 b5 74 cf b4 62 5f f4 5f 19 46 d6 5a 
17 fd 7b d6 83 08 69 d1 92 49 fd 83 f1 14 60 b6 
cd e1 aa 4c 20 83 04 39 4a 23 db d0 ca 3b b6 8b 
94 4d 9f 48 7c 60 18 f2 31 07 f1 9a cf 08 76 d0 
73 ac 9c d6 f3 ac 26 67 62 6c 7d 12 6b 09 28 28 
99 28 c0 5b 4d 13 a8 ad be fb 43 24 70 4f 1c 48 
c5 91 b3 35 3b 74 fb 6b 98 fb df 0f ef 91 af 24 
e9 22 a2 7a 1b 16 88 ac 9d 9a 85 f8 f3 23 d2 c7 
18 f4 bd 31 e9 7f 02 6a d7 1a 18 9b 
ssl_decrypt_record: allocating 540 bytes for decrypt data (old len 32)
Plaintext[508]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 36 33 33 32 32 31 36 33 30 0d 0a 46 
72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 
31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
3e 3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 36 
0d 0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 30 
30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 
31 3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 30 
35 33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 37 
32 0d 0a 43 53 65 71 3a 20 31 20 52 45 47 49 53 
54 45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 73 
69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 2e 
30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 73 
70 6f 72 74 3d 54 4c 53 3e 0d 0a 41 6c 6c 6f 77 
3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 4f 2c 20 
50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 59 45 2c 
20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 4f 4e 53 
2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 49 53 54 
45 52 2c 20 53 55 42 53 43 52 49 42 45 2c 20 52 
45 46 45 52 2c 20 50 55 42 4c 49 53 48 2c 20 55 
50 44 41 54 45 2c 20 4d 45 53 53 41 47 45 0d 0a 
4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 20 37 30 
0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 59 65 
61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 50 20 32 
2e 36 31 2e 30 2e 37 30 0d 0a 45 78 70 69 72 65 
73 3a 20 36 30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 
65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 8c 2f bf 4e 
df 16 d6 8f 3e b0 cb 65 72 52 e5 28 
checking mac (len 492, version 301, ct 23 seq 1)
tls_check_mac mac type:MD5 md 1
Mac[16]:
8c 2f bf 4e df 16 d6 8f 3e b0 cb 65 72 52 e5 28 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 492, seq = 0, nxtseq = 492
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 492
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK633221630

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #19 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 518, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #20 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 518, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #22 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 677
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 672, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 672
Ciphertext[672]:
6e 67 b7 b4 af ed f2 e2 8e b7 f3 d2 f0 d6 2c 72 
7f c8 06 23 e4 44 98 d0 5c d4 61 9d 8f 80 a5 9b 
ec d8 b0 65 f6 f6 67 8e 1b e0 87 d5 f7 ea eb 78 
dd 3a d8 e1 e5 2d b3 df ed df 09 af 99 ab 5a be 
c7 d0 e9 6e 63 d5 cd 91 ef 30 9e 9d ce 2c d5 56 
19 e2 98 a1 6e 15 0b ce 5f 40 ab dc 1b 48 8d 18 
94 f6 6c 60 ea 1d fa 27 8b 89 e4 7f ed c2 3b 8c 
c3 3a 18 e5 88 7a ee 75 cf 7e cb 64 b4 73 a0 d5 
11 a3 6a 4c 37 56 d3 04 a2 46 33 1e d0 b2 32 e3 
e6 bc 47 be c1 39 bb ff d2 a0 d5 5c 02 f0 dd 97 
c2 bc b6 ff 75 df 15 1d 8d 3b aa ab 43 e3 2e 20 
44 4a 65 99 53 33 75 ce 6f 00 8c 8a 79 01 26 3f 
59 f3 56 ce c7 a1 39 d5 8c 64 f0 c9 5f f3 55 29 
ad be 1a 32 76 e5 da d8 d3 db 03 b5 17 de 9c e4 
80 dc 17 8c 68 89 73 28 13 b0 92 48 4b e1 7d 91 
23 24 c8 be 3e 4c c6 93 59 ff 8a 57 b4 54 66 3e 
a6 bd 93 c4 7d d8 60 1c 59 bb 24 f6 25 da 46 39 
51 2f b7 cb 59 fe 85 76 6c 9a 14 b5 b4 ce 38 2e 
f1 33 99 e1 d0 5a eb 2d 7f cd a4 44 c4 20 de 7b 
c5 19 96 3f 35 94 22 9e 1c e3 b2 fc 36 86 08 95 
a9 cf 07 d0 75 9a 7b f0 ee a8 f7 8f 47 a1 17 e3 
50 46 21 04 56 a8 cb 04 e3 c5 a9 d2 f6 8c 0c e8 
db 08 b8 d0 2d 4f fd ed 61 4a 5e 92 b1 ab 8d fc 
4e 86 c5 94 95 36 13 59 e8 f6 5a c2 bd c2 20 c6 
f5 74 e6 34 26 b1 fc 69 da 48 72 f2 23 4c 71 fc 
c0 af 12 f9 4a e6 dd c6 e8 a8 7f 67 90 52 c1 1e 
a2 bb 78 00 a8 44 36 4a c5 8b d7 97 50 ea f1 10 
30 ac 88 99 4c a6 6d 0a 34 59 99 c8 cf 3e ff a0 
e2 3f ea be 0a f9 05 fc c6 24 91 89 1a b1 a9 23 
8e af 84 0c de 92 67 41 2c c6 86 05 bf 52 46 69 
45 7e 63 61 0a 8c 3b c6 ed a2 40 b3 74 2e 34 ce 
4f d0 41 84 49 29 2b 3a 63 1a 7e 38 40 04 f8 62 
1a ea c5 08 e6 8a 2e 0b 0c 9a 10 f2 1a ff d6 52 
5a 10 22 b8 40 18 cd 66 93 3e 42 f4 d6 43 d1 6a 
9a 86 7f 93 f8 f1 f2 90 3f cc 92 a1 a5 ff 58 7d 
1f 43 90 de 7f 32 bb 2d 3a bf 77 71 32 e3 63 46 
ef 9e a6 99 d2 de 00 74 b8 f3 32 3e 57 af 1d b0 
41 aa 70 fc b0 df e9 54 fc c9 a4 95 73 40 4f d9 
2d ef c8 8b a9 f3 a0 d0 68 13 d6 f0 1d 26 bb 0a 
3e e5 ed 82 40 b1 a4 95 db 2d 47 9e 5c 36 de 71 
ef 2f 56 9a 95 a6 65 aa 6b ab c7 3e b1 35 5d fe 
77 e0 6c 68 c7 87 64 82 4b a7 24 17 5a af 64 2d 
ssl_decrypt_record: allocating 704 bytes for decrypt data (old len 540)
Plaintext[672]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 31 38 34 37 32 38 33 38 38 30 0d 0a 
46 72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 
30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 
31 3e 3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 
36 0d 0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 
30 30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 
36 31 3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 
30 35 33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 
37 32 0d 0a 43 53 65 71 3a 20 32 20 52 45 47 49 
53 54 45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 
73 69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 
2e 30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 
73 70 6f 72 74 3d 54 4c 53 3e 0d 0a 41 75 74 68 
6f 72 69 7a 61 74 69 6f 6e 3a 20 44 69 67 65 73 
74 20 75 73 65 72 6e 61 6d 65 3d 22 74 65 73 74 
30 30 31 22 2c 20 72 65 61 6c 6d 3d 22 43 61 6c 
6c 2d 65 58 22 2c 20 6e 6f 6e 63 65 3d 22 31 33 
35 36 61 37 37 62 22 2c 20 75 72 69 3d 22 73 69 
70 3a 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
22 2c 20 72 65 73 70 6f 6e 73 65 3d 22 37 31 31 
38 65 39 32 32 38 62 65 62 32 37 31 33 34 35 61 
30 66 65 32 62 63 38 61 64 32 33 33 32 22 2c 20 
61 6c 67 6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 41 
6c 6c 6f 77 3a 20 49 4e 56 49 54 45 2c 20 49 4e 
46 4f 2c 20 50 52 41 43 4b 2c 20 41 43 4b 2c 20 
42 59 45 2c 20 43 41 4e 43 45 4c 2c 20 4f 50 54 
49 4f 4e 53 2c 20 4e 4f 54 49 46 59 2c 20 52 45 
47 49 53 54 45 52 2c 20 53 55 42 53 43 52 49 42 
45 2c 20 52 45 46 45 52 2c 20 50 55 42 4c 49 53 
48 2c 20 55 50 44 41 54 45 2c 20 4d 45 53 53 41 
47 45 0d 0a 4d 61 78 2d 46 6f 72 77 61 72 64 73 
3a 20 37 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 
3a 20 59 65 61 6c 69 6e 6b 20 53 49 50 2d 54 32 
38 50 20 32 2e 36 31 2e 30 2e 37 30 0d 0a 45 78 
70 69 72 65 73 3a 20 36 30 0d 0a 43 6f 6e 74 65 
6e 74 2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 
0a 53 eb b7 50 8b 49 11 01 51 1b f2 75 b5 2a 2f 
checking mac (len 656, version 301, ct 23 seq 2)
tls_check_mac mac type:MD5 md 1
Mac[16]:
0a 53 eb b7 50 8b 49 11 01 51 1b f2 75 b5 2a 2f 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 656, seq = 492, nxtseq = 1148
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 656
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1847283880

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #23 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 549, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #24 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 549, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #26 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 904
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 899, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 899
Ciphertext[899]:
2a c5 1c f1 2e d6 04 fc e9 c3 2b b0 a1 ee 76 bf 
48 d3 84 a0 8f 32 e4 bb 5e 66 93 20 eb c8 78 3a 
68 95 45 77 20 66 5c b0 c3 2c 33 fb a9 a1 18 18 
60 8d cd ee 47 8d 5d 4e 98 c7 9f 56 cb f9 63 06 
fb 99 b2 28 60 bc ee 7f 58 ee bd 0a f9 7b 0c ef 
06 77 b3 94 f1 dd 68 2d 96 9f 37 b3 d5 6d 13 5e 
3b 47 8e ab 40 e5 da 71 27 d1 05 90 70 fb e4 4a 
04 0b 35 4c 40 f2 32 89 9b ef 98 2c d3 5b 52 5d 
5d 7f 2b b2 8c 45 cb 5c 29 28 e7 21 0e 76 13 18 
90 18 ba 0e af 21 52 eb 3c f0 c2 1f ec 90 4e 9d 
8f c6 e9 58 05 3a 17 30 0d d4 a3 32 74 15 78 f2 
18 19 dc 96 8b 51 97 8f b0 ab c9 4d 31 1f 7e 82 
9a d5 a8 ac 49 e6 2e 97 e6 14 43 ec 6b 58 ba ab 
82 ff 7a 65 f6 3a 1d 33 bd ee be cb dc 04 46 97 
92 2a 33 c7 40 78 db a8 6e 14 ba b5 20 dd 84 c8 
61 cc 59 7d 47 f8 6e 35 50 c5 8a ff fa cd 0e 24 
e4 6e ca f8 b5 fb 05 7f 01 22 c1 7d 8c 11 4b b2 
b5 06 60 03 05 78 7a 3b 29 be 94 dc b8 c9 58 fd 
28 cb 31 0e 73 63 d7 85 da a2 59 e5 a0 6c 04 fc 
a9 77 ee 41 11 f3 df ad ae c0 3c 06 54 3c 0d 91 
94 a3 12 06 53 81 a4 c0 82 c8 6d f4 4f eb 5d 6a 
e3 cf fd 7b 27 1c 8b bc ea 5a 74 ae b8 17 21 5d 
a7 10 5c 25 cc 74 fb ad 44 bb 3c e5 0e 79 fd f9 
4e 38 0f 38 b1 79 be 33 4d fe 91 ab 2b e2 0a f1 
d0 ac 02 84 f7 9d 51 40 09 b6 51 17 f0 82 1c 74 
75 02 27 f8 84 b0 7e 11 2d 50 02 10 a3 ce 03 73 
63 c4 6d 12 2a d9 c5 a4 6f 4c 08 f4 63 f9 04 82 
26 af 11 e4 14 dc 47 e4 be 99 9c eb 56 59 97 c5 
70 d2 cd 0b 62 9d 15 5b 71 52 67 2f 76 2f b3 52 
1e 40 80 5a 7f 00 f5 b5 c9 7a 9f 31 f3 ca 58 62 
ca 31 34 93 5d 82 e7 2b 7e 9f 21 57 56 5c bc 2f 
0a 09 a8 5b bf 5a c3 c8 f4 ad eb d5 87 fa c3 3e 
36 82 65 43 30 99 51 43 60 44 62 7d 21 5c 0c 0a 
8b 62 84 20 7c 01 af 3d 57 55 8d d0 d9 09 e5 78 
03 2f 1d 73 c3 df 44 69 b9 29 72 a2 e0 44 d5 a9 
44 30 3d d8 2b 64 30 c8 07 f3 11 63 50 49 b8 76 
5a 97 19 42 a4 fe d7 e1 f4 09 67 20 cb 87 67 03 
f3 f6 61 24 40 34 46 78 17 7a a8 53 97 35 9b ef 
35 93 cd 89 f1 7b 94 c4 68 01 87 d4 f8 81 95 af 
c0 0d 42 d2 c6 8e e7 23 e7 96 99 29 dc 86 27 1e 
c6 3e 37 e1 f7 02 39 d3 22 a8 08 30 11 03 c0 91 
1e 12 4d ff 1f eb 8b ad 46 11 ac e0 f6 08 b4 e1 
cb f9 e4 71 1e b9 7b 1e 8e 57 7e 64 af 8a dc e4 
69 58 c8 70 43 46 ae bc 6f d1 6e 83 39 61 a1 7b 
47 f2 7c 76 0e 23 06 b9 3c 6c 37 fa 55 fe cc ae 
cc 89 f3 48 be 61 18 53 0a 5c 01 86 9b 1e f1 f4 
60 fb 66 84 75 df 2e 37 9a 13 af 8f 26 87 91 38 
79 36 18 8a f4 2d 0d 0a 9e 1f 6f 96 6f 14 ca f0 
64 3e 02 0b b5 73 41 3d 50 38 60 ba 0d df a6 fe 
a1 88 ca 99 a6 22 6a 34 64 0d 43 c4 b9 7b c3 f8 
5f 31 a3 35 2b 95 81 ce f5 b3 a4 af 43 9c c8 48 
6a 88 ec dd 4c 98 01 89 43 53 34 69 b3 33 ad 1f 
d4 02 7a 95 ed c5 84 77 a0 67 f1 61 4d 32 d9 13 
e5 52 aa e2 b4 74 6b 62 44 3c 89 4b 59 8b f7 28 
0b 67 d8 ea d9 0a 30 67 c7 02 69 64 18 80 4a 54 
06 e3 49 b4 3b 15 24 92 fd 51 f0 67 14 5c 2b ac 
c8 ba 3a 
ssl_decrypt_record: allocating 931 bytes for decrypt data (old len 704)
Plaintext[899]:
49 4e 56 49 54 45 20 73 69 70 3a 31 32 40 31 30 
2e 30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 
2f 32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 
2e 30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 
32 3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 
68 47 34 62 4b 31 39 39 35 33 39 37 39 38 30 0d 
0a 46 72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 
30 30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 
36 31 3e 3b 74 61 67 3d 36 30 37 34 39 31 33 32 
39 0d 0a 54 6f 3a 20 3c 73 69 70 3a 31 32 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 0d 0a 
43 61 6c 6c 2d 49 44 3a 20 31 30 37 31 31 32 39 
39 35 31 40 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 
43 53 65 71 3a 20 31 20 49 4e 56 49 54 45 0d 0a 
43 6f 6e 74 61 63 74 3a 20 3c 73 69 70 3a 74 65 
73 74 30 30 31 40 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 74 72 61 6e 73 70 6f 72 74 3d 
54 4c 53 3e 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 
70 65 3a 20 61 70 70 6c 69 63 61 74 69 6f 6e 2f 
73 64 70 0d 0a 41 6c 6c 6f 77 3a 20 49 4e 56 49 
54 45 2c 20 49 4e 46 4f 2c 20 50 52 41 43 4b 2c 
20 41 43 4b 2c 20 42 59 45 2c 20 43 41 4e 43 45 
4c 2c 20 4f 50 54 49 4f 4e 53 2c 20 4e 4f 54 49 
46 59 2c 20 52 45 47 49 53 54 45 52 2c 20 53 55 
42 53 43 52 49 42 45 2c 20 52 45 46 45 52 2c 20 
50 55 42 4c 49 53 48 2c 20 55 50 44 41 54 45 2c 
20 4d 45 53 53 41 47 45 0d 0a 4d 61 78 2d 46 6f 
72 77 61 72 64 73 3a 20 37 30 0d 0a 55 73 65 72 
2d 41 67 65 6e 74 3a 20 59 65 61 6c 69 6e 6b 20 
53 49 50 2d 54 32 38 50 20 32 2e 36 31 2e 30 2e 
37 30 0d 0a 53 75 70 70 6f 72 74 65 64 3a 20 72 
65 70 6c 61 63 65 73 0d 0a 41 6c 6c 6f 77 2d 45 
76 65 6e 74 73 3a 20 74 61 6c 6b 2c 68 6f 6c 64 
2c 63 6f 6e 66 65 72 65 6e 63 65 2c 72 65 66 65 
72 2c 63 68 65 63 6b 2d 73 79 6e 63 0d 0a 43 6f 
6e 74 65 6e 74 2d 4c 65 6e 67 74 68 3a 20 33 30 
32 0d 0a 0d 0a 76 3d 30 0d 0a 6f 3d 2d 20 32 30 
30 30 30 20 32 30 30 30 30 20 49 4e 20 49 50 34 
20 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 73 3d 53 
44 50 20 64 61 74 61 0d 0a 63 3d 49 4e 20 49 50 
34 20 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 74 3d 
30 20 30 0d 0a 6d 3d 61 75 64 69 6f 20 31 31 37 
38 30 20 52 54 50 2f 41 56 50 20 30 20 38 20 31 
38 20 39 20 31 30 31 0d 0a 61 3d 72 74 70 6d 61 
70 3a 30 20 50 43 4d 55 2f 38 30 30 30 0d 0a 61 
3d 72 74 70 6d 61 70 3a 38 20 50 43 4d 41 2f 38 
30 30 30 0d 0a 61 3d 72 74 70 6d 61 70 3a 31 38 
20 47 37 32 39 2f 38 30 30 30 0d 0a 61 3d 66 6d 
74 70 3a 31 38 20 61 6e 6e 65 78 62 3d 6e 6f 0d 
0a 61 3d 72 74 70 6d 61 70 3a 39 20 47 37 32 32 
2f 38 30 30 30 0d 0a 61 3d 66 6d 74 70 3a 31 30 
31 20 30 2d 31 35 0d 0a 61 3d 72 74 70 6d 61 70 
3a 31 30 31 20 74 65 6c 65 70 68 6f 6e 65 2d 65 
76 65 6e 74 2f 38 30 30 30 0d 0a 61 3d 70 74 69 
6d 65 3a 32 30 0d 0a 61 3d 73 65 6e 64 72 65 63 
76 0d 0a 10 69 30 60 1b 65 e5 22 93 1f ce 8f 46 
28 01 a0 
checking mac (len 883, version 301, ct 23 seq 3)
tls_check_mac mac type:MD5 md 1
Mac[16]:
10 69 30 60 1b 65 e5 22 93 1f ce 8f 46 28 01 a0 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 883, seq = 1148, nxtseq = 2031
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 883
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #27 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 512, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #28 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 512, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #30 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 275
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 270, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 270
Ciphertext[270]:
13 9f d1 a9 be bb c9 d3 40 1b ab 82 25 09 19 5c 
a4 18 2f c4 26 f3 44 5c b2 32 50 9c 52 67 9d c9 
a5 19 41 4e dd b5 05 ec 55 da ba 7f 84 b6 17 a7 
87 03 12 5e f8 13 a4 c4 fa 61 f4 91 14 f7 74 e8 
22 00 7f 5c 93 d5 a7 a7 15 fc 0b 00 6e 68 1d 59 
f7 e0 a2 26 78 05 15 d9 5e 26 62 67 1d b2 73 82 
88 4d 4f c6 59 a3 32 c0 6a 80 31 b9 af 92 1d da 
29 b4 4e ad f8 bc 8a 31 f6 3a 12 05 6f 2d a3 4e 
a2 38 f1 83 9d 8c f8 01 a0 40 cd e2 53 af 8f 44 
57 e3 9e 24 bb 72 68 ac 6d 95 41 18 c4 a7 70 d0 
32 98 af 49 97 42 08 d2 ea d7 95 81 1a 6f c1 76 
f3 47 a4 77 11 b6 99 9c aa 90 2d f6 03 99 8c 4b 
29 a7 df c6 1e fb e6 85 09 7d 0f 42 55 2a 0e 16 
bd fd b6 fa eb 06 77 bc e9 5c ed 2b ca 50 9b 10 
dc 83 02 b7 30 a8 96 d9 08 f8 45 83 09 5d 75 a4 
ce 42 6e 8b 5f 99 60 40 5e 78 94 df 09 6f e5 08 
e7 30 92 f0 dc 92 dc 48 c8 8d ba 1e b4 53 
Plaintext[270]:
41 43 4b 20 73 69 70 3a 31 32 40 31 30 2e 30 2e 
34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 32 2e 
30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 30 2f 
54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 3a 35 
30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 47 34 
62 4b 31 39 39 35 33 39 37 39 38 30 0d 0a 46 72 
6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 31 
40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 
3b 74 61 67 3d 36 30 37 34 39 31 33 32 39 0d 0a 
54 6f 3a 20 3c 73 69 70 3a 31 32 40 31 30 2e 30 
2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 3d 
61 73 35 38 31 38 30 32 35 63 0d 0a 43 61 6c 6c 
2d 49 44 3a 20 31 30 37 31 31 32 39 39 35 31 40 
31 30 2e 30 2e 30 2e 31 37 32 0d 0a 43 53 65 71 
3a 20 31 20 41 43 4b 0d 0a 43 6f 6e 74 65 6e 74 
2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a e9 24 
cb 24 90 ab ce 06 e4 77 f9 01 3e 49 59 02 
checking mac (len 254, version 301, ct 23 seq 4)
tls_check_mac mac type:MD5 md 1
Mac[16]:
e9 24 cb 24 90 ab ce 06 e4 77 f9 01 3e 49 59 02 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 254, seq = 2031, nxtseq = 2285
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 254
decrypted app data fragment: ACK sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as5818025c

Call-ID: [email protected]

CSeq: 1 ACK

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #33 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 1070
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1065, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 1065
Ciphertext[1065]:
af ec ba 53 3b a6 5c 51 6d b5 35 6b 35 14 cc a2 
c9 04 ab 47 2c 34 73 d5 eb 71 d6 56 bb 40 df ca 
72 26 fa 13 ce cd 33 e7 b2 a0 81 ad bc df 88 43 
82 06 5a 05 d7 1d 01 cc 5c bc de 42 43 2c 66 53 
fd b1 69 36 db d4 f6 c8 6d fe 28 fb d6 a2 6e 4a 
92 c1 f7 28 f0 4a 73 5a 26 85 51 af 1c 94 0a 1f 
1c b1 e5 98 c0 d8 f7 79 0c 4e 05 5b 39 a9 08 b4 
ed 22 94 47 70 d7 ea 8c 22 c9 92 26 f5 af b6 1f 
db 1a 6f 90 28 1a db 97 43 fb de f5 df 66 02 5d 
d0 ae 99 e2 32 8c 60 57 b9 41 f3 56 f8 db cc 17 
cb 48 3d cc 18 40 c8 11 57 8d 71 ca 21 08 ef eb 
da 7b ea 32 a2 8b c3 bd be 2b 79 f2 55 4a 34 e9 
ee 8a ca 95 32 32 96 d6 c9 4d 5d 88 cb 59 f7 95 
68 5c fa 0c f1 1d fb 95 46 8c 7e b3 43 9e 25 27 
c0 7b 4e 6b 82 96 07 7c 76 b5 a2 49 41 66 f6 e0 
04 ca 88 6b 36 78 15 89 cb 00 14 a3 ec e1 b6 80 
89 9a dd 65 37 9f e0 41 b9 6c 00 e5 76 65 d1 ae 
78 9b dd 36 93 7a c5 6f ad 96 f9 fa 54 98 3d 4a 
a0 57 b7 d1 93 28 b6 b1 50 ea 67 87 56 70 f0 9f 
36 c2 44 fe 94 e8 b4 69 a9 70 f0 14 6f 03 8a 9a 
37 29 24 17 04 a6 83 bf ee 37 89 ca 64 f3 b6 ea 
8d aa 4e 28 ba d4 7b 98 0f 95 1b d8 3c ae aa 7c 
b4 20 b4 b8 96 c1 a8 84 c7 85 2b 48 6b e2 3a fa 
d6 3b e0 7d ef f7 e9 79 ca 7c 31 c6 09 5a db 80 
01 8c da 6c 10 cd 40 e6 8c 18 fe d1 42 8a 91 7c 
c7 8c 70 68 5b f9 2f e9 81 5a 75 78 c8 14 0a ed 
be a4 16 da 68 8b 52 1b 37 83 d1 ba 28 f5 82 f7 
ee 01 d5 41 2e a6 15 ae 67 cf 17 ca ec 78 73 c9 
3f 7e 3c 25 bc 60 1a 28 0e e1 9c 3d 53 05 aa b3 
7e 17 c1 f9 c5 f9 62 cf bc bd 9a e8 81 21 10 e2 
2e 22 80 67 da bb 71 10 05 c0 a4 cc 3b 52 86 6b 
85 40 d7 44 9f 1c eb a2 aa 03 b6 98 44 6b 42 29 
fe 85 9c 77 22 06 ff 81 1d 5a b8 ac 0f 9a 65 39 
1f 01 02 54 0f f1 eb 83 a1 d6 47 d8 77 59 a6 ff 
38 ec 4b 55 87 58 0f ac d9 af 33 cf 0a a0 d7 07 
68 2d 69 e1 84 96 41 ed 38 34 a9 4d 20 32 d3 cd 
39 09 7d bd 67 87 c4 4a d7 d9 79 0f f2 22 ba 06 
dd e3 00 fa f7 9c cd 3a 31 36 5d c0 e2 e4 ce d2 
5d 10 f3 08 a9 8b 11 78 ee a7 92 85 27 e3 c8 db 
00 f3 b6 a7 9c 07 d4 cd b0 ef 31 19 bc 50 32 18 
fe d6 9b 4e 9d e3 c0 90 15 ba 30 05 8c 93 8f 38 
01 96 a8 ca aa 3d d0 5b c0 91 69 24 c8 9c 58 8c 
47 b5 f6 4a af d2 f4 bd b1 b1 1f 59 52 7b e0 bd 
e4 a0 75 a6 15 6f 3c 8a b3 2b 8f 52 38 f1 be 0c 
35 3d 92 29 93 4d 69 be 7b e8 dc c8 1e b4 e4 b8 
23 dd 2c a3 85 99 16 d1 4c be 88 fe 4c 95 db 92 
00 ae 57 7a f6 49 b2 cb 5f f4 0d ca 35 10 d5 71 
dc ca 24 98 7a 01 8f 6f 19 54 54 34 e1 b2 14 d7 
6a 7b 90 cd 1d b2 9a fd 48 bd 36 93 53 56 9b 2a 
38 ea 37 52 ab 82 87 17 15 4a 52 eb 69 80 ae 7c 
30 68 c8 20 c7 76 43 a6 e1 c9 bb 6e 38 11 23 63 
fb 6b 22 24 3f 63 97 31 d2 fe a4 07 4d 68 d8 96 
d7 38 60 f4 65 b0 c6 5c 91 23 22 04 39 d8 f7 dc 
3f a0 28 65 ce d8 f7 41 90 02 2d 99 5c 6f 29 71 
cd fb a9 d5 73 13 c8 32 6f 8f dc 74 ec e3 ff 1c 
8f 70 f5 3a 86 4d 9f bd 6e 05 9e da 52 0b b0 7d 
bc 96 5f 29 2c 7f 04 ad 61 2e 17 59 5f ff 7f fc 
3f 42 94 49 f7 d5 71 84 10 46 43 ed 8a e9 3c e9 
d7 a9 61 67 97 e5 0a 3e b6 02 44 3f 7f 1b 91 5a 
af 1a e1 3f 16 08 51 7c e2 70 48 67 6d f5 4d d5 
2d 60 07 2c bd 75 ff 06 e3 f0 df bd 22 0d 48 14 
fb d5 a3 c3 d2 9b 05 f8 db 2a f7 51 48 ad 2c d3 
a9 aa 2a 06 16 3c d6 0a 76 02 93 f0 57 05 6f eb 
4c ce 3e dc 11 50 c3 ea f1 e2 e4 35 94 29 97 22 
06 e8 aa 82 27 43 de e2 4c 9a 41 8e e5 23 cd 31 
e6 cf b9 a1 dc 30 92 d9 95 4a b6 e8 05 fd 0a 4a 
c2 43 62 c6 b6 bf 2c f1 df 
ssl_decrypt_record: allocating 1097 bytes for decrypt data (old len 931)
Plaintext[1065]:
49 4e 56 49 54 45 20 73 69 70 3a 31 32 40 31 30 
2e 30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 
2f 32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 
2e 30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 
32 3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 
68 47 34 62 4b 31 38 31 31 34 35 38 35 35 38 0d 
0a 46 72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 
30 30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 
36 31 3e 3b 74 61 67 3d 36 30 37 34 39 31 33 32 
39 0d 0a 54 6f 3a 20 3c 73 69 70 3a 31 32 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 0d 0a 
43 61 6c 6c 2d 49 44 3a 20 31 30 37 31 31 32 39 
39 35 31 40 31 30 2e 30 2e 30 2e 31 37 32 0d 0a 
43 53 65 71 3a 20 32 20 49 4e 56 49 54 45 0d 0a 
43 6f 6e 74 61 63 74 3a 20 3c 73 69 70 3a 74 65 
73 74 30 30 31 40 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 74 72 61 6e 73 70 6f 72 74 3d 
54 4c 53 3e 0d 0a 41 75 74 68 6f 72 69 7a 61 74 
69 6f 6e 3a 20 44 69 67 65 73 74 20 75 73 65 72 
6e 61 6d 65 3d 22 74 65 73 74 30 30 31 22 2c 20 
72 65 61 6c 6d 3d 22 43 61 6c 6c 2d 65 58 22 2c 
20 6e 6f 6e 63 65 3d 22 35 33 61 34 61 36 34 39 
22 2c 20 75 72 69 3d 22 73 69 70 3a 31 32 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 22 2c 20 
72 65 73 70 6f 6e 73 65 3d 22 34 35 38 61 31 32 
38 63 31 30 30 63 32 61 31 34 36 37 65 37 61 36 
35 63 34 66 30 62 66 63 35 62 22 2c 20 61 6c 67 
6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 43 6f 6e 74 
65 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 
61 74 69 6f 6e 2f 73 64 70 0d 0a 41 6c 6c 6f 77 
3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 4f 2c 20 
50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 59 45 2c 
20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 4f 4e 53 
2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 49 53 54 
45 52 2c 20 53 55 42 53 43 52 49 42 45 2c 20 52 
45 46 45 52 2c 20 50 55 42 4c 49 53 48 2c 20 55 
50 44 41 54 45 2c 20 4d 45 53 53 41 47 45 0d 0a 
4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 20 37 30 
0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 59 65 
61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 50 20 32 
2e 36 31 2e 30 2e 37 30 0d 0a 53 75 70 70 6f 72 
74 65 64 3a 20 72 65 70 6c 61 63 65 73 0d 0a 41 
6c 6c 6f 77 2d 45 76 65 6e 74 73 3a 20 74 61 6c 
6b 2c 68 6f 6c 64 2c 63 6f 6e 66 65 72 65 6e 63 
65 2c 72 65 66 65 72 2c 63 68 65 63 6b 2d 73 79 
6e 63 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65 6e 67 
74 68 3a 20 33 30 32 0d 0a 0d 0a 76 3d 30 0d 0a 
6f 3d 2d 20 32 30 30 30 30 20 32 30 30 30 30 20 
49 4e 20 49 50 34 20 31 30 2e 30 2e 30 2e 31 37 
32 0d 0a 73 3d 53 44 50 20 64 61 74 61 0d 0a 63 
3d 49 4e 20 49 50 34 20 31 30 2e 30 2e 30 2e 31 
37 32 0d 0a 74 3d 30 20 30 0d 0a 6d 3d 61 75 64 
69 6f 20 31 31 37 38 30 20 52 54 50 2f 41 56 50 
20 30 20 38 20 31 38 20 39 20 31 30 31 0d 0a 61 
3d 72 74 70 6d 61 70 3a 30 20 50 43 4d 55 2f 38 
30 30 30 0d 0a 61 3d 72 74 70 6d 61 70 3a 38 20 
50 43 4d 41 2f 38 30 30 30 0d 0a 61 3d 72 74 70 
6d 61 70 3a 31 38 20 47 37 32 39 2f 38 30 30 30 
0d 0a 61 3d 66 6d 74 70 3a 31 38 20 61 6e 6e 65 
78 62 3d 6e 6f 0d 0a 61 3d 72 74 70 6d 61 70 3a 
39 20 47 37 32 32 2f 38 30 30 30 0d 0a 61 3d 66 
6d 74 70 3a 31 30 31 20 30 2d 31 35 0d 0a 61 3d 
72 74 70 6d 61 70 3a 31 30 31 20 74 65 6c 65 70 
68 6f 6e 65 2d 65 76 65 6e 74 2f 38 30 30 30 0d 
0a 61 3d 70 74 69 6d 65 3a 32 30 0d 0a 61 3d 73 
65 6e 64 72 65 63 76 0d 0a a9 eb bd 38 80 79 97 
4f a3 d5 9c 57 e3 df 03 9a 
checking mac (len 1049, version 301, ct 23 seq 5)
tls_check_mac mac type:MD5 md 1
Mac[16]:
a9 eb bd 38 80 79 97 4f a3 d5 9c 57 e3 df 03 9a 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 1049, seq = 2285, nxtseq = 3334
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 1049
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1811458558

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;53a4a649&quot;, uri=&quot;sip:[email protected]:5061&quot;, response=&quot;458a128c100c2a1467e7a65c4f0bfc5b&quot;, algorithm=MD5

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #36 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 464, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #37 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 464, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #39 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 485
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 480, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #40 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 485
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 480, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #42 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 675
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 670, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 670
Ciphertext[670]:
5f f9 62 c0 eb c7 e4 26 bc 27 bf 3b c4 7d 72 97 
ab 31 07 46 56 fb 67 db 5e 1d 90 1c ab 70 b1 5a 
ba 79 8b 74 02 39 69 81 87 f5 96 e9 3b 18 1c 1c 
ca cd db fc ea 7d 0d c2 e3 08 23 2c 17 0b b2 34 
02 95 d0 f0 38 4e 54 f6 2d 9c 8e c5 f7 78 e7 51 
ca 44 24 ef 68 4a 34 8d b2 3b 26 d5 b2 72 71 9c 
40 a0 2b 17 28 1a bd 5c 9f 91 d8 03 4c 73 d7 eb 
75 1e 52 14 bc af 6b 45 67 41 d4 a5 df 54 67 de 
f2 8f 86 6f dc b5 50 8a c9 b2 aa 8d 88 b5 79 21 
57 91 a9 58 1d 29 8e 2a a1 92 34 10 b4 a8 b3 7e 
b6 89 bf 06 69 0d b1 1e ec 9a e0 00 a0 a4 fd 25 
a1 a5 48 8b 7b 03 a6 5f 5a f3 40 52 e5 04 82 0f 
5d e3 61 af 45 17 95 5b 03 0d 31 29 1d 42 7e 41 
33 ed 5a 34 68 c0 1d 02 c1 80 b5 73 04 1c 71 d0 
a7 c3 ab 8b a9 c4 56 67 2b 6c 25 6c dc 2c 23 fa 
8d 69 17 e8 75 fe 0f c0 a0 8c fb a2 88 de d8 1f 
63 2a 7f 73 87 5a 14 ab 5f cd f0 53 1c cd 35 fb 
d1 c9 1d 15 59 26 b1 7d c3 ce 8d ef a5 5b 7e f2 
1b e8 77 31 58 41 c0 37 e8 37 b2 cc ac d3 92 e6 
ec 18 df df b0 53 bc 2d d3 a2 2c 0f c1 25 32 25 
ff 83 a6 f5 54 0a ca b7 9f 0e fe 2d 68 fa be 33 
b9 37 09 0c 40 00 c2 b3 9d f3 19 c9 3b cd 7c 17 
0b af c8 69 e0 eb 5f 9e ad e7 31 4b 1c d7 24 31 
64 22 20 08 5c 83 f0 aa f1 a1 94 25 03 9c 29 20 
9d 1e cd c4 ea 85 38 a6 f8 91 e8 3e c6 60 fa 7c 
04 88 6c d2 d4 db 65 ed 8c bc c2 d3 e4 db 8a ba 
c6 b2 a8 3b 74 2c 03 d5 f5 f5 c6 a7 04 de ef a7 
82 41 45 53 ec 4f 73 55 e1 ab 9e aa c6 86 68 8f 
1a 0f 6e 81 09 f1 41 d4 f1 54 39 93 63 76 2f b8 
6f ae 6f d0 79 53 8c 83 f6 0d 66 b0 ef 25 b0 3d 
f3 67 46 ed 3e 49 36 dc 05 e8 05 7c 08 6a 04 6d 
e0 74 72 7c 54 15 d5 cf 8c a4 25 4b 6e 24 c9 13 
15 c2 3e 73 c3 39 51 c0 58 35 8a 28 8f c8 68 ce 
35 9d 36 20 53 1b ed f9 1d ae 20 32 f8 ee 70 51 
b2 74 db ac 0c f0 ae db 64 9d cd 67 e9 56 f4 97 
65 38 4d 30 30 31 67 9f 96 d9 d0 92 2a 2d 25 03 
a3 87 dc 74 80 2d 7d 3f 98 f8 6e c8 e4 3f 01 de 
8a ce 84 8a 45 c6 77 53 04 92 bc 7b 84 08 82 c2 
2a ab 83 cf f1 a3 67 87 54 2f 2d 50 37 fb ad 46 
20 6f 60 ad 2c b9 2a 97 a9 5a 61 8f 7b ff 37 76 
f3 1f 7c ce 10 e6 91 52 9e 28 73 b4 3d 49 4f f9 
2f 49 af 4d 34 40 e6 c6 64 d5 3f ac b3 69 
Plaintext[670]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 38 34 36 38 31 39 33 34 0d 0a 46 72 
6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 31 
40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 
3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 36 0d 
0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 
31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 30 35 
33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 37 32 
0d 0a 43 53 65 71 3a 20 33 20 52 45 47 49 53 54 
45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 73 69 
70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 2e 30 
2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 73 70 
6f 72 74 3d 54 4c 53 3e 0d 0a 41 75 74 68 6f 72 
69 7a 61 74 69 6f 6e 3a 20 44 69 67 65 73 74 20 
75 73 65 72 6e 61 6d 65 3d 22 74 65 73 74 30 30 
31 22 2c 20 72 65 61 6c 6d 3d 22 43 61 6c 6c 2d 
65 58 22 2c 20 6e 6f 6e 63 65 3d 22 31 33 35 36 
61 37 37 62 22 2c 20 75 72 69 3d 22 73 69 70 3a 
31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 22 2c 
20 72 65 73 70 6f 6e 73 65 3d 22 37 31 31 38 65 
39 32 32 38 62 65 62 32 37 31 33 34 35 61 30 66 
65 32 62 63 38 61 64 32 33 33 32 22 2c 20 61 6c 
67 6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 41 6c 6c 
6f 77 3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 4f 
2c 20 50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 59 
45 2c 20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 4f 
4e 53 2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 49 
53 54 45 52 2c 20 53 55 42 53 43 52 49 42 45 2c 
20 52 45 46 45 52 2c 20 50 55 42 4c 49 53 48 2c 
20 55 50 44 41 54 45 2c 20 4d 45 53 53 41 47 45 
0d 0a 4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 20 
37 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 
59 65 61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 50 
20 32 2e 36 31 2e 30 2e 37 30 0d 0a 45 78 70 69 
72 65 73 3a 20 36 30 0d 0a 43 6f 6e 74 65 6e 74 
2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 25 cd 
a4 2f 59 43 78 84 74 8c 2f 76 2f 93 74 85 
checking mac (len 654, version 301, ct 23 seq 6)
tls_check_mac mac type:MD5 md 1
Mac[16]:
25 cd a4 2f 59 43 78 84 74 8c 2f 76 2f 93 74 85 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 654, seq = 3334, nxtseq = 3988
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 654
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK84681934

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]0.0.0.172

CSeq: 3 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #43 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 534
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 529, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #44 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 534
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 529, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #46 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 676
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 671, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 671
Ciphertext[671]:
83 9d d3 77 35 8e 56 17 f6 7a 30 e7 fb d9 34 23 
5b 71 9d 28 aa d8 ed 8f ab a9 13 e4 37 e9 f4 03 
fb a1 72 11 94 36 d3 64 7d 51 42 a7 16 1d 2e 83 
4e fd 86 b6 5f de f2 7c 56 fd 0d 8a 41 36 10 d5 
fd 32 39 8a 81 bc 18 d9 57 13 57 15 78 68 68 19 
9b 82 45 1d 2f 1e f7 1e 70 33 5b 4e ea 28 40 68 
3b af 53 3d f6 cc 47 97 c0 3c 63 ea e4 55 6b d3 
a6 15 f4 46 bb e9 7d 53 0d 19 ea ee 09 1c e7 74 
35 75 6c 0e f8 f8 d6 a4 01 81 60 cf 1f b3 f9 bc 
27 f9 12 c7 3a fc 04 dd 98 43 e3 2d 56 c9 27 12 
75 c9 0f f8 2e 48 c6 a7 8d 0d 7a 79 c3 8a 4d 3c 
8c 06 7d 96 76 2b 3f e1 f1 07 60 fc a9 ba e7 d1 
ea f1 43 a6 4a a0 cd e8 b0 0c f0 a4 9d 2e 3b 3c 
19 52 da 42 c1 c2 a7 4c 32 4a 58 b7 aa 37 cd 9f 
e3 80 ca fe 9a 9e 1b 55 70 d3 9e 7f 76 8c ab 63 
44 8b 1a 9b fc 02 6f df 62 b9 47 1b b9 74 16 15 
a4 14 79 4f 13 ef 2d 3f 8c 27 24 d9 60 fd 8c 46 
d5 ad a3 a5 a3 d1 dd 3f 16 02 8f 3d de 8d 63 7a 
63 66 ae 2e 01 99 63 ca 18 1b 54 05 5d 9e 0d 67 
67 60 f5 d6 4e 58 1b 5a 0a 3e ad 53 4f b7 30 59 
4a 36 2f 66 20 c3 f0 bf bf 6b 8e 2d 90 39 55 fd 
7c 7a 96 7a 8b 7c 53 d3 bb dc ee ba 55 1b cf 69 
8a df 1a b9 56 b8 c4 b0 26 40 1a 09 6a c4 b5 5b 
c4 ed 2e d8 d4 0c 09 6a dd 1e d7 6f 29 63 b9 19 
9c 0d 5e f6 1e 91 43 0d a6 c8 ba 5b 32 a3 7c df 
78 c3 9b 2a d9 77 a1 2f aa 01 37 14 5d 96 da 4c 
7e 73 1a c5 30 f6 f5 5a 0b 09 0f a9 ae fd 8a e2 
75 c2 7b b4 c5 78 3c 22 60 22 cb 44 62 28 80 d8 
15 17 6b e4 f8 02 76 9a a7 4f b6 3b 94 20 b1 18 
44 9f e4 0f 3c 8a c5 1a 06 a5 4d e6 58 49 ee d3 
8d 24 d6 f7 65 55 27 67 89 4b e5 70 3d d9 75 3a 
f7 eb cb 07 cb 6c c7 41 7e 18 24 42 3b 8a 78 45 
79 b6 6f ee 14 0c 03 85 b3 c1 72 1b f0 85 af 01 
61 27 54 1b e7 08 37 0d c6 5d 97 ed 48 05 2c a1 
ff 50 ef 0e f2 28 86 2d 3b b1 1c cf 35 1f b2 9f 
7b d1 e8 85 40 aa d1 c0 b5 fe 6e 8d 91 ae d6 e3 
d1 70 ce 3c 19 80 05 09 61 8d 1f 51 70 2c 43 bb 
81 ae a3 29 e8 aa 04 16 81 49 22 86 5b 32 1d 5e 
9c 7b 50 d8 ea 36 96 09 e9 95 05 b8 aa f3 ea 3a 
3b 4a 49 f5 73 47 9a 7f 38 18 00 c7 06 24 3a cb 
83 56 97 d0 0c f0 9c 38 09 5e f3 96 c0 30 88 f0 
c4 8b 39 34 6d f8 f3 c6 4e c0 22 35 56 ba 11 
Plaintext[671]:
52 45 47 49 53 54 45 52 20 73 69 70 3a 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 20 53 49 50 2f 
32 2e 30 0d 0a 56 69 61 3a 20 53 49 50 2f 32 2e 
30 2f 54 4c 53 20 31 30 2e 30 2e 30 2e 31 37 32 
3a 35 30 36 32 3b 62 72 61 6e 63 68 3d 7a 39 68 
47 34 62 4b 39 36 32 35 34 33 37 31 34 0d 0a 46 
72 6f 6d 3a 20 3c 73 69 70 3a 74 65 73 74 30 30 
31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 
3e 3b 74 61 67 3d 31 32 37 39 38 38 34 36 30 36 
0d 0a 54 6f 3a 20 3c 73 69 70 3a 74 65 73 74 30 
30 31 40 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 
31 3e 0d 0a 43 61 6c 6c 2d 49 44 3a 20 38 30 30 
35 33 37 33 39 33 40 31 30 2e 30 2e 30 2e 31 37 
32 0d 0a 43 53 65 71 3a 20 34 20 52 45 47 49 53 
54 45 52 0d 0a 43 6f 6e 74 61 63 74 3a 20 3c 73 
69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 30 2e 
30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 6e 73 
70 6f 72 74 3d 54 4c 53 3e 0d 0a 41 75 74 68 6f 
72 69 7a 61 74 69 6f 6e 3a 20 44 69 67 65 73 74 
20 75 73 65 72 6e 61 6d 65 3d 22 74 65 73 74 30 
30 31 22 2c 20 72 65 61 6c 6d 3d 22 43 61 6c 6c 
2d 65 58 22 2c 20 6e 6f 6e 63 65 3d 22 30 34 61 
38 62 32 33 33 22 2c 20 75 72 69 3d 22 73 69 70 
3a 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 22 
2c 20 72 65 73 70 6f 6e 73 65 3d 22 34 64 39 66 
36 30 30 31 36 64 32 37 63 38 38 31 64 30 62 34 
32 35 34 63 35 34 63 61 38 64 38 30 22 2c 20 61 
6c 67 6f 72 69 74 68 6d 3d 4d 44 35 0d 0a 41 6c 
6c 6f 77 3a 20 49 4e 56 49 54 45 2c 20 49 4e 46 
4f 2c 20 50 52 41 43 4b 2c 20 41 43 4b 2c 20 42 
59 45 2c 20 43 41 4e 43 45 4c 2c 20 4f 50 54 49 
4f 4e 53 2c 20 4e 4f 54 49 46 59 2c 20 52 45 47 
49 53 54 45 52 2c 20 53 55 42 53 43 52 49 42 45 
2c 20 52 45 46 45 52 2c 20 50 55 42 4c 49 53 48 
2c 20 55 50 44 41 54 45 2c 20 4d 45 53 53 41 47 
45 0d 0a 4d 61 78 2d 46 6f 72 77 61 72 64 73 3a 
20 37 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 
20 59 65 61 6c 69 6e 6b 20 53 49 50 2d 54 32 38 
50 20 32 2e 36 31 2e 30 2e 37 30 0d 0a 45 78 70 
69 72 65 73 3a 20 36 30 0d 0a 43 6f 6e 74 65 6e 
74 2d 4c 65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 9d 
dd fb ba 35 9a b3 b4 32 82 63 85 9d 8a 96 11 
checking mac (len 655, version 301, ct 23 seq 7)
tls_check_mac mac type:MD5 md 1
Mac[16]:
9d dd fb ba 35 9a b3 b4 32 82 63 85 9d 8a 96 11 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 655, seq = 3988, nxtseq = 4643
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 655
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK962543714

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 4 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;04a8b233&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;4d9f60016d27c881d0b4254c54ca8d80&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #47 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 553
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 548, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #48 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 553
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 548, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #50 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 784
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 779, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #51 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 784
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 779, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #55 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 401
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 396, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 396
Ciphertext[396]:
d1 df 6e 63 67 3d 5e b1 2b ec b0 f8 50 af eb 6d 
6f 90 59 18 2f b3 e7 70 b8 1f 67 db 5b 87 11 c7 
d9 c1 28 54 2f 25 c6 a5 d0 ef b1 ac bf 71 f7 b5 
ed bc 65 d1 58 05 1e 2b bc ac e7 09 ff 09 78 c0 
17 9d b4 32 c8 4b c7 f6 f7 94 40 fe d6 af 54 6c 
ca 4d b5 ec 4d 44 85 9d 1a 3a 0e 0d a5 56 99 5d 
7e 21 86 ed 12 a1 33 47 a1 b8 83 29 8d e9 8f 3a 
01 10 62 d1 99 77 65 b6 d7 8a e9 e6 b9 a8 ef 3e 
db 88 6b 91 91 87 8f ce ba 4e df 1b ad 18 4f d4 
65 b3 91 86 22 2f 5f 27 83 68 07 2e 42 ff 7c 70 
a0 7f 9a 2d 90 2f 07 3c b9 b0 54 66 d1 53 d7 c7 
18 48 8d 48 b2 91 2f 2d 2e 51 ac 04 2b ef e1 ac 
98 66 3a 49 ea 67 a6 f9 d8 e3 8f 70 fe 50 1d b9 
1c 1f 84 8e bb 60 ac 40 8e b5 bb 50 36 12 bd 86 
99 06 a0 ca e6 29 93 4e 33 03 0d f5 27 a6 6e 50 
49 b6 14 75 e5 8c ee f4 ee 65 5b 94 56 2c 65 c8 
ec 5e aa e6 b3 96 56 db a5 81 25 57 d7 91 be 37 
90 e2 c3 24 18 e8 91 af da 52 bd cd f4 02 6e bd 
78 d9 68 07 fc 69 99 f8 a3 ba 36 54 59 32 ce 9e 
28 4f fd b6 cc e9 cd f2 9a ef 55 01 2d a3 b4 21 
81 3b 33 ca db d9 45 4d 53 d2 05 a0 d0 d8 0e ee 
1b 8a a1 08 4a 42 64 3a f5 84 85 9a bf 61 de 6c 
60 f4 67 36 b7 a8 fb d4 50 27 4f 0b d8 46 b4 cf 
0e 4a 7e 00 6e 5f 2b 48 28 29 bd 32 62 ce f0 50 
a5 ed b1 74 20 1f 1c c2 59 19 7a 7e 
Plaintext[396]:
41 43 4b 20 73 69 70 3a 31 32 40 31 30 2e 30 2e 
34 2e 36 33 3a 35 30 36 31 3b 74 72 61 6e 73 70 
6f 72 74 3d 54 4c 53 20 53 49 50 2f 32 2e 30 0d 
0a 56 69 61 3a 20 53 49 50 2f 32 2e 30 2f 54 4c 
53 20 31 30 2e 30 2e 30 2e 31 37 32 3a 35 30 36 
32 3b 62 72 61 6e 63 68 3d 7a 39 68 47 34 62 4b 
31 39 36 37 33 37 39 36 39 35 0d 0a 46 72 6f 6d 
3a 20 3c 73 69 70 3a 74 65 73 74 30 30 31 40 31 
30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 
61 67 3d 36 30 37 34 39 31 33 32 39 0d 0a 54 6f 
3a 20 3c 73 69 70 3a 31 32 40 31 30 2e 30 2e 34 
2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 3d 61 73 
33 34 33 35 39 36 37 62 0d 0a 43 61 6c 6c 2d 49 
44 3a 20 31 30 37 31 31 32 39 39 35 31 40 31 30 
2e 30 2e 30 2e 31 37 32 0d 0a 43 53 65 71 3a 20 
32 20 41 43 4b 0d 0a 43 6f 6e 74 61 63 74 3a 20 
3c 73 69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 
30 2e 30 2e 31 37 32 3a 35 30 36 32 3b 74 72 61 
6e 73 70 6f 72 74 3d 54 4c 53 3e 0d 0a 4d 61 78 
2d 46 6f 72 77 61 72 64 73 3a 20 37 30 0d 0a 55 
73 65 72 2d 41 67 65 6e 74 3a 20 59 65 61 6c 69 
6e 6b 20 53 49 50 2d 54 32 38 50 20 32 2e 36 31 
2e 30 2e 37 30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 
65 6e 67 74 68 3a 20 30 0d 0a 0d 0a 9e cd b7 a4 
64 c7 80 6b c9 d1 69 66 d0 2e d1 53 
checking mac (len 380, version 301, ct 23 seq 8)
tls_check_mac mac type:MD5 md 1
Mac[16]:
9e cd b7 a4 64 c7 80 6b c9 d1 69 66 d0 2e d1 53 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 380, seq = 4643, nxtseq = 5023
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 380
decrypted app data fragment: ACK sip:[email protected]:5061;transport=TLS SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1967379695

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as3435967b

Call-ID: [email protected]

CSeq: 2 ACK

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #610 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 583
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 578, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #611 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 583
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 578, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #613 (first time)
  conversation = 0000000007071880, ssl_session = 0000000007071FB8
  record: offset = 0, reported_length_remaining = 301
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 296, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 296
Ciphertext[296]:
4d 95 c3 9d ee 7d 71 1a 38 3f d9 4c b0 82 68 5d 
c7 b6 d9 68 c3 dc c0 c8 33 ec e5 85 22 90 09 d8 
68 cb f9 de cf a7 06 30 6d 7f 84 25 dc fb 25 97 
d3 a4 ec 6a a3 a2 47 07 6c b7 1f 7e 01 c3 5a 1c 
da e7 6d a0 09 5f 70 95 fc d5 a7 1c 23 1e 58 fd 
78 84 85 00 ab d7 98 49 9b 72 d5 4b ea bb 05 77 
e8 a1 64 03 3a 16 a4 95 6a 13 83 98 c6 65 a6 14 
e2 c8 33 d9 05 2b 6e 62 8f 39 7a 51 9b 86 83 b9 
d9 65 2c a0 b3 c2 8a 56 05 a1 6e 6e d0 f6 9f 11 
dc 7c 98 c6 c7 30 4e 8b 95 6f 88 4c 99 c4 98 89 
b8 d9 d3 59 81 e9 a1 ba 6f b3 37 20 9f 49 74 b6 
a6 7a 74 13 49 11 92 ba b2 97 38 4b d6 6d 60 d6 
8c 67 6a 15 a8 55 48 33 f7 2f 3f 22 d7 6f 95 54 
da 3f 24 3c c8 57 0e b0 ca f5 51 62 3e 59 2c 4e 
a3 62 a7 1d c5 07 38 ce fa f7 00 45 4f bf b2 a9 
fd b3 51 5d 74 8a ef 85 5f 60 c8 95 88 1b 11 e5 
9b 93 cf 68 47 18 f9 f1 db a1 05 22 84 1e c6 2b 
aa 9f ff 75 ce 80 ef 74 3b e5 3e dc 74 e4 a3 bb 
a3 15 e3 ba 9f 69 87 0d 
Plaintext[296]:
53 49 50 2f 32 2e 30 20 32 30 30 20 4f 4b 0d 0a 
56 69 61 3a 20 53 49 50 2f 32 2e 30 2f 54 4c 53 
20 31 30 2e 30 2e 34 2e 36 33 3a 35 30 36 31 3b 
62 72 61 6e 63 68 3d 7a 39 68 47 34 62 4b 34 65 
38 31 30 63 38 33 3b 72 70 6f 72 74 0d 0a 46 72 
6f 6d 3a 20 3c 73 69 70 3a 31 32 40 31 30 2e 30 
2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 3d 
61 73 33 34 33 35 39 36 37 62 0d 0a 54 6f 3a 20 
3c 73 69 70 3a 74 65 73 74 30 30 31 40 31 30 2e 
30 2e 34 2e 36 33 3a 35 30 36 31 3e 3b 74 61 67 
3d 36 30 37 34 39 31 33 32 39 0d 0a 43 61 6c 6c 
2d 49 44 3a 20 31 30 37 31 31 32 39 39 35 31 40 
31 30 2e 30 2e 30 2e 31 37 32 0d 0a 43 53 65 71 
3a 20 31 30 32 20 42 59 45 0d 0a 55 73 65 72 2d 
41 67 65 6e 74 3a 20 59 65 61 6c 69 6e 6b 20 53 
49 50 2d 54 32 38 50 20 32 2e 36 31 2e 30 2e 37 
30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65 6e 67 74 
68 3a 20 30 0d 0a 0d 0a 80 2f f9 7a 89 bd b3 21 
44 82 c5 17 55 fe 0d ac 
checking mac (len 280, version 301, ct 23 seq 9)
tls_check_mac mac type:MD5 md 1
Mac[16]:
80 2f f9 7a 89 bd b3 21 44 82 c5 17 55 fe 0d ac 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 280, seq = 5023, nxtseq = 5303
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 280
decrypted app data fragment: SIP/2.0 200 OK

Via: SIP/2.0/TLS 10.0.4.63:5061;branch=z9hG4bK4e810c83;rport

From: &lt;sip:[email protected]:5061&gt;;tag=as3435967b

To: &lt;sip:[email protected]:5061&gt;;tag=607491329

Call-ID: [email protected]

CSeq: 102 BYE

User-Agent: Yealink SIP-T28P 2.61.0.70

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #5 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 98
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 89 bytes, remaining 98

dissect_ssl enter frame #8 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #9 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #10 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2125
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2107 bytes, remaining 2116 
  record: offset = 2116, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 2121 length 0 bytes, remaining 2125

dissect_ssl enter frame #14 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
  record: offset = 139, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 145, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #15 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #16 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 156 offset 11 length 3052702 bytes, remaining 43

dissect_ssl enter frame #18 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 513
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 492
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK633221630

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #19 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #20 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 523
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #16 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 156 offset 11 length 3052702 bytes, remaining 43

dissect_ssl enter frame #22 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 677
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 656
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1847283880

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #23 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #24 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 554
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #26 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 904
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 883
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 1 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #27 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #28 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #30 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 275
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 254
decrypted app data fragment: ACK sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1995397980

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as5818025c

Call-ID: [email protected]

CSeq: 1 ACK

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #33 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1070
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 1049
decrypted app data fragment: INVITE sip:[email protected]:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1811458558

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 2 INVITE

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;53a4a649&quot;, uri=&quot;sip:[email protected]:5061&quot;, response=&quot;458a128c100c2a1467e7a65c4f0bfc5b&quot;, algorithm=MD5

Content-Type: application/sdp

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Supported: replaces

Allow-Events: talk,hold,conference,refer,check-sync

Content-Length: 302

v=0

o=- 20000 20000 IN IP4 10.0.0.172

s=SDP data

c=IN IP4 10.0.0.172

t=0 0

m=audio 11780 RTP/AVP 0 8 18 9 101

a=rtpmap:0 PCMU/8000

a=rtpmap:8 PCMA/8000

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:9 G722/8000

a=fmtp:101 0-15

a=rtpmap:101 telephone-event/8000

a=ptime:20

a=sendrecv

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #36 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #37 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #39 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 485
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #40 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 485
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #42 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 675
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 654
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK84681934

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 3 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;1356a77b&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;7118e9228beb271345a0fe2bc8ad2332&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #43 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 534
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #44 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 534
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #46 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 676
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 655
decrypted app data fragment: REGISTER sip:10.0.4.63:5061 SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK962543714

From: &lt;sip:[email protected]:5061&gt;;tag=1279884606

To: &lt;sip:[email protected]:5061&gt;

Call-ID: [email protected]

CSeq: 4 REGISTER

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Authorization: Digest username=&quot;test001&quot;, realm=&quot;Call-eX&quot;, nonce=&quot;04a8b233&quot;, uri=&quot;sip:10.0.4.63:5061&quot;, response=&quot;4d9f60016d27c881d0b4254c54ca8d80&quot;, algorithm=MD5

Allow: INVITE, INFO, PRACK, ACK, BYE, CANCEL, OPTIONS, NOTIFY, REGISTER, SUBSCRIBE, REFER, PUBLISH, UPDATE, MESSAGE

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Expires: 60

Content-Length: 0

dissect_ssl3_record found association 0000000006322100

dissect_ssl enter frame #47 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 553
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #48 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 553
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #50 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 784
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #51 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 784
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 5061 found 0000000006322100

dissect_ssl enter frame #55 (already visited)
  conversation = 0000000007071880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 401
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 8003 found 0000000000000000
association_find: TCP port 5061 found 0000000006322100
dissect_ssl3_record decrypted len 380
decrypted app data fragment: ACK sip:[email protected]:5061;transport=TLS SIP/2.0

Via: SIP/2.0/TLS 10.0.0.172:5062;branch=z9hG4bK1967379695

From: &lt;sip:[email protected]:5061&gt;;tag=607491329

To: &lt;sip:[email protected]:5061&gt;;tag=as3435967b

Call-ID: [email protected]

CSeq: 2 ACK

Contact: &lt;sip:[email protected]:5062;transport=TLS&gt;

Max-Forwards: 70

User-Agent: Yealink SIP-T28P 2.61.0.70

Content-Length: 0

dissect_ssl3_record found association 0000000006322100</code></pre></div><div id="question-tags" class="tags-container tags">tlsv1 sip ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/f70b9bf28dea69b63edaf6ee463f83ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamicque&#39;s gravatar image" /><p>jamicque<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamicque has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Aug '12, 07:52</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-13610" class="comments-container"></div><div id="comment-tools-13610" class="comment-tools"></div><div class="clear"></div><div id="comment-13610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13645"></span>

<div id="answer-container-13645" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13645-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like your capture mechanism is creating duplicate entries for the server packets, this disrupts decryption. You can either use "editcap -d" to remove the duplicates or you can use "Edit -&gt; Ignore ..." in Wireshark to ignore the duplicates and get decryption working. And of course you should check your capture mechanism to see whether you can make it stop generating duplicates :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13645" class="comments-container"><span id="13658"></span><div id="comment-13658" class="comment"><div id="post-13658-score" class="comment-score"></div><div class="comment-text"><p>Thx SYN-bit ignoring those packet really solved the problem I'm wondering why these packet have occurred. The server is running on vserver, and the host have interface bonding - this can be the problem - I will try to work it out - thx!.</p><p>BTW is there any way in wireshark to automatically ignore all duplicates?</p></div><div id="comment-13658-info" class="comment-info"><span class="comment-age">(15 Aug '12, 12:55)</span> jamicque</div></div><span id="13662"></span><div id="comment-13662" class="comment"><div id="post-13662-score" class="comment-score"></div><div class="comment-text"><blockquote><p>BTW is there any way in wireshark to automatically ignore all duplicates?</p></blockquote><p>No, editcap would be your best best in de-duplicating</p></div><div id="comment-13662-info" class="comment-info"><span class="comment-age">(15 Aug '12, 15:09)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-13645" class="comment-tools"></div><div class="clear"></div><div id="comment-13645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

