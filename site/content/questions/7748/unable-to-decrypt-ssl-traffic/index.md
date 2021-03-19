+++
type = "question"
title = "Unable to decrypt SSL traffic"
description = '''I am attempting to decrypt ssl communication for troublshooting purposes but am unable to decode the traffic. It looks like there is a problem with not enough data to generate the key based on the debug log.  This part of the log file seems to be the same each time I try to decrypt something. The po...'''
date = "2011-12-02T12:32:00Z"
lastmod = "2011-12-02T12:32:00Z"
weight = 7748
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/7748" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt SSL traffic](/questions/7748/unable-to-decrypt-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7748-score" class="post-score" title="current number of votes">0</div><span id="post-7748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to decrypt ssl communication for troublshooting purposes but am unable to decode the traffic. It looks like there is a problem with not enough data to generate the key based on the debug log.<br />
</p><p>This part of the log file seems to be the same each time I try to decrypt something. The portion after this changes as I try different applications/protocols</p><p>===============================================================================================</p><pre><code>Private key imported: KeyID 85:0c:cf:1b:45:ec:f6:b3:99:02:09:5f:d7:4a:a9:b6:...
ssl_init IPv4 addr &#39;172.26.134.118&#39; (172.26.134.118) port &#39;443&#39; filename &#39;C:\Users\mmull04\Documents\myprivatekey.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\Users\mmull04\Documents\myprivatekey.pem successfully loaded.
association_add TCP port 443 protocol http handle 0000000004AA8DC0

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 00000000063C1D00 size 680
  conversation = 00000000063C1880, ssl_session = 00000000063C1D00
  record: offset = 0, reported_length_remaining = 72
packet_from_server: is from server - FALSE
ssl_find_private_key server 172.26.134.118:443
client random len: 16 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
  conversation = 00000000063C1880, ssl_session = 00000000063C1D00
  record: offset = 0, reported_length_remaining = 969
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 964, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 969 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)</code></pre><p>=============================================================================================</p><p>The log file begins as follows</p><pre><code>Private key imported: KeyID 85:0c:cf:1b:45:ec:f6:b3:99:02:09:5f:d7:4a:a9:b6:...
ssl_init IPv4 addr &#39;172.26.134.118&#39; (172.26.134.118) port &#39;443&#39; filename &#39;C:\Users\mmull04\Documents\myprivatekey.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\Users\mmull04\Documents\myprivatekey.pem successfully loaded.
association_add TCP port 443 protocol http handle 0000000004AA8DC0

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 00000000063C1D00 size 680
  conversation = 00000000063C1880, ssl_session = 00000000063C1D00
  record: offset = 0, reported_length_remaining = 72
packet_from_server: is from server - FALSE
ssl_find_private_key server 172.26.134.118:443
client random len: 16 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
  conversation = 00000000063C1880, ssl_session = 00000000063C1D00
  record: offset = 0, reported_length_remaining = 969
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 964, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 969 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 882 bytes, remaining 969 
dissect_ssl3_handshake iteration 0 type 14 offset 965 length 0 bytes, remaining 969

dissect_ssl enter frame #6 (first time)
  conversation = 00000000063C1880, ssl_session = 00000000063C1D00
  record: offset = 0, reported_length_remaining = 118
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 70, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
pre master encrypted[64]:
6f 8e 98 88 4e 4e e5 06 f7 39 ae c3 ab 93 e6 bc 
3f 9c 40 3d ce 60 00 e2 83 76 56 e1 4f e1 94 57 
2c 86 c0 40 d3 9f 72 05 5b f9 b5 e1 e4 bb ce e1 
e5 fb 61 6d c2 d0 42 54 07 f0 0d 1e 34 e8 67 21 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 15 bytes, decr_len 63
decrypted_unstrip_pre_master[63]:
02 e0 41 59 ae ac 12 93 d5 38 33 ac d4 0b 00 03 
01 98 06 4f 85 ee c8 62 73 87 0a c1 17 79 8e 0b 
72 7f 21 80 3a 6d f5 ca 9d d5 e7 c9 13 8c 32 67 
51 f1 3a c3 eb 74 d9 a8 47 7a 02 ca b3 73 22 
pre master secret[48]:
03 01 98 06 4f 85 ee c8 62 73 87 0a c1 17 79 8e 
0b 72 7f 21 80 3a 6d f5 ca 9d d5 e7 c9 13 8c 32 
67 51 f1 3a c3 eb 74 d9 a8 47 7a 02 ca b3 73 22 
ssl_generate_keyring_material:PRF(pre_master_secret)
pre master secret[48]:
03 01 98 06 4f 85 ee c8 62 73 87 0a c1 17 79 8e 
0b 72 7f 21 80 3a 6d f5 ca 9d d5 e7 c9 13 8c 32 
67 51 f1 3a c3 eb 74 d9 a8 47 7a 02 ca b3 73 22 
client random[32]:
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
d6 6d 40 16 db 54 79 16 e1 9b c3 43 9e 27 d1 66 
server random[32]:
4e d9 2f bf 13 a1 64 bb d7 14 0b da d7 b2 39 29 
af 1a 56 a7 e7 be a2 70 b5 24 af 0d e1 a1 bf 0f 
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
03 01 98 06 4f 85 ee c8 62 73 87 0a c1 17 79 8e 
0b 72 7f 21 80 3a 6d f5 
tls_hash: hash seed[77]:
6d 61 73 74 65 72 20 73 65 63 72 65 74 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 d6 6d 40 
16 db 54 79 16 e1 9b c3 43 9e 27 d1 66 4e d9 2f 
bf 13 a1 64 bb d7 14 0b da d7 b2 39 29 af 1a 56 
a7 e7 be a2 70 b5 24 af 0d e1 a1 bf 0f 
hash out[48]:
22 cc 15 aa dc 33 96 75 2f bb 7f 34 65 bb c9 ef 
d6 62 65 c9 9c 6b b7 58 d7 c7 85 7b f3 a4 82 f9 
96 b0 60 fe c2 49 31 4e e7 e3 72 69 1a 2b 4b 19 
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
ca 9d d5 e7 c9 13 8c 32 67 51 f1 3a c3 eb 74 d9 
a8 47 7a 02 ca b3 73 22 
tls_hash: hash seed[77]:
6d 61 73 74 65 72 20 73 65 63 72 65 74 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 d6 6d 40 
16 db 54 79 16 e1 9b c3 43 9e 27 d1 66 4e d9 2f 
bf 13 a1 64 bb d7 14 0b da d7 b2 39 29 af 1a 56 
a7 e7 be a2 70 b5 24 af 0d e1 a1 bf 0f 
hash out[48]:
92 92 f9 eb 89 ad c3 d0 01 5d 83 7e 45 0a c2 b6 
b7 ef db 9e 14 1c 08 21 fd 4a 68 84 6d e7 a7 6e 
fd 09 1d 51 98 bc 52 cc 7c 63 86 da 51 b5 27 89 
PRF out[48]:
b0 5e ec 41 55 9e 55 a5 2e e6 fc 4a 20 b1 0b 59 
61 8d be 57 88 77 bf 79 2a 8d ed ff 9e 43 25 97 
6b b9 7d af 5a f5 63 82 9b 80 f4 b3 4b 9e 6c 90 
master secret[48]:
b0 5e ec 41 55 9e 55 a5 2e e6 fc 4a 20 b1 0b 59 
61 8d be 57 88 77 bf 79 2a 8d ed ff 9e 43 25 97 
6b b9 7d af 5a f5 63 82 9b 80 f4 b3 4b 9e 6c 90 
ssl_generate_keyring_material sess key generation
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
b0 5e ec 41 55 9e 55 a5 2e e6 fc 4a 20 b1 0b 59 
61 8d be 57 88 77 bf 79 
tls_hash: hash seed[77]:
6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 4e d9 2f 
bf 13 a1 64 bb d7 14 0b da d7 b2 39 29 af 1a 56 
a7 e7 be a2 70 b5 24 af 0d e1 a1 bf 0f 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 d6 6d 40 
16 db 54 79 16 e1 9b c3 43 9e 27 d1 66 
hash out[64]:
bb b3 7a 0b db a4 14 d5 8b 29 8f aa 6d 1a f3 1c 
8b 1e 3c 63 4d 15 6a 0b 36 d4 45 94 96 18 e8 06 
13 0d cc 8f e6 57 51 1c d6 61 18 a4 9d 94 7a ed 
6d 53 92 9b 3b b5 c4 8f ba a4 41 b9 ca 45 9a 9e 
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
2a 8d ed ff 9e 43 25 97 6b b9 7d af 5a f5 63 82 
9b 80 f4 b3 4b 9e 6c 90 
tls_hash: hash seed[77]:
6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 4e d9 2f 
bf 13 a1 64 bb d7 14 0b da d7 b2 39 29 af 1a 56 
a7 e7 be a2 70 b5 24 af 0d e1 a1 bf 0f 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 d6 6d 40 
16 db 54 79 16 e1 9b c3 43 9e 27 d1 66 
hash out[64]:
7a b6 65 69 6c 3b a7 02 b7 56 2d 8d 5a d5 ad 4f 
45 b5 d0 fd f2 d5 79 12 ae 7b 7c 09 4e 8b b3 3e 
85 c6 99 f8 dd 3d 44 c6 cc bc 89 32 c2 75 d6 1e 
bb 9e 41 03 46 ec 61 a7 cf 2a 56 ad 7a 04 70 d8 
PRF out[64]:
c1 05 1f 62 b7 9f b3 d7 3c 7f a2 27 37 cf 5e 53 
ce ab ec 9e bf c0 13 19 98 af 39 9d d8 93 5b 38 
96 cb 55 77 3b 6a 15 da 1a dd 91 96 5f e1 ac f3 
d6 cd d3 98 7d 59 a5 28 75 8e 17 14 b0 41 ea 46 
key expansion[64]:
c1 05 1f 62 b7 9f b3 d7 3c 7f a2 27 37 cf 5e 53 
ce ab ec 9e bf c0 13 19 98 af 39 9d d8 93 5b 38 
96 cb 55 77 3b 6a 15 da 1a dd 91 96 5f e1 ac f3 
d6 cd d3 98 7d 59 a5 28 75 8e 17 14 b0 41 ea 46 
Client MAC key[16]:
c1 05 1f 62 b7 9f b3 d7 3c 7f a2 27 37 cf 5e 53 
Server MAC key[16]:
ce ab ec 9e bf c0 13 19 98 af 39 9d d8 93 5b 38 
Client Write key[16]:
96 cb 55 77 3b 6a 15 da 1a dd 91 96 5f e1 ac f3 
Server Write key[16]:
d6 cd d3 98 7d 59 a5 28 75 8e 17 14 b0 41 ea 46 
Client Write IV[8]:
00 00 7f 60 00 00 00 00 
Server Write IV[8]:
00 00 00 00 00 00 00 00 
ssl_generate_keyring_material ssl_create_decoder(client)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material ssl_create_decoder(server)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material: client seq 0, server seq 0
ssl_save_session stored session id[32]:
22 22 02 f0 f8 ad de 03 6e 80 5f 73 5f 4c b4 20 
f4 d5 c1 ad 40 4d 72 08 8b 76 b1 e4 e3 5e ba ca 
ssl_save_session stored master secret[48]:
b0 5e ec 41 55 9e 55 a5 2e e6 fc 4a 20 b1 0b 59 
61 8d be 57 88 77 bf 79 2a 8d ed ff 9e 43 25 97 
6b b9 7d af 5a f5 63 82 9b 80 f4 b3 4b 9e 6c 90 
dissect_ssl3_handshake session keys successfully generated
  record: offset = 75, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
63 13 f5 70 15 45 0f 2b e3 ef 82 93 5b 7c b2 31 
cf 0b af c3 58 04 1b 8f a3 e0 85 f8 0c 35 79 6a 
Plaintext[32]:
14 00 00 0c 3a 41 de ff 51 4f 01 10 6f 29 cf e8 
97 9c 3d ab cb ff e1 c5 06 87 13 8a ef 3d f4 8a 
checking mac (len 16, version 301, ct 22 seq 0)
tls_check_mac mac type:MD5 md 1
Mac[16]:
97 9c 3d ab cb ff e1 c5 06 87 13 8a ef 3d f4 8a 
ssl_decrypt_record: mac ok
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '11, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/dca43b1845c50b5fc716431e181b47e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iwtsyb&#39;s gravatar image" /><p><span>iwtsyb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iwtsyb has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '11, 13:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7748" class="comments-container"></div><div id="comment-tools-7748" class="comment-tools"></div><div class="clear"></div><div id="comment-7748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

