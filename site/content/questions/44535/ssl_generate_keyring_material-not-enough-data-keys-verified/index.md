+++
type = "question"
title = "ssl_generate_keyring_material not enough data (keys verified)"
description = '''Using Version 1.12.5 (v1.12.5-0-g5819e5b from master-1.12), I can&#x27;t get SSL traffic to decrypt for a particular server, debug log shows: ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)  Reading the other threads, I see this is commonly a mismatched private ...'''
date = "2015-07-27T10:24:00Z"
lastmod = "2015-07-27T10:24:00Z"
weight = 44535
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/44535" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ssl\_generate\_keyring\_material not enough data (keys verified)](/questions/44535/ssl_generate_keyring_material-not-enough-data-keys-verified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44535-score" class="post-score" title="current number of votes">0</div><span id="post-44535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Version 1.12.5 (v1.12.5-0-g5819e5b from master-1.12), I can't get SSL traffic to decrypt for a particular server, debug log shows:</p><pre><code>ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)</code></pre><p>Reading the other threads, I see this is commonly a mismatched private key. But, I have verified the private key does indeed match the cert by doing the modulus compare with the cert from capture itself and also writing some java code to do an asym encrypt/decrypt. I see the Client hello with session id = 0 and a non-DH cipher of <code>TLS_RSA_WITH_RC4_128_MD5</code>. I am also able to decrypt the snakeoil example as well as a capture from my local system to a dev server (of course the one I REALLY need to see won't decrypt...)</p><p>This connection does use a client cert, but that wasn't an issue with my local capture which also used it.</p><p>Here's a snippit of my ssl-debug.log</p><pre><code>ssl_association_remove removing TCP 30111 - http handle 0000000005962170
Private key imported: KeyID 36:32:78:72:cd:1f:6d:58:65:90:be:27:a8:af:ae:33:...
ssl_init IPv4 addr &#39;151.22.34.18&#39; (151.22.34.18) port &#39;30111&#39; filename &#39;C:\temp\test.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\temp\test.key successfully loaded.
association_add TCP port 30111 protocol http handle 0000000005962170

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0000000009940720 size 712
association_find: TCP port 46845 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 112
packet_from_server: is from server - FALSE
ssl_find_private_key server 151.22.34.18:30111
ssl_find_private_key: testing 1 keys
client random len: 32 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1369
  need_desegmentation: offset = 79, reported_length_remaining = 1369

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 3759
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 3754, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3750 bytes, remaining 3759

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 22
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 8, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 5 length 4 bytes, remaining 13 
  record: offset = 13, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 18 length 0 bytes, remaining 22

dissect_ssl enter frame #11 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 1448
  need_desegmentation: offset = 0, reported_length_remaining = 1448

dissect_ssl enter frame #14 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 4081
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4076, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3810 bytes, remaining 4081 
dissect_ssl3_handshake iteration 0 type 16 offset 3819 length 258 bytes, remaining 4081 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
pre master encrypted[256]:
| 17 3f 7f eb d4 9c 4b a1 3b 63 a7 68 2b 72 d4 72 |.?....K.;c.h+r.r|
ssl_decrypt_pre_master_secret:RSA_private_decrypt
&lt;snip&gt;
decrypted_unstrip_pre_master[256]:
| 0e 94 12 a1 4d 17 1a 83 1e 40 7f 58 40 fa ae 10 |[email protected]@...|
&lt;snip&gt;
pcry_private_decrypt: stripping 0 bytes, decr_len 256
ssl_decrypt_pre_master_secret wrong pre_master_secret length (256, expected 48)
ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret
trying to use SSL keylog in 
failed to open SSL keylog
dissect_ssl3_handshake can&#39;t generate pre master secret

dissect_ssl enter frame #16 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000006AF1058, ssl_session = 0000000009940720
  record: offset = 0, reported_length_remaining = 310
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 15 offset 5 length 258 bytes, remaining 267 
  record: offset = 267, reported_length_remaining = 43
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 37
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 32, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 140 offset 278 length 15468901 bytes, remaining 310</code></pre><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/727ab653a68cdca4bb614d46dc360aeb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mankiko&#39;s gravatar image" /><p><span>mankiko</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mankiko has no accepted answers">0%</span></p></div></div><div id="comments-container-44535" class="comments-container"></div><div id="comment-tools-44535" class="comment-tools"></div><div class="clear"></div><div id="comment-44535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

