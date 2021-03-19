+++
type = "question"
title = "SSL Decryption Problems"
description = '''I am trying to decrypt an SSL Session in Wireshark. I have loaded the p12 file(including password) into wireshark. Here is the debug output: 2686 bytes read PKCS#12 imported Bag 0/0: PKCS#8 Encrypted key Private key imported: KeyID &amp;lt;keyID#1&amp;gt;... Bag 1/0: Encrypted Bag 1/0 decrypted: Certificate...'''
date = "2011-09-16T10:17:00Z"
lastmod = "2011-09-16T12:01:00Z"
weight = 6426
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/6426" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption Problems](/questions/6426/ssl-decryption-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6426-score" class="post-score" title="current number of votes">0</div><span id="post-6426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt an SSL Session in Wireshark. I have loaded the p12 file(including password) into wireshark. Here is the debug output:</p><pre><code>2686 bytes read
PKCS#12 imported
Bag 0/0: PKCS#8 Encrypted key
Private key imported: KeyID &lt;keyID#1&gt;...
Bag 1/0: Encrypted
Bag 1/0 decrypted: Certificate
Certificate imported: &lt;password&gt; &lt;&lt;remoteDomain&gt;&gt;, KeyID &lt;keyID#2&gt;
ssl_init IPv4 addr &#39;&lt;LocalIP&gt;&#39; (&lt;LocalIP&gt;) port &#39;59199&#39; filename &#39;C:\Users\dbeutler\Desktop\test.p12&#39; &lt;password&gt;(only for p12 file) &#39;&lt;password&gt;&#39;
ssl_init private key file C:\Users\dbeutler\Desktop\test.p12 successfully loaded.
association_add TCP port 59199 protocol http handle 0000000003FF9A90

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0000000005AF1D00 size 680
  conversation = 0000000005AF1880, ssl_session = 0000000005AF1D00
  record: offset = 0, reported_length_remaining = 88
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 83, ssl state 0x00
association_find: TCP port 59199 found 0000000004A74800
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 79 bytes, remaining 88 
packet_from_server: is from server - FALSE
ssl_find_private_key server &lt;RemoteIP&gt;:443
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
  conversation = 0000000005AF1880, ssl_session = 0000000005AF1D00
  record: offset = 0, reported_length_remaining = 150
dissect_ssl3_record found version 0x0300 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 74, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 79, reported_length_remaining = 71
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 85, reported_length_remaining = 65
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 194 offset 90 length 16556088 bytes, remaining 150

dissect_ssl enter frame #7 (first time)
  conversation = 0000000005AF1880, ssl_session = 0000000005AF1D00
  record: offset = 0, reported_length_remaining = 388
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 6, reported_length_remaining = 382
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 60, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 252 offset 11 length 10477783 bytes, remaining 71 
  record: offset = 71, reported_length_remaining = 317
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 312, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 59199 found 0000000004A74800

dissect_ssl enter frame #8 (first time)
  conversation = 0000000005AF1880, ssl_session = 0000000005AF1D00
  record: offset = 0, reported_length_remaining = 50
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 45, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000004990C80

dissect_ssl enter frame #9 (first time)
  conversation = 0000000005AF1880, ssl_session = 0000000005AF1D00
  record: offset = 0, reported_length_remaining = 735
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 730, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 59199 found 0000000004A74800

dissect_ssl enter frame #4 (already visited)
  conversation = 0000000005AF1880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 88
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 79 bytes, remaining 88

dissect_ssl enter frame #6 (already visited)
  conversation = 0000000005AF1880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 150
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79 
  record: offset = 79, reported_length_remaining = 71
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
  record: offset = 85, reported_length_remaining = 65
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 194 offset 90 length 16556088 bytes, remaining 150

dissect_ssl enter frame #7 (already visited)
  conversation = 0000000005AF1880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 388
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 382
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 252 offset 11 length 10477783 bytes, remaining 71 
  record: offset = 71, reported_length_remaining = 317
dissect_ssl3_record: content_type 23
association_find: TCP port 59199 found 0000000004A74800

dissect_ssl enter frame #8 (already visited)
  conversation = 0000000005AF1880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 50
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000004990C80

dissect_ssl enter frame #9 (already visited)
  conversation = 0000000005AF1880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 735
dissect_ssl3_record: content_type 23
association_find: TCP port 59199 found 0000000004A74800</code></pre><p>Any help would be appreciated... Thanks, Danny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '11, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/ae069f0fbc94f4b7673e10473a51cb28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbeutler&#39;s gravatar image" /><p><span>dbeutler</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbeutler has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Sep '11, 11:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-6426" class="comments-container"></div><div id="comment-tools-6426" class="comment-tools"></div><div class="clear"></div><div id="comment-6426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6427"></span>

<div id="answer-container-6427" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6427-score" class="post-score" title="current number of votes">0</div><span id="post-6427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It would help if you also posted the way you configured the key list in the ssl protocol preferences, as it looks like you entered it incorrect.</p><p>This is how it should be:</p><pre><code>&lt;ip-adress-of-server&gt;,&lt;port-on-server&gt;,http,&lt;path-to-server-private-key&gt;,&lt;password-if-pkcs12-key&gt;</code></pre><p>So when connecting to a https-webserver on 1.1.1.1:443 from a client 10.0.0.1:12345, you would enter:</p><pre><code>1.1.1.1,443,http,/tmp/keyfile.pem  or
1.1.1.1,443,http,/tmp/keyfile.pkcs12,mysecretpassword</code></pre><p>Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '11, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6427" class="comments-container"></div><div id="comment-tools-6427" class="comment-tools"></div><div class="clear"></div><div id="comment-6427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

