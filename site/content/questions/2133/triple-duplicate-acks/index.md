+++
type = "question"
title = "Triple Duplicate ACKs"
description = '''I think this is a good one. I&#x27;ll try to reserve my diagnosis until the end. We have two endpoints (both linux) that are 25ms apart (50ms RTT). They are transferring files via an SSH tunnel - actually they are tar-ing to a pipe (|) which directs to an SSH session that executes another tar command on ...'''
date = "2011-02-03T10:44:00Z"
lastmod = "2011-02-18T01:14:00Z"
weight = 2133
keywords = [ "throughput", "ssh", "tcp" ]
aliases = [ "/questions/2133" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Triple Duplicate ACKs](/questions/2133/triple-duplicate-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2133-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I think this is a good one. I'll try to reserve my diagnosis until the end.</p><p>We have two endpoints (both linux) that are 25ms apart (50ms RTT). They are transferring files via an SSH tunnel - actually they are tar-ing to a pipe (|) which directs to an SSH session that executes another tar command on the other side - suboptimal IMHO, but they're unix "gurus", what're you going to do. Anyway... The customer is complaining about the throughput. The endpoints negotiate a window scale of 4 (256k window). The sites are connected via OC192 at &lt;10% utilization - bandwidth ain't an issue. It looks like they go through the normal TCP slow start until they hit about 40Mbps, then we see a big drop in throughput and slow-start kicks in again. The window doesn't drop - well, it goes from 261k to ~255k at various points in the transfer, but those slight drops in window size don't really align with the drops in throughput. We're capturing with a probe/SPAN on one side, and a capture agent on the other. We don't see any packets dropped - what is sent is being received. NOW, what we DO see are trip-dup-ACKs, which I assume are triggering the remote stack's drop in it's congestion window. One of my fellow monkeys traced back up 20 packets or so and found a single (1) out-of-order packet. And this is where we are.</p><p>OPINION: Because of the amount of data flowing I think that one OOO packet is causing the buffers to get blown out of the water. The server AS on both sides is supported by a highly redundant network, it's possible that the OOO packet is the result of one leg in the redundant path having a temporarily slightly higher latency. It seems odd that a smoothly flowing 256k window would suddenly fill up so quickly. This may point to an I/O issue on the receiving server - but if that was the case I would expect to see much more severe drops in TCP Window size. I have NOT verified whether or not the switch is seeing output queue drops on the server interfaces - it's possible that there's a drop going on at the interface level that the probe isn't seeing. Aren't trip-dup-ACKs special though? Is that the receivers way of telling the sender to start SlowStart? It seems that pushing a TCP Zero-Window would have the same effect - but the recovery from a 0 window includes up to a 3 second period of non-communication. Is the trip-dup-ack the big RED slowdown button?</p></div><div id="question-tags" class="tags-container tags">throughput ssh tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '11, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2133" class="comments-container"></div><div id="comment-tools-2133" class="comment-tools"></div><div class="clear"></div><div id="comment-2133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2412"></span>

<div id="answer-container-2412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2412-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Trip-DUP-Ack is meant to trigger TCP Fast Retransmission and by that fast recovery instead of the classical slow start... well not completely instead, but the rate that CWND increases should be rapidly higher compared to slow start. That is also dependend on which OS the sender is using -&gt; RFC states Fast Retransmsission to trigger on the third duplicate ACK (4th ACK /w same ACK number), while Microsoft speeds up the process and does not keep to the RFC by triggering after the 2nd duplicate ACK (3rd total ACK /w same number)</p><p>Your case kind of reminds me of my question to TCP sender behaviour earlier here, remember ? :)</p><p>do you have Speed downlinks between those two stations from Gig to 100M ?</p><p>Also you might want to take a close look at the timings, because I had several cases, where wireshark was talking 'bout OOO but those were in fact fast retransmits and vice versa, but you know that - just commenting for others reading this question</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '11, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-2412" class="comments-container"><span id="2479"></span><div id="comment-2479" class="comment"><div id="post-2479-score" class="comment-score"></div><div class="comment-text"><p>The endpoints are Gig, switch uplinks are 10G, and the interconnects between the sites as OC192s.</p><p>I'm read and reread Comer's opinion on the trip-dup-ack, and I get lost in the RFC about fast retrans. Why isn't there a "Simple" button for this stuff? Thanks for putting the sequence of events more plainly.</p></div><div id="comment-2479-info" class="comment-info"><span class="comment-age">(22 Feb '11, 06:40)</span> GeonJay</div></div></div><div id="comment-tools-2412" class="comment-tools"></div><div class="clear"></div><div id="comment-2412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2136"></span>

<div id="answer-container-2136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2136-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Interesting one, could it be that the Duplicate ACK's have SACK options? telling the sender about the missing packet for each received packet until the OOO packet arrives?</p><p>Could you post the relevant part of the trace somewhere?</p><p>Or the output of the following:</p><pre><code>tshark -r &lt;file&gt; -T fields -e frame.number -e frame.time_relative \
  -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.ack -e tcp.len \
  -e tcp.options.sack_le -e tcp.options.sack_re \
  -e tcp.options.timestamp.tsval -e tcp.options.timestamp.tsecr</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '11, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2136" class="comments-container"><span id="2348"></span><div id="comment-2348" class="comment"><div id="post-2348-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the delay, I've been MIA. I'll working on scrubbing the captures and getting them posted. After digging through IBM's KB we found an article loosely related to this issue. Low-and-behold a simple reboot seems to make the problem disappear for a few days. The SysAd's are STILL asking us to figure out how the network performance is improved by a server reboot. Silly admins.</p></div><div id="comment-2348-info" class="comment-info"><span class="comment-age">(15 Feb '11, 08:14)</span> GeonJay</div></div></div><div id="comment-tools-2136" class="comment-tools"></div><div class="clear"></div><div id="comment-2136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

