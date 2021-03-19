+++
type = "question"
title = "Problem viewing unencrypting SSL packet"
description = '''I&#x27;ve followed the guides etc, but no luck.  Here is the log: ssl_association_remove removing TCP 8443 - http handle 0000000003DC0F70 Private key imported: KeyID ea:a4:54:89:95:d5:9e:3b:41:fa:21:22:0c:e3:12:14:... ssl_init IPv4 addr &#x27;10.10.1.58&#x27; (10.10.1.58) port &#x27;8443&#x27; filename &#x27;C:&#92;applications&#92;keys...'''
date = "2012-06-08T16:15:00Z"
lastmod = "2012-06-09T02:42:00Z"
weight = 11778
keywords = [ "ssl" ]
aliases = [ "/questions/11778" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem viewing unencrypting SSL packet](/questions/11778/problem-viewing-unencrypting-ssl-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11778-score" class="post-score" title="current number of votes">0</div><span id="post-11778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've followed the guides etc, but no luck.</p><p>Here is the log:</p><pre><code>ssl_association_remove removing TCP 8443 - http handle 0000000003DC0F70
Private key imported: KeyID ea:a4:54:89:95:d5:9e:3b:41:fa:21:22:0c:e3:12:14:...
ssl_init IPv4 addr &#39;10.10.1.58&#39; (10.10.1.58) port &#39;8443&#39; filename &#39;C:\applications\keys\foo2.pkf&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\applications\keys\foo2.pkf successfully loaded.
association_add TCP port 8443 protocol http handle 0000000003DC0F70

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0000000005891D30 size 680
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 165
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 160, ssl state 0x00
association_find: TCP port 52160 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 156 bytes, remaining 165 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.10.1.58:8443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 1320
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 1315, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 1320 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0xC011
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 895 bytes, remaining 1320 
dissect_ssl3_handshake iteration 0 type 12 offset 985 length 327 bytes, remaining 1320 
dissect_ssl3_handshake iteration 0 type 14 offset 1316 length 0 bytes, remaining 1320

dissect_ssl enter frame #6 (first time)
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 122
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 70, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
dissect_ssl3_handshake wrong encrypted length (16644 max 66)
  record: offset = 75, reported_length_remaining = 47
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 36, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 25 offset 86 length 12940900 bytes, remaining 122

dissect_ssl enter frame #7 (first time)
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #8 (first time)
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 36, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 55 offset 5 length 4474236 bytes, remaining 41

dissect_ssl enter frame #10 (first time)
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 328
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 323, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 52160 found 0000000000000000
association_find: TCP port 8443 found 0000000004C71780

dissect_ssl enter frame #11 (first time)
  conversation = 0000000005891880, ssl_session = 0000000005891D30
  record: offset = 0, reported_length_remaining = 618
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 613, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 8443 found 0000000004C71780

dissect_ssl enter frame #4 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 165
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 156 bytes, remaining 165

dissect_ssl enter frame #5 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1320
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 1320 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 895 bytes, remaining 1320 
dissect_ssl3_handshake iteration 0 type 12 offset 985 length 327 bytes, remaining 1320 
dissect_ssl3_handshake iteration 0 type 14 offset 1316 length 0 bytes, remaining 1320

dissect_ssl enter frame #6 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 122
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 47
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
  record: offset = 81, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 25 offset 86 length 12940900 bytes, remaining 122

dissect_ssl enter frame #7 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #8 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 55 offset 5 length 4474236 bytes, remaining 41

dissect_ssl enter frame #10 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 328
dissect_ssl3_record: content_type 23
association_find: TCP port 52160 found 0000000000000000
association_find: TCP port 8443 found 0000000004C71780

dissect_ssl enter frame #11 (already visited)
  conversation = 0000000005891880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 618
dissect_ssl3_record: content_type 23
association_find: TCP port 8443 found 0000000004C71780</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/6bb87d03217134ce26979b4c61606d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Darren&#39;s gravatar image" /><p><span>Darren</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Darren has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '12, 18:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-11778" class="comments-container"></div><div id="comment-tools-11778" class="comment-tools"></div><div class="clear"></div><div id="comment-11778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11780"></span>

<div id="answer-container-11780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11780-score" class="post-score" title="current number of votes">1</div><span id="post-11780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The chosen cipher 0xC011 (TLS_ECDHE_RSA_WITH_RC4_128_SHA) is using a DiffieHellman key exchange. It is not possible to decrypt these sessions as the session keys are transferred with randomly generated keys, rather than the servers private key.</p><p>Please limit the accepted cipher list on either the client or the server to non-DH ciphers if you want to do decryption.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11780" class="comments-container"><span id="11784"></span><div id="comment-11784" class="comment"><div id="post-11784-score" class="comment-score"></div><div class="comment-text"><p>Excellent! I configured firefox to not use any DH cipher suites, and it all sprang into life :) It is now using: Cipher Suite: TLS_RSA_WITH_RC4_128_SHA (0x0005)</p></div><div id="comment-11784-info" class="comment-info"><span class="comment-age">(09 Jun '12, 02:42)</span> <span class="comment-user userinfo">Darren</span></div></div></div><div id="comment-tools-11780" class="comment-tools"></div><div class="clear"></div><div id="comment-11780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

