+++
type = "question"
title = "TLS &quot;half&quot; decryption problem"
description = '''Hi everyone. I&#x27;m decrypting MMS traffic with TLS between a client and a server, giving Wireshark the server private key, and everthing works fine, I can see the plain MMS messages. In some cases the TLS handshake has some trouble with TCP retransmissions, reassembled PDU etc. In these cases can happ...'''
date = "2015-07-02T07:02:00Z"
lastmod = "2015-07-14T05:46:00Z"
weight = 43815
keywords = [ "tls", "ssl", "decryption" ]
aliases = [ "/questions/43815" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLS "half" decryption problem](/questions/43815/tls-half-decryption-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43815-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone.</p><p>I'm decrypting MMS traffic with TLS between a client and a server, giving Wireshark the server private key, and everthing works fine, I can see the plain MMS messages.</p><p>In some cases the TLS handshake has some trouble with TCP retransmissions, reassembled PDU etc. In these cases can happen that wireshark is able only to decrypt half of the communication, the traffic from server to client.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screen1.png" alt="alt text" /></p><p>As you can see in the image the MMS traffic from the client is decrypted "Application Data".</p><p>My questions are: Does exist some wireshark setting to resolve this problem? If wireshark can calculate the master key (server side) and use it to decrypt the server traffic, shouldn't be able to decrypt also the client one with the same key?</p><p><strong>UPDATE 1</strong></p><p>I don't know, but maybe it's useful to show more info about frame 82 and 87:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/frame_83.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/frame_87.png" alt="alt text" /></p><p>Frame 87 is the TLS Finished message from Client to Server, and it's decrypted, but the next TLS messages from Client to Server, in frame 94, are encrypted!</p><p><strong>UPDATE 2</strong></p><p>Maybe the problem in in the trace capture phase: for info, I get the pcap traces using default parameters with Wireshark 1.12.3 on Windows 7 (Client Side) and with tcpdump on Centos 6 (server side). Both capture sides show the same problem I'm trying to solve.</p><p><strong>UPDATE 3</strong></p><p>I provide another tarce with the same issue + the ssl debug log. I want to point out that the Change Cipher Spec message from the client is received but not present in the ssl debug log (frame 57)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screen_2_lzgv3aL.png" alt="alt text" /></p><pre><code>dissect_ssl enter frame #51 (first time)
ssl_session_init: initializing ptr 0000000008A50780 size 712
association_find: TCP port 54799 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 335
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 330, ssl state 0x00
association_find: TCP port 54799 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 326 bytes, remaining 335 
packet_from_server: is from server - FALSE
ssl_find_private_key server IPSERVER:3782
ssl_find_private_key: testing 4 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #53 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 1424
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 86, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 82 bytes, remaining 91 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x009D -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 91, reported_length_remaining = 1333
  need_desegmentation: offset = 91, reported_length_remaining = 1333

dissect_ssl enter frame #54 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 2149
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2144, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2140 bytes, remaining 2149

dissect_ssl enter frame #54 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 46, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 5 length 38 bytes, remaining 51 
dissect_ssl3_handshake iteration 0 type 14 offset 47 length 0 bytes, remaining 51

dissect_ssl enter frame #57 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 259

dissect_ssl enter frame #59 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 1424
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1091, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 1087 bytes, remaining 1096 
  record: offset = 1096, reported_length_remaining = 328
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 1101 length 258 bytes, remaining 1363 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
pre master encrypted[256]:
...
ssl_decrypt_pre_master_secret:RSA_private_decrypt
decrypted_unstrip_pre_master[255]:
...
pcry_private_decrypt: stripping 207 bytes, decr_len 255
pre master secret[48]:
...
ssl_generate_keyring_material:PRF(pre_master_secret)
pre master secret[48]:
...
client random[32]:
...
server random[32]:
...
tls12_prf: tls_hash(hash_alg SHA384 secret_len 48 seed_len 77 )
tls_hash: hash secret[48]:
...
tls_hash: hash seed[77]:
...
hash out[48]:
...
PRF out[48]:
...
master secret[48]:
...
ssl_generate_keyring_material sess key generation
tls12_prf: tls_hash(hash_alg SHA384 secret_len 48 seed_len 77 )
tls_hash: hash secret[48]:
...
tls_hash: hash seed[77]:
...
hash out[168]:
...
PRF out[168]:
...
key expansion[168]:
...
Client Write key[32]:
...
Server Write key[32]:
...
Client Write IV[4]:
...
Server Write IV[4]:
...
ssl_generate_keyring_material ssl_create_decoder(client)
ssl_create_decoder CIPHER: AES256
decoder initialized (digest len 48)
ssl_generate_keyring_material ssl_create_decoder(server)
ssl_create_decoder CIPHER: AES256
decoder initialized (digest len 48)
ssl_generate_keyring_material: client seq 0, server seq 0
ssl_save_session stored session id[32]:
...
ssl_save_session stored master secret[48]:
...
dissect_ssl3_handshake session keys successfully generated
  record: offset = 1363, reported_length_remaining = 61
  need_desegmentation: offset = 1363, reported_length_remaining = 61

dissect_ssl enter frame #61 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 40
Ciphertext[40]:
...
Plaintext[32]:
...
dissect_ssl3_handshake iteration 1 type 20 offset 0 length 12 bytes, remaining 16

dissect_ssl enter frame #62 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 46, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 54799 found 0000000000000000
association_find: TCP port 3782 found 0000000004FCE830

dissect_ssl enter frame #63 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 46, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 46
Ciphertext[46]:
...
Plaintext[38]:
...
ssl_add_data_info: new data inserted data_len = 22, seq = 0, nxtseq = 22
association_find: TCP port 3782 found 0000000004FCE830
dissect_ssl3_record decrypted len 22
decrypted app data fragment[22]:
...
dissect_ssl3_record found association 0000000004FCE830

dissect_ssl enter frame #64 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 239
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 234, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 54799 found 0000000000000000
association_find: TCP port 3782 found 0000000004FCE830

dissect_ssl enter frame #65 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 176
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 171, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 171
Ciphertext[171]:
...
ssl_decrypt_record: allocating 203 bytes for decrypt data (old len 72)
Plaintext[163]:
...
ssl_add_data_info: new data inserted data_len = 147, seq = 22, nxtseq = 169
association_find: TCP port 3782 found 0000000004FCE830
dissect_ssl3_record decrypted len 147
decrypted app data fragment[147]:
...
dissect_ssl3_record found association 0000000004FCE830

dissect_ssl enter frame #66 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 65
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 60, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 54799 found 0000000000000000
association_find: TCP port 3782 found 0000000004FCE830

dissect_ssl enter frame #67 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005A815F8, ssl_session = 0000000008A50780
  record: offset = 0, reported_length_remaining = 115
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 110, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 110
Ciphertext[110]:
...
Plaintext[102]:
...
ssl_add_data_info: new data inserted data_len = 86, seq = 169, nxtseq = 255
association_find: TCP port 3782 found 0000000004FCE830
dissect_ssl3_record decrypted len 86
decrypted app data fragment[86]:
...
dissect_ssl3_record found association 0000000004FCE830</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags">tls ssl decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/eca830854093757dbe9847c9d44241b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theo66&#39;s gravatar image" /><p>theo66<br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theo66 has one accepted answer">50%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '15, 01:50</p></div></div><div id="comments-container-43815" class="comments-container"><span id="43821"></span><div id="comment-43821" class="comment"><div id="post-43821-score" class="comment-score"></div><div class="comment-text"><p>Do you have the TCP Protocol preference setting "Do not call subdissectors for error packets" checked?</p></div><div id="comment-43821-info" class="comment-info"><span class="comment-age">(02 Jul '15, 08:46)</span> grahamb ♦</div></div><span id="43839"></span><div id="comment-43839" class="comment"><div id="post-43839-score" class="comment-score"></div><div class="comment-text"><p>No I don't. By checking that setting all the trace remains encrypted.</p></div><div id="comment-43839-info" class="comment-info"><span class="comment-age">(03 Jul '15, 01:10)</span> theo66</div></div><span id="43904"></span><div id="comment-43904" class="comment"><div id="post-43904-score" class="comment-score"></div><div class="comment-text"><p>Out-of-order packets confused the SSL dissectors in the past, perhaps that is the case here. Could you generate a SSL debug log? You can enable this via Preferences -&gt; Protocols -&gt; SSL.</p></div><div id="comment-43904-info" class="comment-info"><span class="comment-age">(06 Jul '15, 14:26)</span> Lekensteyn</div></div><span id="43934"></span><div id="comment-43934" class="comment"><div id="post-43934-score" class="comment-score"></div><div class="comment-text"><p>I get the debug log from another trace with the same issue. I show yout these 2 packet as example: the first from the client, the second from the server. <code> dissect_ssl enter frame #66 (first time) packet_from_server: is from server - FALSE   conversation = 0000000005A815F8, ssl_session = 0000000008A50780   record: offset = 0, reported_length_remaining = 65 dissect_ssl3_record: content_type 23 Application Data decrypt_ssl3_record: app_data len 60, ssl state 0x3F packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 54799 found 0000000000000000 association_find: TCP port 3782 found 0000000004FCE830</code></p><p><code></code></p><p><code>dissect_ssl enter frame #67 (first time) packet_from_server: is from server - TRUE   conversation = 0000000005A815F8, ssl_session = 0000000008A50780   record: offset = 0, reported_length_remaining = 115 dissect_ssl3_record: content_type 23 Application Data decrypt_ssl3_record: app_data len 110, ssl state 0x3F packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder ssl_decrypt_record ciphertext len 110 Ciphertext[110]: ... Plaintext[102]: ... ssl_add_data_info: new data inserted data_len = 86, seq = 169, nxtseq = 255 association_find: TCP port 3782 found 0000000004FCE830 dissect_ssl3_record decrypted len 86 decrypted app data fragment[86]: ... dissect_ssl3_record found association 0000000004FCE830</code></p><p>It seems that the client encoder is missing. As soon as possible I find a way to attach all the debug log.</p></div><div id="comment-43934-info" class="comment-info"><span class="comment-age">(07 Jul '15, 06:51)</span> theo66</div></div><span id="44011"></span><div id="comment-44011" class="comment"><div id="post-44011-score" class="comment-score"></div><div class="comment-text"><p>@theo66 Can you show more of the log? Specifically, I am looking for the part where the SSL state changes to 0x3F. Are unusual messages following that transition? Are the <code>tcp.stream</code> fields ("Stream number" under the TCP layer) the same for both streams? They should be the same, if not, then it could explain your issue.</p></div><div id="comment-44011-info" class="comment-info"><span class="comment-age">(09 Jul '15, 07:53)</span> Lekensteyn</div></div><span id="44096"></span><div id="comment-44096" class="comment not_top_scorer"><div id="post-44096-score" class="comment-score"></div><div class="comment-text"><p>@Lekensteyn I checked, tcp.stream is the same for both streams. I've updated the question with the ssl log.</p></div><div id="comment-44096-info" class="comment-info"><span class="comment-age">(13 Jul '15, 07:53)</span> theo66</div></div></div><div id="comment-tools-43815" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-43815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44132"></span>

<div id="answer-container-44132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44132-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like a bug in the SSL dissector of Wireshark.</p><p>In the debug log you provided (and also visible on the screenshot), there is no trace of a ChangeCipherSpec handshake message. This message is required, see the message flow in <a href="https://tools.ietf.org/html/rfc5246.html#page-36">RFC 5246</a>.</p><p>In your debug log, there is <code>ssl_change_cipher SERVER</code>, but no <code>ssl_change_cipher CLIENT</code> and thus the client decoder is never initialized. Frames 87 and 94 in the screenshot are incorrectly dissected (CertificateVerify and Finished are the expected dissections).</p><p>Are you using large client certificates? Based on your screenshot (and counting the SSL records size and comparing it with the TCP segment length), it looks like you encountered a known issue with SSL record fragmentation (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303">bug 3303</a>).</p><p>Another known issue is related to out-of-order packets (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9461">bug 9461</a>, <a href="https://ask.wireshark.org/questions/34945/decrypt-out-of-order-ssl-trace).">https://ask.wireshark.org/questions/34945/decrypt-out-of-order-ssl-trace).</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '15, 02:46</p></div></div><div id="comments-container-44132" class="comments-container"><span id="44165"></span><div id="comment-44165" class="comment"><div id="post-44165-score" class="comment-score"></div><div class="comment-text"><p>First of all, thank you for your support. The client certificate, like the server one, is approximately 1500 byte. I'm using 2048 bits RSA private keys.</p></div><div id="comment-44165-info" class="comment-info"><span class="comment-age">(15 Jul '15, 01:05)</span> theo66</div></div><span id="44191"></span><div id="comment-44191" class="comment"><div id="post-44191-score" class="comment-score"></div><div class="comment-text"><p>@theo66 Can you try to create a public capture file that reproduces this issue? If it is difficult to reproduce, can you share the packets from the TCP stream (at least packet 86 and 87)? (if you would like to keep it private, see my profile for contact details).</p></div><div id="comment-44191-info" class="comment-info"><span class="comment-age">(15 Jul '15, 14:20)</span> Lekensteyn</div></div><span id="44195"></span><div id="comment-44195" class="comment"><div id="post-44195-score" class="comment-score"></div><div class="comment-text"><p>@Lekensteyn I updated the question adding the screenshot of the trace which produces to the attached ssl debug log. I point out that the change cipher spec message from the client is received but ignored by the ssl dissector (frame 57). I have some difficulties to reproduce the issue now, if you need details about single frames/segments from the second trace (the one which I just added the screenshot) please tell me, but unfortunately I cannot share material containing certificate info and keys.</p></div><div id="comment-44195-info" class="comment-info"><span class="comment-age">(16 Jul '15, 01:57)</span> theo66</div></div><span id="44198"></span><div id="comment-44198" class="comment"><div id="post-44198-score" class="comment-score"></div><div class="comment-text"><p>@theo66 Updated the answer with some possible problems (handshake record fragmentation, out-of-order packets). If you do not mind recompiling, you can try the "quick 'n' dirty hack" at <a href="https://code.wireshark.org/review/5104">https://code.wireshark.org/review/5104</a> to workaround the first issue. For the second out-of-order issue, I can try to write a tool that reorders TCP packets.</p></div><div id="comment-44198-info" class="comment-info"><span class="comment-age">(16 Jul '15, 02:49)</span> Lekensteyn</div></div><span id="44200"></span><div id="comment-44200" class="comment"><div id="post-44200-score" class="comment-score"></div><div class="comment-text"><p>@Lekensteyn At a first glance it seems I have the same issue reported in the link you provide: <a href="https://ask.wireshark.org/questions/34945/decrypt-out-of-order-ssl-trace)">https://ask.wireshark.org/questions/34945/decrypt-out-of-order-ssl-trace)</a></p></div><div id="comment-44200-info" class="comment-info"><span class="comment-age">(16 Jul '15, 03:23)</span> theo66</div></div></div><div id="comment-tools-44132" class="comment-tools"></div><div class="clear"></div><div id="comment-44132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

