+++
type = "question"
title = "Decode with known PSK in DTLS"
description = '''I have a wireshark capture of implementations of DTLS protocol.I have the PSK and I have converted it to corresponding hex.DTLS uses TLS_PSK_WITH_AES_128_CCM_8 cipher suite. My question is hoe can I get the encrypted data from wieshark'''
date = "2015-10-28T02:33:00Z"
lastmod = "2015-10-28T09:26:00Z"
weight = 47010
keywords = [ "dtls" ]
aliases = [ "/questions/47010" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode with known PSK in DTLS](/questions/47010/decode-with-known-psk-in-dtls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47010-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a wireshark capture of implementations of DTLS protocol.I have the PSK and I have converted it to corresponding hex.DTLS uses TLS_PSK_WITH_AES_128_CCM_8 cipher suite.</p><p>My question is hoe can I get the encrypted data from wieshark</p></div><div id="question-tags" class="tags-container tags">dtls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/4c874ab58e6af22972723bf3b8afc882?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kalu&#39;s gravatar image" /><p>kalu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kalu has no accepted answers">0%</span></p></div></div><div id="comments-container-47010" class="comments-container"></div><div id="comment-tools-47010" class="comment-tools"></div><div class="clear"></div><div id="comment-47010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47023"></span>

<div id="answer-container-47023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To decrypt DTLS you don't need a <strong>PSK</strong>. What you need is the private key of the server, similar to SSL Decryption (actually it's technically the same).</p><p>Hare are some online resources to start with:</p><blockquote><p><a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a><br />
<a href="http://blogs.technet.com/b/nettracer/archive/2010/10/01/how-to-decrypt-an-ssl-or-tls-session-by-using-wireshark.aspx">http://blogs.technet.com/b/nettracer/archive/2010/10/01/how-to-decrypt-an-ssl-or-tls-session-by-using-wireshark.aspx</a><br />
<a href="http://www.youtube.com/watch?v=vQtur8fqErI">http://www.youtube.com/watch?v=vQtur8fqErI</a></p></blockquote><p>After that, please use the following sample capture file (includes the private key) to make some tests and then apply that to your environment:</p><blockquote><p><a href="https://wiki.wireshark.org/SampleCaptures#DTLS_with_decryption_keys">https://wiki.wireshark.org/SampleCaptures#DTLS_with_decryption_keys</a></p></blockquote><p>BTW: You'll have to add the RAS key for DTLS under</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; DTLS</p></blockquote><p>The <strong>Protocol</strong> field defines the protocol within DTLS, like SPDY or similar. If your protocol is unknown to the DTLS dissector (it will be flagged red if you try), please choose '<strong>data</strong>'.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/47023_screenshot_01.png" alt="alt text" /></p><p>Decryption will work, but Wireshark won't be able to dissect the payload. In that case you can only see the decrypted data bytes in the <strong>packet bytes pane</strong>.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/47023_screenshot_02_ICE6lsT.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '15, 10:03</p></div></div><div id="comments-container-47023" class="comments-container"><span id="47050"></span><div id="comment-47050" class="comment"><div id="post-47050-score" class="comment-score"></div><div class="comment-text"><p>Hauke has added support for DTLS decryption using PSKs since v1.11.3-rc1-417-g0f05597, the preference should be visible at Preferences -&gt; Protocols -&gt; DTLS for 1.12 and newer. Wouldn't that work here?</p></div><div id="comment-47050-info" class="comment-info"><span class="comment-age">(29 Oct '15, 02:42)</span> Lekensteyn</div></div><span id="47055"></span><div id="comment-47055" class="comment"><div id="post-47055-score" class="comment-score"></div><div class="comment-text"><p>Ah, you're right. I completely missed that enhancement! Thanks for the hint.</p></div><div id="comment-47055-info" class="comment-info"><span class="comment-age">(29 Oct '15, 03:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47023" class="comment-tools"></div><div class="clear"></div><div id="comment-47023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

