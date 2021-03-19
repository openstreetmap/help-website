+++
type = "question"
title = "Customer seeing lots of latency. Are these tcp.retransmits accurate?"
description = '''I&#x27;m seeing about 6% retransmits when I divide the number of packets displayed with display filter tcp.analysis.retransmission/ total number of captured packets. Am I doing this correctly? I also looked under expert and got the same number of retransmissions. I also was reading that for iSCSI traffic...'''
date = "2012-05-30T14:11:00Z"
lastmod = "2012-05-31T14:26:00Z"
weight = 11481
keywords = [ "control", "latency", "retransmissions", "storm", "discards" ]
aliases = [ "/questions/11481" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Customer seeing lots of latency. Are these tcp.retransmits accurate?](/questions/11481/customer-seeing-lots-of-latency-are-these-tcpretransmits-accurate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11481-score" class="post-score" title="current number of votes">0</div><span id="post-11481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing about 6% retransmits when I divide the number of packets displayed with display filter tcp.analysis.retransmission/ total number of captured packets. Am I doing this correctly? I also looked under expert and got the same number of retransmissions. I also was reading that for iSCSI traffic it is recommended to turn off Unicast Storm control. They mention this feature discarding packets when traffic reaches a threshold. What could I look for in the Cisco switch to see if this feature is discarding packets? I see 0 VLAN discard frames on all ports.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-control" rel="tag" title="see questions tagged &#39;control&#39;">control</span> <span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-storm" rel="tag" title="see questions tagged &#39;storm&#39;">storm</span> <span class="post-tag tag-link-discards" rel="tag" title="see questions tagged &#39;discards&#39;">discards</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '12, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p><span>gipper</span><br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-11481" class="comments-container"></div><div id="comment-tools-11481" class="comment-tools"></div><div class="clear"></div><div id="comment-11481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11486"></span>

<div id="answer-container-11486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11486-score" class="post-score" title="current number of votes">0</div><span id="post-11486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is mainly three reasons for a re-transmit</p><ol><li>Packet loss (either data or ACK)</li><li>The receiver can't handle the data (for whatever reason) and does not ACK it</li><li>The sender can't handle the ACK (for whatever reason) and then retransmits</li></ol><p>To figure out what causes the retransmits in your case, the capture file would help to get a first glimpse.</p><p>If you think strom control is dropping packets, I suggest to check the counters on the switch (and also the logs, if logging is enabled).</p><p><strong>Storm control status</strong></p><blockquote><p><code>show strom-control</code></p></blockquote><p>this will show "Blocking" (Filter State) if strom control is dropping packets. HOWEVER, you will see this only during the time of blocking.</p><blockquote><p><code>Switch# show storm-control</code><br />
<code>Interface  Filter State   Upper        Lower        Current</code><br />
<code>---------  -------------  -----------  -----------  ----------</code><br />
<code>Fa0/5      Blocking           1m bps     500k bps    2.08m bps</code><br />
</p></blockquote><p>Storm control will block based on bandwith or packet rate. To get an idea if you get close to the numbers configured for strom control, I suggest to look at the IO Graphs during the timeframe you see the retransmits.</p><blockquote><p><code>Statistics -&gt; IO Graph -&gt; Y Axis -&gt; Unit: Packets/Tick</code><br />
<code>Statistics -&gt; IO Graph -&gt; Y Axis -&gt; Unit: Bits/Tick</code><br />
</p></blockquote><p><strong>Port/Interface statistics counters</strong></p><blockquote><p><code>show interface &lt;interface name&gt;</code></p></blockquote><p><strong>Logs</strong><br />
</p><blockquote><p><code>show log</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '12, 02:32</strong> </span></p></div></div><div id="comments-container-11486" class="comments-container"><span id="11504"></span><div id="comment-11504" class="comment"><div id="post-11504-score" class="comment-score"></div><div class="comment-text"><p>I've uploaded full trace to <a href="ftp://customer:4">ftp://customer:4</a><span class="__cf_email__" data-cfemail="2d4c595f485965586d">[email protected]</span><a href="http://ftp.compellent.com/Gipp/20120530_1.pcap">ftp.compellent.com/Gipp/20120530_1.pcap</a> There'e also smaller saves of the same file first one is 10MB next one is 16MB <a href="ftp://customer:4">ftp://customer:4</a><span class="__cf_email__" data-cfemail="a6c7d2d4c3d2eed3e6">[email protected]</span><a href="http://ftp.compellent.com/Gipp/esxserver3.cap">ftp.compellent.com/Gipp/esxserver3.cap</a> <a href="ftp://customer:4">ftp://customer:4</a><span class="__cf_email__" data-cfemail="3d5c494f584975487d">[email protected]</span><a href="http://ftp.compellent.com/Gipp/esxserver4.cap">ftp.compellent.com/Gipp/esxserver4.cap</a> Here's port counter info from Cisco switch for the port with most retrans</p><pre><code>GigabitEthernet1/0/18 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 001c.0f72.1912 (bia 001c.0f72.1912)
  Description: Link to ESXs12 Fabric A
  MTU 9000 bytes, BW 1000000 Kbit, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 2/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:14, output hang never
  Last clearing of &quot;show interface&quot; counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 1351633
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 9418000 bits/sec, 422 packets/sec
  5 minute output rate 1022000 bits/sec, 405 packets/sec
     3512522867 packets input, 11632586449906 bytes, 0 no buffer
     Received 75497 broadcasts (25625 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 25625 multicast, 283 pause input
     0 input packets with dribble condition detected
     5560805283 packets output, 9690588226086 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out</code></pre></div><div id="comment-11504-info" class="comment-info"><span class="comment-age">(31 May '12, 11:26)</span> <span class="comment-user userinfo">gipper</span></div></div><span id="11507"></span><div id="comment-11507" class="comment"><div id="post-11507-score" class="comment-score"></div><div class="comment-text"><p>oops. Can someone please move the comment to my answer. I picked the wrong option while I converted the question to an answer...</p><p>Done (grahamb) - Thanks (Kurt)</p></div><div id="comment-11507-info" class="comment-info"><span class="comment-age">(31 May '12, 13:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11508"></span><div id="comment-11508" class="comment"><div id="post-11508-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I've uploaded full trace to <code>ftp://customer:4[email protected]ftp.compellent.com/Gipp/20120530_1.pcap</code><br />
</p></blockquote><p>I'm pretty sure, only few people here (if any) are willing to wade through 1,4 GByte of your data. Are you sure you want to disclose that much internal data on the internet!?!</p><blockquote><p>There'e also smaller saves of the same file first one is 10MB next one is 16MB</p></blockquote><p>What did you find in those capture files?</p><blockquote><p>Here's port counter info from Cisco switch for the port with most retrans</p></blockquote><p>can you please format the output, so it's readable? Anyway, I don't see any problem that would explain dropped packets. Did you check the switch logs?</p></div><div id="comment-11508-info" class="comment-info"><span class="comment-age">(31 May '12, 13:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11509"></span><div id="comment-11509" class="comment"><div id="post-11509-score" class="comment-score"></div><div class="comment-text"><p>There are some "Lost Segment", "Retransmission", "DUP ACK", etc. That could be a sign for packet loss, however, it could also be a sign that wireshark did not see all packets (switch mirror problem) or it was not able to write all frames to disk (high packet rate and throughput).</p><ul><li>What's the status of strom control?<br />
</li><li>Is it enabled?<br />
</li><li>If so, how is it configured?<br />
</li><li>Did you check the switch logs?</li></ul></div><div id="comment-11509-info" class="comment-info"><span class="comment-age">(31 May '12, 14:26)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11486" class="comment-tools"></div><div class="clear"></div><div id="comment-11486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

