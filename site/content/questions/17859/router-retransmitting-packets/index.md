+++
type = "question"
title = "router retransmitting packets"
description = '''I would like help figuring out the cause &amp;amp; solution to a packet retransmission issue. I am getting lots of &quot;TCP out-of order&quot;, &quot;TCP DUP-ACK&quot;, &amp;amp; &quot;TCP Retransmission&quot;. This occurs mostly (90%) between two devices communicating within the same VLAN. So client A (192.168.12.151) sends message to...'''
date = "2013-01-22T07:26:00Z"
lastmod = "2013-01-22T08:10:00Z"
weight = 17859
keywords = [ "dup-ack", "out-of-order", "tcp", "retransmission" ]
aliases = [ "/questions/17859" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [router retransmitting packets](/questions/17859/router-retransmitting-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17859-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like help figuring out the cause &amp; solution to a packet retransmission issue. I am getting lots of "TCP out-of order", "TCP DUP-ACK", &amp; "TCP Retransmission". This occurs mostly (90%) between two devices communicating within the same VLAN. So client A (192.168.12.151) sends message to client B (192.168.12.100), through a Sonicwall router (192.168.11.200). Sonicwall router set up 4 VLANS, trunk to Layer 3 switch. Cisco switch has 4 VLANs.</p><p>You can see packet 8 send the packet from 151 to 100. But, packet 9, the router replaces the mac address, the source is now the router</p><p>Any ideas?</p><pre><code>Packet 8
Internet Protocol, Src: 192.168.12.151 (192.168.12.151), Dst: 192.168.12.100 (192.168.12.100)
Ethernet II, Src: Crestron_2a:0c:c6 (00:10:7f:2a:0c:c6), Dst: Crestron_1f:3f:42 (00:10:7f:1f:3f:42)
8   1.049321    192.168.12.151  192.168.12.100  TCP 49157 &gt; crestron-cip [PSH, ACK] Seq=1 Ack=1 Win=62 Len=5

Packet 9
Internet Protocol, Src: 192.168.12.151 (192.168.12.151), Dst: 192.168.12.100 (192.168.12.100)
Ethernet II, Src: Sonicwal_90:ee:c2 (00:17:c5:90:ee:c2), Dst: Crestron_1f:3f:42 (00:10:7f:1f:3f:42)
9   1.049394    192.168.12.151  192.168.12.100  TCP [TCP Out-Of-Order] 49157 &gt; crestron-cip [PSH, ACK] Seq=1 Ack=1 Win=62 Len=5</code></pre></div><div id="question-tags" class="tags-container tags">dup-ack out-of-order tcp retransmission</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/9bdac699e0d71f235c4cd47903364866?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scubagreg67&#39;s gravatar image" /><p>Scubagreg67<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scubagreg67 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '13, 07:31</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-17859" class="comments-container"></div><div id="comment-tools-17859" class="comment-tools"></div><div class="clear"></div><div id="comment-17859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17860"></span>

<div id="answer-container-17860" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17860-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming here that you have a pretty small subnet defined to force the traffic through the SonicWall box. What you're seeing is 100% normal. L3 routers replace the MAC as the IP packet traverses through it. They also decrement the TTL in the IP header, which I'm sure you'll see as well.</p><p>Chances are, you are capturing the same packet twice (as evidenced by the different mac address but same packet) and Wireshark is interpreting it as a retransmission (because it saw it twice).</p><p>So try capturing from just one subnet and see where that takes you. You didn't mention the original problem, though. Are you trying to troubleshoot a specific problem?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-17860" class="comments-container"><span id="17861"></span><div id="comment-17861" class="comment"><div id="post-17861-score" class="comment-score"></div><div class="comment-text"><p>I am seeing the comms between two devices drop out, then come back anywhere from 20 minutes to 1.5 hours later.</p><p>The main device in question is an automation controller. it uses IP tables to establish rules for "allowed" connected clients. The controller has about 20 devices that all but 5 stay connected. The controller stays online, but comms between these 2/3 devices only keep dropping. Here is a error log from controller exhibiting the same exact issue.</p><pre><code>PAC2&gt;ipt
IP Table:
CIP_ID  Type    Status     DevID  Port   IP Address/SiteName
    E0  CIP     UNKNOWN           41794  192.168.012.102
    F9  CIP     ONLINE            41794  172.031.001.140
    FA  CIP     ONLINE            41794  172.031.001.140
    FB  CIP     ONLINE            41794  172.031.001.140
    FC  CIP     ONLINE            41794  172.031.001.140
    FD  CIP     ONLINE            41794  172.031.001.140

PAC2&gt;

84. Warning: Ethernet Device Slot-03.IP-ID-FA Not Responding (IP = 172.31.1.140). Device Offline
     TimeStamp: 11:18:53  1-17-13   UpTime: 5 days 19:50:23.78  Task: CIPretx 
 85. Warning: Ethernet Device Slot-03.IP-ID-FB Not Responding (IP = 172.31.1.140). Device Offline
     TimeStamp: 11:18:56  1-17-13   UpTime: 5 days 19:50:27.18  Task: CIPretx 
 86. Warning: Ethernet Device Slot-03.IP-ID-FC Not Responding (IP = 172.31.1.140). Device Offline
     TimeStamp: 11:18:56  1-17-13   UpTime: 5 days 19:50:27.38  Task: CIPretx 
 87. Warning: Ethernet Device Slot-03.IP-ID-FD Not Responding (IP = 172.31.1.140). Device Offline
     TimeStamp: 11:18:57  1-17-13   UpTime: 5 days 19:50:27.58  Task: CIPretx 
 88. Notice: CIP device fa: back ONLINE
     TimeStamp: 11:19:52  1-17-13   UpTime: 5 days 19:51:22.47  Task: UDP_Serv
 89. Notice: CIP device fb: back ONLINE
     TimeStamp: 11:19:52  1-17-13   UpTime: 5 days 19:51:22.48  Task: UDP_Serv
 90. Notice: CIP device fc: back ONLINE
     TimeStamp: 11:19:52  1-17-13   UpTime: 5 days 19:51:22.48  Task: UDP_Serv
 91. Notice: CIP device fd: back ONLINE
     TimeStamp: 11:19:52  1-17-13   UpTime: 5 days 19:51:22.49  Task: UDP_Serv
 92. Warning: Lost Ethernet link on LAN A. (flags = 1) 
     TimeStamp: 11:44:12  1-17-13   UpTime: 5 days 20:15:43.21  Task: EnetLISR
 93. Warning: IP Address released/expired from server 192.168.202.20
     TimeStamp: 11:44:13  1-17-13   UpTime: 5 days 20:15:44.22  Task: CIP Ping
 94. Warning: Ethernet Device Slot-03.IP-ID-FA Not Responding (IP = 172.31.1.140). DHCP Address was Released.
     TimeStamp: 11:44:13  1-17-13   UpTime: 5 days 20:15:44.23  Task: CIP Ping
 95. Warning: Ethernet Device Slot-03.IP-ID-FB Not Responding (IP = 172.31.1.140). DHCP Address was Released.
     TimeStamp: 11:44:13  1-17-13   UpTime: 5 days 20:15:44.24  Task: CIP Ping
 96. Warning: Ethernet Device Slot-03.IP-ID-FC Not Responding (IP = 172.31.1.140). DHCP Address was Released.
     TimeStamp: 11:44:13  1-17-13   UpTime: 5 days 20:15:44.25  Task: CIP Ping
 97. Warning: Ethernet Device Slot-03.IP-ID-FD Not Responding (IP = 172.31.1.140). DHCP Address was Released.
     TimeStamp: 11:44:13  1-17-13   UpTime: 5 days 20:15:44.26  Task: CIP Ping
 98. Notice: Link established on LAN A
     TimeStamp: 11:45:37  1-17-13   UpTime: 5 days 20:17:07.57  Task: PhyInitA
 99. Notice: New Address obtained from 192.168.202.20
     TimeStamp: 11:45:38  1-17-13   UpTime: 5 days 20:17:08.59  Task: DHCPRedo
100. Notice: Primary Hostname Resolution Configured To Use DNS
     TimeStamp: 11:45:40  1-17-13   UpTime: 5 days 20:17:11.33  Task: CIP Ping
Total Errors Logged = 2110</code></pre></div><div id="comment-17861-info" class="comment-info"><span class="comment-age">(22 Jan '13, 09:01)</span> Scubagreg67</div></div><span id="17873"></span><div id="comment-17873" class="comment"><div id="post-17873-score" class="comment-score"></div><div class="comment-text"><p>The ip addresses in your capture file, are nowhere in the logs !?! So, how are the two pieces of information related to each other?</p></div><div id="comment-17873-info" class="comment-info"><span class="comment-age">(22 Jan '13, 15:07)</span> Kurt Knochner ♦</div></div><span id="40054"></span><div id="comment-40054" class="comment"><div id="post-40054-score" class="comment-score"></div><div class="comment-text"><p>Did this ever get resolved I am having similar errors with a crestron device.</p></div><div id="comment-40054-info" class="comment-info"><span class="comment-age">(24 Feb '15, 13:14)</span> yert</div></div></div><div id="comment-tools-17860" class="comment-tools"></div><div class="clear"></div><div id="comment-17860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

