+++
type = "question"
title = "tcptrace graph and duplicate ACK"
description = '''Hello, Can someone tell (seeing the attached graph) how many duplicate acks in this trace? When i check the pcap file, i am seeing following 5 duplicate ACks Time 0.404 ----- &amp;gt; 2 duplicate ACKs Time 0.472 ------&amp;gt; 2 duplicate ACK Time 3.956 ------ &amp;gt; 1 duplicate ACK. Three retransmissions (in...'''
date = "2014-05-09T17:08:00Z"
lastmod = "2014-05-12T18:40:00Z"
weight = 32696
keywords = [ "dup-ack" ]
aliases = [ "/questions/32696" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcptrace graph and duplicate ACK](/questions/32696/tcptrace-graph-and-duplicate-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Can someone tell (seeing the attached graph) how many duplicate acks in this trace? When i check the pcap file, i am seeing following 5 duplicate ACks</p><p>Time 0.404 ----- &gt; 2 duplicate ACKs Time 0.472 ------&gt; 2 duplicate ACK Time 3.956 ------ &gt; 1 duplicate ACK.</p><p>Three retransmissions (in reverse direction) are at 0.7, 1.15 and 2.068.</p><p>But looking at the attached graph, there are two dup acks (one tick between 1.1 &amp; 1.2 and other between 2.0 and 2.1) but i dont see them in my pcap file. Not sure if i am understanding correctly how duplicate acks are represented in tcptrace graphs.</p><p>Thanks</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcptracegraph.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dup-ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '14, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/39356e003826b924c6b683f177900afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iWireshark&#39;s gravatar image" /><p>iWireshark<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iWireshark has no accepted answers">0%</span></p></img></div></div><div id="comments-container-32696" class="comments-container"></div><div id="comment-tools-32696" class="comment-tools"></div><div class="clear"></div><div id="comment-32696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32740"></span>

<div id="answer-container-32740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32740-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Duplicate ACKs are represented by the little short downward lines. So, in this graph, there appear to be duplicate ACKs around times 0.4, 0.47, 0.7, 1.15, 2.08, 3.9, and 4.0.</p><p>It would help if you made the trace file available so we could correlate the graph with the actual packets.</p><p>Remember that the trptrace graph, like sll the TCP stream graphs, shows one stream in one direction, based on the selected packet, not all captured packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '14, 18:40</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-32740" class="comments-container"></div><div id="comment-tools-32740" class="comment-tools"></div><div class="clear"></div><div id="comment-32740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

