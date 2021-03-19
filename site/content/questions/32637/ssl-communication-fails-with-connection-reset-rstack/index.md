+++
type = "question"
title = "SSL Communication fails with connection reset (RST,ACK)"
description = ''' I have this issue where when a connection is happening between a client and a server (both are hosted on Hyper V) server being windows server 2008 R2 and the client being Windows 8.1 R2 communication fails (both are in the same network). However when I try the same procedure with windows 8.1 physic...'''
date = "2014-05-08T04:02:00Z"
lastmod = "2014-05-09T12:05:00Z"
weight = 32637
keywords = [ "ssl_connection" ]
aliases = [ "/questions/32637" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Communication fails with connection reset (RST,ACK)](/questions/32637/ssl-communication-fails-with-connection-reset-rstack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32637-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Not_WOrking_Capture.jpg" alt="alt text" /><img src="https://osqa-ask.wireshark.org/upfiles/Connection_Working.jpg" alt="alt text" /> I have this issue where when a connection is happening between a client and a server (both are hosted on Hyper V) server being windows server 2008 R2 and the client being Windows 8.1 R2 communication fails (both are in the same network). However when I try the same procedure with windows 8.1 physical machine (server still being 2008 R2 on hyper V), communication successfully happens.</p><p>I am not able to trouble shoot this issue at all, I have attached the screen shots of wireshark capture for both failed and successful communications.</p><p>kind of running in time crunch , any help much appreciated.</p><p>Thanks, GK</p></div><div id="question-tags" class="tags-container tags">ssl_connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '14, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/43ac675ef9fad82c5d145b0de90e9db5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gk_vandamme&#39;s gravatar image" /><p>gk_vandamme<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gk_vandamme has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '14, 04:04</p></div></div><div id="comments-container-32637" class="comments-container"></div><div id="comment-tools-32637" class="comment-tools"></div><div class="clear"></div><div id="comment-32637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32639"></span>

<div id="answer-container-32639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the first session the client (192.168.0.6) closes the connection after having received the Server Hello, Certificate, Server Hello done from the server at 192.168.0.125. So it is probably the server's certificate that the client doesn't like.</p><p>In the second session the SSL handshake continues, so the client (192.168.0.141) is happy with the server's certificate.</p><p>So look at the clients certificate store and see if the certificate (chain) is trusted.</p><hr /><p>As Kurt mentioned the failing client is using TLS1.2 - The server responds with a TLS1.0 Server Hello in both cases.</p><p>Can you change it to use TLS1.0 also?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '14, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 14 May '14, 23:31</p></div></div><div id="comments-container-32639" class="comments-container"><span id="32662"></span><div id="comment-32662" class="comment"><div id="post-32662-score" class="comment-score"></div><div class="comment-text"><p>Checked that .. and the server certificate is added in all the trust stores of the client (Win 8.1) machine. still no luck.. :-(</p></div><div id="comment-32662-info" class="comment-info"><span class="comment-age">(09 May '14, 03:38)</span> gk_vandamme</div></div><span id="32692"></span><div id="comment-32692" class="comment"><div id="post-32692-score" class="comment-score"></div><div class="comment-text"><p>You could export the certificate from the trace as .cer and doubleclick on it to have windows validate it ...</p></div><div id="comment-32692-info" class="comment-info"><span class="comment-age">(09 May '14, 14:24)</span> mrEEde2</div></div></div><div id="comment-tools-32639" class="comment-tools"></div><div class="clear"></div><div id="comment-32639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32681"></span>

<div id="answer-container-32681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32681-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and the server certificate is added in all the trust stores of the client (Win 8.1) machine</p></blockquote><p>In that case the client does not accept the cert due to other reasons. Three possible reasons pop up in my mind.</p><ul><li>Most likely and a problem that is often overseen: The date/time (month, year) on the client is outside of the valid time window of the server cert, and thus the client rejects it. Example: cert valid from 2012-2014. Date on client: 2011. Result: REJECT.</li><li>A mismatch of what is in the certs <strong>subject</strong> (common name) and what the client expected to get. Example: The client accessed 192.168.0.125 and got a cert with the cert subject: <strong>srv001.domain.local</strong>. Result: REJECT.</li><li>The server uses a TLS extension, that is unknown or unsupported by that specific client.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '14, 15:17</p></div></div><div id="comments-container-32681" class="comments-container"><span id="32784"></span><div id="comment-32784" class="comment"><div id="post-32784-score" class="comment-score"></div><div class="comment-text"><ol><li><p>I checked the subject of the certificate on the server , it is issued to xyz.abc.com and the client is accessing xyz.abc.com URL</p></li><li><p>Date time of the certificate matched with that of the client (both of them are in the same time zone)</p></li><li><p>I am attaching the actual wireshark captures of SSL hand shake on both successful and failing clients</p></li><li><p>Please note that the Successful client is a WIN 8.1 physical machine connecting via a physical NIC where as the failing client is 8.1 hosted on hyper V connecting over a virtual switch.</p></li></ol><p>would that make any difference ?</p></div><div id="comment-32784-info" class="comment-info"><span class="comment-age">(14 May '14, 01:50)</span> gk_vandamme</div></div><span id="32785"></span><div id="comment-32785" class="comment"><div id="post-32785-score" class="comment-score"></div><div class="comment-text"><p>FAILED HANDSHAKE CAPTURE</p><p><a href="http://www.filedropper.com/failedhandshakecapture">http://www.filedropper.com/failedhandshakecapture</a></p></div><div id="comment-32785-info" class="comment-info"><span class="comment-age">(14 May '14, 01:54)</span> gk_vandamme</div></div><span id="32786"></span><div id="comment-32786" class="comment"><div id="post-32786-score" class="comment-score"></div><div class="comment-text"><p>WORKING HANDSHAKE CAPTURE</p><p><a href="http://www.filedropper.com/workinghandshakecapture">http://www.filedropper.com/workinghandshakecapture</a></p></div><div id="comment-32786-info" class="comment-info"><span class="comment-age">(14 May '14, 01:57)</span> gk_vandamme</div></div><span id="32805"></span><div id="comment-32805" class="comment"><div id="post-32805-score" class="comment-score"></div><div class="comment-text"><p>Two possible things:</p><ol><li>There is a CRL distribution point in the cert. Maybe the client does not like the ldap sytax or is unable to access the CRL.</li><li>The difference between working and non working is: non working client suggests to use TLS 1.2, working client suggests to use SSL 2.0. Maybe the non working client does not like any of the TLS extensions sent by the server.</li></ol><p>I can't see any clear sign for a problem in the capture file, so you'll probably have to enable some form of 'debugging/logging' on the client to figure out what's going wrong. As a first step, you could try to change the client config to use a different TLS version.</p><p>Regards<br />
Kurt</p></div><div id="comment-32805-info" class="comment-info"><span class="comment-age">(14 May '14, 15:10)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32681" class="comment-tools"></div><div class="clear"></div><div id="comment-32681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

