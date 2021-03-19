+++
type = "question"
title = "How can Wireshark see packets not sent to the host&#x27;s IP address?"
description = '''hi, I&#x27;m looking for more detailed description on how Wireshark works.  From the Wireshark book from Laura Chappell it says the we have: Network --&amp;gt; winpcap / libpcap (capture filters) --&amp;gt; dumpcap (the actual capture engine) --&amp;gt; core dump (filters, dissectors ...).  I guess the NIC driver is...'''
date = "2016-01-08T05:14:00Z"
lastmod = "2016-01-08T16:45:00Z"
weight = 48969
keywords = [ "wireshark" ]
aliases = [ "/questions/48969" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can Wireshark see packets not sent to the host's IP address?](/questions/48969/how-can-wireshark-see-packets-not-sent-to-the-hosts-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>I'm looking for more detailed description on how Wireshark works.</p><p>From the Wireshark book from Laura Chappell it says the we have:</p><p>Network --&gt; winpcap / libpcap (capture filters) --&gt; dumpcap (the actual capture engine) --&gt; core dump (filters, dissectors ...).</p><p>I guess the NIC driver is first that will "see" the frame , correct ?</p><p>If a host receives a broadcast that has not it's IP in the layer 3 header it will drop the packet, correct ?</p><p>So how is Wireshark able to "see" the packet in question ?</p><p>BR</p><p>Adam<br />
</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '16, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '16, 16:48</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-48969" class="comments-container"></div><div id="comment-tools-48969" class="comment-tools"></div><div class="clear"></div><div id="comment-48969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="49003"></span>

<div id="answer-container-49003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49003-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If a host receives a broadcast that has not it's IP in the layer 3 header it will drop the packet, correct ?</p></blockquote><p>There are several paths through which a packet can travel in the host networking stack.</p><p>The "regular" networking stack will, in typical cases, drop IP packets if they're not sent to one of the host's IP addresses <em>or</em> to a broadcast IP address, and, even for those packets, it'll drop them (perhaps with an ICMP response or a TCP RST or something such as that) if there's nothing running on the host listening for those packets at the transport layer (or listening for raw IP packets).</p><p>The path used by the mechanisms that libpcap and WinPcap use does <em>not</em>, by default, filter on anything in layer 3 whatsoever - it doesn't even <em>look at</em> the IP header. The mechanisms may allow a simple layer 2 filter be specified to check, for example, the Ethernet type of a packet, but, if they do provide that type of filtering, libpcap and WinPcap don't use it. Instead, they either tell those mechanisms to apply a "capture filter" (which is what the capture filter string you type into tcpdump or Wireshark or TShark or dumpcap is translated into), and those mechanisms drop packets that don't match the filter, or, if the mechanism doesn't support capture filters (they're supported on Linux, *BSD, OS X, Solaris 11, AIX, and Windows), they filter out the packets themselves.</p><p>So, if there's no capture filter, <em>every</em> packet supplied by the NIC to the host should go through the host networking stack up to the application using libpcap/WinPcap.</p><p>Now, for <em>unicast</em> (rather than broadcast) packets, the NIC will normally reject packets not sent to one of the adapter's MAC addresses, and not even deliver them to the host. However, wired NICs can usually be put into "promiscuous" mode, in which case all packets they see get passed to the host even if they're not to one of the "right" MAC addresses, and they'll get provided to the capture mechanism. For wireless NICs, promiscuous mode often doesn't work, and you may need "monitor" mode.</p><p>Many NICs won't even look at the layer 3 headers of packets at all. Those that do - for example, those doing IP header checksum checking, TCP or UDP packet checksum checking, IP or TCP reassembly, redirecting different packet flows to different queues or interrupting different hosts, etc. - may disable all of that in promiscuous mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49003" class="comments-container"></div><div id="comment-tools-49003" class="comment-tools"></div><div class="clear"></div><div id="comment-49003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48971"></span>

<div id="answer-container-48971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48971-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark (if set by the user) sets the interface via the capture library into promiscuous mode. This allows the NIC to receive all traffic on the wire. See the Wireshark <a href="https://www.wireshark.org/faq.html#q6.6">FAQ</a> for a little more info along with <a href="https://en.wikipedia.org/wiki/Promiscuous_mode">Wikipedia</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48971" class="comments-container"><span id="49004"></span><div id="comment-49004" class="comment"><div id="post-49004-score" class="comment-score"></div><div class="comment-text"><p>Even when <em>not</em> in promiscuous mode, many (most?) NICs won't bother looking at the layer 3 header, so they'll deliver to the host packets with the right MAC destination address but the wrong IP destination address.</p></div><div id="comment-49004-info" class="comment-info"><span class="comment-age">(08 Jan '16, 16:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-48971" class="comment-tools"></div><div class="clear"></div><div id="comment-48971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48983"></span>

<div id="answer-container-48983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48983-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Adam,</p><p>the packet filter in the NIC hardware acts only at L2 (MAC address). Once the packet passes the MAC filter because its dst MAC is the NIC's own (or broadcast or multicast to which the NIC is subscribed, as discussed in other question) <strong>or</strong> because the promiscuous mode is on, software (and thus Wireshark or, even more precisely, WinPcap) will get the packet.</p><p>The reason is that the NIC cannot know in advance whether L3 will be OSI, IPX, IPv4, IPv6, ..., and that there is actually little point in filtering at L3 because the mapping of L3 address to L2 address at LAN is mostly 1:1 (except a few exceptions ;-) ).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48983" class="comments-container"><span id="48986"></span><div id="comment-48986" class="comment"><div id="post-48986-score" class="comment-score"></div><div class="comment-text"><p>I wonder what happens to various OS's and NIC drivers and WinPcap\libpcap if a packet with the correct MAC address and an incorrect destination IP address is received. Does anyone know?</p></div><div id="comment-48986-info" class="comment-info"><span class="comment-age">(08 Jan '16, 09:52)</span> grahamb ♦</div></div><span id="48990"></span><div id="comment-48990" class="comment"><div id="post-48990-score" class="comment-score"></div><div class="comment-text"><p>@grahamb, maybe this topic deserves its own question as not everyone is subscribed to everything that happens on this site?</p><p>My understanding is such that as even Windows machines can act as IP routers under circumstances, arrival of a packet with dst MAC of the local interface and dst IP not matching any of the local interfaces' ones should not cause any fireworks as routers simply forward such packets, so protocol stacks of routing-capable OSes should not get mad on receiving such packet when their routing functionality is not enabled.</p><p>So from the point of view of libpcap/WinPcap visibility of such packet, reception of such packet is a standard situation (at least if we talk about IP).</p><p>From the point of view of L3 protocol stacks in general, different reactions to arrival of a packet of non-local dst L3 address when routing is disabled (silent dropping or some error report packet sent upstream) may be required depending on the specification of that particular protocol, and also depending on a particular scenario (e.g. whether the dst IP matches one of local interfaces' subnets or not). Not that I would know what behaviour is required in such case even for IPv4, leaving other protocols aside ;-)</p></div><div id="comment-48990-info" class="comment-info"><span class="comment-age">(08 Jan '16, 12:33)</span> sindy</div></div></div><div id="comment-tools-48983" class="comment-tools"></div><div class="clear"></div><div id="comment-48983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

