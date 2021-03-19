+++
type = "question"
title = "Round Trip Time (RTT) Graph"
description = '''Hello everyone, I want to make a RTT graph for whole communication between two IP addresses and when I do &#x27;Conversation Filter-&amp;gt;IPv4&#x27; then i got all communication between this two IP addresses, but now when I do RTT Graph it&#x27;s show me the RTT for certain Stream and NOT for whole communication bet...'''
date = "2017-05-19T07:05:00Z"
lastmod = "2017-05-19T12:19:00Z"
weight = 61508
keywords = [ "rtt", "graph" ]
aliases = [ "/questions/61508" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Round Trip Time (RTT) Graph](/questions/61508/round-trip-time-rtt-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61508-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I want to make a RTT graph for whole communication between two IP addresses and when I do 'Conversation Filter-&gt;IPv4' then i got all communication between this two IP addresses, but now when I do RTT Graph it's show me the RTT for certain Stream and NOT for whole communication between this two IPv4 addresses. Is it possible to make some RTT graph for whole communication?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">rtt graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '17, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/6e54c4932635e2972923dfe65553c08b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicola%20Tesla&#39;s gravatar image" /><p>Nicola Tesla<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicola Tesla has no accepted answers">0%</span></p></div></div><div id="comments-container-61508" class="comments-container"></div><div id="comment-tools-61508" class="comment-tools"></div><div class="clear"></div><div id="comment-61508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61510"></span>

<div id="answer-container-61510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61510-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try to use the I/O Graph for that kind: If you put in the IPv4 conversation into the filter field and plot the max value of the tcp.analysis.ack_rtt field at Y-axis. And I suggest to set plot interval to a value less then 1 sec. <img src="https://osqa-ask.wireshark.org/upfiles/2017-05-19_21-15-50.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '17, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '17, 12:22</p></div></div><div id="comments-container-61510" class="comments-container"><span id="61516"></span><div id="comment-61516" class="comment"><div id="post-61516-score" class="comment-score"></div><div class="comment-text"><p>Christian_R Thank you, this is what I want to do, but please, can you explain what is the difference between 'tcp.analysis.ack_rtt' and 'tcp.time_delta'. I suppose that 'tcp.analysis.ack_rtt' is RTT just for ACK packet and 'tcp.time_delta' is the time delay in one direction, but <strong>if</strong> this is true, then how we can find the RTT for every packet and not just for ACK.</p><p>Thank you in advance. :)</p></div><div id="comment-61516-info" class="comment-info"><span class="comment-age">(19 May '17, 14:18)</span> Nicola Tesla</div></div><span id="61517"></span><div id="comment-61517" class="comment"><div id="post-61517-score" class="comment-score">1</div><div class="comment-text"><p>RTT means time between packet is send and answer comes back tcp.time_delta is just the time between two packets in the trace. Think about the sender sends 5 packets in the row. The best RTT measurement for the network is iRTT which measures how fast the 3way handshake is done. But it is measured only once.</p><p>ACK_RTT is from point of view the best you can get even naggle and delayed ack are activated. ACK_RTT measures the speed how fast a segement has been ACKed. Think about that every segment contains is always an ACK, too.</p></div><div id="comment-61517-info" class="comment-info"><span class="comment-age">(19 May '17, 14:48)</span> Christian_R</div></div></div><div id="comment-tools-61510" class="comment-tools"></div><div class="clear"></div><div id="comment-61510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

