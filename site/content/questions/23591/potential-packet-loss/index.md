+++
type = "question"
title = "Potential Packet Loss"
description = '''2 sites connected by VPN over WAN link. We are replicating our VMware VMs over link from our head office (Site A) to a hosted service provider (Site B). 10MB fibre at our end and 100MB at their end. VPN coming from our MS TMG 2010 box (edge firewall mode) to the Hosted Providers Cisco ASA. Have foll...'''
date = "2013-08-06T09:35:00Z"
lastmod = "2013-08-06T22:35:00Z"
weight = 23591
keywords = [ "packetloss", "wireshark" ]
aliases = [ "/questions/23591" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Potential Packet Loss](/questions/23591/potential-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23591-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>2 sites connected by VPN over WAN link. We are replicating our VMware VMs over link from our head office (Site A) to a hosted service provider (Site B). 10MB fibre at our end and 100MB at their end.</p><p>VPN coming from our MS TMG 2010 box (edge firewall mode) to the Hosted Providers Cisco ASA. Have followed recommendation for TMG-Cisco ASA VPN settings (encryption, integrity, DH group etc).</p><p>The VPN is stable, no disconnects.</p><p>But we are getting some unusual connection behaviour. VMware SRM connection issues - various errors/disconnects and RDP session hangs amongst other intermittent things.</p><p>So ran a Wireshark trace on both Virtual Center Servers (one at each site) during the same time period so that I could analyse packets leaving one side and arriving at the other side. Fairly new to Wireshark but will list my findings:</p><ul><li>Seem to have intermittent packet loss in both directions. Can see packets leaving Site A for example and not arriving at Site B. And vice versa.</li><li>Seem to be packets being sent ‘out of order’. Pardon my poor description but when matching up packets on both captures, I can see packets leaving in sequence but upon checking destination server they are in different order. Again happens in both directions. Not sure if this is normal behaviour.</li><li>Packets arriving with different ACK number? Not sure if this is possible but looks like the same packet which has left Site A and arrived at Site B but with different ACK number.</li></ul><p>I tried carrying out simultaneous captures on both Virtual Centers and on the TMG box to see if I could pin down exactly where the packet loss is occurring but I can only see flow of traffic in the one direction on the TMG. Can see traffic coming back the way from Site B on the TMG but obviously it is the encrypted VPN traffic so am unable to see if the packet loss is on the TMG or somewhere else.</p><p>Can anyone offer any hints or tips which would aid me nailing this one down? I believe I can capture traffic on my laptop for a non-windows device (like the Cisco ASA) , would this be my best bet, to run simultaneous captures on the 2 VC’s, the TMG and for the Cisco ASA??</p><p>Should point out, we have other VPNs setup to less bandwidth and higher contended links via VPN and don't have any connection issues.</p><p>Many thanks Steve</p></div><div id="question-tags" class="tags-container tags">packetloss wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/4aa0f184af157a853f02a5faaa8cb4da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tebers&#39;s gravatar image" /><p>tebers<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tebers has no accepted answers">0%</span></p></div></div><div id="comments-container-23591" class="comments-container"></div><div id="comment-tools-23591" class="comment-tools"></div><div class="clear"></div><div id="comment-23591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23599"></span>

<div id="answer-container-23599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23599-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I read your question correctly, you made traces on the VM guests and on the TMG box itself. As these boxes will process the traffic themselves and may have some optimizations (TCP checksum offload, TCP segmentation offload, etc), you will not see exactly what is put on the network (capturing takes place between the IP stack and the NIC driver). It is better to use mirror/span ports to copy the packets found on the network to Wireshark.</p><p>I would proceed with one Wireshark system per location:</p><ol><li><p>At Site A I would span the port on which the TMG is connected. You will see the unencrypted data both ways and also the encrypted data both ways (you might want to use a capture filter like "<code>arp or icmp or host &lt;VM site A&gt; or &lt;VPN endpoint site B&gt;</code>"</p></li><li><p>At Site B I would span both ports of the ASA (the Internet side and the WAN side) and then (if needed) use a capture filter of "<code>arp or icmp or host &lt;VM site B&gt; or &lt;VPN endpoint site A&gt;</code>"</p></li></ol><p>Now you can follow the whole flow and see where the packet-loss and re-ordering is occurring. Please note that IPsec ESP packets have a sequence number too, so you can check those too for packet-loss and re-ordering.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '13, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '13, 22:38</p></div></div><div id="comments-container-23599" class="comments-container"><span id="23655"></span><div id="comment-23655" class="comment"><div id="post-23655-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply.</p><p>Well the first trace I carried out was just on VC's. Simply because the VC's hold the SRM role and it is SRM connection issues we are seeing.</p><p>The second set of traces was on the VC's and the TMG and that was where I discovered that I was only seeing flow of traffic in one direction.</p><p>And I had disabled checksum offload on all the NICs on the VC's and the TMG before running all the traces.</p><p>But regardless of all that, what you have suggested will still be the case. Now... I understand the logic of it perfectly but being fairly new to Wirehsark I am not 100% sure how to put it into practice! So I may come back to you. :)</p><p>Thanks again, Steve</p></div><div id="comment-23655-info" class="comment-info"><span class="comment-age">(08 Aug '13, 08:25)</span> tebers</div></div></div><div id="comment-tools-23599" class="comment-tools"></div><div class="clear"></div><div id="comment-23599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

