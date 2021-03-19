+++
type = "question"
title = "cannot http to server but I can ping it (What else should I analyze?)"
description = '''I have a web server running nagios. When I web to it appears to be getting blocked or not routed from the wireshark output below.  I can ping it and the icmp traffic does appear in Wireshark and I get a proper reply. What can I look at to help me find what is not routing or is blocking it?? 52878 &amp;g...'''
date = "2014-07-10T11:20:00Z"
lastmod = "2014-09-03T07:40:00Z"
weight = 34569
keywords = [ "http", "routing", "blocked" ]
aliases = [ "/questions/34569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cannot http to server but I can ping it (What else should I analyze?)](/questions/34569/cannot-http-to-server-but-i-can-ping-it-what-else-should-i-analyze)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a web server running nagios. When I web to it appears to be getting blocked or not routed from the wireshark output below.</p><p>I can ping it and the icmp traffic does appear in Wireshark and I get a proper reply. What can I look at to help me find what is not routing or is blocking it??</p><pre><code>52878  &gt;http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)
52878  &gt;http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)
52878  &gt;http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_perm=1)</code></pre></div><div id="question-tags" class="tags-container tags">http routing blocked</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '14, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/de64d1089e4cc4476ae8708fd90e5391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parakiteiz&#39;s gravatar image" /><p>parakiteiz<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parakiteiz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '14, 11:29</p></div></div><div id="comments-container-34569" class="comments-container"><span id="34574"></span><div id="comment-34574" class="comment"><div id="post-34574-score" class="comment-score"></div><div class="comment-text"><p>Were the three packets you included captured on the client, or the server? And is the Nagios server unix-based?</p></div><div id="comment-34574-info" class="comment-info"><span class="comment-age">(10 Jul '14, 12:08)</span> smp</div></div><span id="34578"></span><div id="comment-34578" class="comment"><div id="post-34578-score" class="comment-score"></div><div class="comment-text"><p>These 3 packets are captured from the client having the problem. Yes it is a Linux server but from my comments below I down even think it is making it that far.<br />
</p><p>Second look it appears the destination is All-HSRP-router_fd (00:00:0c:07:ac:fd). Which is a HSRP interface on my 3750 switch with the ip of <em>.</em>.253.1. It appears to not be routing on to the 1.0 subnet (vlan 255). When I do a sh ip route I see subnet 1.0 directly connected via vlan 255. So there should be no problems here?</p><p>Third Look: I just did a tracert to 1.89. Wireshark just loaded up on a bunch of Time- to exceeded to live exceeded (Time to live exceeded in transit). I also notice when I ping the address 1.89 I get a TTL of 63 when it is only 2 or 3 devices away. Looks like routing or switching issue.</p><p>What can I do to tie it down to a device?</p></div><div id="comment-34578-info" class="comment-info"><span class="comment-age">(10 Jul '14, 12:36)</span> parakiteiz</div></div><span id="34579"></span><div id="comment-34579" class="comment"><div id="post-34579-score" class="comment-score">1</div><div class="comment-text"><p>This type of L2/L3 problem is a bit out of my element, and I'm not sure this is the forum to get answers to that question. However I am forced to diagnose this type of issue all the time, and there's a simple way to confirm your theory that this is a L2/L3 problem. Simply perform network traces simultaneously on both the client and the server. You should see the SYN packet leave the client, and you should see it arrive on the server. If it doesn't arrive, then you know the problem is in the middle. If it arrives on the server, then there's something on the server (iptables?) filtering out the packet.</p><p>Good luck.</p></div><div id="comment-34579-info" class="comment-info"><span class="comment-age">(10 Jul '14, 12:40)</span> smp</div></div><span id="34581"></span><div id="comment-34581" class="comment"><div id="post-34581-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Looks like routing or switching issue.</p></blockquote><p>If you can ping the same host, but you can't connect to port 80, it's most certainly <strong>not</strong> a routing/switching problem, otherwise the ping would not work either!</p></div><div id="comment-34581-info" class="comment-info"><span class="comment-age">(10 Jul '14, 12:50)</span> Kurt Knochner ♦</div></div><span id="34670"></span><div id="comment-34670" class="comment"><div id="post-34670-score" class="comment-score"></div><div class="comment-text"><p>The two hosts that appear to be problematic 1.89 and 1.234. When I try to http or https to them it goes like this:</p><pre><code>66 62397 &gt; http [SYN} Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1 (Green0
66 [TCP Retransmission] 62397 &gt; http [SYN} Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
62 [TCP Retransmission] 62397 &gt; http [SYN} Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1</code></pre><p>It still appears have that type of traffic hanging on the HSRP mac address (Dst: All-HSRP-Routers_fd (Cisco MAC Adress for vlan and not routing past.</p><p>What else should I be looking for?</p></div><div id="comment-34670-info" class="comment-info"><span class="comment-age">(15 Jul '14, 10:41)</span> parakiteiz</div></div><span id="34672"></span><div id="comment-34672" class="comment not_top_scorer"><div id="post-34672-score" class="comment-score"></div><div class="comment-text"><p>A firewall!</p></div><div id="comment-34672-info" class="comment-info"><span class="comment-age">(15 Jul '14, 10:56)</span> Kurt Knochner ♦</div></div><span id="34680"></span><div id="comment-34680" class="comment not_top_scorer"><div id="post-34680-score" class="comment-score"></div><div class="comment-text"><p>I checked the logs on both firewalls; twice. These hosts did not appear in the logs. We have do have firewalls on our development LAN to separate subnets to emulate production environment.</p></div><div id="comment-34680-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:44)</span> parakiteiz</div></div><span id="34684"></span><div id="comment-34684" class="comment not_top_scorer"><div id="post-34684-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I checked the logs on both firewalls; twice.</p></blockquote><p>If there is a block rule <strong>without</strong> logging, you won't see anything in the logs.</p></div><div id="comment-34684-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:55)</span> Kurt Knochner ♦</div></div><span id="34736"></span><div id="comment-34736" class="comment not_top_scorer"><div id="post-34736-score" class="comment-score"></div><div class="comment-text"><p>I created a span port on the same switch and used the same ip address since I did not hear back from you. I Http'ed to 1.89 from the my workstation and this was the output [TCP Previous segment lost] http 51048 [SYN, ACK] Seq469244521 Win=14600 LEN=0 MSS=1460 [TCP Previous segment lost] http 51048 [SYN, ACK] Seq=140687248 Win=14600 LEN=0 MSS=1460</p><p>When you dig in to the SEQ/ACK analysis you get This is an ACK to the segment in frame:12040 When you dig in to the TCP Analysis Flags you get: [Expert Info (Warn/Sequence): Previous segmentlost (common at capture start)] [Message: Previous Segment lost (common at capture start)] [Severity Level: warn] [Group:Sequence]</p><p>So it looks like my SYN packets are making it there just the ACK packets are getting lost?</p><p>What should I look for next?</p></div><div id="comment-34736-info" class="comment-info"><span class="comment-age">(17 Jul '14, 14:38)</span> parakiteiz</div></div></div><div id="comment-tools-34569" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-34569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35962"></span>

<div id="answer-container-35962" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35962-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks all for you assistance. This appeared to be a self inflicted Routing Issue. On my switch04 I had give int vlan 255 a IP address of <em>.</em>.1.26 which made everything on that VLAN route VLAN 255 no the static route that existed. This appeared to be causing a routing loop.</p><p>I finally figured out my staring at my sh ip route output for like an hour. I then shut the int vlan 255 interface and saw it changed my sh ip route interface and fixed the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '14, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/de64d1089e4cc4476ae8708fd90e5391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parakiteiz&#39;s gravatar image" /><p>parakiteiz<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parakiteiz has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-35962" class="comments-container"></div><div id="comment-tools-35962" class="comment-tools"></div><div class="clear"></div><div id="comment-35962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

