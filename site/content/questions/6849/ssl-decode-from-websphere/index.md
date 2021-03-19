+++
type = "question"
title = "SSL decode from Websphere"
description = '''Hi,  I&#x27;m trying to decode traffic from a (windows) browser to a (Linux) Websphere box. So far I have;  User OPENSSL to extract the default private key from Websphere key.p12. This is the websphere keystore used for SSL. Used OPENSSL to generate an RSA private key, with no password protect. (.pem) Se...'''
date = "2011-10-11T12:56:00Z"
lastmod = "2011-10-11T13:14:00Z"
weight = 6849
keywords = [ "websphere", "ssl" ]
aliases = [ "/questions/6849" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decode from Websphere](/questions/6849/ssl-decode-from-websphere)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to decode traffic from a (windows) browser to a (Linux) Websphere box. So far I have;</p><ol><li>User OPENSSL to extract the default private key from Websphere key.p12. This is the websphere keystore used for SSL.</li><li>Used OPENSSL to generate an RSA private key, with no password protect. (.pem)</li><li>Setup Wireshark as "10.x.x.x,9043,mykey.pem" on the windows client.</li><li>Generated some SSL traffic to the websphere box.</li></ol><p>Now, the debug file seems to read the private key fine, but I can't get any decoding to work. The first bunch of lines from the debug file now follow.</p><p>Any help would be very much appreciated.</p><p>Cheers, Con.</p><pre><code>ssl_init keys string:
10.0.40.70,9043,http,c:\forget\ferm.pem
ssl_init found host entry 10.0.40.70,9043,http,c:\forget\ferm.pem
ssl_init addr &#39;10.0.40.70&#39; port &#39;9043&#39; filename &#39;c:\forget\ferm.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID 20:F2:56:D7:7F:FC:4B:72:B9:B6:58:9F:56:48:A1:57:...
ssl_init private key file c:\forget\ferm.pem successfully loaded
association_add TCP port 9043 protocol http handle 02D2A998

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 04D31B48 size 564
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
dissect_ssl server 10.0.40.70:9043
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 167
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 162 ssl, state 0x00
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 158 bytes, remaining 167 
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #7 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 1996
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 1991 ssl, state 0x11
association_find: TCP port 9043 found 062C9F18
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 1996 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0033 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 1486 bytes, remaining 1996 
dissect_ssl3_handshake iteration 0 type 12 offset 1576 length 412 bytes, remaining 1996 
dissect_ssl3_handshake iteration 0 type 14 offset 1992 length 0 bytes, remaining 1996

dissect_ssl enter frame #9 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 198
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 134 ssl, state 0x17
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
ssl_decrypt_pre_master_secret key 17 different from KEX_RSA(16)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 139, reported_length_remaining = 59
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 53
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48 ssl, state 0x17
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 20 offset 150 length 12947981 bytes, remaining 198

dissect_ssl enter frame #11 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 9043 found 062C9F18
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #12 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48 ssl, state 0x17
association_find: TCP port 9043 found 062C9F18
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 93 offset 5 length 5691555 bytes, remaining 53

dissect_ssl enter frame #14 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 533
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 528 ssl, state 0x17
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1997 found 00000000
association_find: TCP port 9043 found 062C9F18

dissect_ssl enter frame #16 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 421
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 416 ssl, state 0x17
association_find: TCP port 9043 found 062C9F18
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 9043 found 062C9F18

dissect_ssl enter frame #17 (first time)
  conversation = 04D31870, ssl_session = 04D31B48
  record: offset = 0, reported_length_remaining = 581
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 576 ssl, state 0x17
association_find: TCP port 1997 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1997 found 00000000
association_find: TCP port 9043 found 062C9F18

dissect_ssl enter frame #19 (first time)</code></pre></div><div id="question-tags" class="tags-container tags">websphere ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '11, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/9294bb7b1bec89e3a5cf32b0f0b7876d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GreyCon&#39;s gravatar image" /><p>GreyCon<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GreyCon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Oct '11, 13:11</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-6849" class="comments-container"></div><div id="comment-tools-6849" class="comment-tools"></div><div class="clear"></div><div id="comment-6849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6851"></span>

<div id="answer-container-6851" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6851-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that you are using a DH cipher:</p><pre><code>...
dissect_ssl3_hnd_srv_hello found CIPHER 0x0033 -&gt; state 0x17
...</code></pre><p>(cipher 0x33 = TLS_<strong>DHE</strong>_RSA_WITH_AES_128_CBC_SHA)</p><p>It is not possible to decrypt SSL sessions that use a DH cipher based on network traffic and private key. You could restrict the cipher-list on the client to make sure a (non-DH) cipher is chosen that makes it possible to decrypt.</p><p>Cheers,</p><p>Sake</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '11, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6851" class="comments-container"><span id="6853"></span><div id="comment-6853" class="comment"><div id="post-6853-score" class="comment-score"></div><div class="comment-text"><p>Dear Sake, Thank you so much for your prompt and helpful reply. I will have to learn a little more about ciphers :-)</p><p>Cheers, Con</p></div><div id="comment-6853-info" class="comment-info"><span class="comment-age">(11 Oct '11, 14:17)</span> GreyCon</div></div><span id="6854"></span><div id="comment-6854" class="comment"><div id="post-6854-score" class="comment-score"></div><div class="comment-text"><p>(converted your answer to a comment, see the FAQ for details)</p></div><div id="comment-6854-info" class="comment-info"><span class="comment-age">(11 Oct '11, 14:19)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-6851" class="comment-tools"></div><div class="clear"></div><div id="comment-6851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

