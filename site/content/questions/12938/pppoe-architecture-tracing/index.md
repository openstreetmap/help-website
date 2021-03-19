+++
type = "question"
title = "pppoe architecture tracing"
description = '''I have a dsl modem connected directly to my PC. I want to trace few details of the packets passing through my PC with the help of Wireshark.  Using Capture--&amp;gt;Interfaces I can see the only card with the IP = 10.0.0.1(probably because its a pppoe connection). Can someone direct me where exactly thi...'''
date = "2012-07-23T22:37:00Z"
lastmod = "2012-07-24T01:07:00Z"
weight = 12938
keywords = [ "protocol", "pppoe", "stack" ]
aliases = [ "/questions/12938" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pppoe architecture tracing](/questions/12938/pppoe-architecture-tracing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12938-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a dsl modem connected directly to my PC. I want to trace few details of the packets passing through my PC with the help of Wireshark. Using Capture--&gt;Interfaces I can see the only card with the IP = 10.0.0.1(probably because its a pppoe connection). Can someone direct me where exactly this address should be found in the packet(I guise somewher in the lower levels of the protocol stack)?</p><p>Thanks in advance</p><p>I. Lesher</p></div><div id="question-tags" class="tags-container tags">protocol pppoe stack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '12, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/c46b9d0cf13adb17325f5d9519406546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="triplebit&#39;s gravatar image" /><p>triplebit<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="triplebit has no accepted answers">0%</span></p></div></div><div id="comments-container-12938" class="comments-container"></div><div id="comment-tools-12938" class="comment-tools"></div><div class="clear"></div><div id="comment-12938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12941"></span>

<div id="answer-container-12941" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12941-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If it's really PPPoE you should see this packet structure:</p><blockquote><p><code>Frame -&gt; Ethernet -&gt; PPP-over-Ethernet -&gt; Point-to-Point Protocol -&gt; IP -&gt; TCP/UDP/ICMP/etc.</code></p></blockquote><p>The address you mentioned would be in the IP layer in the field "Source:".</p><p>As you usually get a internet routeable address from your provider with PPPoE (not sure about all regions of the world), this could also be a PPPoA connection, due to your IP address (10.0.0.1). The default IP address of a lot PPPoA modems is <strong>10.0.0.138</strong> and the Modem hands out IP addresses in that IP range (DHCP).</p><blockquote><p><code>http://en.wikipedia.org/wiki/Point-to-Point_Protocol_over_ATM</code></p></blockquote><p>PPPoA would look totally different in Wireshark. Look for the IP layer directly and then for the Source field.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '12, 01:31</p></div></div><div id="comments-container-12941" class="comments-container"><span id="12950"></span><div id="comment-12950" class="comment"><div id="post-12950-score" class="comment-score"></div><div class="comment-text"><p>Thnaks Kurt I followed carefully your answer and saw that the structure is exactly how you wrote, i.e Frame -&gt; Ethernet -&gt; PPP-over-Ethernet -&gt; Point-to-Point Protocol -&gt; IP -&gt; TCP/UDP/ICMP/etc. but the address "10.0.0.1" is not in the IP protocol. Instead the IP layer contains the routable addresses of the source and the destination.here is a paste from the Wireshark of an ip layer of a single packet: "Internet Protocol, Src: 85.250.119.39 (85.250.119.39), Dst: 212.235.98.161 (212.235.98.161)" Can you further advise please? Regards I. Lesher</p></div><div id="comment-12950-info" class="comment-info"><span class="comment-age">(24 Jul '12, 04:03)</span> triplebit</div></div><span id="12951"></span><div id="comment-12951" class="comment"><div id="post-12951-score" class="comment-score"></div><div class="comment-text"><blockquote><p>85.250.119.39</p></blockquote><p>O.K. so you do get a "internet routeable" address from your provider, as expected from PPPoE.</p><p>We just need to figure out, why Wireshark shows 10.0.0.1 in the interface list.</p><p>What is the output of the following commands:</p><blockquote><p><code>ipconfig /all</code><br />
<code>dumpcap -D -M</code><br />
</p></blockquote><p>dumpcap is in the Wireshark install directory.</p></div><div id="comment-12951-info" class="comment-info"><span class="comment-age">(24 Jul '12, 04:29)</span> Kurt Knochner ♦</div></div><span id="13011"></span><div id="comment-13011" class="comment"><div id="post-13011-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt Here is the respond for dumpcap -D -M</p><pre><code> 1. \Device\NPF_{7A460928-A487-4219-BEC1-32E09C8B2CEA}  Atheros AR8121/AR8113/AR8114 PCI-E Ethernet Controller(NDIS6.20)    10.0.0.1    network</code></pre><p>Here is the respond for ipconfig /all Actually I cut the answer since it continues with a list of Tunnel adapters which I beleive don't contribute here. Regards I. Lesher</p><pre><code>Windows IP Configuration

   Host Name . . . . . . . . . . . . : kobi-PC
   Primary Dns Suffix  . . . . . . . : 
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

PPP adapter ‡‰…˜ ”‘ ˜‡:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : ‡‰…˜ ”‘ ˜‡
   Physical Address. . . . . . . . . : 
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 85.250.119.39(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.255
   Default Gateway . . . . . . . . . : 0.0.0.0
   DNS Servers . . . . . . . . . . . : 194.90.1.5
                                       212.143.212.143
   NetBIOS over Tcpip. . . . . . . . : Disabled

Ethernet adapter Local Area Connection:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Atheros AR8121/AR8113/AR8114 PCI-E Ethernet Controller(NDIS6.20)
   Physical Address. . . . . . . . . : E0-CB-4E-D3-5C-F1
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::550c:2c41:4fe3:ec1c%11(Preferred) 
   IPv4 Address. . . . . . . . . . . : 10.0.0.1(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : ‰…™‰™‰ 20 ‰…‰ 2012 18:47:09
   Lease Expires . . . . . . . . . . : ‰…‡‰™‰ 26 ‰…‰ 2012 11:47:19
   Default Gateway . . . . . . . . . : 10.0.0.138
   DHCP Server . . . . . . . . . . . : 10.0.0.138
   DHCPv6 IAID . . . . . . . . . . . : 249613134
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-16-D4-C3-6A-E0-CB-4E-D3-5C-F1
   DNS Servers . . . . . . . . . . . : 10.0.0.138
                                       10.0.0.138
   NetBIOS over Tcpip. . . . . . . . : Enabled

Tunnel adapter Local Area Connection* 23:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Microsoft 6to4 Adapter #16
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : 2002:55fa:7727::55fa:7727(Preferred) 
   Default Gateway . . . . . . . . . : 2002:c058:6301::c058:6301
   DNS Servers . . . . . . . . . . . : 194.90.1.5
                                       212.143.212.143
   NetBIOS over Tcpip. . . . . . . . : Disabled</code></pre></div><div id="comment-13011-info" class="comment-info"><span class="comment-age">(26 Jul '12, 01:21)</span> triplebit</div></div><span id="13176"></span><div id="comment-13176" class="comment"><div id="post-13176-score" class="comment-score"></div><div class="comment-text"><p>The interface with your "external" IP address is a ppp adapter. You cannot sniff on those adapters on systems &gt;= Win XP.</p><blockquote><p>Can I use WinPcap on a PPP connection?<br />
<code>http://www.winpcap.org/misc/faq.htm#Q-5</code><br />
</p></blockquote><p>I guess that's the reason why WinPcap does not show the ppp interface.</p></div><div id="comment-13176-info" class="comment-info"><span class="comment-age">(31 Jul '12, 01:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12941" class="comment-tools"></div><div class="clear"></div><div id="comment-12941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

