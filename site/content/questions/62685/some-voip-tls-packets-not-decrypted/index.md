+++
type = "question"
title = "Some VoIP TLS packets not decrypted"
description = '''Using Wireshark 2.2.7 under Windows 7 x64. I have an idea what is going on here but maybe someone can confirm. I have a TLS-encrypted trace of a conversation between a VoIP phone and a PBX. I&#x27;ve supplied the private key from the PBX to Wireshark. I started the trace on the server before reconnecting...'''
date = "2017-07-11T16:06:00Z"
lastmod = "2017-07-13T11:34:00Z"
weight = 62685
keywords = [ "tls", "voip" ]
aliases = [ "/questions/62685" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Some VoIP TLS packets not decrypted](/questions/62685/some-voip-tls-packets-not-decrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62685-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark 2.2.7 under Windows 7 x64.</p><p>I have an idea what is going on here but maybe someone can confirm.</p><p>I have a TLS-encrypted trace of a conversation between a VoIP phone and a PBX. I've supplied the private key from the PBX to Wireshark. I started the trace on the server before reconnecting the phone (turning on the relevant account in the phone), and I can see what I think is a successful key exchange (Client Hello, Server Hello, Client Key Exchange, New Session Ticket) between packets 25 and 31.</p><p>Many packets are decrypted just fine, like this REGISTER:</p><pre><code>dissect_ssl enter frame #37 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000249A3822E80, ssl_session = 00000249A3823850
  record: offset = 0, reported_length_remaining = 933
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 928, ssl state 0x63F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 928
Ciphertext[928]:
| 5a 3c e1 35 d5 95 56 87 29 8b 2a f2 d7 fe 47 bd |Z&lt;.5..V.).*...G.|
[snip]
ssl_decrypt_record: allocating 960 bytes for decrypt data (old len 688)
Plaintext[928]:
| 52 45 47 49 53 54 45 52 20 73 69 70 3a 70 62 75 |REGISTER sip:pbu|
[snip]
ssl_decrypt_record found padding 6 final len 921
checking mac (len 901, version 301, ct 23 seq 2)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 14 ff 77 e6 0a 23 5e cd 4a 37 dd 9a ff 83 ef 66 |..w..#^.J7.....f|
| 93 aa 5a 28                                     |..Z(            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 901, seq = 621, nxtseq = 1522
dissect_ssl3_record decrypted len 901
decrypted app data fragment[901]:
| 52 45 47 49 53 54 45 52 20 73 69 70 3a 70 62 75 |REGISTER sip:pbu|
[snip]
process_ssl_payload: found handle 00000249A0F9A3D0 (sip)
packet_from_server: is from server - FALSE</code></pre><p>However some tell me <code>no decoder available</code>:</p><pre><code>dissect_ssl enter frame #54 (first time)
packet_from_server: is from server - TRUE
  conversation = 00000249A3820220, ssl_session = 00000249A3820790
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
  record: offset = 37, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre><p>I see now that the <code>ssl_session</code> identifiers differ. Have I got multiple TLS conversations going on here? My hunch is that somehow there was a cached key from the previous connection. Why would it use an old key <em>and</em> negotiate a new one? I guess I will try a full phone reboot to force it to lose old keys.</p></div><div id="question-tags" class="tags-container tags">tls voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/e67b3df213fa83c7424b97cb15363847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcbsys&#39;s gravatar image" /><p>mcbsys<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcbsys has no accepted answers">0%</span></p></div></div><div id="comments-container-62685" class="comments-container"></div><div id="comment-tools-62685" class="comment-tools"></div><div class="clear"></div><div id="comment-62685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62756"></span>

<div id="answer-container-62756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62756-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>TLS decryption requires the presence of the full handshake from both the client and server side. In your log, we can find the following line:</p><blockquote><p>decrypt_ssl3_record: app_data len 32, ssl state 0x10</p></blockquote><p>The internal <code>state</code> field is a bitmap, 0x10 means that the <code>SSL_VERSION</code> flag is set and nothing else. That is suspicious. At least the following masks are expected to be set:</p><ul><li>0x01 <code>SSL_CLIENT_RANDOM</code> - indicating that the Client Hello message was seen.</li><li>0x02 <code>SSL_SERVER_RANDOM</code> - indicating that the Server Hello message was seen.</li></ul><p>Lack of either suggests that your capture has started in the middle and is missing the handshake messages. Is it possible that a TCP/TLS connection was already active (for a different SIP account?)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '17, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-62756" class="comments-container"><span id="62769"></span><div id="comment-62769" class="comment"><div id="post-62769-score" class="comment-score"></div><div class="comment-text"><p>Thanks. The capture was done on the server with a <code>host</code> filter on the client's IP. AFAIK, there was only one account active through that IP at the time. You can see ssl_state 0x63F in the packet #37. The only thing I could guess was that a previous session (before I deactivated and re-activated the account on the phone) was cached? I re-ran the test, rebooting the phone, and did not seem to have this overlapping certs issue. I did eventually get a bad mac error, which is what we are actually trying to debug; waiting to hear from the phone vendor after submitting the new trace.</p></div><div id="comment-62769-info" class="comment-info"><span class="comment-age">(13 Jul '17, 18:20)</span> mcbsys</div></div><span id="62780"></span><div id="comment-62780" class="comment"><div id="post-62780-score" class="comment-score"></div><div class="comment-text"><p>Frame 54 has a different conversation ID than 37 and must be a different connection. You can check this by adding a column for the <code>tcp.stream</code> field. What do you mean by "caching"? If it means "it did not close the previous connection", then that could explain it. If it means "it uses session resumption", then no, it would still result in an abbreviated handshake.</p></div><div id="comment-62780-info" class="comment-info"><span class="comment-age">(14 Jul '17, 07:30)</span> Lekensteyn</div></div></div><div id="comment-tools-62756" class="comment-tools"></div><div class="clear"></div><div id="comment-62756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

