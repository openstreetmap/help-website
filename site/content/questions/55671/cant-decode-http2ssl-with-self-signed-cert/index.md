+++
type = "question"
title = "Can&#x27;t decode HTTP2+SSL with self-signed cert"
description = '''My server is running on localhost:4443, with HTTP2 support. I followed the instruction in https://wiki.wireshark.org/SSL, but still can&#x27;t decode SSL packets. Here&#x27;s first few lines of log file Wireshark version: 2.2.0 (v2.2.0-0-g5368c50 from master-2.2) GnuTLS version: 2.12.19 Libgcrypt version: 1.5...'''
date = "2016-09-19T18:14:00Z"
lastmod = "2016-09-21T14:09:00Z"
weight = 55671
keywords = [ "http2.0", "ssl_decrypt" ]
aliases = [ "/questions/55671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decode HTTP2+SSL with self-signed cert](/questions/55671/cant-decode-http2ssl-with-self-signed-cert)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55671-score" class="post-score" title="current number of votes">0</div><span id="post-55671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My server is running on localhost:4443, with HTTP2 support. I followed the instruction in <a href="https://wiki.wireshark.org/SSL,">https://wiki.wireshark.org/SSL,</a> but still can't decode SSL packets.</p><p>Here's first few lines of log file</p><pre><code>Wireshark version: 2.2.0 (v2.2.0-0-g5368c50 from master-2.2)
GnuTLS version:    2.12.19
Libgcrypt version: 1.5.0

KeyID[20]:
| 04 a1 5f 0f 46 4f 3b 09 5e 8d c0 58 23 cc e7 3a |.._.FO;.^..X#..:|
| 6c ea 49 ff                                     |l.I.            |
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init private key file /Users/laike9m/Dev/HTTP2/h2-playground/server.key successfully loaded.
ssl_init port &#39;4443&#39; filename &#39;/Users/laike9m/Dev/HTTP2/h2-playground/server.key&#39; password(only for p12 file) &#39;&#39;
association_add ssl.port port 4443 handle 0x11d0a4f00

dissect_ssl enter frame #13 (first time)
packet_from_server: is from server - FALSE
  conversation = 0x12042f000, ssl_session = 0x12042fbe0
  record: offset = 0, reported_length_remaining = 517
dissect_ssl3_record: content_type 22 Handshake
Calculating hash with offset 5 512
decrypt_ssl3_record: app_data len 512, ssl state 0x00
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 508 bytes, remaining 517 
ssl_dissect_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01</code></pre><p>Here's my settings: <a href="http://postimg.org/image/48r95uo09/">http://postimg.org/image/48r95uo09/</a> (not enough karma to upload here)</p><p>Here's the result: <a href="http://postimg.org/image/a413xkdv1/">http://postimg.org/image/a413xkdv1/</a></p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http2.0" rel="tag" title="see questions tagged &#39;http2.0&#39;">http2.0</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '16, 18:14</strong></p><img src="https://secure.gravatar.com/avatar/820c611835bb6eea4851c318a3b73345?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laike9m&#39;s gravatar image" /><p><span>laike9m</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laike9m has no accepted answers">0%</span></p></div></div><div id="comments-container-55671" class="comments-container"><span id="55731"></span><div id="comment-55731" class="comment"><div id="post-55731-score" class="comment-score"></div><div class="comment-text"><p>What cipher is in use? You cannot use RSA private keys to decrypt sessions using (EC)DHE cipher suites.</p></div><div id="comment-55731-info" class="comment-info"><span class="comment-age">(21 Sep '16, 14:09)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-55671" class="comment-tools"></div><div class="clear"></div><div id="comment-55671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

