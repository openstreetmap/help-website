+++
type = "question"
title = "Computers with LAN?"
description = '''I have two computers connected to a 5port switch in my room. Both computers have the same IP and MAC. Now I also connected the switch to the internet.  _____  ________ | | MAC: AA:CC  | |-----| PC1 | IP: 94.94.94.94  | | |_____| INTERNET ------| SWITCH |   | | _____  | | | | MAC: AA:CC  |________|--...'''
date = "2014-02-03T13:35:00Z"
lastmod = "2014-02-04T02:47:00Z"
weight = 29412
keywords = [ "switch", "lan", "mac-address" ]
aliases = [ "/questions/29412" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Computers with LAN?](/questions/29412/computers-with-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29412-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two computers connected to a 5port switch in my room. Both computers have the same IP and MAC. Now I also connected the switch to the internet.</p><pre><code>                               _____
                ________      |     | MAC: AA:CC
               |        |-----| PC1 | IP:  94.94.94.94
               |        |     |_____|
INTERNET ------| SWITCH |      
               |        |      _____
               |        |     |     | MAC: AA:CC
               |________|-----| PC2 | IP:  94.94.94.94
                              |_____|</code></pre><p>Info:</p><ul><li>MACs are cloned</li><li>Internet works on both computers</li></ul><p>Question:</p><p>If PC1 and PC2 send simultaneously a request for www.google.com/index.html, how does the switch know to which port to forward the answer?</p><p>---------------------------------------------- Further information ----------------------------------------------</p><ul><li><p>If I have Wireshark open on both computers, each instance of Wireshark will sniff totally different packets. Only the broadcast packets are perceived from both instances.</p></li><li><p>On the hub/switch(probably a switch), the blinking occurs only in pairs: PC1-Internet, PC2-Internet. So the switch somehow accurately forwardS the frames to the correct host although both hosts have the same MAC.</p></li></ul></div><div id="question-tags" class="tags-container tags">switch lan mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '14, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/a98c3431c94eacee9b9549d708fdc9da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pitihkos&#39;s gravatar image" /><p>Pitihkos<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pitihkos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '14, 04:50</p></div></div><div id="comments-container-29412" class="comments-container"></div><div id="comment-tools-29412" class="comment-tools"></div><div class="clear"></div><div id="comment-29412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29413"></span>

<div id="answer-container-29413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29413-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure what the goal is in this configuration but I'll give it a try anyways:</p><p>I think you are missing a router in the picture here. The router keeps an ARP table and map IP addresses to MAC addresses. If the router needs to send a packet to an IP address that is in its own subnet it will consult the ARP cache and use the MAC address associated with the IP address and put the frame on the ethernet. The switch simply forwards the ethernet frames to all connected devices and its up to the device's NIC to identify and copy frames that match its own MAC address and pass the packet up to the IP layer. This would mean, that both PCs will receive those packets but only one will expect them. The other one will get confused and - if the transport is TCP - will send out RST packets because there is no local socket matching the IP/TCP quadruple. This will break the session at the remote side and no one will be able to communicateusing TCP.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '14, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-29413" class="comments-container"><span id="29426"></span><div id="comment-29426" class="comment"><div id="post-29426-score" class="comment-score"></div><div class="comment-text"><p>Well my router died so I was trying to experiment with an old hub/switch I have. The router is on the side of the ISP so that's why it's not in the picture.</p><p>I added some further info in the question that shows that the packets are actually forwarded to one host at a time.</p></div><div id="comment-29426-info" class="comment-info"><span class="comment-age">(04 Feb '14, 04:52)</span> Pitihkos</div></div></div><div id="comment-tools-29413" class="comment-tools"></div><div class="clear"></div><div id="comment-29413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29421"></span>

<div id="answer-container-29421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29421-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how does the switch know to which port to forward the answer?</p></blockquote><p>The switch learns the MAC addresses of the attached nodes, by looking at the <strong>source</strong> MAC address. In your case it will learn that the <strong>same</strong> MAC address is attached to port 1 (PC1) and port 2 (PC2). Usually the same MAC address can only be 'attached' to one switch port. Now, it depends on the switch firmware and the configuration what happens if it sees the same MAC address on two different ports at the 'same' time. Some switches will block one of the ports (due to Loop detection - <strong>not</strong> Spanning Tree), others will just forward the frames to all 'attached' ports and other switches might even flood those frames to all switch ports.</p><p>As you say, that you can access the internet through the switch at the same time, I <strong>guess</strong> that your switch accepts the situation and simply forwards the frames to both ports. <strong>Or</strong> your switch is actually a HUB, meaning it forwards the frames to all ports anyway.</p><p>Now, there is also IP and TCP. If you send a SYN frame from PC1 to the internet, the SYN-ACK will come back and the switch forwards that frame to both attached systems. That would (most certainly) result in a RESET from PC2, as it never sent the SYN. That RESET 'could' cause trouble and/or confusion on the system that sent the SYN-ACK. However, as you said, you can communicate from <strong>both</strong> systems (PC1 and PC2) <strong>at the same</strong> time, I guess that the firewall on the internal systems (in my example PC2) blocks the SYN-ACK (no information about the SYN in the state table of the firewall) and thus prevents the RESET. So, PC2 gets all answer packets for PC1, but the local firewall simply blocks them. The same applies vice versa.</p><p>That together (switch behavior and local firewall) <strong>probably</strong> makes your setup work (as far as I can say, based on your description), although you have the same MAC address and the same IP address.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '14, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '14, 02:48</p></div></div><div id="comments-container-29421" class="comments-container"><span id="29425"></span><div id="comment-29425" class="comment"><div id="post-29425-score" class="comment-score"></div><div class="comment-text"><p>There is a second problem though that I forgot to mention. Having Wireshark open on both computers doesn't sniff the same packets. Also on the hub/switch, the blinking occurs only in pairs: PC1-Internet, PC2-Internet. So the switch somehow accurately splits the links and actually forward the frames to the correct host although both hosts have the same MAC.</p></div><div id="comment-29425-info" class="comment-info"><span class="comment-age">(04 Feb '14, 04:47)</span> Pitihkos</div></div><span id="29427"></span><div id="comment-29427" class="comment"><div id="post-29427-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Having Wireshark open on both computers doesn't sniff the same packets.</p></blockquote><p>if the firewall drops the frames, you won't see them in Wireshark. Can you please do the following.</p><ul><li>Take a capture file while you do the same on both systems (ping www.google.com and download some smaller files via HTTP).</li><li>Then disable the local firewall on both systems and repeat the test above, while you still capture on both systems.</li><li>Upload the capture files somewhere (google drive, dropbox, cloudshark.org) and post the link here.</li></ul><p>I'm pretty sure, that something or all I mentioned in my answer actually happens on the net ;-)</p><p>Regards<br />
Kurt</p></div><div id="comment-29427-info" class="comment-info"><span class="comment-age">(04 Feb '14, 06:10)</span> Kurt Knochner ♦</div></div><span id="29429"></span><div id="comment-29429" class="comment"><div id="post-29429-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So the switch somehow accurately forwardS the frames to the correct host <strong>although both hosts have the same MAC</strong>.</p></blockquote><p>Are you <strong>sure</strong> that's really the case?</p></div><div id="comment-29429-info" class="comment-info"><span class="comment-age">(04 Feb '14, 06:47)</span> Kurt Knochner ♦</div></div><span id="29436"></span><div id="comment-29436" class="comment"><div id="post-29436-score" class="comment-score"></div><div class="comment-text"><p>Ok, I think I figured out what happens. When I make a GET request from PC1, then all incoming traffic(including response) will be directed to PC1. When I make a new GET request from PC2, then all traffic gets directed to PC2. That explains also how the internet works fine.</p><p>Unfortunately I can't do that as there is a lot of random traffic in the sniffs. Also, there are no firewalls that I am aware of. I run Ubuntu on both.</p></div><div id="comment-29436-info" class="comment-info"><span class="comment-age">(04 Feb '14, 10:57)</span> Pitihkos</div></div><span id="29437"></span><div id="comment-29437" class="comment"><div id="post-29437-score" class="comment-score"></div><div class="comment-text"><p>Well, if you talk to the Internet <strong>first from PC1</strong> and a <strong>few seconds later</strong> from PC2, the switch has obviously enough time to update its mac/port association, by learning from the source MAC address of the SYN frame.</p></div><div id="comment-29437-info" class="comment-info"><span class="comment-age">(04 Feb '14, 11:28)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29421" class="comment-tools"></div><div class="clear"></div><div id="comment-29421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

