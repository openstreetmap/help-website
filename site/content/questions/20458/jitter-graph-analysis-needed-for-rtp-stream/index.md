+++
type = "question"
title = "Jitter graph analysis needed for RTP stream"
description = '''Hi I have a couple of RTP streams using FIFO as the QoS strategy on one and CBWFQ on the other for performance comparison. Using Wireshark I have ran the RTP stream analysis to get the jitter and delta values in graph format. https://dl.dropboxusercontent.com/u/39248217/RTP%20jitter%20CBWFQ.jpg http...'''
date = "2013-04-16T02:43:00Z"
lastmod = "2013-04-16T08:37:00Z"
weight = 20458
keywords = [ "qos", "jitter", "rtp", "stream", "graph" ]
aliases = [ "/questions/20458" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Jitter graph analysis needed for RTP stream](/questions/20458/jitter-graph-analysis-needed-for-rtp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20458-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a couple of RTP streams using FIFO as the QoS strategy on one and CBWFQ on the other for performance comparison. Using Wireshark I have ran the RTP stream analysis to get the jitter and delta values in graph format.</p><p><a href="https://dl.dropboxusercontent.com/u/39248217/RTP%20jitter%20CBWFQ.jpg">https://dl.dropboxusercontent.com/u/39248217/RTP%20jitter%20CBWFQ.jpg</a> <a href="https://dl.dropboxusercontent.com/u/39248217/RTP%20jitter%20FIFO.jpg">https://dl.dropboxusercontent.com/u/39248217/RTP%20jitter%20FIFO.jpg</a></p><p>I've edited the Y-axis so it fits into the graph, but FIFO has much higher values (indicating poorer performance) but just wondered what is happening here?</p><p>Please could someone shed some light as what each one is actually telling me. There's an obvious difference in how they handle the same RTP stream, but just need the depth of analysis.</p><p>Thanks very much! Dan</p></div><div id="question-tags" class="tags-container tags">qos jitter rtp stream graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/703db8b1016496f63390abe9cd3275a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dscott1709&#39;s gravatar image" /><p>dscott1709<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dscott1709 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '13, 02:43</p></div></div><div id="comments-container-20458" class="comments-container"></div><div id="comment-tools-20458" class="comment-tools"></div><div class="clear"></div><div id="comment-20458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20462"></span>

<div id="answer-container-20462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20462-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I already mentioned in your other question</p><blockquote><p><a href="http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison">http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison</a></p></blockquote><p>it is hard to interpret a graph without any information about the QoS policy used and some information about the rest of the traffic that passed the monitored device (and line).</p><p>Especially regarding the RTP jitter graphs it is pretty hard to give any good explanation without that information. So, please add more details about your test environment and your test parameters.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20462" class="comments-container"><span id="20509"></span><div id="comment-20509" class="comment"><div id="post-20509-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt</p><p>I'm passing an identical traffic mix of RTP video stream, FTP and ICMP over a 2MB serial between two Cisco routers to compare how each QoS scheme (FIFO and CBWFQ) peforms best and what happens. I've given CBWFQ precedence levels of: RTP 7 FTP 4 ICMP 1</p><p>Does that help to give you more insight into why these graphs are different?</p><p>Cheers Dan</p></div><div id="comment-20509-info" class="comment-info"><span class="comment-age">(17 Apr '13, 03:13)</span> dscott1709</div></div><span id="20533"></span><div id="comment-20533" class="comment"><div id="post-20533-score" class="comment-score"></div><div class="comment-text"><p>see my comment here: <a href="http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison">http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison</a></p></div><div id="comment-20533-info" class="comment-info"><span class="comment-age">(17 Apr '13, 12:39)</span> Kurt Knochner ♦</div></div><span id="20658"></span><div id="comment-20658" class="comment"><div id="post-20658-score" class="comment-score"></div><div class="comment-text"><p>can you please post the capture file, used to generate the graphs?</p></div><div id="comment-20658-info" class="comment-info"><span class="comment-age">(20 Apr '13, 06:08)</span> Kurt Knochner ♦</div></div><span id="20659"></span><div id="comment-20659" class="comment"><div id="post-20659-score" class="comment-score"></div><div class="comment-text"><p>based on the source ports in the graphs, I assume it is the same capture file as in question: <a href="http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison">http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison</a></p></div><div id="comment-20659-info" class="comment-info"><span class="comment-age">(20 Apr '13, 08:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20462" class="comment-tools"></div><div class="clear"></div><div id="comment-20462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20471"></span>

<div id="answer-container-20471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20471-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Indeed there's little to tell, other than the remark the there are a lot of markers set, which is unusual, and that there are "Wrong seq number" markers in your FIFO graph output, which raises doubt about the type of stream you analyze.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20471" class="comments-container"><span id="20508"></span><div id="comment-20508" class="comment"><div id="post-20508-score" class="comment-score"></div><div class="comment-text"><p>I have to admit i'm a basic user of Wireshark, so I've selected my RTP stream, clicked Telephony - RTP - Stream Analysis - selected the stream - chose graph. This is what it gave me, so not sure why there would be more markers in place to be honest. there's probably wrong sequence numbers because there was high congestion and this caused delay issues (which i wanted to happen to test which QoS scheme performs best at threshold). Does that help? Thanks, Dan</p></div><div id="comment-20508-info" class="comment-info"><span class="comment-age">(17 Apr '13, 03:12)</span> dscott1709</div></div><span id="20665"></span><div id="comment-20665" class="comment"><div id="post-20665-score" class="comment-score"></div><div class="comment-text"><p>The stream analysis was primarely designed for G.711 your milage with other codecs may vary. Fore one the marker bit has different meaning in Audio and Video.</p></div><div id="comment-20665-info" class="comment-info"><span class="comment-age">(20 Apr '13, 16:02)</span> Anders ♦</div></div><span id="20675"></span><div id="comment-20675" class="comment"><div id="post-20675-score" class="comment-score"></div><div class="comment-text"><p>Is there a difference for the jitter calculation based on the codec used? RTP contains the same timestamp information, regardless of the codes.</p><p><strong>However</strong>, the jitter calculation does indeed not work for the video stream in that capture file!??!</p></div><div id="comment-20675-info" class="comment-info"><span class="comment-age">(21 Apr '13, 07:36)</span> Kurt Knochner ♦</div></div><span id="20682"></span><div id="comment-20682" class="comment"><div id="post-20682-score" class="comment-score"></div><div class="comment-text"><p>In video streams you can have more than one packet with the same time stamp if I remember correctly. The marker bit indicating the last one(?)I would guess this throws the jitter analysis off.</p></div><div id="comment-20682-info" class="comment-info"><span class="comment-age">(21 Apr '13, 10:45)</span> Anders ♦</div></div><span id="20683"></span><div id="comment-20683" class="comment"><div id="post-20683-score" class="comment-score"></div><div class="comment-text"><p>looking at the capture file again, I can confirm your assumption. There are multiple frames with the same timestamp, while the last frame with that timestamp has the marker bit set.</p><p>Thanks for this hint!</p></div><div id="comment-20683-info" class="comment-info"><span class="comment-age">(21 Apr '13, 11:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20471" class="comment-tools"></div><div class="clear"></div><div id="comment-20471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

