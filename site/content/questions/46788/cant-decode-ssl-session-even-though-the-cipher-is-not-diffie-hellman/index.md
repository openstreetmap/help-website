+++
type = "question"
title = "can&#x27;t decode SSL session even though the cipher is not diffie hellman"
description = '''I have a HTTPS session (not with diffie hellman cipher suite) https://www.cloudshark.org/captures/e6e3be94e89b . I have the server key for it(http://pastebin.com/raw.php?i=w8ed5kZA), but it still doesn&#x27;t decode, not sure why. My wireshark is version 1.8.2 running on Ubuntu 12.04.  Thanks. The follow...'''
date = "2015-10-20T17:33:00Z"
lastmod = "2015-10-21T09:08:00Z"
weight = 46788
keywords = [ "wireshark" ]
aliases = [ "/questions/46788" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [can't decode SSL session even though the cipher is not diffie hellman](/questions/46788/cant-decode-ssl-session-even-though-the-cipher-is-not-diffie-hellman)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46788-score" class="post-score" title="current number of votes">0</div><span id="post-46788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a HTTPS session (not with diffie hellman cipher suite) <a href="https://www.cloudshark.org/captures/e6e3be94e89b">https://www.cloudshark.org/captures/e6e3be94e89b</a> . I have the server key for it(<a href="http://pastebin.com/raw.php?i=w8ed5kZA),">http://pastebin.com/raw.php?i=w8ed5kZA),</a> but it still doesn't decode, not sure why. My wireshark is version 1.8.2 running on Ubuntu 12.04.</p><p>Thanks.</p><p>The following is the ssl debug log produced by SSL.</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0x7fed677e4000
Private key imported: KeyID 82:a5:37:de:f9:c9:fa:9c:ac:97:3a:f5:1a:9b:c0:e5:...
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;443&#39; filename &#39;/home/jim1/server.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /home/jim1/server.key successfully loaded.
association_add TCP port 443 protocol http handle 0x7fed677e4000

dissect_ssl enter frame #6 (first time)
ssl_session_init: initializing ptr 0x7fed4cb733b8 size 680
  conversation = 0x7fed4cb72d00, ssl_session = 0x7fed4cb733b8
  record: offset = 0, reported_length_remaining = 121
packet_from_server: is from server - FALSE
ssl_find_private_key server 127.0.0.1:443
client random len: 32 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #8 (first time)
  conversation = 0x7fed4cb72d00, ssl_session = 0x7fed4cb733b8
  record: offset = 0, reported_length_remaining = 547
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0035 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 86, reported_length_remaining = 461
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 447, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 91 length 443 bytes, remaining 538 
  record: offset = 538, reported_length_remaining = 9
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 4, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 543 length 0 bytes, remaining 547

dissect_ssl enter frame #10 (first time)
  conversation = 0x7fed4cb72d00, ssl_session = 0x7fed4cb733b8
  record: offset = 0, reported_length_remaining = 198
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
pre master encrypted[128]:
28 d9 f1 41 21 8d a0 9b c5 70 75 76 b5 2b a6 69 
ff c0 62 60 02 9a 6c 3a d2 b8 3a 2a 96 71 53 ab 
b8 5d 14 1a ea 45 bb a6 57 a7 b7 46 01 6c 0d ab 
ed 23 9d ff a0 06 e7 5b 91 42 b7 2d f2 0f 7d 9c 
bd 32 5c ac 39 bd 2c bb 7a 93 f3 cf f4 5c b1 d9 
eb a3 91 93 a5 10 1c e7 5e ec 71 a4 a0 50 bf 0f 
0d 38 8c 01 a1 87 5c 9c c3 ed 5a 13 67 e4 a8 86 
9a a3 f1 eb 3f ea 7d b5 ec 44 78 dd 25 63 32 16 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: decrypted data is too long ?!? (256 max 128)
ssl_decrypt_pre_master_secret wrong pre_master_secret length (0, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 139, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 145, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 215 offset 150 length 12748211 bytes, remaining 198</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '15, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-46788" class="comments-container"></div><div id="comment-tools-46788" class="comment-tools"></div><div class="clear"></div><div id="comment-46788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46794"></span>

<div id="answer-container-46794" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46794-score" class="post-score" title="current number of votes">2</div><span id="post-46794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)</p></blockquote><p>The private key does not match the public key!</p><p><strong>RSA Key (private key):</strong></p><pre><code>openssl.exe rsa -noout -modulus -in key.txt
Modulus=BAD3E5526C6630EC0E75E725B39B2F0F835157317480FC98788237504416082D
2D5A2E378B074390F33E656F255A8028BC13526C4E2DD067184B2820A96FDD7C95682872
C4C3D654D49B19C6ED10A809D93189E535039E0BC561B0F31A3AF31D10D0F163F0402FDE
C9F9A3EED921E17522B7838C9B94C9654905318D836BDABE9DA296945623DD2CA7CAF607
C06D15652EC51019A059E402D445410E3658D08DC8DAFEE1D83D4DEBCDCF6CD3B328E4C5
804DB73426032CB30D4EF6F57DA1AB147EF349B020D9E162FD7623769D6C49A229C1415D
98D35DC2EC9AD839F4A7262E50CC65FC17FD96F003C35E32F5891399089D0986EACFEBC6
2C0A7CEE465D3043</code></pre><p><strong>Cert (public key):</strong> (extracted from the pcap file)</p><pre><code>openssl.exe x509 -noout -modulus -in cert.der -inform DER
Modulus=BB2BDF187533201DD7D05230B46996B978AD06DE1AC4F9390FD0E8A64E59612308
583292FC65AF8B63E51727FD13E1B59D9701DEB2C3F0C835B795D24A3A99CD9007084DA354
D97E27871CD4AFF137C4EF79E7560246EA684B19B8A7987CC2D5354D24CF9801E2B0F23C95
0916A532CB468AD0034AD0FA428D84F05352B02887</code></pre><p>As you can see, the Modulus is different. That means the RSA private key does not match the public key in the cert!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46794" class="comments-container"><span id="46803"></span><div id="comment-46803" class="comment"><div id="post-46803-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@kurt</span>-knochner, it was my fault. I thought the SSL private key is in /etc/apache2/ssl, but it was actually in /etc/ssl/private according configure file sites-available/default-ssl.</p></div><div id="comment-46803-info" class="comment-info"><span class="comment-age">(21 Oct '15, 09:08)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-46794" class="comment-tools"></div><div class="clear"></div><div id="comment-46794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

