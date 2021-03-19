+++
type = "question"
title = "Investigating delay and latency"
description = '''I am new to WireShark, Sorry for the silly question, I am a bit confuse about normal delay in network as stated in Wireshark 101. I am investigating delay and latency on a live office network, which type of traffic are consider as having high latency. The following shots are from a the packet captur...'''
date = "2016-10-07T13:07:00Z"
lastmod = "2016-10-08T04:32:00Z"
weight = 56227
keywords = [ "delayed" ]
aliases = [ "/questions/56227" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Investigating delay and latency](/questions/56227/investigating-delay-and-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to WireShark, Sorry for the silly question, I am a bit confuse about normal delay in network as stated in Wireshark 101. I am investigating delay and latency on a live office network, which type of traffic are consider as having high latency. The following shots are from a the packet capture,</p><p>64.233.184.x to 193.x.x.x This is an external to internal, [TCP keep-alive] [ACK] is this a normal delay?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/B.png" alt="alt text" /> Local 193.x.x.x to 191.96.x.x Can this also be termed as normal delay? How do I investigate TCP packets with problems, that is what is the cause? <img src="https://osqa-ask.wireshark.org/upfiles/A.png" alt="alt text" /> Will produce any more information on request.</p><p>yabadoo</p></div><div id="question-tags" class="tags-container tags">delayed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '16, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/430ab79dcdecce6449403c9d41492aba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yabad0o&#39;s gravatar image" /><p>yabad0o<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yabad0o has no accepted answers">0%</span></p></img></div></div><div id="comments-container-56227" class="comments-container"></div><div id="comment-tools-56227" class="comment-tools"></div><div class="clear"></div><div id="comment-56227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56231"></span>

<div id="answer-container-56231" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56231-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Keep alive is not a delay. It just indicates that the server was not sending data for some time and the client is probing the server to see if the connection is still up from that side. A ACK would mean that the connection has to be kept out. At each keep-alive interval, this is done, if for the same period of time, there is no data transfer. Without a pcap it is hard to say where the delay is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '16, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/9a1678211e56b7aa690fcf07f4eeb13a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prajith%20Vettil&#39;s gravatar image" /><p>Prajith Vettil<br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prajith Vettil has one accepted answer">100%</span></p></img></div></div><div id="comments-container-56231" class="comments-container"></div><div id="comment-tools-56231" class="comment-tools"></div><div class="clear"></div><div id="comment-56231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

