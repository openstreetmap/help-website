+++
type = "question"
title = "Connection drop issue"
description = '''I am having a desktop application which can talk to a server application using TCP/IP. It was working all these days but now we ran into an issue. The log message in the server shows that the socket is disconnected after a while, but we are able to exchange heart beat messages even after that. When ...'''
date = "2011-09-20T00:48:00Z"
lastmod = "2011-09-20T01:10:00Z"
weight = 6455
keywords = [ "rst", "ack", "sockets" ]
aliases = [ "/questions/6455" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connection drop issue](/questions/6455/connection-drop-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6455-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having a desktop application which can talk to a server application using TCP/IP. It was working all these days but now we ran into an issue. The log message in the server shows that the socket is disconnected after a while, but we are able to exchange heart beat messages even after that. When i ran the Wireshark tool i am getting this log which i dont know how to interpret.</p><pre><code>4297    36.375489   192.168.1.135   50.19.123.218   TCP bvcontrol &gt; 843 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1
4324    36.613058   50.19.123.218   192.168.1.135   TCP 843 &gt; bvcontrol [RST, ACK] Seq=1 Ack=1 Win=0 Len=0
4347    37.060445   192.168.1.135   50.19.123.218   TCP bvcontrol &gt; 843 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1
4427    37.297452   50.19.123.218   192.168.1.135   TCP 843 &gt; bvcontrol [RST, ACK] Seq=3393086915 Ack=1 Win=0 Len=0
4453    37.764487   192.168.1.135   50.19.123.218   TCP bvcontrol &gt; 843 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1</code></pre></div><div id="question-tags" class="tags-container tags">rst ack sockets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '11, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/553cd8674d3587e0a1556111261f4ea9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeeva&#39;s gravatar image" /><p>Jeeva<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeeva has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '11, 06:48</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6455" class="comments-container"></div><div id="comment-tools-6455" class="comment-tools"></div><div class="clear"></div><div id="comment-6455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6456"></span>

<div id="answer-container-6456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6456-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a regular output when the client tries to connect to the server, but the server does not accept an incoming connection. You see the client initiating the TCP connection in the first packet, by sending a SYN. Normally the server would react by sending a SYN,ACK himself - but here in packet two you see the server sending back a Reset flagged packet (RST,ACK).</p><p>This means either the server does not have the application listening on port 843 (check with netstat on the server), or there might be another device in place (firewall, ACL router...) filtering traffic and reacting to connections on port 843 with sending back Reset.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '11, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-6456" class="comments-container"><span id="6457"></span><div id="comment-6457" class="comment"><div id="post-6457-score" class="comment-score"></div><div class="comment-text"><p>Thank you Landi for your response, actually i am not able to put a picture here to show you the complete log that is why it is totaly misleading. After initial connection i am getting SYN,ACK after a while when the connection is dropped i am getting this log message</p></div><div id="comment-6457-info" class="comment-info"><span class="comment-age">(20 Sep '11, 02:39)</span> Jeeva</div></div><span id="6459"></span><div id="comment-6459" class="comment"><div id="post-6459-score" class="comment-score"></div><div class="comment-text"><p>Which actually points to the application on port 843 running on the server has crashed or because of whatever reasons stopped working. There is no other reason why the server should send back Reset packets, except for those 2 previously mentioned.</p></div><div id="comment-6459-info" class="comment-info"><span class="comment-age">(20 Sep '11, 04:42)</span> Landi</div></div><span id="19019"></span><div id="comment-19019" class="comment"><div id="post-19019-score" class="comment-score"></div><div class="comment-text"><p>RST packet after SYNC only 2 reason for that 1.Server not reachable. 2.Server taking long time to respond.</p></div><div id="comment-19019-info" class="comment-info"><span class="comment-age">(01 Mar '13, 02:34)</span> m_1607</div></div><span id="19037"></span><div id="comment-19037" class="comment"><div id="post-19037-score" class="comment-score"></div><div class="comment-text"><blockquote><p>RST packet after SYNC only 2 reason for that 1.Server not reachable.</p></blockquote><p>actually: no.</p><p>If the <strong>server</strong> (the system) is not reachable you will either run into a timeout (firewall dropped packet, last hop - the system - not online) or you will get some ICMP error, if the network is not reachable and that ICMP packet makes it through to your client.</p><blockquote><p>2.Server taking long time to respond.</p></blockquote><p>actually: no.</p><p>If the server <strong>takes a long time to answer</strong> you will eventually get an answer <strong>after a long time</strong> and not a RESET.</p></div><div id="comment-19037-info" class="comment-info"><span class="comment-age">(01 Mar '13, 09:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-6456" class="comment-tools"></div><div class="clear"></div><div id="comment-6456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

