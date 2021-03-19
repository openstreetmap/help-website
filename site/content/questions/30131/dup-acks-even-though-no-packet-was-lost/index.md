+++
type = "question"
title = "DUP ACKs even though no packet was lost"
description = '''I have two network devices involved in this wireshark capture  the embedded device, 10.222.156.120 the server, 10.222.156.1, which is a Java application on an Ubuntu 12.04 64 bit machine  The capture is done on the server. The embedded device connects to the server and starts sending data. The serve...'''
date = "2014-02-24T07:55:00Z"
lastmod = "2014-02-24T09:23:00Z"
weight = 30131
keywords = [ "dup-ack", "retransmissions", "wireshark" ]
aliases = [ "/questions/30131" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [DUP ACKs even though no packet was lost](/questions/30131/dup-acks-even-though-no-packet-was-lost)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30131-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two network devices involved in this <a href="http://www.cloudshark.org/captures/1d1c1dcdf9bf">wireshark capture</a></p><ul><li>the embedded device, 10.222.156.120</li><li>the server, 10.222.156.1, which is a Java application on an Ubuntu 12.04 64 bit machine</li></ul><p>The capture is done on the server.</p><p>The embedded device connects to the server and starts sending data. The server never sends anything.</p><p>Everything goes well until packet #108 is sent. The server now starts sending DUP ACKs and does not even stop when a fast retransmission og packet #109 is sent by the embedded device.</p><p>As far as I can see, no packet was lost. I believe this because the capture was done on the server (using tcpdump).</p><p>What can be the cause of the DUP ACKs?</p></div><div id="question-tags" class="tags-container tags">dup-ack retransmissions wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '14, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/2e5c0360a6c4fbf91bd6d7ef647e5cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="colorcoded&#39;s gravatar image" /><p>colorcoded<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="colorcoded has no accepted answers">0%</span></p></div></div><div id="comments-container-30131" class="comments-container"></div><div id="comment-tools-30131" class="comment-tools"></div><div class="clear"></div><div id="comment-30131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30135"></span>

<div id="answer-container-30135" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30135-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>The tcp.checksum of tcp.seq==76234 is invalid in packets 109 and 122 so the receiving TCP validly discards those. Only the timer based retransmission in packet number 135 if correct which is when linux acknowledges the segment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '14, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Feb '14, 11:39</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-30135" class="comments-container"><span id="30167"></span><div id="comment-30167" class="comment"><div id="post-30167-score" class="comment-score"></div><div class="comment-text"><p>Thank you! You just helped me find a hard bug in my embedded system.</p></div><div id="comment-30167-info" class="comment-info"><span class="comment-age">(24 Feb '14, 23:54)</span> colorcoded</div></div></div><div id="comment-tools-30135" class="comment-tools"></div><div class="clear"></div><div id="comment-30135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

