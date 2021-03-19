+++
type = "question"
title = "overlapping packets"
description = '''I contacted you before 5 weeks asking for help about overlapping outgoing packets in time in wireshark program. And you told me that the problem is in timestamping of outgoing packets. So the packets were timestamped on host and because of that there was delay of actual sending of packets and they w...'''
date = "2013-07-22T10:48:00Z"
lastmod = "2013-07-23T10:14:00Z"
weight = 23244
keywords = [ "overlapping" ]
aliases = [ "/questions/23244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [overlapping packets](/questions/23244/overlapping-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I contacted you before 5 weeks asking for help about overlapping outgoing packets in time in wireshark program. And you told me that the problem is in timestamping of outgoing packets. So the packets were timestamped on host and because of that there was delay of actual sending of packets and they were overlapped.</p><p>You told me to make outgoing packets be timestamped on the card so they would be more precisely measured. Then I bought Intel i210-t1 network card (kernel 3.3.4-5.fc17.i686.PAE Fedora 17) and compiled igb driver with PTP (Precision Time Protocol) option and with tcpdump command and -j adapter option captured traffic on that network card.</p><p>I hoped that now outgoing won't be overlapped in time but they still are overlapped. So I am surprised how is it possible that when they are timestamped on the card there would be overlapping of outgoing packets.</p><p>When igb driver is not compiled with PTP option tcpdump gives warning that timestamping on the card is not supported but when I compiled with that option everything has gone well, not any warning was printed when I started tcpdump with -j adapter option.</p><p>Do you know what can be the problem so the outgoing packets are still overlapped?</p><p>Thank you in advance, Milutin Aksic.</p></div><div id="question-tags" class="tags-container tags">overlapping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/78a6e59556f3af952df58b4ffd32cb3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="micacim&#39;s gravatar image" /><p>micacim<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="micacim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '13, 11:01</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-23244" class="comments-container"><span id="23254"></span><div id="comment-23254" class="comment"><div id="post-23254-score" class="comment-score"></div><div class="comment-text"><p>What is the output of the following command?</p><blockquote><p>tcpdump -ni eth0 -J</p></blockquote><p>What was the parameter you chose for <code>tcpdump -j</code>?</p><p>can you please post a sample capture file somewhere?</p></div><div id="comment-23254-info" class="comment-info"><span class="comment-age">(22 Jul '13, 14:32)</span> Kurt Knochner ♦</div></div><span id="23286"></span><div id="comment-23286" class="comment"><div id="post-23286-score" class="comment-score"></div><div class="comment-text"><p>Hello, The output of the command tcpdump -ni eth0 -J is: <code> Time stamp types for eth0 (use option -j to set):   host (Host)   adapter (Adapter)   adapter_unsynced (Adapter, not synced with system time)</code> The parameter for tcpdump -j command was 'adapter' and link to the capture file is: <a href="https://www.dropbox.com/s/i2qyr99v690u47h/ts_src.pcap">https://www.dropbox.com/s/i2qyr99v690u47h/ts_src.pcap</a> For example in this file for packet 12. with sending time 0.299593 and length 1514 bytes on the link of 100Mb/s duration is about 115 microseconds but the next packet 13. is sent only 9 microseconds after the beginning of 12.packet. So they are overlapped. How is it possible?</p></div><div id="comment-23286-info" class="comment-info"><span class="comment-age">(23 Jul '13, 07:29)</span> micacim</div></div></div><div id="comment-tools-23244" class="comment-tools"></div><div class="clear"></div><div id="comment-23244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23300"></span>

<div id="answer-container-23300" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23300-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So they are overlapped. How is it possible?</p></blockquote><p>Maybe this is due to (TCP) offloading in the driver. Please try to disable that with ethtool (see man page - Option -k / -K).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23300" class="comments-container"><span id="23317"></span><div id="comment-23317" class="comment"><div id="post-23317-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the last answer this tcp offloading helped me to reduce the overlapping but there are still some overlapping for certain packets if you can see. This is the link to new capture file: <a href="https://www.dropbox.com/s/kl0i6s4s77w2wfw/ts3_src.pcap">https://www.dropbox.com/s/kl0i6s4s77w2wfw/ts3_src.pcap</a> For example for packets no. 564, 747, 920, 954, 999, there are overlappings. Do you know what is the reason for this? Regards, Milutin.</p></div><div id="comment-23317-info" class="comment-info"><span class="comment-age">(24 Jul '13, 01:11)</span> micacim</div></div><span id="23320"></span><div id="comment-23320" class="comment"><div id="post-23320-score" class="comment-score"></div><div class="comment-text"><p>I'd not expect to see correct timestamps as long as you have NOT successfully turned off TCP offloading. As you can see in your provided trace those +1518bytes frames are all "virtual" and contain more than one physical packet - so their timestamps can't almost be correct</p></div><div id="comment-23320-info" class="comment-info"><span class="comment-age">(24 Jul '13, 02:16)</span> Landi</div></div><span id="23322"></span><div id="comment-23322" class="comment"><div id="post-23322-score" class="comment-score"></div><div class="comment-text"><blockquote><p>this tcp offloading helped me to reduce the overlapping</p></blockquote><p>wait a moment. Did you <strong>en</strong>able or <strong>dis</strong>able TCP offloading? I asked you to <strong>disable</strong> it, as well as any other form of offloading ;-)</p><p>See the man page of ethtool.</p><pre><code>-K --features --offload
    Changes the offload parameters and other features of the specified network device. The following feature names are built-in and others may be defined by the kernel. 
rx on|off
    Specifies whether RX checksumming should be enabled. 
tx on|off
    Specifies whether TX checksumming should be enabled. 
sg on|off
    Specifies whether scatter-gather should be enabled. 
tso on|off
    Specifies whether TCP segmentation offload should be enabled. 
ufo on|off
    Specifies whether UDP fragmentation offload should be enabled 
gso on|off
    Specifies whether generic segmentation offload should be enabled 
gro on|off
    Specifies whether generic receive offload should be enabled 
lro on|off
    Specifies whether large receive offload should be enabled 
rxvlan on|off
    Specifies whether RX VLAN acceleration should be enabled 
txvlan on|off
    Specifies whether TX VLAN acceleration should be enabled 
ntuple on|off
    Specifies whether Rx ntuple filters and actions should be enabled 
rxhash on|off
    Specifies whether receive hashing offload should be enabled </code></pre><p>Option -k will tell you if there is any offloading enabled on your system. Could you please post the output of</p><blockquote><p>ethtool -k eth0</p></blockquote><p>If eth0 is your interface...</p></div><div id="comment-23322-info" class="comment-info"><span class="comment-age">(24 Jul '13, 03:50)</span> Kurt Knochner ♦</div></div><span id="23360"></span><div id="comment-23360" class="comment"><div id="post-23360-score" class="comment-score"></div><div class="comment-text"><p>This is the output of ethtool -k eth0 after I disabled all offloads:</p><pre><code>Features for eth0:
rx-checksumming: on
tx-checksumming: on
    tx-checksum-ipv4: on
    tx-checksum-ip-generic: off [fixed]
    tx-checksum-ipv6: on
    tx-checksum-fcoe-crc: off [fixed]
    tx-checksum-sctp: on [fixed]
scatter-gather: on
    tx-scatter-gather: on
    tx-scatter-gather-fraglist: off [fixed]
tcp-segmentation-offload: off
    tx-tcp-segmentation: off
    tx-tcp-ecn-segmentation: off [fixed]
    tx-tcp6-segmentation: off
udp-fragmentation-offload: off [fixed]
generic-segmentation-offload: off
generic-receive-offload: off
large-receive-offload: off
rx-vlan-offload: off
tx-vlan-offload: off [requested on]
ntuple-filters: off [fixed]
receive-hashing: off
highdma: on [fixed]
rx-vlan-filter: on [fixed]
vlan-challenged: off [fixed]
tx-lockless: off [fixed]
netns-local: off [fixed]
tx-gso-robust: off [fixed]
tx-fcoe-segmentation: off [fixed]
fcoe-mtu: off [fixed]
tx-nocache-copy: on
loopback: off [fixed]</code></pre><p>and the capture file is at: <a href="https://www.dropbox.com/s/qdgr65carh0r5sz/ts_sto.pcap">https://www.dropbox.com/s/qdgr65carh0r5sz/ts_sto.pcap</a> Regards, Milutin.</p></div><div id="comment-23360-info" class="comment-info"><span class="comment-age">(25 Jul '13, 08:37)</span> micacim</div></div><span id="23363"></span><div id="comment-23363" class="comment"><div id="post-23363-score" class="comment-score"></div><div class="comment-text"><p>please disable checksumming and scatter-gather as well and then re-try.</p></div><div id="comment-23363-info" class="comment-info"><span class="comment-age">(25 Jul '13, 10:56)</span> Kurt Knochner ♦</div></div><span id="23375"></span><div id="comment-23375" class="comment not_top_scorer"><div id="post-23375-score" class="comment-score"></div><div class="comment-text"><p>After I disable checksumming and scatter-gather output of ethtool -k is:</p><pre><code>rx-checksumming: off
tx-checksumming: on
    tx-checksum-ipv4: off
    tx-checksum-ip-generic: off [fixed]
    tx-checksum-ipv6: off
    tx-checksum-fcoe-crc: off [fixed]
    tx-checksum-sctp: on [fixed]
scatter-gather: off
    tx-scatter-gather: off [requested on]
    tx-scatter-gather-fraglist: off [fixed]
tcp-segmentation-offload: off
    tx-tcp-segmentation: off [requested on]
    tx-tcp-ecn-segmentation: off [fixed]
    tx-tcp6-segmentation: off [requested on]
udp-fragmentation-offload: off [fixed]
generic-segmentation-offload: off [requested on]
generic-receive-offload: off
large-receive-offload: off
rx-vlan-offload: off
tx-vlan-offload: off [requested on]
ntuple-filters: off [fixed]
receive-hashing: off
highdma: on [fixed]
rx-vlan-filter: on [fixed]
vlan-challenged: off [fixed]
tx-lockless: off [fixed]
netns-local: off [fixed]
tx-gso-robust: off [fixed]
tx-fcoe-segmentation: off [fixed]
fcoe-mtu: off [fixed]
tx-nocache-copy: on
loopback: off [fixed]</code></pre><p>and the link to capture file is: <a href="https://www.dropbox.com/s/qdgr65carh0r5sz/ts_sto.pcap">https://www.dropbox.com/s/qdgr65carh0r5sz/ts_sto.pcap</a></p><p>There are still overlappings.</p></div><div id="comment-23375-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:35)</span> micacim</div></div><span id="23376"></span><div id="comment-23376" class="comment not_top_scorer"><div id="post-23376-score" class="comment-score"></div><div class="comment-text"><p>What are the frames, you think there is overlapping?</p></div><div id="comment-23376-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:39)</span> Kurt Knochner ♦</div></div><span id="23378"></span><div id="comment-23378" class="comment not_top_scorer"><div id="post-23378-score" class="comment-score"></div><div class="comment-text"><p>I sent you capture file and there you can see that there are still overlappings.</p></div><div id="comment-23378-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:47)</span> micacim</div></div><span id="23379"></span><div id="comment-23379" class="comment not_top_scorer"><div id="post-23379-score" class="comment-score"></div><div class="comment-text"><p>please tell me the frames.</p></div><div id="comment-23379-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:48)</span> Kurt Knochner ♦</div></div><span id="23380"></span><div id="comment-23380" class="comment not_top_scorer"><div id="post-23380-score" class="comment-score"></div><div class="comment-text"><p>What do you mean tell me the frames?</p></div><div id="comment-23380-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:51)</span> micacim</div></div><span id="23381"></span><div id="comment-23381" class="comment not_top_scorer"><div id="post-23381-score" class="comment-score"></div><div class="comment-text"><p>I sent you capture file. You can see the frames there.</p></div><div id="comment-23381-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:55)</span> micacim</div></div><span id="23382"></span><div id="comment-23382" class="comment not_top_scorer"><div id="post-23382-score" class="comment-score"></div><div class="comment-text"><p>@micacim</p><p>Your multiple "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-23382-info" class="comment-info"><span class="comment-age">(26 Jul '13, 01:58)</span> grahamb ♦</div></div><span id="23383"></span><div id="comment-23383" class="comment not_top_scorer"><div id="post-23383-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What do you mean tell me the frames?</p></blockquote><p>tell me the frame number, where you think there is overlapping. Just to ensure we are talking about the same thing!</p></div><div id="comment-23383-info" class="comment-info"><span class="comment-age">(26 Jul '13, 02:59)</span> Kurt Knochner ♦</div></div><span id="23384"></span><div id="comment-23384" class="comment not_top_scorer"><div id="post-23384-score" class="comment-score"></div><div class="comment-text"><p>BTW: As I don't know how time stamping is implemented internally on the card, I suspect that the packet is not time stamped when it is really transmitted, but when the NIC hardware receives the packet from the system, before it is placed in an internal send buffer. That would explain why you see time stamp deltas that are smaller than the transmit time of a frame. The only way to figure this out is probably by asking Intel.</p></div><div id="comment-23384-info" class="comment-info"><span class="comment-age">(26 Jul '13, 03:08)</span> Kurt Knochner ♦</div></div><span id="23388"></span><div id="comment-23388" class="comment not_top_scorer"><div id="post-23388-score" class="comment-score"></div><div class="comment-text"><p>Can you send me the link of the web page where I should ask Intel about my problem. I have put it on Intel Community forum but nobody answered. Thank you in advance, Milutin.</p></div><div id="comment-23388-info" class="comment-info"><span class="comment-age">(26 Jul '13, 09:20)</span> micacim</div></div><span id="23397"></span><div id="comment-23397" class="comment not_top_scorer"><div id="post-23397-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can you send me the link of the web page where I should ask Intel about my problem.</p></blockquote><p>I don't know the Intel Support Organization. As you have bought the NIC, I suggest to read the accompanying documents. I'm sure there is a hint how to contact Intel Support. Otherwise, I suggest to search google for: Intel support.</p></div><div id="comment-23397-info" class="comment-info"><span class="comment-age">(27 Jul '13, 00:09)</span> Kurt Knochner ♦</div></div><span id="23477"></span><div id="comment-23477" class="comment not_top_scorer"><div id="post-23477-score" class="comment-score"></div><div class="comment-text"><p>Hello, I need to tell you something. I have captured the traffic with tcpdump -j adapter and tcpdump -j host, with timestamping enabled and disabled, and in both cases delays of packets are the same so I think that timestamping was not done at all although there was no any warrning saying that this type of timestamping was not supported. How is it possible that there was no any timestamping on the card?</p></div><div id="comment-23477-info" class="comment-info"><span class="comment-age">(31 Jul '13, 06:15)</span> micacim</div></div><span id="23652"></span><div id="comment-23652" class="comment not_top_scorer"><div id="post-23652-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How is it possible that there was no any timestamping on the card?</p></blockquote><p>Maybe a bug in the linux/libpcap/tcpdump code or a bug in the NIC firmware?</p></div><div id="comment-23652-info" class="comment-info"><span class="comment-age">(08 Aug '13, 08:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23300" class="comment-tools"><span class="comments-showing"> showing 5 of 18 </span> <a href="#" class="show-all-comments-link">show 13 more comments</a></div><div class="clear"></div><div id="comment-23300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

