+++
type = "question"
title = "MTU larger than interface allows with DF bit set"
description = '''I have a capture between two servers that have an MTU set to 1500 Bytes. Within the capture I have SQL TDS packets that are transferring data packets above 1500 Bytes with the DF bit set. Why are these packets traversing the network when I can&#x27;t ping above 1500 Bytes between the two servers? When I ...'''
date = "2015-11-11T21:15:00Z"
lastmod = "2015-11-12T00:24:00Z"
weight = 47529
keywords = [ "tds", "mtu", "sql" ]
aliases = [ "/questions/47529" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MTU larger than interface allows with DF bit set](/questions/47529/mtu-larger-than-interface-allows-with-df-bit-set)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47529-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture between two servers that have an MTU set to 1500 Bytes. Within the capture I have SQL TDS packets that are transferring data packets above 1500 Bytes with the DF bit set. Why are these packets traversing the network when I can't ping above 1500 Bytes between the two servers? When I try to ping with the DF bit set the packets are not even captured by Wireshark and the notification appears in the DOS prompt.</p><p>Any help is greatly appreciated.</p><p>Cheers.</p><pre><code>&gt;ping 10.2.8.120 -l 1400

Pinging 10.2.8.120 with 1400 bytes of data:

Reply from 10.2.8.120: bytes=1400 time&lt;1ms TTL=128

Reply from 10.2.8.120: bytes=1400 time&lt;1ms TTL=128

&gt;ping 10.2.8.120 -l 1600

Pinging 10.2.8.120 with 1600 bytes of data:

Reply from 10.2.8.120: bytes=1600 time&lt;1ms TTL=128

Reply from 10.2.8.120: bytes=1600 time&lt;1ms TTL=128

&gt;ping 10.2.8.120 -l 1600 -f

Pinging 10.2.8.120 with 1600 bytes of data:

Packet needs to be fragmented but DF set.

Packet needs to be fragmented but DF set.

No. Delta Time  Source  Destination Protocol  Length  TCP Length  Bytes in flight IP Identification Arrival Time  Info

546735  0.000176  3930.032301 10.2.8.206  10.2.8.120  TDS   1460  1460  0x473d (18237)  01:32.5 Response[Packet size limited during capture]

546736  0.000005  3930.032306 10.2.8.206  10.2.8.120  TDS 104,678 798 2258  0x473e (18238)  01:32.5 Unknown Packet Type: 13 (Not last buffer) (Not last buffer)

546737  0.00004 3930.032346 10.2.8.120  10.2.8.206  TCP   0   0x0e20 (3616) 01:32.5 49538 &gt; 1433 [ACK] Seq=1990537 Ack=2276450 Win=131328 Len=0

546738  0.001548  3930.033894 10.2.8.120  10.2.8.206  TDS 7992  8000  8000  0x0e21 (3617) 01:32.5 Remote Procedure Call (Not last buffer)

546739  0.000056  3930.03395  10.2.8.120  10.2.8.206  TDS   1112  9112  0x0e27 (3623) 01:32.5 Remote Procedure Call</code></pre></div><div id="question-tags" class="tags-container tags">tds mtu sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '15, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/a64d398f30a711d53c2705c7104314b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krazynedkelly&#39;s gravatar image" /><p>krazynedkelly<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krazynedkelly has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '15, 02:45</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-47529" class="comments-container"></div><div id="comment-tools-47529" class="comment-tools"></div><div class="clear"></div><div id="comment-47529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47533"></span>

<div id="answer-container-47533" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47533-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you have done a local trace. If have enabled "TCP Chimney Offload" or "Receive Segment Coalsecing" then the packets in the capture appaer larger. Because the capture point is inside the system. The NIC slices the segments to maximum allowed MTU.<br />
This could be done for transmitting frames by the function called "TCP Chimney Offloading" or "Large Send Offloading"<br />
And for the receiving frames it is called "Receive Segment Coalescing" or "Large Receive Offloading", but it is not as common in use as TCP Oflloading.<br />
</p><p>These are the names how they are used at Windows Systems. The global settings can be seen with this command <code>netsh int tcp show global</code> But maybe you need to alter the interface settings, too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '15, 00:49</p></div></div><div id="comments-container-47533" class="comments-container"></div><div id="comment-tools-47533" class="comment-tools"></div><div class="clear"></div><div id="comment-47533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

