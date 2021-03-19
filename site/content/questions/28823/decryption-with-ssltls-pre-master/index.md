+++
type = "question"
title = "Decryption with SSL/TLS pre-master"
description = '''Hey All, I am looking for a way to decrypt non-browser based traffic (i.e. e-mail, Citrix ICA, SFTP) on my local machine utilizing pre-master secrets. I know this is possible when utilizing the SSLKEYLOGFILE as described here, http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html. ...'''
date = "2014-01-12T09:33:00Z"
lastmod = "2015-02-16T00:11:00Z"
weight = 28823
keywords = [ "tls", "decryption", "ssl" ]
aliases = [ "/questions/28823" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Decryption with SSL/TLS pre-master](/questions/28823/decryption-with-ssltls-pre-master)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28823-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey All,</p><p>I am looking for a way to decrypt non-browser based traffic (i.e. e-mail, Citrix ICA, SFTP) on my local machine utilizing pre-master secrets. I know this is possible when utilizing the SSLKEYLOGFILE as described here, <a href="http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html.">http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html.</a></p><p>The above link only appears to work for browser based traffic. My question is, how can I do the same level of decryption using Wireshark and pre-master secrets for non-browser based traffic?</p><p>Thank you for the help!</p></div><div id="question-tags" class="tags-container tags">tls decryption ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '14, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/422421655ff2e126be7341dcce9345e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brooks&#39;s gravatar image" /><p>Brooks<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brooks has no accepted answers">0%</span></p></div></div><div id="comments-container-28823" class="comments-container"><span id="28888"></span><div id="comment-28888" class="comment"><div id="post-28888-score" class="comment-score"></div><div class="comment-text"><p>Kurt,I can obtain the first part of the requirement the Session-ID from the Wireshark trace. The master key will be the tough part. I am a bit new to OpenSSL, but it appears possible to extract the master key by parsing through memory. The article link below provides more information on that topic,</p><p><a href="http://www.cloudshield.com/blog/advanced-malware/how-to-decrypt-openssl-sessions-using-wireshark-and-ssl-session-identifiers/">http://www.cloudshield.com/blog/advanced-malware/how-to-decrypt-openssl-sessions-using-wireshark-and-ssl-session-identifiers/</a></p><p>Jmayer, thank you for the comment. I do not have access to the source code for the applications, so I will be unable to add any additional code.</p></div><div id="comment-28888-info" class="comment-info"><span class="comment-age">(14 Jan '14, 15:02)</span> Brooks</div></div><span id="39940"></span><div id="comment-39940" class="comment"><div id="post-39940-score" class="comment-score"></div><div class="comment-text"><p>I know its late but If you have the source code of the application then you can extract the master key from the SSL structure which is used to make the ssl system calls like ssl_write and so on..</p></div><div id="comment-39940-info" class="comment-info"><span class="comment-age">(19 Feb '15, 02:03)</span> koundi</div></div></div><div id="comment-tools-28823" class="comment-tools"></div><div class="clear"></div><div id="comment-28823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="28825"></span>

<div id="answer-container-28825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28825-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How are you going to get the session keys? The applications you mentioned (most certainly) won't export the session keys, as some browsers do!?!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '14, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-28825" class="comments-container"><span id="28889"></span><div id="comment-28889" class="comment"><div id="post-28889-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am a bit new to OpenSSL, but it appears possible to extract the master key by parsing through memory</p></blockquote><p>Yes, that's possible, but only 'easy' if the client software is using the OpenSSL library (easy because other people have documented what to look for). For other Software (ICA, SFTP?, etc.) <strong>you</strong> will have to do the reverse engineering yourself to get that key. Not impossible, but quite some work.</p></div><div id="comment-28889-info" class="comment-info"><span class="comment-age">(14 Jan '14, 16:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28825" class="comment-tools"></div><div class="clear"></div><div id="comment-28825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28828"></span>

<div id="answer-container-28828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28828-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First you will have to find out which of these communication methods use ssl/tls for encryption at all. sftp definitely doesn't, I don't know about the others. The you will need to find out which library is being used to implement ssl/tls. If that library is loaded dynamically, create you own copy of that library and add code to export the (pre-) master secret. Build and the modified lib and replace the existing one with your own build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '14, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/f1397f7833ee927f0c26a9fcb92fff11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmayer&#39;s gravatar image" /><p>jmayer<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmayer has no accepted answers">0%</span></p></div></div><div id="comments-container-28828" class="comments-container"></div><div id="comment-tools-28828" class="comment-tools"></div><div class="clear"></div><div id="comment-28828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39880"></span>

<div id="answer-container-39880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39880-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>SFTP does not use SSL/TLS but SSH, that cannot be decrypted with the same methods as SSL.</p><p>The link you gave is dead, but it was likely describing a method where you run a NSS browser (Firefox) with <a href="https://developer.mozilla.org/en-US/docs/NSS_Key_Log_Format"><code>SSLKEYLOGFILE</code></a>. From the comments it seems that you think that SSL Session-ID are the only means to match a master-key, but this is not the case. The <code>CLIENT_RANDOM</code> value can be used instead of the Session-ID.</p><p>For applications not using NSS, but OpenSSL, you can use a debugger or interpose the SSL library as documented <a href="http://security.stackexchange.com/q/80158/2630">here</a>. Whether it is HTTP, SMTP, IMAP or FTP, these all use SSL for transport encryption so the same methods apply.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '15, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-39880" class="comments-container"></div><div id="comment-tools-39880" class="comment-tools"></div><div class="clear"></div><div id="comment-39880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

