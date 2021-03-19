+++
type = "question"
title = "Suspected retransmission with differently sized segment"
description = '''Is TCP allowed to retransmit, using a segment that is different (larger) from the original segment? From a Wireshark capture I see a TCP segment which presumably is not ACK:ed within time so a retransmission  is made but this time with a slightly larger payload?!? Both segments are ACK:ed separetly ...'''
date = "2013-12-01T12:46:00Z"
lastmod = "2013-12-02T10:32:00Z"
weight = 27617
keywords = [ "retransmissions", "tcp", "size" ]
aliases = [ "/questions/27617" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Suspected retransmission with differently sized segment](/questions/27617/suspected-retransmission-with-differently-sized-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27617-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is TCP allowed to retransmit, using a segment that is different (larger) from the original segment?</p><p>From a Wireshark capture I see a TCP segment which presumably is not ACK:ed within time so a retransmission is made but this time with a slightly larger payload?!? Both segments are ACK:ed separetly (one with SACK). I'm pretty sure that it is only the larger packet that is picked up at the application layer. What may be the cause of this?</p><pre><code>Time         From    To      Info  
yy26.720721, xx.46 , xx.202, [PSH, ACK] Seq=206 Ack=25 Win=63733 Len=29  
yy26.720767, xx.202, xx.46 , [PSH, ACK] Seq=25 Ack=235 Win=64615 Len=26  
yy26.925563, xx.202, xx.46 , [TCP Retransmission][PSH, ACK] Seq=25 Ack=235 Win=64615 Len=64  
yy26.925802, xx.46 , xx.202, [ACK] Seq=235 Ack=89 Win=63669 Len=0 SLE=25 SRE=51  
yy27.220114, xx.46 , xx.202, [PSH, ACK] Seq=235 Ack=89 Win=63669 Len=1</code></pre></div><div id="question-tags" class="tags-container tags">retransmissions tcp size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/ea560e87377fa949e68cacf774b5327f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssh9614&#39;s gravatar image" /><p>ssh9614<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssh9614 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 09:55</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-27617" class="comments-container"></div><div id="comment-tools-27617" class="comment-tools"></div><div class="clear"></div><div id="comment-27617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27668"></span>

<div id="answer-container-27668" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27668-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My answer:</p><p>The TCP data length in a retransmitted TCP segment can certainly be larger than in the originally transmitted TCP segment.</p><p>Think of it this way: The sending application adds more data to the TCP send buffer between the first transmission and the retransmission and thus more data is available to be sent in the retransmission.</p><p>The receiving TCP stack is responsible for properly re-constructing the data stream (handling data received twice &amp; etc) before passing the data to the receiving application.</p><p>One slightly interesting note: The window size advertised by the receiver (xx.46) is reduced by 64 to 63669 and remains at that value in the two acks thus suggesting that the receiving application (xx.46) has not yet read the data from the receive TCP buffer by the end of the sequence shown.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-27668" class="comments-container"></div><div id="comment-tools-27668" class="comment-tools"></div><div class="clear"></div><div id="comment-27668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

