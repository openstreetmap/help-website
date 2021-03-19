+++
type = "question"
title = "AMQP traffic on SSL/TLS"
description = '''Hello, I have a wireshark traffic file with AMQPS messages so encrypted with SSL/TLS. I have the private key in PEM format (RSA PRIVATE KEY) but I&#x27;m not able to create a new entry in the RSA key list because it warning me that dissector protocol &#x27;amqp&#x27; on port 5671 isn&#x27;t available. How can I decrypt...'''
date = "2015-08-28T07:27:00Z"
lastmod = "2015-08-28T07:48:00Z"
weight = 45463
keywords = [ "tls", "ssl", "amqp", "ssl_decrypt" ]
aliases = [ "/questions/45463" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [AMQP traffic on SSL/TLS](/questions/45463/amqp-traffic-on-ssltls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45463-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a wireshark traffic file with AMQPS messages so encrypted with SSL/TLS. I have the private key in PEM format (RSA PRIVATE KEY) but I'm not able to create a new entry in the RSA key list because it warning me that dissector protocol 'amqp' on port 5671 isn't available. How can I decrypt AMQP traffic ?</p><p>Thanks, Paolo</p></div><div id="question-tags" class="tags-container tags">tls ssl amqp ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/c10ec9c985651547d921f4c045bbed27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppatierno&#39;s gravatar image" /><p>ppatierno<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppatierno has no accepted answers">0%</span></p></div></div><div id="comments-container-45463" class="comments-container"></div><div id="comment-tools-45463" class="comment-tools"></div><div class="clear"></div><div id="comment-45463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45468"></span>

<div id="answer-container-45468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45468-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>in the latest <strong>development release (1.99.x)</strong>, the AMPQ dissector adds itself to the ssl dissector with port 5671 (see packet-ampq.c - ssl_dissector_add), so this should be possible if you try it with 1.99.x. BTW: Wireshark 1.12.x does not have that code, you it won't work with 1.12.x! What is your Wireshark version?</p><p>See my answer to a similar question for some background information:</p><blockquote><p><a href="https://ask.wireshark.org/questions/20910/cannot-decrypt-fix-protocol-over-ssl">https://ask.wireshark.org/questions/20910/cannot-decrypt-fix-protocol-over-ssl</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '15, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '15, 08:14</p></div></div><div id="comments-container-45468" class="comments-container"><span id="45480"></span><div id="comment-45480" class="comment"><div id="post-45480-score" class="comment-score"></div><div class="comment-text"><p>I'm using 1.12.5</p></div><div id="comment-45480-info" class="comment-info"><span class="comment-age">(28 Aug '15, 09:36)</span> ppatierno</div></div><span id="45481"></span><div id="comment-45481" class="comment"><div id="post-45481-score" class="comment-score"></div><div class="comment-text"><p>then it won't work. Please try <a href="https://www.wireshark.org/download.html">1.99.8</a></p></div><div id="comment-45481-info" class="comment-info"><span class="comment-age">(28 Aug '15, 09:38)</span> Kurt Knochner ♦</div></div><span id="45482"></span><div id="comment-45482" class="comment"><div id="post-45482-score" class="comment-score"></div><div class="comment-text"><p>However I installed 1.99.8. I added the private key in the RSA key list without errors ... good. After loading the pcapng file with captured traffic I still see the encrypted traffic and not in clear ... it seems decryption isn't working. Do I need to execute some action ?</p><p>Thanks, Paolo</p></div><div id="comment-45482-info" class="comment-info"><span class="comment-age">(28 Aug '15, 10:04)</span> ppatierno</div></div><span id="45483"></span><div id="comment-45483" class="comment"><div id="post-45483-score" class="comment-score"></div><div class="comment-text"><p>should work out of-the-box. Can you please provide the SSL debug file (see SSL preferences)? I guess you are using a cipher (DHE, DHCE), which cannot be decrypted with the RSA key.</p></div><div id="comment-45483-info" class="comment-info"><span class="comment-age">(28 Aug '15, 10:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-45468" class="comment-tools"></div><div class="clear"></div><div id="comment-45468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

