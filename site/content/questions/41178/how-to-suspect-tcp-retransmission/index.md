+++
type = "question"
title = "How to suspect TCP Retransmission"
description = '''WireShark displays &quot;This frame is a (suspected) retransmission&quot;. But if I apply filter with same seq num such as &quot;tcp.seq == 1199864719&quot;, I could see only one packet for that seq num. So I want to know how to suspect TCP restansmission on Wireshark. Best Regards, Dennis Nam'''
date = "2015-04-03T09:01:00Z"
lastmod = "2015-04-03T10:02:00Z"
weight = 41178
keywords = [ "retransmission", "tcp" ]
aliases = [ "/questions/41178" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to suspect TCP Retransmission](/questions/41178/how-to-suspect-tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>WireShark displays "This frame is a (suspected) retransmission". But if I apply filter with same seq num such as "tcp.seq == 1199864719", I could see only one packet for that seq num.</p><p>So I want to know how to suspect TCP restansmission on Wireshark.</p><p>Best Regards, Dennis Nam</p></div><div id="question-tags" class="tags-container tags">retransmission tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '15, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/074a371c25b457347c4bef7337ac0979?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dennis%20Nam&#39;s gravatar image" /><p>Dennis Nam<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dennis Nam has no accepted answers">0%</span></p></div></div><div id="comments-container-41178" class="comments-container"></div><div id="comment-tools-41178" class="comment-tools"></div><div class="clear"></div><div id="comment-41178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41179"></span>

<div id="answer-container-41179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41179-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on where you are capturing in relation to the point of packet loss (upstream or downstream). It is normal to see the sequence number only once if you are capturing downstream from the point of packet loss.</p><p>If you are capturing upstream from the point of packet loss--packets are being dropped <em>after</em> they pass your capture point--then Wireshark will see both the original packet and the retranmission and it will be clear that the second one is a retransmission. In this case, you will see the expected sequence number twice.</p><p>If you are capturing downstream from the point of packet loss--packets are being dropped <em>before</em> they pass your capture point--then Wireshark will only see the retransmission. In this case, there will be a gap in the sequence numbers, Wireshark's expert will say "Previous segment not captured," and then the expected packet will show up later. In this case, you will see the expected sequence number only once.</p><p>Unfortunately, out-of-order packets look exactly the same as retransmissions where you are downstream from the point of packet loss: There is a gap in the sequence numbers and the packet shows up later than expected. Wireshark has to try to distinguish between out-of-order packets and retransmissions.</p><p>In Wireshark versions up to and including 1.10.x, Wireshark will identify the packet as an out-of-order packet if it appears within 3 ms of where it should have been, and will identify it as a retransmission if it appears more than 3 ms from where it should have been. This is a hard-coded number, and Wireshark can mis-identify out-of-order packets as retransmissions and vice-versa.</p><p>Beginning with Wireshark 1.12.x, if the TCP three-way handshake is present in the trace, Wireshark will calculate the initial round-trip time and compare to that instead of to 3 ms. If the three-way handshake is not present, then Wireshark will use the 3-ms rule.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '15, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-41179" class="comments-container"><span id="45794"></span><div id="comment-45794" class="comment"><div id="post-45794-score" class="comment-score"></div><div class="comment-text"><p>Thank you, that information was very useful!</p></div><div id="comment-45794-info" class="comment-info"><span class="comment-age">(11 Sep '15, 08:46)</span> BrunoF</div></div></div><div id="comment-tools-41179" class="comment-tools"></div><div class="clear"></div><div id="comment-41179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

