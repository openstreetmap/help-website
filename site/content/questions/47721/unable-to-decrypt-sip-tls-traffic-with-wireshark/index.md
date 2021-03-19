+++
type = "question"
title = "unable to decrypt SIP TLS traffic with Wireshark"
description = '''Hello I want to see the SIP communication between my server and an endpoint which is on SIP TLS. I have the private key from the server and captured the initial handshake. However I&#x27;m not able to decrypt the messages. Is there anything I&#x27;m missing? You perhaps spot something in the log which i don&#x27;t...'''
date = "2015-11-18T08:03:00Z"
lastmod = "2015-11-23T03:00:00Z"
weight = 47721
keywords = [ "tls", "sip", "decrypt" ]
aliases = [ "/questions/47721" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unable to decrypt SIP TLS traffic with Wireshark](/questions/47721/unable-to-decrypt-sip-tls-traffic-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47721-score" class="post-score" title="current number of votes">0</div><span id="post-47721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I want to see the SIP communication between my server and an endpoint which is on SIP TLS. I have the private key from the server and captured the initial handshake. However I'm not able to decrypt the messages. Is there anything I'm missing? You perhaps spot something in the log which i don't.</p><pre><code>dissect_ssl enter frame #28 (first time)
ssl_session_init: initializing ptr 000000000A182FA0 size 712
association_find: TCP port 32941 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000006DE15D8, ssl_session = 000000000A182FA0
  record: offset = 0, reported_length_remaining = 195
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 190, ssl state 0x00
association_find: TCP port 32941 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 186 bytes, remaining 195 
packet_from_server: is from server - FALSE
ssl_find_private_key server 172.19.253.22:5061
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #35 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006DE15D8, ssl_session = 000000000A182FA0
  record: offset = 0, reported_length_remaining = 1448

dissect_ssl enter frame #36 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006DE15D8, ssl_session = 000000000A182FA0
  record: offset = 0, reported_length_remaining = 128

dissect_ssl enter frame #47 (first time)
packet_from_server: is from server - FALSE
  conversation = 0000000006DE15D8, ssl_session = 000000000A182FA0
  record: offset = 0, reported_length_remaining = 214
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 150, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 146 bytes, remaining 155 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 11
ssl_generate_pre_master_secret: not enough data to generate key (required state 17)
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 155, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 161, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 43 offset 166 length 3990203 bytes, remaining 214

dissect_ssl enter frame #50 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006DE15D8, ssl_session = 000000000A182FA0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #54 (first time)
packet_from_server: is from server - TRUE
  conversation = 0000000006DE15D8, ssl_session = 000000000A182FA0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 240 offset 5 length 12105667 bytes, remaining 53</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/1e438446594e5221381491023d3b5dc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="romo&#39;s gravatar image" /><p><span>romo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="romo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Nov '15, 08:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-47721" class="comments-container"><span id="47722"></span><div id="comment-47722" class="comment"><div id="post-47722-score" class="comment-score"></div><div class="comment-text"><p>Please include the Wireshark version you are using. Is this the full debug log? I don't see the Server Hello which mentions the cipher suite that is in use. Very likely your client is using a cipher suite with the Diffie-Hellman key exchange. See <a href="http://security.stackexchange.com/a/42350/2630">this post</a> for investigating further.</p></div><div id="comment-47722-info" class="comment-info"><span class="comment-age">(18 Nov '15, 08:16)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="47853"></span><div id="comment-47853" class="comment"><div id="post-47853-score" class="comment-score"></div><div class="comment-text"><p>i use WS version 1.12.8 You can see the full log here: <a href="https://sprend.com/download.htm?C=0825d50fef974fb7b1b69b9e39a71224">https://sprend.com/download.htm?C=0825d50fef974fb7b1b69b9e39a71224</a> i've been checking the posts with the DHE issue but i couldn't find similarities to my problem(besides i cannot decrypt it)</p></div><div id="comment-47853-info" class="comment-info"><span class="comment-age">(22 Nov '15, 23:13)</span> <span class="comment-user userinfo">romo</span></div></div><span id="47856"></span><div id="comment-47856" class="comment"><div id="post-47856-score" class="comment-score"></div><div class="comment-text"><p>This is the content of the file. Not enough to analyze the problem.</p><pre><code>Wireshark SSL debug log

Private key imported: KeyID 08:fd:4e:ed:4b:f7:39:3b:86:90:62:e5:07:97:89:4a:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;172.19.253.22&#39; (172.19.253.22) port &#39;5061&#39; filename &#39;C:\Users\E706515\Desktop\key.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\Users\E706515\Desktop\key.key successfully loaded.
association_add TCP port 5061 protocol sip handle 0000000005F728D0
</code></pre></div><div id="comment-47856-info" class="comment-info"><span class="comment-age">(23 Nov '15, 00:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47858"></span><div id="comment-47858" class="comment"><div id="post-47858-score" class="comment-score">1</div><div class="comment-text"><p>Hello Kurt Yes very short indeed. No idea why i only posted this part. Please try here again: <a href="https://www.dropbox.com/s/dz3qp35at2fyq90/wslog.txt?dl=0">https://www.dropbox.com/s/dz3qp35at2fyq90/wslog.txt?dl=0</a></p></div><div id="comment-47858-info" class="comment-info"><span class="comment-age">(23 Nov '15, 01:06)</span> <span class="comment-user userinfo">romo</span></div></div></div><div id="comment-tools-47721" class="comment-tools"></div><div class="clear"></div><div id="comment-47721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47859"></span>

<div id="answer-container-47859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47859-score" class="post-score" title="current number of votes">2</div><span id="post-47859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your connection is using a Diffie Hellman cipher (0xC02F = TLS1_TXT_ECDHE_RSA_WITH_AES_128_GCM_SHA256).</p><blockquote><p>dissect_ssl3_hnd_srv_hello found <strong>CIPHER 0xC02F</strong> -&gt; state 0x16</p></blockquote><p>That's the reason why you can't decrypt it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '15, 01:31</strong> </span></p></div></div><div id="comments-container-47859" class="comments-container"><span id="47861"></span><div id="comment-47861" class="comment"><div id="post-47861-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt Thanks for clarifying.</p></div><div id="comment-47861-info" class="comment-info"><span class="comment-age">(23 Nov '15, 02:44)</span> <span class="comment-user userinfo">romo</span></div></div><span id="47862"></span><div id="comment-47862" class="comment"><div id="post-47862-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p></div><div id="comment-47862-info" class="comment-info"><span class="comment-age">(23 Nov '15, 03:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47859" class="comment-tools"></div><div class="clear"></div><div id="comment-47859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

