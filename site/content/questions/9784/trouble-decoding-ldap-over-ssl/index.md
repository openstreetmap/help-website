+++
type = "question"
title = "Trouble decoding LDAP over SSL"
description = '''I&#x27;m trying to decode LDAP traffic over SSL to troubleshoot an issue we&#x27;re having. I&#x27;ve setup the SSL protocol properties with the PFX file that has the private key in it and I&#x27;ve decoded both source 636 and dest 636 as LDAP, but it never wants to actually decode anything and just leaves everything a...'''
date = "2012-03-27T06:55:00Z"
lastmod = "2012-03-27T07:38:00Z"
weight = 9784
keywords = [ "decode", "ssl", "ldap" ]
aliases = [ "/questions/9784" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trouble decoding LDAP over SSL](/questions/9784/trouble-decoding-ldap-over-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9784-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decode LDAP traffic over SSL to troubleshoot an issue we're having. I've setup the SSL protocol properties with the PFX file that has the private key in it and I've decoded both source 636 and dest 636 as LDAP, but it never wants to actually decode anything and just leaves everything as TCP. I'm running Wireshark 1.6.5. I know that I've done this in the past with an earlier version of Wireshark. If I leave it un-decoded, it'll show the data packets as TLSv1 and indicate that there is encrypted LDAP traffic in the packet, so I'm not sure what the deal is, but I'm obviously missing something.</p><p>Edit: debug file moved from "answer" to question:</p><pre><code>ssl_association_remove removing TCP 636 - ldap handle 0000000003DAB350
ssl_init keys string:
1.1.1.1,636,ldap,c:\\server.pem
ssl_init found host entry 1.1.1.1,636,ldap,c:\\server.pem
ssl_init addr &#39;1.1.1.1&#39; port &#39;636&#39; filename &#39;c:\\server.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID 08:c7:ea:d2:...
ssl_init private key file c:\\server.pem successfully loaded
association_add TCP port 636 protocol ldap handle 0000000003DAB350

dissect_ssl enter frame #3 (first time)
ssl_session_init: initializing ptr 00000000086A1F48 size 672
  conversation = 00000000086A1CE8, ssl_session = 00000000086A1F48
  record: offset = 0, reported_length_remaining = 133
dissect_ssl3_record found version 0x0301 -&gt; state 0x10
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 128, ssl state 0x10
association_find: TCP port 65250 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 65250 found 0000000000000000
association_find: TCP port 636 found 000000004E9C5230

dissect_ssl enter frame #4 (first time)
  conversation = 00000000086A1CE8, ssl_session = 00000000086A1F48
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 48, ssl state 0x10
association_find: TCP port 636 found 000000004E9C5230
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 636 found 000000004E9C5230</code></pre></div><div id="question-tags" class="tags-container tags">decode ssl ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '12, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/8c9cbc025922240dfd5cb3e1a65d00fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="infinity9999&#39;s gravatar image" /><p>infinity9999<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="infinity9999 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '12, 08:49</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9784" class="comments-container"></div><div id="comment-tools-9784" class="comment-tools"></div><div class="clear"></div><div id="comment-9784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9785"></span>

<div id="answer-container-9785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you reviewed the <a href="http://wiki.wireshark.org/SSL">SSL</a> page on the wiki? That states that the key should be in PEM format and gives some conversion recipes, and also discusses LDAP but I don't think that info is applicable in your case.</p><p>Using the SSL dissector preferences you can also set an SSL Debug file. Doing that and posting the contents here may help us to answer your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '12, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9785" class="comments-container"><span id="9786"></span><div id="comment-9786" class="comment"><div id="post-9786-score" class="comment-score"></div><div class="comment-text"><p>Yes, I've read it. I've tried both PEM and PFX (1.6.5 allows PFX or P12 with the password). I just tried with 1.4.11 and that didn't work either.<br />
</p><p>The debug shows this (snippet from the top), which appears to me to be working as it should (i.e. it can read in the key and appears to be able to figure out which packets to dissect):</p><p>ssl_association_remove removing TCP 636 - ldap handle 0000000003DAB350 ssl_init keys string: 1.1.1.1,636,ldap,c:\server.pem ssl_init found host entry 1.1.1.1,636,ldap,c:\server.pem ssl_init addr '1.1.1.1' port '636' filename 'c:\server.pem' password(only for p12 file) '(null)' Private key imported: KeyID 08:c7:ea:d2:... ssl_init private key file c:\server.pem successfully loaded association_add TCP port 636 protocol ldap handle 0000000003DAB350</p><p>dissect_ssl enter frame #3 (first time) ssl_session_init: initializing ptr 00000000086A1F48 size 672 conversation = 00000000086A1CE8, ssl_session = 00000000086A1F48 record: offset = 0, reported_length_remaining = 133 dissect_ssl3_record found version 0x0301 -&gt; state 0x10 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 128, ssl state 0x10 association_find: TCP port 65250 found 0000000000000000 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available association_find: TCP port 65250 found 0000000000000000 association_find: TCP port 636 found 000000004E9C5230</p><p>dissect_ssl enter frame #4 (first time) conversation = 00000000086A1CE8, ssl_session = 00000000086A1F48 record: offset = 0, reported_length_remaining = 53 dissect_ssl3_record: content_type 23 decrypt_ssl3_record: app_data len 48, ssl state 0x10 association_find: TCP port 636 found 000000004E9C5230 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available association_find: TCP port 636 found 000000004E9C5230</p></div><div id="comment-9786-info" class="comment-info"><span class="comment-age">(27 Mar '12, 08:34)</span> infinity9999</div></div><span id="9787"></span><div id="comment-9787" class="comment"><div id="post-9787-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment and (due to the comment length limits) copied the debug output into the question and formatted it as "code".</p></div><div id="comment-9787-info" class="comment-info"><span class="comment-age">(27 Mar '12, 08:51)</span> grahamb ♦</div></div><span id="9788"></span><div id="comment-9788" class="comment"><div id="post-9788-score" class="comment-score"></div><div class="comment-text"><p>I'm wondering if it's becuase I'm not seeing the SSL handshake in my trace. Does the handshake need to be in the trace for it to actually decode things?</p></div><div id="comment-9788-info" class="comment-info"><span class="comment-age">(27 Mar '12, 09:20)</span> infinity9999</div></div><span id="9789"></span><div id="comment-9789" class="comment"><div id="post-9789-score" class="comment-score"></div><div class="comment-text"><p>Yes. That is where the session key is derived from the master key to use during the subsequent data exchanges.</p></div><div id="comment-9789-info" class="comment-info"><span class="comment-age">(27 Mar '12, 09:24)</span> grahamb ♦</div></div><span id="9790"></span><div id="comment-9790" class="comment not_top_scorer"><div id="post-9790-score" class="comment-score"></div><div class="comment-text"><p>I'm looking in my trace and I do see handshakes occuring. Do I need to decode things from the handshake packet itself? I thought you could just decode from any packet that was talking on that port.</p></div><div id="comment-9790-info" class="comment-info"><span class="comment-age">(27 Mar '12, 09:28)</span> infinity9999</div></div><span id="9791"></span><div id="comment-9791" class="comment not_top_scorer"><div id="post-9791-score" class="comment-score"></div><div class="comment-text"><p>Does it make a difference that it's LDAP against Active Directory?</p></div><div id="comment-9791-info" class="comment-info"><span class="comment-age">(27 Mar '12, 09:40)</span> infinity9999</div></div><span id="9792"></span><div id="comment-9792" class="comment not_top_scorer"><div id="post-9792-score" class="comment-score"></div><div class="comment-text"><p>Re needing the handshake. Yes that must be present in the trace. What do you mean by "decode from the handshake packet itself"? The debug log should show the info from the handshakes and the calculation of the session key.</p><p>Re LDAP against AD. Not that I know of.</p></div><div id="comment-9792-info" class="comment-info"><span class="comment-age">(27 Mar '12, 09:49)</span> grahamb ♦</div></div><span id="9793"></span><div id="comment-9793" class="comment not_top_scorer"><div id="post-9793-score" class="comment-score"></div><div class="comment-text"><p>See also <a href="http://ask.wireshark.org/questions/7886/ssl-decrypting-problem">this</a> question which was also about AD LDAP over SSL. They had issues with the key exchange cipher that prevented decryption.</p></div><div id="comment-9793-info" class="comment-info"><span class="comment-age">(27 Mar '12, 09:58)</span> grahamb ♦</div></div><span id="9794"></span><div id="comment-9794" class="comment not_top_scorer"><div id="post-9794-score" class="comment-score"></div><div class="comment-text"><p>I do show this in the debug log, but the packet says it's using Cipher Suite TLS_RSA_WITH_AES_128_CBC_SHA (0x002f):</p><pre><code>    dissect_ssl enter frame #172799 (first time)
  conversation = 000000000D954BE8, ssl_session = 000000000D9550B0
  record: offset = 0, reported_length_remaining = 145
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x002F -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 86, reported_length_remaining = 59
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 53
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 254 offset 97 length 16114481 bytes, remaining 145 </code></pre></div><div id="comment-9794-info" class="comment-info"><span class="comment-age">(27 Mar '12, 10:59)</span> infinity9999</div></div><span id="9795"></span><div id="comment-9795" class="comment not_top_scorer"><div id="post-9795-score" class="comment-score"></div><div class="comment-text"><p>Also, re: the decode packet, disregard that. That was part of a doc that we had used that described decrypting SSL on non-standard ports. My brain hasn't been all there recently.</p></div><div id="comment-9795-info" class="comment-info"><span class="comment-age">(27 Mar '12, 11:08)</span> infinity9999</div></div><span id="9796"></span><div id="comment-9796" class="comment not_top_scorer"><div id="post-9796-score" class="comment-score"></div><div class="comment-text"><p>That is the first part of the key exchange that has the server hello and certificate, the next part is the client key exchange, the change cipher spec and handshake finished. That is the key frame you need to inspect in the debug log.</p><p>The snakeoil demo on the SSL wiki page uses TLS_RSA_WITH_AES_256_CBC_SHA (0x0035) which is stronger than you are using, so no worries there.</p><p>You need to inspect (or post) the next part of the debug log that shows the session key generation.</p></div><div id="comment-9796-info" class="comment-info"><span class="comment-age">(27 Mar '12, 13:45)</span> grahamb ♦</div></div><span id="9797"></span><div id="comment-9797" class="comment not_top_scorer"><div id="post-9797-score" class="comment-score"></div><div class="comment-text"><pre><code>dissect_ssl enter frame #172811 (first time)
  conversation = 000000000D954BE8, ssl_session = 000000000D9550B0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #172812 (first time)
  conversation = 000000000D954BE8, ssl_session = 000000000D9550B0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 227 offset 5 length 15358476 bytes, remaining 53 </code></pre></div><div id="comment-9797-info" class="comment-info"><span class="comment-age">(27 Mar '12, 14:26)</span> infinity9999</div></div><span id="9843"></span><div id="comment-9843" class="comment not_top_scorer"><div id="post-9843-score" class="comment-score"></div><div class="comment-text"><p>Did more digging and testing. I think the issue lies that the server hello packet in response to the client request doesn't list the certificate in it, only the change cipher spec and encrypted handshake. The handshake occurs for the application, but the cert is never passed along, so wireshark probably can't figure out what to decrypt.</p></div><div id="comment-9843-info" class="comment-info"><span class="comment-age">(29 Mar '12, 11:52)</span> infinity9999</div></div><span id="9850"></span><div id="comment-9850" class="comment not_top_scorer"><div id="post-9850-score" class="comment-score"></div><div class="comment-text"><p>And more digging is uncovering some more info. Basically the issue we're investigating is what looks like a complete network drop for about a minute on the server end. In the trace, we can see all the resets followed by normal activity. However after the resets go through, I'm able to decrypt at the least the bind traffic. It looks like there's more, but it's not decrypting. So, I'm thinking that we have something like persistent connections that are just maintaining themselves without doing handshakes with the certs or something so I can't decrypt prior to the resets.</p></div><div id="comment-9850-info" class="comment-info"><span class="comment-age">(29 Mar '12, 13:45)</span> infinity9999</div></div><span id="9855"></span><div id="comment-9855" class="comment"><div id="post-9855-score" class="comment-score">1</div><div class="comment-text"><p>The SSL client and server can cache the keying information for each session. This will prevent a new connection from doing the CPU expensive key exchange.</p><p>As you already noticed, the "Certificate" message is missing in those cases. But more importantly, the "ClientKeyExchange" message is missing, it is this message that contains the keying material (encrypted with the public key from the Certificate).</p><p>Wireshark uses the private key from the server to decrypt the "ClientKeyExchange" to get to the keying material for that particular SSL session. Without the keying material, no SSL decryption!</p></div><div id="comment-9855-info" class="comment-info"><span class="comment-age">(30 Mar '12, 01:04)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9785" class="comment-tools"><span class="comments-showing"> showing 5 of 15 </span> <a href="#" class="show-all-comments-link">show 10 more comments</a></div><div class="clear"></div><div id="comment-9785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

