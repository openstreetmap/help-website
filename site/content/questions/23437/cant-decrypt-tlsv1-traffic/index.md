+++
type = "question"
title = "Can&#x27;t Decrypt TLSv1 Traffic"
description = '''I’m using Wireshark v1.10.1. I have provided the private key to Wireshark SSL protocol preference. But the TLS traffic isn’t decrypted. Here is my Wireshark SSL debug file. Wireshark SSL debug log  ssl_association_remove removing TCP 443 - http handle 03B40638 Private key imported: KeyID 9d:d0:e4:66...'''
date = "2013-07-29T21:08:00Z"
lastmod = "2013-07-30T00:57:00Z"
weight = 23437
keywords = [ "tlsv1" ]
aliases = [ "/questions/23437" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't Decrypt TLSv1 Traffic](/questions/23437/cant-decrypt-tlsv1-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23437-score" class="post-score" title="current number of votes">0</div><span id="post-23437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’m using Wireshark v1.10.1.</p><p>I have provided the private key to Wireshark SSL protocol preference. But the TLS traffic isn’t decrypted. Here is my Wireshark SSL debug file.</p><p>Wireshark SSL debug log</p><pre><code>ssl_association_remove removing TCP 443 - http handle 03B40638
Private key imported: KeyID 9d:d0:e4:66:dd:8e:fb:cf:ea:e4:96:52:cc:92:29:67:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;172.16.0.254&#39; (172.16.0.254) port &#39;443&#39; filename &#39;C:\test\cert.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\test\cert.pem successfully loaded.
association_add TCP port 443 protocol http handle 03B40638
Private key imported: KeyID 9d:d0:e4:66:dd:8e:fb:cf:ea:e4:96:52:cc:92:29:67:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;172.16.252.1&#39; (172.16.252.1) port &#39;443&#39; filename &#39;C:\test\cert.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\test\cert.pem successfully loaded.
association_add TCP port 443 protocol http handle 03B40638

dissect_ssl enter frame #8 (first time)
ssl_session_init: initializing ptr 06041F98 size 592
  conversation = 06041D84, ssl_session = 06041F98
  record: offset = 0, reported_length_remaining = 109
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 104, ssl state 0x00
association_find: TCP port 4287 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 100 bytes, remaining 109 
packet_from_server: is from server - FALSE
ssl_find_private_key server 172.16.0.254:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #10 (first time)
  conversation = 06041D84, ssl_session = 06041F98
  record: offset = 0, reported_length_remaining = 137
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 81, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 86 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
trying to use SSL keylog in 
failed to open SSL keylog
  cannot find master secret in keylog file either
dissect_ssl3_hnd_srv_hello found CIPHER 0x000A -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 86, reported_length_remaining = 51
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 92, reported_length_remaining = 45
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 40, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 188 offset 97 length 1583727 bytes, remaining 137 
....................</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '13, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/43b2b8e73aa872562883c308ee588da4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yuji&#39;s gravatar image" /><p><span>Yuji</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yuji has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '13, 00:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-23437" class="comments-container"></div><div id="comment-tools-23437" class="comment-tools"></div><div class="clear"></div><div id="comment-23437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23440"></span>

<div id="answer-container-23440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23440-score" class="post-score" title="current number of votes">3</div><span id="post-23440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since the "ChangeCipherSpec" handshake message comes directly after the "ServerHello" handshake message, this is a resumed SSL session. Wireshark needs the full SSL handshake to be able to decrypt the packets. You can accomplish this by closing all the client application (browser?) windows and then start capturing before opening the client application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '13, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23440" class="comments-container"></div><div id="comment-tools-23440" class="comment-tools"></div><div class="clear"></div><div id="comment-23440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

