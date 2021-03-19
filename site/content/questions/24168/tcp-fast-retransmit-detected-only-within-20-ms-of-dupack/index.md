+++
type = "question"
title = "TCP Fast Retransmit detected only within 20 ms of DupACK"
description = '''Hi, TCP Fast Retransmit detection is explained as: / If there were &amp;gt;=2 duplicate ACKs in the reverse direction (there might be duplicate acks missing from the trace) and if this sequence number matches those ACKs and if the packet occurs within 20ms of the last duplicate ack then this is a fast r...'''
date = "2013-08-29T08:53:00Z"
lastmod = "2013-08-29T10:05:00Z"
weight = 24168
keywords = [ "fast", "dupack", "retransmission", "tcp" ]
aliases = [ "/questions/24168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Fast Retransmit detected only within 20 ms of DupACK](/questions/24168/tcp-fast-retransmit-detected-only-within-20-ms-of-dupack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>TCP Fast Retransmit detection is explained as:</p><p>/ <em>If there were &gt;=2 duplicate ACKs in the reverse direction (there might be duplicate acks missing from the trace) and if this sequence number matches those ACKs and if the packet occurs within 20ms of the last duplicate ack then this is a fast retransmission</em> /</p><p>Why does the retransmitted packet have to occur within 20 ms of DUPACK? If you collect a trace on the sender, I could see this work, but in a receiver trace, or a trace from the network core, Fast Retransmit'ed packet can occur well after 20 ms of DUPACK.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">fast dupack retransmission tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/72478c24289d27d3471f91b0c40f622b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="instalater&#39;s gravatar image" /><p>instalater<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="instalater has no accepted answers">0%</span></p></div></div><div id="comments-container-24168" class="comments-container"></div><div id="comment-tools-24168" class="comment-tools"></div><div class="clear"></div><div id="comment-24168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24171"></span>

<div id="answer-container-24171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24171-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a somewhat arbitrary value that is hard-coded into Wireshark to try to distinguish between Receive Time Out (RTO) retransmissions and Fast Retransmissions. There isn't really a reliable way for Wireshark to determine what triggered a retransmission, so it's possible for Wireshark to mis-identify the type of retransmission. It's also possible for Wireshark to mis-identify out-of-order packets as retransmissions.</p><p>You're right that a Fast Retransmission can show up more than 20 ms after the Duplicate ACK that triggered the retransmission. Normally, data would still be flowing, and Duplicate ACKs would keep being generated, so the retransmission would usually be within 20 ms of <em>a</em> Duplicate ACK, although not necessarily <em>the</em> Duplicate ACK that triggered the Fast Retransmission. This would not be true if the lost packet was near the end of the data stream and data has stopped flowing.</p><p>It's also possible that Duplicate ACKs are being generated and showing up in the Wireshark trace, but are not making it to the sender due to some network problem. The sender will eventually send a RTO retransmission, but Wireshark will identify it as a Fast Retransmission due to the Duplicate ACKs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '13, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-24171" class="comments-container"></div><div id="comment-tools-24171" class="comment-tools"></div><div class="clear"></div><div id="comment-24171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

