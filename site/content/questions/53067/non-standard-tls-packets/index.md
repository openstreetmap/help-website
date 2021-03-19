+++
type = "question"
title = "Non-Standard TLS Packets?"
description = '''TL;DR: How can I verify which TLS library a local client is using with a remote server? I have a client going through a Firewall then hitting a Web Server. The issue arrose when the client could not successfully upload a file onto the Web Server&#x27;s file sharing application (custom site on some type o...'''
date = "2016-05-31T04:22:00Z"
lastmod = "2016-05-31T04:48:00Z"
weight = 53067
keywords = [ "tls", "ssl", "standards", "tlsv1" ]
aliases = [ "/questions/53067" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Non-Standard TLS Packets?](/questions/53067/non-standard-tls-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53067-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>TL;DR: How can I verify which TLS library a local client is using with a remote server?</p><p>I have a client going through a Firewall then hitting a Web Server. The issue arrose when the client could not successfully upload a file onto the Web Server's file sharing application (custom site on some type of *Nix platform). Took me a couple hours to figure out that a key TLS response from the server was never making it back to the client after the data was uploaded. I told the firewall guys to disable any type of Deep Packet Inspection, and all was good. Re-enable, and it broke.</p><p>So something about how this mystery server crafts its TLS1.0 packets causes the Packet Inspection feature of multiple brands of firewalls to trigger an alarm and drop. While all other packets in this TLS session appear to be okay (we do form a valid session).</p><p>I do not have access to this Web Server nor will I be able to get too many details out of it. Is there any way to get to the bottom of this? My guess is that it's using a custom, or non-standard, TLS protocol? How can I verify this? I haven't messed around much with decrypting SSL session traffic with Wireshark, but would this do it? If I only have access to client side?</p><p>Any tips with this matter would be appreciated. Right now the solution is just to disable Packet Inspection for this server.</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags">tls ssl standards tlsv1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '16, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/31c542f97fd3c3763faadbaa39db73db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="synthetiq&#39;s gravatar image" /><p>synthetiq<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="synthetiq has no accepted answers">0%</span></p></div></div><div id="comments-container-53067" class="comments-container"></div><div id="comment-tools-53067" class="comment-tools"></div><div class="clear"></div><div id="comment-53067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53068"></span>

<div id="answer-container-53068" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53068-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Using Wireshark you can capture the traffic at the client, but you may not be able to decrypt it as you don't have the server's private key.</p><p>If the encryption is performed with a suitable algorithm you might be able to get the client to emit a pre-master secret to use for decryption, see the Wiki <a href="https://wiki.wireshark.org/SSL">SSL</a> page for more info.</p><p>The capture, even if not decryptable may still show useful info about the TLS session so if possible you should upload the capture to a public file share, e.g. <a href="https://www.cloudshark.org/">Cloudshark</a>, Google Drive, Dropbox etc. and edit your question with a link back to the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '16, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53068" class="comments-container"><span id="53070"></span><div id="comment-53070" class="comment"><div id="post-53070-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the suggestion, Graham.<br />
</p><p>Unfortunately I cannot get the PCAP to a public server, so I'll have to go down the pre-master secret route.</p><p>Thanks again!</p></div><div id="comment-53070-info" class="comment-info"><span class="comment-age">(31 May '16, 04:53)</span> synthetiq</div></div><span id="53073"></span><div id="comment-53073" class="comment"><div id="post-53073-score" class="comment-score"></div><div class="comment-text"><p>I'm going to mark this comment as the answer as I've just managed to decrypt my own TLS traffic to Gmail using the links you provided above.</p><p>I can carry this knowledge to the problem network and at least make progress (hopefully)!</p><p>Thanks again for your response!</p></div><div id="comment-53073-info" class="comment-info"><span class="comment-age">(31 May '16, 05:51)</span> synthetiq</div></div></div><div id="comment-tools-53068" class="comment-tools"></div><div class="clear"></div><div id="comment-53068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

