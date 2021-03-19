+++
type = "question"
title = "Can ACKs happen outside the RWIN?"
description = '''I hope this is a straightforward question. Can the receiving side send ACKs at significantly less than the RWIN size? Example: Note the bytes in flight Receiving side 1.1.1.1 Sending side 2.2.2.2 48 0.000 1.1.1.1 2.2.2.2 TCP printer &amp;gt; netviewdm1 [ACK] Seq=3 Ack=32798 Win=64296 Len=0 TSV=26412037 ...'''
date = "2012-06-15T13:14:00Z"
lastmod = "2012-06-15T13:36:00Z"
weight = 11972
keywords = [ "ack", "rwin", "tcp" ]
aliases = [ "/questions/11972" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can ACKs happen outside the RWIN?](/questions/11972/can-acks-happen-outside-the-rwin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11972-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I hope this is a straightforward question. Can the receiving side send ACKs at significantly less than the RWIN size? Example:</p><p>Note the bytes in flight</p><p>Receiving side 1.1.1.1<br />
Sending side 2.2.2.2</p><pre><code>48  0.000   1.1.1.1 2.2.2.2 TCP printer &gt; netviewdm1 [ACK] Seq=3 Ack=32798 Win=64296 Len=0 TSV=26412037 TSER=3842799487
49  0.029   2.2.2.2 1.1.1.1 LPD LPD continuation [Number of bytes in flight: 1368]
50  0.000   2.2.2.2 1.1.1.1 LPD LPD continuation [Number of bytes in flight: 2736]
51  0.000   1.1.1.1 2.2.2.2 TCP printer &gt; netviewdm1 [ACK] Seq=3 Ack=35534 Win=64296 Len=0 TSV=26412040 TSER=3842799519
52  0.000   2.2.2.2 1.1.1.1 LPD LPD continuation [Number of bytes in flight: 1368]
53  0.000   2.2.2.2 1.1.1.1 LPD LPD continuation [Number of bytes in flight: 2736]
54  0.000   1.1.1.1 2.2.2.2 TCP printer &gt; netviewdm1 [ACK] Seq=3 Ack=38270 Win=64296 Len=0 TSV=26412040 TSER=3842799519
55  0.000   2.2.2.2 1.1.1.1 LPD LPD continuation [Number of bytes in flight: 1368]
56  0.000   2.2.2.2 1.1.1.1 LPD LPD continuation [Number of bytes in flight: 2720]
57  0.000   1.1.1.1 2.2.2.2 TCP printer &gt; netviewdm1 [ACK] Seq=3 Ack=40990 Win=64296 Len=0 TSV=26412040 TSER=3842799519</code></pre><p>Even though the RWIN is 64296, the receiving side (Windows)keeps sending ACKs after only 2 packets, with a total bytes in flight of less than 4 KB. This happens for the duration of the transfer, which averages 26 KBps over a 12 Mbps MPLS port w/ 30-35 ms latency. TCP scaling is off.</p><p>I don't understand, can someone help me?</p></div><div id="question-tags" class="tags-container tags">ack rwin tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '12, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/b98b1d62aa0a004fdd0907fdc3825043?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BlueArcher&#39;s gravatar image" /><p>BlueArcher<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BlueArcher has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11972" class="comments-container"></div><div id="comment-tools-11972" class="comment-tools"></div><div class="clear"></div><div id="comment-11972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11974"></span>

<div id="answer-container-11974" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11974-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is normal behavior. The fact that there is not an ACK for every packet is because Delayed ACK has been enabled. RFC 1122 says that there SHOULD be an ACK for at least every second segment, and this is the most commonly seen behavior. However, the use of SHOULD means that an implementation can disregard that recommendation if desired, so you will sometimes see ACKs less often than every two segments.</p><p>There is no real performance problem with ACKing every two packets, rather than less often. If the data flow is bidirectional, the ACKs will piggyback on data packets. If the data flow is unidirectional, there is no data flowing in the direction of the ACK packets, so the empty ACK packets are not contending with data packets for use of the wire.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '12, 13:47</p></div></div><div id="comments-container-11974" class="comments-container"><span id="11976"></span><div id="comment-11976" class="comment"><div id="post-11976-score" class="comment-score"></div><div class="comment-text"><p>I guess I am confused because I expect the RWIN to determine when an ACK is sent? Without scaling, every 65 KB an ACK would be sent vs this case of every 4 KB. It seems like this is a very inefficient way to transmit data over higher latency because you are waiting on the ACKs before sending more data.</p><p>Or are you saying that the ACKs are sent independently of the incoming data stream? I.E. the sending machine is not sending 2 segments and then waiting for an ACK.</p></div><div id="comment-11976-info" class="comment-info"><span class="comment-age">(15 Jun '12, 14:04)</span> BlueArcher</div></div><span id="11977"></span><div id="comment-11977" class="comment"><div id="post-11977-score" class="comment-score"></div><div class="comment-text"><p>To further my question, how can I determine why the transfer is only running at 26 KBps over what should be 8-12 Mbps of available bandwidth? The high ACK rate was my only lead :)</p></div><div id="comment-11977-info" class="comment-info"><span class="comment-age">(15 Jun '12, 14:08)</span> BlueArcher</div></div><span id="11979"></span><div id="comment-11979" class="comment"><div id="post-11979-score" class="comment-score"></div><div class="comment-text"><p>RWIN does not determine when ACKs are sent. RWIN determines how much data can be unacknowledged at any given time. The receiver is sending ACKs every two packets, but the sender is not waiting for the ACKs before sending more data. The sender is sending continuously.</p><p>If the receiver waited until RWIN bytes were sent before responding with an ACK, then the sender would have to pause until the ACK was received. Because of the frequent ACKs, the sender never has to pause, because it is constantly informed that there is room in the receive buffer of the receiving system.</p></div><div id="comment-11979-info" class="comment-info"><span class="comment-age">(15 Jun '12, 14:24)</span> Jim Aragon</div></div><span id="11982"></span><div id="comment-11982" class="comment"><div id="post-11982-score" class="comment-score"></div><div class="comment-text"><p>Thank you sir!</p></div><div id="comment-11982-info" class="comment-info"><span class="comment-age">(15 Jun '12, 15:46)</span> BlueArcher</div></div></div><div id="comment-tools-11974" class="comment-tools"></div><div class="clear"></div><div id="comment-11974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

