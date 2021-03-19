+++
type = "question"
title = "How do you capture Subnetwork packets in wireshark ?"
description = '''Hello , I have a pfSense installed as a Router in my local network , I have Installed WireShark on pfSense &amp;amp; am able to trace all the packets passing through LAN or wlan in my local network. but how can i trace the traffic of subnets under my local network. ? I need to trace the client who are c...'''
date = "2015-11-05T00:48:00Z"
lastmod = "2015-11-05T03:31:00Z"
weight = 47277
keywords = [ "wireshark-1.12.8" ]
aliases = [ "/questions/47277" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do you capture Subnetwork packets in wireshark ?](/questions/47277/how-do-you-capture-subnetwork-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47277-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello ,</p><p>I have a pfSense installed as a Router in my local network , I have Installed WireShark on pfSense &amp; am able to trace all the packets passing through LAN or wlan in my local network. but how can i trace the traffic of subnets under my local network. ?</p><p>I need to trace the client who are connected with the subnet which is created by making hotspots on local network . I tried with the following approach on CLI but did not get desired information :- <a href="http://www.binarytides.com/tcpdump-tutorial-sniffing-analysing-packets/">http://www.binarytides.com/tcpdump-tutorial-sniffing-analysing-packets/</a></p><p>Thanks in Advance</p></div><div id="question-tags" class="tags-container tags">wireshark-1.12.8</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/95b8ef56b38cb48d36b04d1dc548a328?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user5901&#39;s gravatar image" /><p>user5901<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user5901 has no accepted answers">0%</span></p></div></div><div id="comments-container-47277" class="comments-container"></div><div id="comment-tools-47277" class="comment-tools"></div><div class="clear"></div><div id="comment-47277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47282"></span>

<div id="answer-container-47282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47282-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not 100% certain that you are using the correct terminology for subnetworks. Normally, if we say our company network is 10.0.0.0/8, (so we are using all of 10.x.x.x), we might then break this down into subnetworks like 10.0.1.0/24, and 10.0.2.0/24 (each subnet having an address space of 254 hosts). We would then have a router say with gateway address 10.0.1.1 and 10.0.2.1 routing between those subnetworks. If this is what you mean and all of the traffic you want to see is visible to pfSense on your router, then you could capture traffic just for the 2nd subnet with the capture filter "net 10.0.2.0/24".</p><p>If however by subnetworks, you mean traffic that is local to a particular LAN and might not all reach the router you mention, you will need to use something like port-mirroring on a switch with an interface in that subnetwork, and then capture that on a PC running Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-47282" class="comments-container"><span id="47290"></span><div id="comment-47290" class="comment"><div id="post-47290-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer.</p><p>Let me explain my architecture to you, I have a local network of 192.168.1.0/24 and I can monitor all the LAN/WLAN traffic of this network. Now Let us suppose if a user with ip 192.168.1.10 makes a hotspot/wifi using his system and creates a subnetwork of 10.10.2.0/24 range. So,will I be able to detect the traffic/Packets of this subnetwork which is created by making hotspots. ?</p></div><div id="comment-47290-info" class="comment-info"><span class="comment-age">(05 Nov '15, 04:45)</span> user5901</div></div><span id="47356"></span><div id="comment-47356" class="comment"><div id="post-47356-score" class="comment-score"></div><div class="comment-text"><p>Supposing your pfSense is the only gateway from 192.168.1.0/24 to the outside world:</p><ul><li><p>you WILL be able to see the traffic which goes between 10.10.2.0/24 and the outside world,</p></li><li><p>you WILL NOT be able to see the traffic which runs inside the 10.10.2.0/24 (between the "hotspot" users).</p></li></ul><p>Now, I <em>suppose</em> that in order to allow bi-directional traffic between 10.10.2.0/24 and the outside world, the 192.168.1.10 has to apply NAT on the traffic which goes from 10.10.2.0/24 to the outside world, because otherwise you would not forward the response packets for 10.10.2.0/24's requests to 192.168.1.10, as you probably haven't set up "route -net 10.10.2.0/24 gw 192.168.1.10" in your pfSense.</p><p>If the above is true, then you'll see all the traffic between 10.10.2.0/24 and the outside world, but its "local side" IP address will always be 192.168.1.10 in your captures. So you will not be able to reliably tell 192.168.1.10's own traffic from the traffic of the 10.10.2.0/24 members hidden behind 192.168.1.10.</p></div><div id="comment-47356-info" class="comment-info"><span class="comment-age">(07 Nov '15, 00:03)</span> sindy</div></div><span id="47502"></span><div id="comment-47502" class="comment"><div id="post-47502-score" class="comment-score"></div><div class="comment-text"><p>Basically, if the 10.10.2.0/24 network is being NAT'd to the 192.168.1.10 address, then NO, you will not see any source IP addresses from the 10.10.2.0 network nor will you see any L2 MAC addresses as a source other than the 192.168.1.10 device.</p><p>The only way you might suspect this, is due to a sudden increase in traffic to/from that particular address.</p><p>Best to just use a wifi tool such as kismet or inSSIDer to periodically detect rogue AP's within your office.</p></div><div id="comment-47502-info" class="comment-info"><span class="comment-age">(10 Nov '15, 20:13)</span> Rooster_50</div></div></div><div id="comment-tools-47282" class="comment-tools"></div><div class="clear"></div><div id="comment-47282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

