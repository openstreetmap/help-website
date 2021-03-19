+++
type = "question"
title = "ARP Broadcast frequency"
description = '''So, 192.168.1.204 device is broadcasting, &quot;Who has 192.168.1.10? Tell 192.168.1.204&quot; I understand this. I see no packet where 192.168.1.10 returns to 192.168.1.204 I understand that it night be directly to 192.168.1.204; and I might not see it. But why does 192.168.1.204 ask so many times? Seem like...'''
date = "2017-02-15T15:49:00Z"
lastmod = "2017-02-17T11:30:00Z"
weight = 59447
keywords = [ "arq", "broadcasting" ]
aliases = [ "/questions/59447" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ARP Broadcast frequency](/questions/59447/arp-broadcast-frequency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So, 192.168.1.204 device is broadcasting, "Who has 192.168.1.10? Tell 192.168.1.204"</p><p>I understand this.</p><p>I see no packet where 192.168.1.10 returns to 192.168.1.204</p><p>I understand that it night be directly to 192.168.1.204; and I might not see it.</p><p>But why does 192.168.1.204 ask so many times?</p><p>Seem like 192.168.1.10 is either not answering or 192.168.1.204 is sending way to many requests.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">arq broadcasting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/02928a0228ba76abd87a58c974b3683e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcalcutt&#39;s gravatar image" /><p>dcalcutt<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcalcutt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '17, 10:47</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-59447" class="comments-container"><span id="59452"></span><div id="comment-59452" class="comment"><div id="post-59452-score" class="comment-score"></div><div class="comment-text"><p>What is "so many times"? ARP cache will time out so it will ask every time it doesn't have it in its cache.</p><p>Also, if it is extremely rapid, are you certain the response is making it back to the requester or if the requested host is in fact replying?</p></div><div id="comment-59452-info" class="comment-info"><span class="comment-age">(15 Feb '17, 17:07)</span> Rooster_50</div></div><span id="59487"></span><div id="comment-59487" class="comment"><div id="post-59487-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/IMG_2823a.jpg" alt="alt text" /></p></div><div id="comment-59487-info" class="comment-info"><span class="comment-age">(16 Feb '17, 15:19)</span> dcalcutt</div></div></div><div id="comment-tools-59447" class="comment-tools"></div><div class="clear"></div><div id="comment-59447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59454"></span>

<div id="answer-container-59454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59454-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But why does 192.168.1.204 ask so many times?</p></blockquote><p>Because it wants to send a packet to 192.168.1.10, and therefore needs to know its MAC address, but, for whatever reason, 192.168.1.10 isn't responding with its MAC address, and neither is any other device on that LAN segment, so it keeps trying in the hopes that eventually somebody will respond.</p><p>That's how ARP works.</p><p>I suggest you figure out what's wrong with 192.168.1.10. If what's wrong with it is that it doesn't exist any more, you need to figure out why 192.168.1.204 is trying to send it packets and fix that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '17, 17:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-59454" class="comments-container"><span id="59466"></span><div id="comment-59466" class="comment"><div id="post-59466-score" class="comment-score"></div><div class="comment-text"><p>Its only occurring for the IP cameras and the DVR that goes with it.</p><p>Same manufacturer, so I'm guessing its the cameras.</p></div><div id="comment-59466-info" class="comment-info"><span class="comment-age">(16 Feb '17, 04:49)</span> dcalcutt</div></div><span id="59485"></span><div id="comment-59485" class="comment"><div id="post-59485-score" class="comment-score"></div><div class="comment-text"><p>I'm assuming that wireshark and only see general packets, as well as packet for the computer I'm using, 192.168.1.148</p><p>Am I correct that if a packet was sent directly from 192.168.1.10 to 192.168.1.204 I would not see it?</p></div><div id="comment-59485-info" class="comment-info"><span class="comment-age">(16 Feb '17, 15:14)</span> dcalcutt</div></div><span id="59490"></span><div id="comment-59490" class="comment"><div id="post-59490-score" class="comment-score"></div><div class="comment-text"><p>What you see on an Ethernet network depends on how the network is constructed.</p><p>If all the hosts on the Ethernet segment are plugged into a <a href="https://wiki.wireshark.org/HubReference">real hub</a>, then, if you're capturing in promiscuous mode, you should be able to see all traffic on the network, whether it's being sent to or from the machine doing the capture or not. If you're <em>not</em> capturing in promiscuous mode, you'll see only broadcast traffic, multicast traffic, traffic sent to the machine doing the capturing, and traffic coming from the machine doing the capturing.</p><p>If they hosts are plugged into a switch, then, unless the host doing the capturing is plugged into a "mirror port" or "SPAN port" or whatever it's called on the switch in question, whether you're capturing in promiscuous mode or not, you'll see only broadcast traffic, multicast traffic, traffic sent to the machine doing the capturing, and traffic coming from the machine doing the capturing. Only if you capture in promiscuous mode <em>on a mirror/SPAN/whatever port</em> will you see all traffic.</p><p>Not all switches <em>support</em> mirror/SPAN/whatever ports. Many devices such as DSL and cable modems, Wi-Fi routers, and even some "hubs" ("switching hubs") are, in fact, switches.</p></div><div id="comment-59490-info" class="comment-info"><span class="comment-age">(16 Feb '17, 22:32)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-59454" class="comment-tools"></div><div class="clear"></div><div id="comment-59454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59512"></span>

<div id="answer-container-59512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The ARP requests are send with a frequency of 1 per second. This is usually an indicator, that the ARP request was never answered.</p><p>You might want to check the configuration, if 192.168.1.10 is referenced somewhere as DVR, gateway, DNS server, time server or somewhere else in the configuration. Please note, that certain parameters might be set a DHCP server.</p><p>To understand the situation you need a trace file from the point of view of 192.168.1.204. As Guy Harris pointed out, this requires a hub or a SPAN port.</p><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-59512" class="comments-container"><span id="59997"></span><div id="comment-59997" class="comment"><div id="post-59997-score" class="comment-score"></div><div class="comment-text"><p>Well the computer I'm using to capture the packets, is on a switch.</p><p>I'm going to run the Ethernet to the router to see if that makes a difference.</p></div><div id="comment-59997-info" class="comment-info"><span class="comment-age">(10 Mar '17, 16:44)</span> dcalcutt</div></div><span id="59998"></span><div id="comment-59998" class="comment"><div id="post-59998-score" class="comment-score"></div><div class="comment-text"><p>WEll, that made no difference.</p><p>I even tried making my computer the same IP address as the router, just to see what would happen. But I got nothing interesting.</p><p>I just want to know if the router is responding to all the request for the MAC addesses</p></div><div id="comment-59998-info" class="comment-info"><span class="comment-age">(10 Mar '17, 17:09)</span> dcalcutt</div></div></div><div id="comment-tools-59512" class="comment-tools"></div><div class="clear"></div><div id="comment-59512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

