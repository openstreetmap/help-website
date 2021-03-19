+++
type = "question"
title = "Strange ICMP packets..."
description = '''A colleague of mine has sent me this strange PCAP file. He has taken a PCAP file on a core switch and capture the ping packets from my PC to a remote device. The first ICMP echo msg gets an echo reply. But then a third echo request is sent (without any reply found in the trace). Take a look at the n...'''
date = "2016-10-14T07:57:00Z"
lastmod = "2016-10-14T10:06:00Z"
weight = 56370
keywords = [ "icmp", "strange" ]
aliases = [ "/questions/56370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange ICMP packets...](/questions/56370/strange-icmp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A colleague of mine has sent me this strange PCAP file. He has taken a PCAP file on a core switch and capture the ping packets from my PC to a remote device. The first ICMP echo msg gets an echo reply. But then a third echo request is sent (without any reply found in the trace). Take a look at the negative timing of this packet... This schema does repeat indefinitely.</p><p>Any idea about the potential cause of this strange behaviour ?<img src="https://osqa-ask.wireshark.org/upfiles/2016-10-14_16-54-27.gif" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">icmp strange</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p>thierryn<br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span></p></img></div></div><div id="comments-container-56370" class="comments-container"></div><div id="comment-tools-56370" class="comment-tools"></div><div class="clear"></div><div id="comment-56370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56373"></span>

<div id="answer-container-56373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56373-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suspect packet three is a duplicate of packet 1. Notice the TTL: packet 1 is decremented (127 instead of 128). What is the span or mirror port setup? I would suspect two source ports into a single destination.</p><p>I can replicate something very close, except for the specific timing. With a poorly(*) configured port mirror or span setup on my switch/router, I can end up with the same as you have:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/icmp.png" alt="alt text" /></p><p>The ttl change is telling in that you crossed a router so it is not likely a layer2 loop or anything like that; the specific configuration for this is to configure a router with mirror port capability and then:</p><ol><li>Copy ingress of incoming ICMP request from the source, so in my case port connected to 192.168.1.14 (/24). So we see an ICMP request with full TTL. We would not see any response because we limited to ingress. Frame 4.</li><li>Copy BOTH ingress and egress of ICMP response, so port connected to 192.168.3.178. We will see the ICMP request as it leaves the router so ttl is decremented, and then the response with full ttl as we see it before routing. We see both because we have ingress and egress set. Frames 5 and 6.</li><li>Destination mirror for this test was the same port for both of these links</li></ol><p>There are probably other ways to get this. The timing is dependent on a lot of things. I have seen Cisco span ports mirror packets out of order (obvious to see when it happens with TCP). This diagnostic feature is usually lower priority than other device functions, so you never really know how that will affect the timing. What happens when we mirror two 1GB ports into a single 1GB destination? Not good things...</p><p>Also the negative timestamp is common for me when I capture on two separate interfaces at the same time. Instead of setting the mirror destination to the same port as in point 3 above, use separate destinations but capture on the same PC, with two NICs. Make one of the them a USB NIC and heavily load the system. Timing could be a mess.</p><p>*My assertion that this is poor is true for me - I have no need to configure my span ports in this manner for my daily work. However, it may be perfectly valid for whatever it is you are trying to do. For understanding ICMP echo flows across a router this is probably not the best choice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '16, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 15 Oct '16, 03:28</p></div></div><div id="comments-container-56373" class="comments-container"><span id="56400"></span><div id="comment-56400" class="comment"><div id="post-56400-score" class="comment-score"></div><div class="comment-text"><p>What can explain a TTL=127 for a duplicate packets ?</p></div><div id="comment-56400-info" class="comment-info"><span class="comment-age">(14 Oct '16, 23:15)</span> thierryn</div></div><span id="56401"></span><div id="comment-56401" class="comment"><div id="post-56401-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-56401-info" class="comment-info"><span class="comment-age">(15 Oct '16, 00:19)</span> Jaap ♦</div></div><span id="56490"></span><div id="comment-56490" class="comment"><div id="post-56490-score" class="comment-score"></div><div class="comment-text"><p>I would assume, somehow a router is influencing it's TTL. Awkward indeed.</p></div><div id="comment-56490-info" class="comment-info"><span class="comment-age">(18 Oct '16, 02:38)</span> SynAck</div></div><span id="56491"></span><div id="comment-56491" class="comment"><div id="post-56491-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What can explain a TTL=127 for a duplicate packets ?</p></blockquote><p>As @Bob Jones has already explained - the same "logical packet" is captured twice, before and after passing through a router.</p><ul><li><p>each pass through a router decrements packet's TTL to prevent packets to loop through the network forever if routing errors create a loop. This explains why the two copies of the packet have a TTL differing by 1,</p></li><li><p>the mirroring mechanism in the switch may not deliver frames grabbed at different sources in the same order in which they passed the source ports. This would explain why a packet with lower TTL was captured before a packet with higher TTL, but not why there is a negative timestamp delta between them, because the timestamps are assigned by the capturing machine, not the mirroring switch,</p></li><li><p>this leads to suspicion that the capture has been taken at several interfaces simultaneously and their timestamper-to-file propagation times were different (so the packet with earlier timestamp was written to the file later than the one with later timestamp) or that the capture file has been merged from two source files captured on different machines with slightly offset real time clock.</p></li></ul></div><div id="comment-56491-info" class="comment-info"><span class="comment-age">(18 Oct '16, 03:00)</span> sindy</div></div></div><div id="comment-tools-56373" class="comment-tools"></div><div class="clear"></div><div id="comment-56373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

