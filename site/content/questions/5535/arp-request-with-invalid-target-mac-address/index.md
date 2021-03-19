+++
type = "question"
title = "ARP request with invalid target MAC address"
description = '''I have a network capture that has excessive ARP traffic in it. It averages 150 to 250 ARP requests per second. The requests are cycling through all of the addresses on the subnet (255.255.254.0) in a random order. The Ethernet II data shows the destination as a broadcast but the ARP details show the...'''
date = "2011-08-05T11:47:00Z"
lastmod = "2011-08-05T12:05:00Z"
weight = 5535
keywords = [ "arp" ]
aliases = [ "/questions/5535" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ARP request with invalid target MAC address](/questions/5535/arp-request-with-invalid-target-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5535-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a network capture that has excessive ARP traffic in it. It averages 150 to 250 ARP requests per second. The requests are cycling through all of the addresses on the subnet (255.255.254.0) in a random order.</p><p>The Ethernet II data shows the destination as a broadcast but the ARP details show the target as a specific invalid MAC address instead of all zeros. All of the packets are to one of about 10 different invalid target MAC addresses regardless of the target IP address.</p><p>I would appreciate any information or reference material. I could only find information related to ARP responses with an invalid MAC.<br />
</p><p>Is this normal operation for some hardware?<br />
Is this a hardware malfunction?<br />
Is this a deliberate attack?<br />
</p><p>No. Time Source Destination Protocol Length Info<br />
12 0.003992 Procurve f4:4f:00 Broadcast ARP 60 Who has 192.168.248.12<br />
Frame 12: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)<br />
Ethernet II, Src: Procurve_f4:4f:00 (00:1f:fe:f4:4f:00), Dst: Broadcast (ff:ff:ff:ff:ff:ff)<br />
Address Resolution Protocol (request)<br />
Hardware type: Ethernet (1)<br />
Protocol type: IP (0x0800)<br />
Hardware size: 6<br />
Protocol size: 4<br />
Opcode: request (1)<br />
[Is gratuitous: False]<br />
Sender MAC address: Procurve_f4:4f:00 (00:1f:fe:f4:4f:00)<br />
Sender IP address: 192.168.248.1 (192.168.248.1)<br />
Target MAC address: 06:0b:2b:06:01:02 (06:0b:2b:06:01:02)<br />
Target IP address: 192.168.248.127 (192.168.248.127)</p></div><div id="question-tags" class="tags-container tags">arp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '11, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/3401c4a75bf3edde84461eaf7010fb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vicbug643839032&#39;s gravatar image" /><p>Vicbug643839032<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vicbug643839032 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-5535" class="comments-container"></div><div id="comment-tools-5535" class="comment-tools"></div><div class="clear"></div><div id="comment-5535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5536"></span>

<div id="answer-container-5536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5536-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Excessive ARP requests on the magnitude that you observe are usually a sign of bad news.</p><p>Within certain intervals an ARP sweep may be caused a few regular tasks, for example:</p><ul><li>Network management / inventory system</li><li>DHCP Server scanning for available aderesses</li></ul><p>This is usually a "one and done" pattern.</p><p>The target MAC address for an ARP request is set to zero for many IP implementations. However, certain systems don't zero the transmit buffers and send out some slag. Other systems put there the address that is already in their buffer when they confirm the validity of the ARP cache.</p><p>I am somewhat riddled by the Procurve source address:</p><ul><li>If this is a layer 2 switch the ARP sweep could be caused by a funky configuration (like SNMP trap destination) or a firmware bug.</li><li>If this is a layer 3 switch you have to work your way outward to see the root cause for the ARP request.</li></ul><p>What happens after the switch receives an ARP response? Do you see any packets send to the target system?</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '11, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span> </br></br></p></div></div><div id="comments-container-5536" class="comments-container"></div><div id="comment-tools-5536" class="comment-tools"></div><div class="clear"></div><div id="comment-5536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

