+++
type = "question"
title = "SSL decryption fails"
description = '''I&#x27;m trying to decrypt SSL traffic, which I&#x27;ve done several times before without problems. Now I&#x27;m using wireshark 1.8.3. on linux 64 bit and something gone wrong - decryption doesn&#x27;t work. I checked just everything (with great help of Sake Blok&#x27;s Sharkfest&#x27;09 presentation) - private key and certific...'''
date = "2012-10-04T13:23:00Z"
lastmod = "2012-10-08T11:53:00Z"
weight = 14717
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/14717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decryption fails](/questions/14717/ssl-decryption-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt SSL traffic, which I've done several times before without problems. Now I'm using wireshark 1.8.3. on linux 64 bit and something gone wrong - decryption doesn't work.</p><p>I checked just everything (with great help of Sake Blok's Sharkfest'09 presentation) - private key and certificate match, I have entire session in capture file, I do not use Server Key Exchange etc.</p><p>After several hours trying I desperately created own certificate and SSL server (openssl server) - which I would expect to work, but nope, no luck.</p><p>Strange thing is that decrypting same traffic using same setup works on Window platform. The difference is here (from SSl debug log). Notice different values in "pcry_private_decrypt: stripping XXX bytes, decr_len 128", despite using exactly same data.</p><p>Windows (decryption works):</p><pre><code>....
dissect_ssl enter frame #8 (first time)
  conversation = 0520184C, ssl_session = 05201CE8
  record: offset = 0, reported_length_remaining = 228
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 132, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 128 bytes, remaining 137
pre master encrypted[128]:
6a 5e 45 15 8d 5d 98 90 d9 53 3d 88 f0 96 e3 33
d8 75 0a 12 c4 00 0f 03 60 06 21 56 ac c2 bd 06
8d 4c 30 b3 78 eb 0c 73 44 0e 79 a9 52 ed 28 fb
7f da 25 fa 8c bc 0e 58 66 9d b1 37 82 25 a2 f7
bc 3a b1 ad 08 4a 4b 98 7f bc 11 6c df 88 3d 80
ff 1b 45 97 16 6a a9 28 ff d4 45 a7 40 f9 55 f1
67 12 fb c3 a2 00 14 ae a3 dd b8 e3 9d 2c 72 10
ed 34 9a 2f 30 96 a3 a7 53 27 32 99 be 79 b3 6c
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 79 bytes, decr_len 127
decrypted_unstrip_pre_master[127]:
02 9a 17 68 3c f6 79 18 ba d7 62 7c 8c 51 a4 4a
e7 e6 fb 41 92 6d 0a f1 93 fc 16 f6 41 93 ab c9
18 8f 90 14 c3 80 0e 05 8c 44 db 83 a6 59 5e 7b
66 d1 fc 71 5e 22 2d bf eb 6f 65 6b 67 92 fa 28
02 c4 e7 79 ff 09 58 14 82 bb 66 a5 1a 50 00 03
03 2a 9f 37 ae d0 ac 15 62 bd 8b 34 dd 08 07 ae
6e a1 05 cb b1 fc 91 24 1d eb 7a f5 21 e9 89 53
22 29 d8 27 e0 ff e5 e1 c1 09 75 f4 41 c2 13
pre master secret[48]:
03 03 2a 9f 37 ae d0 ac 15 62 bd 8b 34 dd 08 07
ae 6e a1 05 cb b1 fc 91 24 1d eb 7a f5 21 e9 89
53 22 29 d8 27 e0 ff e5 e1 c1 09 75 f4 41 c2 13
......</code></pre><p>Linux (decryption fails):</p><pre><code>....
dissect_ssl enter frame #8 (first time)
  conversation = 0x7f8062854880, ssl_session = 0x7f8062854f38
  record: offset = 0, reported_length_remaining = 228
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 132, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 128 bytes, remaining 137
pre master encrypted[128]:
6a 5e 45 15 8d 5d 98 90 d9 53 3d 88 f0 96 e3 33
d8 75 0a 12 c4 00 0f 03 60 06 21 56 ac c2 bd 06
8d 4c 30 b3 78 eb 0c 73 44 0e 79 a9 52 ed 28 fb
7f da 25 fa 8c bc 0e 58 66 9d b1 37 82 25 a2 f7
bc 3a b1 ad 08 4a 4b 98 7f bc 11 6c df 88 3d 80
ff 1b 45 97 16 6a a9 28 ff d4 45 a7 40 f9 55 f1
67 12 fb c3 a2 00 14 ae a3 dd b8 e3 9d 2c 72 10
ed 34 9a 2f 30 96 a3 a7 53 27 32 99 be 79 b3 6c
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 0 bytes, decr_len 128
decrypted_unstrip_pre_master[128]:
c1 a3 35 5c de 95 b5 c4 d6 b9 76 0f cb 6d 10 52
55 1b 71 1b 9e d4 1c 9e a4 f5 5b 27 48 9d 7b bf
98 b0 5d ce f0 42 15 4c d1 34 48 4e a1 5e 5c 48
d6 32 34 a8 54 d2 e8 7c f1 04 81 42 15 a4 f1 18
ef ae 38 c5 de 3c d7 89 3f 72 b4 13 11 4f 8b 2c
d7 6e 08 5f 1c e2 0d f1 a8 1e 7f 63 08 ba cd 11
ba e0 d3 4e 7f 9f 1f db 5c b0 f6 ef fd b8 1b c2
55 7d 8c 65 27 24 0b 3b fb 18 3b 0f 2f 12 2c 21
ssl_decrypt_pre_master_secret wrong pre_master_secret length (128, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 137, reported_length_remaining = 91
......</code></pre><p>Any help would ve greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">ssl decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '12, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/477ab2a2074857c0bb7d051f3c49f676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jurij%20Sikorsky&#39;s gravatar image" /><p>Jurij Sikorsky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jurij Sikorsky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '12, 13:24</p></div></div><div id="comments-container-14717" class="comments-container"></div><div id="comment-tools-14717" class="comment-tools"></div><div class="clear"></div><div id="comment-14717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14784"></span>

<div id="answer-container-14784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14784-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Windows:</p><blockquote><p>conversation = 0520184C, ssl_session = 05201CE8</p></blockquote><p>Linux:</p><blockquote><p>conversation = 0x7f8062854880, ssl_session = 0x7f8062854f38</p></blockquote><p>If this is really the same capture file, why is there a different conversation / ssl session? Could be a bug....</p><p>Can you post the capture file (<a href="http://cloudshark.org">cloudshark.org</a>) together with the private key (here)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14784" class="comments-container"><span id="14795"></span><div id="comment-14795" class="comment"><div id="post-14795-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>thank you for your response. I doublechecked it, and the numbers are same and it's really exactly the same capture file. Please find it here: <a href="http://cloudshark.org/captures/4a79aa3714b7">http://cloudshark.org/captures/4a79aa3714b7</a></p><p>I noticed this dirrefence earlier, but didn't consider it to be a problem, because it's too short to be real ssl session ID, I thought it's some internal representation in the decoder, probably platform dependent.</p><p>Private key is too long for the comment, please find it here: <a href="http://www.sikorky.cz/ssl/privkey.pem">http://www.sikorky.cz/ssl/privkey.pem</a></p><p>Please let me know your findings.</p><p>Regards,</p><p>Jurij</p></div><div id="comment-14795-info" class="comment-info"><span class="comment-age">(08 Oct '12, 13:25)</span> Jurij Sikorsky</div></div><span id="14799"></span><div id="comment-14799" class="comment"><div id="post-14799-score" class="comment-score"></div><div class="comment-text"><p>All files are here: <a href="http://www.sikorky.cz/ssl/">http://www.sikorky.cz/ssl/</a></p><ul><li>capture file</li><li>private key</li><li>linux log</li><li>windows log</li></ul></div><div id="comment-14799-info" class="comment-info"><span class="comment-age">(08 Oct '12, 14:26)</span> Jurij Sikorsky</div></div><span id="14904"></span><div id="comment-14904" class="comment"><div id="post-14904-score" class="comment-score"></div><div class="comment-text"><p>it works on my Ubuntu 12.04. (64 Bit - VMware) - Wireshark 1.8.3!</p><p>So, what is your system? Did you compile Wireshark 1.8.3 yourself? If you downloaded somewhere, please post the link/source for that download.</p></div><div id="comment-14904-info" class="comment-info"><span class="comment-age">(10 Oct '12, 13:29)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-14784" class="comment-tools"></div><div class="clear"></div><div id="comment-14784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

