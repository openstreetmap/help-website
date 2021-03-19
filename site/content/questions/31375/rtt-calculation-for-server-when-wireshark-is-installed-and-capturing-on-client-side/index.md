+++
type = "question"
title = "Rtt calculation for server? when Wireshark is installed and capturing on client side?"
description = '''Hi. a. Since Wireshark is installed on client-side, i can fully appreciate RTT calculation for client (start of SYN sent out to receival of corresponding SYN-ACK). But how does Wshark calculate RTT for server (start of SYN sent out from server to receival of corresponding SYN-ACK at server-end) when...'''
date = "2014-04-02T02:21:00Z"
lastmod = "2014-04-02T02:49:00Z"
weight = 31375
keywords = [ "rtt", "rtt_ack", "time", "round", "trip" ]
aliases = [ "/questions/31375" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rtt calculation for server? when Wireshark is installed and capturing on client side?](/questions/31375/rtt-calculation-for-server-when-wireshark-is-installed-and-capturing-on-client-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31375-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>a. Since <strong>Wireshark is installed on client-side</strong>, i can fully appreciate RTT calculation for client (start of SYN sent out to receival of corresponding SYN-ACK).</p><p>But how does Wshark calculate RTT for server (start of SYN sent out from server to receival of corresponding SYN-ACK at server-end) when no wireshark is installed at server-end to record the sent and receival times of relevant pkts? Does this calculation rely on TCP header timestamps calculated at client side(installed with wireshark) after the pkts are received at server?</p><p>b. <strong>[Source=Client] [Destination=Server] [RTT_ACK =0.2111]</strong></p><p>Does the above refer to (RTT=0.2111) for SYN sent out by server and ACK received by server?</p><p>This RTT ACK value increases during my capture. Is it normal? What could lead to increase in RTT ACK? High CPU and/or memory utilization?</p><p>c. Btw, i saw someone posted the following response in another thread</p><p><em>RTT for TCP sessions, which can be done by finding the <strong>initial SYN</strong>, and then (after setting a time reference on it) looking at the relative time of the <strong>ACK (third packet</strong> in the TCP three way handshake).</em></p><p>=&gt; i thought the RTT should be time between start of <strong>SYN</strong> sent out to receival of corresponding <strong>SYN-ACK?</strong>, and no relation to the 3rd packet?</p><p>Seek your kind guidance : )</p></div><div id="question-tags" class="tags-container tags">rtt rtt_ack time round trip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/66ff60caa109e46ba0cc25637cbbddaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walnut23&#39;s gravatar image" /><p>walnut23<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walnut23 has no accepted answers">0%</span></p></div></div><div id="comments-container-31375" class="comments-container"></div><div id="comment-tools-31375" class="comment-tools"></div><div class="clear"></div><div id="comment-31375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31376"></span>

<div id="answer-container-31376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31376-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>a. The RTT should be the same for client and server, since it is the same distance. There are exceptions of course, e.g. when asynchronous routing is in place, but if both systems use the same path the RTT is basically the same.</p><p>b. Wireshark tells you in the SEQ/ACK analysis "this is an ACK to the segment in frame x". If you select that frame and use the popup menu to set a time reference on it, you can use the time display format "seconds since beginning of the capture" to see that the ACK has exactly that time. So if you're looking at the SYN-ACK it is the time it took to receive it as an reaction to the SYN. If you're capturing on the client, this is the "initial RTT" (if, and only if, captured on the client! Otherwise look at the ACK in the third packet).</p><p>And yes, RTT changes over time. Sometimes it goes up, sometimes it goes slightly down, but it is usually not faster than the initial RTT. Reason is, that small packets have better chances of passing through routers and other devices quickly, while big packets are sometimes queued in a buffer until there is room for them. Depending on the load on the devices in the path from client to server the RTT can fluctuate.</p><p>c. If you only look at SYN to SYN-ACK you <strong>need</strong> to have captured on the client, otherwise there is parts of the path missing. When looking at SYN, SYN-ACK, ACK all parts of the path are included, so this will tell you the RTT no matter where you capture. If you take a look at your capture you'll notice that the ACK from the client is so fast that it doesn't really have a significantly higher RTT value than when looking at the SYN-ACK. So if your capture device is in the middle between client and server you can still tell RTT from looking at how long the handshake took, from SYN to ACK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Apr '14, 02:50</p></div></div><div id="comments-container-31376" class="comments-container"><span id="31448"></span><div id="comment-31448" class="comment"><div id="post-31448-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your prompt response.</p><p>a. If the following statement is true</p><p><em>both systems use the same path the RTT is basically the same,</em></p><p>Assuming Synchronous Routing,</p><ul><li><p>Then why is the capture showing significantly higher values of RTT ACK in the direction from client to server?</p></li><li><p>At some points of my capture, I am seeing &gt;200ms of RTT ACK from client-to-server compared to &lt;50ms from server-to-client?</p></li><li><p>How does wireshark installed in Client detect time of packets rcv at server-end?</p></li></ul><p>b. I apologise for the typo for 2nd question [Source=<strong>Client</strong>] [Destination=Server] [RTT_ACK =0.2111]</p><ul><li>May I confirm again that the above refer to (RTT=0.2111) for SYN sent out <strong>by</strong> <strong>CLIENT</strong> and ACK received by server?</li></ul></div><div id="comment-31448-info" class="comment-info"><span class="comment-age">(02 Apr '14, 18:36)</span> walnut23</div></div><span id="31456"></span><div id="comment-31456" class="comment"><div id="post-31456-score" class="comment-score"></div><div class="comment-text"><p>You need to keep in mind that Wireshark can only calculate timings based on the location the packets were captured.</p><p>E.g. if you capture at the client, the packets have timestamps of them arriving and leaving the client. This means that anything coming from the server will have a very short ACK time because you do not have network distance delay. For packets coming in from the server the timing will be significantly higher because RTT of the path is added as network distance delay.</p><p>To investigate this kind of thing you might want to take two captures, one at the client and one at the server. If you compare RTT ACKs in each of the captures you'll see that the timing is always fast for packets that are sent to the other system, and slow for those coming in.</p><p>So to answer the 3rd question: Wireshark can't detect time of the packets received at the server end. It can only do that if you capture at the server, too. But then the trace will not have the timings on the client end, of course.</p><p>Regarding b., without a capture and specific packet numbers it is not exactly clear what timings you're looking at, but RTT_ACK is just the time that it took to acknowledge a packet. So in case of a SYN going out and a SYN-ACK coming in, the RTT-ACK in the SYN-ACK is the time that it took to acknowledge the SYN, including all delays. Depending on the capture location, this value may be higher or lower - higher at the client, lower at the server.</p></div><div id="comment-31456-info" class="comment-info"><span class="comment-age">(03 Apr '14, 00:53)</span> Jasper ♦♦</div></div></div><div id="comment-tools-31376" class="comment-tools"></div><div class="clear"></div><div id="comment-31376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

