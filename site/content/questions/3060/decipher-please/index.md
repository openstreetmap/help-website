+++
type = "question"
title = "Decipher please"
description = '''Can anyone help me with defining what is happening with this packet. Here are the results; Frame 30 2.759459 192.168.1.27 192.168.19.14 TCP 51132 &amp;gt; 44000 [PSH, ACK Seq=1 Ack=1 Win=262140 Len=148 Frame 31 3.058855 192.168.1.27 192.168.19.14 CTP [TCP Reransmission] 51132 &amp;gt; 44000 [PSH, ACK Seq=1 ...'''
date = "2011-03-23T13:38:00Z"
lastmod = "2011-03-23T16:32:00Z"
weight = 3060
keywords = [ "post", "wireshark", "first" ]
aliases = [ "/questions/3060" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decipher please](/questions/3060/decipher-please)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3060-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone help me with defining what is happening with this packet. Here are the results;</p><p>Frame 30 2.759459 192.168.1.27 192.168.19.14 TCP 51132 &gt; 44000 [PSH, ACK Seq=1 Ack=1 Win=262140 Len=148</p><p>Frame 31 3.058855 192.168.1.27 192.168.19.14 CTP [TCP Reransmission] 51132 &gt; 44000 [PSH, ACK Seq=1 Ack=1 Win=262140 Len=148</p><p>Frame 102 12.153875 192.168.19.14 192.168.1.27 TCP 44000 &gt; 51132 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0 MSS=1460 SACK_PERM=1 WS=2</p><p>I have another Retransmission and then a TreeDisconnect Request 3 Frames later.</p></div><div id="question-tags" class="tags-container tags">post wireshark first</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '11, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/4d6a3a30db58bacca74ab259f0732e28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zevans2001&#39;s gravatar image" /><p>zevans2001<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zevans2001 has no accepted answers">0%</span></p></div></div><div id="comments-container-3060" class="comments-container"></div><div id="comment-tools-3060" class="comment-tools"></div><div class="clear"></div><div id="comment-3060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3067"></span>

<div id="answer-container-3067" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3067-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Typically, it's easier if you post the pcap file somwehere. In this case, frame 30 is sent after the three-way TCP handshake. You're using relative sequence numbers, and previous frames are not present so it's impossible to be sure, but since the ACK and SEQ are at 1, I'll assume this is the start of the conversation.<br />
</p><p>After frame 30 is sent, a response is not seen from .14. So .27 retransmits the frame after tcp retransmission timer (of approx 300ms) goes off.</p><p>Frame 102 is the response to a SYN sent by .27. So the question is, why didn't we see the SYN packet? Most likely, the span port was inundated and dropped the packet, capturing machine keep up, or you simply missed it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-3067" class="comments-container"></div><div id="comment-tools-3067" class="comment-tools"></div><div class="clear"></div><div id="comment-3067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3069"></span>

<div id="answer-container-3069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3069-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmmmm .....</p><p>The post shows a very short extract from your tracefile. Alas, the packets are completely out of context.</p><p>Frame 30 shows 192.168.1.27 sending 148 byte to 192.168.19.14.</p><p>Frame 31 shows that the sender did not get the expected acknowledgement from the receiver. So 192.168.1.27 decides to send the same 148 byte again. This is called a retransmission. It's a service provided by TCP for the application.</p><p>Frame 102 belongs to a connection setup happening between your two systems. The connection was initiated by 192.168.1.27 and this packet shows .19.14's response. This packet is certainly send because somewhere between packets 31 and 102 the previous session was terminated. If all packets from the conversation were recorded you should see packets with the FIN or RST bit set.</p><hr /><p>The retransmissions happen, because either the packet from the sender or the acknowledgment from the receiver were dropped. The cause of the drop is absolutely unclear from that short snippet.</p><p>From frames 30 and 31 alone I can not tell, if the 148 byte ultimately made it to the destination</p><hr /><p>The Tree Disconnect probably belongs to an SMB session running on port 139 or 445. That would be a workstation saying "good bye" to a Windows (or Linux/Samba) file server.</p><hr /><p>That "deciphers" your three packets. I'm afraid, unless you provide a bit more background information this won't really help.</p><p>I suggest to look at the <a href="http://www.wireshark.org/docs/wsug_html_chunked/index.html">Wireshark Users guide</a> or browse through the <a href="http://wiki.wireshark.org/">Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-3069" class="comments-container"><span id="3119"></span><div id="comment-3119" class="comment"><div id="post-3119-score" class="comment-score"></div><div class="comment-text"><p>Here is the capture in plain text. Can you help:</p><p>No. Time Source Destination Protocol Info 45 9.206394 192.168.1.27 192.168.19.14 TCP 53710 &gt; 44000 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=2 SACK_PERM=1</p><p>Frame 45: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) Ethernet II, Src: Dell_9f:db:d9 (b8:ac:6f:9f:db:d9), Dst: Adtran_3d:a1:98 (00:a0:c8:3d:a1:98) Internet Protocol, Src: 192.168.1.27 (192.168.1.27), Dst: 192.168.19.14 (192.168.19.14) Transmission Control Protocol, Src Port: 53710 (53710), Dst Port: 44000 (44000), Seq: 0, Len: 0</p><p>No. Time Source Destination Protocol Info 46 9.208663 192.168.19.14 192.168.1.27 TCP 44000 &gt; 53710 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0 MSS=1460 SACK_PERM=1 WS=2</p><p>Frame 46: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) Ethernet II, Src: Adtran_3d:a1:98 (00:a0:c8:3d:a1:98), Dst: Dell_9f:db:d9 (b8:ac:6f:9f:db:d9) Internet Protocol, Src: 192.168.19.14 (192.168.19.14), Dst: 192.168.1.27 (192.168.1.27) Transmission Control Protocol, Src Port: 44000 (44000), Dst Port: 53710 (53710), Seq: 0, Ack: 1, Len: 0</p><p>No. Time Source Destination Protocol Info 47 9.208720 192.168.1.27 192.168.19.14 TCP 53710 &gt; 44000 [ACK] Seq=1 Ack=1 Win=262140 Len=0</p><p>Frame 47: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) Ethernet II, Src: Dell_9f:db:d9 (b8:ac:6f:9f:db:d9), Dst: Adtran_3d:a1:98 (00:a0:c8:3d:a1:98) Internet Protocol, Src: 192.168.1.27 (192.168.1.27), Dst: 192.168.19.14 (192.168.19.14) Transmission Control Protocol, Src Port: 53710 (53710), Dst Port: 44000 (44000), Seq: 1, Ack: 1, Len: 0</p><p>No. Time Source Destination Protocol Info 51 9.470464 192.168.1.27 192.168.19.14 TCP 53710 &gt; 44000 [PSH, ACK] Seq=1 Ack=1 Win=262140 Len=148</p><p>Frame 51: 202 bytes on wire (1616 bits), 202 bytes captured (1616 bits) Ethernet II, Src: Dell_9f:db:d9 (b8:ac:6f:9f:db:d9), Dst: Adtran_3d:a1:98 (00:a0:c8:3d:a1:98) Internet Protocol, Src: 192.168.1.27 (192.168.1.27), Dst: 192.168.19.14 (192.168.19.14) Transmission Control Protocol, Src Port: 53710 (53710), Dst Port: 44000 (44000), Seq: 1, Ack: 1, Len: 148 Data (148 bytes)</p><p>0000 80 92 01 03 01 00 69 00 00 00 20 00 00 39 00 00 ......i... ..9.. 0010 38 00 00 35 00 00 16 00 00 13 00 00 0a 07 00 c0 8..5............ 0020 00 00 33 00 00 32 00 00 2f 00 00 07 05 00 80 03 ..3..2../....... 0030 00 80 00 00 66 00 00 05 00 00 04 01 00 80 08 00 ....f........... 0040 80 00 00 63 00 00 62 00 00 61 00 00 15 00 00 12 ...c..b..a...... 0050 00 00 09 06 00 40 00 00 65 00 00 64 00 00 60 00 [email protected]`. 0060 00 14 00 00 11 00 00 08 00 00 06 04 00 80 00 00 ................ 0070 03 02 00 80 af 2b 19 8b 51 68 02 f9 df 9a 1e 9d .....+..Qh...... 0080 36 7d 70 a8 54 0c 0b 0c e2 7a 55 cf 37 2c 59 16 6}p.T....zU.7,Y. 0090 ab 9c f8 da ....</p><p>No. Time Source Destination Protocol Info 52 9.472640 192.168.19.14 192.168.1.27 TCP 44000 &gt; 53710 [ACK] Seq=1 Ack=149 Win=6912 Len=0</p><p>Frame 52: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) Ethernet II, Src: Adtran_3d:a1:98 (00:a0:c8:3d:a1:98), Dst: Dell_9f:db:d9 (b8:ac:6f:9f:db:d9) Internet Protocol, Src: 192.168.19.14 (192.168.19.14), Dst: 192.168.1.27 (192.168.1.27) Transmission Control Protocol, Src Port: 44000 (44000), Dst Port: 53710 (53710), Seq: 1, Ack: 149, Len: 0</p><p>No. Time Source Destination Protocol Info 53 9.662426 Dell_a9:c8:2c Broadcast ARP Who has 192.168.1.188? Tell 192.168.1.29</p></div><div id="comment-3119-info" class="comment-info"><span class="comment-age">(25 Mar '11, 07:04)</span> zevans2001</div></div><span id="3124"></span><div id="comment-3124" class="comment"><div id="post-3124-score" class="comment-score"></div><div class="comment-text"><p>These packets show a 3-way-handshake where the two systems establish their connection. That's happening in frames 45 through 47.</p><p>In frame 51 the initiator of the session (presumably the client) sends 148 byte to the remote system. In frame 52 the receiver acknowledges that the 148 byte.</p><p>Alas, I can not make sense from the content. You might want to identify which processes or applications are involved in the exchange. Assuming that 192.168.19.14 is a server of sorts I expect that a process is listening to port 44000.</p></div><div id="comment-3124-info" class="comment-info"><span class="comment-age">(25 Mar '11, 09:03)</span> packethunter</div></div><span id="3125"></span><div id="comment-3125" class="comment"><div id="post-3125-score" class="comment-score"></div><div class="comment-text"><p>On a Windows system running XP or later try <strong>netstat -ano</strong> to see the process id for the server process. Using the Task Manager you can find out which program is serving the port.</p></div><div id="comment-3125-info" class="comment-info"><span class="comment-age">(25 Mar '11, 09:03)</span> packethunter</div></div></div><div id="comment-tools-3069" class="comment-tools"></div><div class="clear"></div><div id="comment-3069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

