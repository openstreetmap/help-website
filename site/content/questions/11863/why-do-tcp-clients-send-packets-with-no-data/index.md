+++
type = "question"
title = "Why do TCP clients send packets with no data?"
description = '''After the TCP connection between server and client establishes, I&#x27;m seeing a lot of TCP packets with no length like the one below, where 172.16.80.65 is the client and 172.16.178.77 is the server: 70 1.064245 172.16.80.65 172.16.178.77 TCP cvspserver &amp;gt; 60000 [ACK] Seq=1112 Ack=33028 Win=65535 Len...'''
date = "2012-06-12T20:12:00Z"
lastmod = "2012-06-13T01:46:00Z"
weight = 11863
keywords = [ "tcp", "analysis" ]
aliases = [ "/questions/11863" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why do TCP clients send packets with no data?](/questions/11863/why-do-tcp-clients-send-packets-with-no-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11863-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After the TCP connection between server and client establishes, I'm seeing a lot of TCP packets with no length like the one below, where 172.16.80.65 is the client and 172.16.178.77 is the server:</p><pre><code>70  1.064245    172.16.80.65    172.16.178.77   TCP cvspserver &gt; 60000 [ACK] Seq=1112 Ack=33028 Win=65535 Len=0
detail:Frame 74 (60 bytes on wire, 60 bytes captured)</code></pre><p>I determined the 60 bytes are from:</p><pre><code>20 bytes TCP header + 20 bytes IP header + 14 bytes Ethernet + 6 bytes Trailer</code></pre><p>Do these packets belong to the TCP/IP protocol? If so, what's their purpose? and why are they sent so frequently? (perhaps to maintain or check the connection between server and clients)</p><p><strong>UPDATE:</strong></p><p>Hi,you guys should have a look on this picture:(server 80.77 is linux,client 80.65 is WindowsXp) (1)surely,No.1,No.2 and No.3 mean TCP three-way handshaking. (2)No.4 means a message from my client application.(just like a login message req) (3)Focus on No.5 and No.7,actually my server application doesn't send these packets and only send No.6 to reply the No.4's login req. (4)Focus on No.14 and No.18,I also have no idea about these kind of packets that came from client 80.65. So,Is there any veteran could give me an understandable answer.Too many thanks! <img src="https://osqa-ask.wireshark.org/upfiles/tcp_catch.bmp" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcp analysis</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '12, 20:12</strong></p><img src="https://secure.gravatar.com/avatar/eb9828f2ae3d482ad932d4192f555a4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="waterjacky&#39;s gravatar image" /><p>waterjacky<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="waterjacky has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '12, 20:23</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11863" class="comments-container"></div><div id="comment-tools-11863" class="comment-tools"></div><div class="clear"></div><div id="comment-11863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11865"></span>

<div id="answer-container-11865" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11865-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is a TCP/IP packet that has to do with maintaining the connection. "[ACK]" indicates that this packet has the ACK bit set. 172.16.80.65 is acknowledging data from 172.16.178.77. The Ack number of 33028 means that it has successfully received data through byte 33027, and it expects byte 33028 next. The data length is zero because 192.16.80.65 is only acknowledging data; it is not sending any data.</p><p>There are other circumstances in which a system will send TCP packets with zero length. You will need a TCP/IP reference. <a href="http://www.tcpipguide.com/free/index.htm">The TCP/IP Guide</a> is a little awkward to use, but it's online and free.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '12, 22:33</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-11865" class="comments-container"><span id="11884"></span><div id="comment-11884" class="comment"><div id="post-11884-score" class="comment-score"></div><div class="comment-text"><p>Have a look on my answer,there are some concrete discription, thanks.</p></div><div id="comment-11884-info" class="comment-info"><span class="comment-age">(13 Jun '12, 19:53)</span> waterjacky</div></div></div><div id="comment-tools-11865" class="comment-tools"></div><div class="clear"></div><div id="comment-11865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11866"></span>

<div id="answer-container-11866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11866-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packets with an ACK flag and 0 size can be TCP Keepalive packets. So (usually) no need to worry about those.</p><p>See <a href="http://tools.ietf.org/html/rfc1122#page-101">RFC 1122 - 4.2.3.6 TCP Keep-Alives</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '12, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '12, 03:37</p></div></div><div id="comments-container-11866" class="comments-container"><span id="11868"></span><div id="comment-11868" class="comment"><div id="post-11868-score" class="comment-score"></div><div class="comment-text"><p>If the packet is a normal ACK or used as a Keep-Alive can be determined by looking at the SEQ of the packet:</p><pre><code>Such a segment generally contains SEG.SEQ = SND.NXT-1 and
may or may not contain one garbage octet of data.</code></pre><p>(from the RFC)</p></div><div id="comment-11868-info" class="comment-info"><span class="comment-age">(13 Jun '12, 04:10)</span> SYN-bit ♦♦</div></div><span id="11869"></span><div id="comment-11869" class="comment"><div id="post-11869-score" class="comment-score"></div><div class="comment-text"><p>You're right. However, the TCP Keep-Alive section contains a lot "could", "should", "some", "however" and "unfortunately".</p><p>Especially the section about the mentioned SEQ number starts with</p><blockquote><p><strong><code>Some TCP implementations</code></strong> <code>, however, have included a keep-alive mechanism.</code></p></blockquote><p>I would not bet on that SEQ calculation mechanism ;-)</p></div><div id="comment-11869-info" class="comment-info"><span class="comment-age">(13 Jun '12, 04:22)</span> Kurt Knochner ♦</div></div><span id="11871"></span><div id="comment-11871" class="comment"><div id="post-11871-score" class="comment-score"></div><div class="comment-text"><p>It's always nice to discuss RFC interpretations, as they do leave room for discussion even though they have been formulated carefully.</p><p>The way I read that part of the RFC is that there is no Keep-Alive implementation in the TCP protocol, but some systems have implemented a Keep-Alive mechanism by sending a packet with SEG.SEQ = SND.NXT-1 forcing the other side to send an ACK. However, some implementations do not send the ACK for an empty packet, so that one garbage octet (as it is outside the RCV window) is used to force the ACK from the other side.</p><p>This is in line with what I have seen live</p></div><div id="comment-11871-info" class="comment-info"><span class="comment-age">(13 Jun '12, 04:35)</span> SYN-bit ♦♦</div></div><span id="11872"></span><div id="comment-11872" class="comment"><div id="post-11872-score" class="comment-score"></div><div class="comment-text"><p>I have not seen any systems sending out ACK's by themselves with SEG.SEQ = SND.NXT as a Kaap-Alive mechanism. Have you? Do you have a trace you can share? It is always nice to broaden one's mind :-)</p><p>Funny though, I was at a customer this week who saw 15-20% retransmissions on a windows system (based on the TCP stats of the interface).</p><p>A little trace showed Keep-Alive packets. So Windows 2008R2 is not able to distinguish between a retransmission and a Keep-Alive (with one octet garbage).</p></div><div id="comment-11872-info" class="comment-info"><span class="comment-age">(13 Jun '12, 04:40)</span> SYN-bit ♦♦</div></div><span id="11873"></span><div id="comment-11873" class="comment"><div id="post-11873-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Have you? Do you have a trace you can share? It is always nice to broaden one's mind :-)</p></blockquote><p>I'm searching one :-) Hold on ....</p></div><div id="comment-11873-info" class="comment-info"><span class="comment-age">(13 Jun '12, 04:42)</span> Kurt Knochner ♦</div></div><span id="11883"></span><div id="comment-11883" class="comment not_top_scorer"><div id="post-11883-score" class="comment-score"></div><div class="comment-text"><p>Have a look on my answer,there are some concrete discription, thanks.</p></div><div id="comment-11883-info" class="comment-info"><span class="comment-age">(13 Jun '12, 19:52)</span> waterjacky</div></div><span id="11973"></span><div id="comment-11973" class="comment not_top_scorer"><div id="post-11973-score" class="comment-score"></div><div class="comment-text"><p>RFC 1122 specifies that keep-alive packets must only be sent when a certain (undefined) interval has passed. In the graphic, it appears that the time column is formatted for seconds since beginning of capture, in which case all zero-length ACKs from the client are seen within just over 1 ms of the preceding packet, and all zero-length ACKs from the server are seen within well under 1 ms of the preceding packet. I'd say these are normal ACKs, not keep-alives. It's extremely unlikely that a TCP implementation considers the connection "idle" after less than 1 ms.</p></div><div id="comment-11973-info" class="comment-info"><span class="comment-age">(15 Jun '12, 13:26)</span> Jim Aragon</div></div></div><div id="comment-tools-11866" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-11866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

