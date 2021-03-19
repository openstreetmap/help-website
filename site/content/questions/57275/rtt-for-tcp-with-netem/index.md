+++
type = "question"
title = "RTT for TCP with netem"
description = '''I have the following simple network topology:  Two Laptops using Linux Ubuntu 14.04 and 16.04 with Kernel Version 4.4.0 They are directly connected using 1Gbps Ethernet interface. PC1: 10.0.0.1/24 &amp;amp; PC2: 10.0.0.2/24 PC2 runs netem to add artificial delay of 100ms Both laptops run iperf v2.0.9 PC...'''
date = "2016-11-10T12:45:00Z"
lastmod = "2016-11-10T13:36:00Z"
weight = 57275
keywords = [ "iperf", "capture", "tcp", "rtt" ]
aliases = [ "/questions/57275" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTT for TCP with netem](/questions/57275/rtt-for-tcp-with-netem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57275-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following simple network topology:</p><ol><li>Two Laptops using Linux Ubuntu 14.04 and 16.04 with Kernel Version 4.4.0</li><li>They are directly connected using 1Gbps Ethernet interface.</li><li>PC1: 10.0.0.1/24 &amp; PC2: 10.0.0.2/24</li><li>PC2 runs netem to add artificial delay of 100ms</li><li>Both laptops run iperf v2.0.9</li><li>PC1 runs as a server and PC2 as a client</li></ol><p>When I start the TCP connection on PC2, iperf reports the correct RTT which is around 100ms, however when I capture the traffic using wireshark again on PC2 and try to analyze the RTT. The RTT given by Wireshark is very small compared to what it should be. My question what is the cause of this behavior?</p></div><div id="question-tags" class="tags-container tags">iperf capture tcp rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '16, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/566cfe38b17a31f0dc825c86538cf3d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hany%20Assasa&#39;s gravatar image" /><p>Hany Assasa<br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hany Assasa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '16, 13:15</p></div></div><div id="comments-container-57275" class="comments-container"><span id="57276"></span><div id="comment-57276" class="comment"><div id="post-57276-score" class="comment-score"></div><div class="comment-text"><p>Which PC is running Wireshark? Which side reports this RTT? Both, or just the client? Can you post a short piece of trace in a public location? Since it is iperf traffic, there should not be any confidentiality issues.</p></div><div id="comment-57276-info" class="comment-info"><span class="comment-age">(10 Nov '16, 13:13)</span> Bob Jones</div></div><span id="57278"></span><div id="comment-57278" class="comment"><div id="post-57278-score" class="comment-score"></div><div class="comment-text"><p>@Bob Jones, I added more description. Tomorrow I will upload the capture files.</p></div><div id="comment-57278-info" class="comment-info"><span class="comment-age">(10 Nov '16, 13:16)</span> Hany Assasa</div></div></div><div id="comment-tools-57275" class="comment-tools"></div><div class="clear"></div><div id="comment-57275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57279"></span>

<div id="answer-container-57279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57279-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When the client runs at the same PC like netem (PC2), Wireshark shows the actual RTT (the delay from the SYN packet sent by the client to the SYN,ACK sent by the server) as seen on the wire because the client's SYN packet is delayed before reaching the wire and the server's SYN,ACK packet is delayed on the way from the wire to the IP stack, and netem is further from the wire than libpcap.</p><p>If you swap the roles and run the client at PC1 and server at PC2, the values shown by iperf and Wireshark should match.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '16, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57279" class="comments-container"><span id="57293"></span><div id="comment-57293" class="comment"><div id="post-57293-score" class="comment-score"></div><div class="comment-text"><p>It's probably another example of why capturing on one of the two systems involved is not a good idea. A third, independent capture PC between sender and receiver should show what really happens.</p></div><div id="comment-57293-info" class="comment-info"><span class="comment-age">(11 Nov '16, 01:00)</span> Jasper ♦♦</div></div><span id="57299"></span><div id="comment-57299" class="comment"><div id="post-57299-score" class="comment-score"></div><div class="comment-text"><p>@Jasper, I disagree, for this particular case it is irrelevant whether you capture "in the middle of the wire" or at one end of it.</p><p>The problem here is that the delay is inserted between the wire and the client application, and the RTT is evaluated as "SYN+ACK.timestamp - SYN.timestamp". So the "software delay" between the wire and the application has to be inserted at the server end.</p></div><div id="comment-57299-info" class="comment-info"><span class="comment-age">(11 Nov '16, 02:24)</span> sindy</div></div><span id="57301"></span><div id="comment-57301" class="comment"><div id="post-57301-score" class="comment-score"></div><div class="comment-text"><p>@sindy okay, maybe I'm overthinking this. I always evaluate RTT via SYN - SYN/ACK - ACK.</p></div><div id="comment-57301-info" class="comment-info"><span class="comment-age">(11 Nov '16, 03:20)</span> Jasper ♦♦</div></div><span id="57307"></span><div id="comment-57307" class="comment"><div id="post-57307-score" class="comment-score"></div><div class="comment-text"><p>Why?</p><pre><code> client                server
    |--------            | \
    |        SYN         |  &gt; forward delay
    |           --------&gt;| /
    |                    |
    |             -------| \
    |      SYN/ACK       |  &gt; return delay
    |&lt;-----              | /
    |                    |
    |--------            | \
    |        ACK         |  &gt; forward delay
    |           --------&gt;| /</code></pre><p>So to me, both (SYN to SYN/ACK delay) and (SYN/ACK to ACK) delay contain the complete round trip, i.e. one pass through the client-&gt;server path and one pass through the server-&gt;client path (and should thus be almost the same). So maybe you calculate the RTT as an average of the two?</p><p>The problem here that the delay is not in the network but between the NIC and the application (iperf in this case) at one of the ends. So yes, I should probably extend my answer as "if you look at the SYN to SYN/ACK distance in the capture, the netem must run at server side; if you measure the SYN/ACK to ACK value, the netem must run at client side".</p><pre><code>           silicon               copper
 client                netem                server
    |--------SYN--------&gt;|                    |
    :                    :                    :
    |                    |                    |
    |                    |--------SYN--------&gt;|
    |                    |&lt;-----SYN/ACK-------|
    :                    :                    :
    |&lt;-----SYN/ACK-------|                    |
    |--------ACK--------&gt;|                    |
    :                    :                    :
    |                    |--------ACK--------&gt;|</code></pre></div><div id="comment-57307-info" class="comment-info"><span class="comment-age">(11 Nov '16, 03:55)</span> sindy</div></div><span id="57309"></span><div id="comment-57309" class="comment"><div id="post-57309-score" class="comment-score"></div><div class="comment-text"><p>@sindy I need to be able to determine RTT via the handshake no matter where the capture device is placed, because for best capture quality I cannot capture on either client or server as the results are always biased. SYN to SYN/ACK and SYN/ACK to ACK are not good enough unless you're on or very close to client or server. How I do this I documented here:</p><p><a href="https://blog.packet-foo.com/2014/07/determining-tcp-initial-round-trip-time/">https://blog.packet-foo.com/2014/07/determining-tcp-initial-round-trip-time/</a></p></div><div id="comment-57309-info" class="comment-info"><span class="comment-age">(11 Nov '16, 04:10)</span> Jasper ♦♦</div></div><span id="57311"></span><div id="comment-57311" class="comment not_top_scorer"><div id="post-57311-score" class="comment-score"></div><div class="comment-text"><p>OK, @Jasper, your article covers the generic case (very nicely as always).</p><p>I was trying to share the perspective of the OP who captures either at client or at server machine, except that the path causing the delay is not between the two machines as usually but inside one of the machines. Also, the iperf always measures the RTT from the point of view of either the server or the client, not from the middle of the path.</p></div><div id="comment-57311-info" class="comment-info"><span class="comment-age">(11 Nov '16, 04:24)</span> sindy</div></div><span id="57312"></span><div id="comment-57312" class="comment not_top_scorer"><div id="post-57312-score" class="comment-score"></div><div class="comment-text"><p>Thanks @sindy, and you're right, this question is more about a different aspect of RTT.</p></div><div id="comment-57312-info" class="comment-info"><span class="comment-age">(11 Nov '16, 04:30)</span> Jasper ♦♦</div></div></div><div id="comment-tools-57279" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-57279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

