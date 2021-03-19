+++
type = "question"
title = "ssl_generate_pre_master_secret: not enough data to generate key (required state 17)"
description = '''Hi Everyone, Here is my issue: I am able to decrypt TLS packet through Wireshark but somehow I am not able to do it with all the packets that are supposed to. So I am getting this error for those packets: ssl_generate_pre_master_secret: not enough data to generate key (required state 17)  Here is th...'''
date = "2015-04-24T07:03:00Z"
lastmod = "2016-06-15T14:07:00Z"
weight = 41780
keywords = [ "key", "error" ]
aliases = [ "/questions/41780" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [ssl\_generate\_pre\_master\_secret: not enough data to generate key (required state 17)](/questions/41780/ssl_generate_pre_master_secret-not-enough-data-to-generate-key-required-state-17)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41780-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone,</p><p>Here is my issue:</p><p>I am able to decrypt TLS packet through Wireshark but somehow I am not able to do it with all the packets that are supposed to. So I am getting this error for those packets:</p><pre><code>ssl_generate_pre_master_secret: not enough data to generate key (required state 17)</code></pre><p>Here is the whole frame:</p><pre><code>dissect_ssl enter frame #19 (first time)
packet_from_server: is from server - FALSE
  conversation = 055C1208, ssl_session = 07161490
  record: offset = 0, reported_length_remaining = 358
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 11
ssl_generate_pre_master_secret: not enough data to generate key (required state 17)
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 267, reported_length_remaining = 91
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 85
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 80, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 41 offset 278 length 15319293 bytes, remaining 358</code></pre><p>I also tried to look for the meaning of the "state 17" but I couldn't find it :S</p><p>I appreciate any help, thanks.</p></div><div id="question-tags" class="tags-container tags">key error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/47ad1875bc04a89706829a3c72962b43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="felipe&#39;s gravatar image" /><p>felipe<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="felipe has no accepted answers">0%</span></p></div></div><div id="comments-container-41780" class="comments-container"></div><div id="comment-tools-41780" class="comment-tools"></div><div class="clear"></div><div id="comment-41780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41782"></span>

<div id="answer-container-41782" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41782-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Asked and answered multiple times, eg. <a href="https://ask.wireshark.org/questions/17630">https://ask.wireshark.org/questions/17630</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '15, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41782" class="comments-container"><span id="53384"></span><div id="comment-53384" class="comment"><div id="post-53384-score" class="comment-score"></div><div class="comment-text"><p>How is this question the same? These logs say it is in state 11 but required 17 and make no mention of DH. Those logs fail in state 0x17 but require 0x37 or 0x57. It also does not say what state 17 actually is like the OP was asking.</p></div><div id="comment-53384-info" class="comment-info"><span class="comment-age">(12 Jun '16, 15:30)</span> Steiny</div></div></div><div id="comment-tools-41782" class="comment-tools"></div><div class="clear"></div><div id="comment-41782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53480"></span>

<div id="answer-container-53480" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53480-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I agree that this question doesn't appear to be about using a DH cipher. I suspect that the capture doesn't include all the required frames that setup a TLS session, because of the state value.</p><p>The "state" is a set of bitflags that indicate what elements of a TLS session have been seen, the current list of bitflags from the source code is:</p><pre><code>#define SSL_CLIENT_RANDOM       (1&lt;&lt;0)
#define SSL_SERVER_RANDOM       (1&lt;&lt;1)
#define SSL_CIPHER              (1&lt;&lt;2)
#define SSL_HAVE_SESSION_KEY    (1&lt;&lt;3)
#define SSL_VERSION             (1&lt;&lt;4)
#define SSL_MASTER_SECRET       (1&lt;&lt;5)
#define SSL_PRE_MASTER_SECRET   (1&lt;&lt;6)
#define SSL_CLIENT_EXTENDED_MASTER_SECRET (1&lt;&lt;7)
#define SSL_SERVER_EXTENDED_MASTER_SECRET (1&lt;&lt;8)
#define SSL_SERVER_HELLO_DONE   (1&lt;&lt;9)
#define SSL_NEW_SESSION_TICKET  (1&lt;&lt;10)</code></pre><p>This a state value of 11 shows that bits 0 and 4 have been set, i.e. SSL_CLIENT_RANDOM and SSL_VERSION have been located, and state 17 has the additional flags SSL_SERVER_RANDOM and SSL_CIPHER.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53480" class="comments-container"></div><div id="comment-tools-53480" class="comment-tools"></div><div class="clear"></div><div id="comment-53480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

