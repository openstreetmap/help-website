+++
type = "question"
title = "TLSv1 decode problem with &quot;no decoder available&quot;"
description = '''Wireshark SSL debug log as following: Wireshark SSL debug log  ssl_association_remove removing TCP 443 - http handle 000000000462E6F0 2665 bytes read PKCS#12 imported Bag 0/0: PKCS#8 Encrypted key Private key imported: KeyID 28:59:c6:a1:a4:4b:97:bf:3e:0e:6f:2a:cb:3a:65:83:... ssl_load_key: swapping ...'''
date = "2014-06-30T01:15:00Z"
lastmod = "2014-06-30T02:04:00Z"
weight = 34283
keywords = [ "tlsv1" ]
aliases = [ "/questions/34283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TLSv1 decode problem with "no decoder available"](/questions/34283/tlsv1-decode-problem-with-no-decoder-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34283-score" class="post-score" title="current number of votes">0</div><span id="post-34283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark SSL debug log as following:</p><p>Wireshark SSL debug log</p><pre><code>ssl_association_remove removing TCP 443 - http handle 000000000462E6F0
2665 bytes read
PKCS#12 imported
Bag 0/0: PKCS#8 Encrypted key
Private key imported: KeyID 28:59:c6:a1:a4:4b:97:bf:3e:0e:6f:2a:cb:3a:65:83:...
ssl_load_key: swapping p and q parameters and recomputing u
Bag 1/0: Encrypted
Bag 1/0 decrypted: Certificate
Certificate imported: sut01 &lt;&lt;ERROR&gt;&gt;, KeyID 2859c6a1a44b97bf3e0e6f2acb3a65835727c78e
ssl_init IPv4 addr &#39;192.168.253.1&#39; (192.168.253.1) port &#39;443&#39; filename &#39;C:\rpcPfxCert.pfx&#39; password(only for p12 file) &#39;123&#39;
ssl_init private key file C:\rpcPfxCert.pfx successfully loaded.
association_add TCP port 443 protocol http handle 000000000462E6F0

dissect_ssl enter frame #1 (first time)
ssl_session_init: initializing ptr 000000000615D9E0 size 688
  conversation = 000000000615D6B8, ssl_session = 000000000615D9E0
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 443 found 000000000868EFF0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000868EFF0
  record: offset = 37, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 443 found 000000000868EFF0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000868EFF0

dissect_ssl enter frame #2 (first time)
  conversation = 000000000615D6B8, ssl_session = 000000000615D9E0
  record: offset = 0, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 443 found 000000000868EFF0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000868EFF0
  record: offset = 37, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 443 found 000000000868EFF0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000868EFF0

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 000000000615E358 size 688
  conversation = 000000000615E030, ssl_session = 000000000615E358
  record: offset = 0, reported_length_remaining = 261
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 256, ssl state 0x10
association_find: TCP port 49571 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 49571 found 0000000000000000
association_find: TCP port 443 found 000000000868EFF0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '14, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/02c8bd77a8aaccc6feceefa536c578c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="james%20aichi&#39;s gravatar image" /><p><span>james aichi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="james aichi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jun '14, 02:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34283" class="comments-container"></div><div id="comment-tools-34283" class="comment-tools"></div><div class="clear"></div><div id="comment-34283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34285"></span>

<div id="answer-container-34285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34285-score" class="post-score" title="current number of votes">1</div><span id="post-34285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your capture starts immediately with Application Data records. Since the encryption of TLS packets depends on previously agreed parameters, you cannot decrypt these packets without a prior completed handshake. You will not be able to decrypt this capture.</p><p>Try getting a new capture, before actually connecting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '14, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-34285" class="comments-container"></div><div id="comment-tools-34285" class="comment-tools"></div><div class="clear"></div><div id="comment-34285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

