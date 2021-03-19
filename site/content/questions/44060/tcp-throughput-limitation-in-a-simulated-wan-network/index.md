+++
type = "question"
title = "TCP Throughput Limitation in a simulated WAN Network"
description = '''I have the following WAN network topology in which I simulate it using Network Simulator ns3: Wireless Station &amp;lt;---Wireless Link---&amp;gt; Access Point &amp;lt;...Wired Link...&amp;gt; Router &amp;lt;...Wired Link...&amp;gt; OnOffApplication  The wireless link uses 802.11ad and supports up to 5 Gbps with Two Level ...'''
date = "2015-07-10T10:30:00Z"
lastmod = "2015-07-10T10:30:00Z"
weight = 44060
keywords = [ "throughput", "802.11", "wan", "tcp", "simulator" ]
aliases = [ "/questions/44060" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Throughput Limitation in a simulated WAN Network](/questions/44060/tcp-throughput-limitation-in-a-simulated-wan-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44060-score" class="post-score" title="current number of votes">0</div><span id="post-44060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following WAN network topology in which I simulate it using Network Simulator ns3:</p><p>Wireless Station &lt;---Wireless Link---&gt; Access Point &lt;...Wired Link...&gt; Router &lt;...Wired Link...&gt; OnOffApplication</p><ol><li>The wireless link uses 802.11ad and supports up to 5 Gbps with Two Level Aggregation (MSDU + MPDU Aggregations).</li><li>The wired Links are Full Duplex Ethernet with 10 Gbps of Bandwidth and 20 ms of propagation delay.</li><li>The OnOffApplication uses TCP as transport layer. It generates data with a rate of 4Gbps and the packet is 1448 Bytes.</li></ol><p>The OnOffApplication establishes a TCP connection towards the Wireless Station using Cubic Variant and I keep the application on On State to keep always sending packets. However, despite the high bandwidth I have, the perceived throughput by the client is very low and it is around 25 Mbps. I have tuned the receive buffer on the two ends to support up to 4 MBytes. So I assume the transmitted will be limited by its congestion window.</p><p>So what's the limiting factor of the throughput in my simulation? Is there any parameters that I need to tune?</p><p><strong>Note:</strong> When I decrease the delay on the wired link, I start to get high throughput and I can reach up to 3 Gbps for a delay of 0.1 ms.</p><p>So why TCP is so affected by propagation delay?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-wan" rel="tag" title="see questions tagged &#39;wan&#39;">wan</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-simulator" rel="tag" title="see questions tagged &#39;simulator&#39;">simulator</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '15, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/566cfe38b17a31f0dc825c86538cf3d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hany%20Assasa&#39;s gravatar image" /><p><span>Hany Assasa</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hany Assasa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jul '15, 10:49</strong> </span></p></div></div><div id="comments-container-44060" class="comments-container"></div><div id="comment-tools-44060" class="comment-tools"></div><div class="clear"></div><div id="comment-44060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

