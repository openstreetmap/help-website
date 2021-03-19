+++
type = "question"
title = "Error decrypting SSL traffic"
description = '''I have searched the forum and found only one other question with the same error, which was not answered. I am trying to decrypt an SSL connection. It doesn&#x27;t use DH, so I understand it should be possible to decrypt. The following log shows the error. Specifically, it appears to be ssl_generate_pre_m...'''
date = "2015-10-26T15:01:00Z"
lastmod = "2015-10-26T15:01:00Z"
weight = 46961
keywords = [ "ssl", "decryption", "error" ]
aliases = [ "/questions/46961" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error decrypting SSL traffic](/questions/46961/error-decrypting-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46961-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have searched the forum and found only one other question with the same error, which was not answered. I am trying to decrypt an SSL connection. It doesn't use DH, so I understand it should be possible to decrypt. The following log shows the error.</p><p>Specifically, it appears to be<br />
<code>ssl_generate_pre_master_secret: not enough data to generate key (required state 17)</code></p><hr /><pre><code>Wireshark SSL debug log

ssl_association_remove removing TCP 443 - http handle 0x10e060a10
Private key imported: KeyID 7a:68:98:9b:11:ee:eb:07:ac:b8:05:8d:fe:d6:d6:57:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;172.16.9.8&#39; (172.16.9.8) port &#39;443&#39; filename &#39;/Users/obeattie/Desktop/key.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /Users/obeattie/Desktop/key.key successfully loaded.
association_add TCP port 443 protocol http handle 0x10e060a10

dissect_ssl enter frame #3 (first time)
ssl_session_init: initializing ptr 0x10bfa6440 size 712
association_find: TCP port 57514 found 0x0
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x10bfa6440
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 124, ssl state 0x00
association_find: TCP port 57514 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129 
packet_from_server: is from server - FALSE
ssl_find_private_key server 172.16.9.8:443
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x10bfa6440
  record: offset = 0, reported_length_remaining = 326
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 11
ssl_generate_pre_master_secret: not enough data to generate key (required state 17)
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 82 offset 278 length 11871576 bytes, remaining 326

dissect_ssl enter frame #7 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x10bfa6440
  record: offset = 0, reported_length_remaining = 245
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 240, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 57514 found 0x0
association_find: TCP port 443 found 0x1104b0d20

dissect_ssl enter frame #8 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x10bfa6440
  record: offset = 0, reported_length_remaining = 1380
  need_desegmentation: offset = 0, reported_length_remaining = 1380

dissect_ssl enter frame #9 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x10bfa6440
  record: offset = 0, reported_length_remaining = 1557
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1552, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 57514 found 0x0
association_find: TCP port 443 found 0x1104b0d20

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #6 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 326
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
  record: offset = 267, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 273, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 82 offset 278 length 11871576 bytes, remaining 326

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 245
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 57514 found 0x0
association_find: TCP port 443 found 0x1104b0d20

dissect_ssl enter frame #9 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 1557
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 57514 found 0x0
association_find: TCP port 443 found 0x1104b0d20

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #6 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 326
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
  record: offset = 267, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 273, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 82 offset 278 length 11871576 bytes, remaining 326

dissect_ssl enter frame #7 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 245
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 57514 found 0x0
association_find: TCP port 443 found 0x1104b0d20

dissect_ssl enter frame #9 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 1557
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 57514 found 0x0
association_find: TCP port 443 found 0x1104b0d20

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #3 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 129
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 120 bytes, remaining 129

dissect_ssl enter frame #6 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0x10ee01058, ssl_session = 0x0
  record: offset = 0, reported_length_remaining = 326
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
  record: offset = 267, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 273, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 82 offset 278 length 11871576 bytes, remaining 326</code></pre></div><div id="question-tags" class="tags-container tags">ssl decryption error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '15, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/acab65d674375c233a783d1aad163528?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="obeattie&#39;s gravatar image" /><p>obeattie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="obeattie has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-46961" class="comments-container"><span id="46962"></span><div id="comment-46962" class="comment"><div id="post-46962-score" class="comment-score"></div><div class="comment-text"><p>there seems to be something wrong with the ssl debug file. Take a look at the frame numbers. They are jumping back and forth !?</p><p>Can you please do the following:</p><ul><li>close Wireshark</li><li>empty the ssl debug file</li><li>open Wireshark</li><li>load the pcap file</li><li>close Wireshark</li><li>upload the full ssl debug file somewhere</li></ul></div><div id="comment-46962-info" class="comment-info"><span class="comment-age">(26 Oct '15, 15:10)</span> Kurt Knochner ♦</div></div><span id="47053"></span><div id="comment-47053" class="comment"><div id="post-47053-score" class="comment-score"></div><div class="comment-text"><p>@obeattie In addition, please add the version of Wireshark that you are using.</p></div><div id="comment-47053-info" class="comment-info"><span class="comment-age">(29 Oct '15, 02:59)</span> Lekensteyn</div></div><span id="47059"></span><div id="comment-47059" class="comment"><div id="post-47059-score" class="comment-score"></div><div class="comment-text"><p>Offtopic, @Lekensteyn, could the ssl debug log have the version added to the first entry?</p></div><div id="comment-47059-info" class="comment-info"><span class="comment-age">(29 Oct '15, 05:09)</span> grahamb ♦</div></div><span id="47064"></span><div id="comment-47064" class="comment"><div id="post-47064-score" class="comment-score"></div><div class="comment-text"><p>Offtopic #2 :-)), @Lekensteyn, could please add some code to the SSL dissector to detect ciphers with Diffie Hellman and add a warning/info message to the ssl debug log?</p></div><div id="comment-47064-info" class="comment-info"><span class="comment-age">(29 Oct '15, 07:14)</span> Kurt Knochner ♦</div></div><span id="47065"></span><div id="comment-47065" class="comment"><div id="post-47065-score" class="comment-score"></div><div class="comment-text"><p>Offtopic #3 :-)), @Lekensteyn, and some code to detect SSL session resume or TLS tickets with missing key exchange plus an info/warning in the ssl debug log?</p></div><div id="comment-47065-info" class="comment-info"><span class="comment-age">(29 Oct '15, 07:16)</span> Kurt Knochner ♦</div></div><span id="47066"></span><div id="comment-47066" class="comment not_top_scorer"><div id="post-47066-score" class="comment-score"></div><div class="comment-text"><p>Offtopic replies: I was thinking about adding the string representation of the cipher suites and WS version, but adding hints is probably a good idea! Patch is in being baked.</p></div><div id="comment-47066-info" class="comment-info"><span class="comment-age">(29 Oct '15, 07:16)</span> Lekensteyn</div></div><span id="47069"></span><div id="comment-47069" class="comment not_top_scorer"><div id="post-47069-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner You do not seem to have a Gerrit account, is that correct? The patch for versions is at <a href="https://code.wireshark.org/review/11403,">https://code.wireshark.org/review/11403,</a> I will look into adding expert info for session resumption.</p></div><div id="comment-47069-info" class="comment-info"><span class="comment-age">(29 Oct '15, 08:23)</span> Lekensteyn</div></div><span id="47091"></span><div id="comment-47091" class="comment not_top_scorer"><div id="post-47091-score" class="comment-score"></div><div class="comment-text"><p>@Lekensteyn: No, I don't have a Gerrit account yet as I don't have the feeling I have something useful to cotribute to the code ;-)</p><blockquote><p>The patch for versions is at <a href="https://code.wireshark.org/review/11403,">https://code.wireshark.org/review/11403,</a></p></blockquote><p>I'll have a look, but I'm sure you know much better than me what you are doing ;-)</p><blockquote><p>I will look into adding expert info for session resumption.</p></blockquote><p>Thanks!</p></div><div id="comment-47091-info" class="comment-info"><span class="comment-age">(30 Oct '15, 08:22)</span> Kurt Knochner ♦</div></div><span id="47316"></span><div id="comment-47316" class="comment not_top_scorer"><div id="post-47316-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner I have added the session resumption hint in <a href="https://code.wireshark.org/review/11583.">https://code.wireshark.org/review/11583.</a> I have doubt on adding another warning for DH suites though, the user can easily learn this by looking at the handshake. And if an expert info field is added to the ClientKeyExchange packet, then it will not be visible in other packets (like Application data). Adding it to every Application Data message introduces some noise. So in the end I think it is better to educate the user on dissecting packets. Thoughts?</p></div><div id="comment-47316-info" class="comment-info"><span class="comment-age">(05 Nov '15, 14:25)</span> Lekensteyn</div></div></div><div id="comment-tools-46961" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-46961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

