+++
type = "question"
title = "An error occurred in the secure channel support"
description = '''In the application in question, I get this message when trying to access/download to an embedded web server: An error occurred in the secure channel support I&#x27;ve made a WireShark log of the communication: www.roswall.com/ws_log.zip I stumble over the following part. Any ideas to what I should be loo...'''
date = "2015-01-20T17:39:00Z"
lastmod = "2015-01-21T01:13:00Z"
weight = 39325
keywords = [ "sslv3" ]
aliases = [ "/questions/39325" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [An error occurred in the secure channel support](/questions/39325/an-error-occurred-in-the-secure-channel-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39325-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the application in question, I get this message when trying to access/download to an embedded web server: An error occurred in the secure channel support</p><p>I've made a WireShark log of the communication: www.roswall.com/ws_log.zip</p><p>I stumble over the following part. Any ideas to what I should be looking at or for on this PC?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Packet.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">sslv3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '15, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/3811f6e667571aac1c38e086a6e9b07f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benneharli&#39;s gravatar image" /><p>benneharli<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benneharli has no accepted answers">0%</span></p></img></div></div><div id="comments-container-39325" class="comments-container"></div><div id="comment-tools-39325" class="comment-tools"></div><div class="clear"></div><div id="comment-39325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39330"></span>

<div id="answer-container-39330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39330-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the tracefile, the client is the one closing the connection with a FIN. Sometimes after receiving the "ServerHello", sometimes even before sending the "ClientHello". This should be looked into.</p><p>The TCP/RST you are seeing is not the problem itself, but is also not correct. When the client sends the FIN, it means it will not transmit data itself anymore, but it should accept data from the server. When the server sends the first part of the "Certificate" message (frame 22), the client responds with the TCP/RST (frame 22). This is not compliant to the TCP RFC.</p><p>One thing that might trigger this behavior on the client is the fact that the server starts the TCP session with a window size of 0 and then after the 3-way-handshake increases the window size to a normal value. Which is compliant to the TCP RFC, but still unusual behavior.</p><p>So the combination of TCP implementations might be the culprit here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '15, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '15, 01:17</p></div></div><div id="comments-container-39330" class="comments-container"><span id="39332"></span><div id="comment-39332" class="comment"><div id="post-39332-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'll look into this, and see what I find.</p></div><div id="comment-39332-info" class="comment-info"><span class="comment-age">(21 Jan '15, 01:39)</span> benneharli</div></div><span id="39333"></span><div id="comment-39333" class="comment"><div id="post-39333-score" class="comment-score"></div><div class="comment-text"><p>I guess this is what you refer to?</p><p><a href="http://wiki.wireshark.org/TCP%20ZeroWindow">http://wiki.wireshark.org/TCP%20ZeroWindow</a></p></div><div id="comment-39333-info" class="comment-info"><span class="comment-age">(21 Jan '15, 01:46)</span> benneharli</div></div><span id="39334"></span><div id="comment-39334" class="comment"><div id="post-39334-score" class="comment-score"></div><div class="comment-text"><p>Yes it is, however, the article handles the case where during a data transfer, the window size decreases until it reached zero, meaning the receiver of the data is not able to fetch the data from the TCP receive buffer quickly enough.</p><p>In your case, the embedded system starts with a zero window, which is peculiar, but not forbidden. Maybe it wants to reserve resources by waiting for the 3-way handshake to complete before allocating memory buffers.</p></div><div id="comment-39334-info" class="comment-info"><span class="comment-age">(21 Jan '15, 02:23)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-39330" class="comment-tools"></div><div class="clear"></div><div id="comment-39330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

