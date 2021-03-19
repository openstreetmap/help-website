+++
type = "question"
title = "Decrypting SSL/HTTPs (Mac Mail to Exchange 2010), have private key file, but cannot figure out."
description = '''Greetings. I am the administrator of an Exchange 2010 server which is using an SSL certificate that I created using a Windows Server CA. I&#x27;m troubleshooting an issue with Mac Mail disconnecting from the mail server every 2-3 minutes, and attempting to see what is going on by decrypting the conversat...'''
date = "2014-10-30T15:53:00Z"
lastmod = "2014-10-30T15:53:00Z"
weight = 37480
keywords = [ "exchange", "ssl_decrypt" ]
aliases = [ "/questions/37480" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting SSL/HTTPs (Mac Mail to Exchange 2010), have private key file, but cannot figure out.](/questions/37480/decrypting-sslhttps-mac-mail-to-exchange-2010-have-private-key-file-but-cannot-figure-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37480-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings.</p><p>I am the administrator of an Exchange 2010 server which is using an SSL certificate that I created using a Windows Server CA. I'm troubleshooting an issue with Mac Mail disconnecting from the mail server every 2-3 minutes, and attempting to see what is going on by decrypting the conversation between Mac Mail and the Exchange server. The communication appears to be happening only over the remote port 443 https, I believe Mac Mail is connecting to "Outlook Anywhere" or perhaps Exchange Web Services and hence only connecting to Port 443.</p><p>I exported the private key and certificate from the Exchange server which resulted in a .pfx file. On my macbook I then ran openssl to convert the .pfx file to a .pem file:</p><p>openssl pkcs12 -in privkey_careful.pfx -out privkey_careful.pem -nodes</p><p>The resulting file contained both the private key and a certificate as well as other metadata, so I deleted everything besides</p><pre><code>-----BEGIN PRIVATE KEY-----
.........key data
-----END PRIVATE KEY-----</code></pre><p>from the file.</p><p>I then opened my capture file created with wireshark on my macbook which captured the period of disconnection of the mail client to the Exchange server. In the wireshark preferences I went to Protocols-&gt;SSL and configured a new key, specifiying the IP address of the Exchange server, the port 443 (I also tried 0), and specified a debug file, and the private key file.</p><p>I click OK/apply and it looks like Wireshark is applying something to each packet, but I do not see any decrypted information anywhere. Browsing the captured packets looks the same as it did before.</p><p>partial SSL debug log file below. Any hints on what I might be doing wrong appreicate. Thank you.</p><p>Wireshark SSL debug log</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0x109234710
Private key imported: KeyID c5:31:c4:23:0c:6b:e5:df:8f:9b:dd:b4:97:22:1a:fc:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;27.112.87.163&#39; (27.112.87.163) port &#39;443&#39; filename &#39;/Users/123user/Downloads/privkey_careful.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /Users/123user/Downloads/privkey_careful.pem successfully loaded.
association_add TCP port 443 protocol http handle 0x109234710

dissect_ssl enter frame #523 (first time)
ssl_session_init: initializing ptr 0x10a6a7310 size 688
  conversation = 0x10a6a6fe8, ssl_session = 0x10a6a7310
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 38, ssl state 0x10
association_find: TCP port 63069 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63069 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #524 (first time)
ssl_session_init: initializing ptr 0x10a6a7a68 size 688
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #525 (first time)
ssl_session_init: initializing ptr 0x10a6a8158 size 688
  conversation = 0x10a6a7e30, ssl_session = 0x10a6a8158
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 38, ssl state 0x10
association_find: TCP port 63073 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63073 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #526 (first time)
ssl_session_init: initializing ptr 0x10a6a8848 size 688
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63057 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63057 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #531 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #533 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63057 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63057 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #536 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #537 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #540 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63057 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63057 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #541 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #542 (first time)
  conversation = 0x10a6a7e30, ssl_session = 0x10a6a8158
  record: offset = 0, reported_length_remaining = 283
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 278, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #543 (first time)
  conversation = 0x10a6a7e30, ssl_session = 0x10a6a8158
  record: offset = 0, reported_length_remaining = 287
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 282, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #546 (first time)
ssl_session_init: initializing ptr 0x10a6aaab8 size 688
  conversation = 0x10a6aa790, ssl_session = 0x10a6aaab8
  record: offset = 0, reported_length_remaining = 42
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 37, ssl state 0x10
association_find: TCP port 63072 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63072 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #548 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 80, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #551 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 186
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 144, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #553 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #558 (first time)
ssl_session_init: initializing ptr 0x10a6abfb8 size 688
  conversation = 0x10a6ab960, ssl_session = 0x10a6abfb8
  record: offset = 0, reported_length_remaining = 217
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 212, ssl state 0x00
association_find: TCP port 63087 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 208 bytes, remaining 217 
packet_from_server: is from server - FALSE
ssl_find_private_key server 54.200.14.109:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #562 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #564 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #566 (first time)
ssl_session_init: initializing ptr 0x10a6ad248 size 688
  conversation = 0x10a6acf20, ssl_session = 0x10a6ad248
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63067 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63067 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #567 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #570 (first time)
  conversation = 0x10a6a6fe8, ssl_session = 0x10a6a7310
  record: offset = 0, reported_length_remaining = 413
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 408, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #571 (first time)
ssl_session_init: initializing ptr 0x10a6adc10 size 688
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 169
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 164, ssl state 0x00
association_find: TCP port 63088 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 160 bytes, remaining 169 
packet_from_server: is from server - FALSE
ssl_find_private_key server 54.200.14.109:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #573 (first time)
  conversation = 0x10a6a6fe8, ssl_session = 0x10a6a7310
  record: offset = 0, reported_length_remaining = 288
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 283, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #575 (first time)
ssl_session_init: initializing ptr 0x10a6ae740 size 688
  conversation = 0x10a6ae418, ssl_session = 0x10a6ae740
  record: offset = 0, reported_length_remaining = 42
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 37, ssl state 0x10
association_find: TCP port 63074 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63074 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #577 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 1448
  need_desegmentation: offset = 0, reported_length_remaining = 1448

dissect_ssl enter frame #578 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 1770
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1765, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 1770 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 1676 bytes, remaining 1770 
dissect_ssl3_handshake iteration 0 type 14 offset 1766 length 0 bytes, remaining 1770 

dissect_ssl enter frame #581 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 267
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
trying to use SSL keylog in 
failed to open SSL keylog

dissect_ssl enter frame #582 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #583 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 219 offset 5 length 11403237 bytes, remaining 41 

dissect_ssl enter frame #587 (first time)
  conversation = 0x10a6acf20, ssl_session = 0x10a6ad248
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 63067 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63067 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #589 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #590 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
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
dissect_ssl3_handshake iteration 1 type 191 offset 11 length 13626809 bytes, remaining 47 

dissect_ssl enter frame #592 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 541
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 536, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63088 found 0x0
association_find: TCP port 443 found 0x10e637a70

dissect_ssl enter frame #593 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 1448
  need_desegmentation: offset = 0, reported_length_remaining = 1448

dissect_ssl enter frame #594 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 1638
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1633, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63088 found 0x0
association_find: TCP port 443 found 0x10e637a70

dissect_ssl enter frame #597 (first time)
  conversation = 0x10a6acf20, ssl_session = 0x10a6ad248
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #598 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #601 (first time)
ssl_session_init: initializing ptr 0x10a6b11f0 size 688
  conversation = 0x10a6b0ec8, ssl_session = 0x10a6b11f0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63064 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63064 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #602 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #604 (first time)
  conversation = 0x10a6ac4f0, ssl_session = 0x10a6adc10
  record: offset = 0, reported_length_remaining = 282
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 277, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x10e637a70

dissect_ssl enter frame #607 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 80, ssl state 0x10
association_find: TCP port 63057 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63057 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #609 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 186
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 144, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #611 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63057 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63057 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #612 (first time)
ssl_session_init: initializing ptr 0x10a6b26f0 size 688
  conversation = 0x10a6b23c8, ssl_session = 0x10a6b26f0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63063 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63063 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #615 (first time)
  conversation = 0x10a6b0ec8, ssl_session = 0x10a6b11f0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 63064 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63064 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #619 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 80, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #620 (first time)
ssl_session_init: initializing ptr 0x10a6b36b0 size 688
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 201
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 196, ssl state 0x00
association_find: TCP port 63089 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 192 bytes, remaining 201 
packet_from_server: is from server - FALSE
ssl_find_private_key server 54.200.14.109:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #622 (first time)
  conversation = 0x10a6b0ec8, ssl_session = 0x10a6b11f0
  record: offset = 0, reported_length_remaining = 138
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 101
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 96, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #625 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 186
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0
  record: offset = 37, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 144, ssl state 0x10
association_find: TCP port 993 found 0x10a275fb0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #662 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #671 (first time)
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
trying to use SSL keylog in 
failed to open SSL keylog
  cannot find master secret in keylog file either
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 86, reported_length_remaining = 47
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 206 offset 97 length 15021299 bytes, remaining 133 

dissect_ssl enter frame #673 (first time)
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #674 (first time)
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 41
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 219 offset 5 length 12240129 bytes, remaining 41 

dissect_ssl enter frame #675 (first time)
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 541
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 536, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63089 found 0x0
association_find: TCP port 443 found 0x10e637a70

dissect_ssl enter frame #676 (first time)
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 1448
  need_desegmentation: offset = 0, reported_length_remaining = 1448

dissect_ssl enter frame #677 (first time)
  conversation = 0x10a6b2ab8, ssl_session = 0x10a6b36b0
  record: offset = 0, reported_length_remaining = 1638
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1633, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63089 found 0x0
association_find: TCP port 443 found 0x10e637a70

dissect_ssl enter frame #681 (first time)
  conversation = 0x10a6a8520, ssl_session = 0x10a6a8848
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 63057 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63057 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #682 (first time)
  conversation = 0x10a6b23c8, ssl_session = 0x10a6b26f0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 63063 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63063 found 0x0
association_find: TCP port 993 found 0x10a275fb0

dissect_ssl enter frame #683 (first time)
  conversation = 0x10a6a7740, ssl_session = 0x10a6a7a68
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 63061 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 63061 found 0x0
association_find: TCP port 993 found 0x10a275fb0</code></pre></div><div id="question-tags" class="tags-container tags">exchange ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '14, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/0cfaf6cf7e832981ecffd003ba0d3135?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevinlong206&#39;s gravatar image" /><p>kevinlong206<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevinlong206 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Oct '14, 01:39</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-37480" class="comments-container"></div><div id="comment-tools-37480" class="comment-tools"></div><div class="clear"></div><div id="comment-37480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

