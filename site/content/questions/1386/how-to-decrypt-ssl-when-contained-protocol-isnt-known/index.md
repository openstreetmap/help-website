+++
type = "question"
title = "How to decrypt SSL when contained protocol isn&#x27;t known?"
description = '''I&#x27;m using wireshark to inspect and hopefully decrypt a connection; the encrypted protocol details aren&#x27;t known. I&#x27;ve set up SSL decryption as instructed at http://wiki.wireshark.org/SSL, but I&#x27;m not sure how significant the specification of the embedded protocol is. I tried something like: x.x.x.x,4...'''
date = "2010-12-17T11:59:00Z"
lastmod = "2010-12-17T17:00:00Z"
weight = 1386
keywords = [ "ssl" ]
aliases = [ "/questions/1386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt SSL when contained protocol isn't known?](/questions/1386/how-to-decrypt-ssl-when-contained-protocol-isnt-known)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1386-score" class="post-score" title="current number of votes">0</div><span id="post-1386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark to inspect and hopefully decrypt a connection; the encrypted protocol details aren't known. I've set up SSL decryption as instructed at http://wiki.wireshark.org/SSL, but I'm not sure how significant the specification of the embedded protocol is. I tried something like:</p><p>x.x.x.x,4001,Data,c:cp.pem or x.x.x.x,4001,http,c:cp.pem</p><p>but in both cases wireshark doesn't show me any decrypted data.</p><p>I logged to the SSL debug file, below...</p><pre><code>ssl_association_remove removing TCP 0 - http handle 044D9EA0
ssl_init keys string:
x.x.x.x,25472,http,c:\cp.pem
ssl_init found host entry x.x.x.x,25472,http,c:\cp.pem
ssl_init addr &#39;x.x.x.x&#39; port &#39;25472&#39; filename &#39;c:\cp.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID ef:bc:76:41:d5:1b:8d:a4:c1:0a:fa:80:a1:05:bc:30:...
ssl_init private key file c:\cp.pem successfully loaded
association_add TCP port 25472 protocol http handle 044D9EA0

dissect_ssl enter frame #1 (first time)
ssl_session_init: initializing ptr 06161A30 size 584
  conversation = 06161868, ssl_session = 06161A30
  record: offset = 0, reported_length_remaining = 1

dissect_ssl enter frame #3 (first time)
  conversation = 06161868, ssl_session = 06161A30
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record found version 0x0300 -&gt; state 0x10
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 55036 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 55036 found 00000000
association_find: TCP port 25472 found 05CAC010
  record: offset = 37, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 64, ssl state 0x10
association_find: TCP port 55036 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 55036 found 00000000
association_find: TCP port 25472 found 05CAC010

dissect_ssl enter frame #4 (first time)
  conversation = 06161868, ssl_session = 06161A30
  record: offset = 0, reported_length_remaining = 1
  need_desegmentation: offset = 0, reported_length_remaining = 1

dissect_ssl enter frame #6 (first time)
  conversation = 06161868, ssl_session = 06161A30
  record: offset = 0, reported_length_remaining = 106
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 55036 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 55036 found 00000000
association_find: TCP port 25472 found 05CAC010
  record: offset = 37, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 64, ssl state 0x10
association_find: TCP port 55036 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 55036 found 00000000
association_find: TCP port 25472 found 05CAC010

dissect_ssl enter frame #14 (first time)
ssl_session_init: initializing ptr 0616259C size 584
  conversation = 06162258, ssl_session = 0616259C
  record: offset = 0, reported_length_remaining = 72
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 67, ssl state 0x00
association_find: TCP port 55148 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 63 bytes, remaining 72 
packet_from_server: is from server - FALSE
ssl_find_private_key server x.x.x.x:25472
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #27 (first time)
  conversation = 06162258, ssl_session = 0616259C
  record: offset = 0, reported_length_remaining = 1460
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0035 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1381
  need_desegmentation: offset = 79, reported_length_remaining = 1381

dissect_ssl enter frame #28 (first time)
  conversation = 06162258, ssl_session = 0616259C
  record: offset = 0, reported_length_remaining = 1877
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 1854, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 1850 bytes, remaining 1859 
  record: offset = 1859, reported_length_remaining = 18
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 13, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 1864 length 5 bytes, remaining 1877 
dissect_ssl3_handshake iteration 0 type 14 offset 1873 length 0 bytes, remaining 1877

dissect_ssl enter frame #30 (first time)
  conversation = 06162258, ssl_session = 0616259C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #31 (first time)
  conversation = 06162258, ssl_session = 0616259C
  record: offset = 0, reported_length_remaining = 2498
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 1886, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 1882 bytes, remaining 1891 
  record: offset = 1891, reported_length_remaining = 607
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 260, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 1896 length 256 bytes, remaining 2156 
pre master encrypted[256]:
97 09 d7 2f d8 da 1d 3f 60 55 d5 fa 95 e0 1b 94 
dd f6 48 4b 0c 82 aa 2f f2 b0 5e 7d a0 60 b8 2c 
30 54 4d 26 d1 a8 3a fc 00 87 fa bd a3 0e 73 b0 
35 34 65 09 30 8b 60 67 77 5a 24 76 9b 12 d1 91 
75 80 f9 09 af f3 1c 24 64 df d1 43 10 90 63 b6 
44 3c 03 0d a5 81 6d 3f 29 7f 25 0e 19 83 f8 5e 
25 9e 6c c1 f8 18 25 ab f0 7e e8 aa 50 29 22 1a 
94 bf 32 f2 a3 4f a9 44 6e 96 10 13 c7 31 7e 7a 
cc d2 6d e6 f2 24 ee 59 d9 bf 08 86 2f fe 2d 79 
6a 94 0c 51 65 75 f6 ec 1d 18 bd 8f c7 90 ec d9 
08 f5 f6 a7 9e 56 42 8f 28 7e 4c c1 00 d4 0e 34 
6d 60 7c 74 33 09 2f d9 74 d2 e5 32 b0 ae ce 25 
f3 eb 55 78 e9 c5 e9 61 64 89 9b f3 5d 62 aa 1c 
88 6a 6d 30 71 1c 1b 17 00 42 6b 12 9b 0f 56 90 
5f d7 98 5e a6 27 94 2a 25 ab 95 3c d2 ec 5f 07 
1e dd ee 8c e6 ae 8d e2 c7 da 84 06 14 49 1c c2 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 211 bytes, decr_len 256
decrypted_unstrip_pre_master[256]:
03 1f 7d de 96 11 d5 0e ee 86 c6 87 b8 d8 44 69 
61 06 d3 1f 36 57 87 22 58 60 3f b5 08 e9 37 6e 
08 15 39 e1 9b d8 24 b2 b7 61 c3 15 51 cc 2a 6b 
65 ce 89 d9 59 28 a0 f6 a9 24 70 f9 35 77 c2 07 
a1 66 49 11 0c 1c 0b 1a 4e eb ac 14 91 95 4f 77 
9f 07 45 09 cc 69 55 c3 19 9a d7 92 bc 02 45 bc 
6d 42 59 fd 7a ed c3 07 35 20 05 a3 35 3c d1 35 
03 bd a8 68 89 31 50 24 28 2f db 5f 20 26 6e 0d 
82 6d 93 fe b3 c1 fb b4 4d 9d 3a 8c 9e d1 5b 81 
19 8a 93 16 ab 6e 6f 56 59 cb 99 14 46 6d 1a 18 
0b 72 a7 c7 cd f7 6c 62 42 b5 bb d5 6c 65 0a 19 
0e 44 38 b7 03 90 07 c9 2b 81 a1 03 4f 55 fa ec 
71 ec 70 c6 76 0d 80 36 6d 88 06 88 8c 45 83 6d 
72 77 00 5b fc 83 fd 54 75 32 b8 99 89 6e c5 02 
f4 12 67 2a 4e ba 0d 09 63 f5 f7 5b 54 f1 6d 87 
21 ea 25 a0 8f 24 1b 6a 0a c7 7c 72 74 6f a8 65 
ssl_decrypt_pre_master_secret wrong pre_master_secret length (45, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 2156, reported_length_remaining = 342
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 262, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 15 offset 2161 length 258 bytes, remaining 2423 
  record: offset = 2423, reported_length_remaining = 75
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 2429, reported_length_remaining = 69
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 64, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 6 offset 2434 length 4099005 bytes, remaining 2498</code></pre><p>(rest of ssl debug output deleted by SYNbit to enhance readability)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '10, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/2a39aed820c125e6db9826fa8180043f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dwhsix&#39;s gravatar image" /><p><span>dwhsix</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dwhsix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Dec '10, 00:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-1386" class="comments-container"></div><div id="comment-tools-1386" class="comment-tools"></div><div class="clear"></div><div id="comment-1386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1387"></span>

<div id="answer-container-1387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1387-score" class="post-score" title="current number of votes">2</div><span id="post-1387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the protocol that is encrypted by SSL is unknown, it's best to use the "data" dissector. The ssl keys list will become something like:</p><pre><code>1.1.1.1,1234,data,/tmp/server.key</code></pre><p>Regarding your session not being decrypted, it looks like the private key does not match the certificate. This is a usual cause for the following extract from your ssl-debug log:</p><pre><code>ssl_decrypt_pre_master_secret wrong pre_master_secret length (45, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret</code></pre><p>Please have a look at the presentation (<a href="https://www.cacetech.com/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">powerpoint</a> or <a href="http://www.lovemytool.com/blog/2009/06/sake_blok_11.html">video</a>) I gave at Sharkfest'09 about troubleshooting SSL for further information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '10, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1387" class="comments-container"><span id="1388"></span><div id="comment-1388" class="comment"><div id="post-1388-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I suspect that's probably the case and I wondered if that's what that debug entry meant.</p><p>A little puzzled, because I'm pretty sure it's the correct private key. But obviously not... I'll dig a little more.</p><p>Thanks!</p></div><div id="comment-1388-info" class="comment-info"><span class="comment-age">(17 Dec '10, 13:54)</span> <span class="comment-user userinfo">dwhsix</span></div></div><span id="1390"></span><div id="comment-1390" class="comment"><div id="post-1390-score" class="comment-score"></div><div class="comment-text"><p>In my presentation I show how you can check if the two match... :-)</p></div><div id="comment-1390-info" class="comment-info"><span class="comment-age">(17 Dec '10, 17:00)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-1387" class="comment-tools"></div><div class="clear"></div><div id="comment-1387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

