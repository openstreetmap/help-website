+++
type = "question"
title = "Delayed ACK"
description = '''Normally when looking through packet captures I link the packets by the ACK and SEQ numbers. However if Delayed ACK is enabled am I right in thinking that you might see every ACK from the sender as the sender my send an ACK that might acknowledge multiple packets ? In short my question is what consi...'''
date = "2014-08-12T01:30:00Z"
lastmod = "2014-08-12T09:50:00Z"
weight = 35427
keywords = [ "tcp_delayed_ack" ]
aliases = [ "/questions/35427" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Delayed ACK](/questions/35427/delayed-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35427-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Normally when looking through packet captures I link the packets by the ACK and SEQ numbers. However if Delayed ACK is enabled am I right in thinking that you might see every ACK from the sender as the sender my send an ACK that might acknowledge multiple packets ?</p><p>In short my question is what considerations must be taking when dealing with packet captures containing traffic that use the delayed ACK technique.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">tcp_delayed_ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '14, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div></div><div id="comments-container-35427" class="comments-container"></div><div id="comment-tools-35427" class="comment-tools"></div><div class="clear"></div><div id="comment-35427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35435"></span>

<div id="answer-container-35435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35435-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just keep in mind that acknowledgements are cumulative. An ACK number of 10,000, for example, means "I have received all data through byte 9,999, and I expect 10,000 next."</p><p>You could add the field tcp.analysis.acks_frame as a custom column. Wireshark will then tell you exactly which data packet an ACK packet is acknowledging. Again, this is cumulative, so the ACK includes all previous data packets from that same host on the same TCP connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '14, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-35435" class="comments-container"><span id="35437"></span><div id="comment-35437" class="comment"><div id="post-35437-score" class="comment-score"></div><div class="comment-text"><p>Thanks. So without delayed ACK I should see an ACK for each segment. With delayed ACK I will not and as you mentioned multiple segments can be acknowledged via a single (cumulative) ACK ?</p></div><div id="comment-35437-info" class="comment-info"><span class="comment-age">(12 Aug '14, 11:34)</span> bart80</div></div></div><div id="comment-tools-35435" class="comment-tools"></div><div class="clear"></div><div id="comment-35435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

