+++
type = "question"
title = "Decrypt SIP messages on IP phone logged in to lync"
description = '''Hi , I have to decrypt the SIP messages on wire shark. I have a phone which is logged in to Lync server and is sending packets when there is communication between the phone and server. Please tell me how i can decrypt the messages. I have a .pem file and have given the serverip,port,sip,&amp;lt;file loc...'''
date = "2013-07-03T23:05:00Z"
lastmod = "2013-07-04T01:40:00Z"
weight = 22630
keywords = [ "capture-filter", "sip" ]
aliases = [ "/questions/22630" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypt SIP messages on IP phone logged in to lync](/questions/22630/decrypt-sip-messages-on-ip-phone-logged-in-to-lync)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I have to decrypt the SIP messages on wire shark. I have a phone which is logged in to Lync server and is sending packets when there is communication between the phone and server. Please tell me how i can decrypt the messages. I have a .pem file and have given the serverip,port,sip,&lt;file locatoin=""&gt; in preferences (SSL).</p><p>Thanks in advance, SL.</p></div><div id="question-tags" class="tags-container tags">capture-filter sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/a4f8ee34fa25afcc0166de02a4618bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Srinivas%20Lolla&#39;s gravatar image" /><p>Srinivas Lolla<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Srinivas Lolla has no accepted answers">0%</span></p></div></div><div id="comments-container-22630" class="comments-container"></div><div id="comment-tools-22630" class="comment-tools"></div><div class="clear"></div><div id="comment-22630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22634"></span>

<div id="answer-container-22634" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22634-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For SSl decryption to work, you need the private key from the server. A .pem file is usually a certificate, not a private key. Does your .pem file start with something like:</p><pre><code>-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCoi1wPzMODtqZW9Yvun0pOC50PPmmtJQbxyHbjMxhARLN9N8aK</code></pre><p>If not, it is either not the private key or it is not in the correct format.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22634" class="comments-container"><span id="22637"></span><div id="comment-22637" class="comment"><div id="post-22637-score" class="comment-score"></div><div class="comment-text"><p>My Pem file is starts like this ::</p><p>Bag Attributes Microsoft Local Key set: &lt;no values=""&gt; localKeyID: 01 00 00 00 friendlyName: le-e965d996-09b2-4b52-8e44-3d62e03b52aa Microsoft CSP Name: Microsoft RSA SChannel Cryptographic Provider Key Attributes X509v3 Key Usage: 10 -----BEGIN ENCRYPTED PRIVATE KEY----- MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQI9Fwi9ruu9SICAggA MBQGCCqGSIb3DQMHBAi30XOn+iUA9ASCBMhza5Nq8lpCluyOc2uz1cx00DWpdMmb TkMRw6Wsx3FfV8NexDYWZ/Zy4efx5Qq1+vx4+Oi1frhlb7AR5+hiZgV6l8pFDOl+</p></div><div id="comment-22637-info" class="comment-info"><span class="comment-age">(04 Jul '13, 02:17)</span> Srinivas Lolla</div></div><span id="22640"></span><div id="comment-22640" class="comment"><div id="post-22640-score" class="comment-score"></div><div class="comment-text"><p>This is a PKCS12 formatted private key with a passphrase. Wireshark is able to read the key if you provide the passphrase too in the SSL RSA Keys list.</p></div><div id="comment-22640-info" class="comment-info"><span class="comment-age">(04 Jul '13, 03:52)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-22634" class="comment-tools"></div><div class="clear"></div><div id="comment-22634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

