+++
type = "question"
title = "FTP over explicit SSL"
description = '''Hello, i need to decrypt the commands sent by FTP over explicit SSL. i had a couple of tries, but it never succeded. I searched the internet up and down but it seems that nobody needed it before! i already put the key file in Preferences/protocols/ssl but the stream never got decrypted!'''
date = "2012-02-08T09:24:00Z"
lastmod = "2016-07-10T14:49:00Z"
weight = 8904
keywords = [ "ftps", "ftpes", "explicit", "secure", "ftp" ]
aliases = [ "/questions/8904" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [FTP over explicit SSL](/questions/8904/ftp-over-explicit-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8904-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i need to decrypt the commands sent by FTP over explicit SSL. i had a couple of tries, but it never succeded.</p><p>I searched the internet up and down but it seems that nobody needed it before!</p><p>i already put the key file in Preferences/protocols/ssl but the stream never got decrypted!</p></div><div id="question-tags" class="tags-container tags">ftps ftpes explicit secure ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '12, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/1444b5edfac0767b1a0548ddbbec247c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeaceTrain&#39;s gravatar image" /><p>PeaceTrain<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeaceTrain has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '12, 09:26</p></div></div><div id="comments-container-8904" class="comments-container"></div><div id="comment-tools-8904" class="comment-tools"></div><div class="clear"></div><div id="comment-8904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8905"></span>

<div id="answer-container-8905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8905-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>Oh, decryption of FTPS is indeed needed, I use it a lot :-)</em></p><p>In explicit FTPS (or FTPES), the start of the command channel is cleartext until the AUTH TLS command is given and accepted. After that a normal SSL session is being set up. So the packet flow is like this:</p><pre><code>S-&gt;C [cleartext]220 Welcome to FTP server
C-&gt;S [cleartext]AUTH TLS
S-&gt;C [cleartext]234 Proceed with negotiation.
C-&gt;S [SSL] ClientHello
S-&gt;C [SSL] ServerHello
etc.</code></pre><p>When you decode this session as SSL, the first three cleartext messages will appear as "Ignored Unknown Record" and the rest of the session should be visible as SSL, including decryption.</p><p><strong>Three common sources of decryption to fail are:</strong></p><ol><li>The SSL session is reused, so you see only a short SSL handshake (look for the "ClientKeyExchange", if it is missing, you have a short handshake)</li><li>There was a DH cipher chosen by the server (Look for the chosen cipher in the "ServerHello" message, if it contains DH or DHE, you're out of luck with decryption)</li><li>The private key could not be read by wireshark (look at the SSL debug file) or the key does not match the certificate (look for "wrong pre_master secret length" messages in the SSL debug file)</li></ol><p>Hope this helps to get you on your way!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8905" class="comments-container"></div><div id="comment-tools-8905" class="comment-tools"></div><div class="clear"></div><div id="comment-8905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53968"></span>

<div id="answer-container-53968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53968-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I hope it's OK if I extend this rather out-of-date question somewhat... I'm attempting to track down exactly where the clientHello and serverHello packets are in FTPeS. It's right out there in the open with https negotiation, but since this is using ftp for the transfer, it's just showing a stream of octal characters, though I am able to make out the certificate transfer, thanks to Wireshark's display.</p><p>Immediately after the 234 authentication method accepted message from the server, there is a 571B request message using ftp, which I'm going to assume is the clientHello packet.</p><p>My issue is that I'm trying to decode which version of tls is being offered at this point. As I mentioend, I'm just using the decode, but from what I've read, the "clientHello" will begin with a "type" of 0x01, followed by 3 bytes for the length, until we come to the tls version. So in this case, I've been searching the decode for a 0x01, followed by 3 rangom bytes, for what I believe is 0x303 for tls v1.2.<br />
</p><p>From all this, I'm guessing that MAYBE, that the 10th byte in from the beginning of the request command appears to be the tls type. But that's a WAG, not even a SWAG (Scientific Wild @$$ Guess.)</p><p>As I mentioned at the beginning of this, the http decode is so much simpler to read. I would really appreciate help with the FTPeS decode.</p><p>Thanks very much in advance,</p><p>Mark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '16, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/313f691c681d31213fe9a7ee2b66ecba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mhlevy&#39;s gravatar image" /><p>mhlevy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mhlevy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53968" class="comments-container"></div><div id="comment-tools-53968" class="comment-tools"></div><div class="clear"></div><div id="comment-53968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

