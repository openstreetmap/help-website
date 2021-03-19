+++
type = "question"
title = "What is decoder decrypt_ssl3_record: no decoder available"
description = '''Hello Team, Can someone help me to understand why we can&#x27;t decrypt SSL communication? This is capture on windows 2008 web server. One thing that stands out from trace are the following: no decoder available decrypt_ssl3_record: using client decoder  decrypt_ssl3_record: no decoder available Any comm...'''
date = "2017-03-16T08:05:00Z"
lastmod = "2017-03-16T08:38:00Z"
weight = 60110
keywords = [ "decrypt_ssl3_record" ]
aliases = [ "/questions/60110" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is decoder decrypt\_ssl3\_record: no decoder available](/questions/60110/what-is-decoder-decrypt_ssl3_record-no-decoder-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60110-score" class="post-score" title="current number of votes">0</div><span id="post-60110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Team, Can someone help me to understand why we can't decrypt SSL communication? This is capture on windows 2008 web server. One thing that stands out from trace are the following: no decoder available</p><p>decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available</p><p>Any comment or feedback appreciated. Thank u</p><p>Wireshark SSL debug log :</p><pre><code>Wireshark version: 2.2.5 (v2.2.5-0-g440fd4d)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

KeyID[20]:
| 4f 53 67 9a 82 f5 a6 b7 af a1 84 b1 d7 0b b9 d8 |OSg.............|
| d5 c9 b3 9f                                     |....            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file F:/openssl/wildccf2018.ukey successfully loaded.
ssl_init port &#39;443&#39; filename &#39;F:/openssl/wildccf2018.ukey&#39; password(only for p12 file) &#39;&#39;
association_add ssl.port port 443 handle 00000000047F5C60

dissect_ssl enter frame #477 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000000073DDB10, ssl_session = 00000000073DE080
  record: offset = 0, reported_length_remaining = 741
ssl_try_set_version found version 0x0301 -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 736, ssl state 0x10
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #478 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000000073DDB10, ssl_session = 00000000073DE080
  record: offset = 0, reported_length_remaining = 101
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 96, ssl state 0x10
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #480 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000000073DDB10, ssl_session = 00000000073DE080
  record: offset = 0, reported_length_remaining = 5269
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 5264, ssl state 0x10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #2037 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000000074873F0, ssl_session = 0000000007487DC0
  record: offset = 0, reported_length_remaining = 169
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 164
decrypt_ssl3_record: app_data len 164, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 160 bytes, remaining 169 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #2038 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000000074873F0, ssl_session = 0000000007487DC0
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #2040 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000000074873F0, ssl_session = 0000000007487DC0
  record: offset = 0, reported_length_remaining = 4766
ssl_try_set_version found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4761
decrypt_ssl3_record: app_data len 4761, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 4766 
ssl_try_set_version found version 0x0301 -&gt; state 0x11
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0xC014 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA -&gt; state 0x17
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 2552 bytes, remaining 4766 
lookup(KeyID)[20]:
| 4f 53 67 9a 82 f5 a6 b7 af a1 84 b1 d7 0b b9 d8 |OSg.............|
| d5 c9 b3 9f                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 00000000056ACBA0
dissect_ssl3_handshake iteration 0 type 22 offset 2646 length 1781 bytes, remaining 4766 
dissect_ssl3_handshake iteration 0 type 12 offset 4431 length 327 bytes, remaining 4766 
dissect_ssl3_handshake iteration 0 type 14 offset 4762 length 0 bytes, remaining 4766

dissect_ssl enter frame #2046 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000000074873F0, ssl_session = 0000000007487DC0
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 70
decrypt_ssl3_record: app_data len 70, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 217
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_decrypt_pre_master_secret: session uses Diffie-Hellman key exchange (cipher suite 0xC014 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA) and cannot be decrypted using a RSA private key file.
ssl_generate_pre_master_secret: can&#39;t decrypt pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x217
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 86 48
decrypt_ssl3_record: app_data len 48, ssl state 0x217
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 152 offset 86 length 8466910 bytes, remaining 134

dissect_ssl enter frame #2047 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000000074873F0, ssl_session = 0000000007487DC0
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x217
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 48
decrypt_ssl3_record: app_data len 48, ssl state 0x217
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 199 offset 11 length 3439322 bytes, remaining 59

dissect_ssl enter frame #2037 (already visited)
packet_from_server: is from server - FALSE
  conversation = 00000000074873F0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 169
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 160 bytes, remaining 169

dissect_ssl enter frame #2040 (already visited)
packet_from_server: is from server - TRUE
  conversation = 00000000074873F0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4766
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 4766 
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 2552 bytes, remaining 4766 
dissect_ssl3_handshake iteration 0 type 22 offset 2646 length 1781 bytes, remaining 4766 
dissect_ssl3_handshake iteration 0 type 12 offset 4431 length 327 bytes, remaining 4766 
dissect_ssl3_handshake iteration 0 type 14 offset 4762 length 0 bytes, remaining 4766

dissect_ssl enter frame #2046 (already visited)
packet_from_server: is from server - FALSE
  conversation = 00000000074873F0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 152 offset 86 length 8466910 bytes, remaining 134</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decrypt_ssl3_record" rel="tag" title="see questions tagged &#39;decrypt_ssl3_record&#39;">decrypt_ssl3_record</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '17, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/ab618917f1f0273174970a9a612dfdad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pozzccf&#39;s gravatar image" /><p><span>pozzccf</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pozzccf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Mar '17, 08:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60110" class="comments-container"></div><div id="comment-tools-60110" class="comment-tools"></div><div class="clear"></div><div id="comment-60110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60111"></span>

<div id="answer-container-60111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60111-score" class="post-score" title="current number of votes">0</div><span id="post-60111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your SSL debug log:</p><blockquote><p>ssl_decrypt_pre_master_secret: session uses Diffie-Hellman key exchange (cipher suite 0xC014 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA) and cannot be decrypted using a RSA private key file.</p></blockquote><p>As per the SSL Wiki page, an SSL session that uses a DH key exchange can't be decrypted using the RSA private key file. Instead you have to persuade the client to give up the pre-master secret and then configure Wireshark to use that (SSL preferences, (Pre)-Master-Secret log filename).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '17, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Mar '17, 08:39</strong> </span></p></div></div><div id="comments-container-60111" class="comments-container"></div><div id="comment-tools-60111" class="comment-tools"></div><div class="clear"></div><div id="comment-60111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

