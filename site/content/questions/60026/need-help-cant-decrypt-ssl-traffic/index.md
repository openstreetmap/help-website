+++
type = "question"
title = "Need help: Can&#x27;t decrypt SSL traffic"
description = '''Hi there! I&#x27;m unable to decrypt some SSL Traffic. Here is the debug log: Wireshark SSL debug log Wireshark version: 2.2.5 (v2.2.5-0-g440fd4d) GnuTLS version: 3.2.15 Libgcrypt version: 1.6.2  dissect_ssl enter frame #4 (first time) packet_from_server: is from server - FALSE  conversation = 000001C940...'''
date = "2017-03-13T04:11:00Z"
lastmod = "2017-03-13T04:51:00Z"
weight = 60026
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/60026" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help: Can't decrypt SSL traffic](/questions/60026/need-help-cant-decrypt-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60026-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there!</p><p>I'm unable to decrypt some SSL Traffic. Here is the debug log:</p><p>Wireshark SSL debug log</p><pre><code>Wireshark version: 2.2.5 (v2.2.5-0-g440fd4d)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

dissect_ssl enter frame #4 (first time)
packet_from_server: is from server - FALSE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 169
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 164
decrypt_ssl3_record: app_data len 164, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 160 bytes, remaining 169 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 1460
ssl_try_set_version found version 0x0303 -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 85
decrypt_ssl3_record: app_data len 85, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 90 
ssl_try_set_version found version 0x0303 -&gt; state 0x91
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x003D TLS_RSA_WITH_AES_256_CBC_SHA256 -&gt; state 0x97
  record: offset = 90, reported_length_remaining = 1370
  need_desegmentation: offset = 90, reported_length_remaining = 1370

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 3324
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 3319
decrypt_ssl3_record: app_data len 3319, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3315 bytes, remaining 3324 
lookup(KeyID)[20]:
| 02 ff 3a e6 1a ba e6 78 d1 25 d9 16 ff ef de 7c |..:....x.%.....||
| f2 45 e2 3f                                     |.E.?            |
ssl_find_private_key_by_pubkey: lookup result: 0000000000000000

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4
decrypt_ssl3_record: app_data len 4, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #11 (first time)
packet_from_server: is from server - FALSE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 358
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 262
decrypt_ssl3_record: app_data len 262, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 297
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 91
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 278 80
decrypt_ssl3_record: app_data len 80, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 58 offset 278 length 5738267 bytes, remaining 358

dissect_ssl enter frame #13 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x297
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 80
decrypt_ssl3_record: app_data len 80, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 100 offset 5 length 8965755 bytes, remaining 85

dissect_ssl enter frame #17 (first time)
packet_from_server: is from server - FALSE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 325
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 320, ssl state 0x297
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 354
  need_desegmentation: offset = 0, reported_length_remaining = 354

dissect_ssl enter frame #20 (first time)
packet_from_server: is from server - TRUE
  conversation = 000001C940D36700, ssl_session = 000001C940D370D0
  record: offset = 0, reported_length_remaining = 1525
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1520, ssl state 0x297
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre></div><div id="question-tags" class="tags-container tags">ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '17, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/6dad0b84bda433d9abd3f57c3df67dd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pu7A&#39;s gravatar image" /><p>Pu7A<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pu7A has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '17, 04:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60026" class="comments-container"></div><div id="comment-tools-60026" class="comment-tools"></div><div class="clear"></div><div id="comment-60026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60027"></span>

<div id="answer-container-60027" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60027-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seemed to be some sort of error loading the key file. After closing Wireshark and reopening, it worked.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/6dad0b84bda433d9abd3f57c3df67dd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pu7A&#39;s gravatar image" /><p>Pu7A<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pu7A has no accepted answers">0%</span></p></div></div><div id="comments-container-60027" class="comments-container"></div><div id="comment-tools-60027" class="comment-tools"></div><div class="clear"></div><div id="comment-60027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

