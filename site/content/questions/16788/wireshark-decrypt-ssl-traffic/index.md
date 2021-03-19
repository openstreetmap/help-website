+++
type = "question"
title = "Wireshark Decrypt SSL traffic"
description = '''Trying to decrypt SSL traffic inside Wireshark Wireshark setup is using: 192.168.2.60(server),443(port),http(protocol - have also tried data) and associated private key SSL decrypt log/output: ======================================================== ssl_association_remove removing TCP 443 - data han...'''
date = "2012-12-11T19:08:00Z"
lastmod = "2012-12-12T02:53:00Z"
weight = 16788
keywords = [ "wireshark" ]
aliases = [ "/questions/16788" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Decrypt SSL traffic](/questions/16788/wireshark-decrypt-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16788-score" class="post-score" title="current number of votes">0</div><span id="post-16788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to decrypt SSL traffic inside Wireshark</p><p>Wireshark setup is using: 192.168.2.60(server),443(port),http(protocol - have also tried <em>data</em>) and associated private key</p><p>SSL decrypt log/output:</p><p>========================================================</p><pre><code>ssl_association_remove removing TCP 443 - data handle 0375D520
Private key imported: KeyID 9a:64:14:cf:59:cf:a1:7a:55:4b:fb:c1:c4:66:b3:35:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;192.168.2.60&#39; (192.168.2.60) port &#39;443&#39; filename &#39;C:\theta\theta2.rsa.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\theta\theta2.rsa.pem successfully loaded.
association_add TCP port 443 protocol data handle 0375D520

dissect_ssl enter frame #114 (first time)
ssl_session_init: initializing ptr 05AE73E8 size 588
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 245
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 240, ssl state 0x00
association_find: TCP port 44256 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 236 bytes, remaining 245 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.2.60:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #153 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 2045
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2040, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 2045 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0016 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 1530 bytes, remaining 2045 
dissect_ssl3_handshake iteration 0 type 12 offset 1613 length 424 bytes, remaining 2045 
dissect_ssl3_handshake iteration 0 type 14 offset 2041 length 0 bytes, remaining 2045

dissect_ssl enter frame #156 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 158
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 102, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 98 bytes, remaining 107 
ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 107, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 113, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 8 offset 118 length 11577009 bytes, remaining 158

dissect_ssl enter frame #187 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #188 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 67 offset 5 length 5141154 bytes, remaining 45

dissect_ssl enter frame #190 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 170
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 24, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 44256 found 00000000
association_find: TCP port 443 found 07550E50
  record: offset = 29, reported_length_remaining = 141
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 136, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 44256 found 00000000
association_find: TCP port 443 found 07550E50

dissect_ssl enter frame #191 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 461
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 456, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 07550E50

dissect_ssl enter frame #192 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 1357
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1352, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 07550E50

dissect_ssl enter frame #194 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 29
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 24, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #197 (first time)
  conversation = 05AE6F64, ssl_session = 05AE73E8
  record: offset = 0, reported_length_remaining = 29
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 24, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '12, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/985c8ec06ea1b8cb7f0edfa28f63f138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeremycook123&#39;s gravatar image" /><p><span>jeremycook123</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeremycook123 has no accepted answers">0%</span></p></div></div><div id="comments-container-16788" class="comments-container"></div><div id="comment-tools-16788" class="comment-tools"></div><div class="clear"></div><div id="comment-16788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16792"></span>

<div id="answer-container-16792" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16792-score" class="post-score" title="current number of votes">1</div><span id="post-16792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The SSL session is using the DH key exchange algorithm which can't be decrypted, the debug log shows this with the line:</p><pre><code>ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt</code></pre><p>If you can set the server or the client to use a different cipher suite that doesn't use DH then SSL decryption should work. You will have to search elsewhere to determine how to set the cipher suite for your server and client.</p><p>See the <a href="http://wiki.wireshark.org/SSL">SSL Wiki</a> page for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '12, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-16792" class="comments-container"></div><div id="comment-tools-16792" class="comment-tools"></div><div class="clear"></div><div id="comment-16792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

