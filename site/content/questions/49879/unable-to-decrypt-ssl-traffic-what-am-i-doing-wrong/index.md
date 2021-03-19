+++
type = "question"
title = "Unable to decrypt SSL traffic, what am I doing wrong ?"
description = '''Wireshark v2.0.1 GnuTLS 3.2.15 PEM Format passphraseless private key added to SSL protocol. Has been successfully loaded.  SSL RSA keys list preferences: IP Address=10.139.233.26 Port=10080 Protocol=http  Have ensured, Client Hello/Server Hello captured. Have filtered on tcp stream and exported, SSL...'''
date = "2016-02-04T22:24:00Z"
lastmod = "2016-02-09T09:21:00Z"
weight = 49879
keywords = [ "ssl", "tlsv1.2" ]
aliases = [ "/questions/49879" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to decrypt SSL traffic, what am I doing wrong ?](/questions/49879/unable-to-decrypt-ssl-traffic-what-am-i-doing-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49879-score" class="post-score" title="current number of votes">0</div><span id="post-49879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark v2.0.1 GnuTLS 3.2.15 PEM Format passphraseless private key added to SSL protocol. Has been successfully loaded.</p><p><code> SSL RSA keys list preferences: IP Address=10.139.233.26 Port=10080 Protocol=http</code></p><p>Have ensured, Client Hello/Server Hello captured.</p><p>Have filtered on tcp stream and exported, SSL debug log following:</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.0.1 (v2.0.1-0-g59ea380 from master-2.0)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

ssl_association_remove removing TCP 10080 - http handle 00000000088B4800
KeyID[20]:
| ae 4d dc ef 87 7a 05 e1 30 4a 1b 59 1b d8 20 10 |.M...z..0J.Y.. .|
| 45 ba 69 7a                                     |E.iz            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file D:/temp/nopassphrase.key successfully loaded.
ssl_init port &#39;10080&#39; filename &#39;D:/temp/nopassphrase.key&#39; password(only for p12 file) &#39;&#39;
association_add TCP port 10080 protocol http handle 00000000088B4800

dissect_ssl enter frame #4 (first time)
association_find: TCP port 47180 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 177
decrypt_ssl3_record: app_data len 177, ssl state 0x00
association_find: TCP port 47180 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 173 bytes, remaining 182 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 81
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0x003D TLS_RSA_WITH_AES_256_CBC_SHA256 -&gt; state 0x17
  record: offset = 86, reported_length_remaining = 1362
  need_desegmentation: offset = 86, reported_length_remaining = 1362

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 2682
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 2677
decrypt_ssl3_record: app_data len 2677, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2673 bytes, remaining 2682 
lookup(KeyID)[20]:
| ae 4d dc ef 87 7a 05 e1 30 4a 1b 59 1b d8 20 10 |.M...z..0J.Y.. .|
| 45 ba 69 7a                                     |E.iz            |
ssl_find_private_key_by_pubkey: lookup result: 000000000942BA40

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 42
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 37
decrypt_ssl3_record: app_data len 37, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 5 length 29 bytes, remaining 42 
dissect_ssl3_handshake iteration 0 type 14 offset 38 length 0 bytes, remaining 42

dissect_ssl enter frame #10 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 1792
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 1787
decrypt_ssl3_record: app_data len 1787, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 1521 bytes, remaining 1792 
lookup(KeyID)[20]:
| 18 23 aa a8 6d 41 5c 54 28 97 25 25 6c 96 44 f0 |.#..mA\T(.%%l.D.|
| 99 43 cc 22                                     |.C.&quot;            |
ssl_find_private_key_by_pubkey: lookup result: 0000000000000000
dissect_ssl3_handshake iteration 0 type 16 offset 1530 length 258 bytes, remaining 1792 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 217
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret

dissect_ssl enter frame #12 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 269
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 264
decrypt_ssl3_record: app_data len 264, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 15 offset 5 length 260 bytes, remaining 269

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x217
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 80
decrypt_ssl3_record: app_data len 80, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 250 offset 5 length 11866047 bytes, remaining 85

dissect_ssl enter frame #18 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 91
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x217
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 80
decrypt_ssl3_record: app_data len 80, ssl state 0x217
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 11 length 1731724 bytes, remaining 91

dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 800, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 47180 found 0000000000000000
association_find: TCP port 10080 found 000000000A538FD0

dissect_ssl enter frame #20 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 885
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 880, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #22 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 389
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 384, ssl state 0x217
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #23 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 197
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 192, ssl state 0x217
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #24 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 64, ssl state 0x217
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #25 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 000000000B181980
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 64, ssl state 0x217
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #4 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 173 bytes, remaining 182

dissect_ssl enter frame #6 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
  record: offset = 86, reported_length_remaining = 1362
  need_desegmentation: offset = 86, reported_length_remaining = 1362

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2682
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2673 bytes, remaining 2682

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 42
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 13 offset 5 length 29 bytes, remaining 42 
dissect_ssl3_handshake iteration 0 type 14 offset 38 length 0 bytes, remaining 42

dissect_ssl enter frame #10 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1792
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 1521 bytes, remaining 1792 
dissect_ssl3_handshake iteration 0 type 16 offset 1530 length 258 bytes, remaining 1792

dissect_ssl enter frame #12 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 269
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 15 offset 5 length 260 bytes, remaining 269

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec

dissect_ssl enter frame #16 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 250 offset 5 length 11866047 bytes, remaining 85

dissect_ssl enter frame #18 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 91
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 11 length 1731724 bytes, remaining 91

dissect_ssl enter frame #19 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #20 (already visited)
packet_from_server: is from server - FALSE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 885
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #22 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 389
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #23 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 197
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #24 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #25 (already visited)
packet_from_server: is from server - TRUE
  conversation = 000000000B181160, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tlsv1.2" rel="tag" title="see questions tagged &#39;tlsv1.2&#39;">tlsv1.2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/d24c9430a844e121d24261254a38cbd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TwoYrOldGorilla&#39;s gravatar image" /><p><span>TwoYrOldGorilla</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TwoYrOldGorilla has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '16, 21:58</strong> </span></p></div></div><div id="comments-container-49879" class="comments-container"></div><div id="comment-tools-49879" class="comment-tools"></div><div class="clear"></div><div id="comment-49879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50022"></span>

<div id="answer-container-50022" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50022-score" class="post-score" title="current number of votes">1</div><span id="post-50022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TwoYrOldGorilla has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are affected by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12042">bug 12042</a> which is a regression introduced with Wireshark 2.0 and will be fixed in 2.0.2 (which is scheduled for 11 February). The issue occurs when Wireshark 2.0 and 2.0.1 are used to decrypt a SSL capture which contain a Client Certificate (also known as two-way SSL or mutual authentication). As a workaround, you can try to ignore the Client Certificate packet.</p><p>Details of analysis:</p><pre><code>dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
...
dissect_ssl3_record: content_type 22 Handshake
...
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 2673 bytes, remaining 2682 
lookup(KeyID)[20]:
| ae 4d dc ef 87 7a 05 e1 30 4a 1b 59 1b d8 20 10 |.M...z..0J.Y.. .|
| 45 ba 69 7a                                     |E.iz            |
ssl_find_private_key_by_pubkey: lookup result: 000000000942BA40</code></pre><p>Type 11 is a Certificate and the private key lookup has succeeded. It should be used unless another certificate is found.</p><pre><code>dissect_ssl enter frame #10 (first time)
packet_from_server: is from server - FALSE
...
dissect_ssl3_record: content_type 22 Handshake
...
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 1521 bytes, remaining 1792 
lookup(KeyID)[20]:
| 18 23 aa a8 6d 41 5c 54 28 97 25 25 6c 96 44 f0 |.#..mA\T(.%%l.D.|
| 99 43 cc 22                                     |.C.&quot;            |
ssl_find_private_key_by_pubkey: lookup result: 0000000000000000</code></pre><p>Oops, another Certificate (handshake message type 11), but this time it is <em>not</em> from the server. The client certificate cannot be used for decryption and the key lookup fails and clears the previously found private key.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-50022" class="comments-container"></div><div id="comment-tools-50022" class="comment-tools"></div><div class="clear"></div><div id="comment-50022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

