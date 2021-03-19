+++
type = "question"
title = "Problem decryption traffic between Exchange and another server"
description = '''Hello! I&#x27;ve faced with problem decryption traffic between Exchange and another server that uses Exchange Web Services. I see handshake in traces, but no decoder available. What could be the problem? Wireshark SSL debug log  ssl_association_remove removing TCP 443 - http handle 000000000599FAE0 3489 ...'''
date = "2015-12-13T04:53:00Z"
lastmod = "2015-12-13T08:51:00Z"
weight = 48484
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/48484" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem decryption traffic between Exchange and another server](/questions/48484/problem-decryption-traffic-between-exchange-and-another-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48484-score" class="post-score" title="current number of votes">0</div><span id="post-48484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I've faced with problem decryption traffic between Exchange and another server that uses Exchange Web Services. I see handshake in traces, but no decoder available. What could be the problem?</p><pre><code>Wireshark SSL debug log

ssl_association_remove removing TCP 443 - http handle 000000000599FAE0
3489 bytes read
PKCS#12 imported
Bag 0/0: PKCS#8 Encrypted key
Private key imported: KeyID d9:f3:bc:7f:67:bf:bf:85:49:49:02:2f:d4:33:02:e3:...
ssl_load_key: swapping p and q parameters and recomputing u
Bag 1/0: Encrypted
Bag 1/0 decrypted: Certificate
Certificate imported: ruspbvm3209.swc02.tlab.alcatel.ru &lt;&lt;error&gt;&gt;, KeyID d9f3bc7f67bfbf854949022fd43302e3cac7a182
ssl_init IPv4 addr &#39;172.17.3.209&#39; (172.17.3.209) port &#39;443&#39; filename &#39;C:\Users\pkropach\Desktop\ca-exch.pfx&#39; password(only for p12 file) &#39;123&#39;
ssl_init private key file C:\Users\pkropach\Desktop\ca-exch.pfx successfully loaded.
association_add TCP port 443 protocol http handle 000000000599FAE0

dissect_ssl enter frame #48 (first time)
ssl_session_init: initializing ptr 0000000007342690 size 712
association_find: TCP port 48689 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000006941908, ssl_session = 0000000007342690
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 21 Alert
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 48689 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #3522 (first time)
ssl_session_init: initializing ptr 00000000073A6C40 size 712
association_find: TCP port 62166 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 000000000695EA68, ssl_session = 00000000073A6C40
  record: offset = 0, reported_length_remaining = 230
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 225, ssl state 0x00
association_find: TCP port 62166 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 221 bytes, remaining 230 
packet_from_server: is from server - FALSE
ssl_find_private_key server 172.17.3.209:443
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #3524 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000695EA68, ssl_session = 00000000073A6C40
  record: offset = 0, reported_length_remaining = 2065
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2060, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 2065 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0xC013 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 1640 bytes, remaining 2065 
dissect_ssl3_handshake iteration 0 type 12 offset 1730 length 327 bytes, remaining 2065 
dissect_ssl3_handshake iteration 0 type 14 offset 2061 length 0 bytes, remaining 2065 

dissect_ssl enter frame #3529 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000695EA68, ssl_session = 00000000073A6C40
  record: offset = 0, reported_length_remaining = 75
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 70, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt
ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret
trying to use SSL keylog in 
failed to open SSL keylog
dissect_ssl3_handshake can&#39;t generate pre master secret

dissect_ssl enter frame #3533 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000695EA68, ssl_session = 00000000073A6C40
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #3536 (first time)
packet_from_server: is from server - FALSE
  conversation = 000000000695EA68, ssl_session = 00000000073A6C40
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 211 offset 5 length 16071396 bytes, remaining 53 </code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '15, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/aff1dd3119968bf75edb77eae62f22e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pavelnt&#39;s gravatar image" /><p><span>pavelnt</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pavelnt has no accepted answers">0%</span></p></div></div><div id="comments-container-48484" class="comments-container"></div><div id="comment-tools-48484" class="comment-tools"></div><div class="clear"></div><div id="comment-48484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48485"></span>

<div id="answer-container-48485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48485-score" class="post-score" title="current number of votes">0</div><span id="post-48485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answer (which will not make you happy) is in the log:</p><pre><code>ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt</code></pre><p>The detailed explanation is in the answer to <a href="https://ask.wireshark.org/questions/37223/wireshark-decryption">this question</a>.</p><p>So to decrypt the session contents, you would have to get the negotiated session key from one of the machines in conversation. Whether the Microsoft software allows that is a question to another forum.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '15, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Dec '15, 05:21</strong> </span></p></div></div><div id="comments-container-48485" class="comments-container"><span id="48486"></span><div id="comment-48486" class="comment"><div id="post-48486-score" class="comment-score"></div><div class="comment-text"><p>Is it normal that I see</p><p>ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt</p><p>not for all pcap traces?</p></div><div id="comment-48486-info" class="comment-info"><span class="comment-age">(13 Dec '15, 06:06)</span> <span class="comment-user userinfo">pavelnt</span></div></div><span id="48487"></span><div id="comment-48487" class="comment"><div id="post-48487-score" class="comment-score"></div><div class="comment-text"><p>It is normal if you talk about traces taken between different endpoints; it would be weird if two ssl negotiations between the same endpoints (i.e. same applications, not just same IP addresses) would use different session key establishment methods.</p></div><div id="comment-48487-info" class="comment-info"><span class="comment-age">(13 Dec '15, 06:22)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48490"></span><div id="comment-48490" class="comment"><div id="post-48490-score" class="comment-score"></div><div class="comment-text"><p>I receive traces from the same machine. But I don't see "ssl_decrypt_pre_master_secret session uses DH (17) key exchange".</p><p>Wireshark SSL debug log</p><p>ssl_association_remove removing TCP 443 - http handle 0000000005613710 3489 bytes read PKCS#12 imported Bag 0/0: PKCS#8 Encrypted key Private key imported: KeyID d9:f3:bc:7f:67:bf:bf:85:49:49:02:2f:d4:33:02:e3:... ssl_load_key: swapping p and q parameters and recomputing u Bag 1/0: Encrypted Bag 1/0 decrypted: Certificate Certificate imported: ruspbvm3209.swc02.tlab.alcatel.ru &lt;&lt;error&gt;&gt;, KeyID d9f3bc7f67bfbf854949022fd43302e3cac7a182 ssl_init IPv4 addr '172.17.3.209' (172.17.3.209) port '443' filename 'C:\Users\pkropach\Desktop\ca-exch.pfx' password(only for p12 file) '123' ssl_init private key file C:\Users\pkropach\Desktop\ca-exch.pfx successfully loaded. association_add TCP port 443 protocol http handle 0000000005613710</p><p>dissect_ssl enter frame #50 (first time) ssl_session_init: initializing ptr 0000000009283F50 size 712 association_find: TCP port 52511 found 0000000000000000 packet_from_server: is from server - FALSE conversation = 00000000066E1D78, ssl_session = 0000000009283F50 record: offset = 0, reported_length_remaining = 37 dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10 dissect_ssl3_record: content_type 21 Alert decrypt_ssl3_record: app_data len 32, ssl state 0x10 association_find: TCP port 52511 found 0000000000000000 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available</p></div><div id="comment-48490-info" class="comment-info"><span class="comment-age">(13 Dec '15, 08:05)</span> <span class="comment-user userinfo">pavelnt</span></div></div><span id="48491"></span><div id="comment-48491" class="comment"><div id="post-48491-score" class="comment-score"></div><div class="comment-text"><p>I receive traces from Linux computer that connects to Exchange server. I'd like to see response from Exchange server, because I have problem with bad request (http 400).</p></div><div id="comment-48491-info" class="comment-info"><span class="comment-age">(13 Dec '15, 08:09)</span> <span class="comment-user userinfo">pavelnt</span></div></div><span id="48492"></span><div id="comment-48492" class="comment"><div id="post-48492-score" class="comment-score"></div><div class="comment-text"><p>as for the ssl decoder behaviour, I don't have enough information. I'd filter each tcp session into a separate pcap file and only if the SSL debug log would still say something different for packets with same role in those individual sessions, I'd start to worry. I cannot imagine why the same client and server would use DH key negotiation for one session and other negotiation method for another one. I cannot see the "handshake" keyword in the logs you've posted in the comment. (hint: if the comment is still editable for you, put 4 spaces before each line of the log, it will be much more readable)</p></div><div id="comment-48492-info" class="comment-info"><span class="comment-age">(13 Dec '15, 08:36)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48493"></span><div id="comment-48493" class="comment not_top_scorer"><div id="post-48493-score" class="comment-score"></div><div class="comment-text"><p>Wireshark can only decrypt a flow if the key negotiation phase is available in the capture (which is a necessary condition but not a sufficient one) or if you provide it with the private (deciphering) keys of both parties in some other way.</p><p>As for the real task you need to accomplish, i.e. quite off-topic wrt the initial decryption question: capturing the exchange on the network can tell you <em>what</em> has happened but not <em>why</em> it has happened. So if you get "400 Bad Request" final response to your request, you cannot expect a detailed (or even correct) explanation of what the server does not like about your request. Most often there is no explanation at all.</p><p>So if your real goal is to find out why the server does not like your client's request, the first place to look for explanation is the server's error log. I suppose you know what you are sending in your request; if you are not sure, run a web server on linux, let it log the incoming requests' contents in detail, and let your linux client send the request to it instead of the Exchange. It should be much faster than fiddling around with decryption.</p></div><div id="comment-48493-info" class="comment-info"><span class="comment-age">(13 Dec '15, 08:51)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48485" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-48485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

