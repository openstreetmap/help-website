+++
type = "question"
title = "TCP 3 way handshake data in third message"
description = '''Hi, I have both a Linux and a Windows application. Both behave in the same way when a client connects to a server. I have WIRESHARK captures where it is clear to see that both applications perform the 3 way handshake but add some data (24 bytes in case if Linux, 16 bytes in case of Windows). The six...'''
date = "2014-09-05T07:37:00Z"
lastmod = "2014-09-08T23:44:00Z"
weight = 36023
keywords = [ "data", "3-way", "tcp" ]
aliases = [ "/questions/36023" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP 3 way handshake data in third message](/questions/36023/tcp-3-way-handshake-data-in-third-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36023-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have both a Linux and a Windows application. Both behave in the same way when a client connects to a server. I have WIRESHARK captures where it is clear to see that both applications perform the 3 way handshake but add some data (24 bytes in case if Linux, 16 bytes in case of Windows). The sixteen bytes I see being included from the windows side are fairly logical: immediately after getting confirmation of the connection I send a 16 byte message (CASyncSocket::OnConnect event). Its exactly those 16 bytes I see. From the Linux side I recognize some of the bytes (for example: the port number the client will use/has connected to) but I can't find where it sends that info.</p><p>My most important question though is: is sending extra data along with the final ACK a usual thing to do? It does not seem to do any harm as everything works but I am still curious.</p></div><div id="question-tags" class="tags-container tags">data 3-way tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '14, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/87e4c9a110f3a8c793ecb55b74556099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fd9750&#39;s gravatar image" /><p>fd9750<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fd9750 has no accepted answers">0%</span></p></div></div><div id="comments-container-36023" class="comments-container"></div><div id="comment-tools-36023" class="comment-tools"></div><div class="clear"></div><div id="comment-36023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36025"></span>

<div id="answer-container-36025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36025-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This might be "<a href="http://lwn.net/Articles/508865/">tcp fast open</a>" handshakes.<br />
Does <code>cat /proc/sys/net/ipv4/tcp_fastopen</code> show a 1 on your linux?<br />
Can you post a sample to <a href="https://appliance.cloudshark.org/upload/">cloudshark.org</a>?<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '14, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-36025" class="comments-container"><span id="36026"></span><div id="comment-36026" class="comment"><div id="post-36026-score" class="comment-score"></div><div class="comment-text"><p>such a useful link,thanks mrEEde for sharing this link.</p></div><div id="comment-36026-info" class="comment-info"><span class="comment-age">(05 Sep '14, 10:11)</span> kishan pandey</div></div></div><div id="comment-tools-36025" class="comment-tools"></div><div class="clear"></div><div id="comment-36025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36095"></span>

<div id="answer-container-36095" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36095-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, in the mean time everything has become clear:</p><p>1) Waiting for a short period before returning the third ACK is apparently common practice on both the Windows and the Linux TCP/IP stacks. If you send data shortly after connecting (getting the second SYN/ACK message) it just rides along in the packet with the required third ACK. If you don't send data fast enough the third ACK gets sent in a separate package without data.</p><p>2) The 24 byte block that gets sent by the Linux side turns out to be application specific and was hidden in the example code I used to implement my own code. The "hiding" was caused by the fact that every other send action was done using the Linux "write" function while the one that sent the 24 bytes was done by means of the Linux "send" function. That one performs a write operation directly to the socket instead of going via the file descriptor used by the "write" function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '14, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/87e4c9a110f3a8c793ecb55b74556099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fd9750&#39;s gravatar image" /><p>fd9750<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fd9750 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-36095" class="comments-container"></div><div id="comment-tools-36095" class="comment-tools"></div><div class="clear"></div><div id="comment-36095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

