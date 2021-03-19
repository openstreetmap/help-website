+++
type = "question"
title = "I can&#x27;t export SSL keys with a capture with more than one certificate configured"
description = '''Hello, I&#x27;m analysing the communication between a printer with its own certificate and a server with its own certificate (HTTPs). I&#x27;m trying to test a client-server application environment and there&#x27;s custom software installed inside the printer and inside the server. I&#x27;ve configured 3 RSA Keys List ...'''
date = "2013-04-12T10:04:00Z"
lastmod = "2013-04-12T22:54:00Z"
weight = 20384
keywords = [ "ssl" ]
aliases = [ "/questions/20384" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I can't export SSL keys with a capture with more than one certificate configured](/questions/20384/i-cant-export-ssl-keys-with-a-capture-with-more-than-one-certificate-configured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm analysing the communication between a printer with its own certificate and a server with its own certificate (HTTPs). I'm trying to test a client-server application environment and there's custom software installed inside the printer and inside the server. I've configured 3 RSA Keys List entries: one for the server (443 port) and 2 for the printer (443 and 7627 ports). SSL traffic is completely decoded and everything works well. I'm interested in sending this decoded traffic but I can't send the certificates, so I've been trying to use the SSL Session exporting. I've generated a file that containg 2 Pre-Master Keys but when I try to use it in substitution of the certificates, it doesn't work: I must keep the printer RSA Key List entries (but I can avoid to configure the server entrie). What's the problem? What can I send you to troubleshoot this problem?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '13, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/fd9d1ca793c1df117f8420c1a1ad1c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Markus22&#39;s gravatar image" /><p>Markus22<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Markus22 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '13, 06:49</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20384" class="comments-container"></div><div id="comment-tools-20384" class="comment-tools"></div><div class="clear"></div><div id="comment-20384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20388"></span>

<div id="answer-container-20388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20388-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand you correctly, when you configure wireshark with the 3 private keys, all SSL data is decrypted. And then when you export the SSL session keys and remove the 3 private keys, but instead point wireshark to the exported SSL session keys, you do see the server traffic decrypted, but the SSL traffic to the printer stays encrypted. Is this correct?</p><p>If so, the reason might be that the printer is not using an SSL cache, so it won't be using SSL SessionID's. The export of the SSL session keys is done based on the SSL SessionID's. Can you verify in your tracefile that all SSL sessions to the printer have a SessionID length of 0? If this is the case, you might want to file an enhancement request on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> to extend the functionality of the "Export SSL session keys" functionality. It would really help development if you can attach the tracefile and the private key. Of course you might want to make new traces based on a test certificate/key pair (selfsigned is fine).</p><p>If you're not sure if this is the case, please upload the tracefile to www.cloudshark.org and paste the link to the file here as a comment. If you are able to post the private key here too, that would be most useful, but then you probably should use a self-signed test certificate/key pair first to generate the trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '13, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20388" class="comments-container"></div><div id="comment-tools-20388" class="comment-tools"></div><div class="clear"></div><div id="comment-20388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

