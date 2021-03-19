+++
type = "question"
title = "Routing traffic from primary router to firewall with IPSec tunnel not working"
description = '''I have both a ASUS RT-AC68U primary router and a Zywall USG20W firewall connected to the Internet. The firewall supports an IPSec tunnel to a remote location. The primary router has a static route for the remote network pointed to the LAN firewall connection. All routing appears to be working. When ...'''
date = "2015-06-07T11:04:00Z"
lastmod = "2015-06-08T12:53:00Z"
weight = 42947
keywords = [ "firewall", "router", "ipsec" ]
aliases = [ "/questions/42947" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Routing traffic from primary router to firewall with IPSec tunnel not working](/questions/42947/routing-traffic-from-primary-router-to-firewall-with-ipsec-tunnel-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42947-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have both a ASUS RT-AC68U primary router and a Zywall USG20W firewall connected to the Internet. The firewall supports an IPSec tunnel to a remote location. The primary router has a static route for the remote network pointed to the LAN firewall connection. All routing appears to be working. When in this configuration I cannot bring up an https session with my remote NAS box. If I add a router to my PC for the remote network pointed directly to the firewall, the https session works fine. So, bouncing the traffic thru the primary router is not working. Running wireshark, I see the following error messages:</p><p>171 16.375639000 172.29.35.30 172.29.27.100 TCP 66 [TCP Spurious Retransmission] 443→1682 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0 MSS=1386 SACK_PERM=1 WS=16</p><p>172 16.375701000 172.29.27.100 172.29.35.30 TCP 66 [TCP Dup ACK 133#1] 1682→443 [ACK] Seq=210 Ack=1 Win=66304 Len=0 SLE=0 SRE=1</p><p>I did try lowering my MTU on the PC Ethernet port to 1386 thinking the primary router may be passing too large of a packet for the IPSec tunnel on the Firewall, but the same problem occurred. Any thoughts on what might be happening?</p></div><div id="question-tags" class="tags-container tags">firewall router ipsec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '15, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/f815dcd043dee3bc2e98014e2a2b93b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SedonaRider&#39;s gravatar image" /><p>SedonaRider<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SedonaRider has no accepted answers">0%</span></p></div></div><div id="comments-container-42947" class="comments-container"><span id="42949"></span><div id="comment-42949" class="comment"><div id="post-42949-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace on cloudshark or dropbox?</p></div><div id="comment-42949-info" class="comment-info"><span class="comment-age">(07 Jun '15, 11:59)</span> Christian_R</div></div><span id="42950"></span><div id="comment-42950" class="comment"><div id="post-42950-score" class="comment-score"></div><div class="comment-text"><p>It is my first time using Cloudshark, but I think it is now uploaded. The URL is: <a href="https://www.cloudshark.org/captures/c8bf551babc8">https://www.cloudshark.org/captures/c8bf551babc8</a><br />
</p><p>My PC is 172.29.27.100 and the NAS box is 172.29.35.30</p><p>I should add that I have a ping monitor running in the background which works fine, indicating the routing is set up correctly from my PC to the primary router, to the firewall, across the IPSec VPN to the remote location and back.<br />
</p></div><div id="comment-42950-info" class="comment-info"><span class="comment-age">(07 Jun '15, 13:19)</span> SedonaRider</div></div></div><div id="comment-tools-42947" class="comment-tools"></div><div class="clear"></div><div id="comment-42947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42952"></span>

<div id="answer-container-42952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42952-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What I can say is that the SYN and the ICMP Request got an answer. But the ACK of the 3Way Handshake and all other following packets don´t reach the NAS. The cause I can´t tell you at the moment. Can you trace next to the internal FW or the NAS?</p><p>And as you told you send to the router Asus and the Answers are sent from the FW directly to the client. So it could be interesting what happens between Router and FW.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '15, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div></div><div id="comments-container-42952" class="comments-container"><span id="42953"></span><div id="comment-42953" class="comment"><div id="post-42953-score" class="comment-score"></div><div class="comment-text"><p>Thank you for looking at the records. It is surprising that bouncing the packet thru the primary router would disrupt the communication. I uploaded a trace of where I have the static route in my PC and the communication works fine.<br />
</p><p><a href="https://www.cloudshark.org/captures/56ac591188f5">https://www.cloudshark.org/captures/56ac591188f5</a></p><p>I am not experienced with reading traces, but I do see what you are saying when comparing it to the trace where it works.<br />
</p><p>I agree it would be good to see what is happening between the ASUS and firewall, plus probably the firewall and NAS box at the remote location. The ASUS static route is working for packets, so I would suspect the packet is being forwarded to the firewall. There are no error or blocked messages in the log, so it would seem the firewall would pass this forward to the NAS box as it has the other messages. I wonder if there is something in the SSL handshake that does not like the return being one hop shorter.<br />
</p></div><div id="comment-42953-info" class="comment-info"><span class="comment-age">(07 Jun '15, 17:49)</span> SedonaRider</div></div><span id="42959"></span><div id="comment-42959" class="comment"><div id="post-42959-score" class="comment-score"></div><div class="comment-text"><p>It is like I guessed. But why it is so I Can't tell you without further documentation.</p></div><div id="comment-42959-info" class="comment-info"><span class="comment-age">(08 Jun '15, 00:13)</span> Christian_R</div></div></div><div id="comment-tools-42952" class="comment-tools"></div><div class="clear"></div><div id="comment-42952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42957"></span>

<div id="answer-container-42957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42957-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm personally seeing 4 or so (RST,ACK) packets to that IP address of 172.29.35.30. Which tells me that packets are indeed getting there, however, something (possibly a firewall) is blocking traffic to there. Please correct me if I'm wrong guys.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '15, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-42957" class="comments-container"><span id="42961"></span><div id="comment-42961" class="comment"><div id="post-42961-score" class="comment-score"></div><div class="comment-text"><p>The RST are send by the client. In this case they are just a follow up.</p></div><div id="comment-42961-info" class="comment-info"><span class="comment-age">(08 Jun '15, 00:17)</span> Christian_R</div></div><span id="42962"></span><div id="comment-42962" class="comment"><div id="post-42962-score" class="comment-score"></div><div class="comment-text"><p>Ok got it, but what could be causing the client to be sending the RST packets? I do see that the 3-way handshake is successful to 172.29.35.30 and then there is a client Hello at the ssl handshake, then there are a whole bunch of Hello retransmissions from the client to the NAS.</p></div><div id="comment-42962-info" class="comment-info"><span class="comment-age">(08 Jun '15, 00:23)</span> Beldum</div></div><span id="42963"></span><div id="comment-42963" class="comment"><div id="post-42963-score" class="comment-score"></div><div class="comment-text"><p>The prob is that the 3way handshake is not succesfully for both sides. The NAS is missing the ACK (asuming , because I only have the trace of the client) And the RST is probably application related in this case.</p></div><div id="comment-42963-info" class="comment-info"><span class="comment-age">(08 Jun '15, 00:33)</span> Christian_R</div></div></div><div id="comment-tools-42957" class="comment-tools"></div><div class="clear"></div><div id="comment-42957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42983"></span>

<div id="answer-container-42983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42983-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently there is asymmetric routing in your setup.</p><p><strong>Frame #1:</strong> Source/Destination MAC both Austek. So, the SYN goes to your ASUS router<br />
<strong>Frame #2:</strong> Source MAC Zyxel: Destination MAC: Austek. So, the SYN-ACK went trough the ZyWall. It's strange that the firewall let it pass, as it has not seen the SYN frame, <strong>UNLESS</strong> the Asus router does a L2 forward to the Zywall (which comments in the question suggest).<br />
<strong>Frame #3:</strong> Source/Destination MAC both Austek. So, the SYN goes to your ASUS router, as well as the next few frames.</p><p>The ZyWall is a statefull firewall, and those devices don't like to see only parts of a TCP connection. They <strong>need</strong> to see the whole traffic to be able to handle it correctly.</p><p>To test my assumption, please add a route to the remote network to the ZyWall on your PC. If that works, there is something wrong with the L2 forward of the router to the Firewall (maybe the firewall does some MAC checks as well). If it does not work, even with the route to the firewall, there is something else broken in your network and/or router/firewall. However, it's impossible to figure out what, by looking at capture files! So, in that case, please double check the configuration of all involved systems and ask your local ZyWall guru for help.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '15, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-42983" class="comments-container"><span id="42984"></span><div id="comment-42984" class="comment"><div id="post-42984-score" class="comment-score"></div><div class="comment-text"><p>Yes, the route is asymmetrical. I have added the route to the remote network to my PC so it points directly to the Zywall firewall instead of the primary router and everything works fine. I had not thought of the firewall doing mac checks. It is a good point. However, you would think something would turn up in the log of the Zywall if it detects a problem. I wonder if the ReadyNAS box is detecting a different hop count each way and dropping the session. Hence, the reason why no message is returned. I have not found a log to check on that box.</p></div><div id="comment-42984-info" class="comment-info"><span class="comment-age">(08 Jun '15, 13:36)</span> SedonaRider</div></div><span id="42985"></span><div id="comment-42985" class="comment"><div id="post-42985-score" class="comment-score"></div><div class="comment-text"><p>It's (most certainly) <strong>not</strong> the NAS, as a different hop count (TTL) is totally normal and should not lead to any network disruption.</p><p>I think it's the ZyWall, even if it does not log anything. Could be a bug or a simple (missing) config option.</p></div><div id="comment-42985-info" class="comment-info"><span class="comment-age">(08 Jun '15, 13:41)</span> Kurt Knochner ♦</div></div><span id="42993"></span><div id="comment-42993" class="comment"><div id="post-42993-score" class="comment-score"></div><div class="comment-text"><p>If the NAS had a problem with TTL counts, it would not allowed to connect the nas to a network where a dynamic routing protocol is active.</p></div><div id="comment-42993-info" class="comment-info"><span class="comment-age">(08 Jun '15, 22:30)</span> Christian_R</div></div></div><div id="comment-tools-42983" class="comment-tools"></div><div class="clear"></div><div id="comment-42983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

