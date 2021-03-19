+++
type = "question"
title = "unable to decrypt HTTPS traffic with Wireshark"
description = '''Hello, I have tried the latest developers edition (2.0.0rc1), 1.99 and the latest stable, 1.12.8 and I am unable to decrypt traffic from one particular certificate.  I am able to decrypt traffic from another website with another key so I believe my wireshark settings are set to a working state. The ...'''
date = "2015-10-26T14:45:00Z"
lastmod = "2015-10-28T14:25:00Z"
weight = 46959
keywords = [ "decryption" ]
aliases = [ "/questions/46959" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [unable to decrypt HTTPS traffic with Wireshark](/questions/46959/unable-to-decrypt-https-traffic-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46959-score" class="post-score" title="current number of votes">0</div><span id="post-46959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have tried the latest developers edition (2.0.0rc1), 1.99 and the latest stable, 1.12.8 and I am unable to decrypt traffic from one particular certificate.<br />
</p><p>I am able to decrypt traffic from another website with another key so I believe my wireshark settings are set to a working state.</p><p>The certificate was created in IIS and exported to a PFX file. I have extracted the key with openssl and removed the password.</p><p>I created a test site in a new windows server install and bound the certificate. The site is a basic IIS under construction page.</p><p>My debug shows these messages (edited down):</p><pre><code>ssl_init private key file C:\temp\key.key successfully loaded.
ssl_find_private_key server 10.1.1.1:443
ssl_find_private_key: testing 1 keys
dissect_ssl enter frame #1349 (first time)
packet_from_server: is from server - TRUE
  conversation = 000000000464CAF8, ssl_session = 0000000007998780
  record: offset = 0, reported_length_remaining = 3778
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 3773, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 3778 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x002F -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
ssl_decrypt_pre_master_secret wrong pre_master_secret length (256, expected 48)
ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret
trying to use SSL keylog in 
failed to open SSL keylog
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '15, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/a8d247c0f9db07bc6a38b8d53c174875?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandyw&#39;s gravatar image" /><p><span>Sandyw</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandyw has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '15, 14:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-46959" class="comments-container"></div><div id="comment-tools-46959" class="comment-tools"></div><div class="clear"></div><div id="comment-46959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46960"></span>

<div id="answer-container-46960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46960-score" class="post-score" title="current number of votes">0</div><span id="post-46960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)</p></blockquote><p>That's a possible sign, that you have the wrong private key for the certificate.</p><p>Please check the <strong>Modulus</strong> of the private key and the public key (cert). See my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/46788/cant-decode-ssl-session-even-though-the-cipher-is-not-diffie-hellman">https://ask.wireshark.org/questions/46788/cant-decode-ssl-session-even-though-the-cipher-is-not-diffie-hellman</a><br />
</p></blockquote><p>BTW: What's the Wireshark version that created the ssl debug file? 2.0.0rc should have some code to match the private/public key based on the Modulus. See the comment of <span>@Lekensteyn</span> in the following question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/46834/ssl-failure-to-decrypt-pre-secret">https://ask.wireshark.org/questions/46834/ssl-failure-to-decrypt-pre-secret</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '15, 15:06</strong> </span></p></div></div><div id="comments-container-46960" class="comments-container"><span id="47014"></span><div id="comment-47014" class="comment"><div id="post-47014-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for responding Kurt</p><p>Regarding the modulus, I ran the following commands as per another post I saw before yours (<a href="https://ask.wireshark.org/questions/22813/not-able-to-decrypt-ssl-data-with-private-keys):">https://ask.wireshark.org/questions/22813/not-able-to-decrypt-ssl-data-with-private-keys):</a></p><pre><code>openssl x509 -noout -modulus -inform DER -in certfile.cert

openssl rsa -noout -modulus -in privatekey.key</code></pre><p>The two outputs were identical which tell me I'm using the right private key.</p><p>I've gone between the latest stable release and the latest dev release so I can't remember which release I was on when I posted the debug but I'll re-post as I've re-installed 2.0.0rc1. The capture was done with 1.12.8 but the debug logs is from opening the file with 2.0.0rc1.</p><p>Went back to Edit this so its readable..I'm not used to the formatting in this forum..</p><hr /><pre><code>Wireshark SSL debug log
ssl_association_remove removing TCP 443 - http handle 0000000004BF2BC0
KeyID[20]:
| f9 bd d3 76 37 69 bd 3d e6 db f1 90 cf 11 c7 da |...v7i.=........|
| b5 9d 13 90                                     |....            |
ssl_init private key file C:\temp\keynopwd.key successfully loaded.
ssl_init port &#39;443&#39; filename &#39;C:\temp\keynopwd.key&#39; password(only for p12 file) &#39;&#39;
association_add TCP port 443 protocol http handle 0000000004BF2BC0
KeyID[20]:
| f9 bd d3 76 37 69 bd 3d e6 db f1 90 cf 11 c7 da |...v7i.=........|
| b5 9d 13 90                                     |....            |
ssl_init private key file C:\temp\keynopwd.key successfully loaded.
ssl_init port &#39;443&#39; filename &#39;C:\temp\keynopwd.key&#39; password(only for p12 file) &#39;&#39;
association_add TCP port 443 protocol http handle 0000000004BF2BC0
dissect_ssl enter frame #824 (first time)
association_find: TCP port 49309 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 177
decrypt_ssl3_record: app_data len 177, ssl state 0x00
association_find: TCP port 49309 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 173 bytes, remaining 182 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01
dissect_ssl enter frame #825 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 1460
  need_desegmentation: offset = 0, reported_length_remaining = 1460
dissect_ssl enter frame #829 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 4109
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 4104
decrypt_ssl3_record: app_data len 4104, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 4109 
ssl_dissect_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_dissect_hnd_srv_hello found CIPHER 0xC014 -&gt; state 0x17
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 2275 bytes, remaining 4109 
lookup(KeyID)[20]:
| f9 bd d3 76 37 69 bd 3d e6 db f1 90 cf 11 c7 da |...v7i.=........|
| b5 9d 13 90                                     |....            |
ssl_find_private_key_by_pubkey: lookup result: 0000000005BCFAC0
dissect_ssl3_handshake iteration 0 type 22 offset 2369 length 1401 bytes, remaining 4109 
dissect_ssl3_handshake iteration 0 type 12 offset 3774 length 327 bytes, remaining 4109 
dissect_ssl3_handshake iteration 0 type 14 offset 4105 length 0 bytes, remaining 4109
dissect_ssl enter frame #831 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 70
decrypt_ssl3_record: app_data len 70, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
ssl_restore_master_key can&#39;t find pre-master secret by Unencrypted pre-master secret
ssl_decrypt_pre_master_secret key exchange 24 different from KEX_RSA (30)
ssl_generate_pre_master_secret: can&#39;t decrypt pre-master secret
ssl_restore_master_key can&#39;t find pre-master secret by Encrypted pre-master secret
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 86 48
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 147 offset 86 length 1415968 bytes, remaining 134
dissect_ssl enter frame #832 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
ssl_load_keyfile dtls/ssl.keylog_file is not configured!
ssl_finalize_decryption state = 0x17
ssl_restore_master_key can&#39;t find master secret by Session ID
ssl_restore_master_key can&#39;t restore master secret using an empty Session Ticket
ssl_restore_master_key can&#39;t find master secret by Client Random
  Cannot find master secret
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 11 48
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 52 offset 11 length 16100397 bytes, remaining 59
dissect_ssl enter frame #848 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 410
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 49309 found 0000000000000000
association_find: TCP port 443 found 0000000005D8BA10
  record: offset = 37, reported_length_remaining = 373
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 368, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl enter frame #855 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000008BC0E10
  record: offset = 0, reported_length_remaining = 245
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 240, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl enter frame #824 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000008BBD6B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 173 bytes, remaining 182
dissect_ssl enter frame #829 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 4109
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 81 bytes, remaining 4109 
dissect_ssl3_handshake iteration 0 type 11 offset 90 length 2275 bytes, remaining 4109 
dissect_ssl3_handshake iteration 0 type 22 offset 2369 length 1401 bytes, remaining 4109 
dissect_ssl3_handshake iteration 0 type 12 offset 3774 length 327 bytes, remaining 4109 
dissect_ssl3_handshake iteration 0 type 14 offset 4105 length 0 bytes, remaining 4109
dissect_ssl enter frame #831 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000008BBD6B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 134
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
  record: offset = 75, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 81, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 147 offset 86 length 1415968 bytes, remaining 134
dissect_ssl enter frame #832 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
  record: offset = 6, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
dissect_ssl3_handshake iteration 1 type 52 offset 11 length 16100397 bytes, remaining 59
dissect_ssl enter frame #848 (already visited)
packet_from_server: is from server - FALSE
  conversation = 0000000008BBD6B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 410
dissect_ssl3_record: content_type 23 Application Data
  record: offset = 37, reported_length_remaining = 373
dissect_ssl3_record: content_type 23 Application Data
dissect_ssl enter frame #855 (already visited)
packet_from_server: is from server - TRUE
  conversation = 0000000008BBD6B0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 245
dissect_ssl3_record: content_type 23 Application Data</code></pre><hr /></div><div id="comment-47014-info" class="comment-info"><span class="comment-age">(28 Oct '15, 07:13)</span> <span class="comment-user userinfo">Sandyw</span></div></div><span id="47020"></span><div id="comment-47020" class="comment"><div id="post-47020-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>ssl_dissect_hnd_srv_hello found CIPHER <strong>0xC014</strong> -&gt; state 0x17</p></blockquote><p>I was looking for that line! 0xC014 is a cipher with Diffie Hellman key exchange (TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA) and that means <strong>you cannot decrpyt</strong> it by using the RSA key of the server. That's why DH is being used.</p><p>So, unless you can convince the browser (or server) to export the session keys, there is <strong>no</strong> way to decrypt this session.</p><p>See here:</p><blockquote><p><a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/</a><br />
</p><p><a href="https://www.google.com/?q=site%3Aask.wireshark.org+SSLKEYLOGFILE">https://www.google.com/?q=site%3Aask.wireshark.org+SSLKEYLOGFILE</a><br />
</p></blockquote><p>and my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff">https://ask.wireshark.org/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-47020-info" class="comment-info"><span class="comment-age">(28 Oct '15, 08:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46960" class="comment-tools"></div><div class="clear"></div><div id="comment-46960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47037"></span>

<div id="answer-container-47037" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47037-score" class="post-score" title="current number of votes">0</div><span id="post-47037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok I feel rather stupid about that..I <em>thought</em> I fixed that yesterday</p><p>I originally posted that it didn't work but it just did! Doesn't work with 1.12.5 but it just worked with the latest dev release.</p><p>The strange part is that I was testing a similar but different certificate, bought from the same place but just a few months prior, also SHA256 and I <em>was</em> able to decrypt with 1.12.5 of Wireshark. Same web server, same client.</p><p>Thank you so much!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/a8d247c0f9db07bc6a38b8d53c174875?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandyw&#39;s gravatar image" /><p><span>Sandyw</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandyw has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '15, 14:31</strong> </span></p></div></div><div id="comments-container-47037" class="comments-container"></div><div id="comment-tools-47037" class="comment-tools"></div><div class="clear"></div><div id="comment-47037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

