+++
type = "question"
title = "stream graph for rtt"
description = '''Hi,  while using stream graph for rtt it shows a single point in graph for the selected packet.if i mark packets it shows pints for the marked packets in the graph. How to get graph for the whole pcap file or for a set of packets in the file? '''
date = "2013-06-05T15:56:00Z"
lastmod = "2013-06-05T22:18:00Z"
weight = 21781
keywords = [ "rtt", "streamgraph" ]
aliases = [ "/questions/21781" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [stream graph for rtt](/questions/21781/stream-graph-for-rtt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21781-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, while using stream graph for rtt it shows a single point in graph for the selected packet.if i mark packets it shows pints for the marked packets in the graph. How to get graph for the whole pcap file or for a set of packets in the file?<br />
</p></div><div id="question-tags" class="tags-container tags">rtt streamgraph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '13, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/1bfd7c73ffe5eef5c45238e0e0f548a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SThomas&#39;s gravatar image" /><p>SThomas<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SThomas has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '13, 15:57</p></div></div><div id="comments-container-21781" class="comments-container"></div><div id="comment-tools-21781" class="comment-tools"></div><div class="clear"></div><div id="comment-21781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21786"></span>

<div id="answer-container-21786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21786-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use Satistics IO Graph to draw the RTT over time for each or a filtered set of packets.</p><p>Open Statistics IO Graph, change the Y-axis Unit to "Advanced".</p><p>Here you can set the Calc: to MIN(*) and put "tcp.analysis.ack_rtt" in the field</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IOGraphsctrace.pcap.png" alt="IOGraph_RTT" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '13, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></img></div></div><div id="comments-container-21786" class="comments-container"></div><div id="comment-tools-21786" class="comment-tools"></div><div class="clear"></div><div id="comment-21786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

