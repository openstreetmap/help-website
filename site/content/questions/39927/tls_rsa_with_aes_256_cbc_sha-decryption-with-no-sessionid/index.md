+++
type = "question"
title = "TLS_RSA_WITH_AES_256_CBC_SHA decryption with no sessionID"
description = '''Hi, I have read answers on this forum and i am trying to decrypt a tls capture with sessionID length 0.But I am running into some trouble in making wireshark read my master key.So please help!! I have master key from openssl and this is what my premaster_ras.log file looks like  RSA Session-ID: Mast...'''
date = "2015-02-18T06:09:00Z"
lastmod = "2015-02-18T09:30:00Z"
weight = 39927
keywords = [ "tls", "decryption", "ssl_decrypt" ]
aliases = [ "/questions/39927" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA decryption with no sessionID](/questions/39927/tls_rsa_with_aes_256_cbc_sha-decryption-with-no-sessionid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39927-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have read answers on this forum and i am trying to decrypt a tls capture with sessionID length 0.But I am running into some trouble in making wireshark read my master key.So please help!!</p><p>I have master key from openssl and this is what my premaster_ras.log file looks like</p><p>RSA Session-ID: Master-Key:7e94966b1345e253c4d2dc4d738d33dec03d8149181ab6630891cfe08c2436cd8ed97cdbcac33b9efc81c3feef415ae0</p><p>and this is my <a href="https://docs.google.com/document/d/1JXUh855WoLFqFtCXYUQd9uBy63-pU8CFSchzff4P5_Y/edit?usp=sharing">Debug file</a>.</p><p>I put a print in my code and printed the SSL master key and sessionID</p><p>koundi-Session ID is 0000000000000000000000000000000000000000000000000000000000000000</p><p>koundi-master key is 7e94966b1345e253c4d2dc4d738d33dec03d8149181ab6630891cfe08c2436cd8ed97cdbcac33b9efc81c3feef415ae0 session_id_length is :0 master_key_length is :48</p><p>Thanks!!</p></div><div id="question-tags" class="tags-container tags">tls decryption ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '15, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div></div><div id="comments-container-39927" class="comments-container"></div><div id="comment-tools-39927" class="comment-tools"></div><div class="clear"></div><div id="comment-39927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39932"></span>

<div id="answer-container-39932" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39932-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Mapping from a Session ID to a master secret can only be resolved if the Server Hello message contains such a Session ID. In your case it is empty:</p><blockquote><p>ssl_restore_session Cannot restore using an empty SessionID</p></blockquote><p>Solution: find the Client Hello message and copy its Client Random (32-bytes, 64 hex chars). Then create the SSL keylog file containing:</p><pre><code>CLIENT_RANDOM (64 hex chars here) 7e94966b1345e253c....(etc)....9efc81c3feef415ae0</code></pre><p>Reload the capture file and you are set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '15, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-39932" class="comments-container"><span id="39937"></span><div id="comment-39937" class="comment"><div id="post-39937-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for replying, I did try giving the Client random yesterday but i gave only 16 hex chars ..So it did not work today i gave it 64 hex chars and it shows in my debug file that master secret found and it does decrypt the frames.But in the UI wireshark packets are still encrypted tls.Also I am NOT trying to decrypt https ..so can u help me with that too:)</p><p>Thanks :)</p></div><div id="comment-39937-info" class="comment-info"><span class="comment-age">(18 Feb '15, 22:20)</span> koundi</div></div></div><div id="comment-tools-39932" class="comment-tools"></div><div class="clear"></div><div id="comment-39932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

