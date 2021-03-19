+++
type = "question"
title = "Slow NFS dup ack"
description = '''Hi, I am experiencing slow performance from my VNX NFS server (primarily reads). When performing a TCP capture on the VNX (server) and HP (client) I notice there are many &quot;dup ack&quot; and &quot;out of order&quot; packets. Currently I have jumbo frames configured on both the VNX and HP servers, I have been assure...'''
date = "2013-06-03T19:19:00Z"
lastmod = "2013-06-04T13:59:00Z"
weight = 21722
keywords = [ "dup-ack" ]
aliases = [ "/questions/21722" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow NFS dup ack](/questions/21722/slow-nfs-dup-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am experiencing slow performance from my VNX NFS server (primarily reads). When performing a TCP capture on the VNX (server) and HP (client) I notice there are many "dup ack" and "out of order" packets. Currently I have jumbo frames configured on both the VNX and HP servers, I have been assured that jumbo frames are configured on all switches between the devices. The only verification I can perform is a ping? (I'm not sure if this is a valid test?)</p><pre><code>[[email protected] ~]# ping -s 9000 10.230.61.77
PING 10.230.61.77 (10.230.61.77) 9000(9028) bytes of data.
9008 bytes from 10.230.61.77: icmp_seq=1 ttl=255 time=0.384 ms
9008 bytes from 10.230.61.77: icmp_seq=2 ttl=255 time=0.380 ms
9008 bytes from 10.230.61.77: icmp_seq=3 ttl=255 time=0.364 ms</code></pre><p>Here is a sample output from the client and server, any ideas what is causing this?</p><pre><code>NFS Server (VNX 5300)
New Column Time        Source                Destination           Protocol Length Info                                                            No.
   163 4.527343    10.230.61.77          10.230.61.9           TCP      62702  [TCP segment of a reassembled PDU]                              62702
   164 4.527343    10.230.61.77          10.230.61.9           NFS      3098   V3 READ Reply (Call In 162) Len:65536                           3098
   165 4.527343    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=545641 Win=10183 Len=0 TSval=326998566 TSecr=30912434 66
   166 4.527343    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=563537 Win=10183 Len=0 TSval=326998566 TSecr=30912434 66
   167 4.527343    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=581433 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   168 4.527343    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=593413 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   169 4.527343    10.230.61.9           10.230.61.77          NFS      230    V3 READ Call (Reply In 243), FH:0x0eefae18 Offset:1572864 Len:65536 230
   170 4.527343    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6905 Ack=611309 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   171 4.527343    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6905 Ack=629205 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   172 4.527343    10.230.61.77          10.230.61.9           TCP      62702  [TCP segment of a reassembled PDU]                              62702
   173 4.527343    10.230.61.77          10.230.61.9           NFS      3098   V3 READ Reply (Call In 107) Len:65536                           3098
   174 4.527343    10.230.61.9           10.230.61.77          TCP      78     760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=668029 78
   175 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#1] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=676977 78
   176 4.527343    10.230.61.77          10.230.61.9           TCP      9014   [TCP Out-Of-Order] [TCP segment of a reassembled PDU]           9014
   177 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#2] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=685925 78
   178 4.527343    10.230.61.77          10.230.61.9           TCP      9014   [TCP Out-Of-Order] [TCP segment of a reassembled PDU]           9014
   179 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#3] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=694873 78
   180 4.527343    10.230.61.77          10.230.61.9           TCP      3098   [TCP Out-Of-Order] [TCP segment of a reassembled PDU]           3098
   181 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#4] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=703821 78
   182 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#5] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=712769 78
   183 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#6] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=721717 78
   184 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#7] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=724749 78
   185 4.527343    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 174#8] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=733697 78

NFS Client (HP ProLiant DL360p Gen8)
New Column Time        Source                Destination           Protocol Length Info                                                            No.
   209 4.527618    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=545641 Win=10183 Len=0 TSval=326998566 TSecr=30912434 66
   210 4.527678    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   211 4.527750    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   212 4.527763    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=563537 Win=10183 Len=0 TSval=326998566 TSecr=30912434 66
   213 4.527822    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   214 4.527894    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   215 4.527907    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=581433 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   216 4.527978    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   217 4.527990    10.230.61.77          10.230.61.9           NFS      3098   V3 READ Reply (Call In 126) Len:65536                           3098
   218 4.527998    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6741 Ack=593413 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   219 4.528012    10.230.61.9           10.230.61.77          NFS      230    V3 READ Call (Reply In 340), FH:0x0eefae18 Offset:1572864 Len:65536 230
   220 4.528064    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   221 4.528136    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   222 4.528149    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6905 Ack=611309 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   223 4.528209    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   224 4.528281    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   225 4.528294    10.230.61.9           10.230.61.77          TCP      66     760 &gt; nfs [ACK] Seq=6905 Ack=629205 Win=10183 Len=0 TSval=326998567 TSecr=30912434 66
   226 4.528353    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   227 4.528426    10.230.61.77          10.230.61.9           TCP      9014   [TCP Previous segment not captured] [TCP segment of a reassembled PDU] 9014
   228 4.528438    10.230.61.9           10.230.61.77          TCP      78     760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=668029 78
   229 4.528498    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   230 4.528509    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#1] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=676977 78
   231 4.528570    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   232 4.528580    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#2] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=685925 78
   233 4.528642    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   234 4.528652    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#3] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=694873 78
   235 4.528715    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   236 4.528725    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#4] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998567 TSecr=30912434 SLE=659081 SRE=703821 78
   237 4.528787    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   238 4.528798    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#5] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=712769 78
   239 4.528870    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   240 4.528880    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#6] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=721717 78
   241 4.528884    10.230.61.77          10.230.61.9           NFS      3098   V3 READ Reply (Call In 206) Len:65536                           3098
   242 4.528889    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#7] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=724749 78
   243 4.528959    10.230.61.77          10.230.61.9           TCP      9014   [TCP segment of a reassembled PDU]                              9014
   244 4.528970    10.230.61.9           10.230.61.77          TCP      78     [TCP Dup ACK 228#8] 760 &gt; nfs [ACK] Seq=6905 Ack=638153 Win=10164 Len=0 TSval=326998568 TSecr=30912434 SLE=659081 SRE=733697 78</code></pre><ul><li>edit - akismet thinks im pasting spam :/ so here is my reply *</li></ul><p>Packet captures:- VNX <a href="http://cloudshark.org/captures/1f8ff433f45c">http://cloudshark.org/captures/1f8ff433f45c</a> HP server <a href="http://cloudshark.org/captures/5d0ae1a8c89f">http://cloudshark.org/captures/5d0ae1a8c89f</a></p><p>Here are the new pings, it looks like the packets are being fragmented after 8973 bytes? I know the servers are set to 9000 MTU and the switches are said to be set to 9044 MTU.</p><pre><code>[[email protected] ~]# ping -M do -s 8972 10.230.61.77
PING 10.230.61.77 (10.230.61.77) 8972(9000) bytes of data.
8980 bytes from 10.230.61.77: icmp_seq=1 ttl=255 time=0.351 ms
8980 bytes from 10.230.61.77: icmp_seq=2 ttl=255 time=0.367 ms
8980 bytes from 10.230.61.77: icmp_seq=3 ttl=255 time=0.347 ms

[[email protected] ~]# ping -M do -s 8973 10.230.61.77
PING 10.230.61.77 (10.230.61.77) 8973(9001) bytes of data.
From 10.230.61.9 icmp_seq=1 Frag needed and DF set (mtu = 9000)
From 10.230.61.9 icmp_seq=1 Frag needed and DF set (mtu = 9000)
From 10.230.61.9 icmp_seq=1 Frag needed and DF set (mtu = 9000)</code></pre><ul><li>edit 05/06/2013*</li></ul><p>Thanks very much for the input so far, it is evident that packets are being lost from 10.230.61.77 (VNX) to 10.230.61.9 (HP Server). I have managed to get the switch config for the ports where these devices patch into and I have noticed that we have flow control (pause enabled) for all the ports except the VNX which has flow control disabled. Isn't it best to enable flow control throughout?</p><p>The setup is as follows:- VNX -(10Gb)- switch -(10 Gb)- switch -(1 Gb)- HP Server</p><p>EMC VNX:-</p><pre><code>Broadcom 10 Gigabit Ethernet Controller
0:  fxg-1-0  IRQ: 24
txflowctl=disable rxflowctl=disable
Link: Up
0:  fxg-1-1  IRQ: 25
txflowctl=disable rxflowctl=disable
Link: Up</code></pre><p>VNX switch port:-</p><pre><code>interface port 1/28
pause enable
switchport mode trunk
switchport trunk add 10-11,20-21,4078
flooding dlf enable
flooding mc enable
flooding bc enable
flooding limit 100000</code></pre><p>HP switch port:-</p><pre><code>interface port 1/8
pause enable
switchport mode trunk
switchport trunk native 11
switchport trunk add 10</code></pre><p>HP Server:-</p><pre><code>[[email protected] ~]# ethtool -a eth4
Pause parameters for eth4:
Autonegotiate:  on
RX:             on
TX:             on</code></pre></div><div id="question-tags" class="tags-container tags">dup-ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '13, 19:19</strong></p><img src="https://secure.gravatar.com/avatar/1ce649a675fca2f5c781be34d79582c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elfelvin&#39;s gravatar image" /><p>elfelvin<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elfelvin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jun '13, 22:17</p></div></div><div id="comments-container-21722" class="comments-container"><span id="21724"></span><div id="comment-21724" class="comment"><div id="post-21724-score" class="comment-score"></div><div class="comment-text"><p>Could you upload the capture from a file to cloudshark and post the URL? Should be a lot easier to read through (<a href="http://cloudshark.org/).">http://cloudshark.org/).</a> Duplicate acks here effectively mean that 10.230.61.9 detects packet loss for this TCP session and is pushing for a retransmission.</p><p>For the ping test, could you try setting the do-not-fragment flag? I believe that's either <code>-M dont</code> or <code>-D</code> flag depending.</p></div><div id="comment-21724-info" class="comment-info"><span class="comment-age">(03 Jun '13, 19:32)</span> Quadratic</div></div><span id="21725"></span><div id="comment-21725" class="comment"><div id="post-21725-score" class="comment-score"></div><div class="comment-text"><p>I cannot add a comment, akismet thinks im pasting spam. I have edited the main post with details</p></div><div id="comment-21725-info" class="comment-info"><span class="comment-age">(03 Jun '13, 20:20)</span> elfelvin</div></div><span id="21726"></span><div id="comment-21726" class="comment"><div id="post-21726-score" class="comment-score"></div><div class="comment-text"><p>Thanks.</p><p>10.232.61.9 is saying that it has to fragment, which I believe is your HP client, since it's the IP with the false checksum errors in the client-side trace file. It might have negotiated PMTU from upstream, otherwise I'd check the network card settings and support for jumbo frames on that client.</p><p>From the "edited" name in the files, how have they been changed? There are ACKs for missing segments through the VNX trace, meaning that the traffic actually did happen but this capture file didn't get it. There is definitely actual packet loss observed from the client too, with those duplicate ACKs, despite the trace file not having all the packets that the two systems actually saw.</p><p>How is CPU looking on these systems during the performance issues? With a large amount of packets, all fragmented, the processor may be being taxed which could also explain why the local packet capture is missing packets that had to have happened (the acks for segments not in the trace).</p></div><div id="comment-21726-info" class="comment-info"><span class="comment-age">(03 Jun '13, 21:52)</span> Quadratic</div></div><span id="21757"></span><div id="comment-21757" class="comment"><div id="post-21757-score" class="comment-score"></div><div class="comment-text"><p>I still cannot post responses. I have updated my main post.</p></div><div id="comment-21757-info" class="comment-info"><span class="comment-age">(04 Jun '13, 22:23)</span> elfelvin</div></div><span id="21939"></span><div id="comment-21939" class="comment"><div id="post-21939-score" class="comment-score"></div><div class="comment-text"><p>I have compared a working NFS pcap to my "slow" one and noticed that after packet 30 (ie where the export gets mounted) there is no 3 way handshake with the NFS server and it seems like the window size is about ~24000 whereas the working capture is using a window size of ~139000. I am using the same client but to different VNX servers to test this scenario.</p><p>My question is, why / how is the NFS client still talking with the server even though there is no 3 way handshake? Is it possible that because this handshake is missing that the TCP window size was never updated, and this is what is causing my slow response?</p><p>The capture starts before I mount the export so there is no chance I would have missed it.</p><p>Any NFS gurus out there?</p></div><div id="comment-21939-info" class="comment-info"><span class="comment-age">(11 Jun '13, 19:25)</span> elfelvin</div></div><span id="21940"></span><div id="comment-21940" class="comment not_top_scorer"><div id="post-21940-score" class="comment-score"></div><div class="comment-text"><p>If you don't have the three-way handshake in the trace, how are you determining the receive window size? You need the handshake to say what the window scale factor is.</p><p>Was the session ever actually torn down? If you don't have the three-way handshake but see TCP data sent between the hosts, either the session already existed before you started the trace or the trace somehow did not capture the handshake. Rest assured, if there is no three-way handshake there is no TCP session, so it definitely happened if you're seeing TCP data segments.</p><p>Edit: I'm also going to delete my old answer since this isn't quite answered conclusively yet it appears. Can you post the comparison traces of good and bad? The "bad" trace you first uploaded definitely had packet loss, and determining the source of that will hopefully lead to the source of the problem. Moving Wireshark to the switch upstream from the client may be one possible way to start pinpointing it.</p></div><div id="comment-21940-info" class="comment-info"><span class="comment-age">(11 Jun '13, 20:16)</span> Quadratic</div></div><span id="26997"></span><div id="comment-26997" class="comment not_top_scorer"><div id="post-26997-score" class="comment-score"></div><div class="comment-text"><p>elfelvin - did you resolve this and if so, how? We have a similar issue with our VNX using 10Gb to talk to "HP" boxes.</p></div><div id="comment-26997-info" class="comment-info"><span class="comment-age">(14 Nov '13, 05:20)</span> ou812</div></div><span id="38367"></span><div id="comment-38367" class="comment not_top_scorer"><div id="post-38367-score" class="comment-score"></div><div class="comment-text"><p>Hi, Sorry for taking so long to reply, but the issue was with a buffer on the switch. Basically VNX 10G -&gt; 10G Swith -&gt; 1G Switch -&gt; 1G HP interface</p><p>I can't remember the exact switch metric but looking at the switch port statistics where the HP server was patched into I could see a metric relating to dropped packets incrementing. We spoke to the vendor and they acknowledged that going from a 10G switch to a 1G switch had this affect as the memory / buffer on the switch was not large enough to cope and thus it dropped the packets.</p><p>Regards, Elvin</p></div><div id="comment-38367-info" class="comment-info"><span class="comment-age">(05 Dec '14, 08:34)</span> elfelvin</div></div></div><div id="comment-tools-21722" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-21722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21749"></span>

<div id="answer-container-21749" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21749-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The traffic is going from the server (VNX) 10.230.61.77:2049 towards the client (HP) . The server is using tcp segmentation offload leaving it to the ethernet card to segment the data when it is sent over the ethernet. This actually does happen as the largest tcp.len that arrives at the client is tcp.len==8948 which fills the ip.len to a full jumbo frame. As the session negotiated the tcp sack option we can use the tcp.options.sack_le gt 0 filter to find all reports of a lost segment.</p><p>The first lost segment reported missing by the client is is tcp.seq == 638153. This 'segment' however was never seen as such at the VNX trace as tcp.dstport==760 and tcp.seq le 638153 shows. It was part of the 'large_send' segment with tcp.seq == 593413 and tcp.len == 62636. This is causing the wireshark logic to flag it as an "Out-of-Order" segment. BTW. "tcp segmentation offload" will also confuse wireshark by incoming acks for seq numbers that we never saw being sent...</p><p>Summary: The client trace clearly shows that packets are not arriving in the client's TCP stack. They are also missing in the clients trace, meaning they were never received from the interface. The missing packets are at the very end (#22-24) of a batch of 24 packets arriving basically at the same time. So, a good guess is that they are dropped because of a insufficient queue size on the interfaces along the path - possibly at the HP client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-21749" class="comments-container"></div><div id="comment-tools-21749" class="comment-tools"></div><div class="clear"></div><div id="comment-21749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

