+++
type = "question"
title = "A Question regarding weird Duplicate ICMP response"
description = '''Hi Guys, I tried to use winpcap to write a software running on PC (with 2 ethernet cards) to emulate a NAT. In that way, I could use a pesudo external IP address to access an internal IP. The architecture is as attached graph. However when I tried to ping the pesudo external IP address, I always get...'''
date = "2013-12-02T00:53:00Z"
lastmod = "2013-12-02T01:39:00Z"
weight = 27647
keywords = [ "redirect", "icmp" ]
aliases = [ "/questions/27647" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [A Question regarding weird Duplicate ICMP response](/questions/27647/a-question-regarding-weird-duplicate-icmp-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27647-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I tried to use winpcap to write a software running on PC (with 2 ethernet cards) to emulate a NAT. In that way, I could use a pesudo external IP address to access an internal IP. The architecture is as attached graph. However when I tried to ping the pesudo external IP address, I always get a lot of DUPLICATE ICMP response, does anyone knows why is that?</p><p>I do a ping from 146.208.243.51 -&gt; 146.208.233.8, on the NAT server, the IP address and MAC address is converted to internal LAN's IP address/MAC address; and when the PC2 reply the ping, the NAT server will convert those IP/MAC address back to external IP/MAC address. However, when the ping response packet send back to the external network, I got following output. I've also tried if the PC3 stay in the same subnet as the NAT server, it seems everything work ok. But if the IP packet goes to Router/Gateway, this strange behavior is observed.<img src="https://osqa-ask.wireshark.org/upfiles/1_1.JPG" alt="alt text" /></p><pre><code>64 bytes from 146.208.233.8: icmp_seq=1 ttl=62 time=4.09 ms
64 bytes from 146.208.233.8: icmp_seq=1 ttl=61 time=4.39 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=60 time=4.60 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=59 time=4.69 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=58 time=4.73 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=57 time=4.82 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=56 time=4.85 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=55 time=4.94 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=54 time=5.08 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=53 time=5.27 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=52 time=5.45 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=51 time=5.65 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=50 time=5.82 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=49 time=5.95 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=48 time=6.03 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=47 time=6.12 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=46 time=6.20 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=45 time=6.28 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=44 time=6.38 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=43 time=6.45 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=42 time=6.52 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=41 time=6.56 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=40 time=6.65 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=39 time=6.69 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=38 time=6.78 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=37 time=6.81 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=36 time=6.90 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=35 time=6.94 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=34 time=7.02 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=33 time=7.06 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=32 time=7.15 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=31 time=7.19 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=30 time=7.27 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=29 time=7.31 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=28 time=7.40 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=27 time=7.44 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=26 time=7.52 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=25 time=7.56 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=24 time=7.65 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=23 time=7.68 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=22 time=7.77 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=21 time=7.80 ms (DUP!)
64 bytes from 146.208.233.8: icmp_seq=1 ttl=20 time=7.89 ms (DUP!)</code></pre><p>Does anybody knows why?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">redirect icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/bbf88acd96e1a1f909172c86bd1cce6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jianhui&#39;s gravatar image" /><p>Jianhui<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jianhui has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 01:28</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27647" class="comments-container"></div><div id="comment-tools-27647" class="comment-tools"></div><div class="clear"></div><div id="comment-27647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27651"></span>

<div id="answer-container-27651" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27651-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>as you can see, the TTL is 'counting' down. That's usually a sign for a routing loop. However, as you wrote the NAT code yourself, it could also be a bug in your code.</p><p>It's hard to diagnose without a capture file, taken at the right place(s). Can you post one at Google drive, dropbox, cloudshark.org, or mega.co.nz?</p><p>You should take a capture between PC2 -&gt; PC(NAT) and between PC(NAT) -&gt; GW1 at the same time.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 03:30</p></div></div><div id="comments-container-27651" class="comments-container"><span id="27684"></span><div id="comment-27684" class="comment"><div id="post-27684-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your quick response. I capture a log from the NAT server to capture wireshark log on both ethernet interface.The log is put on <a href="https://dl.dropboxusercontent.com/u/80123665/icmp.pcapng">https://dl.dropboxusercontent.com/u/80123665/icmp.pcapng</a> . You could use icmp filter to see ping request/response.</p><p>For example, You could see:</p><p>msg No. 257, ping request sent from 146.208.243.51 -&gt; 146.208.233.8</p><p>msg No. 299, the ping request has been converted into internal LAN, IP/MAC address has been converted to 10.168.0.100 -&gt; 10.168.0.2</p><p>msg No. 302, the ping response sent back from 10.168.0.2 -&gt; 10.168.0.100</p><p>msg No. 262, the ping response has been converted back into external LAN, IP/MAC address has been converted to 146.208.233.8 -&gt; 146.208.243.51</p><p>After that, I got 2 redirect message (msg 275,277) from 146.208.234.171 and 146.208.235.84, does that mean the router are suggesting other gateway? And I got a ICMP time-tolive exceeded packet in message No.313.</p><p>In this case, for internal LAN, I use the internal ethernet LAN MAC ID for both 10.168.0.1 and 10.168.0.100; for external LAN, I use the external LAN MAC ID for both 146.208.235.150 and 146.208.233.8 IP address. Is this an issue for the router?</p><p>Thanks a lot, Jianhui</p></div><div id="comment-27684-info" class="comment-info"><span class="comment-age">(02 Dec '13, 20:15)</span> Jianhui</div></div><span id="27685"></span><div id="comment-27685" class="comment"><div id="post-27685-score" class="comment-score"></div><div class="comment-text"><p>A clarification of the system diagram is the PC3 is actually a Linux server instead of a PC running Microsoft Windows 7.</p></div><div id="comment-27685-info" class="comment-info"><span class="comment-age">(02 Dec '13, 20:22)</span> Jianhui</div></div><span id="27692"></span><div id="comment-27692" class="comment"><div id="post-27692-score" class="comment-score">1</div><div class="comment-text"><p>In Frame #257 the ICMP request is coming from a Cisco MAC address (I guess GW1). Then in Frame #262, the ICMP response is going to the MAC of a Dell system (Dell_d9:a5:d0 (00:1c:23:d9:a5:d0)). Then you get two ICMP redirects (Frame #275,277) from systems that are not included in your picture (IP: 146.208.234.171 and 146.208.235.84) and both have a <strong>different MAC</strong> address than the Dell address !??!</p><p><strong>Spoiler</strong>: I guess, there is something terribly wrong with your network setup and most certainly there is a routing problem, as I suspect a routing loop somewhere ;-)</p><p>Please post the output of the following commands on <strong>both</strong> systems: PC(NAT) and GW1</p><blockquote><p>netstat -nr<br />
ipconfig -a<br />
tracert -d 146.208.243.51<br />
</p></blockquote><p>and the equivalent output on your Cisco device (GW1?).</p><p>Please identify the systems that sent the ICMP redirects ( 146.208.234.171 and 146.208.235.84) and check how they are involved.</p><p>Next thing: The ICMP request/reply is first shown completely on the external side of PC(NAT): Frames: #257,#262 and <strong>only after that</strong> on the internal side: #299,#302. That's not how NAT works.</p><p>On a a NAT device, I would have expected the following packet sequence:</p><ul><li>External: ICMP request</li><li>Internal: ICMP request (address translated to internal)</li><li>Internal: ICMP reply</li><li>External: ICMP reply (address translated to external)</li></ul><p>Did you configure the NAT IP address (146.208.233.8) on PC(NAT) as a secondary address?</p><p>To me it looks like you did that and the IP stack of the 'NAT' system answers the external ICMP requests (see ICMP packet sequence in the capture file). Then your WinPcap 'NAT code' takes the request and sends it to the internal side, which is then answered by the internal PC.</p><p>If that is true: That's not a good idea.</p><p>My suggestion:</p><ol><li>Fix your network setup: Check routing, etc.</li><li>Think about how NAT should work</li><li>Fix your IP configuration on PC(NAT)</li><li>Maybe also required: Fix your WinPcap NAT code</li><li>Repeat tests</li></ol></div><div id="comment-27692-info" class="comment-info"><span class="comment-age">(03 Dec '13, 02:42)</span> Kurt Knochner ♦</div></div><span id="27738"></span><div id="comment-27738" class="comment"><div id="post-27738-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your detailed response. I think I understand the issue right now.</p><p>I overlook the MAC address of the incoming ping request from external LAN, that MAC address (GW1's MAC address) is the MAC address that I should used for the ping response. However when I write NAT code, I convert that ping response Packet's Dest MAC address to the final destination's MAC address (PC3's MAC address instead of GW1's MAC address). It means I sent back a packet with a MAC address that cannot reached in the sub-net. That cause problem to the router while result in the Duplicate ping response.(But I'm not sure how the loopback route is created by the router, maybe you could shed some light on that ;-) )</p><p>As for the NAT problem you point out, I think that is caused by wireshark' logging algorithm. It puzzled me too when I see the log the first time. Then I found if you reorder the logging packets by time (instead of by sequence number) you would see the expected packet sequence:</p><p>External: ICMP request</p><p>Internal: ICMP request (address translated to internal)</p><p>Internal: ICMP reply</p><p>External: ICMP reply (address translated to external)</p><p>Thanks again for your great help on this, It is really very helpful! Jianhui</p></div><div id="comment-27738-info" class="comment-info"><span class="comment-age">(03 Dec '13, 17:47)</span> Jianhui</div></div><span id="27750"></span><div id="comment-27750" class="comment"><div id="post-27750-score" class="comment-score"></div><div class="comment-text"><blockquote><p>It means I sent back a packet with a MAC address that cannot reached in the sub-net.</p></blockquote><p>Yes, and therefore no other system should 'feel' itself responsible for that packet. Why you get the ICMP redirects is unclear to me and I cannot give you any good explanation, as I don't know the rest of your infrastructure. I leave it up to you to figure out what's going on ;-)</p><blockquote><p>Then I found if you reorder the logging packets by time (instead of by sequence number) you would see the expected packet sequence:</p></blockquote><p>you are right. I did not check that. That's probably related to the way WinPcap (or dumpcap) buffers frames internally before they get flushed out to a capture file, especially if you capture on two interfaces at the same time</p><p><strong>Note to myself:</strong> Don't assume <strong>anything</strong> ;-))</p><blockquote><p>Thanks again for your great help on this, It is really very helpful! Jianhui</p></blockquote><p>You're welcome, especially as these kinds of problem are rather interesting to diagnose :-)</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-27750-info" class="comment-info"><span class="comment-age">(04 Dec '13, 02:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27651" class="comment-tools"></div><div class="clear"></div><div id="comment-27651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

