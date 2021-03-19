+++
type = "question"
title = "Understanding HTTP Packet Data"
description = '''I am trying to understand how the acknowledgment number is generated. I thought it was the sequence number + the length. Could someone please explain this to me? The first packet is my computer as the source, and it alternates from there. Image: https://ibb.co/miHFUk'''
date = "2017-07-23T11:52:00Z"
lastmod = "2017-07-23T12:53:00Z"
weight = 63016
keywords = [ "acknowledgement" ]
aliases = [ "/questions/63016" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding HTTP Packet Data](/questions/63016/understanding-http-packet-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to understand how the acknowledgment number is generated. I thought it was the sequence number + the length. Could someone please explain this to me? The first packet is my computer as the source, and it alternates from there. Image: <a href="https://ibb.co/miHFUk">https://ibb.co/miHFUk</a></p></div><div id="question-tags" class="tags-container tags">acknowledgement</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '17, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/3962b2c1048cf6eda0cdbe8ad3434562?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="droidus&#39;s gravatar image" /><p>droidus<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="droidus has no accepted answers">0%</span></p></div></div><div id="comments-container-63016" class="comments-container"></div><div id="comment-tools-63016" class="comment-tools"></div><div class="clear"></div><div id="comment-63016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63021"></span>

<div id="answer-container-63021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63021-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your understanding is correct, but your <code>Length</code> column doesn't show the size of the TCP payload alone but most likely the size of the whole frame including Ethernet, IP and TCP layer. Seq numbers only reflect the TCP payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '17, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63021" class="comments-container"><span id="63028"></span><div id="comment-63028" class="comment"><div id="post-63028-score" class="comment-score"></div><div class="comment-text"><p>Is there any way to show the TCP payload alone?</p></div><div id="comment-63028-info" class="comment-info"><span class="comment-age">(23 Jul '17, 15:45)</span> droidus</div></div><span id="63030"></span><div id="comment-63030" class="comment"><div id="post-63030-score" class="comment-score"></div><div class="comment-text"><p>Right click on one of the TCP data packets and choose follow TCP stream. A new window will pop up containing the TCP data.</p></div><div id="comment-63030-info" class="comment-info"><span class="comment-age">(23 Jul '17, 21:14)</span> Uli</div></div></div><div id="comment-tools-63021" class="comment-tools"></div><div class="clear"></div><div id="comment-63021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63023"></span>

<div id="answer-container-63023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The ACK-Number in TCP is used to acknowledge received data from the sender:</p><ul><li>A send B 100 Bytes of data with sequence number 1000</li><li>B receives this data and acknowledge this with sending a packet with ACK number 1100</li><li>A send further 100 Bytes (now with sequence number 1100)</li><li>B receives the second packet and acknowledge this with ACK number 1200</li></ul><p>However for data from B to A the sequence and acknowledge numbers for this direction is independent of A -&gt; B.</p><p>Now to real live:</p><ul><li>A can send more TCP data packets in a row without waiting for the acknowledgement. (Data packet 1 with seq 1000 and 100 Bytes; data packet 2 with seq 1100 and 100 Bytes data; data packet 3 with seq 1200 and 100 Bytes data, etc)</li><li>B acknowledge not every packet on its on. It can summarize the acknowledgement. (B send packet with ACK number 1300 for data packet 1, 2 and 3)</li><li>The frequency of ACKs depends of the implementation of the TCP stack, the received packets (e.g. A send B a packet with PSH bit set) and features like "Delayed ACK" etc.</li></ul><p>Pakets with SYN or FIN bits set are acknowledged by incrementing the received sequence number by 1 (A-&gt;B SYN with seq 100 =&gt; B-&gt;A SYN/ACK with seq 3200 and ack 101 =&gt; A-&gt;B ACK with seq 101 and ack 3201).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '17, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-63023" class="comments-container"></div><div id="comment-tools-63023" class="comment-tools"></div><div class="clear"></div><div id="comment-63023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

