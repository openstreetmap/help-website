+++
type = "question"
title = "Decode TLS Traffic"
description = '''Trying to decode a TLS packet capture and it isn&#x27;t working. Can someone point me to what is going wrong. First part of ssl debug file is below. Wireshark SSL debug log  ssl_association_remove removing TCP 443 - http handle 0000000004650E80 Private key imported: KeyID 9e:a7:11:d1:92:19:ab:42:ba:4b:e0...'''
date = "2015-05-30T15:13:00Z"
lastmod = "2015-06-01T03:32:00Z"
weight = 42766
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/42766" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode TLS Traffic](/questions/42766/decode-tls-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42766-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to decode a TLS packet capture and it isn't working. Can someone point me to what is going wrong. First part of ssl debug file is below.</p><p>Wireshark SSL debug log</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0000000004650E80
Private key imported: KeyID 9e:a7:11:d1:92:19:ab:42:ba:4b:e0:44:aa:a2:f3:5c:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;10.1.16.129&#39; (10.1.16.129) port &#39;443&#39; filename &#39;C:\SoftwareLib\Putty\serverprivkey.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\SoftwareLib\Putty\serverprivkey.pem successfully loaded.
association_add TCP port 443 protocol http handle 0000000004650E80

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 00000000081C0720 size 712
association_find: TCP port 38423 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 216
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 211, ssl state 0x00
association_find: TCP port 38423 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 207 bytes, remaining 216 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.1.16.129:443
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 86
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
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #8 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 203 offset 5 length 8445086 bytes, remaining 37

dissect_ssl enter frame #12 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 76 offset 11 length 4320174 bytes, remaining 43

dissect_ssl enter frame #13 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 255
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 250, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 38423 found 0000000000000000
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 648
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 643, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 38423 found 0000000000000000
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 1263
  need_desegmentation: offset = 0, reported_length_remaining = 1263

dissect_ssl enter frame #25 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #25 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 1083
  need_desegmentation: offset = 0, reported_length_remaining = 1083

dissect_ssl enter frame #37 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #38 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 1263
  need_desegmentation: offset = 0, reported_length_remaining = 1263

dissect_ssl enter frame #49 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #49 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 1083
  need_desegmentation: offset = 0, reported_length_remaining = 1083

dissect_ssl enter frame #61 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #61 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 903
  need_desegmentation: offset = 0, reported_length_remaining = 903

dissect_ssl enter frame #73 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #73 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 723
  need_desegmentation: offset = 0, reported_length_remaining = 723

dissect_ssl enter frame #80 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #85 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 1263
  need_desegmentation: offset = 0, reported_length_remaining = 1263

dissect_ssl enter frame #92 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #92 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 1083
  need_desegmentation: offset = 0, reported_length_remaining = 1083

dissect_ssl enter frame #107 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 9021
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 9016, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004C7B210

dissect_ssl enter frame #107 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000005731058, ssl_session = 00000000081C0720
  record: offset = 0, reported_length_remaining = 903
  need_desegmentation: offset = 0, reported_length_remaining = 903</code></pre></div><div id="question-tags" class="tags-container tags">ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '15, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/68beada090dad3d95ef1329af021aa2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EASGCS&#39;s gravatar image" /><p>EASGCS<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EASGCS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '15, 01:53</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-42766" class="comments-container"></div><div id="comment-tools-42766" class="comment-tools"></div><div class="clear"></div><div id="comment-42766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42788"></span>

<div id="answer-container-42788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42788-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)</code></pre><p>That line is an indicator that you have loaded the wrong private key for the TLS session. Please double check that.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42788" class="comments-container"></div><div id="comment-tools-42788" class="comment-tools"></div><div class="clear"></div><div id="comment-42788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

