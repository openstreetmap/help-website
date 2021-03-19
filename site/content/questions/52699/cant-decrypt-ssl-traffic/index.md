+++
type = "question"
title = "Can&#x27;t decrypt SSL traffic"
description = '''I&#x27;m trying to decode SSL traffic but I&#x27;m failing so far. I seem to have the correct private key but I can&#x27;t make sense of the log file. At first I was using ECDHE and modified my application to dump the pre master secret but that failed in a very similar way. The capture file and private key can be ...'''
date = "2016-05-17T15:55:00Z"
lastmod = "2016-05-18T07:47:00Z"
weight = 52699
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/52699" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decrypt SSL traffic](/questions/52699/cant-decrypt-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52699-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decode SSL traffic but I'm failing so far. I seem to have the correct private key but I can't make sense of the log file. At first I was using ECDHE and modified my application to dump the pre master secret but that failed in a very similar way.</p><p>The capture file and private key can be found here: <a href="https://www.dropbox.com/sh/4o0qr7hwfoobyrz/AACzzEk9VlrL6XpVQfztIsfma">https://www.dropbox.com/sh/4o0qr7hwfoobyrz/AACzzEk9VlrL6XpVQfztIsfma</a></p><p>This is not https traffic but a custom protocol that sits on top of SSL.</p><p>Any pointers would be greatly appreciated!</p><p>Log follows</p><hr /><pre><code>Wireshark SSL debug log

Wireshark version: 2.0.3 (v2.0.3-0-geed34f0 from master-2.0)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2

ssl_association_remove removing TCP 1677 - data handle 0000025D1D90EFB0
KeyID[20]:
| e9 c1 00 8a f9 61 66 ac b3 1b 37 80 3b df 59 93 |.....af...7.;.Y.|
| ec b7 5c c4                                     |..\.            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file C:/Users/jpmendoza/Desktop/poa-new.key successfully loaded.
ssl_init port &#39;1677&#39; filename &#39;C:/Users/jpmendoza/Desktop/poa-new.key&#39; password(only for p12 file) &#39;&#39;
association_add TCP port 1677 protocol data handle 0000025D1D90EFB0

dissect_ssl enter frame #3 (first time)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000025D1FD1D810
  record: offset = 0, reported_length_remaining = 550

dissect_ssl enter frame #4 (first time)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000025D1FD1D810
  record: offset = 0, reported_length_remaining = 1007
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 58
decrypt_ssl3_record: app_data len 58, ssl state 0x10
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
ssl_dissect_hnd_srv_hello found CIPHER 0x009D TLS_RSA_WITH_AES_256_GCM_SHA384 -&gt; state 0x16
  record: offset = 63, reported_length_remaining = 944
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 68 930
decrypt_ssl3_record: app_data len 930, ssl state 0x16
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 68 length 926 bytes, remaining 998 
lookup(KeyID)[20]:
| e9 c1 00 8a f9 61 66 ac b3 1b 37 80 3b df 59 93 |.....af...7.;.Y.|
| ec b7 5c c4                                     |..\.            |
ssl_find_private_key_by_pubkey: lookup result: 0000025D1E4BDBF0
  record: offset = 998, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 1003 4
decrypt_ssl3_record: app_data len 4, ssl state 0x16
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1003 length 0 bytes, remaining 1007

dissect_ssl enter frame #5 (first time)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000025D1FD1D810
  record: offset = 0, reported_length_remaining = 226
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 170
decrypt_ssl3_record: app_data len 170, ssl state 0x216
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 166 bytes, remaining 175 
ssl_save_master_key not saving empty (pre-)master secret for Session Ticket!
  record: offset = 175, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Not using Session resumption
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x616
ssl_restore_master_key can&#39;t restore master secret using an empty Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Client Random
  Cannot find master secret
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 181, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 186 40
decrypt_ssl3_record: app_data len 40, ssl state 0x616
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 156 offset 186 length 7346719 bytes, remaining 226

dissect_ssl enter frame #3 (already visited)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 550

dissect_ssl enter frame #4 (already visited)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1007
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
  record: offset = 63, reported_length_remaining = 944
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 11 offset 68 length 926 bytes, remaining 998 
  record: offset = 998, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 14 offset 1003 length 0 bytes, remaining 1007

dissect_ssl enter frame #5 (already visited)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 226
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 166 bytes, remaining 175 
  record: offset = 175, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
  record: offset = 181, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 156 offset 186 length 7346719 bytes, remaining 226

dissect_ssl enter frame #6 (first time)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000025D1FD1D810
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #8 (first time)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000025D1FD1D810
  record: offset = 0, reported_length_remaining = 3595
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 3590, ssl state 0x616
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1677 found 0000025D1F07A2E0

dissect_ssl enter frame #8 (already visited)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 3595
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #11 (first time)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000025D1FD1D810
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 46, ssl state 0x616
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #11 (already visited)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 51
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #8 (already visited)
association_find: TCP port 1677 found 0000025D1F07A2E0
packet_from_server: is from server - TRUE
  conversation = 0000025D1FD1D300, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 3595
dissect_ssl3_record: content_type 23 Application Data</code></pre></div><div id="question-tags" class="tags-container tags">ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '16, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/fe3fe9326117d87c4e999abe8722c81c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="superdude&#39;s gravatar image" /><p>superdude<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="superdude has no accepted answers">0%</span></p></div></div><div id="comments-container-52699" class="comments-container"></div><div id="comment-tools-52699" class="comment-tools"></div><div class="clear"></div><div id="comment-52699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52731"></span>

<div id="answer-container-52731" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52731-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>After spending hours with this issue I saw my blindness: I'm capturing incoming traffic, not outgoing. I have the same problem as <a href="https://ask.wireshark.org/questions/27296/wireshark-only-capturing-incoming-packets">https://ask.wireshark.org/questions/27296/wireshark-only-capturing-incoming-packets</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/fe3fe9326117d87c4e999abe8722c81c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="superdude&#39;s gravatar image" /><p>superdude<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="superdude has no accepted answers">0%</span></p></div></div><div id="comments-container-52731" class="comments-container"></div><div id="comment-tools-52731" class="comment-tools"></div><div class="clear"></div><div id="comment-52731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

