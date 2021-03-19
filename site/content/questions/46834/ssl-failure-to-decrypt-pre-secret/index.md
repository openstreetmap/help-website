+++
type = "question"
title = "SSL Failure to decrypt pre-secret"
description = '''I have an SSL session. I have checked that the private key attached to the session is correct for the certificate which is shown as being received from the server using openssl pkcs8 -modulus. Yet the decrypt of the pre master secret is not correct. dissect_ssl enter frame #19 (first time) packet_fr...'''
date = "2015-10-22T07:30:00Z"
lastmod = "2015-10-29T02:57:00Z"
weight = 46834
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/46834" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Failure to decrypt pre-secret](/questions/46834/ssl-failure-to-decrypt-pre-secret)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46834-score" class="post-score" title="current number of votes">0</div><span id="post-46834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an SSL session. I have checked that the private key attached to the session is correct for the certificate which is shown as being received from the server using openssl pkcs8 -modulus.</p><p>Yet the decrypt of the pre master secret is not correct.</p><pre><code>dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - FALSE
  conversation = 00000000057C13E8, ssl_session = 00000000036F38B0
  record: offset = 0, reported_length_remaining = 198
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 134, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 130 bytes, remaining 139 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
pre master encrypted[128]:
| 9a 23 93 d6 e3 40 cf 8f 1f cb a9 c3 9c 03 ca 27 |.#[email protected]&#39;|
| ba 7f 8d 86 f4 0d 46 ef 01 95 65 e9 0d 6d 9c de |......F...e..m..|
| 1f 7a cb 5b 8b a8 5e 10 a4 01 7b c5 00 8d b6 ec |.z.[..^...{.....|
| e2 a5 c9 97 31 45 81 60 71 0c c3 b1 76 68 0c 9e |....1E.`q...vh..|
| b5 78 d7 f9 52 c9 fe a9 26 a9 83 94 39 62 bf cd |.x..R...&amp;...9b..|
| de 2c 9e 96 f9 5a d4 f7 b3 89 eb 34 de 65 1c cf |.,...Z.....4.e..|
| ef de ae 0a dd aa 82 08 53 71 5a b3 67 05 45 c7 |........SqZ.g.E.|
| 46 9f 6c f7 ec 49 70 b5 70 28 60 ea 6e 66 2d 4d |F.l..Ip.p(`.nf-M|
ssl_decrypt_pre_master_secret:RSA_private_decrypt
decrypted_unstrip_pre_master[128]:
| 63 0c 93 bf a1 64 5b 2b ab 06 46 6a 71 64 16 42 |c....d[+..Fjqd.B|
| ab 36 d2 83 71 a9 32 43 e5 03 6d 8e 05 6d 06 e1 |.6..q.2C..m..m..|
| e1 89 43 f7 51 7b 64 f1 23 e1 6b 4d 50 2f d6 d8 |..C.Q{d.#.kMP/..|
| ec 0b 16 b3 6e e6 4c 97 b9 87 b7 a6 8e cd 88 60 |....n.L........`|
| cc 8c 67 01 52 8f 3a 0e b3 53 fb dd cd 2a f3 06 |..g.R.:..S...*..|
| 83 81 aa 55 99 f5 50 43 ad b5 12 7b 63 1f b4 0a |...U..PC...{c...|
| 4b 52 1d 56 4e 79 77 d1 50 e9 36 03 a5 a1 fd 20 |KR.VNyw.P.6.... |
| b4 a8 4c db 8d dd ec 67 3c 89 d8 17 ac 7c 94 36 |..L....g&lt;....|.6|
pcry_private_decrypt: stripping 0 bytes, decr_len 128
ssl_decrypt_pre_master_secret wrong pre_master_secret length (128, expected 48)
ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret</code></pre><p>Could there be any other reason apart from an incorrect key?</p><p>Wireshark 1.12.8 on Windows.</p><p>Robert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '15, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/03bd741d32edec34e0d3ec40d6f92fdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronslow&#39;s gravatar image" /><p><span>ronslow</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronslow has no accepted answers">0%</span></p></div></div><div id="comments-container-46834" class="comments-container"><span id="46870"></span><div id="comment-46870" class="comment"><div id="post-46870-score" class="comment-score"></div><div class="comment-text"><p>Can you try your capture with the current <a href="https://www.wireshark.org/download/automated/win64/">2.0.0rc</a>? It has a fix for <a href="https://ask.wireshark.org/questions/43788/struggling-to-decrypt-ssl">an edge case for the RSA private key parameters</a> and has a new method to match private keys against public keys (it uses the modulus+exponent instead of a user-entered address+port).</p></div><div id="comment-46870-info" class="comment-info"><span class="comment-age">(23 Oct '15, 01:59)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="46975"></span><div id="comment-46975" class="comment"><div id="post-46975-score" class="comment-score"></div><div class="comment-text"><p>Following Lekensteyn's suggestion, upgrade to Wireshark 2.0.0rc1 solved the problem for me.</p></div><div id="comment-46975-info" class="comment-info"><span class="comment-age">(27 Oct '15, 03:14)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46976"></span><div id="comment-46976" class="comment"><div id="post-46976-score" class="comment-score"></div><div class="comment-text"><p>Yup. Worked. See answer below. Thanks Lekensteyn.</p></div><div id="comment-46976-info" class="comment-info"><span class="comment-age">(27 Oct '15, 03:15)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46978"></span><div id="comment-46978" class="comment"><div id="post-46978-score" class="comment-score"></div><div class="comment-text"><p>O.K. and what was the problem? Wrong key, as I assumed first in my answer?</p></div><div id="comment-46978-info" class="comment-info"><span class="comment-age">(27 Oct '15, 04:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46979"></span><div id="comment-46979" class="comment"><div id="post-46979-score" class="comment-score"></div><div class="comment-text"><p>No, correct key. Works in Wireshark 2.0.0rc1 therefore must be a bug in Wireshark 1.12.8</p></div><div id="comment-46979-info" class="comment-info"><span class="comment-age">(27 Oct '15, 04:14)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46980"></span><div id="comment-46980" class="comment not_top_scorer"><div id="post-46980-score" class="comment-score"></div><div class="comment-text"><p>O.K. good to know. Thanks.</p></div><div id="comment-46980-info" class="comment-info"><span class="comment-age">(27 Oct '15, 04:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47052"></span><div id="comment-47052" class="comment not_top_scorer"><div id="post-47052-score" class="comment-score"></div><div class="comment-text"><p><span>@ronslow</span> Can you link to logs from the 1.12 and 2.0 releases? If it is confidential, you can mail it to me using my PGP key 0xE9B345052419DC1097A9FC9473C4D7C13DB3073A.</p></div><div id="comment-47052-info" class="comment-info"><span class="comment-age">(29 Oct '15, 02:57)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-46834" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-46834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46836"></span>

<div id="answer-container-46836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46836-score" class="post-score" title="current number of votes">0</div><span id="post-46836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>ssl_decrypt_pre_master_secret wrong pre_master_secret length (128, expected 48) ssl_generate_pre_master_secret: can't decrypt pre master secret</p></blockquote><p>Most certainly, the private key does not match the public key!</p><p>See my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/46788/cant-decode-ssl-session-even-though-the-cipher-is-not-diffie-hellman">https://ask.wireshark.org/questions/46788/cant-decode-ssl-session-even-though-the-cipher-is-not-diffie-hellman</a></p></blockquote><p><strong>UPDATE:</strong></p><blockquote><p>I <strong>have checked</strong> that the private key attached to the session is correct for the certificate which is shown as being received from the server <strong>using openssl pkcs8 -modulus</strong>.</p></blockquote><p>O.K. I did not see that in the first place. So, if you are 100% sure that the private key matches the public key in the cert (please double check that), it could be a bug in Wireshark, or something else. Is it possible to upload the whole ssl debug file somewhere and post the link here? If yes, the please do the following:</p><ul><li>close Wireshark</li><li>empty the ssl debug file</li><li>start Wireshark and load the pcap</li><li>close Wirshark</li><li>upload the ssl debug file</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '15, 09:10</strong> </span></p></div></div><div id="comments-container-46836" class="comments-container"><span id="46843"></span><div id="comment-46843" class="comment"><div id="post-46843-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.12.8 on Windows 10. Snakeoil decrypts fine. I have previously decrypted other sessions using a different key/cert. Debug log shows that Wireshark is loading the key correctly for the ip address. 100% sure the private key matches the certificate coming from the server There's no issue with the certificate needing to be in the trust store, is there?</p></div><div id="comment-46843-info" class="comment-info"><span class="comment-age">(22 Oct '15, 09:25)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46844"></span><div id="comment-46844" class="comment"><div id="post-46844-score" class="comment-score"></div><div class="comment-text"><p>Wireshark debug at <a href="http://pastebin.com/TtiTsDWb">http://pastebin.com/TtiTsDWb</a> There is a TCP retransmissions at packets 18 and 19 but I don't think that this makes a difference. The same public key/cert combination failed in previous sessions without a TCP retransmission</p></div><div id="comment-46844-info" class="comment-info"><span class="comment-age">(22 Oct '15, 09:40)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46851"></span><div id="comment-46851" class="comment"><div id="post-46851-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ssl_restore_session Cannot restore using an empty SessionID<br />
trying to use SSL keylog in C:\Users\ronslow\Documents\xbundle\pms.log<br />
failed to open SSL keylog<br />
cannot find master secret in keylog file either</p></blockquote><p>looks like SSL session reuse/resumption was used and the initial handshake was not included in the pcap file, thus Wireshark can't generate the session key.</p></div><div id="comment-46851-info" class="comment-info"><span class="comment-age">(22 Oct '15, 12:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46858"></span><div id="comment-46858" class="comment"><div id="post-46858-score" class="comment-score"></div><div class="comment-text"><p>Don't think so Kurt. Packet 16 has got the handshake and Wireshark is correctly selecting the private key. I always find this attempt to find a SessionID.</p></div><div id="comment-46858-info" class="comment-info"><span class="comment-age">(22 Oct '15, 14:13)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46865"></span><div id="comment-46865" class="comment"><div id="post-46865-score" class="comment-score"></div><div class="comment-text"><p>I'm pretty sure it's as I said. In the ssl debug output, you can see, that your client is sending an SSL session ID in the CLIENT HELO. If there was no other (full) SSL handshake in Frame #0 - Frame #15, Wireshark won't be able to generate the session key.</p><pre><code>dissect_ssl enter frame #16 (first time)
ssl_session_init: initializing ptr 0000000003CF58B0 size 712
association_find: TCP port 57452 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000005F013E8, ssl_session = 0000000003CF58B0 &lt;==== HERE</code></pre><p>Same problem, as described here:</p><blockquote><p><a href="https://ask.wireshark.org/questions/43788/struggling-to-decrypt-ssl">https://ask.wireshark.org/questions/43788/struggling-to-decrypt-ssl</a></p></blockquote><p>To test my assumption, you can do this:</p><ul><li>completely restart the client and/or the server (kill the process)</li><li>then capture the <strong>very first</strong> TLS connection between them.</li></ul><p>Are you then able to decrypt the pcap file?</p><p>If so, I'm right.<br />
</p><p>If you are still unable to decrypt the pcap, it's something else that just looks very similar to SSL session resumption.</p></div><div id="comment-46865-info" class="comment-info"><span class="comment-age">(22 Oct '15, 15:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46871"></span><div id="comment-46871" class="comment not_top_scorer"><div id="post-46871-score" class="comment-score"></div><div class="comment-text"><p>The SessionID length at packet 16 in the raw PCAP is 0. Looks like a bug in Wireshark. It's using a cached SessionID from some other session?</p></div><div id="comment-46871-info" class="comment-info"><span class="comment-age">(23 Oct '15, 02:44)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46872"></span><div id="comment-46872" class="comment not_top_scorer"><div id="post-46872-score" class="comment-score"></div><div class="comment-text"><p>In the debug log you can find that <code>ssl_restore_session</code> did not (re)use a previous session key. You have configured a RSA private key and Wireshark is trying to use that key for decrypting the RSA-encrypted premaster secret from the ClientKeyExchange message. Apparently the RSA key is not correct (or read incorrectly). Can you try a newer Wireshark version as mentioned in the comment to your question?</p></div><div id="comment-46872-info" class="comment-info"><span class="comment-age">(23 Oct '15, 02:50)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="46977"></span><div id="comment-46977" class="comment not_top_scorer"><div id="post-46977-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for looking into this.</p></div><div id="comment-46977-info" class="comment-info"><span class="comment-age">(27 Oct '15, 03:16)</span> <span class="comment-user userinfo">ronslow</span></div></div></div><div id="comment-tools-46836" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-46836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

