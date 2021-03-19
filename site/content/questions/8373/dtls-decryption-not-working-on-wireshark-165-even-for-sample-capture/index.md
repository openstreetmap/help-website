+++
type = "question"
title = "DTLS decryption not working on Wireshark 1.6.5, even for sample capture"
description = '''Hi everyone, Wireshark will not decrypt a DTLS capture, even when using the sample capture and private key provided in http://wiki.wireshark.org/DTLS (SampleCaptures/snakeoil.tgz). My log file is shown below. Any help is greatly appreciated! Private key imported: KeyID dd:29:74:15:7b:e6:76:47:f5:f0:...'''
date = "2012-01-13T09:20:00Z"
lastmod = "2012-04-13T14:11:00Z"
weight = 8373
keywords = [ "decryption", "dtls", "ssl" ]
aliases = [ "/questions/8373" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DTLS decryption not working on Wireshark 1.6.5, even for sample capture](/questions/8373/dtls-decryption-not-working-on-wireshark-165-even-for-sample-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8373-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>Wireshark will not decrypt a DTLS capture, even when using the sample capture and private key provided in http://wiki.wireshark.org/DTLS (SampleCaptures/snakeoil.tgz).</p><p>My log file is shown below. Any help is greatly appreciated!</p><pre><code>Private key imported: KeyID dd:29:74:15:7b:e6:76:47:f5:f0:68:3e:8a:55:61:62:...
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;4433&#39; filename &#39;c:\snakeoil-rsa.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file c:\snakeoil-rsa.key successfully loaded.
association_add UDP port 4433 protocol http handle 03F07738
ssl_session_init: initializing ptr 0511187C size 588
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls server 127.0.0.1:4433
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 106, ssl state 0
decrypt_dtls_record: no session key
dissect_dtls_hnd_hello_common found random state 1
association_find: UDP port 4433 found 05F92B20
packet_from_server: is from server - TRUE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 15, ssl state 11
decrypt_dtls_record: no session key
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 106, ssl state 11
decrypt_dtls_record: no session key
dissect_dtls_hnd_hello_common found random state 11
association_find: UDP port 4433 found 05F92B20
packet_from_server: is from server - TRUE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 82, ssl state 11
decrypt_dtls_record: no session key
dissect_dtls_hnd_hello_common found random state 13
dissect_dtls_hnd_srv_hello found cipher 35, state 17
dissect_dtls_hnd_srv_hello not enough data to generate key (required state 37)
association_find: UDP port 4433 found 05F92B20
packet_from_server: is from server - TRUE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 844, ssl state 17
decrypt_dtls_record: no session key
association_find: UDP port 4433 found 05F92B20
packet_from_server: is from server - TRUE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 12, ssl state 17
decrypt_dtls_record: no session key
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 140, ssl state 17
decrypt_dtls_record: no session key
dissect_dtls_handshake found SSL_HND_CLIENT_KEY_EXCHG, state 17
pre master encrypted[128]:
7c bc c8 94 6c 2e ef 41 70 73 86 76 93 49 e4 d0 
c4 68 d2 25 ef 1a 77 fa a3 cc 26 e4 af bf 33 b4 
6d a3 c4 1a f5 75 77 15 8a c2 01 50 3b bb f9 0b 
83 f5 38 cf ec a5 28 02 6b 72 b0 ac 91 1c 21 ed 
57 5e 5a b5 80 5b 31 fd 67 36 15 ca d5 e7 1b f6 
af 85 f6 67 f0 05 80 1c 26 d6 f7 78 39 8d 41 d6 
ed 68 46 bf 49 1d de a5 09 40 e9 29 72 ba 87 de 
a1 9c a3 59 ff c6 da 42 92 4c 47 a7 58 9d 0f 84 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: can&#39;t decrypt key:Invalid object
ssl_decrypt_pre_master_secret wrong pre_master_secret length (0, expected 48)
dissect_dtls_handshake can&#39;t decrypt pre master secret
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 20
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 64, ssl state 17
decrypt_dtls_record: no session key
association_find: UDP port 4433 found 05F92B20
packet_from_server: is from server - TRUE
dissect_dtls_record: content_type 20
association_find: UDP port 4433 found 05F92B20
packet_from_server: is from server - TRUE
dissect_dtls_record: content_type 22
decrypt_dtls_record: app_data len 64, ssl state 17
decrypt_dtls_record: no session key
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 23
decrypt_dtls_record: app_data len 48, ssl state 17
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
decrypt_dtls_record: using client decoder
decrypt_dtls_record: allocating 80 bytes for decrypt data (old len 32)
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
dissect_dtls_record: content_type 23
decrypt_dtls_record: app_data len 48, ssl state 17
association_find: UDP port 33192 found 00000000
packet_from_server: is from server - FALSE
decrypt_dtls_record: using client decoder
association_find: UDP port 33192</code></pre><p>Thanks,</p><p>Gene</p></div><div id="question-tags" class="tags-container tags">decryption dtls ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '12, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/22ba4aa0cedbc3ced41ef3a160a8625d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gene&#39;s gravatar image" /><p>gene<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gene has no accepted answers">0%</span></p></div></div><div id="comments-container-8373" class="comments-container"></div><div id="comment-tools-8373" class="comment-tools"></div><div class="clear"></div><div id="comment-8373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10141"></span>

<div id="answer-container-10141" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10141-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is working now (tested on Version 1.7.1-SVN-41356 (SVN Rev 41356 from /trunk)). Thanks to all involved for fixing this!</p><p>-Gene</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/22ba4aa0cedbc3ced41ef3a160a8625d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gene&#39;s gravatar image" /><p>gene<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gene has no accepted answers">0%</span></p></div></div><div id="comments-container-10141" class="comments-container"></div><div id="comment-tools-10141" class="comment-tools"></div><div class="clear"></div><div id="comment-10141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

