+++
type = "question"
title = "Ethernet packet &amp; ARP"
description = '''From viewing a random capture taken on a Windows host in my network, is it normal to see two different structured ARP related packets:  An ethernet frame with a broadcast destination address of FF:FF containing an ARP request with a target hardware address of 00:00 An ethernet frame where the hardwa...'''
date = "2015-08-27T06:11:00Z"
lastmod = "2015-08-27T07:46:00Z"
weight = 45400
keywords = [ "arp" ]
aliases = [ "/questions/45400" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ethernet packet & ARP](/questions/45400/ethernet-packet-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45400-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From viewing a random capture taken on a Windows host in my network, is it normal to see two different structured ARP related packets:</p><ol><li>An ethernet frame with a broadcast destination address of FF:FF containing an ARP request with a target hardware address of 00:00</li><li>An ethernet frame where the hardware destination address AND target hardware address are the same</li></ol><p>Are there any specific scenarios that would explain where you would see the packet structured in point 1 over point 2 &amp; vice versa?</p></div><div id="question-tags" class="tags-container tags">arp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/7ed8c3ce35fb8f90f49428398992b223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brad_101&#39;s gravatar image" /><p>Brad_101<br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brad_101 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Aug '15, 06:13</p></div></div><div id="comments-container-45400" class="comments-container"></div><div id="comment-tools-45400" class="comment-tools"></div><div class="clear"></div><div id="comment-45400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45403"></span>

<div id="answer-container-45403" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45403-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>UpdatedAnswer because a trace was posted:</strong><br />
In the tracefile different forms of ARPs could be seen:<br />
Case <strong>1</strong>: Frame #1, A normal Broadcasted ARP-Request<br />
Case <strong>2</strong>: Frame #2, It is a normal Unicast Response to a ARP Request<br />
Case <strong>3</strong>: Frame #11, An Unicast ARP request mostly used to refresh the ARP Cache<br />
Case <strong>4</strong>: Frame #6, It is marked as Gratious ARP (Reply) by Wireshark, but in accordance to the <a href="https://www.ietf.org/rfc/rfc3927.txt">RFC 3927</a> it is an ARP Announcement)<br />
Case <strong>5</strong>: Frame #17, It is marked as Gratious ARP (Reply) and also as a duplicated IP by Wireshark, but in accordance to the RFC 3927 it is an ARP Announcement)<br />
</p><p>So the problem is that the IP address 192.168.0.120 is used by 3 MAC addresses. Of course it could be, that these MAC Adresses belongs to the same host. But nevertheless if I were you, I would investigate it if it is correctly.</p><p>Here is a nice link about ARP: <a href="http://linux-ip.net/html/ether-arp.html">http://linux-ip.net/html/ether-arp.html</a></p><hr /><p>Next I have listed some special types of ARP packets:<br />
<br />
</p><p><strong>The Gratious ARP Request:</strong><br />
A gratuitous ARP request is an ARP request packet, in which the source and destination IP are both set to the IP of the machine, which is issuing the packet and the destination MAC is the <strong>ff:ff:ff:ff:ff:ff</strong> broadcast address. Ordinarily, the reply packet will not occur.<br />
<em>Example:</em></p><pre><code>Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: 00:b0:9f:38:a3:d5, Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request/gratuitous ARP)
    Hardware type: Ethernet (1)
    Protocol type: IP (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: request (1)
    [Is gratuitous: True]
    Sender MAC address: 00:b0:9f:38:a3:d5
    Sender IP address: 192.168.10.2 (192.168.10.2)
    Target MAC address: Broadcast (ff:ff:ff:ff:ff:ff)
    Target IP address: 192.168.10.2 (192.168.10.2)
 </code></pre><br />
<p><strong>The Gratious ARP Response/Reply</strong><br />
A gratuitous ARP reply is an ARP Response/Reply packet, in which the source and destination IP are both set to the IP of the machine, which is issuing the packet and the target MAC is the sender MAC. A gratuitous ARP Response/Reply is a reply, to which no request has been made. It could be a in some cases a directed one. (For example duplicate Address detection)<br />
<em>Example:</em></p><pre><code>Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: 00:b0:9f:38:a3:d5, Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (reply/gratuitous ARP)
    Hardware type: Ethernet (1)
    Protocol type: IP (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: reply (2)
    [Is gratuitous: True]
    Sender MAC address: 00:b0:9f:38:a3:d5
    Sender IP address: 192.168.10.2 (192.168.10.2)
    Target MAC address: 00:b0:9f:38:a3:d5
    Target IP address: 192.168.10.2 (192.168.10.2)</code></pre><br />
<p><strong>The ARP Probe RFC 3927</strong><br />
A host probes to see if an address is already in use by broadcasting an ARP Request for the desired address. The client MUST fill in the 'sender hardware address' field of the ARP Request with the hardware address of the interface through which it is sending the packet. The 'sender IP address' field MUST be set to all zeroes, to avoid polluting ARP caches in other hosts on the same link in the case where the address turns out to be already in use by another host.<br />
In addition, if A host MUST respond to a conflicting ARP packet as described in either (a) or (b) below:</p><p>(a) Upon receiving a conflicting ARP packet, a host MAY elect to immediately configure a new IPv4 Link-Local address as described above, or (b) If a host currently has active TCP connections or other reasons to prefer to keep the same IPv4 address, and it has not seen any other conflicting ARP packets within the last DEFEND_INTERVAL seconds, then it MAY elect to attempt to defend its address by recording the time that the conflicting ARP packet was received, and then broadcasting one single ARP announcement, giving its own IP and hardware addresses as the sender addresses of the ARP. Having done this, the host can then continue to use the address normally without any further special action. However, if this is not the first<br />
<em>Example</em></p><pre><code>Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: 00:b0:9f:38:a3:d5, Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol 
    Hardware type: Ethernet (1)
    Protocol type: IP (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: reply (2)
    [Is gratuitous: True]
    Sender MAC address: 00:b0:9f:38:a3:d5
    Sender IP address: 0.0.0.0
    Target MAC address: 00:00:00:00:00:00
    Target IP address: 192.168.10.2</code></pre><br />
<p><strong>The ARP Announcement RFC 3927</strong><br />
An ARP announcement is identical to the ARP Probe described above, except that now the sender and target IP addresses are both set to the host's newly selected IPv4 address. The purpose of these ARP announcements is to make sure that other hosts on the link do not have stale ARP cache entries left over from some other host that may previously have been using the same address.<br />
In addition, if during this period the host receives any ARP Probe where the packet's 'target IP address' is the address being probed for, and the packet's 'sender hardware address' is not the hardware address of the interface the host is attempting to configure, then the host MUST similarly treat this as an address conflict and select a new address as above.This can occur if two (or more) hosts attempt to configure the same IPv4 Link-Local address at the same time.<br />
<em>Example</em></p><pre><code>Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: 00:b0:9f:38:a3:d5, Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol 
    Hardware type: Ethernet (1)
    Protocol type: IP (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: reply (2)
    [Is gratuitous: True]
    Sender MAC address: 00:b0:9f:38:a3:d5
    Sender IP address: 192.168.10.2
    Target MAC address: 00:00:00:00:00:00
    Target IP address: 192.168.10.2</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Aug '15, 14:58</p></div></div><div id="comments-container-45403" class="comments-container"><span id="45404"></span><div id="comment-45404" class="comment"><div id="post-45404-score" class="comment-score"></div><div class="comment-text"><p>Thanks Christian.</p><p>What would a frame look like containing a 'normal' ARP request? I thought the first case above would have been it(?).</p><p>After posting the question, I noticed that in the second case it is in fact an ARP request to a VRRP IP but the ARP header doesn't mention 'gratuitous'. Would you still feel that frame is a gratuitous ARP request?</p><p>I am just trying to understand what would be normal, what they'd look &amp; in what conditions/scenarios you'd expect to see other (perhaps gratuitous) ARP's and what would they look like - how would you differentiate one from the other basically....</p></div><div id="comment-45404-info" class="comment-info"><span class="comment-age">(27 Aug '15, 08:33)</span> Brad_101</div></div><span id="45413"></span><div id="comment-45413" class="comment"><div id="post-45413-score" class="comment-score"></div><div class="comment-text"><p>Yes you are right, I mixed the fields. It would be easier to talk about with a picture.<br />
Case 1: is a normal ARP Request.<br />
<br />
</p></div><div id="comment-45413-info" class="comment-info"><span class="comment-age">(27 Aug '15, 11:47)</span> Christian_R</div></div><span id="45414"></span><div id="comment-45414" class="comment"><div id="post-45414-score" class="comment-score"></div><div class="comment-text"><p>Please upload a capture file somewhere publicly accessible, like www.cloudshark.org, and post a link to the capture file.</p><p>You said "An ethernet frame where the hardware destination address AND target hardware address are the same." A gratuitous ARP is when the sender IP address and target IP address are the same, not when the hardware addresses are the same.</p><p>To give a meaningful answer, we need to see the actual Ethernet frames, including hardware addresses, IP addresses, and opcode field.</p><p>If the Ethernet destination address and the target hardware address are the same, that simply means that it is a unicast ARP, which can be seen in different circumstances.</p></div><div id="comment-45414-info" class="comment-info"><span class="comment-age">(27 Aug '15, 12:10)</span> Jim Aragon</div></div><span id="45415"></span><div id="comment-45415" class="comment"><div id="post-45415-score" class="comment-score"></div><div class="comment-text"><p>@Jim Aragon: Yes you are right with the tracefile. I read some of the question details wrong.</p></div><div id="comment-45415-info" class="comment-info"><span class="comment-age">(27 Aug '15, 12:16)</span> Christian_R</div></div><span id="45419"></span><div id="comment-45419" class="comment"><div id="post-45419-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/file/d/0BxWWq7ozi-PFakpYbEJfYzBQMFU/view?usp=sharing">https://drive.google.com/file/d/0BxWWq7ozi-PFakpYbEJfYzBQMFU/view?usp=sharing</a></p><p>With this example capture:</p><ol><li>Is packet 1 &amp; 2 a normal ARP request and reply?</li><li>What is packet 27 &amp; 28 then? The destination IP is a VRRP IP (hosts default gateway). The ethernet destination address is the MAC address of the target IP address which the ARP request is asking for - why is that?</li></ol></div><div id="comment-45419-info" class="comment-info"><span class="comment-age">(27 Aug '15, 13:15)</span> Brad_101</div></div><span id="45420"></span><div id="comment-45420" class="comment not_top_scorer"><div id="post-45420-score" class="comment-score"></div><div class="comment-text"><p>I am preparing an answer... it will be a longer one</p></div><div id="comment-45420-info" class="comment-info"><span class="comment-age">(27 Aug '15, 13:38)</span> Christian_R</div></div><span id="45433"></span><div id="comment-45433" class="comment not_top_scorer"><div id="post-45433-score" class="comment-score"></div><div class="comment-text"><p>Fram27 is Case 3. Frame28 is Case 2.</p><p>The VRRP device is only allowed ro communicate with his VRRP addres. And sometimes every Device refreshes his ARP cache. To reduce Broadcasts they try ot fitst as an Unicast ARP Request.</p></div><div id="comment-45433-info" class="comment-info"><span class="comment-age">(27 Aug '15, 21:44)</span> Christian_R</div></div><span id="45453"></span><div id="comment-45453" class="comment not_top_scorer"><div id="post-45453-score" class="comment-score"></div><div class="comment-text"><p>Thanks Christian for your help.</p></div><div id="comment-45453-info" class="comment-info"><span class="comment-age">(28 Aug '15, 06:34)</span> Brad_101</div></div></div><div id="comment-tools-45403" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-45403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

