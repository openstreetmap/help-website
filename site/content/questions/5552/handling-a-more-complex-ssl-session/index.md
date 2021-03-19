+++
type = "question"
title = "Handling a more complex SSL session?"
description = '''Hi everyone, I&#x27;ve been using wireshark to record my packets to a service, with that I&#x27;ve been able to find out my login data that was encrypted with a simple TLSv1 connection. Now the rest of the communication is done with a more secure TLS connection and I&#x27;ve hit a solid wall. The packets came up a...'''
date = "2011-08-07T06:30:00Z"
lastmod = "2011-08-07T06:53:00Z"
weight = 5552
keywords = [ "tlsv1", "encryption" ]
aliases = [ "/questions/5552" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Handling a more complex SSL session?](/questions/5552/handling-a-more-complex-ssl-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5552-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I've been using wireshark to record my packets to a service, with that I've been able to find out my login data that was encrypted with a simple TLSv1 connection. Now the rest of the communication is done with a more secure TLS connection and I've hit a solid wall.</p><p>The packets came up as TPKT in wireshark, after searching I read something about telling wireshark to handle them as SSL connections (because I could clearly see a digital certificate being sent) and all these connections changed to TSLv1 from TPKT and the certificate exchanges are sent via TCP between the handshakes.</p><p>So, now I have a handshake that consists of 3 certificates.</p><p>From reading lots of Google search results and the TLS protocol, this is by all means a standard part of TLS.</p><p>Part of this connection (from what i could tell from reading the tls standards) involves passing a session ID which i'm assuming is what the "token ID" i get as a response my my login was for?</p><p>The Tlsv1 socket class that im using with my application, however doesn't have anything about setting a session ID manually neither can i see anything regarding connections where certificates get sent over :/ (i.e. I dont know if that is normal or my tlsv1 socket class is lacking?)</p><p>I honestly don't know how I am supposed to handle this connection or how to decrypt it... I'm at a point where I don't actually know what I even need to search on the internet for :|</p><p>Any help is much appreciated.</p></div><div id="question-tags" class="tags-container tags">tlsv1 encryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '11, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/722a3e77d4695f7bad60b6d4711ee14a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lukus001&#39;s gravatar image" /><p>lukus001<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lukus001 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Aug '11, 06:34</p></div></div><div id="comments-container-5552" class="comments-container"></div><div id="comment-tools-5552" class="comment-tools"></div><div class="clear"></div><div id="comment-5552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5553"></span>

<div id="answer-container-5553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5553-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now the rest of the communication is done with a more secure TLS connection</p></blockquote><p>What do you mean with "More secure TLS connection? Was a longer (stronger) key used? Or maybe a stronger cipher?</p><blockquote><p>The packets came up as TPKT in wireshark, after searching I read something about telling wireshark to handle them as SSL connections (because I could clearly see a digital certificate being sent) and all these connections changed to TSLv1 from TPKT and the certificate exchanges are sent via TCP between the handshakes.</p></blockquote><p>The fact that a certificate is being sent, does not make it SSL or TLS. There are other protocols using X.509 certificates.</p><blockquote><p>Part of this connection (from what i could tell from reading the tls standards) involves passing a session ID which i'm assuming is what the "token ID" i get as a response my my login was for?</p></blockquote><p>The SSL/TLS SessionID field is used as an index into the SSL session cache, which makes it possible to re-use the negotiated keying material. It is not at all related to any Application Layer ID (like a token ID that you are mentioning).</p><blockquote><p>I honestly don't know how I am supposed to handle this connection or how to decrypt it...</p></blockquote><p>If the site is using SSL/TLS, you are not supposed to be able to decrypt it ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '11, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5553" class="comments-container"><span id="5557"></span><div id="comment-5557" class="comment"><div id="post-5557-score" class="comment-score"></div><div class="comment-text"><p>-By more secure, I mean instead of using just the one certificate (which is what the login uses) it is now using 3 certificates during the handshake..</p><p>-How would one find the correct protocol? Wireshark seemed to be happy to interpret it as TLSv1 and it seemed more fitting for this service too.</p><p>-I must have interpreted the Tls docs wrong then, thank you :)</p><p>-Well the connection is for a game 'lobby' client, some of it we "know" (by looking at the action script source) but takes about 10 times longer that way :/</p><p>Thanks for answering once again SYNbit.</p></div><div id="comment-5557-info" class="comment-info"><span class="comment-age">(07 Aug '11, 07:28)</span> lukus001</div></div><span id="5567"></span><div id="comment-5567" class="comment"><div id="post-5567-score" class="comment-score"></div><div class="comment-text"><p>It's not uncommon to see multiple certificates in the SSL handshake, as there can be multiple intermediate certificate authorities. This does not make the SSL session more secure, it just means the trust relationship is more complex.</p><p>If Wireshark is happy decoding it as TLS, then it probably is TLS indeed :-)</p></div><div id="comment-5567-info" class="comment-info"><span class="comment-age">(07 Aug '11, 23:42)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5553" class="comment-tools"></div><div class="clear"></div><div id="comment-5553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

