+++
type = "question"
title = "TCP Out-of-order VS Retransmission"
description = '''I&#x27;ve got a situation where there appears to be timeouts on the client side. I&#x27;ve zeroed in on a sample, but I see this multiple places. The dialog is going fine and the client sends 67 bytes of data in #1478 and the host is ACKs in #1479. The client then sends the same sequence packet as it did in #...'''
date = "2011-03-25T13:33:00Z"
lastmod = "2011-03-25T16:08:00Z"
weight = 3131
keywords = [ "ack", "out-of-order" ]
aliases = [ "/questions/3131" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Out-of-order VS Retransmission](/questions/3131/tcp-out-of-order-vs-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3131-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got a situation where there appears to be timeouts on the client side. I've zeroed in on a sample, but I see this multiple places. The dialog is going fine and the client sends 67 bytes of data in #1478 and the host is ACKs in #1479. The client then sends the same sequence packet as it did in #1478, but the data is larger. In fact, it contains everything #1478 did, plus the next block of data it was to send. This was reported as a TCP Out-of-order as opposed to a retransmission.<br />
</p><ol><li><p>Is this considered an out-of-order because the second packet was different in its data portion (seq and ack were the same)?</p></li><li><p>Am I reading this correctly that the client never saw the ACK in #1479? It was 27 seconds before the out-of-order packet came in that duplicated the data in #1478. It seems like if the client did not get the ACK it it would have retransmitted earlier.</p></li><li><p>Is it normal to see the same packet sequence number sent with additional data? I guess this can only happen when an ack is dropped and in the meantime additional data was written right?</p></li></ol><p>start of edit on 3/28 &gt;&gt;&gt;</p><p>4) Assuming the ACK in #1479 was dropped caused the retransmission, albiet with additional data, to happen in #1480, what can be learned from the fact that the retransmission was 27 seconds later? Shouldn't the retransmission have happened (with or without subsequent data) every half second or so?<br />
</p><p>Some additional information, that second set of data that was appended was a new request to the host and could have have been sent any number of seconds later. I am envisioning a problem on the client side of the network and then, with the additional data being added somehow clearing up the problem and allowing the larger frame through a faulty wireless AP or router?</p><p>&lt;&lt;&lt; end of edit on 3/28</p><p>Thanks for any insights!</p><p>(5101 is the host)</p><p>No. Time Source Destination Protocol Info</p><p>1474 11:33:11.197 200.10.10.147 200.10.10.33 TCP 1061 &gt; 5101 [PSH, ACK] Seq=657606914 Ack=3891546886 Win=32220 Len=255</p><p>1475 11:33:11.258 200.10.10.33 200.10.10.147 TCP 5101 &gt; 1061 [PSH, ACK] Seq=3891546886 Ack=657607169 Win=65213 Len=39</p><p>1476 11:33:11.462 200.10.10.147 200.10.10.33 TCP 1061 &gt; 5101 [ACK] Seq=657607169 Ack=3891546925 Win=32181 Len=0</p><p>1477 11:33:11.462 200.10.10.33 200.10.10.147 TCP 5101 &gt; 1061 [PSH, ACK] Seq=3891546925 Ack=657607169 Win=65213 Len=213</p><p>1478 11:33:11.483 200.10.10.147 200.10.10.33 TCP 1061 &gt; 5101 [PSH, ACK] Seq=657607169 Ack=3891547138 Win=31968 Len=67</p><p>1479 11:33:11.615 200.10.10.33 200.10.10.147 TCP 5101 &gt; 1061 [ACK] Seq=3891547138 Ack=657607236 Win=65146 Len=0</p><p>1480 11:33:38.671 200.10.10.147 200.10.10.33 TCP [TCP Out-Of-Order] 1061 &gt; 5101 [PSH, ACK] Seq=657607169 Ack=3891547138 Win=31968 Len=350</p><p>1481 11:33:38.729 200.10.10.33 200.10.10.147 TCP 5101 &gt; 1061 [PSH, ACK] Seq=3891547138 Ack=657607519 Win=65535 Len=39</p><p>1482 11:33:38.871 200.10.10.147 200.10.10.33 TCP [TCP Previous segment lost] 1061 &gt; 5101 [ACK] Seq=657607519 Ack=3891547177 Win=31929 Len=0</p><p>1483 11:33:38.947 200.10.10.33 200.10.10.147 TCP 5101 &gt; 1061 [PSH, ACK] Seq=3891547177 Ack=657607519 Win=65535 Len=204</p><p>1484 11:33:39.073 200.10.10.147 200.10.10.33 TCP 1061 &gt; 5101 [ACK] Seq=657607519 Ack=3891547381 Win=31725 Len=0</p><p>1485 11:33:57.861 200.10.10.147 200.10.10.33 TCP [TCP Dup ACK 1484#1] 1061 &gt; 5101 [ACK] Seq=657607519 Ack=3891547381 Win=31725 Len=0</p></div><div id="question-tags" class="tags-container tags">ack out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '11, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/96f54c80d7829218b63d145864a91eab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="motdc&#39;s gravatar image" /><p>motdc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="motdc has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Mar '11, 06:54</p></div></div><div id="comments-container-3131" class="comments-container"></div><div id="comment-tools-3131" class="comment-tools"></div><div class="clear"></div><div id="comment-3131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3132"></span>

<div id="answer-container-3132" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3132-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For (1): this problem was actually just fixed in Wireshark yesterday (rev 36323). You can pick up an automated build (with that rev or higher) to check it out; now Wireshark will only call it a retransmission instead of out-of-order.</p><p>For (2): Yes, that seems like it is the case.</p><p>For (3): I saw it once years ago too, so I suppose it's relatively normal (but I definitely not a TCP expert).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-3132" class="comments-container"><span id="3173"></span><div id="comment-3173" class="comment"><div id="post-3173-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info that it was just fixed! I'll have to download it today.</p></div><div id="comment-3173-info" class="comment-info"><span class="comment-age">(28 Mar '11, 05:43)</span> motdc</div></div></div><div id="comment-tools-3132" class="comment-tools"></div><div class="clear"></div><div id="comment-3132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3133"></span>

<div id="answer-container-3133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3133-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes to #3. TCP is a stream based protocol. So instead of just retransmitting what went missing, it will try to take the full load of data if available. So the SEQ# demarcs the <em>start</em> of the segment. The fact that it has additional payload doesn't change the start of the segment. Only the TCP LEN changes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-3133" class="comments-container"><span id="3174"></span><div id="comment-3174" class="comment"><div id="post-3174-score" class="comment-score"></div><div class="comment-text"><p>I can see how the second frame received from the client would have a superset of the data in the case of a lost ACK. What troubles me is that 27 seconds had passed betwwen the first and second frame. If the ACK were dropped then the client would be retransimitting (both before and after the next set of data was appended) every 1/2 second. That still seems fishy to me.</p></div><div id="comment-3174-info" class="comment-info"><span class="comment-age">(28 Mar '11, 05:50)</span> motdc</div></div><span id="3192"></span><div id="comment-3192" class="comment"><div id="post-3192-score" class="comment-score">1</div><div class="comment-text"><p>It's hard to follow your text output - not dedicated enough to follow it via txt output! :) If the sender does not get an ack from the receiver, the RTO should trigger a retransmission. It shouldn't be 27 seconds, so I do agree that something fishy is going on. If the sender is not <em>that</em> busy, take a look at the IP ID to see if there is a sudden jump in the 27 second window. Perhaps it was retransmitting and you missed that as well. That would be one explanation.</p></div><div id="comment-3192-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:45)</span> hansangb</div></div></div><div id="comment-tools-3133" class="comment-tools"></div><div class="clear"></div><div id="comment-3133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

