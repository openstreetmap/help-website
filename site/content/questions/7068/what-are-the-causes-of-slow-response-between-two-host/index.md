+++
type = "question"
title = "What are the causes of slow response between two host?"
description = '''We are using the SAS progaram to run through a drive that is in the data center and the user are experiencing real slowness on a gig link running wireshark I saw a lots of  [TCP segment of Reassembled PDU] between two host and the program runs so slow. 10.119.xx.yy 10.120.xx.yy TCP 1514 [TCP segment...'''
date = "2011-10-25T11:01:00Z"
lastmod = "2014-06-09T10:07:00Z"
weight = 7068
keywords = [ "reassemby", "segment", "pdu", "tcp", "smb" ]
aliases = [ "/questions/7068" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What are the causes of slow response between two host?](/questions/7068/what-are-the-causes-of-slow-response-between-two-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7068-score" class="post-score" title="current number of votes">0</div><span id="post-7068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are using the SAS progaram to run through a drive that is in the data center and the user are experiencing real slowness on a gig link running wireshark I saw a lots of [TCP segment of Reassembled PDU] between two host and the program runs so slow.</p><pre><code>10.119.xx.yy    10.120.xx.yy    TCP 1514    [TCP segment of a reassembled PDU]
10.119.xx.yy    10.120.xx.yy    TCP 1514    [TCP segment of a reassembled PDU]
10.119.xx.yy    10.120.xx.yy    TCP 1514    [TCP segment of a reassembled PDU]
10.119.xx.yy    10.120.xx.yy    TCP 1514    [TCP segment of a reassembled PDU]

Transmission Control Protocol, Src Port: eims-admin (4199), Dst Port: netbios-ssn (139), Seq: 64145, Ack: 52, Len: 1460

Window size value: 63710</code></pre><p>The network seems to be not the issue here as we are utilizing less than 10% of the Bandwidth. The latency between sites is 6ms when we do traceroute and ping.</p><p>Please assist in explaining / analyzing what this means?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassemby" rel="tag" title="see questions tagged &#39;reassemby&#39;">reassemby</span> <span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '11, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/b641fd0297a0c7a5d5abb8fd2c28e8be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mEc&#39;s gravatar image" /><p><span>mEc</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mEc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Oct '11, 07:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7068" class="comments-container"></div><div id="comment-tools-7068" class="comment-tools"></div><div class="clear"></div><div id="comment-7068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7080"></span>

<div id="answer-container-7080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7080-score" class="post-score" title="current number of votes">3</div><span id="post-7080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The frame from your posting is part of a message from the workstation to the server. This can be deducted from the destination port 139.</p><p>The hint "TCP segment of a reassembled PDU" indicates that the workstation is sending a large message to the server. In fact the message is so large that it is split over several frames. As soon as Wireshark sees the last frame it pieces the segments together and decodes the whole message.</p><p>As you have provided some interesting and important information we can find one probable cause for the sluggish response.</p><p>The TCP window size controls how many bytes a sender can transmit to the remote end. The window size can roughly be compared to the volume of a water hose: If you don't have enough water in the hose water comes out sputtering. If you have too much water the pressure blows a valve.</p><p>The "volume of the network pipe" can be calculated by multiplying the bandwidth given in byte per second with the round trip time. For your network the calculation goes like this:</p><ul><li>Slowest link = 1 Gigabit per second = 125 MByte/sec = 125.000.000 Byte/sec</li><li>Round Trip Time = 6 msec = 0,006 sec</li><li>Window Size = 125.000.000 * 0,006 = 750.000 Byte</li></ul><p>If the client is running Windows XP this will not be a problem, as SMB requests are limited to something less then 64 kB. If the client is running Windows Vista or 7 the window size can be a problem, as the client can request more than 64 kB at a time using SMB pipelining - if the SAS programmer was smart enough to use the right system calls.</p><p>Also, SMB is not the best protocol for WAN links. This is discussed in <a href="http://ask.wireshark.org/questions/3044/slow-afp-and-smb-performance?page=1#3066" title="slow AFP and SMB performance">this answer</a> to another question.</p><p>Last, but not least you want to check if the server is busy. Wireshark has some excellent tools for that: Statistics -&gt; Service Response Time -&gt; SMB is a huge help. Use the display filter ip.src == 10.120.yy.yy (your servers address) to focus on the response times for just this server. Finally an advanced IO graph showing the server load for your server reveals the number of concurrent requests handled by that system.</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Oct '11, 07:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7080" class="comments-container"><span id="7096"></span><div id="comment-7096" class="comment"><div id="post-7096-score" class="comment-score"></div><div class="comment-text"><p>PH has given an excellent response here. SMB + WAN = headache. 6ms RTT isn't so bad though, and you seem to have plenty of bandwidth. You need to determine if the client and/or server is/are having resource contention issues - check CPU and disk I/O while the transfer is going on. An overactive antivirus can also slow things down depending on what kind of file(s) you're transferring.</p></div><div id="comment-7096-info" class="comment-info"><span class="comment-age">(27 Oct '11, 06:14)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="33584"></span><div id="comment-33584" class="comment"><div id="post-33584-score" class="comment-score"></div><div class="comment-text"><p>What a great explanation.Thanks. You helped me, help myself in debugging a network sluggishness issue. Search is a wonderful thing.</p></div><div id="comment-33584-info" class="comment-info"><span class="comment-age">(09 Jun '14, 10:07)</span> <span class="comment-user userinfo">kwold</span></div></div></div><div id="comment-tools-7080" class="comment-tools"></div><div class="clear"></div><div id="comment-7080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

