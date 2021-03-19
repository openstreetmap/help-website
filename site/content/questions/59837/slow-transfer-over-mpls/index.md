+++
type = "question"
title = "Slow transfer over MPLS"
description = '''Hello, Our company has a 5MB IP/VPN MPLS between our Seattle and Portland offices. When we move files between offices we see very slow transfer speeds, along the lines of 150kb ps to 350kb ps. I know we aren&#x27;t going to move files at 4-5mb per second but this seems awfully slow. I grabbed some packet...'''
date = "2017-03-03T12:56:00Z"
lastmod = "2017-03-05T17:48:00Z"
weight = 59837
keywords = [ "slow", "mpls" ]
aliases = [ "/questions/59837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow transfer over MPLS](/questions/59837/slow-transfer-over-mpls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59837-score" class="post-score" title="current number of votes">0</div><span id="post-59837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Our company has a 5MB IP/VPN MPLS between our Seattle and Portland offices. When we move files between offices we see very slow transfer speeds, along the lines of 150kb ps to 350kb ps. I know we aren't going to move files at 4-5mb per second but this seems awfully slow.</p><p>I grabbed some packets during a transfer from the Netgear Nas in Seattle 192.168.2.10 to my local desktop in Portland 192.168.0.172 and I am hoping someone could take a look and see if you can see anything that will aid in our troubleshooting. I just started at this company so I don't have any history of this issue other than "it's always been slow".</p><p>You can find the export from wireshark here: <a href="https://drive.google.com/file/d/0B6OdS4hheiP2U3Z3RDVkdWx5Ykk/view?usp=sharing">https://drive.google.com/file/d/0B6OdS4hheiP2U3Z3RDVkdWx5Ykk/view?usp=sharing</a></p><p>Note that before this transfer I set the MTU size on my local network card and on the NAS to 1400 because I thought maybe it was just a lot of fragmentation. This had no effect on the transfer speeds.</p><p>Here are the results when I ping the NAS from my computer. Pinging 192.168.2.10 with 32 bytes of data: Reply from 192.168.2.10: bytes=32 time=12ms TTL=60 Reply from 192.168.2.10: bytes=32 time=7ms TTL=60 Reply from 192.168.2.10: bytes=32 time=8ms TTL=60 Reply from 192.168.2.10: bytes=32 time=24ms TTL=60</p><p>Ping statistics for 192.168.2.10: Packets: Sent = 4, Received = 4, Lost = 0 (0% loss), Approximate round trip times in milli-seconds: Minimum = 7ms, Maximum = 24ms, Average = 12ms</p><p>Thanks in advance for any advice you can offer!</p><p>Danny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '17, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/8b7aebc4503816ef17ff3b08e156eb42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dannyq&#39;s gravatar image" /><p><span>dannyq</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dannyq has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Mar '17, 12:58</strong> </span></p></div></div><div id="comments-container-59837" class="comments-container"><span id="59842"></span><div id="comment-59842" class="comment"><div id="post-59842-score" class="comment-score"></div><div class="comment-text"><p>Looks like you have got packet loss. Maybe you have somewhere a duplex mismatch in Seattle or Portland.</p></div><div id="comment-59842-info" class="comment-info"><span class="comment-age">(03 Mar '17, 15:10)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="59846"></span><div id="comment-59846" class="comment"><div id="post-59846-score" class="comment-score"></div><div class="comment-text"><p>Try a continuous ping with 1200 byte payload.</p></div><div id="comment-59846-info" class="comment-info"><span class="comment-age">(04 Mar '17, 10:20)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="59861"></span><div id="comment-59861" class="comment"><div id="post-59861-score" class="comment-score"></div><div class="comment-text"><p>What bandwidth is configured / reserved for your link?</p><p>A quick analysis using Statistics -&gt; IO Graph reveals a bandwidth of approx. 2 MBit/sec.</p></div><div id="comment-59861-info" class="comment-info"><span class="comment-age">(05 Mar '17, 10:12)</span> <span class="comment-user userinfo">packethunter</span></div></div></div><div id="comment-tools-59837" class="comment-tools"></div><div class="clear"></div><div id="comment-59837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59863"></span>

<div id="answer-container-59863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59863-score" class="post-score" title="current number of votes">1</div><span id="post-59863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In my opinion, packet losses are a major component of the cause of the slowness here.</p><p>While the overall throughput averages around just under 2.5 Mbps, there are periods where the instantaneous rate gets close to the maximum 5 Mbps. When the flow ramps up to this rate, we then see multiple packet losses - with the associated Selective ACKs and retransmissions. The flow rate reduces and then ramps up again.</p><p>At those times of maximum throughput, we have ramped up to just 6 or 7 packets in flight (approx. 10 KB), then we get more packet losses and repeat the cycle.</p><p>So <span>@dannyq</span>, you should be hunting for the cause of these packet losses in the path between your client and server. We might lean towards looking at the WAN, but it could be anywhere.</p><p>The fact that they seem to occur when we have about 10 KB "in flight" might be a clue (a device with not much buffer space?). Or (same symptom stated differently) it might the fact that we lose packets when we get close to the 5 Mbps throughput rate (devices at edge of the WAN can't keep up?).</p><p>Could your MPLS link be oversubscribed by other traffic to/from other offices? If I could, I'd begin by seeing if other MPLS traffic is suffering packet losses.</p><p>It could, of course, be any of the other usual suspects (e.g., duplex mismatch as already mentioned elsewhere in this post, overloaded device such as a firewall, etc, etc).</p><p>Finally perhaps we can say what is NOT the problem here. To save any time spent looking in the wrong areas.</p><p><strong>Window Sizes and Scaling:</strong></p><p>The RTT for the SMB file transfer seems to be around 8ms but sometimes up to 11ms. At 5 Mbit/sec and with RTT of 10ms, the Bandwidth Delay Product is just 10 KB.</p><p>So even if TCP Window Scaling was not used (64 KB window), we should still be easily able to fill the 5 Mbps link.</p><p>Although we don't see the 3-way handshake for the SMB connection, we do see them for some HTTPS connections between the same client and server. These show a client scale of 8 (x256) and a server scale of 7 (x128).</p><p>The observed in-flight data from the server never fills the client's receive window.</p><p>We can therefore say that the "slow" flow does not appear to be related to Window Scaling or Window Sizing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '17, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p><span>Philst</span><br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></div></div><div id="comments-container-59863" class="comments-container"></div><div id="comment-tools-59863" class="comment-tools"></div><div class="clear"></div><div id="comment-59863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

