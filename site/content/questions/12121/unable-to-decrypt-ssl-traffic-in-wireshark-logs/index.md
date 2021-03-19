+++
type = "question"
title = "unable to decrypt ssl traffic in wireshark logs"
description = '''I have applied the correct ips as well as the server key for this log but am still unable to decypt it . this waqs taken from the client system connected to my server. there were no proxies involved. ssl_association_remove removing TCP 443 - http handle 00000000049BDF30 1821 bytes read PKCS#12 impor...'''
date = "2012-06-21T19:47:00Z"
lastmod = "2012-06-21T20:05:00Z"
weight = 12121
keywords = [ "decryption" ]
aliases = [ "/questions/12121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unable to decrypt ssl traffic in wireshark logs](/questions/12121/unable-to-decrypt-ssl-traffic-in-wireshark-logs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have applied the correct ips as well as the server key for this log but am still unable to decypt it . this waqs taken from the client system connected to my server. there were no proxies involved.</p><pre><code>ssl_association_remove removing TCP 443 - http handle 00000000049BDF30
1821 bytes read
PKCS#12 imported
Bag 0/0: Encrypted
Bag 0/0 decrypted: Certificate
Certificate imported: *.eclinicalweb.com &lt;&lt;ERROR&gt;&gt;, KeyID #########################
Bag 1/0: PKCS#8 Encrypted key
Private key imported: KeyID **:**:**:**:**:**:**:**:**:**:**:**:**:**..........
ssl_init IPv4 addr &#39;63.251.45.171&#39; (63.251.45.171) port &#39;443&#39; filename &#39;C:\Users\jalaj\Documents\mongoose.p12&#39; password(only for p12 file) &#39;**********&#39;
ssl_init private key file &#39;C:\Users\jalaj\Documents\mongoose.p12
successfully loaded.

association_add TCP port 443 protocol http handle 00000000049BDF30

dissect_ssl enter frame #3 (first time)
ssl_session_init: initializing ptr 00000000063A1DA8 size 680
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #4 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #6 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #9 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #10 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 388

dissect_ssl enter frame #15 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 324

dissect_ssl enter frame #18 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 436

dissect_ssl enter frame #19 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #20 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #21 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 404

dissect_ssl enter frame #22 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #23 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 20

dissect_ssl enter frame #24 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #25 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #26 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #27 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #28 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 340

dissect_ssl enter frame #29 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #30 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #31 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 244

dissect_ssl enter frame #32 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 132

dissect_ssl enter frame #33 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 164

dissect_ssl enter frame #34 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 324

dissect_ssl enter frame #35 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 292

dissect_ssl enter frame #108 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #114 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #115 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #116 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #117 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #118 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 308

dissect_ssl enter frame #119 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #120 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #121 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #122 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #123 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #124 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 388

dissect_ssl enter frame #125 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 404

dissect_ssl enter frame #126 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #127 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #128 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #129 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 68

dissect_ssl enter frame #130 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 132

dissect_ssl enter frame #131 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #132 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 68

dissect_ssl enter frame #133 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 68

dissect_ssl enter frame #143 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #144 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #145 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #146 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #147 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 500

dissect_ssl enter frame #148 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #149 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 68

dissect_ssl enter frame #150 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 132

dissect_ssl enter frame #151 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #152 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 52

dissect_ssl enter frame #155 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #157 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #160 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #164 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #168 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #169 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #172 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #174 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #177 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #180 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512
  need_desegmentation: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #286 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 21829

dissect_ssl enter frame #286 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 187

dissect_ssl enter frame #292 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #294 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #295 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #298 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #299 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #301 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #306 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #309 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #313 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 512

dissect_ssl enter frame #314 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 448
  need_desegmentation: offset = 0, reported_length_remaining = 448

dissect_ssl enter frame #581 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #752 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 19468

dissect_ssl enter frame #752 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 484
  need_desegmentation: offset = 0, reported_length_remaining = 484

dissect_ssl enter frame #924 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 36
  need_desegmentation: offset = 0, reported_length_remaining = 36

dissect_ssl enter frame #997 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 13149

dissect_ssl enter frame #997 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 307
  need_desegmentation: offset = 0, reported_length_remaining = 307

dissect_ssl enter frame #1006 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 2400

dissect_ssl enter frame #1006 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 467
  need_desegmentation: offset = 0, reported_length_remaining = 467

dissect_ssl enter frame #1164 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 10988

dissect_ssl enter frame #1164 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 187
  need_desegmentation: offset = 0, reported_length_remaining = 187

dissect_ssl enter frame #1576 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 28247

dissect_ssl enter frame #1576 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 72
  need_desegmentation: offset = 0, reported_length_remaining = 72

dissect_ssl enter frame #1604 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 6952

dissect_ssl enter frame #1604 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 396
  need_desegmentation: offset = 0, reported_length_remaining = 396

dissect_ssl enter frame #1864 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 12587

dissect_ssl enter frame #1864 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 5
  need_desegmentation: offset = 0, reported_length_remaining = 5

dissect_ssl enter frame #1901 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 6949

dissect_ssl enter frame #1901 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 60
  need_desegmentation: offset = 0, reported_length_remaining = 60

dissect_ssl enter frame #1929 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 7576

dissect_ssl enter frame #1929 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 164
  need_desegmentation: offset = 0, reported_length_remaining = 164

dissect_ssl enter frame #1950 (first time)
ssl_session_init: initializing ptr 000000000642ACF8 size 680
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 156
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 151, ssl state 0x00
association_find: TCP port 53971 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 147 bytes, remaining 156 
packet_from_server: is from server - FALSE
ssl_find_private_key server 209.104.252.126:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #1953 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 912
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 80, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 76 bytes, remaining 85 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 85, reported_length_remaining = 827
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 813, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 90 length 809 bytes, remaining 903 
  record: offset = 903, reported_length_remaining = 9
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 908 length 0 bytes, remaining 912

dissect_ssl enter frame #1954 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
trying to use SSL keylog in 
failed to open SSL keylog
  record: offset = 139, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 226 offset 150 length 1596209 bytes, remaining 182

dissect_ssl enter frame #1958 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 131 offset 11 length 6225535 bytes, remaining 43

dissect_ssl enter frame #1959 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 574
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 569, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 53971 found 0000000000000000
association_find: TCP port 443 found 00000000094CBE80

dissect_ssl enter frame #1960 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 123
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 118, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000094CBE80

dissect_ssl enter frame #1961 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 845
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 840, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 53971 found 0000000000000000
association_find: TCP port 443 found 00000000094CBE80

dissect_ssl enter frame #2009 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 8726

dissect_ssl enter frame #2009 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 38
  need_desegmentation: offset = 0, reported_length_remaining = 38

dissect_ssl enter frame #2028 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 426
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 421, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000094CBE80

dissect_ssl enter frame #2029 (first time)
  conversation = 000000000642A3D0, ssl_session = 000000000642ACF8
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #2062 (first time)
  conversation = 00000000063A1880, ssl_session = 00000000063A1DA8
  record: offset = 0, reported_length_remaining = 5744</code></pre></div><div id="question-tags" class="tags-container tags">decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '12, 19:47</strong></p><img src="https://secure.gravatar.com/avatar/873d1cb77a5c6be056cd7b8261e15cf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jalaj&#39;s gravatar image" /><p>jalaj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jalaj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jun '12, 20:02</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-12121" class="comments-container"></div><div id="comment-tools-12121" class="comment-tools"></div><div class="clear"></div><div id="comment-12121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12122"></span>

<div id="answer-container-12122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12122-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like your SSL traffic is going to server 209.104.252.126 (ssl_find_private_key server 209.104.252.126:443), however you configured 63.251.45.171 as server-address in the SSL protocol preferences (ssl_init IPv4 addr '63.251.45.171' (63.251.45.171) port '443' filename 'C:\Users\jalaj\Documents\mongoose.p12' password(only for p12 file) '<strong><em>*</em></strong>***').</p><p>You need to reconfigure your SSL protocol settings with server-ip-address 209.104.252.126</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '12, 20:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12122" class="comments-container"><span id="12135"></span><div id="comment-12135" class="comment"><div id="post-12135-score" class="comment-score"></div><div class="comment-text"><p>thanks will try that too</p></div><div id="comment-12135-info" class="comment-info"><span class="comment-age">(23 Jun '12, 06:15)</span> jalaj</div></div><span id="12151"></span><div id="comment-12151" class="comment"><div id="post-12151-score" class="comment-score"></div><div class="comment-text"><p>I tried that but it did not help. so i used a different ip wireshark and took that servers key. this did not have such ip differences but i am still unable to decrypt.</p><p><code> ssl_association_remove removing TCP 443 - http handle 000000000473F660 1821 bytes read PKCS#12 imported Bag 0/0: Encrypted Bag 0/0 decrypted: Certificate Certificate imported: .eclinicalweb.com &lt;&lt;error&gt;&gt;, KeyID ***** Bag 1/0: PKCS#8 Encrypted key Private key imported: KeyID ::::::::::... ssl_init IPv4 addr '63.251.45.162' (63.251.45.162) port '443' filename 'C:\Users\jalaj\mongoose.p12' password(only for p12 file) '' ssl_init private key file C:\Users\jalaj\mongoose.p12 successfully loaded. association_add TCP port 443 protocol http handle 000000000473F660</code></p><p><code></code></p><p><code>dissect_ssl enter frame #1 (first time) ssl_session_init: initializing ptr 0000000006041AE0 size 680   conversation = 0000000006041880, ssl_session = 0000000006041AE0   record: offset = 0, reported_length_remaining = 1280   need_desegmentation: offset = 0, reported_length_remaining = 1280</code></p><code></code><p>dissect_ssl enter frame #2 (first time) conversation = 0000000006041880, ssl_session = 0000000006041AE0 record: offset = 0, reported_length_remaining = 1415 dissect_ssl3_record found version 0x0301 -&gt; state 0x10 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 1410, ssl state 0x10 association_find: TCP port 443 found 0000000008073D30 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #4 (first time) conversation = 0000000006041880, ssl_session = 0000000006041AE0 record: offset = 0, reported_length_remaining = 1265 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 1260, ssl state 0x10 association_find: TCP port 443 found 0000000008073D30 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #33 (first time) ssl_session_init: initializing ptr 0000000006043D40 size 680 conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 109 dissect_ssl3_record: content_type 22 decrypt_ssl3_record: app_data len 104, ssl state 0x00 association_find: TCP port 2810 found 0000000000000000 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 1 offset 5 length 100 bytes, remaining 109 packet_from_server: is from server - FALSE ssl_find_private_key server 63.251.45.162:443 dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01</p><p>dissect_ssl enter frame #34 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 79 dissect_ssl3_record found version 0x0301 -&gt; state 0x11 dissect_ssl3_record: content_type 22 decrypt_ssl3_record: app_data len 74, ssl state 0x11 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13 ssl_restore_session can't find stored session dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17 dissect_ssl3_hnd_srv_hello trying to generate keys ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57) dissect_ssl3_hnd_srv_hello can't generate keyring material</p><p>dissect_ssl enter frame #35 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 43 dissect_ssl3_record: content_type 20 dissect_ssl3_change_cipher_spec packet_from_server: is from server - TRUE ssl_change_cipher SERVER record: offset = 6, reported_length_remaining = 37 dissect_ssl3_record: content_type 22 decrypt_ssl3_record: app_data len 32, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 2 offset 11 length 9471278 bytes, remaining 43</p><p>dissect_ssl enter frame #37 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 43 dissect_ssl3_record: content_type 20 dissect_ssl3_change_cipher_spec packet_from_server: is from server - FALSE ssl_change_cipher CLIENT record: offset = 6, reported_length_remaining = 37 dissect_ssl3_record: content_type 22 decrypt_ssl3_record: app_data len 32, ssl state 0x17 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 195 offset 11 length 117357 bytes, remaining 43</p><p>dissect_ssl enter frame #38 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 849 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 844, ssl state 0x17 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 2810 found 0000000000000000 association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #41 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 1165 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 1160, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #42 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 755 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 750, ssl state 0x17 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 2810 found 0000000000000000 association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #43 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 1280 need_desegmentation: offset = 0, reported_length_remaining = 1280</p><p>dissect_ssl enter frame #44 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 1415 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 1410, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #46 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 516 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 511, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #47 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 848 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 843, ssl state 0x17 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 2810 found 0000000000000000 association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #48 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 1168 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 1163, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</p><p>dissect_ssl enter frame #49 (first time) conversation = 00000000060435A8, ssl_session = 0000000006043D40 record: offset = 0, reported_length_remaining = 779 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 774, ssl state 0x17 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 2810 found 0000000000000000 association_find: TCP port 443 found 0000000008073D30</p></code><p><code>dissect_ssl enter frame #50 (first time)   conversation = 00000000060435A8, ssl_session = 0000000006043D40   record: offset = 0, reported_length_remaining = 585 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 580, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 443 found 0000000008073D30</code></p></div><div id="comment-12151-info" class="comment-info"><span class="comment-age">(25 Jun '12, 11:04)</span> jalaj</div></div><span id="12152"></span><div id="comment-12152" class="comment"><div id="post-12152-score" class="comment-score"></div><div class="comment-text"><p>i did try changing the ip in the ssl protocol in wireshark but that did not help so i tried the below given method to troubleshoot further</p></div><div id="comment-12152-info" class="comment-info"><span class="comment-age">(25 Jun '12, 11:06)</span> jalaj</div></div><span id="35496"></span><div id="comment-35496" class="comment"><div id="post-35496-score" class="comment-score"></div><div class="comment-text"><p>hi,</p><p>who is the certificate authority? was it a SAN cert?</p><p>I am having the same problem, trying to decrypt HTTPS traffic and unable to do so.</p></div><div id="comment-35496-info" class="comment-info"><span class="comment-age">(14 Aug '14, 17:01)</span> net_tech</div></div><span id="35507"></span><div id="comment-35507" class="comment"><div id="post-35507-score" class="comment-score"></div><div class="comment-text"><p>@net_tech: Please ask your own question, instead of commenting on a 2 year old (abandoned) question ;-))</p></div><div id="comment-35507-info" class="comment-info"><span class="comment-age">(15 Aug '14, 09:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12122" class="comment-tools"></div><div class="clear"></div><div id="comment-12122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

