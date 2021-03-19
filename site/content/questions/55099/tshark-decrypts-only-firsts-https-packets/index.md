+++
type = "question"
title = "Tshark decrypts only firsts https packets"
description = '''Hi everyone, I have an issue with tshark. It decrypts only firsts https request then stop to decrypt https traffic. Any idea? The debug file content: dissect_ssl enter frame #302 (first time) packet_from_server: is from server - FALSE  conversation = 0x1f8dda0, ssl_session = 0x1f8e5c0  record: offse...'''
date = "2016-08-24T13:35:00Z"
lastmod = "2016-08-26T09:42:00Z"
weight = 55099
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/55099" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark decrypts only firsts https packets](/questions/55099/tshark-decrypts-only-firsts-https-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55099-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I have an issue with tshark. It decrypts only firsts https request then stop to decrypt https traffic.</p><p>Any idea?</p><p>The debug file content:</p><pre><code>dissect_ssl enter frame #302 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1f8dda0, ssl_session = 0x1f8e5c0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 48, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl enter frame #313 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1f88f40, ssl_session = 0x1f89760
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 48, ssl state 0x6BF
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 02 e9 42 6a 0f 83 15 a5 1f de 64 b0 c4 91 a7 94 |..Bj......d.....|
| 6e 4e d3 dd 6b f7 85 13 43 90 c5 c4 97 0d 1f 73 |nN..k...C......s|
| d0 d4 87 32 37 1e 04 2a 50 fc 5e d0 7f 6a 08 a0 |...27..*P.^..j..|
Plaintext[32]:
| 01 00 f7 43 17 7d 18 86 00 43 07 84 d2 be 6c e5 |...C.}...C....l.|
| 3c 10 26 bb 21 a7 09 09 09 09 09 09 09 09 09 09 |&lt;.&amp;.!...........|
ssl_decrypt_record found padding 9 final len 22
checking mac (len 2, version 303, ct 21 seq 5)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| f7 43 17 7d 18 86 00 43 07 84 d2 be 6c e5 3c 10 |.C.}...C....l.&lt;.|
| 26 bb 21 a7                                     |&amp;.!.            |
ssl_decrypt_record: mac ok
dissect_ssl enter frame #457 (first time)
association_find: TCP port 58491 found (nil)
packet_from_server: is from server - FALSE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 512
decrypt_ssl3_record: app_data len 512, ssl state 0x00
association_find: TCP port 58491 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 508 bytes, remaining 517
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01
dissect_ssl enter frame #459 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 161
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x91
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 81
decrypt_ssl3_record: app_data len 81, ssl state 0x91
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x93
ssl_dissect_hnd_srv_hello found CIPHER 0x002F TLS_RSA_WITH_AES_128_CBC_SHA -&gt; state 0x97
  record: offset = 86, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Session resumption using Session Ticket
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x97
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 97 64
decrypt_ssl3_record: app_data len 64, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 21 offset 97 length 15483064 bytes, remaining 161
dissect_ssl enter frame #461 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x97
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 69
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 64
decrypt_ssl3_record: app_data len 64, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 246 offset 11 length 14460938 bytes, remaining 75
dissect_ssl enter frame #462 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 528, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 58491 found (nil)
association_find: TCP port 443 found 0x1f548a0
dissect_ssl enter frame #464 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 2896
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 448, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 453, reported_length_remaining = 2443
  need_desegmentation: offset = 453, reported_length_remaining = 2443
dissect_ssl enter frame #465 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 4421
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4416, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl enter frame #469 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 757
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 752, ssl state 0x97
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl enter frame #470 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x1fabd80, ssl_session = 0x1facc30
  record: offset = 0, reported_length_remaining = 1610
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 448, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 453, reported_length_remaining = 1157
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1152, ssl state 0x97
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre></div><div id="question-tags" class="tags-container tags">ssl decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/119e08a239cdc806297bb34eb03cdb7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mickael_R&#39;s gravatar image" /><p>Mickael_R<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mickael_R has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '16, 14:11</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-55099" class="comments-container"></div><div id="comment-tools-55099" class="comment-tools"></div><div class="clear"></div><div id="comment-55099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55127"></span>

<div id="answer-container-55127" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55127-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you have unsufficient key material or packets turned out-of-order.</p><pre><code>dissect_ssl enter frame #313 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x1f88f40, ssl_session = 0x1f89760</code></pre><p>See this conversation (and <code>ssl_session</code>) identifier? It is different from the other ones below.</p><pre><code>  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 48, ssl state 0x6BF
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 02 e9 42 6a 0f 83 15 a5 1f de 64 b0 c4 91 a7 94 |..Bj......d.....|
| 6e 4e d3 dd 6b f7 85 13 43 90 c5 c4 97 0d 1f 73 |nN..k...C......s|
| d0 d4 87 32 37 1e 04 2a 50 fc 5e d0 7f 6a 08 a0 |...27..*P.^..j..|
Plaintext[32]:
| 01 00 f7 43 17 7d 18 86 00 43 07 84 d2 be 6c e5 |...C.}...C....l.|
| 3c 10 26 bb 21 a7 09 09 09 09 09 09 09 09 09 09 |&lt;.&amp;.!...........|
ssl_decrypt_record found padding 9 final len 22
checking mac (len 2, version 303, ct 21 seq 5)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| f7 43 17 7d 18 86 00 43 07 84 d2 be 6c e5 3c 10 |.C.}...C....l.&lt;.|
| 26 bb 21 a7                                     |&amp;.!.            |
ssl_decrypt_record: mac ok

dissect_ssl enter frame #457 (first time)
association_find: TCP port 58491 found (nil)
packet_from_server: is from server - FALSE
  conversation = 0x1fabd80, ssl_session = 0x1facc30</code></pre><p>See? It is different. So unless you managed to get keys for this session and captured the full unabbreviated handshake, you will not be able to decrypt it.</p><pre><code>  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 22 Handshake</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '16, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-55127" class="comments-container"><span id="55129"></span><div id="comment-55129" class="comment"><div id="post-55129-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks, I'm gonna check what's wrong and what my ssl_session ID changed</p></div><div id="comment-55129-info" class="comment-info"><span class="comment-age">(26 Aug '16, 11:44)</span> Mickael_R</div></div><span id="55131"></span><div id="comment-55131" class="comment"><div id="post-55131-score" class="comment-score"></div><div class="comment-text"><p>The internal <code>conversation</code> and <code>ssl_session</code> change for each TCP connection. Perhaps you have only partially captured the SSL session (TCP connection).</p></div><div id="comment-55131-info" class="comment-info"><span class="comment-age">(26 Aug '16, 12:17)</span> Lekensteyn</div></div></div><div id="comment-tools-55127" class="comment-tools"></div><div class="clear"></div><div id="comment-55127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

