+++
type = "question"
title = "Wireshark Decryption"
description = '''In almost every blog I read about ssl decryption with Wireshark, I found the following limitation: Wireshark wont be able to decrypt ssl traffic if Diffie-Hellman Ephemeral (DHE) or RSA Ephemeral is negotiated between the two communication parties.  It seems that even ssl Wireshark&#x27;s wiki supports t...'''
date = "2014-10-21T03:27:00Z"
lastmod = "2014-10-21T04:31:00Z"
weight = 37223
keywords = [ "ssl", "dhe", "wireshark", "decryption" ]
aliases = [ "/questions/37223" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Decryption](/questions/37223/wireshark-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37223-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In almost every blog I read about ssl decryption with Wireshark, I found the following limitation:</p><p>Wireshark wont be able to decrypt ssl traffic if Diffie-Hellman Ephemeral (DHE) or RSA Ephemeral is negotiated between the two communication parties.</p><p>It seems that even <a href="http://wiki.wireshark.org/SSL">ssl Wireshark's wiki</a> supports that. I'm curious and wolud like to know why Wireshark has such that limitation?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">ssl dhe wireshark decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '14, 10:05</p></div></div><div id="comments-container-37223" class="comments-container"></div><div id="comment-tools-37223" class="comment-tools"></div><div class="clear"></div><div id="comment-37223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37230"></span>

<div id="answer-container-37230" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37230-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm curious and wolud like to know why Wireshark has such <strong>that limitation</strong>?</p></blockquote><p>That's not a 'limititation' of Wireshark (in the sense, the developers are not able to implement it), it's the way how the Diffie Hellman algorithm works.</p><p>If you are using a SSL/TLS handshake without DH, the session key gets encrypted with the public (RSA) key of the server (more or less!!). So, if you have access to the private key of the server, you will be able to decrypt the session key and thus decrypt the whole SSL/TLS session.</p><p>With Diffie Hellman, the session key will never be transmitted (it's being calculated on both sides), so you won't be able to intercept it and use it for decryption of the session. That's what Diffie Hellman was developped for. Securely establishing a base crypto key that both parties can use, but nobody else. I recommend the book "Applied Cryptography" if you are interested in all the details.</p><p>Having said that, there is no technical way to decrypt an SSL/TLS session where DH was used, unless one of the parties (client or server) discloses the session key (not the DH key!!).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '14, 06:45</p></div></div><div id="comments-container-37230" class="comments-container"></div><div id="comment-tools-37230" class="comment-tools"></div><div class="clear"></div><div id="comment-37230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

