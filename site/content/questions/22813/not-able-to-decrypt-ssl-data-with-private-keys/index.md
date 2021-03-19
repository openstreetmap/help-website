+++
type = "question"
title = "Not able to decrypt SSL data with Private Keys"
description = '''Hi there, I m trying to decrypt SSL encrypted data using wireshark, but i m not able to do so. I have provided the RSA keys and the key location in the wireshark, also i m using TLS_RSA_WITH_RC4_128_SHA, so typically Diffie Helmann concept is outta context here. The following is the snap from the de...'''
date = "2013-07-10T08:01:00Z"
lastmod = "2015-10-22T15:27:00Z"
weight = 22813
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/22813" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not able to decrypt SSL data with Private Keys](/questions/22813/not-able-to-decrypt-ssl-data-with-private-keys)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22813-score" class="post-score" title="current number of votes">0</div><span id="post-22813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I m trying to decrypt SSL encrypted data using wireshark, but i m not able to do so. I have provided the RSA keys and the key location in the wireshark, also i m using TLS_RSA_WITH_RC4_128_SHA, so typically Diffie Helmann concept is outta context here. The following is the snap from the debug,</p><pre><code>ssl_association_remove removing TCP 443 - http handle 04453A50
Private key imported: KeyID 5d:bf:fb:fa:7f:5a:a7:57:7f:30:80:36:39:15:d5:1a:...

ssl_init IPv4 addr &#39;2.56.4.2&#39; (2.56.4.2) port &#39;443&#39; filename &#39;C:\Documents and Settings\Administrator\Desktop\latest_server.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\Documents and Settings\Administrator\Desktop\latest_server.key successfully loaded.
association_add TCP port 443 protocol http handle 04453A50

dissect_ssl enter frame #22 (first time)
ssl_session_init: initializing ptr 0566222C size 588
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 94
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 89, ssl state 0x00
association_find: TCP port 1479 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 85 bytes, remaining 94 
packet_from_server: is from server - FALSE
ssl_find_private_key server 2.56.4.2:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #24 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 1145
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 1066
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 1052, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 84 length 1048 bytes, remaining 1136 
  record: offset = 1136, reported_length_remaining = 9
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 1141 length 0 bytes, remaining 1145 

dissect_ssl enter frame #25 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 186
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
pre master encrypted[128]:
71 de ea fa d9 77 eb f9 36 dc 59 30 4d 64 71 79 
c6 31 a4 13 e8 cc cc 8e 45 0e 08 e4 c7 e7 b6 50 
54 e9 80 f1 eb 3e 7d 4a 68 e2 1f f5 e6 ca 84 ec 
33 39 9e 4a f8 fa ff 35 a8 a2 e9 4a 88 aa 46 77 
16 46 52 06 89 56 57 31 7b d5 b2 41 d6 2b c6 95 
21 cb 8a 71 cb e2 1f 05 c1 a9 bd 52 43 d0 d7 6b 
b5 75 00 1a ca 1a 4f 47 b1 38 91 5d 3f 22 8c f8 
af ec 07 7c be 64 08 a5 ae 63 32 04 56 62 3f d7 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 0 bytes, decr_len 128
decrypted_unstrip_pre_master[128]:
81 e2 42 e6 47 c6 f7 a1 cf f5 65 c5 e6 09 b4 7a 
d9 ed 35 60 a4 d0 71 b3 29 ca 96 c4 cc fc ec b9 
6c cb 19 50 91 a8 83 92 93 20 7d 3c 2d 34 82 f5 
b8 fe 3d 2c 27 2f 6b 6d 13 3a f8 16 8f c9 d4 75 
d8 85 64 7b b9 8e 4d 4d 11 e6 5c bb 69 0f 01 b8 
ab 0e db 7b 1f 76 a9 0f f5 57 a5 65 ae 5a 59 2e 
58 19 0b f4 bc 40 4b e6 4a db 33 27 9b a6 1c a3 
57 3d 8e 3f 10 9e 1e ae f5 d2 39 26 25 7e b5 cf 
ssl_decrypt_pre_master_secret wrong pre_master_secret length (128, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 139, reported_length_remaining = 47
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 250 offset 150 length 1576909 bytes, remaining 186 

dissect_ssl enter frame #26 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 47
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 41
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 36, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 187 offset 11 length 2702752 bytes, remaining 47 

dissect_ssl enter frame #27 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 322
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 317, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 1479 found 00000000
association_find: TCP port 443 found 04B14C48

dissect_ssl enter frame #28 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 320
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 315, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04B14C48

dissect_ssl enter frame #29 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460

dissect_ssl enter frame #31 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 2920
  need_desegmentation: offset = 0, reported_length_remaining = 2920

dissect_ssl enter frame #32 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 4380
  need_desegmentation: offset = 0, reported_length_remaining = 4380

dissect_ssl enter frame #33 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 5840
  need_desegmentation: offset = 0, reported_length_remaining = 5840

dissect_ssl enter frame #35 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 7300
  need_desegmentation: offset = 0, reported_length_remaining = 7300

dissect_ssl enter frame #36 (first time)
  conversation = 05661DF4, ssl_session = 0566222C
  record: offset = 0, reported_length_remaining = 8214
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 8182, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04B14C48
  record: offset = 8187, reported_length_remaining = 27
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 22, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
</code></pre><p>I am using my servers (Apache) keys to decrypt the data.</p><p>Please let me know what needs to be done in this context.</p><p>Thanks,</p><p>Ananth !!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '13, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/1a002d088b2603e068102c1fea7e7d7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ananth&#39;s gravatar image" /><p><span>Ananth</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ananth has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jul '13, 12:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-22813" class="comments-container"></div><div id="comment-tools-22813" class="comment-tools"></div><div class="clear"></div><div id="comment-22813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22827"></span>

<div id="answer-container-22827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22827-score" class="post-score" title="current number of votes">0</div><span id="post-22827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The debug data:</p><pre><code>ssl_decrypt_pre_master_secret wrong pre_master_secret length (128, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret</code></pre><p>Usually indicate that the provided private key does not correspond to the certificate in that particular SSL session. Are you sure you provided the right key?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22827" class="comments-container"><span id="22829"></span><div id="comment-22829" class="comment"><div id="post-22829-score" class="comment-score"></div><div class="comment-text"><p>Yes. The key which was used in Apache servers SSL session ( in httpd.conf) was copied and placed in this wire shark</p><p>Thanks, Ananth !!</p></div><div id="comment-22829-info" class="comment-info"><span class="comment-age">(10 Jul '13, 21:04)</span> <span class="comment-user userinfo">Ananth</span></div></div><span id="22831"></span><div id="comment-22831" class="comment"><div id="post-22831-score" class="comment-score"></div><div class="comment-text"><p>Since your filename is "latest_server.key", could it be that between making the packet capture and copying the key, the key could have been changed on the server?</p><p>Here is how you can check whether the certificate and key really match. First extract the certificate from the packet capture. Go to the "Certificate" SSL handshake message (of the session you wish to decrypt). Expand the subtrees until you see a line like this:</p><pre><code>Certificate ([email protected],id-at-commonName=public.sharkfest.local,id-at-organizationName=Sharkfest Lab,id-at-stateOrProvinceName=Noord-Holland,id-at-countryName=NL)</code></pre><p>If there are more lines like that, then the CA chain is sent by the server too. Click on the first certificate (this will be the certificate with the common name of the server in it).</p><p>Now rightclick on the certificate and choose "Export Selected Packet Bytes..." and save the certificate to a file.</p><p>Now check whether the output of the following two cammands is the same:</p><pre><code>openssl x509 -noout -modulus -inform DER -in certfile.cert
openssl rsa -noout -modulus -in privatekey.key</code></pre><p>Or in a oneliner:</p><pre><code>(openssl x509 -noout -modulus -inform DER -in certfile.cert ; openssl rsa -noout -modulus -in privatekey.key) | uniq | wc -l</code></pre><p>If the key matches the certificate, the output will be "1", if it doesn't the output will be "2"</p></div><div id="comment-22831-info" class="comment-info"><span class="comment-age">(11 Jul '13, 00:02)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22832"></span><div id="comment-22832" class="comment"><div id="post-22832-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Now check whether the output of the following two cammands is the same:<br />
openssl x509 -noout -modulus -inform DER -in certfile.cert<br />
openssl rsa -noout -modulus -in privatekey.key</p></blockquote><p>wouldn't that be a great extension for Wireshark to identify wrong keys during SSL decryption?</p></div><div id="comment-22832-info" class="comment-info"><span class="comment-age">(11 Jul '13, 00:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22833"></span><div id="comment-22833" class="comment"><div id="post-22833-score" class="comment-score"></div><div class="comment-text"><p>Yes it would <span>@Kurt</span>, it's been on my mind to add it... but time is not on my side unfortunately...</p></div><div id="comment-22833-info" class="comment-info"><span class="comment-age">(11 Jul '13, 01:04)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22834"></span><div id="comment-22834" class="comment not_top_scorer"><div id="post-22834-score" class="comment-score"></div><div class="comment-text"><p>Is there already an enhancement request for this?</p></div><div id="comment-22834-info" class="comment-info"><span class="comment-age">(11 Jul '13, 01:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46574"></span><div id="comment-46574" class="comment"><div id="post-46574-score" class="comment-score">1</div><div class="comment-text"><p>In Wireshark 2.0 (<a href="https://code.wireshark.org/review/10766),">https://code.wireshark.org/review/10766),</a> SSL keys will be matched by their public key instead of by a user-supplied address. Thus, the wrong key problem is solved.</p></div><div id="comment-46574-info" class="comment-info"><span class="comment-age">(15 Oct '15, 10:37)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="46863"></span><div id="comment-46863" class="comment not_top_scorer"><div id="post-46863-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thus, the wrong key problem is solved.</p></blockquote><p>perfect. +1 for that!</p></div><div id="comment-46863-info" class="comment-info"><span class="comment-age">(22 Oct '15, 15:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22827" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-22827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

