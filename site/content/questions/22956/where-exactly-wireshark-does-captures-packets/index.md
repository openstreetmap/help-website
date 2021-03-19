+++
type = "question"
title = "Where exactly wireshark does captures packets?"
description = '''Hi, Could you please explain where exactly does wireshark captures incoming packets? Is it above device driver? Or, in between device driver and network interface? thanks,'''
date = "2013-07-14T09:19:00Z"
lastmod = "2013-07-14T09:35:00Z"
weight = 22956
keywords = [ "wireshark" ]
aliases = [ "/questions/22956" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Where exactly wireshark does captures packets?](/questions/22956/where-exactly-wireshark-does-captures-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22956-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Could you please explain where exactly does wireshark captures <em>incoming</em> packets? Is it above device driver? Or, in between device driver and network interface?</p><p>thanks,</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/7d7de3c3ec20545d2b8b7297cafd0efa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adityaholla&#39;s gravatar image" /><p>adityaholla<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adityaholla has no accepted answers">0%</span></p></div></div><div id="comments-container-22956" class="comments-container"></div><div id="comment-tools-22956" class="comment-tools"></div><div class="clear"></div><div id="comment-22956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22957"></span>

<div id="answer-container-22957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22957-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Basically the capturing framework is placed between the NIC driver and higher layer protocols in the kernel (e.g. TCP/IP).</p><p>For a general overview of the libpcap architecture, please read this:</p><blockquote><p><a href="http://sharkfest.wireshark.org/sharkfest.11/presentations/McCanne-Sharkfest%2711_Keynote_Address.pdf">http://sharkfest.wireshark.org/sharkfest.11/presentations/McCanne-Sharkfest%2711_Keynote_Address.pdf</a></p></blockquote><p>For WinPcap (the capturing framework of Wireshark on Windows), please see <a href="https://www.winpcap.org/misc/faq.htm#Q-26">WinPcap FAQ Q-26</a> and the architecture overview paper of WinPcap.</p><blockquote><p><a href="http://www.winpcap.org/docs/iscc01-wpcap.pdf">http://www.winpcap.org/docs/iscc01-wpcap.pdf</a><br />
<a href="https://www.winpcap.org/docs/th_degio.zip">https://www.winpcap.org/docs/th_degio.zip</a> (please skip the first few italian pages)</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '13, 10:11</p></div></div><div id="comments-container-22957" class="comments-container"><span id="22958"></span><div id="comment-22958" class="comment"><div id="post-22958-score" class="comment-score"></div><div class="comment-text"><p>Thanks much Kurt.</p><p>Is it true for outgoing packets also? Because, wireshark even gives ethernet header(this header is added by device driver), right?</p><p>I'll go thru given pdf.</p><p>Thanks much!</p></div><div id="comment-22958-info" class="comment-info"><span class="comment-age">(14 Jul '13, 09:54)</span> adityaholla</div></div><span id="22959"></span><div id="comment-22959" class="comment"><div id="post-22959-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Is it true for outgoing packets also? Because, wireshark even gives ethernet header(this header is added by device driver), right?</p></blockquote><p>For outgoing packets, the driver, in an OS-dependent fashion, arranges that the packet be handed to the capture mechanism at about the same time that it's handed to the hardware to transmit.</p></div><div id="comment-22959-info" class="comment-info"><span class="comment-age">(14 Jul '13, 10:47)</span> Guy Harris ♦♦</div></div><span id="22960"></span><div id="comment-22960" class="comment"><div id="post-22960-score" class="comment-score">1</div><div class="comment-text"><p>Usually in an operating system the NIC driver is only responsible for direct hardware access (receiving and transmitting of network frames, generating interrupts etc.). If the OS wants to send a frame, it (actually a higher level driver) will create the ethernet frame and pass that to the hardware NIC driver in order to send it. Due to this architecture it is possible to intercept outgoing frames before they are sent, as the capture driver is placed 'somewhere' between the NIC driver (hardware) and the upper layer drivers (ethernet, ip, tcp, etc.).</p></div><div id="comment-22960-info" class="comment-info"><span class="comment-age">(14 Jul '13, 10:57)</span> Kurt Knochner ♦</div></div><span id="22961"></span><div id="comment-22961" class="comment"><div id="post-22961-score" class="comment-score"></div><div class="comment-text"><p>Systems with BPF (*BSD, OS X, possibly AIX and Solaris 11 but I don't have access to the source): the capture mechanism (BPF) is called by the driver.</p><p>Linux: drivers end up calling OS kernel routines such as <code>dev_hard_start_xmit()</code> for transmitting packets and <code>netif_receive_skb()</code> for received packets, passing them the entire packet, complete with a link-layer header (except when it doesn't...), and those routines hand packets to all PF_PACKET sockets.</p><p>Other UN*Xes: I don't have access to the source, and so can't check.</p><p>Windows: the WinPcap capture mechanism's driver uses the Windows NDIS mechanism, which supplies received packets to a "protocol" (which is what the driver registers itself as) and can also supply transmitted packets if requested to do so (WinPcap requests it to do so). For received packets, the driver hands packets to NDIS to then supply to protocols; I'm not sure where transmitted packets are handled.</p></div><div id="comment-22961-info" class="comment-info"><span class="comment-age">(14 Jul '13, 11:35)</span> Guy Harris ♦♦</div></div><span id="28375"></span><div id="comment-28375" class="comment"><div id="post-28375-score" class="comment-score"></div><div class="comment-text"><p>OK, Guy, so would you suggest to me scenarios under which dev_hard_start_xmit() sends a packet to a PF_PACKET socket (because, say, dumpcap is running) ... but does <em>not</em> send the packet to the hardware?</p><p>I'm facing a case where I can see the DNS lookup on the wire, the ARP exchange on the wire (the receiver is subnet-local) ... but not the TCP SYN. Whereas, the pcap gathered from the host itself sees the DNS exchange, the ARP exchange, <em>and</em> the TCP SYN</p><p>client ------- switch -------- {network} ------- server</p><p>dumpcap running on the client and a sniffer plugged into a mirror port on the switch</p><p>Linux 3.8.0-34-generic #49 precise (Ubuntu 12.04.03 LTS)</p><p>Does IPTables twink with dev_hard_start_xmit's behavior? [Not enabled in my case, but I'm wanting to understand the entire space, not just solve my particular issue.]</p><p>--sk</p></div><div id="comment-28375-info" class="comment-info"><span class="comment-age">(24 Dec '13, 16:18)</span> skendric</div></div><span id="28391"></span><div id="comment-28391" class="comment not_top_scorer"><div id="post-28391-score" class="comment-score"></div><div class="comment-text"><blockquote><p>would you suggest to me scenarios under which dev_hard_start_xmit() sends a packet to a PF_PACKET socket (because, say, dumpcap is running) ... but does not send the packet to the hardware?</p></blockquote><p>good question.</p><blockquote><p>Does IPTables twink with dev_hard_start_xmit's behavior? [</p></blockquote><p>I did a quick test. If you drop frames in the OUTPUT chain, Wireshark will <strong>not</strong> see them, so iptables handles the packet before the kernel gets a chance to send a copy to dumpcap.</p><p>So, here are some possible explanations that might cause your TCP traffic to appear in Wireshark on the client, but not on the wire. Some of these ideas might sound weird, but that's what I have seen in the wild several times ;-) People configure something and then forget about the fact and then wonder why certain things don't work :-)</p><ul><li>You have several interfaces and the packet takes a different route than you believe (host route, etc.) - think also about policy based routing!</li><li>another chain in iptables modifies the packet. Think about NAT and the like. I did not test it, but I think that could well cause the described behavior, from what I remember about troubleshooting on iptables firewalls</li><li>there is a transparent (TCP) proxy running on the client that 'takes care' of the connection requests. This is usually the case for http(s) and ftp, where that behavior is desirable to scan the traffic.</li><li>there is some kind of tunnel (VPN like IPSEC or OpenVPN, IPinIP, etc.) on the client and the TCP packets are routed into that tunnel</li><li>Did you compare the MAC address of the ARP reply with the one in the TCP SYN? Are they identical?</li></ul><p>There might be other reasons, but without a deeper insight in your environment it's hard to figure out what's going on.</p><p>Regards<br />
Kurt</p></div><div id="comment-28391-info" class="comment-info"><span class="comment-age">(25 Dec '13, 15:16)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22957" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

