+++
type = "question"
title = "How Key Expansion is structured"
description = '''From the wireshark logs I can see that the first 32 bytes are used for Client Write Key where in RFC5246 it stated that the first bytes are for the MAC then the Key and then the IV. What is the correct order? I&#x27;m using protocol TLS_RSA_WITH_AES_256_GCM_SHA384 Thanks key expansion[168]: | 74 0e 20 ea...'''
date = "2016-10-17T12:15:00Z"
lastmod = "2016-10-18T01:38:00Z"
weight = 56475
keywords = [ "tls", "key", "expansion" ]
aliases = [ "/questions/56475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How Key Expansion is structured](/questions/56475/how-key-expansion-is-structured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56475-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From the wireshark logs I can see that the first 32 bytes are used for Client Write Key where in RFC5246 it stated that the first bytes are for the MAC then the Key and then the IV. What is the correct order? I'm using protocol <code>TLS_RSA_WITH_AES_256_GCM_SHA384</code></p><p>Thanks</p><pre><code>key expansion[168]:
| 74 0e 20 ea 20 ea 7b db dd d8 31 85 e6 1c ec 52 |t. . .{...1....R|
| be a0 8d ad 48 73 08 ac 0e 09 06 4f dd a4 68 5f |....Hs.....O..h_|
| 2d 4d d3 bf 92 3d 96 a8 38 a4 c0 35 21 f9 dd ce |-M...=..8..5!...|
| 9e a9 28 60 c5 a5 17 38 85 ca fe a9 66 35 db 1f |..(`...8....f5..|
| b5 68 3e 15 4c 81 23 64 7d e6 31 f0 40 79 80 17 |.h&gt;.L.#d}.1.@y..|
| 03 06 0d 27 d5 4f 52 f0 6c 8a 30 12 65 3d 9c 70 |...&#39;.OR.l.0.e=.p|
| 74 18 cb 6b 77 55 24 f9 e2 06 83 48 89 83 10 3c |t..kwU$....H...&lt;|
| 59 70 83 b1 04 38 c6 cf 19 2f 17 4c 19 f5 bb 6e |Yp...8.../.L...n|
| 58 b6 d6 da 92 f0 64 14 55 8f f1 4a 43 1c ef c2 |X.....d.U..JC...|
| 7e 67 a3 8b b8 c4 b3 71 61 28 c2 58 8d 3b 1c a8 |~g.....qa(.X.;..|
| b1 fe 63 20 7b 19 61 b6                         |..c {.a.        |
Client Write key[32]:
| 74 0e 20 ea 20 ea 7b db dd d8 31 85 e6 1c ec 52 |t. . .{...1....R|
| be a0 8d ad 48 73 08 ac 0e 09 06 4f dd a4 68 5f |....Hs.....O..h_|
Server Write key[32]:
| 2d 4d d3 bf 92 3d 96 a8 38 a4 c0 35 21 f9 dd ce |-M...=..8..5!...|
| 9e a9 28 60 c5 a5 17 38 85 ca fe a9 66 35 db 1f |..(`...8....f5..|
Client Write IV[4]:
| b5 68 3e 15                                     |.h&gt;.            |
Server Write IV[4]:
| 4c 81 23 64                                     |L.#d            |</code></pre></div><div id="question-tags" class="tags-container tags">tls key expansion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/bacee67f0acee64cbdea5e568e29dcaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gil%20Fefer&#39;s gravatar image" /><p>Gil Fefer<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gil Fefer has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '16, 00:55</p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-56475" class="comments-container"></div><div id="comment-tools-56475" class="comment-tools"></div><div class="clear"></div><div id="comment-56475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56487"></span>

<div id="answer-container-56487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56487-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>AEAD ciphers (like the AES-GCM family) do not need an additional MAC key since the construction already provides authentication (AEAD = Authenticated Encryption with Additional Data).</p><p>In <a href="https://tools.ietf.org/html/rfc5246#section-6.3">RFC 5246 (Section 6.3)</a> you can find the following partitioning of the key expansion block:</p><pre><code>  client_write_MAC_key[SecurityParameters.mac_key_length]
  server_write_MAC_key[SecurityParameters.mac_key_length]
  client_write_key[SecurityParameters.enc_key_length]
  server_write_key[SecurityParameters.enc_key_length]
  client_write_IV[SecurityParameters.fixed_iv_length]
  server_write_IV[SecurityParameters.fixed_iv_length]</code></pre><p>For <code>TLS_RSA_WITH_AES_256_GCM_SHA384</code>, the MAC key length is zero (as explained above). The encryption key length is 32 bytes (due to AES256). The "IV" block is actually being used as part of the GCM nonce and is four bytes.</p><p>You can find these details also in <a href="https://tools.ietf.org/html/rfc5288">RFC 5288</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '16, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56487" class="comments-container"></div><div id="comment-tools-56487" class="comment-tools"></div><div class="clear"></div><div id="comment-56487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

