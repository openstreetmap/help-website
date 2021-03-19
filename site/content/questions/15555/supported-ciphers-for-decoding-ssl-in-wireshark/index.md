+++
type = "question"
title = "Supported ciphers for decoding SSL in Wireshark ?"
description = '''I have been playing with decoding SSL, in Wireshark/Tshark between version 1.0-1.9 (what ships with CentOS 5 and what I could build on CentOS 6). Apart from plain finger trouble and trying to get the correct SSL key format in ~/.wireshark/ for different versions of Wireshark, and not realizing that ...'''
date = "2012-11-05T15:04:00Z"
lastmod = "2012-11-06T01:01:00Z"
weight = 15555
keywords = [ "ssl" ]
aliases = [ "/questions/15555" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Supported ciphers for decoding SSL in Wireshark ?](/questions/15555/supported-ciphers-for-decoding-ssl-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15555-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been playing with decoding SSL, in Wireshark/Tshark between version 1.0-1.9 (what ships with CentOS 5 and what I could build on CentOS 6).</p><p>Apart from plain finger trouble and trying to get the correct SSL key format in ~/.wireshark/ for different versions of Wireshark, and not realizing that the decrypted data appears in an initially hidden pane rather than where it would normally appear in a non-SSL, I notice decryption only works for some ciphers. I was using "openssl s_client -cipher xxx" to force a particular choice, talking to OpenSSL POPS/IMAPS/IMAP(STARTTLS) and Apache. I realize that Diffie-Hellman is unsupported, but I could only decrypt some of the other ciphers. E.g. the export-grade ciphers EXP-DES-CBC-SHA, EXP-RC2-CBC-MD5, EXP-RC4-MD5 fail to decrypt, as do any SSLv2 ciphers.</p><p>I wondered if I am still missing something obvious, or whether that's just a limit on what's possible.</p><p>E.g. with version 1.6,</p><p># tshark -V -o ssl.keys_list:192.168.5.6,993,imap.private.key host 192.168.5.6</p><p>$ echo 0 logout | openssl s_client -cipher EXP-RC4-MD5 -tls1 -connect 192.168.5.6:993</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '12, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/15e8cc4271eec8d4c25ac13dfd5192db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adaviel&#39;s gravatar image" /><p>adaviel<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adaviel has no accepted answers">0%</span></p></div></div><div id="comments-container-15555" class="comments-container"></div><div id="comment-tools-15555" class="comment-tools"></div><div class="clear"></div><div id="comment-15555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15561"></span>

<div id="answer-container-15561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15561-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you check the SSL debug log of Wireshark? If you find the following message (or a similar one), the cipher suite you tried to decrypt is not supported.</p><blockquote><p><code>can't find cipher suite</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15561" class="comments-container"><span id="15593"></span><div id="comment-15593" class="comment"><div id="post-15593-score" class="comment-score"></div><div class="comment-text"><p>I see that message (can't find cipher) for the Diffie-Hellman ciphers DHE-RSA-AES256-SHA, EDH-RSA-DES-CBC3-SHA but not for the others. For EXP-RC4-MD5 I see e.g.</p><blockquote><p>ssl_decrypt_pre_master_secret wrong pre_master_secret length</p></blockquote></div><div id="comment-15593-info" class="comment-info"><span class="comment-age">(06 Nov '12, 13:15)</span> adaviel</div></div><span id="15662"></span><div id="comment-15662" class="comment"><div id="post-15662-score" class="comment-score"></div><div class="comment-text"><p>I tried it myself. Indeed it does not work.</p><p>I also tried to use the pre-master secret file (output of openssl s_client), but that does not work either (error messages).</p><p>I'm trying to figure out what's going wrong. That can take some time....</p></div><div id="comment-15662-info" class="comment-info"><span class="comment-age">(07 Nov '12, 14:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15561" class="comment-tools"></div><div class="clear"></div><div id="comment-15561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

