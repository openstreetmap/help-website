+++
type = "question"
title = "Windows 7 ignores TCP MSS"
description = '''Is it possible that Windows 7 ignores TCP MSS? Even if another side announces MSS 256 bytes TCP/IP stack on Windows 7 sends TCP segments with payload &amp;gt; 256 bytes. Please find pcap files and a simple server program for testing this issue by following the link below: Wireshark logs. The issue can b...'''
date = "2012-03-15T23:16:00Z"
lastmod = "2012-03-17T01:26:00Z"
weight = 9573
keywords = [ "windows7", "mss", "tcp" ]
aliases = [ "/questions/9573" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Windows 7 ignores TCP MSS](/questions/9573/windows-7-ignores-tcp-mss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9573-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible that Windows 7 ignores TCP MSS? Even if another side announces MSS 256 bytes TCP/IP stack on Windows 7 sends TCP segments with payload &gt; 256 bytes. Please find pcap files and a simple server program for testing this issue by following the link below:</p><p><a href="http://dl.dropbox.com/u/3796696/tcp_mss_wireshark_logs.zip">Wireshark logs</a>.</p><p>The issue can be reproduced on Windows 7 PC only (32/64 bits), i.e. not on Windows XP/Linux machines. Chimney Offload State is disabled on my Windows 7 PC:</p><p>F:&gt;netsh interface tcp show global<br />
Querying active state...<br />
TCP Global Parameters<br />
Receive-Side Scaling State : enabled<br />
<strong>Chimney Offload State : disabled</strong><br />
NetDMA State : enabled<br />
Direct Cache Acess (DCA) : disabled<br />
Receive Window Auto-Tuning Level : normal<br />
Add-On Congestion Control Provider : none<br />
ECN Capability : disabled<br />
RFC 1323 Timestamps : disabled<br />
** The above autotuninglevel setting is the result of Windows Scaling heuristics<br />
overriding any local/policy configuration on at least one profile.<br />
</p><p>Thanks, Max.</p></div><div id="question-tags" class="tags-container tags">windows7 mss tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '12, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/ddb772138e2878f4d8c47ec438317ef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgalemin&#39;s gravatar image" /><p>mgalemin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgalemin has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '12, 19:45</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></br></p></div></div><div id="comments-container-9573" class="comments-container"></div><div id="comment-tools-9573" class="comment-tools"></div><div class="clear"></div><div id="comment-9573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="9594"></span>

<div id="answer-container-9594" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9594-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here's a link to an article called <a href="http://blogs.technet.com/b/nettracer/archive/2010/07/30/why-doesn-t-windows-2008-server-send-tcp-segments-smaller-than-536-bytes.aspx">Why Doesn't Windows Server 2008 negotiate TCP MSS smaller than 536 bytes?</a> Although it's about Windows Server 2008, I think it's the same thing you're encountering on Windows 7. The author's conclusion is that recent versions of Windows don't recognize MSS values smaller than 536 bytes because Microsoft has coded them to not accept an MTU value smaller than 576 bytes. Google did not turn up a lot of information about this, and some of it was confusing.</p><p>Your original question was "Is it possible that Windows 7 ignores TCP MSS?" The answer seems to be "Yes, for values less than 536." Whether it's a violation of the TCP RFCs or not, you have confirmed it using Wireshark. If your device has to interact with Windows 7 computers, you have to accommodate this behavior.</p><p>The embedded device you're working on may have a limited amount of RAM, but there is still a practical minimum. If you want your device to communicate with Windows systems, you will have to equip it with enough RAM to handle a 536-byte MSS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '12, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-9594" class="comments-container"><span id="9598"></span><div id="comment-9598" class="comment"><div id="post-9598-score" class="comment-score"></div><div class="comment-text"><p>Hi Jim,</p><p>Thanks a lot for your comment, it confirms and explains the original issue.</p><p>Basically in my case the main problem is not a limited amount of RAM but rather a maximum size of a data packet which can be transmitted over the air. Embedded device is a Radio Frequency modem and for some configurations maximum data packet length should be limited to a particular value to minimise RF channel occupation time. But it seems that I can't use MSS smaller than 536 bytes on Windows 7 PC. Thanks again!</p><p>Cheers, Max.</p></div><div id="comment-9598-info" class="comment-info"><span class="comment-age">(17 Mar '12, 00:21)</span> mgalemin</div></div></div><div id="comment-tools-9594" class="comment-tools"></div><div class="clear"></div><div id="comment-9594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9599"></span>

<div id="answer-container-9599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9599-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>(I converted your "answers" to "comments", please read the FAQ for details)</p><p>From RFC 791 (Internet Protocol):</p><p>"All hosts must be prepared to accept datagrams of up to 576 octets (whether they arrive whole or in fragments)."</p><p>So the MTU size of a link may be smaller, in which case fragmentation at the IP layer will occur if bigger IP datagrams are sent. The way to minimize the RF occupation is therefor to not only lower the MSS, but also lower the MTU on both sides of the RF link. This will make sure that each individual IP datagram that is sent over the link will have a maximum size.</p><p>Of course this would mean that Win7 packets that do not follow the low MSS will indeed be fragmented at the IP layer, just before being put on the RF link. And they will be re-assembled by the IP stack at the receiving end.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '12, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-9599" class="comments-container"><span id="9600"></span><div id="comment-9600" class="comment"><div id="post-9600-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you answer, SYN-bit. However, from my understanding the problem is not in IP layer (which is L3 in OSI model) but rather in TCP layer (L4). IP layer doesn't know anything about TCP MSS and it's a TCP layer responsibility to handle maximum size of data segment to be passed to the IP layer.</p><p>Changing default MTU with IP datagram fragmentation on gateway device is a reasonable workaround but unfortunately it's not an easy fix in our network configuration. In any case I'm very surprised that Windows Vista/2008/7 just silently ignores announced small MSS value.</p></div><div id="comment-9600-info" class="comment-info"><span class="comment-age">(17 Mar '12, 01:48)</span> mgalemin</div></div><span id="9602"></span><div id="comment-9602" class="comment"><div id="post-9602-score" class="comment-score"></div><div class="comment-text"><p>Yes and no. Since the TCP layer knows the IP layer MUST be able to send 576 byte datagrams, it can deduct that (without extra IP or TCP options) it must be able to send 536 byte segments to the IP layer.</p><p>Since you said it is the RF link occupation that is of concern, the packet size limitation is basically a L2 limitation, which should be enforced as close to L2 as possible. That's why I think you should fix it in the IP layer by reducing the MTU. That way, there will never be a packet bigger than what you set the limit too on the RF link.</p></div><div id="comment-9602-info" class="comment-info"><span class="comment-age">(17 Mar '12, 02:23)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9599" class="comment-tools"></div><div class="clear"></div><div id="comment-9599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9577"></span>

<div id="answer-container-9577" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9577-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think that Windows 7 probably ignores the MSS of 256 since IPv4 requires an MTU of at least 576 bytes, which would lead to a minimum MSS of 536. With IPv6 the minimum MTU is 1280, resulting in an even larger minimum MSS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '12, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-9577" class="comments-container"><span id="9590"></span><div id="comment-9590" class="comment"><div id="post-9590-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for your reply. Basically RFC 879 says:</p><ul><li>TCP provides an option that may be used at the time a connection is</li><li>established (only) to indicate the maximum size TCP segment that can</li><li>be accepted on that connection. This Maximum Segment Size (MSS)</li><li>announcement (often mistakenly called a negotiation) is sent from the</li><li>data receiver to the data sender and says "I can accept TCP segments</li><li>up to size X". The size (X) <strong>may be larger or smaller than the</strong></li><li><strong>default</strong>. The MSS can be used completely independently in each</li><li>direction of data flow. The result may be quite different maximum</li><li>sizes in the two directions.</li></ul><p>So for example if PC is connected to an embedded device with small amount of RAM device will anounce MSS with value smaller than the default one. This is basically my case as I have RF embedded controller with Lwip TCP/IP stack connected to the network through RF link.</p><p>The question is why TCP/IP stack on both Linux and Windows XP operating systems handles MSS but TCP/IP stack on Windows 7 ignores TCP MSS parameter? From my prospective it's a kind of violation of TCP standard.</p><p>Please find additional wireshark traces and a simple server program for testing this issue in the attachment. I captured wireshark logs on both server and client machines. Server always was Linux Ubuntu PC and client were Win 7, Win XP and Linux Ubuntu.</p><p>Test case:</p><ol><li>Run test server program with particular MSS parameter, for example:</li></ol><p>./tcpsrv --port=51234 --mss=128</p><ol><li><p>Establish raw TCP connection from putty;</p></li><li><p>Send 1200 bytes of data.</p></li></ol><p><a href="http://dl.dropbox.com/u/3796696/tcp_mss_wireshark_logs.zip">Wireshark logs</a>.</p></div><div id="comment-9590-info" class="comment-info"><span class="comment-age">(16 Mar '12, 18:24)</span> mgalemin</div></div></div><div id="comment-tools-9577" class="comment-tools"></div><div class="clear"></div><div id="comment-9577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

