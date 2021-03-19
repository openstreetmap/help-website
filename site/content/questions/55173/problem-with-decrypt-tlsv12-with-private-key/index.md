+++
type = "question"
title = "Problem with decrypt TLSv1.2 with private key"
description = '''Traffic is successfully decrypted on computer where traces were collected, but I can&#x27;t decrypt the same traces on another computer. I use the same pem key on both computers. dissect_ssl enter frame #340 (first time) packet_from_server: is from server - TRUE  conversation = 000000000B217470, ssl_sess...'''
date = "2016-08-29T11:07:00Z"
lastmod = "2016-08-29T11:07:00Z"
weight = 55173
keywords = [ "tlsv1.2" ]
aliases = [ "/questions/55173" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with decrypt TLSv1.2 with private key](/questions/55173/problem-with-decrypt-tlsv12-with-private-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55173-score" class="post-score" title="current number of votes">0</div><span id="post-55173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Traffic is successfully decrypted on computer where traces were collected, but I can't decrypt the same traces on another computer. I use the same pem key on both computers.</p><pre><code>dissect_ssl enter frame #340 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000B217470, ssl_session = 000000000B2181B0
  record: offset = 0, reported_length_remaining = 142
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 86
decrypt_ssl3_record: app_data len 86, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 82 bytes, remaining 91 
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0x009D TLS_RSA_WITH_AES_256_GCM_SHA384 -&gt; state 0x17
  record: offset = 91, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
ssl_dissect_change_cipher_spec Session resumption using Session Ticket
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t find master secret by Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 97, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 102 40
decrypt_ssl3_record: app_data len 40, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 242 offset 102 length 10155291 bytes, remaining 142</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tlsv1.2" rel="tag" title="see questions tagged &#39;tlsv1.2&#39;">tlsv1.2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/aff1dd3119968bf75edb77eae62f22e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pavelnt&#39;s gravatar image" /><p><span>pavelnt</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pavelnt has no accepted answers">0%</span></p></div></div><div id="comments-container-55173" class="comments-container"></div><div id="comment-tools-55173" class="comment-tools"></div><div class="clear"></div><div id="comment-55173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

