+++
type = "question"
title = "Decrypt error after Handshake protocol: certificate"
description = '''Hi, I&#x27;m implementing mutual authentication for a particular virtual host on my sever. Once I received the client SHA256 signed cert I got below alert.  Level: fatal, description: Decrypt error frame 16: server received client cert frame 17: server sent decrypt error According to http://tools.ietf.or...'''
date = "2014-10-28T17:39:00Z"
lastmod = "2014-10-28T17:39:00Z"
weight = 37419
keywords = [ "ssl", "authentication", "client", "decrypt", "error" ]
aliases = [ "/questions/37419" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt error after Handshake protocol: certificate](/questions/37419/decrypt-error-after-handshake-protocol-certificate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37419-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm implementing mutual authentication for a particular virtual host on my sever. Once I received the client SHA256 signed cert I got below alert.</p><p>Level: fatal, description: Decrypt error</p><p>frame 16: server received client cert</p><p>frame 17: server sent decrypt error</p><p>According to <a href="http://tools.ietf.org/html/rfc5246">http://tools.ietf.org/html/rfc5246</a></p><p>decrypt_error means</p><pre><code>  A handshake cryptographic operation failed, including being unable
  to correctly verify a signature or validate a Finished message.
  This message is always fatal.</code></pre><p>I guess in my case the server is not able to verify signature. can you let me know what might be the reasons for server not able to verify cert signature? I have the necessary root and int. certs. Do you think it has something to do with SHA256? Other client certs for which I see successful handshakes are sha1.</p><p>wireshark debug logs:</p><p>dissect_ssl enter frame #16 (first time) conversation = 0000000006D169A8, ssl_session = 0000000006D16FE8 record: offset = 0, reported_length_remaining = 3894 dissect_ssl3_record: content_type 22 Handshake decrypt_ssl3_record: app_data len 3889, ssl state 0x17 packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3885 bytes, remaining 3894</p><p>dissect_ssl enter frame #16 (first time) conversation = 0000000006D169A8, ssl_session = 0000000006D16FE8 record: offset = 0, reported_length_remaining = 186 need_desegmentation: offset = 0, reported_length_remaining = 186</p><p>dissect_ssl enter frame #17 (first time) conversation = 0000000006D169A8, ssl_session = 0000000006D16FE8 record: offset = 0, reported_length_remaining = 7 dissect_ssl3_record: content_type 21 Alert decrypt_ssl3_record: app_data len 2, ssl state 0x17 packet_from_server: is from server - TRUE decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">ssl authentication client decrypt error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '14, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/bb70f80627326b82596e15280925b820?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopi1828&#39;s gravatar image" /><p>gopi1828<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopi1828 has no accepted answers">0%</span></p></div></div><div id="comments-container-37419" class="comments-container"><span id="37432"></span><div id="comment-37432" class="comment"><div id="post-37432-score" class="comment-score"></div><div class="comment-text"><p>Is your question why the server is unable to handle the request or why Wireshark is (possibly) unable to decrypt the session?</p></div><div id="comment-37432-info" class="comment-info"><span class="comment-age">(29 Oct '14, 05:32)</span> Kurt Knochner ♦</div></div><span id="37442"></span><div id="comment-37442" class="comment"><div id="post-37442-score" class="comment-score"></div><div class="comment-text"><p>My question is why the server unable to handle the request</p></div><div id="comment-37442-info" class="comment-info"><span class="comment-age">(29 Oct '14, 08:41)</span> gopi1828</div></div><span id="37443"></span><div id="comment-37443" class="comment"><div id="post-37443-score" class="comment-score"></div><div class="comment-text"><p>O.K. that's impossible to tell without looking at the logs of the server or without decrypting the session. Are you able to decrypt the session in Wireshark?</p></div><div id="comment-37443-info" class="comment-info"><span class="comment-age">(29 Oct '14, 12:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37419" class="comment-tools"></div><div class="clear"></div><div id="comment-37419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

