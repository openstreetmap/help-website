+++
type = "question"
title = "Unable to decrypt SSL sessions in wireshark"
description = '''I am not able to decrypt SSL sessions in Wireshark. Does anyone know what is wrong? Thanks for any assistance. Here is the debug output: ssl_init private key file B:&#92;downloads&#92;certs&#92;server1-rsa.key successfully loaded. association_add TCP port 443 protocol http handle 059E54D0  dissect_ssl enter fra...'''
date = "2014-05-09T10:56:00Z"
lastmod = "2014-05-09T11:02:00Z"
weight = 32668
keywords = [ "wireshark" ]
aliases = [ "/questions/32668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt SSL sessions in wireshark](/questions/32668/unable-to-decrypt-ssl-sessions-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32668-score" class="post-score" title="current number of votes">0</div><span id="post-32668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not able to decrypt SSL sessions in Wireshark. Does anyone know what is wrong? Thanks for any assistance.</p><p>Here is the debug output:</p><pre><code>ssl_init private key file B:\downloads\certs\server1-rsa.key successfully loaded.
association_add TCP port 443 protocol http handle 059E54D0

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 06571BC4 size 588
  conversation = 06571838, ssl_session = 06571BC4
  record: offset = 0, reported_length_remaining = 177
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 172, ssl state 0x00
association_find: TCP port 34237 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 168 bytes, remaining 177 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.168.136:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #5 (first time)
  conversation = 06571838, ssl_session = 06571BC4
  record: offset = 0, reported_length_remaining = 1024
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 57, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 53 bytes, remaining 62 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0xC014
  record: offset = 62, reported_length_remaining = 962
  need_desegmentation: offset = 62, reported_length_remaining = 962

dissect_ssl enter frame #7 (first time)
  conversation = 06571838, ssl_session = 06571BC4
  record: offset = 0, reported_length_remaining = 2422
  need_desegmentation: offset = 0, reported_length_remaining = 2422

dissect_ssl enter frame #9 (first time)
  conversation = 06571838, ssl_session = 06571BC4
  record: offset = 0, reported_length_remaining = 3559
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 3554, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3550 bytes, remaining 3559 

dissect_ssl enter frame #11 (first time)
  conversation = 06571838, ssl_session = 06571BC4
  record: offset = 0, reported_length_remaining = 679
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 655, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 5 length 651 bytes, remaining 660 
  record: offset = 660, reported_length_remaining = 19
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 14, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 13 offset 665 length 6 bytes, remaining 679 
dissect_ssl3_handshake iteration 0 type 14 offset 675 length 0 bytes, remaining 679 

dissect_ssl enter frame #13 (first time)
  conversation = 06571838, ssl_session = 06571BC4
  record: offset = 0, reported_length_remaining = 214
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 7, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 12 
  record: offset = 12, reported_length_remaining = 202
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 138, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 17 length 134 bytes, remaining 155 
dissect_ssl3_handshake wrong encrypted length (34052 max 134)
  record: offset = 155, reported_length_remaining = 59
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 161, reported_length_remaining = 53
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48, ssl state 0x13
packet_from_server: is from server - FALSE
decrypt_ssl3_</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '14, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/48f35d438f777b73b548eff5f2d61778?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchen&#39;s gravatar image" /><p><span>lchen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '14, 11:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-32668" class="comments-container"></div><div id="comment-tools-32668" class="comment-tools"></div><div class="clear"></div><div id="comment-32668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32670"></span>

<div id="answer-container-32670" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32670-score" class="post-score" title="current number of votes">0</div><span id="post-32670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>dissect_ssl3_hnd_srv_hello <strong>can't find cipher suite 0xC014</strong></p></blockquote><p>Your version of Wireshark does not know how to decrypt <strong>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (cipher suite 0xc014)</strong>.</p><p>Only the latest development version (1.11.x) is able to handle that cipher. Please download that and try it again.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32670" class="comments-container"></div><div id="comment-tools-32670" class="comment-tools"></div><div class="clear"></div><div id="comment-32670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

