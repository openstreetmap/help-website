+++
type = "question"
title = "Slow upload speed from Windows stations to SSL hosts"
description = '''Hi there, Since 3 or 4 months ago, I&#x27;m facing a really strange problem in a network containing around 100 workstations running mixed OSes (Windows 7, MacOS and Linux). This problem consists in a very slow traffic when trying to upload files to some HTTPS website from Windows (and only from Windows!!...'''
date = "2014-12-29T06:48:00Z"
lastmod = "2014-12-30T05:35:00Z"
weight = 38768
keywords = [ "offload", "retransmissions", "tcp" ]
aliases = [ "/questions/38768" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow upload speed from Windows stations to SSL hosts](/questions/38768/slow-upload-speed-from-windows-stations-to-ssl-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>Since 3 or 4 months ago, I'm facing a really strange problem in a network containing around 100 workstations running mixed OSes (Windows 7, MacOS and Linux). This problem consists in a very slow traffic when trying to upload files to some HTTPS website from Windows (and only from Windows!!) workstations. A good reproducible test would be an upload to wetransfer.com or sendspace likely sites, where I get speeds around 5KB/s, taking like 6 hours to upload a 60MB file. Doing the same test (at the same time) from a Mac or Linux station, I get the full link speed (which is 50Mb/s), finishing the upload in less than a minute.</p><p>Trying to figure out the issue, I ran Wireshark in the router (a Debian Linux running iptables) where I noticed lots of TCP Retransmission coming from the Windows host as you can check in he link below:</p><p><a href="https://www.cloudshark.org/captures/277dec1b6152?filter=ip.src%3D%3D192.168.8.26">CloudShark Link</a></p><p>I know what does those retransmissions mean and that maybe this is the symptom of some other problem, but I can't understand why this only happen to Windows workstations. This problem is seriously affecting the job of the company since this makes impossible send emails with attachments, use Teamviewer for remote access and so on. Not less important, I tested one of the workstations connecting directly to the internet link with a public ip address, and then this problem simply has gone, as the issue would be directly related to my Linux firewall.</p><p>Thanks in advance for any help on that.</p><p>Best,</p><p>Danilo</p></div><div id="question-tags" class="tags-container tags">offload retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '14, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/bb846de9e6160b0a92b0abd277e97234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mussolini&#39;s gravatar image" /><p>Mussolini<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mussolini has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Dec '14, 13:40</p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-38768" class="comments-container"><span id="38773"></span><div id="comment-38773" class="comment"><div id="post-38773-score" class="comment-score">1</div><div class="comment-text"><p>I could see that windows workstation(192.168.8.26) is sending packet with tcp len with size more than standard mtu size along with DF bit set and your router is discarding them replying with icmp fragmentation needed message not sure if this icmp messages are delivered to source windows system because it keeps on sending larger mtu size packets.you can try disabling jumbo frame option on this system(192.168.8.26) and then give a try</p></div><div id="comment-38773-info" class="comment-info"><span class="comment-age">(29 Dec '14, 20:28)</span> kishan pandey</div></div><span id="38788"></span><div id="comment-38788" class="comment"><div id="post-38788-score" class="comment-score"></div><div class="comment-text"><p>Hi Kishan, Thanks for the reply. Actually I don't have jumbo frame set on this machine, it's just set to default. Neither all the other Windows workstations have jumbo frame set and they also behave like this.</p></div><div id="comment-38788-info" class="comment-info"><span class="comment-age">(30 Dec '14, 04:22)</span> Mussolini</div></div></div><div id="comment-tools-38768" class="comment-tools"></div><div class="clear"></div><div id="comment-38768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38793"></span>

<div id="answer-container-38793" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38793-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Mussolini,</p><p>you got quite an interesting trace file. I try to give my answer first, and then describe, how I came to the summary.</p><p><strong>Summary</strong></p><p>It could be, that the network card on your Debian box is reassembling TCP segments (i. e. individual IP packets) into one large segment and fails forwarding these packets. Fixing the problem would require a configuration in your Linux firewall / router.</p><p><strong>Detailed Analysis</strong></p><p>Based on the display filter provided in the link to cloudshark I assume that the windows machine is using the IP address 192.168.8.26. Unfortunately we don't have a packet that could be used as a finger print.</p><p>This system is visible with 2 TCP sessions in the trace file:</p><ul><li>A session on TCP port 3389 to 192.168.8.1 (probably your gateway / router / firewall)</li><li>A session on TCP port 443 to 54.231.9.49</li></ul><p>As a bonus - and already identified by kishan pandey as a potential indicator for trouble - we get 4 ICMP messages "fragmentation needed" (type 3, code 4).</p><p>As kishan already pointed out, the "fragmentation needed" messages are triggerd by abnormally large frames. Apply the filter <strong><code>ip.len &gt; 1500</code></strong> to see that 192.168.9.120 is also generating these messages.</p><p><strong>Background: Packet sizes</strong></p><p>Unless Jumbo Frames are used the maximum size of an IP packet is 1500 bytes. As 20 bytes are used the IP header and another 20 bytes are used for the TCP header this leaves 1460 bytes for application data. This value is called the "maximum segment size" (MSS).</p><p>The packet size might be reduced to accommodate PPPoE, IPsec or other headers. (We ignore TCP or IP options to keep things simple). Both endpoints of the TCP connection have to know how much data can be stuffed into a packet, so they exchange the MSS size during the handshake. You would see the value 1460 within your LAN or 1452 if the remote site is using PPPoE.</p><p><strong>Jumbo frames in the trace</strong></p><p>Unfortunately, the trace does not show the connection start for the two clients. So we don't know the maximum segment size. Still it is a safe bet to assume that the MSS is 1460 or less.</p><p><strong>TCP reassembly</strong></p><p>It would be great to have a trace file that is not recorded on a separate device (using a SPAN port or a tap). I am pretty sure that this trace will show, that 192.168.8.26 is sending packets with an IP lengh of 1500 or less. In other words: <strong>You do not have jumbo frames in your LAN</strong></p><p>Still, your trace shows jumbo frames. These are most likely generated in your Debian Linux box. This could be the work of TCP Offloading in your network card (in the Windows world it is called "TCP chimney"), or a result of the software used in your Linux box.</p><p><strong>Artefacts of the TCP reassembly</strong></p><p>The reassembly within your Linux box becomes clear when looking at the IP Identification. Try to apply the IP ID and the IP Length as columens (Display filter <code>ip.id</code> and <code>ip.len</code>). You will notice, that the IP-ID should be incremented by one with each packets. Notice, that the IP-ID is incrementing in a non-linear way. Everytime the IP length is exceeded 1500 bytes the IP ID is increased by more than 1.</p><p>The jumbo frame now exists within the memory of your firewall / router. When forwarding the packet to the external interface (or maybe, when the NAT process is applied) the IP stack notices that the frame exceeds the maximum packet length for the interface and discards the packet. The source (192.168.8.26) is informed with an "ICMP fragmentation needed".</p><p>You don't see the ICMP packet for every single frame, because the kernel throttles the number of ICMP packets.</p><p><strong>Why Windows, and not Linux?</strong></p><p>I could imagine that the problem also exists with Linux clients. Windows and Linux will probably react in different ways to the ICMP fragmentation method. As the sender did nothing wrong the fragmentation needed message is confusing at best. If you show us a trace file with both Windows and Linux boxes transmitting simultaneously we can see the difference.</p><p><strong>How to fix this?</strong></p><p>Please check the configuration of your Linux box. At some level (either network card or network stack) multiple incoming TCP segments are combined into the jumbo frame. Either use the offloading mechanism of your external network card to transmit the large packet or disable the segment reassembly for incoming data.</p><p>Good luck and happy hunting</p><p>PS: Just to still my curiosity: I would be interested to know</p><ul><li>a) how Linux systems look like in the trace</li><li>b) what software is involved in your Linux box (Kernel, version, possible firewall / proxy ...)</li><li>c) what parameter fixes the behaviour</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Dec '14, 12:17</p></div></div><div id="comments-container-38793" class="comments-container"><span id="38800"></span><div id="comment-38800" class="comment"><div id="post-38800-score" class="comment-score"></div><div class="comment-text"><p>Hi Mr. Hunter!! :) First of all, I would like to thank you for your great explanation about this topic. For sure this improved my tiny knowledge.</p><p>Well, making things clear, you were right! Actually, I have the same behaviour on Linux workstations, only on Macs I can do it with no issues. I tried Linux again and got exactly the same slowness. Here is a dump when trying to upload from Linux:</p><p><a href="https://www.cloudshark.org/captures/637ee10f27f2?filter=ip.addr%3D%3D192.168.9.22">Dump Linux</a></p><p>I could send only this small dump once Cloudshark limit the size to 1.5M only. Is there any other place to upload pcap files?</p><p>So, before I read your great post, I found something that got my attention in this <a href="http://www.lartc.org/lartc.html#LARTC.COOKBOOK.MTU-DISCOVERY">link</a>, item 15.7 where it says "<em>Path MTU Discovery doesn't work as well as it should anymore</em>". Then, I tried applying this iptables rule to set the MSS:</p><pre><code>iptables -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --set-mss 128</code></pre><p>So then, for the first time the things started working!! The uploads worked as it should but I still notice some unstable behaviour during the process. The progress bar goes to 5MB and stops, sometimes it continue, sometimes it starts again from zero, then going until the end. I guess this makes sense, since we set a very small segment size. Considering your explanation, I set the MSS to 1400 and until now, it's working fine for both Windows and Linux stations. Below I uploaded a dump (in two parts because of the size) after MSS set:</p><p><a href="https://www.cloudshark.org/captures/2c172e3a1f97?filter=ip.addr%3D%3D192.168.8.26">Dump with TCPMSS set - Part1</a></p><p><a href="https://www.cloudshark.org/captures/2d31c8a698c7?filter=ip.addr%3D%3D192.168.8.26">Dump with TCPMSS set - Part2</a></p><p>Regarding your questions:</p><p><strong>a)</strong> Sent above</p><p><strong>b)</strong> Debian 7.6 / 1 SMP Debian 3.2.60-1+deb7u1 x86_64 GNU/Linux / Iptables v1.4.14 / Proxy transparent with Squid</p><p><strong>c)</strong> The iptables rule I just applied.</p><p>Thanks again and let me know if you would like to check any other information.</p><p>Best,</p><p>Danilo</p></div><div id="comment-38800-info" class="comment-info"><span class="comment-age">(30 Dec '14, 10:28)</span> Mussolini</div></div><span id="38805"></span><div id="comment-38805" class="comment"><div id="post-38805-score" class="comment-score">1</div><div class="comment-text"><p>Hi Danilo,</p><p>your situation will not be solved by changing the MSS. Changing the segment size (or packet size or MTU size) will change the appearance, but it will not fix your problem.</p><p>More likely, you have a configuration issue on your Linux firewall / router. Try the <code>ethtool</code> to disable the TCP offloading feature.</p><p>Now, let's have a look at your trace files:</p><p>The "Dump Linux" shows exactly the same behaviour. Let's look at a few interesting frames:</p><ul><li>In frame 704 we see a packet of 2960 byte length from the server (IP length is 2676)</li><li>Clearly, two separate frames received by the system were concatenated either by hardware (TCP offloading) or by a software function</li><li>This oversized message is most probably split into two frames and transmitted without problems to the workstation.</li><li>Note that the workstation acknowledges the data in frame 706. Note the time difference between frames 704 and 706: This all happens within 1 millisecond. Typical LAN speed, no retransmission, everything is fine and speedy.</li></ul><p>Conclusion: Whatever is happening on your Linux box affects both directions (from inside to outside and vice versa).</p><p>Next a look at frame the Linux upload trace. Starting from frame 934 things go down hill. Try the display filter <code>tcp.port == 39553</code> and set a time reference to frame 934.</p><ul><li>Note that the round trip time calculated from frames 553 to 619 is 158 milliseconds</li><li>In 934 we see a large packet from the client. This is probably the TCP offloading engine that combined two packets from the network into one packet for the router to reduce processing and interrupt load. The large packet triggers the "ICMP fragementation needed" message in 935</li><li>In frames 938 and 939 the same happens for another oversized chunk of data</li><li>The message displayed in frame 934 was not delivered to the server. It is never acknowledged.</li><li>In frame 1085 the server sends some data. The ACK-no from this frame tells the client, that data from frame 938 did not make it.</li><li>In frame 1154 the client finally realizes that the packet was lost, retransmit a single packet and waits for an acknowledgement. As we did not generate the oversized packet an ACK arrives after 191 milliseconds. That is a bit longer than the RTT. The server probably was expecting more data and tried to delay the ACK.</li><li>Based on the timing I would dare saying, that the workstation is undergoing a TCP slow start. This is, why only a single packet was send and more data only follows after this packet was ACK'd.</li><li>Now the client tries to send two packets at once, (this is the TCP slow start at work). As seen in frame 1307 these packets get reassembled and trigger another ICMP message.</li><li>The sender is now assuming that a WAN link is seriously clogged up and wants to give the router a chance to work off the transmission queue. The next retransmission in 1840 follows after 1.4 seconds.</li></ul><p>If you had Voice over IP in that trace file we could probably see the phone call going from the user to the help desk. :-)</p><p>When comparing the situation to the Windows-trace file you see that Microsoft is not much better: Retransmissions are triggered within 500 milliseconds.</p><p>The tracefiles that you provided clearly show, that the problem resides within your Linux router / firewall. The router is sending ICMP messages (and drops frames) when it should not. Both Linux and Windows systems ignore the packets, because they did nothing wrong. As TCP is not aware of the packet drops, the sender has to recovered from the packet loss by using extremly slow TCP mechanisms.</p><p>The same problem is discussed at a <a href="https://blogs.kent.ac.uk/unseenit/2013/10/18/stalled-scp-and-hanging-tcp-connections/">blog</a>. According to the blog, the Linux command <code>ethtool -K eth0 gso off</code> turns off TCP offloading. This would cause your Linux box to process each packet individually.</p><p>Happy hunting</p></div><div id="comment-38805-info" class="comment-info"><span class="comment-age">(30 Dec '14, 13:24)</span> packethunter</div></div><span id="38910"></span><div id="comment-38910" class="comment"><div id="post-38910-score" class="comment-score"></div><div class="comment-text"><p>Hi Packet, how are you ? Hope you had a great new years eve.</p><p>Sorry for the delay, but I'm just came back to work and also my emails! ;)</p><p>Well, reading your last post (and now testing from inside the company, not remote) I notice interesting outputs regarding the Offload. I have eth1 (Internal) and eth2 (external) interfaces, the ethtool output was like this:</p><pre><code>[email protected]:~# ethtool --show-offload eth2
Features for eth2:
rx-checksumming: on
tx-checksumming: off
    tx-checksum-ipv4: off
    tx-checksum-unneeded: off [fixed]
    tx-checksum-ip-generic: off [fixed]
    tx-checksum-ipv6: off [fixed]
    tx-checksum-fcoe-crc: off [fixed]
    tx-checksum-sctp: off [fixed]
scatter-gather: off
    tx-scatter-gather: off
    tx-scatter-gather-fraglist: off [fixed]
tcp-segmentation-offload: off
    tx-tcp-segmentation: off
    tx-tcp-ecn-segmentation: off [fixed]
    tx-tcp6-segmentation: off [fixed]
udp-fragmentation-offload: off [fixed]
generic-segmentation-offload: off [requested on]
generic-receive-offload: on
large-receive-offload: off [fixed]
rx-vlan-offload: on
tx-vlan-offload: on
ntuple-filters: off [fixed]
receive-hashing: off [fixed]
highdma: off [fixed]
rx-vlan-filter: off [fixed]
vlan-challenged: off [fixed]
tx-lockless: off [fixed]
netns-local: off [fixed]
tx-gso-robust: off [fixed]
tx-fcoe-segmentation: off [fixed]
fcoe-mtu: off [fixed]
tx-nocache-copy: off
loopback: off [fixed]

[email protected]:~# ethtool --show-offload eth1
Features for eth1:
rx-checksumming: on
tx-checksumming: on
    tx-checksum-ipv4: off [fixed]
    tx-checksum-unneeded: off [fixed]
    tx-checksum-ip-generic: on
    tx-checksum-ipv6: off [fixed]
    tx-checksum-fcoe-crc: off [fixed]
    tx-checksum-sctp: off [fixed]
scatter-gather: on
    tx-scatter-gather: on
    tx-scatter-gather-fraglist: off [fixed]
tcp-segmentation-offload: on
    tx-tcp-segmentation: on
    tx-tcp-ecn-segmentation: off [fixed]
    tx-tcp6-segmentation: on
udp-fragmentation-offload: off [fixed]
generic-segmentation-offload: off
generic-receive-offload: on
large-receive-offload: off [fixed]
rx-vlan-offload: on
tx-vlan-offload: on
ntuple-filters: off [fixed]
receive-hashing: on
highdma: on [fixed]
rx-vlan-filter: on [fixed]
vlan-challenged: off [fixed]
tx-lockless: off [fixed]
netns-local: off [fixed]
tx-gso-robust: off [fixed]
tx-fcoe-segmentation: off [fixed]
fcoe-mtu: off [fixed]
tx-nocache-copy: on
loopback: off [fixed]</code></pre><p>I don't know why, but eth2 was with RX enabled and TX disabled, while the eth1 was both enabled. I don't know if that was the problem, but to be sure and as you recommended, I disabled offload control on both cards and now the things started working!! Even without the iptables rule I mencioned before, the things seems to be working and I can't see jumbo frames in Wireshark anymore . I will test that better during this day but it really sounds good. Is that a problem to work like this ? This router is an Intel Quad-core CPU machine.</p><p>Well, I don't know how to thank you for the time you spent on this case and for the great explanations, you are like a monster of TCP. ;) Which makes me wonder how to be a TCP specialist like you.</p><p>Best Regards,</p><p>Danilo</p></div><div id="comment-38910-info" class="comment-info"><span class="comment-age">(06 Jan '15, 10:40)</span> Mussolini</div></div></div><div id="comment-tools-38793" class="comment-tools"></div><div class="clear"></div><div id="comment-38793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

