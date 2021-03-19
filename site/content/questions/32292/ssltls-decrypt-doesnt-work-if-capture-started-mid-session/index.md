+++
type = "question"
title = "SSL/TLS decrypt doesn&#x27;t work if capture started mid-session"
description = '''I think I have SSL/TLS decryption properly-configured: as long as I start capturing before my SSL/TLS session starts, then I see the HTTP messages pulled out of the TLSv1 packets. However, if I start a capture in the middle of an SSL/TLS session, I see nothing besides TLSv1 or TCP packets. I don&#x27;t r...'''
date = "2014-04-29T09:25:00Z"
lastmod = "2014-04-29T13:45:00Z"
weight = 32292
keywords = [ "tls", "ssl", "ssl_decrypt", "decryption" ]
aliases = [ "/questions/32292" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSL/TLS decrypt doesn't work if capture started mid-session](/questions/32292/ssltls-decrypt-doesnt-work-if-capture-started-mid-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32292-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I think I have SSL/TLS decryption properly-configured: as long as I start capturing before my SSL/TLS session starts, then I see the HTTP messages pulled out of the TLSv1 packets. However, if I start a capture in the middle of an SSL/TLS session, I see nothing besides TLSv1 or TCP packets.</p><p>I don't remember having this limitation last time I tried capturing and decoding SSL or TLS (over a year ago), and I cannot find evidence that it should be this way.</p><p>I have the private certificate for the server I am talking to, and in the <strong>Wireshark: Capture Options</strong> dialog, I have a capture filter limiting to only the IPv4 of the host I want to monitor.</p><p>The client is Chrome 34, and the server is Windows Server 2012 (pre-R2). I have a Citrix Netscaler device in front of the server. I am using Wireshark 1.10.7 on Windows 8.1 x64.</p></div><div id="question-tags" class="tags-container tags">tls ssl ssl_decrypt decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '14, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/a978a7e5a8f57b35976b16b12b4a3d10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aren%20Cambre&#39;s gravatar image" /><p>Aren Cambre<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aren Cambre has no accepted answers">0%</span></p></div></div><div id="comments-container-32292" class="comments-container"></div><div id="comment-tools-32292" class="comment-tools"></div><div class="clear"></div><div id="comment-32292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32296"></span>

<div id="answer-container-32296" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32296-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You <strong>need</strong> the TLS handshake with the key exchange in the capture file to be able to decrypt the traffic.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '14, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32296" class="comments-container"></div><div id="comment-tools-32296" class="comment-tools"></div><div class="clear"></div><div id="comment-32296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

