+++
type = "question"
title = "monitoring icmp using tcpdump"
description = '''i am new to tcpdump when i used  tcpdump -i cloudbr0 icmp tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on cloudbr0, link-type EN10MB (Ethernet), capture size 65535 bytes 11:20:42.844355 IP 112.X.X.13 &amp;gt; 115.X.X.62: ICMP echo request, id 512, seq 25623, lengt...'''
date = "2013-04-03T23:29:00Z"
lastmod = "2013-04-05T01:53:00Z"
weight = 20073
keywords = [ "tcpdump" ]
aliases = [ "/questions/20073" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [monitoring icmp using tcpdump](/questions/20073/monitoring-icmp-using-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20073-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am new to tcpdump</p><p>when i used</p><p><strong>tcpdump -i cloudbr0 icmp</strong></p><p>tcpdump: verbose output suppressed, use -v or -vv for full protocol decode</p><p>listening on cloudbr0, link-type EN10MB (Ethernet), capture size 65535 bytes</p><p>11:20:42.844355 IP 112.X.X.13 &gt; 115.X.X.62: ICMP echo request, id 512, seq 25623, length 8</p><p>i believe this means 112.X.X.13 is making ICMP request to 115.X.X.62</p><p>But none of the above ip belongs to me nor to my virtual machines.Then why is it showing in my interface.</p><p>If i have enabled promiscuous mode then does that mean,all the packets going through that switch will reach my interface.</p></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/6a6d36cecf235655a1d157c269a4db88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krrypto&#39;s gravatar image" /><p>krrypto<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krrypto has no accepted answers">0%</span></p></div></div><div id="comments-container-20073" class="comments-container"></div><div id="comment-tools-20073" class="comment-tools"></div><div class="clear"></div><div id="comment-20073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="20104"></span>

<div id="answer-container-20104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20104-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do the IP's belong to other systems in the network where your machines are located? If so, then these packets are most likely flooded by the switch. A switch will forward a packet to all ports in the same vlan if the destination mac-address of the packet is unknown to the switch. This can be caused by:</p><ul><li>a system that has been shut off, but it still receives traffic (arp timeouts are usually longer than switch forwarding table timeouts)</li><li>There is asymmetric routing and so one switch does not see outgoing packets from the particular system</li><li>The system has not send any packet for a while</li><li>etc.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '13, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20104" class="comments-container"></div><div id="comment-tools-20104" class="comment-tools"></div><div class="clear"></div><div id="comment-20104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20075"></span>

<div id="answer-container-20075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20075-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Promiscuous mode means all packets passing by the network interface will be captured, it doesn't affect the switch that the NIC is connected to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '13, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-20075" class="comments-container"><span id="20076"></span><div id="comment-20076" class="comment"><div id="post-20076-score" class="comment-score"></div><div class="comment-text"><p>can u tell me how can a packet which is not intended for my machine enters my interface.</p></div><div id="comment-20076-info" class="comment-info"><span class="comment-age">(04 Apr '13, 02:42)</span> krrypto</div></div></div><div id="comment-tools-20075" class="comment-tools"></div><div class="clear"></div><div id="comment-20075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20107"></span>

<div id="answer-container-20107" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20107-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tcpdump -i <strong>cloudbr0</strong> icmp</p></blockquote><p>cloud<strong>br0</strong> sounds like a bridge interface on Linux. If your sniffer system runs in bridge mode, that might be the reason why you see traffic of other systems. Without a detailed description of your setup, it is hard to tell what is going on. So, can you please add some information about that <strong>cloudbr0</strong> interface and how the systems are connected to the switch <strong>and</strong> if the switch is a real switch and not just a <strong>switching hub</strong>.</p><p>BTW: Your switch may run in <strong>fail open mode</strong> due to may errors on a port. In fail open mode, it will basically work like a hub and you will see all traffic. Please check the switch logs.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '13, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '13, 01:53</p></div></div><div id="comments-container-20107" class="comments-container"></div><div id="comment-tools-20107" class="comment-tools"></div><div class="clear"></div><div id="comment-20107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

