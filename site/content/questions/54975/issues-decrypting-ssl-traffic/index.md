+++
type = "question"
title = "issues decrypting SSL Traffic"
description = '''I am trying to decrypt ssl communication for troublshooting but am unable to decode the traffic.  Any help would be greatly appreciated Following is the Debug logs: Wireshark SSL debug log  Wireshark version: 2.0.5 (v2.0.5-0-ga3be9c6 from master-2.0) GnuTLS version: 3.2.15 Libgcrypt version: 1.6.2  ...'''
date = "2016-08-19T07:22:00Z"
lastmod = "2016-08-19T08:11:00Z"
weight = 54975
keywords = [ "decryption", "ssl_decrypt", "ssl" ]
aliases = [ "/questions/54975" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [issues decrypting SSL Traffic](/questions/54975/issues-decrypting-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54975-score" class="post-score" title="current number of votes">0</div><span id="post-54975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt ssl communication for troublshooting but am unable to decode the traffic.</p><p>Any help would be greatly appreciated</p><p>Following is the Debug logs:</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.0.5 (v2.0.5-0-ga3be9c6 from master-2.0)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

ssl_association_remove removing TCP 443 - http handle 00000277EE1E2800
4013 bytes read
PKCS#12 imported
Bag 0/0: PKCS#8 Encrypted key
KeyID[20]:
| 51 f1 fe 2a f4 26 7b db bc 55 30 fb c9 34 58 d8 |Q..*.&amp;{..U0..4X.|
| 50 dd 4f 25                                     |P.O%            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file C:/cert.pfx successfully loaded.
ssl_init port &#39;443&#39; filename &#39;C:/cert.pfx&#39; password(only for p12 file) &#39;Password&#39;
association_add TCP port 443 protocol http handle 00000277EE1E2800

dissect_ssl enter frame #4 (first time)
association_find: TCP port 17008 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 80
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 75
decrypt_ssl3_record: app_data len 75, ssl state 0x00
association_find: TCP port 17008 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 71 bytes, remaining 80 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 1380
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 49
decrypt_ssl3_record: app_data len 49, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 45 bytes, remaining 54 
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0x0039 TLS_DHE_RSA_WITH_AES_256_CBC_SHA -&gt; state 0x17
  record: offset = 54, reported_length_remaining = 1326

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 1380

dissect_ssl enter frame #8 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 1190

dissect_ssl enter frame #12 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 198
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 134
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 139, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 150 48
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 186 offset 150 length 5662814 bytes, remaining 198

dissect_ssl enter frame #13 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec No Session resumption, missing packets?
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 48
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 141 offset 11 length 9969585 bytes, remaining 59

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 901
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 896, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 17008 found 0000000000000000
association_find: TCP port 443 found 00000277EFF042E0

dissect_ssl enter frame #15 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 1380

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 00000277F0B25AD0
  record: offset = 0, reported_length_remaining = 625

dissect_ssl enter frame #4 (already visited)
packet_from_server: is from server - FALSE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 80
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 71 bytes, remaining 80

dissect_ssl enter frame #6 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1380
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 45 bytes, remaining 54 
  record: offset = 54, reported_length_remaining = 1326

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1380

dissect_ssl enter frame #8 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1190

dissect_ssl enter frame #12 (already visited)
packet_from_server: is from server - FALSE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 198
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
  record: offset = 139, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 145, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 186 offset 150 length 5662814 bytes, remaining 198

dissect_ssl enter frame #13 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 141 offset 11 length 9969585 bytes, remaining 59

dissect_ssl enter frame #14 (already visited)
packet_from_server: is from server - FALSE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 901
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #15 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1380

dissect_ssl enter frame #16 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000277F0B252B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 625</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/9a8cace9c1d4bf4f790328ca93e8c58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WireSharrkUser&#39;s gravatar image" /><p><span>WireSharrkUser</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WireSharrkUser has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '16, 08:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54975" class="comments-container"><span id="54979"></span><div id="comment-54979" class="comment"><div id="post-54979-score" class="comment-score"></div><div class="comment-text"><p>Have you done the steps which are described here: <a href="https://blog.packet-foo.com/2016/07/how-to-use-wireshark-to-steal-passwords/">https://blog.packet-foo.com/2016/07/how-to-use-wireshark-to-steal-passwords/</a></p></div><div id="comment-54979-info" class="comment-info"><span class="comment-age">(19 Aug '16, 08:11)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-54975" class="comment-tools"></div><div class="clear"></div><div id="comment-54975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54978"></span>

<div id="answer-container-54978" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54978-score" class="post-score" title="current number of votes">2</div><span id="post-54978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="WireSharrkUser has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your capture is using a cipher suite using the Diffie-Hellman key exchange:</p><pre><code>ssl_dissect_hnd_srv_hello found CIPHER 0x0039 TLS_DHE_RSA_WITH_AES_256_CBC_SHA -&gt; state 0x17
                                                  ^^^</code></pre><p>This does not work with a RSA private key file. See <a href="http://security.stackexchange.com/q/35639/2630">Decrypting TLS in Wireshark when using DHE_RSA ciphersuites</a> for an alternative.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '16, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-54978" class="comments-container"></div><div id="comment-tools-54978" class="comment-tools"></div><div class="clear"></div><div id="comment-54978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

