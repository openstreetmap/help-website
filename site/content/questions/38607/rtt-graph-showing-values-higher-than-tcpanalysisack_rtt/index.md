+++
type = "question"
title = "RTT Graph showing values higher than tcp.analysis.ack_rtt"
description = '''Hi, I&#x27;m trying to understand how the RTT Graph (Statistics --&amp;gt; TCP StreamGraph --&amp;gt; RTT graph) relates to the ACK RTT. What I&#x27;m seeing, for a capture with a single TCP connection, is that the graph has much higher values for many data points than the calculated field tcp.analysis.ack_rtt. In fa...'''
date = "2014-12-16T14:47:00Z"
lastmod = "2014-12-16T18:40:00Z"
weight = 38607
keywords = [ "rtt", "tcp", "graph" ]
aliases = [ "/questions/38607" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [RTT Graph showing values higher than tcp.analysis.ack\_rtt](/questions/38607/rtt-graph-showing-values-higher-than-tcpanalysisack_rtt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38607-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to understand how the RTT Graph (Statistics --&gt; TCP StreamGraph --&gt; RTT graph) relates to the ACK RTT.</p><p>What I'm seeing, for a capture with a single TCP connection, is that the graph has much higher values for many data points than the calculated field tcp.analysis.ack_rtt. In fact, when sorting by the RTT column (I added it), I have only 5 points above 0.01s, whereas the graph has hundreds!</p><p>Here is the top end of the RTTs (sorted ascending):</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Top_RTTs.PNG" alt="alt text" /></p><p>Here is the graph: <img src="https://osqa-ask.wireshark.org/upfiles/RTT_Graph.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">rtt tcp graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '14, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/5e328c06f52f13af7cad3eb828441674?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoggiy&#39;s gravatar image" /><p>yoggiy<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoggiy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-38607" class="comments-container"></div><div id="comment-tools-38607" class="comment-tools"></div><div class="clear"></div><div id="comment-38607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38608"></span>

<div id="answer-container-38608" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38608-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>The values for tcp.analysis.ack_rtt are correct. Wireshark does not implement the Round Trip Time Graph correctly. This is a known bug. (See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10722">Bug 10722</a> at the Wireshark Bugzilla.) Round-Trip Time is supposed to be the time between a data packet and an ACK packet sent IN RESPONSE TO that data packet. ACKs are cumulative, and due to Delayed ACK, an ACK can acknowledge multiple data packets, but only the time between the last data packet in the series (the one that actually triggered the ACK) and the ACK is a valid RTT. However, Wireshark plots a dot on the Round-Trip Time graph for every data packet, not just the one that triggered the ACK.</p><p>tcp.analysis.ack_rtt is plotted once per ACK, not once per data packet. If you want a graph of Round Trip Time values, go to the Advanced IO Graph, select MAX(*) as the Calc type and enter tcp.analysis.ack_rtt as the field name.</p><p>When Delayed ACKs are not in use, and there is one ACK packet for each data packet, the Round Trip Time graph should be correct.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '14, 18:40</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></img></div></div><div id="comments-container-38608" class="comments-container"><span id="38634"></span><div id="comment-38634" class="comment"><div id="post-38634-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jim. I can't explain why Google didn't find that!!?</p></div><div id="comment-38634-info" class="comment-info"><span class="comment-age">(18 Dec '14, 15:50)</span> yoggiy</div></div></div><div id="comment-tools-38608" class="comment-tools"></div><div class="clear"></div><div id="comment-38608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

