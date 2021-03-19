+++
type = "question"
title = "SSL decryption issue using p12 (.pfx)"
description = '''I need to capture and decrypt https traffic from my exchange server. I&#x27;ve exported the exchange server&#x27;s SSL certificate, and loaded it into wireshark under the ssl protocol, but my packets still are not being decrypted. 5.54.209.223,443,http,C:certname.pfx, (no password) Picking an example packet, ...'''
date = "2011-10-18T11:29:00Z"
lastmod = "2011-10-18T15:24:00Z"
weight = 6963
keywords = [ "ssl", "decryption", "exchange" ]
aliases = [ "/questions/6963" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decryption issue using p12 (.pfx)](/questions/6963/ssl-decryption-issue-using-p12-pfx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6963-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to capture and decrypt https traffic from my exchange server.</p><p>I've exported the exchange server's SSL certificate, and loaded it into wireshark under the ssl protocol, but my packets still are not being decrypted.</p><p>5.54.209.223,443,http,C:certname.pfx, (no password)</p><p>Picking an example packet, I've grabbed a encrypted packet from my server responding to the client (#139) packet 139 in my capture remains encrypted I can go into "Decode As" and reselect Decode and SSL, but it still does not decode the SSL encrypted data. Looking through the log file for #139 I see:</p><pre><code>dissect_ssl enter frame #139 (first time)
  conversation = 00000000058B55C0, ssl_session = 00000000058B6450
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1043, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (already visited)
  conversation = 00000000058B55C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (already visited)
  conversation = 00000000058B55C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (first time)
  conversation = 00000000058B55C0, ssl_session = 00000000058B6450
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1043, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (already visited)
  conversation = 00000000058B55C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (already visited)
  conversation = 00000000058B55C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (first time)
  conversation = 00000000058B55C0, ssl_session = 00000000058B6450
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1043, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (already visited)
  conversation = 00000000058B55C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 000000000475A330

dissect_ssl enter frame #139 (already visited)
  conversation = 00000000058B55C0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 000000000475A330</code></pre><p>As you can see, wireshark finds an association, but fails to find a decoder. I know it's the correct SSL certificate.</p><p>Any Ideas?</p></div><div id="question-tags" class="tags-container tags">ssl decryption exchange</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '11, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/dec9d72c33be3bff4921838b17f9a736?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cabal&#39;s gravatar image" /><p>cabal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cabal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '11, 15:08</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-6963" class="comments-container"></div><div id="comment-tools-6963" class="comment-tools"></div><div class="clear"></div><div id="comment-6963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6969"></span>

<div id="answer-container-6969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6969-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to look at the whole establishment. Probably a Diffie-Hellman cipher. Check for <code>dissect_ssl3_hnd_srv_hello found CIPHER 0x0033 -&gt; state 0x17</code> in your log. DH cipher can't be decoded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6969" class="comments-container"><span id="6971"></span><div id="comment-6971" class="comment"><div id="post-6971-score" class="comment-score"></div><div class="comment-text"><p>I'm using cipher 0x0005 I'm not sure which cipher this represents, but I do see this in the log:</p><pre><code>dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 86, reported_length_remaining = 71
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 65
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 30 offset 97 length 3627431 bytes, remaining 157</code></pre><p>Perhaps I can reconfigure the client browser to list only ciphers wireshark can decrypt? Does anyone have a list of what ciphers wireshark can decrypt?</p></div><div id="comment-6971-info" class="comment-info"><span class="comment-age">(18 Oct '11, 14:33)</span> cabal</div></div><span id="6972"></span><div id="comment-6972" class="comment"><div id="post-6972-score" class="comment-score"></div><div class="comment-text"><p>OK, I changed the allowable SSL ciphers on the server too:</p><pre><code>TLS_RSA_WITH_AES_128_CBC_SHA
TLS_RSA_WITH_AES_256_CBC_SHA
TLS_RSA_WITH_RC4_128_SHA
TLS_RSA_WITH_3DES_EDE_CBC_SHA
TLS_RSA_WITH_RC4_128_MD5
SSL_CK_RC4_128_WITH_MD5
SSL_CK_DES_192_EDE3_CBC_WITH_MD5
TLS_RSA_WITH_NULL_SHA
TLS_RSA_WITH_NULL_MD5
TLS_RSA_WITH_AES_128_CBC_SHA256
TLS_RSA_WITH_AES_256_CBC_SHA256
TLS_RSA_WITH_NULL_SHA256</code></pre><p>None of these should be Diffie-Helman</p><p>I still can't decode packets:</p><pre><code>dissect_ssl enter frame #577 (first time)
  conversation = 0000000005B67290, ssl_session = 0000000005B67FB0
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1043, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004A0A300

dissect_ssl enter frame #577 (already visited)
  conversation = 0000000005B67290, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000004A0A300

dissect_ssl enter frame #577 (first time)
  conversation = 0000000005B67290, ssl_session = 0000000005B67FB0
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1043, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004A0A300

dissect_ssl enter frame #577 (already visited)
  conversation = 0000000005B67290, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1048
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000004A0A300</code></pre><p>Any Ideas?</p></div><div id="comment-6972-info" class="comment-info"><span class="comment-age">(18 Oct '11, 15:01)</span> cabal</div></div><span id="6973"></span><div id="comment-6973" class="comment"><div id="post-6973-score" class="comment-score"></div><div class="comment-text"><p>(converted your answers to comments as they seem to address Jaap's answer, please see the FAQ for details)</p></div><div id="comment-6973-info" class="comment-info"><span class="comment-age">(18 Oct '11, 15:15)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-6969" class="comment-tools"></div><div class="clear"></div><div id="comment-6969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6974"></span>

<div id="answer-container-6974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6974-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a few things you need to take into account when decrypting SSL traffic.</p><p>First of all the key must be in PEM format or PKCS12 (with or without password). Did your ssl-debug file state that the key was successfully loaded?</p><p>Next, the full SSL handshake needs to be present in the trace so that the proper keys can be extracted. A reused SSL session (with a short handshake) does not provide the keying material and can therefor only be decrypted when the original full handshake is also present in the tracefile.</p><p>Then, as Jaap mentioned, when a DH cipher is used, the keying material is exchanged using the Diffie Hellman protocol which uses dynamically created keypairs instead of the server's public and private key. Therefor Wireshark is not able to decrypt these sessions.</p><p>Now to your issue. Please check whether the certificate is loaded successfully. Then check whether the full SSL handshake is present in your tracefile. It thsi does not solve your issue, it would help to see the full ssl-debug log.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6974" class="comments-container"></div><div id="comment-tools-6974" class="comment-tools"></div><div class="clear"></div><div id="comment-6974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

