+++
type = "question"
title = "Having trouble decrypting TLSV1 traffic using private key of the server"
description = '''SSL debug log is as follows, any tips would be appreciated I&#x27;ve set up preferences in WireShark to any,443,http,&amp;lt;path to=&quot;&quot; my=&quot;&quot; .p12=&quot;&quot;&amp;gt;,&amp;lt;password&amp;gt; Wireshark SSL debug log  ssl_association_remove removing TCP 443 - http handle 0000000006CC94D0 5368 bytes read PKCS#12 imported Bag 0/0: ...'''
date = "2015-08-18T16:10:00Z"
lastmod = "2015-08-19T02:13:00Z"
weight = 45220
keywords = [ "ssl", "tlsv1" ]
aliases = [ "/questions/45220" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Having trouble decrypting TLSV1 traffic using private key of the server](/questions/45220/having-trouble-decrypting-tlsv1-traffic-using-private-key-of-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45220-score" class="post-score" title="current number of votes">0</div><span id="post-45220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>SSL debug log is as follows, any tips would be appreciated</p><p>I've set up preferences in WireShark to any,443,http,&lt;path to="" my="" .p12=""&gt;,&lt;password&gt;</p><pre><code>Wireshark SSL debug log

ssl_association_remove removing TCP 443 - http handle 0000000006CC94D0
5368 bytes read
PKCS#12 imported
Bag 0/0: PKCS#8 Encrypted key
Private key imported: KeyID 4c:19:79:46:f4:87:65:4c:bf:69:09:06:58:42:b1:39:...
ssl_load_key: swapping p and q parameters and recomputing u
Bag 1/0: Encrypted
Bag 1/0 decrypted: Certificate
Certificate imported: test.yyy.net &lt;&lt;error&gt;&gt;, KeyID 4c197946f487654cbf6909065842b139570f106c
Bag 1/1: Certificate
Certificate imported: Go Daddy Root Certificate Authority - G2 &lt; &lt; ERROR &gt; &gt;, KeyID 210f2c89f7c4cd5d1b825e38d6c6593ba69375ae
Bag 1/2: Certificate
Certificate imported: Go Daddy Secure Certificate Authority - G2 &lt; &lt; ERROR &gt; &gt;, KeyID b455501483451fee8ca0a10cf5afde3a4c5e1159
ssl_init IPv4 addr &#39;any&#39; (0.0.0.0) port &#39;443&#39; filename &#39;C:\Users\yyy\Documents\yyy.p12&#39; password(only for p12 file) &#39;yyy&#39;
ssl_init private key file C:\Users\yyy\Documents\yyy.p12 successfully loaded.
association_add TCP port 443 protocol http handle 0000000006CC94D0
5368 bytes read
PKCS#12 imported
Bag 0/0: PKCS#8 Encrypted key
Private key imported: KeyID 4c:19:79:46:f4:87:65:4c:bf:69:09:06:58:42:b1:39:...
ssl_load_key: swapping p and q parameters and recomputing u
Bag 1/0: Encrypted
Bag 1/0 decrypted: Certificate
Certificate imported: test.yyy.net &lt;&lt;error&gt;&gt;, KeyID 4c197946f487654cbf6909065842b139570f106c
Bag 1/1: Certificate
Certificate imported: Go Daddy Root Certificate Authority - G2 &lt; &lt; ERROR &gt; &gt;, KeyID 210f2c89f7c4cd5d1b825e38d6c6593ba69375ae
Bag 1/2: Certificate
Certificate imported: Go Daddy Secure Certificate Authority - G2 &lt; &lt; ERROR &gt; &gt;, KeyID b455501483451fee8ca0a10cf5afde3a4c5e1159
ssl_init IPv6 addr &#39;any&#39; (::) port &#39;443&#39; filename &#39;C:\Users\yyy\Documents\yyy.p12&#39; password(only for p12 file) &#39;yyy&#39;
ssl_init private key file C:\Users\yyy\Documents\yyy.p12 successfully loaded.
association_add TCP port 443 protocol http handle 0000000006CC94D0

dissect_ssl enter frame #18 (first time)
ssl_session_init: initializing ptr 000000000B1A1D50 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #21 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 3979
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 3974, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 3979 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 3979 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 3979 
dissect_ssl3_handshake iteration 0 type 14 offset 3975 length 0 bytes, remaining 3979 

dissect_ssl enter frame #25 (first time)
ssl_session_init: initializing ptr 000000000B1A2A80 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41798, ssl_session = 000000000B1A2A80
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #28 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41798, ssl_session = 000000000B1A2A80
  record: offset = 0, reported_length_remaining = 3979
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 3974, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 3979 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 3979 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 3979 
dissect_ssl3_handshake iteration 0 type 14 offset 3975 length 0 bytes, remaining 3979 

dissect_ssl enter frame #32 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #33 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41798, ssl_session = 000000000B1A2A80
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #34 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41798, ssl_session = 000000000B1A2A80
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 196 offset 5 length 10367117 bytes, remaining 53 

dissect_ssl enter frame #35 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 236 offset 5 length 2045894 bytes, remaining 53 

dissect_ssl enter frame #36 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41798, ssl_session = 000000000B1A2A80
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 144, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #37 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 165
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 160, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #39 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #40 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 165
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 160, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #45 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #46 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 165
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 160, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #50 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #51 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 1173
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1168, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #54 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41798, ssl_session = 000000000B1A2A80
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #56 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B41618, ssl_session = 000000000B1A1D50
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #69 (first time)
ssl_session_init: initializing ptr 000000000B1A51E0 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #72 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #74 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #75 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 88 offset 5 length 10535436 bytes, remaining 53 

dissect_ssl enter frame #78 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 341
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 336, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #79 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #80 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 64, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #83 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #84 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 405
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 400, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #85 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #86 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 64, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #91 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #92 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #93 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 1813
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1808, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #94 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #95 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42198, ssl_session = 000000000B1A51E0
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 64, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #105 (first time)
ssl_session_init: initializing ptr 000000000B1A7730 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #108 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #111 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #112 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 165 offset 5 length 14038478 bytes, remaining 53 

dissect_ssl enter frame #115 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 288, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #116 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #117 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #119 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 000000000B1A7730
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #108 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #111 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #112 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 165 offset 5 length 14038478 bytes, remaining 53 

dissect_ssl enter frame #115 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #116 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #117 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #119 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B427B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #124 (first time)
ssl_session_init: initializing ptr 000000000B1A9070 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #125 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #126 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 250 offset 5 length 5359313 bytes, remaining 53 

dissect_ssl enter frame #128 (first time)
ssl_session_init: initializing ptr 000000000B1A9860 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #129 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #130 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 229 offset 5 length 1973127 bytes, remaining 53 

dissect_ssl enter frame #134 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 464, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #139 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #140 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 229
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 224, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #142 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #143 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #128 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 

dissect_ssl enter frame #129 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #130 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 229 offset 5 length 1973127 bytes, remaining 53 

dissect_ssl enter frame #134 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 469
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #139 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #140 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 229
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #142 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #150 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 9029
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9024, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #150 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 1051
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0
  record: offset = 37, reported_length_remaining = 1014
  need_desegmentation: offset = 37, reported_length_remaining = 1014

dissect_ssl enter frame #153 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 4293
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4288, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #150 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 9029
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #150 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1051
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0
  record: offset = 37, reported_length_remaining = 1014
  need_desegmentation: offset = 37, reported_length_remaining = 1014

dissect_ssl enter frame #153 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4293
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #160 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 128, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #165 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #166 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #167 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #168 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 197
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 192, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #169 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #170 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #171 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #173 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #174 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42B88, ssl_session = 000000000B1A9860
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #179 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #181 (first time)
ssl_session_init: initializing ptr 000000000B1AD270 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #184 (first time)
ssl_session_init: initializing ptr 000000000B1ADAE0 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #187 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #188 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #191 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #192 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 190 offset 5 length 13426308 bytes, remaining 53 

dissect_ssl enter frame #195 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #196 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 50 offset 5 length 7649018 bytes, remaining 53 

dissect_ssl enter frame #197 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 800, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #198 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #199 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #200 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 277
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 272, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #201 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #202 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #203 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #204 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #207 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #187 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #188 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #191 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #192 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 190 offset 5 length 13426308 bytes, remaining 53 

dissect_ssl enter frame #195 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #196 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 50 offset 5 length 7649018 bytes, remaining 53 

dissect_ssl enter frame #197 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #198 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #199 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #200 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 277
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #201 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #202 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #203 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #204 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #207 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #210 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #211 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #214 (first time)
ssl_session_init: initializing ptr 000000000B1B02E0 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #217 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #220 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #221 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 54 offset 5 length 4234981 bytes, remaining 53 

dissect_ssl enter frame #222 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #224 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 853
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 848, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #225 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #226 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #227 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #210 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #211 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #217 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #220 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #221 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 54 offset 5 length 4234981 bytes, remaining 53 

dissect_ssl enter frame #222 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #224 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 853
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #225 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #226 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #227 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #233 (first time)
ssl_session_init: initializing ptr 000000000B1B1DD0 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #237 (first time)
ssl_session_init: initializing ptr 000000000B1B2640 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #240 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B43988, ssl_session = 000000000B1AD270
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #241 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #242 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B438B8, ssl_session = 000000000B1ADAE0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #243 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #246 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #247 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 108 offset 5 length 6234692 bytes, remaining 53 

dissect_ssl enter frame #248 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #251 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #252 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 177 offset 5 length 5650390 bytes, remaining 53 

dissect_ssl enter frame #253 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 277
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 272, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #254 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #255 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #256 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 288, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #257 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #258 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #259 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 000000000B1B1DD0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #261 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 000000000B1B2640
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #266 (first time)
ssl_session_init: initializing ptr 000000000B1B4E40 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 000000000B1B4E40
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #267 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 000000000B1B4E40
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #268 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 000000000B1B4E40
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 184 offset 5 length 6287901 bytes, remaining 53 

dissect_ssl enter frame #271 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 000000000B1B4E40
  record: offset = 0, reported_length_remaining = 965
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 960, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #275 (first time)
ssl_session_init: initializing ptr 000000000B1B5CA0 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #255 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #256 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #257 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #258 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #259 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44A50, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #261 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44B20, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #266 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 

dissect_ssl enter frame #267 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #268 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 184 offset 5 length 6287901 bytes, remaining 53 

dissect_ssl enter frame #271 (already visited)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45010, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 965
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #279 (first time)
ssl_session_init: initializing ptr 000000000B1B6510 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #280 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #281 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 96 offset 5 length 6505200 bytes, remaining 53 

dissect_ssl enter frame #282 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 4303
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4298, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 4303 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 3554 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 12 offset 3644 length 327 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 13 offset 3975 length 320 bytes, remaining 4303 
dissect_ssl3_handshake iteration 0 type 14 offset 4299 length 0 bytes, remaining 4303 

dissect_ssl enter frame #285 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 293
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 288, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #286 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #287 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #289 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B452A0, ssl_session = 000000000B1B6510
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #293 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B44430, ssl_session = 000000000B1B02E0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #294 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #297 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 212 offset 5 length 2789173 bytes, remaining 53 

dissect_ssl enter frame #300 (first time)
ssl_session_init: initializing ptr 000000000B1B7F80 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B459C8, ssl_session = 000000000B1B7F80
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #301 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B459C8, ssl_session = 000000000B1B7F80
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #302 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B459C8, ssl_session = 000000000B1B7F80
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 160 offset 5 length 14036976 bytes, remaining 53 

dissect_ssl enter frame #303 (first time)
ssl_session_init: initializing ptr 000000000B1B8770 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 86
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x10
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #304 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #305 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 93 offset 5 length 8850048 bytes, remaining 53 

dissect_ssl enter frame #307 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 421
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 416, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #308 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #309 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #314 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 277
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 272, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #315 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B451D0, ssl_session = 000000000B1B5CA0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #319 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B42AB8, ssl_session = 000000000B1A9070
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #320 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #321 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 341
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 336, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #322 (first time)
ssl_session_init: initializing ptr 000000000B1B9F80 size 712
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45CA8, ssl_session = 000000000B1B9F80
  record: offset = 0, reported_length_remaining = 1260
  need_desegmentation: offset = 0, reported_length_remaining = 1260

dissect_ssl enter frame #325 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #326 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 117
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 112, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0

dissect_ssl enter frame #327 (first time)
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
  conversation = 0000000007B45A98, ssl_session = 000000000B1B8770
  record: offset = 0, reported_length_remaining = 356
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0
  record: offset = 37, reported_length_remaining = 319
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 192, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0
  record: offset = 234, reported_length_remaining = 122
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0
  record: offset = 271, reported_length_remaining = 85
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 80, ssl state 0x16
association_find: TCP port 443 found 00000000070F70E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 00000000070F70E0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/c414ed501efda8e470d80bbf7c36fe5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gberesnev&#39;s gravatar image" /><p><span>gberesnev</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gberesnev has no accepted answers">0%</span></p></div></div><div id="comments-container-45220" class="comments-container"></div><div id="comment-tools-45220" class="comment-tools"></div><div class="clear"></div><div id="comment-45220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45231"></span>

<div id="answer-container-45231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45231-score" class="post-score" title="current number of votes">2</div><span id="post-45231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is an important message from your logs:</p><pre><code>dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)</code></pre><p>0x16 means that you are missing the Client Random bytes and (pre-)master secret and therefore cannot establish the session key.</p><p><em>Problem 1:</em> In all <code>packet_from_server: is from server -</code> cases, the result is <code>TRUE</code> meaning that your capture does not contain any data from a SSL client. This would explain the missing Client Random which is <a href="https://tools.ietf.org/html/rfc5246.html#section-8.1">required</a> for obtaining the master secret given a pre-master secret.</p><p><em>Problem 2:</em> Note that cipher is 0xC013 which is ECDHE-RSA-AES128-SHA. This is an DHE cipher suite so you cannot use a RSA private key to decrypt an non-existing encrypted RSA pre-master secret that would appear in a ClientKeyExchange handshake message. Use <a href="https://security.stackexchange.com/a/42350/2630">SSL keylog files</a> instead or force weaker, non-DHE ciphers for testing.</p><p><em>Problem 3:</em> the message does not contain a Certificate handshake message and looks like an <a href="https://tools.ietf.org/html/rfc5246.html#page-37">abbreviated handshake</a>. This means that even if a RSA cipher suite is in use, the encrypted pre-master secret is still not sent over the wire and you still cannot decrypt the traffic unless you have an earlier decrypted session (with the same session identifier) in the same capture (given the RSA private key).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '15, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-45231" class="comments-container"></div><div id="comment-tools-45231" class="comment-tools"></div><div class="clear"></div><div id="comment-45231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

