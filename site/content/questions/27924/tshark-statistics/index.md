+++
type = "question"
title = "tshark statistics"
description = '''Hello, on tshark statistics I see that a whole packet 1514 bytes is in the time interval of 1 microsecond. It is proper behaviour? |---------------------------------------- | Interval | Frames | Bytes |  |---------------------------------------- | 0.000000 &amp;lt;&amp;gt; 0.000001 | 1 | 1514 |  | 0.000001 ...'''
date = "2013-12-08T12:50:00Z"
lastmod = "2013-12-08T13:19:00Z"
weight = 27924
keywords = [ "statistics" ]
aliases = [ "/questions/27924" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark statistics](/questions/27924/tshark-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27924-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, on tshark statistics I see that a whole packet 1514 bytes is in the time interval of 1 microsecond. It is proper behaviour?</p><p>|----------------------------------------</p><p>| Interval | Frames | Bytes |</p><p>|----------------------------------------</p><p>| 0.000000 &lt;&gt; 0.000001 | 1 | 1514 |</p><p>| 0.000001 &lt;&gt; 0.000002 | 0 | 0 |<br />
</p><p>| 0.000002 &lt;&gt; 0.000003 | 0 | 0 |<br />
</p><p>| 0.000003 &lt;&gt; 0.000004 | 0 | 0 |</p><p>| 0.000004 &lt;&gt; 0.000005 | 0 | 0 |<br />
</p><p>| 0.000005 &lt;&gt; 0.000006 | 1 | 1514 |<br />
</p><p>| 0.000006 &lt;&gt; 0.000007 | 0 | 0 |</p><p>I have capture only headers to my trace pcap file.</p></div><div id="question-tags" class="tags-container tags">statistics</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '13, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/28071bd7cf93e424c03dec9086ffa60f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net16&#39;s gravatar image" /><p>net16<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net16 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '13, 13:03</p></div></div><div id="comments-container-27924" class="comments-container"></div><div id="comment-tools-27924" class="comment-tools"></div><div class="clear"></div><div id="comment-27924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27925"></span>

<div id="answer-container-27925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27925-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>It is proper behaviour?</p></blockquote><p>It depends on the speed of the network. In a 1Gbit/s network, it takes ~ 1.5 microseconds to transmit a full frame. Your values are plausible in a Gbit network, as there is a time gap of 5 microseconds between the frames.</p><p>Regarding the time frame 0-1 microsecond. That's just the calculation interval. It tells you the time slot of the <strong>arrival time</strong> of the frame. As there is no information in the capture file how long it took to transmit the frame, it does <strong>not</strong> mean that the frame arrived fully in that time frame.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '13, 13:25</p></div></div><div id="comments-container-27925" class="comments-container"><span id="27927"></span><div id="comment-27927" class="comment"><div id="post-27927-score" class="comment-score"></div><div class="comment-text"><p>Kurt, thank you for the opinion. Hmm, I have 100Mb/s link and gap is another (I write above values a bit random - for explanation purposes). It seems that all packets in my traces are received during 1 microsecond. It is normal on FastEthernet interfaces too? On the Wireshark display list we can see only arrival time and I cannot check if tshark fits 1514 bytes during 1 microsecond.</p><p>It would be possible in such scenarion that tshark divide 1514 on two part: 900 bytes during 1 us and the rest 614 bytes during next 1 us?</p><p>Regards</p><p>Ps. I just wrote your extended answer. I understand that my second question is unfounded. Thanks.</p></div><div id="comment-27927-info" class="comment-info"><span class="comment-age">(08 Dec '13, 13:36)</span> net16</div></div><span id="27929"></span><div id="comment-27929" class="comment"><div id="post-27929-score" class="comment-score"></div><div class="comment-text"><p>Are those two frames both incoming or outgoing?</p></div><div id="comment-27929-info" class="comment-info"><span class="comment-age">(08 Dec '13, 13:54)</span> Kurt Knochner ♦</div></div><span id="27930"></span><div id="comment-27930" class="comment"><div id="post-27930-score" class="comment-score"></div><div class="comment-text"><p>It is incoming traffic, but I see the same (1514 during 1 us interval) on outgoing interface.</p></div><div id="comment-27930-info" class="comment-info"><span class="comment-age">(08 Dec '13, 14:24)</span> net16</div></div><span id="27931"></span><div id="comment-27931" class="comment"><div id="post-27931-score" class="comment-score"></div><div class="comment-text"><p>Can you post a capture file?</p></div><div id="comment-27931-info" class="comment-info"><span class="comment-age">(08 Dec '13, 14:26)</span> Kurt Knochner ♦</div></div><span id="27932"></span><div id="comment-27932" class="comment"><div id="post-27932-score" class="comment-score"></div><div class="comment-text"><p>It can be problem. Maybe you have any trace which divides packet on two part - one to first microsecond and second part to second microsecond?</p><p>But I think that it is not possible - according to your answer about arrival times and time slots.</p></div><div id="comment-27932-info" class="comment-info"><span class="comment-age">(08 Dec '13, 14:39)</span> net16</div></div><span id="27933"></span><div id="comment-27933" class="comment not_top_scorer"><div id="post-27933-score" class="comment-score"></div><div class="comment-text"><p>tshark does not divide frames. The arrival time is either in one interval or in another.</p></div><div id="comment-27933-info" class="comment-info"><span class="comment-age">(08 Dec '13, 14:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27925" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-27925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

