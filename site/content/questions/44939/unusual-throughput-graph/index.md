+++
type = "question"
title = "Unusual Throughput Graph"
description = '''I&#x27;m got a capture with what seems like some very poor tcp performance. the general stats are listed below. The throughput graphs is pretty strange and I&#x27;m hoping for some explanation. Total Frames: 9655 TCP Duplicate ACKs: 1356 - 14% TCP Retransmissions: 167 - 1.7% TCP Out-of-Order - 373 - 3.9% TCP ...'''
date = "2015-08-09T16:47:00Z"
lastmod = "2015-08-10T23:20:00Z"
weight = 44939
keywords = [ "graph", "throughput" ]
aliases = [ "/questions/44939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unusual Throughput Graph](/questions/44939/unusual-throughput-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44939-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm got a capture with what seems like some very poor tcp performance. the general stats are listed below. The throughput graphs is pretty strange and I'm hoping for some explanation. Total Frames: 9655 TCP Duplicate ACKs: 1356 - 14% TCP Retransmissions: 167 - 1.7% TCP Out-of-Order - 373 - 3.9% TCP Zero Window Segment - 2 (Client) Packets A--&gt;B: 3975 Bytes A--&gt;B: 12503695 Bits/s A--&gt;B: 3,012,201 Duration: 33.2081<img src="https://osqa-ask.wireshark.org/upfiles/Unusual_TCP_Time-Seq_Graph2_FB2pxoy.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Unusual_TCP_Time-Seq_Graph_plJkYSS.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">graph throughput</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '15, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/6e0fda2a5c8d02515d88f004b33a9998?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fritzbied&#39;s gravatar image" /><p>fritzbied<br />
<span class="score" title="6 reputation points">6</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fritzbied has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44939" class="comments-container"></div><div id="comment-tools-44939" class="comment-tools"></div><div class="clear"></div><div id="comment-44939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44954"></span>

<div id="answer-container-44954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44954-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure exactly what the question here is but ...<br />
The trace seems to have been taken at the client at 10.27.4.144 streaming data to the server at 10.21.21.78 even though the capture name suggests the opposite...<br />
The statistics show that 3975 packets were needed to transfer 12 503 695 bytes within 33.2 seconds that is an average packet size of 3145 bytes/packet and a throughput of 376.6 kbyte/s. There are a few slow retransmits and the actual transfer time is shorter than the 33.2 seconds.<br />
Depending on the infrastructure between client and server doesn't necessarily look like a 'very poor' TCP performance to me.</p><p>The 'strange-ness' of the graph is due to TCP segmentation offload being enabled</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '15, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-44954" class="comments-container"><span id="44967"></span><div id="comment-44967" class="comment"><div id="post-44967-score" class="comment-score"></div><div class="comment-text"><p>Interesting....tcp segmentation offloading, will have to look into it. The captured was taken with NETMON on a Windows 2008 server and analyzed on a Windows 8.1. I was trying to understand the TCP ack behavior based on the graph.</p><p>If the graph is not impacted by TCP segmentation offloading can you explain the ack line jumping up and down with reference to the segment throughput line? First time I have seen something like this on our network. Or am I totally missing the point on this?</p><p>Thanks in advance</p><p>Fritzbied</p></div><div id="comment-44967-info" class="comment-info"><span class="comment-age">(11 Aug '15, 14:24)</span> fritzbied</div></div><span id="44973"></span><div id="comment-44973" class="comment"><div id="post-44973-score" class="comment-score"></div><div class="comment-text"><blockquote><p>can you explain the ack line jumping up and down with reference to the segment throughput line?</p></blockquote><p>hard to tell without the pcap file. Would it be possible to upload the capture file somewhere and post the link here for further analysis?</p></div><div id="comment-44973-info" class="comment-info"><span class="comment-age">(11 Aug '15, 16:07)</span> Kurt Knochner ♦</div></div><span id="44988"></span><div id="comment-44988" class="comment"><div id="post-44988-score" class="comment-score"></div><div class="comment-text"><p>I believe its the seq numbers that are 'jumping up and down' due to retransmissions ... and the ack numbers are increasing pretty steadily ...<br />
Without the pcap it's hard to tell though</p></div><div id="comment-44988-info" class="comment-info"><span class="comment-age">(12 Aug '15, 00:30)</span> mrEEde</div></div><span id="44990"></span><div id="comment-44990" class="comment"><div id="post-44990-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I believe its the seq numbers that are 'jumping up and down' due to retransmissions</p></blockquote><p>hm.. the time/sequence graph usually only shows data in one direction, which would mean that either the SEQ <strong>or</strong> the ACK numbers are really 'jumping' (no idea what would cause that) <strong>OR</strong> that there is a bug in Wireshark. We would need the pcap file to figure out what's going on.</p></div><div id="comment-44990-info" class="comment-info"><span class="comment-age">(12 Aug '15, 00:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-44954" class="comment-tools"></div><div class="clear"></div><div id="comment-44954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

