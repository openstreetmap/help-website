+++
type = "question"
title = "Wireshark and Virtual Box - Bridge and multi adaptor capture causes network loop"
description = '''I&#x27;m experimenting with Bridging and Traffic control in Ubuntu and using a virtual box for this. I want to see what happens to the packets in Wireshark and found a behaviour which I&#x27;d like to understand  In virtual box I have two Host Only adapaters with DHCP disabled -  In my Host end of the adapter...'''
date = "2017-01-29T20:06:00Z"
lastmod = "2017-01-31T16:49:00Z"
weight = 59137
keywords = [ "virtualbox", "loop" ]
aliases = [ "/questions/59137" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and Virtual Box - Bridge and multi adaptor capture causes network loop](/questions/59137/wireshark-and-virtual-box-bridge-and-multi-adaptor-capture-causes-network-loop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59137-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm experimenting with Bridging and Traffic control in Ubuntu and using a virtual box for this. I want to see what happens to the packets in Wireshark and found a behaviour which I'd like to understand</p><p>In virtual box I have two Host Only adapaters with DHCP disabled - In my Host end of the adapters one of these (AdaptorA) has an IP address (192.168.11.1) the other (AdaptorB) is not bound to IPV4</p><p>Inside Ubuntu I bridge the two adapters This works fine and I can send a packet to 192.168.11.2 and wireshark monitoring AdapterB - sees the ARP requests. If I fake an arp entry then I see the packet as I'd expect. Fake ARP entry "arp -s 192.168.11.2 00-11-22-33-44-55 -N 192.168.11.1"</p><p>However if I then (in Wireshark) select monitor BOTH AdapterA and AdapterB and then send one packet - Wireshark sees over 845000 packets before I killed it and it crashed - so it looks to me like a loop is formed. This is repeatable I have not seen this bridgeing type behaviou before on real adapters so I don't think this is normal. I don't currently have a host with multiple physical adaptors so I can't check.</p><p>Other (network) software installed on the Host is Windows 7 , AirMagnet, Cisco AnyConnect and the Virtual PC (for the Windows XP VM) so I'm not expecting this to be a regular problem</p><p>Inside Ubuntu both interfaces are "LinkLocal only" and I bridged them using the following commands</p><pre><code>brctl addbr bypass0
brctl addif bypass0 enp0s3
brctl addif bypass0 enp0s8
brctl setfd bypass0 0
brctl sethello bypass0 2
brctl setmaxage bypass0 12
brctl stp bypass0 off
ip link set dev bypass0 up</code></pre><p>I'm sending a Single UDP packet on port 24 (using a program called packet Sender by Dan Nagle)</p><ul><li>If I monitor AdaptorA I see one packet</li><li>If I monitor AdaptorB I see two packets (not sure exactly why)</li><li>If I monitor AdaptorA and AdaptorB I see an unlimited number of packets which I think is wrong</li></ul><p>Changing STP to ON did not change the unlimited number of packets</p><p>I intend to use a Traffic control to simulate a delay (from <a href="https://www.excentis.com/blog/use-linux-traffic-control-impairment-node-test-environment-part-1">https://www.excentis.com/blog/use-linux-traffic-control-impairment-node-test-environment-part-1</a> ) using commands such as</p><pre><code>tc qdisc add dev bypass0 root netem delay 100ms</code></pre><p>So I want to see how long it takes for packets to traverse my Linux box before I swap to real cards so I'd like to work around this</p><p>Thanks for reading and any hints or things to check</p></div><div id="question-tags" class="tags-container tags">virtualbox loop</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '17, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/3a058cc2ff4addb9763d000a44ad873d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjwilson01&#39;s gravatar image" /><p>rjwilson01<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjwilson01 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '17, 20:12</p></div></div><div id="comments-container-59137" class="comments-container"><span id="59150"></span><div id="comment-59150" class="comment"><div id="post-59150-score" class="comment-score"></div><div class="comment-text"><p>Try <em>not</em> setting promiscuous mode while capturing and see if that makes a difference.</p></div><div id="comment-59150-info" class="comment-info"><span class="comment-age">(30 Jan '17, 08:23)</span> Jaap ♦</div></div><span id="59163"></span><div id="comment-59163" class="comment"><div id="post-59163-score" class="comment-score"></div><div class="comment-text"><p>Thanks I've Tried disabling promiscuous mode in the host and it still generates a lot of traffic I tried installing wireshark inside the VM - If I monitor both ports inside the VM I don't get lots of traffic.</p><p>If I monitor both inside the VM and monitor both ports on the host - then the VM Wireshark does see a lot of packets , not as many but I believe that is just lack of processing power. So this is a real effect on the VirtualBox/Wireshark monitoring.</p><p>I also tried two Wiresharks running in the host, each monitoring one network card - this also caused the loop.<br />
</p><p>The loop also occurs for traffic initiated by the VM I tried disabling all the IPV4 (and IPV6) within the VM - this stopped traffic initiated within the VM however it still has a loop.</p><p>I also disabled the two interfaces (leaving the bridge interface enabled), this still bridged traffic (ie traffic came out the second interface) but also still caused the loop when monitoring both interfaces in the host.</p><p>I disabled promiscuous mode in the VM as well</p><p>I think I'll see if using the wireshark inside the VM is enough to confirm how the Traffic control operates.</p></div><div id="comment-59163-info" class="comment-info"><span class="comment-age">(30 Jan '17, 16:14)</span> rjwilson01</div></div><span id="59176"></span><div id="comment-59176" class="comment"><div id="post-59176-score" class="comment-score"></div><div class="comment-text"><p>There's also <a href="https://npcap.org">a new packet sniffer library for Windows</a> in the works, which may make a difference as well.</p></div><div id="comment-59176-info" class="comment-info"><span class="comment-age">(31 Jan '17, 01:52)</span> Jaap ♦</div></div><span id="59199"></span><div id="comment-59199" class="comment"><div id="post-59199-score" class="comment-score"></div><div class="comment-text"><p>Given the behaviour a new PCAP sounds appropriate - thanks for point that out I ;ve tried a few things NPCAP (leaving WinPcap present and in legacy mode ) and I think it probably is a driver problem. It does not loop the network with NPCAP installed in either PWinPcap emulation or not. But it also does not show the second packet. The second packet is still present inside the VM Wireshark capture</p><p>I'm still looking into it as I've got some hardware now and so will send this through a Cisco switch with a SPAN to try and see actual traffic. But I have to move on - I've confirmed that the Traffic control works</p><p>One thing on that shortcut you posted I can't get to <a href="https://npcap.org/">https://npcap.org/</a> I must go to <a href="http://npcap.org/">http://npcap.org/</a> which redirects me to <a href="https://nmap.org/npcap/">https://nmap.org/npcap/</a> I'd guess its a browser setting</p></div><div id="comment-59199-info" class="comment-info"><span class="comment-age">(31 Jan '17, 16:48)</span> rjwilson01</div></div></div><div id="comment-tools-59137" class="comment-tools"></div><div class="clear"></div><div id="comment-59137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59200"></span>

<div id="answer-container-59200" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59200-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>WinPCAP driver problem causes Loops when interacting with VirtualBox drivers</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '17, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/3a058cc2ff4addb9763d000a44ad873d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjwilson01&#39;s gravatar image" /><p>rjwilson01<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjwilson01 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-59200" class="comments-container"></div><div id="comment-tools-59200" class="comment-tools"></div><div class="clear"></div><div id="comment-59200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

