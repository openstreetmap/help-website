+++
type = "question"
title = "Difficulty Decrypting SSL"
description = '''I am having trouble decrypting TLSv1.2 and TCP traffic. I am fairly certain that the cipher is not DHE, and I have provided wireshark with the private key through the SSL section in preferences, and it appears to have loaded properly. When the key is applied, all of the proper SSL handshake packets ...'''
date = "2016-07-07T10:22:00Z"
lastmod = "2016-07-12T11:28:00Z"
weight = 53909
keywords = [ "ssl", "tcp", "ssl_decrypt" ]
aliases = [ "/questions/53909" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Difficulty Decrypting SSL](/questions/53909/difficulty-decrypting-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53909-score" class="post-score" title="current number of votes">0</div><span id="post-53909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having trouble decrypting TLSv1.2 and TCP traffic. I am fairly certain that the cipher is not DHE, and I have provided wireshark with the private key through the SSL section in preferences, and it appears to have loaded properly. When the key is applied, all of the proper SSL handshake packets become visible. However, outside of those, the rest of the packets remain encrypted or are now marked as malformed. When I attempt to view the contents, there is a decrypted SSL data option, but it often only contains 1 byte of data or up to half of the size of the encrypted data. Not sure what is going wrong. Here is an excerpt of my debug file:</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) 
GnuTLS version:    3.2.15 
Libgcrypt version: 1.6.2

ssl_association_remove removing TCP 48784 - tcp handle 04433168
KeyID[20]:
| 20 fe 52 45 8e 5c 65 fd f7 60 88 85 b2 0c 0e ef | .RE.\e..`......|
| a1 13 b9 58                                     |...X            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file C:/Users/Trader/Documents/ssl/key.nocrypt.pem successfully loaded.
ssl_init port &#39;48784&#39; filename &#39;C:/Users/Trader/Documents/ssl/key.nocrypt.pem&#39; password(only for p12 file) &#39;&#39;
association_add TCP port 48784 protocol tcp handle 04433168

dissect_ssl enter frame #4 (first time)
association_find: TCP port 64106 found 00000000
packet_from_server: is from server - FALSE
  conversation = 06250BB0, ssl_session = 06251108
  record: offset = 0, reported_length_remaining = 198
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 193
decrypt_ssl3_record: app_data len 193, ssl state 0x00
association_find: TCP port 64106 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 189 bytes, remaining 198 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - TRUE
  conversation = 06250BB0, ssl_session = 06251108
  record: offset = 0, reported_length_remaining = 1053
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 81
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0x003C TLS_RSA_WITH_AES_128_CBC_SHA256 -&gt; state 0x17
  record: offset = 86, reported_length_remaining = 967
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 91 953
decrypt_ssl3_record: app_data len 953, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 91 length 949 bytes, remaining 1044 
lookup(KeyID)[20]:
| 20 fe 52 45 8e 5c 65 fd f7 60 88 85 b2 0c 0e ef | .RE.\e..`......|
| a1 13 b9 58                                     |...X            |
ssl_find_private_key_by_pubkey: lookup result: 04FE7208
  record: offset = 1044, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 1049 4
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1049 length 0 bytes, remaining 1053

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - FALSE
  conversation = 06250BB0, ssl_session = 06251108
  record: offset = 0, reported_length_remaining = 267
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 262
decrypt_ssl3_record: app_data len 262, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 217
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
pre master encrypted[256]:
| 22 f2 8e 47 f1 f4 dc 78 b6 6c 2d b1 92 e4 9f 50 |&quot;..G...x.l-....P|
| b4 10 25 ca f9 6c e2 02 4b b1 93 12 d2 96 d2 84 |..%..l..K.......|
| b6 6b 7c 53 6d 96 36 7f 2c c5 57 a0 42 f0 13 88 |.k|Sm.6.,.W.B...|
| 71 35 99 41 25 c7 11 aa b7 a5 4b 3f 83 2c b5 49 |q5.A%.....K?.,.I|
| da 75 bc 99 2a f8 a0 9a fc 5f 2f 9f 15 0c 33 24 |.u..*...._/...3$|
| 1b 3d ac 04 a2 14 4b 67 f6 4f 80 ce 39 44 16 62 |.=....Kg.O..9D.b|
| 81 b5 06 8f 19 53 67 6e 73 c4 eb 7a 23 2d 9f 47 |.....Sgns..z#-.G|
| f8 76 3d df 21 db f2 d2 e2 c5 0a ed 6f b5 40 66 |.v=.!.......o.@f|
| 52 2c a1 0e e3 e6 93 fc 56 7d 00 94 92 14 2c db |R,......V}....,.|
| c2 0a 56 21 92 51 1f d0 d0 4d ec 51 87 65 e4 ba |..V!.Q...M.Q.e..|
| 4c 32 3a e4 0d 37 9d 4c f9 dc 5a 5d 15 32 28 ba |L2:..7.L..Z].2(.|
| 70 f6 c2 4d f5 f7 2b 35 c6 f4 43 ea a4 54 9e 64 |p..M..+5..C..T.d|
| b9 f4 fb 15 41 9e 6b ea 62 af 94 eb ce c6 4c fb |....A.k.b.....L.|
| d5 8f 0b f8 53 02 9a 68 eb c5 e3 13 11 cf f5 7d |....S..h.......}|
| 2f 22 db 0e 27 8f 2a 2f ea cd 3f 29 73 ae 4c a9 |/&quot;..&#39;.*/..?)s.L.|
| 7e 33 78 56 d6 cd af bc 5d e0 33 e3 d1 be ae dc |~3xV....].3.....|
ssl_decrypt_pre_master_secret: RSA_private_decrypt
decrypted_unstrip_pre_master[255]:
| 02 72 2f ed 58 7d 3e df be 21 99 e1 b4 41 f1 45 |.r/.X}&gt;..!...A.E|
| a9 ab 15 ce 5f 06 f1 23 fd 65 13 b5 4b e7 ce b8 |...._..#.e..K...|
| 42 fc 3f 57 c4 d4 f6 eb cd fd 63 b4 46 3d fa a4 |B.?W......c.F=..|
| c0 f8 7e 6d ad 9a 89 38 29 3e 6a a8 52 9f b6 ef |..~m...8)&gt;j.R...|
| ef c2 88 55 86 9f 1e c1 e3 fa 6a cc a4 af 87 c0 |...U......j.....|
| 6e 79 be e8 15 8a e5 5b bc 76 fc 2f 4a a1 7a 7b |ny.....[.v./J.z{|
| 3a 88 41 bd 10 8f 2d 0f d7 ab 1e fb 76 af 8c d8 |:.A...-.....v...|
| 42 a4 d4 af c7 6b 4a a8 fe 3b 1c bb ce 87 ef 05 |B....kJ..;......|
| 5f 19 ed 28 de 28 df ce 6c 2d 8f 32 8c 81 d5 4e |_..(.(..l-.2...N|
| a9 96 fc 6f 0f 44 8b 54 e4 63 22 4d f2 2a 4a 4c |...o.D.T.c&quot;M.*JL|
| 57 01 34 0f 8b c3 d7 f3 09 14 e5 63 43 d8 1f 39 |W.4........cC..9|
| dc 15 67 d5 6c 74 63 82 03 c5 1f 82 5c c0 3d 27 |..g.ltc.....\.=&#39;|
| 01 5e 54 b8 1d 04 43 a5 b8 8d 58 68 91 5a 00 03 |.^T...C...Xh.Z..|
| 03 7d 86 db d0 65 87 43 40 5d 79 71 44 46 51 25 |.}[email protected]]yqDFQ%|
| 88 a5 d6 43 3d f0 8c 1e 86 af 4f 0d 4d e3 47 ea |...C=.....O.M.G.|
| 94 f6 5d 39 d0 8b c4 56 19 ee 85 b0 9b da 55    |..]9...V......U |
pcry_private_decrypt: stripping 207 bytes, decr_len 255
pre master secret[48]:
| 03 03 7d 86 db d0 65 87 43 40 5d 79 71 44 46 51 |..}[email protected]]yqDFQ|
| 25 88 a5 d6 43 3d f0 8c 1e 86 af 4f 0d 4d e3 47 |%...C=.....O.M.G|
| ea 94 f6 5d 39 d0 8b c4 56 19 ee 85 b0 9b da 55 |...]9...V......U|

dissect_ssl enter frame #8 (first time)
packet_from_server: is from server - FALSE
  conversation = 06250BB0, ssl_session = 06251108
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x257
ssl_generate_keyring_material:PRF(pre_master_secret)
pre master secret[48]:
| 03 03 7d 86 db d0 65 87 43 40 5d 79 71 44 46 51 |..}[email protected]]yqDFQ|
| 25 88 a5 d6 43 3d f0 8c 1e 86 af 4f 0d 4d e3 47 |%...C=.....O.M.G|
| ea 94 f6 5d 39 d0 8b c4 56 19 ee 85 b0 9b da 55 |...]9...V......U|
client random[32]:
| 57 7e 75 c9 74 07 bb c8 21 2f 4c 03 9c d5 68 aa |W~u.t...!/L...h.|
| 05 84 bf 88 cd 1b 79 7f 04 fc 2e ce c6 8e 28 72 |......y.......(r|
server random[32]:
| 57 7e 75 c9 30 09 d3 f8 7e 11 35 b1 f6 b6 38 69 |W~u.0...~.5...8i|
| f6 68 04 c6 83 12 11 91 25 eb 2c 72 f5 49 3a 45 |.h......%.,r.I:E|
tls12_prf: tls_hash(hash_alg SHA256 secret_len 48 seed_len 77 )
tls_hash: hash secret[48]:
| 03 03 7d 86 db d0 65 87 43 40 5d 79 71 44 46 51 |..}[email protected]]yqDFQ|
| 25 88 a5 d6 43 3d f0 8c 1e 86 af 4f 0d 4d e3 47 |%...C=.....O.M.G|
| ea 94 f6 5d 39 d0 8b c4 56 19 ee 85 b0 9b da 55 |...]9...V......U|
tls_hash: hash seed[77]:
| 6d 61 73 74 65 72 20 73 65 63 72 65 74 57 7e 75 |master secretW~u|
| c9 74 07 bb c8 21 2f 4c 03 9c d5 68 aa 05 84 bf |.t...!/L...h....|
| 88 cd 1b 79 7f 04 fc 2e ce c6 8e 28 72 57 7e 75 |...y.......(rW~u|
| c9 30 09 d3 f8 7e 11 35 b1 f6 b6 38 69 f6 68 04 |.0...~.5...8i.h.|
| c6 83 12 11 91 25 eb 2c 72 f5 49 3a 45          |.....%.,r.I:E   |
hash out[48]:
| 8b b3 87 41 d7 1b b9 80 ba 49 54 63 34 40 3e bf |[email protected]&gt;.|
| fd b8 70 18 c5 60 f6 d7 70 eb f0 e9 5d 9a 78 33 |..p..`..p...].x3|
| c8 73 ab 5f 04 f8 9a 6b 17 8b 18 41 a5 bb b7 58 |.s._...k...A...X|
PRF out[48]:
| 8b b3 87 41 d7 1b b9 80 ba 49 54 63 34 40 3e bf |[email protected]&gt;.|
| fd b8 70 18 c5 60 f6 d7 70 eb f0 e9 5d 9a 78 33 |..p..`..p...].x3|
| c8 73 ab 5f 04 f8 9a 6b 17 8b 18 41 a5 bb b7 58 |.s._...k...A...X|
master secret[48]:
| 8b b3 87 41 d7 1b b9 80 ba 49 54 63 34 40 3e bf |[email protected]&gt;.|
| fd b8 70 18 c5 60 f6 d7 70 eb f0 e9 5d 9a 78 33 |..p..`..p...].x3|
| c8 73 ab 5f 04 f8 9a 6b 17 8b 18 41 a5 bb b7 58 |.s._...k...A...X|
ssl_generate_keyring_material sess key generation
tls12_prf: tls_hash(hash_alg SHA256 secret_len 48 seed_len 77 )
tls_hash: hash secret[48]:
| 8b b3 87 41 d7 1b b9 80 ba 49 54 63 34 40 3e bf |[email protected]&gt;.|
| fd b8 70 18 c5 60 f6 d7 70 eb f0 e9 5d 9a 78 33 |..p..`..p...].x3|
| c8 73 ab 5f 04 f8 9a 6b 17 8b 18 41 a5 bb b7 58 |.s._...k...A...X|
tls_hash: hash seed[77]:
| 6b 65 79 20 65 78 70 61 6e 73 69 6f 6e 57 7e 75 |key expansionW~u|
| c9 30 09 d3 f8 7e 11 35 b1 f6 b6 38 69 f6 68 04 |.0...~.5...8i.h.|
| c6 83 12 11 91 25 eb 2c 72 f5 49 3a 45 57 7e 75 |.....%.,r.I:EW~u|
| c9 74 07 bb c8 21 2f 4c 03 9c d5 68 aa 05 84 bf |.t...!/L...h....|
| 88 cd 1b 79 7f 04 fc 2e ce c6 8e 28 72          |...y.......(r   |
hash out[128]:
| 7f aa 67 69 7a 2d 2e 55 fe 42 f2 86 fb 93 a9 33 |..giz-.U.B.....3|
| af 4a 27 75 ef 39 9d 85 20 ed ab ad 9e 6f 84 ab |.J&#39;u.9.. ....o..|
| ee c7 cb d3 64 19 e3 7a cd bb ae 3f 02 d2 55 bf |....d..z...?..U.|
| 94 9e 6f 54 6c 98 b8 c1 db 46 3b 49 84 88 16 31 |..oTl....F;I...1|
| 5d 43 41 a4 f4 2a 29 86 19 8b 73 53 f3 56 3b 5a |]CA..*)...sS.V;Z|
| 5e 72 ae 33 d8 19 ce 5f d5 5d ec f2 29 94 a3 8d |^r.3..._.]..)...|
| 2a b8 84 89 ef dc 4f fe 3d cc 03 22 5e 97 f4 83 |*.....O.=..&quot;^...|
| 20 52 de 6d 92 36 66 bf 16 dc 8c 98 7b e5 9a 4a | R.m.6f.....{..J|
PRF out[128]:
| 7f aa 67 69 7a 2d 2e 55 fe 42 f2 86 fb 93 a9 33 |..giz-.U.B.....3|
| af 4a 27 75 ef 39 9d 85 20 ed ab ad 9e 6f 84 ab |.J&#39;u.9.. ....o..|
| ee c7 cb d3 64 19 e3 7a cd bb ae 3f 02 d2 55 bf |....d..z...?..U.|
| 94 9e 6f 54 6c 98 b8 c1 db 46 3b 49 84 88 16 31 |..oTl....F;I...1|
| 5d 43 41 a4 f4 2a 29 86 19 8b 73 53 f3 56 3b 5a |]CA..*)...sS.V;Z|
| 5e 72 ae 33 d8 19 ce 5f d5 5d ec f2 29 94 a3 8d |^r.3..._.]..)...|
| 2a b8 84 89 ef dc 4f fe 3d cc 03 22 5e 97 f4 83 |*.....O.=..&quot;^...|
| 20 52 de 6d 92 36 66 bf 16 dc 8c 98 7b e5 9a 4a | R.m.6f.....{..J|
key expansion[128]:
| 7f aa 67 69 7a 2d 2e 55 fe 42 f2 86 fb 93 a9 33 |..giz-.U.B.....3|
| af 4a 27 75 ef 39 9d 85 20 ed ab ad 9e 6f 84 ab |.J&#39;u.9.. ....o..|
| ee c7 cb d3 64 19 e3 7a cd bb ae 3f 02 d2 55 bf |....d..z...?..U.|
| 94 9e 6f 54 6c 98 b8 c1 db 46 3b 49 84 88 16 31 |..oTl....F;I...1|
| 5d 43 41 a4 f4 2a 29 86 19 8b 73 53 f3 56 3b 5a |]CA..*)...sS.V;Z|
| 5e 72 ae 33 d8 19 ce 5f d5 5d ec f2 29 94 a3 8d |^r.3..._.]..)...|
| 2a b8 84 89 ef dc 4f fe 3d cc 03 22 5e 97 f4 83 |*.....O.=..&quot;^...|
| 20 52 de 6d 92 36 66 bf 16 dc 8c 98 7b e5 9a 4a | R.m.6f.....{..J|
Client MAC key[32]:
| 7f aa 67 69 7a 2d 2e 55 fe 42 f2 86 fb 93 a9 33 |..giz-.U.B.....3|
| af 4a 27 75 ef 39 9d 85 20 ed ab ad 9e 6f 84 ab |.J&#39;u.9.. ....o..|
Server MAC key[32]:
| ee c7 cb d3 64 19 e3 7a cd bb ae 3f 02 d2 55 bf |....d..z...?..U.|
| 94 9e 6f 54 6c 98 b8 c1 db 46 3b 49 84 88 16 31 |..oTl....F;I...1|
Client Write key[16]:
| 5d 43 41 a4 f4 2a 29 86 19 8b 73 53 f3 56 3b 5a |]CA..*)...sS.V;Z|
Server Write key[16]:
| 5e 72 ae 33 d8 19 ce 5f d5 5d ec f2 29 94 a3 8d |^r.3..._.]..)...|
Client Write IV[16]:
| 2a b8 84 89 ef dc 4f fe 3d cc 03 22 5e 97 f4 83 |*.....O.=..&quot;^...|
Server Write IV[16]:
| 20 52 de 6d 92 36 66 bf 16 dc 8c 98 7b e5 9a 4a | R.m.6f.....{..J|
ssl_generate_keyring_material ssl_create_decoder(client)
ssl_create_decoder CIPHER: AES
decoder initialized (digest len 32)
ssl_generate_keyring_material ssl_create_decoder(server)
ssl_create_decoder CIPHER: AES
decoder initialized (digest len 32)
ssl_generate_keyring_material: client seq 0, server seq 0
ssl_save_master_key inserted (pre-)master secret for Client Random
stored key[32]:
| 57 7e 75 c9 74 07 bb c8 21 2f 4c 03 9c d5 68 aa |W~u.t...!/L...h.|
| 05 84 bf 88 cd 1b 79 7f 04 fc 2e ce c6 8e 28 72 |......y.......(r|
stored (pre-)master secret[48]:
| 8b b3 87 41 d7 1b b9 80 ba 49 54 63 34 40 3e bf |[email protected]&gt;.|
| fd b8 70 18 c5 60 f6 d7 70 eb f0 e9 5d 9a 78 33 |..p..`..p...].x3|
| c8 73 ab 5f 04 f8 9a 6b 17 8b 18 41 a5 bb b7 58 |.s._...k...A...X|
ssl_save_master_key inserted (pre-)master secret for Session ID
stored key[32]:
| a7 72 f4 44 18 ab a4 ba 69 b8 8d 05 ab 4b 02 57 |.r.D....i....K.W|
| 8b 29 2f 75 b0 c5 f4 b1 43 b7 31 ca 7f 95 81 bb |.)/u....C.1.....|
stored (pre-)master secret[48]:
| 8b b3 87 41 d7 1b b9 80 ba 49 54 63 34 40 3e bf |[email protected]&gt;.|
| fd b8 70 18 c5 60 f6 d7 70 eb f0 e9 5d 9a 78 33 |..p..`..p...].x3|
| c8 73 ab 5f 04 f8 9a 6b 17 8b 18 41 a5 bb b7 58 |.s._...k...A...X|
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #10 (first time)
packet_from_server: is from server - FALSE
  conversation = 06250BB0, ssl_session = 06251108
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 80, ssl state 0x23F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 80
Ciphertext[80]:
| 69 ef 0b b4 58 70 8c 18 05 79 cd c8 ae 27 59 71 |i...Xp...y...&#39;Yq|
| 8e f1 8f 8a 90 1a d1 e7 14 69 be 97 df 02 16 a8 |.........i......|
| 34 90 b4 c1 88 c6 e2 e1 1f a0 74 42 a7 40 c9 f7 |[email protected]|
| 8c 6f c1 9a af 65 ef 46 85 53 6e f8 6d b2 02 ad |.o...e.F.Sn.m...|
| 74 34 03 25 c7 e7 1e 88 c4 b7 a5 d3 a5 2e b7 f7 |t4.%............|
ssl_decrypt_record: allocating 112 bytes for decrypt data (old len 32)
Plaintext[64]:
| 14 00 00 0c 4d 29 67 7e b8 a8 8e c9 42 dc 80 bb |....M)g~....B...|
| 36 9d ca df c1 0d 33 83 7d 23 59 b1 f5 dd d0 2e |6.....3.}#Y.....|
| 45 2b cb 7c 18 4b 6b 21 d7 55 d5 27 35 4c 24 0c |E+.|.Kk!.U.&#39;5L$.|
| 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f |................|
ssl_decrypt_record found padding 15 final len 48
checking mac (len 16, version 303, ct 22 seq 0)
tls_check_mac mac type:SHA256 md 8
Mac[32]:
| 36 9d ca df c1 0d 33 83 7d 23 59 b1 f5 dd d0 2e |6.....3.}#Y.....|
| 45 2b cb 7c 18 4b 6b 21 d7 55 d5 27 35 4c 24 0c |E+.|.Kk!.U.&#39;5L$.|
ssl_decrypt_record: mac ok
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/4c299277b9a6967470c3e8c4c51bcc4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dldurks&#39;s gravatar image" /><p><span>dldurks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dldurks has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '16, 10:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-53909" class="comments-container"><span id="53910"></span><div id="comment-53910" class="comment"><div id="post-53910-score" class="comment-score">1</div><div class="comment-text"><p>The conversation is using TLS_RSA_WITH_AES_128_CBC_SHA256 which is not an uncommon cipher. The handshake message seems correctly decrypted. Can you add a pcap <strong>file</strong> with the full handshake and some example application data packets?</p></div><div id="comment-53910-info" class="comment-info"><span class="comment-age">(07 Jul '16, 10:29)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-53909" class="comment-tools"></div><div class="clear"></div><div id="comment-53909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53914"></span>

<div id="answer-container-53914" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53914-score" class="post-score" title="current number of votes">0</div><span id="post-53914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dldurks has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have no idea what protocol it is, but it seems to decrypt fine for me. I reproduced it as follows, create premaster.txt containing:</p><pre><code>CLIENT_RANDOM 577e75c97407bbc8212f4c039cd568aa0584bf88cd1b797f04fc2ecec68e2872 8bb38741d71bb980ba49546334403ebffdb87018c560f6d770ebf0e95d9a7833c873ab5f04f89a6b178b1841a5bbb758</code></pre><p>Run tshark with:</p><pre><code>tshark -o ssl.keylog_file:premaster.txt -r test7.pcap -d tcp.port==48784,ssl -Y ssl -o ssl.debug_file:ssl-debug.txt</code></pre><p>The debug log file contains "ssl_decrypt_record: mac ok" so the data is apparently correctly decrypted.</p><p>To me it seems that your application fragments the data over multiple TLS records. Remember that TLS offers a stream with no message boundaries as far as the application is concerned. To see the decrypted stream, use the <strong>Follow</strong> -&gt; <strong>SSL Stream</strong> option. If you set the "Show and save data as" option to "Hex Dump", then you might be able to interpret your protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-53914" class="comments-container"><span id="53940"></span><div id="comment-53940" class="comment"><div id="post-53940-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Lekensteyn</span> I believe it should be TCP protocol. Unfortunately, when I attempt to follow the SSL stream, I am presented with only two lines of data, or 24 bytes. I agree that this is odd as it appears to decrypt successfully, yet it seems to only decrypt a very small amount of data.</p></div><div id="comment-53940-info" class="comment-info"><span class="comment-age">(08 Jul '16, 07:59)</span> <span class="comment-user userinfo">dldurks</span></div></div><span id="53942"></span><div id="comment-53942" class="comment"><div id="post-53942-score" class="comment-score"></div><div class="comment-text"><p>In addition, after decryption, a majority of my packets are marked as malformed</p></div><div id="comment-53942-info" class="comment-info"><span class="comment-age">(08 Jul '16, 08:26)</span> <span class="comment-user userinfo">dldurks</span></div></div><span id="53967"></span><div id="comment-53967" class="comment"><div id="post-53967-score" class="comment-score"></div><div class="comment-text"><p>@didurks It does not look like the TCP protocol at all though it could be a protocol layered on top of TCP. Where did you get this capture from?</p></div><div id="comment-53967-info" class="comment-info"><span class="comment-age">(10 Jul '16, 14:27)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="53980"></span><div id="comment-53980" class="comment"><div id="post-53980-score" class="comment-score"></div><div class="comment-text"><p><span>@Lekensteyn</span> As far as I know it is TCP traffic with TLS layered on top of it. I don't want to go into too much detail, but this traffic represents communication between my server and a java application.</p></div><div id="comment-53980-info" class="comment-info"><span class="comment-age">(11 Jul '16, 07:03)</span> <span class="comment-user userinfo">dldurks</span></div></div><span id="53982"></span><div id="comment-53982" class="comment"><div id="post-53982-score" class="comment-score"></div><div class="comment-text"><p>@didurks If it is communication between your server and a Java application, could it be a proprietary protocol not implemented in Wireshark? Anyway, I showed how you could try to interpret the protocol, is that helpful?</p></div><div id="comment-53982-info" class="comment-info"><span class="comment-age">(11 Jul '16, 08:14)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="53984"></span><div id="comment-53984" class="comment not_top_scorer"><div id="post-53984-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Lekensteyn</span> It should definitely be tcp, and it is using from port 48786 on the host machine. What makes you think that that it is something other than TCP? I am the most confused as to why only a very small part of the encrypted data is being decrypted. When I select the Decrypted SSL data tab in most of the packets, I only get 1 byte of decrypted data. I tried to interpret the protocol, but whenever I try to follow either the TCP stream or the SSL stream, the data appears to remain encrypted.</p></div><div id="comment-53984-info" class="comment-info"><span class="comment-age">(11 Jul '16, 08:54)</span> <span class="comment-user userinfo">dldurks</span></div></div><span id="53988"></span><div id="comment-53988" class="comment not_top_scorer"><div id="post-53988-score" class="comment-score"></div><div class="comment-text"><p>@didurks Let me try to clarify this. TCP is involved, but it is not the application data protocol in SSL. You have this layered structure: TCP / SSL / your protocol (encrypted by SSL). Seeing one byte of decrypted SSL for each record is certainly possible, it is not wrong. In the capture file from your deleted comment (which I do not have anymore) I clearly saw a pattern but could not interpret it since I have no idea what protocol is involved. <strong>The SSL dissector works fine</strong>, but perhaps you expected to see a different application protocol other than the current one.</p></div><div id="comment-53988-info" class="comment-info"><span class="comment-age">(11 Jul '16, 10:03)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="53993"></span><div id="comment-53993" class="comment not_top_scorer"><div id="post-53993-score" class="comment-score"></div><div class="comment-text"><p>@didurks For now you can use the "protocol" field in the SSL RSA keys dialog (later on I plan to make it a Decode as... option). What application data protocol is it anyway?</p></div><div id="comment-53993-info" class="comment-info"><span class="comment-age">(11 Jul '16, 12:48)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="53994"></span><div id="comment-53994" class="comment not_top_scorer"><div id="post-53994-score" class="comment-score"></div><div class="comment-text"><p><span>@Lekensteyn</span> I'll have to figure that out, but which application layer protocols are supported?</p></div><div id="comment-53994-info" class="comment-info"><span class="comment-age">(11 Jul '16, 13:18)</span> <span class="comment-user userinfo">dldurks</span></div></div><span id="54008"></span><div id="comment-54008" class="comment not_top_scorer"><div id="post-54008-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@dldurks</span> If you enter an invalid protocol name at the RSA key files dialog then you will get the valid protocol names.</p></div><div id="comment-54008-info" class="comment-info"><span class="comment-age">(12 Jul '16, 09:58)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="54009"></span><div id="comment-54009" class="comment not_top_scorer"><div id="post-54009-score" class="comment-score"></div><div class="comment-text"><p><span>@Lekensteyn</span> the application layer is apparently using protocol buffers, so unfortunately I won't be able to get much help from wireshark here.</p></div><div id="comment-54009-info" class="comment-info"><span class="comment-age">(12 Jul '16, 11:28)</span> <span class="comment-user userinfo">dldurks</span></div></div></div><div id="comment-tools-53914" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-53914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

