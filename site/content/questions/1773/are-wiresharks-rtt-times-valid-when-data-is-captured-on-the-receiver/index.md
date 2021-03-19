+++
type = "question"
title = "Are Wireshark&#x27;s RTT Times Valid When Data is Captured on the Receiver?"
description = '''How does Wireshark calculate the round-trip times used in the TCP Stream Graph &amp;gt; Round Trip Time Graph? Am I correct in thinking that Wireshark calculates the round-trip time by taking the difference between the time stamp of the data packet and the time stamp of the corresponding ACK packet, as ...'''
date = "2011-01-17T12:10:00Z"
lastmod = "2012-04-09T07:38:00Z"
weight = 1773
keywords = [ "rtt" ]
aliases = [ "/questions/1773" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are Wireshark's RTT Times Valid When Data is Captured on the Receiver?](/questions/1773/are-wiresharks-rtt-times-valid-when-data-is-captured-on-the-receiver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1773-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Wireshark calculate the round-trip times used in the TCP Stream Graph &gt; Round Trip Time Graph? Am I correct in thinking that Wireshark calculates the round-trip time by taking the difference between the time stamp of the data packet and the time stamp of the corresponding ACK packet, as seen by the Wireshark system that is doing the capturing? If so, wouldn't that mean that the round-trip time graph is pretty much meaningless if the capture is done on the client and the client is the data receiver?</p><p>We have four times:</p><p>Time 1: The data packet is transmitted by the server.</p><p>Time 2: The data packet is received by the client.</p><p>Time 3: The ACK is transmitted by the client.</p><p>Time 4: The ACK is received by the server.</p><p>The true round-trip time is the difference between time 1 and time 4. If we're capturing on the client, we see only time 2 and time 3. The difference between these two times represents the client response latency, not the round-trip time.</p><p>I find the Round Trip Time Graph to be useful. I want to make sure I'm not using it when it's not showing me valid data.</p><p>So, am I correct in thinking that the Round Trip Time Graph is only meaningful when the traffic is captured at or near the sender, or does Wireshark have a different method for calculating the round-trip time?</p></div><div id="question-tags" class="tags-container tags">rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '11, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-1773" class="comments-container"></div><div id="comment-tools-1773" class="comment-tools"></div><div class="clear"></div><div id="comment-1773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9999"></span>

<div id="answer-container-9999" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9999-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess I'll answer my own question, after doing some research, since no one else did.</p><p>If you're looking at two packets, an initial packet of some sort and a response packet, the RTT is not accurate unless the packets are captured on or very near the sender of the initial packet. For example, a TCP data packet and the corresponding ACK packet, or a DNS query and the DNS response, or a DHCP DISCOVER and the corresponding DHCP OFFER. The farther you are from the sending machine, the more of the round-trip path is omitted from the RTT calculation.</p><p>However, as Jasper points out in <a href="http://ask.wireshark.org/questions/4210/measuring-round-trip-time">this post</a>, there is a special case for measuring the initial RTT of a TCP session when you capture all three packets of the TCP three-way handshake. In that case, the time difference between the SYN (first packet) and the ACK (third packet) of the three-way handshake includes all components of a round trip regardless of where the capturing device is placed. Of course, this technique only shows the initial RTT at the start of the TCP conversation. It does not allow you to calculate RTTs that occur later in the conversation, after the three-way handshake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '12, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9999" class="comments-container"></div><div id="comment-tools-9999" class="comment-tools"></div><div class="clear"></div><div id="comment-9999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10031"></span>

<div id="answer-container-10031" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10031-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's all about perspective and what you are trying to measure.</p><p>In any capture scenario, there are always 2 segments (for lack of a better word) over which packets traverse between client and server. The 1st segment is from client to capture point, and the 2nd is from capture point to server. RTT is calculated from the point at which Wireshark captures the data and yes, RTT is always valid (barring any bugs of course), but it's valid from the perspective of Wireshark, not from the perspective of the client (or server).</p><p>If you're trying to measure end-to-end RTT, then you need to capture as close to the client as possible. If, on the other hand, you are interested in determining server processing time, then you need to capture as close to the server as possible. Capture points lying somewhere in between client and server will yield RTT's also somewhere in between total RTT and server processing time. This may or may not be as useful to someone, but it all depends on what you trying to measure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '12, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-10031" class="comments-container"></div><div id="comment-tools-10031" class="comment-tools"></div><div class="clear"></div><div id="comment-10031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

