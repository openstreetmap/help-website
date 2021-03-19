+++
type = "question"
title = "Wireshark decrypts SSL traces just partly"
description = '''Hello, What is the reason why Wireshark was able to decrypt only 60% of SSL (https) packets to only one https-server. The server certificate has been provided in .p12 format with a password one day after pulled the traces from the network. What can we do to decrypt the remaining 40%? Is it right tha...'''
date = "2014-02-25T05:03:00Z"
lastmod = "2014-02-25T09:30:00Z"
weight = 30176
keywords = [ "ssl_connection", "decrypt", "ssl_decrypt" ]
aliases = [ "/questions/30176" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark decrypts SSL traces just partly](/questions/30176/wireshark-decrypts-ssl-traces-just-partly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30176-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>What is the reason why Wireshark was able to decrypt only 60% of SSL (https) packets to only one https-server. The server certificate has been provided in .p12 format with a password one day after pulled the traces from the network.</p><p>What can we do to decrypt the remaining 40%?</p><p>Is it right that Wireshark can't save the decrypted packets to a different file by means wireshark can decrypt on the fly (while capturing or reading a tracefile) only?</p><p>thx for hints, Steffen</p></div><div id="question-tags" class="tags-container tags">ssl_connection decrypt ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '14, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/bee49869be792a7d6aee203210f9892e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Discovery&#39;s gravatar image" /><p>Discovery<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Discovery has no accepted answers">0%</span></p></div></div><div id="comments-container-30176" class="comments-container"></div><div id="comment-tools-30176" class="comment-tools"></div><div class="clear"></div><div id="comment-30176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30183"></span>

<div id="answer-container-30183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30183-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>why Wireshark was able to decrypt only 60% of SSL</p></blockquote><p>maybe the other 40% of connections were using a cipher with Diffier Hellman (DH or DHE - see SSL/TLS handshake). If that is the case, you cannot decrypt those connections with the server private key only.</p><blockquote><p>What can we do to decrypt the remaining 40%?</p></blockquote><p>If Diffie Hellmann is the reason:</p><ul><li>Configure the clients and/or the server to <strong>not</strong> use Diffie Hellmann. However, that's a dumb idea, as DH is a security plus.</li><li>Let your clients (browser) dump the sessions keys and use those to decrypt the session (see links below)</li></ul><p><strong>Decrypt SSL with Diffie Hellmann:</strong></p><ul><li><a href="http://ask.wireshark.org/questions/21011/decrypting-tls-messages-which-is-using-diffie-hellman-algorithm">http://ask.wireshark.org/questions/21011/decrypting-tls-messages-which-is-using-diffie-hellman-algorithm</a><br />
</li><li><a href="http://ask.wireshark.org/questions/10730/how-to-config-master-key-and-session-id-in-wireshark">http://ask.wireshark.org/questions/10730/how-to-config-master-key-and-session-id-in-wireshark</a><br />
</li></ul><blockquote><p>Is it right that Wireshark can't save the decrypted packets to a different file by means wireshark can decrypt on the fly</p></blockquote><p>Yes and no. It depends on the Wireshark version you are using and the functionality you need. See the answer to a similar question.</p><blockquote><blockquote><p><a href="http://ask.wireshark.org/questions/23614/save-a-capture-after-decryption">http://ask.wireshark.org/questions/23614/save-a-capture-after-decryption</a><br />
</p></blockquote></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-30183" class="comments-container"><span id="30187"></span><div id="comment-30187" class="comment"><div id="post-30187-score" class="comment-score"></div><div class="comment-text"><p>many thx to your large answer.</p><p>But there is no DH used in the SSL handshakes.</p><p>Steffen</p></div><div id="comment-30187-info" class="comment-info"><span class="comment-age">(25 Feb '14, 10:13)</span> Discovery</div></div><span id="30188"></span><div id="comment-30188" class="comment"><div id="post-30188-score" class="comment-score"></div><div class="comment-text"><p>so, what do you see in the SSL Decryption debug log?</p></div><div id="comment-30188-info" class="comment-info"><span class="comment-age">(25 Feb '14, 10:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30183" class="comment-tools"></div><div class="clear"></div><div id="comment-30183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

