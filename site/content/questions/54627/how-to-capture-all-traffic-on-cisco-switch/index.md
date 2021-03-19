+++
type = "question"
title = "How to capture all traffic on cisco switch"
description = '''i wanna capture all traffic in my network as i have 50 cisco 2960 switch and i need to optimize my network for the best performance '''
date = "2016-08-06T12:35:00Z"
lastmod = "2016-08-07T00:48:00Z"
weight = 54627
keywords = [ "cisco" ]
aliases = [ "/questions/54627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture all traffic on cisco switch](/questions/54627/how-to-capture-all-traffic-on-cisco-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i wanna capture all traffic in my network as i have 50 cisco 2960 switch and i need to optimize my network for the best performance</p></div><div id="question-tags" class="tags-container tags">cisco</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '16, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/0646425dcb9d43c968a737753db646cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mohamed%20Adel&#39;s gravatar image" /><p>Mohamed Adel<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mohamed Adel has no accepted answers">0%</span></p></div></div><div id="comments-container-54627" class="comments-container"></div><div id="comment-tools-54627" class="comment-tools"></div><div class="clear"></div><div id="comment-54627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54629"></span>

<div id="answer-container-54629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54629-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's not the way to do it. If you have so much traffic that you need to optimize the network for performance, the tools needed to capture all of that traffic would me more expensive than the network.</p><p>You have</p><ul><li><p>traffic counters on the switch ports, so you can see which devices generate the most traffic and in which direction.</p></li><li><p>the knowledge of the current physical topology - where your client stations, storage servers, printers, and gateway routers to internet and eventually other networks are connected, and how your switches are connected to each other.</p></li><li><p>the knowledge about logical data flows - whether the clients mostly download data from the internet, or load data from the file servers, process them and send a similar volume of data back, or mostly generate HD video streams to be recorded on the file servers...</p></li></ul><p>This is the input information you need to optimize the network. Wireshark running at the client stations (or monitoring them using SPAN one by one) can help you confirm your theoretical assumptions about logical data flows.</p><p>The rules for LAN are:</p><ul><li><p>interconnections between switches should be kept at minimum, so elements sending high volumes of data to each other should be connected to the same switch and there should never be more than two switches on a path between any two devices</p></li><li><p>unavoidable interconnections between switches must have as much as available capacity - use the "port channel" feature to aggregate several physical links into a logical one. Doing so also provides redundancy against failure of a single port or cable.</p></li></ul><p>To answer your question technically, to safely capture all traffic on a single full-duplex port of any given bit rate, you need two ports of the same bit rate on the capturing machine, each capturing one direction at the monitored port, and a disk with enough speed and capacity to store the data. To monitor a closed group of ports on a single switch (closed in terms that the member ports of the group only send traffic to each other), it is enough to have as many monitoring ports as the traffic ports in the group (as it is enough to monitor either Tx or Rx direction of each of the ports) So if you would want to monitor using SPAN on a Cisco switch, you would have to dedicate half of the ports to traffic and the other half to monitoring, which a) a 2960 doesn't permit and b) may not be possible as you don't have enough free ports to make them monitoring ones.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '16, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Aug '16, 00:50</p></div></div><div id="comments-container-54629" class="comments-container"></div><div id="comment-tools-54629" class="comment-tools"></div><div class="clear"></div><div id="comment-54629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

