+++
type = "question"
title = "Persistently Capturing VLAN Tags with Intel Pro/1000 CT NIC Card under CentOS 6.3"
description = '''I am in need to capture packets that contain VLAN tags on my Intel Pro/1000 CT NIC Card. When I try to capture packets using the command: tcpdump -ni eth2 vlan I do NOT capture any packets. I then issue the command: ifconfig eth2 mtu 1522 I then try to capture packets using the command: tcpdump -ni ...'''
date = "2012-11-01T12:11:00Z"
lastmod = "2013-05-03T11:11:00Z"
weight = 15476
keywords = [ "capture", "vlan", "intel" ]
aliases = [ "/questions/15476" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Persistently Capturing VLAN Tags with Intel Pro/1000 CT NIC Card under CentOS 6.3](/questions/15476/persistently-capturing-vlan-tags-with-intel-pro1000-ct-nic-card-under-centos-63)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15476-score" class="post-score" title="current number of votes">0</div><span id="post-15476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am in need to capture packets that contain VLAN tags on my Intel Pro/1000 CT NIC Card.</p><p>When I try to capture packets using the command: <strong>tcpdump -ni eth2 vlan</strong></p><p><strong>I do NOT capture any packets.</strong></p><p>I then issue the command: <strong>ifconfig eth2 mtu 1522</strong></p><p>I then try to capture packets using the command: <strong>tcpdump -ni eth2 vlan</strong></p><p><strong>I CAN now capture packets</strong></p><p>I then save my settings in my cfg file: <strong>/etc/sysconfig/network-scripts/ifcfg-eth2</strong><br />
</p><blockquote><p>Please read /usr/share/doc/initscripts-*/<a href="http://sysconfig.txt">sysconfig.txt</a><br />
for the documentation of these parameters.<br />
DEVICE=eth2<br />
BOOTPROTO=none<br />
NETMASK=255.255.255.0<br />
TYPE=Ethernet<br />
IPADDR=10.2.1.1<br />
HWADDR=00:1b:21:a0:17:27<br />
<strong>MTU=1522</strong><br />
</p></blockquote><p>I then <strong>reboot</strong> the computer.</p><p>After the <strong>reboot</strong> I issue the command: <strong>tcpdump -ni eth2 vlan</strong></p><blockquote><p><strong>Now NO packets are captured.</strong></p></blockquote><p>I check the interface settings using: <strong>ifconfig eth2</strong></p><p>The MTU setting is still there:<br />
</p><p><strong>ifconfig eth2</strong></p><blockquote><p>eth2 Link encap:Ethernet HWaddr 00:1B:21:A0:17:27<br />
inet addr:10.2.1.1 Bcast:10.2.1.255 Mask:255.255.255.0<br />
inet6 addr: fe80::21b:21ff:fea0:1727/64 Scope:Link<br />
UP BROADCAST RUNNING MULTICAST <strong>MTU:1522</strong> Metric:1<br />
RX packets:2 errors:0 dropped:0 overruns:0 frame:0<br />
TX packets:26 errors:0 dropped:0 overruns:0 carrier:0<br />
collisions:0 txqueuelen:1000<br />
RX bytes:120 (120.0 b) TX bytes:4181 (4.0 KiB)<br />
Interrupt:17 Memory:f0680000-f06a0000<br />
</p></blockquote><p>I then issue the command: <strong>ifconfig eth2 mtu 1524</strong> and <strong>ifconfig eth2 mtu 1522</strong><br />
(Toggling the MTU setting)</p><p>I then try to capture packets using the command: <strong>tcpdump -ni eth2 vlan</strong></p><blockquote><p><strong>I CAN now capture packets</strong><br />
</p></blockquote><p>Any idea how to make the ability to capture packets permanent between reboots?<br />
</p><p>Thanks in advance for any wisdom and guidance!!<br />
</p><p>-John<br />
</p><h1 id="various-settings">Various settings:</h1><p><strong>ifconfig eth2</strong></p><blockquote><p>eth2 Link encap:Ethernet HWaddr 00:1B:21:A0:17:27<br />
inet addr:10.2.1.1 Bcast:10.2.1.255 Mask:255.255.255.0<br />
inet6 addr: fe80::21b:21ff:fea0:1727/64 Scope:Link<br />
UP BROADCAST RUNNING MULTICAST <strong>MTU:1522</strong> Metric:1<br />
RX packets:2 errors:0 dropped:0 overruns:0 frame:0<br />
TX packets:26 errors:0 dropped:0 overruns:0 carrier:0<br />
collisions:0 txqueuelen:1000<br />
RX bytes:120 (120.0 b) TX bytes:4181 (4.0 KiB)<br />
Interrupt:17 Memory:f0680000-f06a0000<br />
</p></blockquote><p><strong>ethtool -i eth2</strong></p><blockquote><p>driver: e1000e<br />
version: 1.9.5-k<br />
firmware-version: 1.8-0<br />
bus-info: 0000:30:00.0<br />
</p></blockquote><p><strong>modinfo -d -p e1000e</strong></p><blockquote><p>EEE:Enable/disable on parts that support the feature<br />
CrcStripping:Enable CRC Stripping, disable if your BMC needs the CRC<br />
WriteProtectNVM:Write-protect NVM [WARNING: disabling this can lead to corrupted NVM]<br />
KumeranLockLoss:Enable Kumeran lock loss workaround<br />
SmartPowerDownEnable:Enable PHY smart power down<br />
IntMode:Interrupt Mode<br />
InterruptThrottleRate:Interrupt Throttling Rate<br />
RxAbsIntDelay:Receive Absolute Interrupt Delay<br />
RxIntDelay:Receive Interrupt Delay<br />
TxAbsIntDelay:Transmit Absolute Interrupt Delay<br />
TxIntDelay:Transmit Interrupt Delay<br />
copybreak:Maximum size of packet that is copied to a new buffer on receive<br />
</p></blockquote><p><strong>lspci</strong><br />
</p><blockquote><p>20:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection<br />
30:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection<br />
</p></blockquote><p><strong>ethtool eth2</strong></p><blockquote><p>Settings for eth2:<br />
Supported ports: [ TP ]<br />
Supported link modes: 10baseT/Half 10baseT/Full<br />
100baseT/Half 100baseT/Full<br />
1000baseT/Full<br />
Supports auto-negotiation: Yes<br />
Advertised link modes: 10baseT/Half 10baseT/Full<br />
100baseT/Half 100baseT/Full<br />
1000baseT/Full<br />
Advertised pause frame use: No<br />
Advertised auto-negotiation: Yes<br />
Speed: 1000Mb/s<br />
Duplex: Full<br />
Port: Twisted Pair<br />
PHYAD: 1<br />
Transceiver: internal<br />
Auto-negotiation: on<br />
MDI-X: off<br />
Supports Wake-on: pumbg<br />
Wake-on: g<br />
Current message level: 0x00000001 (1)<br />
Link detected: yes<br />
</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-intel" rel="tag" title="see questions tagged &#39;intel&#39;">intel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '12, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/cccf8e497e5c13ae9a4dac3641c2521c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xq1&#39;s gravatar image" /><p><span>xq1</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xq1 has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Nov '12, 13:59</strong> </span></p></div></div><div id="comments-container-15476" class="comments-container"></div><div id="comment-tools-15476" class="comment-tools"></div><div class="clear"></div><div id="comment-15476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15481"></span>

<div id="answer-container-15481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15481-score" class="post-score" title="current number of votes">0</div><span id="post-15481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like a problem with the driver or the hardware itself. Did you try to capture on the other 82574L adapter?</p><p>BTW: You could try to boot the PC from Knoppix and/or BackTrack Live CD and check if you can capture. If it work, it might be a driver problem in CentOS 6.3. If it does not work it might be a problem with the adapter itself.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15481" class="comments-container"><span id="15494"></span><div id="comment-15494" class="comment"><div id="post-15494-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>It will be very difficult to try and use a live CD as the problem is that this is a headless setup.</p><p>Both Intel interfaces behave the same.</p><p>If I use a Broadcom based NIC I have no problem capturing.<br />
</p><p>So this issue is somewhat related to the hardware and options with the driver for the Intel NIC.</p><p>In the past Broadcom support gave me a procedure for updating parameters in the firmware to allow VLAN tagged packets to be captured.</p><p>INTEL is refusing to assist in resolution so I am trying to procure Broadcom based NICs.</p><p>The fact that I can get it to work but it is not persistent over a restart is puzzling and points to a combo driver/hardware issue.</p><p>Words of wisdom are welcome. :-)</p><p>-John</p></div><div id="comment-15494-info" class="comment-info"><span class="comment-age">(02 Nov '12, 05:44)</span> <span class="comment-user userinfo">xq1</span></div></div><span id="15495"></span><div id="comment-15495" class="comment"><div id="post-15495-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment as that's how this site works, please see the FAQ.</p><p>There are occasions when you have to post a comment as an answer, e.g. if your comment is long, but otherwise replies to answers or other comments should be made as comments.</p></div><div id="comment-15495-info" class="comment-info"><span class="comment-age">(02 Nov '12, 05:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-15481" class="comment-tools"></div><div class="clear"></div><div id="comment-15481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20935"></span>

<div id="answer-container-20935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20935-score" class="post-score" title="current number of votes">0</div><span id="post-20935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I did this by adding the following lines to /etc/rc.local because I was running into the same issue configuring it in the network script file on Centos 6.3</p><pre><code>/sbin/ifconfig eth1 0.0.0.0 promisc up mtu 1524
/bin/sleep 2
/sbin/ifconfig eth1 0.0.0.0 promisc up mtu 1522</code></pre><p>The problem with not being able to see tagged traffic was driving me crazy and I was on a wild goose chase looking at my libpcap version until I ran across this article.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '13, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/578c3241120f04d9957777e77fcec46c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spantree33&#39;s gravatar image" /><p><span>spantree33</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spantree33 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 May '13, 06:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></br></p></div></div><div id="comments-container-20935" class="comments-container"></div><div id="comment-tools-20935" class="comment-tools"></div><div class="clear"></div><div id="comment-20935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

