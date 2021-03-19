+++
type = "question"
title = "Unable to decrypt HTTPS in wireshark"
description = '''Hello team,  I have 2 sniffers (one is 138K, the other is 47M). Both sniffers are destined to same vip same cert. I can decrypt the small sniffer. But I cannot decrypt the big one. Here is some information from debug. This is for critical troubleshooting. Thanks a lot for the help. dissect_ssl enter...'''
date = "2017-01-19T09:12:00Z"
lastmod = "2017-01-19T09:12:00Z"
weight = 58889
keywords = [ "decrypt", "https" ]
aliases = [ "/questions/58889" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt HTTPS in wireshark](/questions/58889/unable-to-decrypt-https-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58889-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello team, I have 2 sniffers (one is 138K, the other is 47M). Both sniffers are destined to same vip same cert. I can decrypt the small sniffer. But I cannot decrypt the big one.</p><p>Here is some information from debug. This is for critical troubleshooting. Thanks a lot for the help.</p><pre><code>dissect_ssl enter frame #4 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000004711700, ssl_session = 00000000047120D0
  record: offset = 0, reported_length_remaining = 146
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 141
decrypt_ssl3_record: app_data len 141, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 137 bytes, remaining 146 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000004711700, ssl_session = 00000000047120D0
  record: offset = 0, reported_length_remaining = 177
ssl_try_set_version found version 0x0303 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 81
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
ssl_try_set_version found version 0x0303 -&gt; state 0x11
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0x003D TLS_RSA_WITH_AES_256_CBC_SHA256 -&gt; state 0x17
  record: offset = 86, reported_length_remaining = 91
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Session resumption using Session ID
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 97 80
decrypt_ssl3_record: app_data len 80, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 107 offset 97 length 9561053 bytes, remaining 177 

dissect_ssl enter frame #8 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000004711700, ssl_session = 00000000047120D0
  record: offset = 0, reported_length_remaining = 91
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 80
decrypt_ssl3_record: app_data len 80, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 74 offset 11 length 14921458 bytes, remaining 91 

dissect_ssl enter frame #9 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000004711700, ssl_session = 00000000047120D0
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000004711700, ssl_session = 00000000047120D0
  record: offset = 0, reported_length_remaining = 4485
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 4480, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000004711700, ssl_session = 00000000047120D0
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 304, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #27 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000004714A40, ssl_session = 0000000004715410
  record: offset = 0, reported_length_remaining = 146
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 141
decrypt_ssl3_record: app_data len 141, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 137 bytes, remaining 146 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01</code></pre></div><div id="question-tags" class="tags-container tags">decrypt https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '17, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/c96f49c12169d51f64dc338c2d3f4a82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ping2&#39;s gravatar image" /><p>ping2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ping2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '17, 09:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58889" class="comments-container"></div><div id="comment-tools-58889" class="comment-tools"></div><div class="clear"></div><div id="comment-58889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

