+++
type = "question"
title = "Decrypt with RSA key not working"
description = '''I am using nginx on top of flask server. When i am running my site through browser as https it runs ok but if i use same key to decrypt the data using wireshark its not decrypting it. Any suggestion'''
date = "2014-11-21T22:48:00Z"
lastmod = "2014-11-25T01:15:00Z"
weight = 38064
keywords = [ "ssl" ]
aliases = [ "/questions/38064" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt with RSA key not working](/questions/38064/decrypt-with-rsa-key-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38064-score" class="post-score" title="current number of votes">0</div><span id="post-38064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using nginx on top of flask server. When i am running my site through browser as https it runs ok but if i use same key to decrypt the data using wireshark its not decrypting it. Any suggestion</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '14, 22:48</strong></p><img src="https://secure.gravatar.com/avatar/ce0f9d9ed0323c3f77360a99349b921d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="singh&#39;s gravatar image" /><p><span>singh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="singh has no accepted answers">0%</span></p></div></div><div id="comments-container-38064" class="comments-container"><span id="38065"></span><div id="comment-38065" class="comment"><div id="post-38065-score" class="comment-score"></div><div class="comment-text"><p>I suspect something is wrong. Unfortunately with the info you've given that's all we can say. Have you looked at the Wiki page on <a href="http://wiki.wireshark.org/SSL">SSL</a>?</p><p>If you post the contents of the SSL debug log (the path is set in the SSL dissector preferences) by editing your question then someone may be able to help.</p></div><div id="comment-38065-info" class="comment-info"><span class="comment-age">(22 Nov '14, 02:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38118"></span><div id="comment-38118" class="comment"><div id="post-38118-score" class="comment-score"></div><div class="comment-text"><p>Decrypt with RSA key not working</p><p>This is Log file Wireshark SSL debug log</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0x119d800
Private key imported: KeyID 71:67:3d:02:ae:65:dc:95:c7:ea:4e:0f:12:b7:48:73:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;443&#39; filename &#39;/var/www/demoapp/wirekey.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /var/www/demoapp/wirekey.pem successfully loaded.
association_add TCP port 443 protocol http handle 0x119d800

dissect_ssl enter frame #8 (first time)
ssl_session_init: initializing ptr 0x7f3b56ba18f0 size 688
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 194
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 189, ssl state 0x00
association_find: TCP port 49049 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 185 bytes, remaining 194 
packet_from_server: is from server - FALSE
ssl_find_private_key server 127.0.0.1:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #10 (first time)
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 1059
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0xC02F
  record: offset = 79, reported_length_remaining = 980
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 756, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 84 length 752 bytes, remaining 840 
  record: offset = 840, reported_length_remaining = 219
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 205, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 845 length 201 bytes, remaining 1050 
  record: offset = 1050, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1055 length 0 bytes, remaining 1059

dissect_ssl enter frame #12 (first time)
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 162
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 70, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
ssl_decrypt_pre_master_secret key exchange 0 different from KEX_RSA (16)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 75, reported_length_remaining = 87
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 81
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 76, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 86 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 0 offset 90 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 178 offset 94 length 11722625 bytes, remaining 162

dissect_ssl enter frame #13 (first time)
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 316
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 311, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 49049 found (nil)
association_find: TCP port 443 found 0x583abd0

dissect_ssl enter frame #17 (first time)
ssl_session_init: initializing ptr 0x7f3b56ba2990 size 688
  conversation = 0x7f3b56ba2380, ssl_session = 0x7f3b56ba2990
  record: offset = 0, reported_length_remaining = 162
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 157, ssl state 0x00
association_find: TCP port 49050 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 153 bytes, remaining 162 
packet_from_server: is from server - FALSE
ssl_find_private_key server 127.0.0.1:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #19 (first time)
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 258
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 202, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 198 bytes, remaining 207 
  record: offset = 207, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 213, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 206 offset 218 length 1097350 bytes, remaining 258

dissect_ssl enter frame #20 (first time)
  conversation = 0x7f3b56ba2380, ssl_session = 0x7f3b56ba2990
  record: offset = 0, reported_length_remaining = 1059
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
trying to use SSL keylog in 
failed to open SSL keylog
  cannot find master secret in keylog file either
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0xC02F
  record: offset = 79, reported_length_remaining = 980
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 756, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 84 length 752 bytes, remaining 840 
  record: offset = 840, reported_length_remaining = 219
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 205, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 845 length 201 bytes, remaining 1050 
  record: offset = 1050, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1055 length 0 bytes, remaining 1059

dissect_ssl enter frame #22 (first time)
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 283
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 278, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x583abd0

dissect_ssl enter frame #24 (first time)
  conversation = 0x7f3b56ba2380, ssl_session = 0x7f3b56ba2990
  record: offset = 0, reported_length_remaining = 162
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 70, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
ssl_decrypt_pre_master_secret key exchange 0 different from KEX_RSA (16)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 75, reported_length_remaining = 87
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 81
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 76, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 0 offset 86 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 0 offset 90 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 95 offset 94 length 1036009 bytes, remaining 162

dissect_ssl enter frame #25 (first time)
  conversation = 0x7f3b56ba2380, ssl_session = 0x7f3b56ba2990
  record: offset = 0, reported_length_remaining = 258
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 202, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 198 bytes, remaining 207 
  record: offset = 207, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 213, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 179 offset 218 length 16005502 bytes, remaining 258

dissect_ssl enter frame #41 (first time)
  conversation = 0x7f3b56ba2380, ssl_session = 0x7f3b56ba2990
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 26, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #8 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 194
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 185 bytes, remaining 194

dissect_ssl enter frame #8 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 194
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 185 bytes, remaining 194

dissect_ssl enter frame #10 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 1059
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 980
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 84 length 752 bytes, remaining 840 
  record: offset = 840, reported_length_remaining = 219
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 12 offset 845 length 201 bytes, remaining 1050 
  record: offset = 1050, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 1055 length 0 bytes, remaining 1059

dissect_ssl enter frame #12 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 162
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 87
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 81, reported_length_remaining = 81
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 86 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 0 offset 90 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 178 offset 94 length 11722625 bytes, remaining 162

dissect_ssl enter frame #13 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 316
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 49049 found (nil)
association_find: TCP port 443 found 0x583abd0

dissect_ssl enter frame #17 (already visited)
  conversation = 0x7f3b56ba2380, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 162
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 153 bytes, remaining 162

dissect_ssl enter frame #19 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 258
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 198 bytes, remaining 207 
  record: offset = 207, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 213, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 206 offset 218 length 1097350 bytes, remaining 258

dissect_ssl enter frame #20 (already visited)
  conversation = 0x7f3b56ba2380, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 1059
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 980
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 84 length 752 bytes, remaining 840 
  record: offset = 840, reported_length_remaining = 219
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 12 offset 845 length 201 bytes, remaining 1050 
  record: offset = 1050, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 1055 length 0 bytes, remaining 1059

dissect_ssl enter frame #22 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 283
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 443 found 0x583abd0

dissect_ssl enter frame #24 (already visited)
  conversation = 0x7f3b56ba2380, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 162
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 87
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 81, reported_length_remaining = 81
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 0 offset 86 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 0 offset 90 length 0 bytes, remaining 162 
dissect_ssl3_handshake iteration 0 type 95 offset 94 length 1036009 bytes, remaining 162

dissect_ssl enter frame #25 (already visited)
  conversation = 0x7f3b56ba2380, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 258
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 198 bytes, remaining 207 
  record: offset = 207, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 213, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 179 offset 218 length 16005502 bytes, remaining 258

dissect_ssl enter frame #41 (already visited)
  conversation = 0x7f3b56ba2380, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 21 Alert

dissect_ssl enter frame #8 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 194
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 185 bytes, remaining 194

dissect_ssl enter frame #8 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 194
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 185 bytes, remaining 194

dissect_ssl enter frame #69 (first time)
  conversation = 0x7f3b56ba12e0, ssl_session = 0x7f3b56ba18f0
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 26, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #69 (already visited)
  conversation = 0x7f3b56ba12e0, ssl_session = (nil)
  record: offset = 0, reported_length_remaining = 31
dissect_ssl3_record: content_type 21 Alert</code></pre></div><div id="comment-38118-info" class="comment-info"><span class="comment-age">(25 Nov '14, 01:15)</span> <span class="comment-user userinfo">singh</span></div></div></div><div id="comment-tools-38064" class="comment-tools"></div><div class="clear"></div><div id="comment-38064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

