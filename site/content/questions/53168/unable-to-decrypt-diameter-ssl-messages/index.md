+++
type = "question"
title = "Unable to decrypt diameter SSL messages."
description = '''Hi everyone, I am unable to decrypt the SSL diameter based messages on wireshark even after adding the server.key in RSK key field. This is my ssl debug log. Wireshark SSL debug log  Wireshark version: 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) GnuTLS version: 3.2.15 Libgcrypt version: 1.6.2 ssl_asso...'''
date = "2016-06-03T02:36:00Z"
lastmod = "2016-06-08T03:43:00Z"
weight = 53168
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/53168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt diameter SSL messages.](/questions/53168/unable-to-decrypt-diameter-ssl-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53168-score" class="post-score" title="current number of votes">0</div><span id="post-53168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I am unable to decrypt the SSL diameter based messages on wireshark even after adding the server.key in RSK key field. This is my ssl debug log.</p><p>Wireshark SSL debug log</p><p>Wireshark version: 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) GnuTLS version: 3.2.15 Libgcrypt version: 1.6.2</p><pre><code>ssl_association_remove removing TCP 3869 - diameter handle 00000000059A7E80
KeyID[20]:
| d2 4a 15 8f b6 90 86 a1 2b 8b 64 6d c6 2c 42 8d |.J......+.dm.,B.|
| 55 bf 89 04                                     |U...            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file C:/Users/rprasad/Documents/server.key successfully loaded.
ssl_init port &#39;3869&#39; filename &#39;C:/Users/rprasad/Documents/server.key&#39; password(only for p12 file) &#39;&#39;
association_add TCP port 3869 protocol ssl handle 00000000059F6010

dissect_ssl enter frame #1575 (first time)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 00000000082F3970
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 128, ssl state 0x10
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 3869 found 0000000006F5B280

dissect_ssl enter frame #1577 (first time)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 00000000082F3970
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 144, ssl state 0x10
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #2884 (first time)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 00000000082F3970
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 304, ssl state 0x10
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #2888 (first time)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 00000000082F3970
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 800, ssl state 0x10
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1577 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2884 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2888 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1577 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2884 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2888 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1577 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2884 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2888 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1577 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2884 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2888 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1575 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1577 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2884 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 309
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #2888 (already visited)
association_find: TCP port 3869 found 0000000006F5B280
packet_from_server: is from server - TRUE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 805
dissect_ssl3_record: content_type 23 Application Data

dissect_ssl enter frame #1577 (already visited)
association_find: TCP port 6551 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 00000000082F34A0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 149
dissect_ssl3_record: content_type 23 Application Data</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/1345786bf19e3dd881cc9962f31f33e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M%20Roshan%20Prasad&#39;s gravatar image" /><p><span>M Roshan Prasad</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M Roshan Prasad has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jun '16, 02:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53168" class="comments-container"><span id="53176"></span><div id="comment-53176" class="comment"><div id="post-53176-score" class="comment-score"></div><div class="comment-text"><p>Can you post the capture file someplace accessible--e.g., <a href="http://cloudshark.org">cloudshark.org</a>? We'll need to see the start of the TLS session, especially the "server hello" message.</p><p>Also, is the above the complete start of the log? It seems that the first few messages aren't about the TLS setup.</p></div><div id="comment-53176-info" class="comment-info"><span class="comment-age">(03 Jun '16, 06:16)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-53168" class="comment-tools"></div><div class="clear"></div><div id="comment-53168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53184"></span>

<div id="answer-container-53184" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53184-score" class="post-score" title="current number of votes">0</div><span id="post-53184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JeffMorriss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Jeff, I re created the RSA key and added the same in Wireshark and it looks to be working fine now. Thank you..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/1345786bf19e3dd881cc9962f31f33e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M%20Roshan%20Prasad&#39;s gravatar image" /><p><span>M Roshan Prasad</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M Roshan Prasad has one accepted answer">100%</span></p></div></div><div id="comments-container-53184" class="comments-container"><span id="53187"></span><div id="comment-53187" class="comment"><div id="post-53187-score" class="comment-score"></div><div class="comment-text"><p>Great. I'll Accept your answer so that your question will show up as having been answered--see the FAQ for details.</p></div><div id="comment-53187-info" class="comment-info"><span class="comment-age">(03 Jun '16, 13:00)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="53308"></span><div id="comment-53308" class="comment"><div id="post-53308-score" class="comment-score"></div><div class="comment-text"><p>Hello Jeff. Looks like my wire shark is able to do a follow SSL stream only when there is a start of the TLS session, with "server hello" message and certificate exchange messages.</p></div><div id="comment-53308-info" class="comment-info"><span class="comment-age">(08 Jun '16, 03:09)</span> <span class="comment-user userinfo">M Roshan Prasad</span></div></div><span id="53309"></span><div id="comment-53309" class="comment"><div id="post-53309-score" class="comment-score"></div><div class="comment-text"><p>and the next consecutive messages i am not able to do the Follow SSL stream.</p></div><div id="comment-53309-info" class="comment-info"><span class="comment-age">(08 Jun '16, 03:10)</span> <span class="comment-user userinfo">M Roshan Prasad</span></div></div><span id="53310"></span><div id="comment-53310" class="comment"><div id="post-53310-score" class="comment-score"></div><div class="comment-text"><p>i have uploaded the same in cloudshark.org, the one with Server Hello you can find in <a href="https://www.cloudshark.org/captures/4baddb1bc4fa">https://www.cloudshark.org/captures/4baddb1bc4fa</a> and the next consecutive where i am not able to do a Follow SSL Stream is in <a href="https://www.cloudshark.org/captures/1c0406a67f7c.">https://www.cloudshark.org/captures/1c0406a67f7c.</a> Please help me with this</p></div><div id="comment-53310-info" class="comment-info"><span class="comment-age">(08 Jun '16, 03:15)</span> <span class="comment-user userinfo">M Roshan Prasad</span></div></div><span id="53311"></span><div id="comment-53311" class="comment"><div id="post-53311-score" class="comment-score"></div><div class="comment-text"><p>Like any of the <a href="https://packetpushers.net/using-wireshark-to-decode-ssltls-packets/">tutorials</a> or <a href="https://ask.wireshark.org/questions/24488/decrypt-ssl">answers</a>, will tell you</p><pre><code>Important: The capture must include the initial SSL/TLS session establishment. In other words, the CLIENTHELLO and SERVERHELLO exchange. Beware captures taken where a session has been resumed. Ideally, ensure any capture either a) is of packets related to an entirely new device connecting or b) where a device that has already previously established a session is used, it is used after a considerable time after the last session was established.</code></pre></div><div id="comment-53311-info" class="comment-info"><span class="comment-age">(08 Jun '16, 03:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53184" class="comment-tools"></div><div class="clear"></div><div id="comment-53184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

