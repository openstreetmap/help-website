+++
type = "question"
title = "When is RTT calculated?"
description = '''When I look at a TCP connection I see that nearly every ACK packet is used to transmit data to the other side which is perfectly fine. So in theory every sent packet should get an ACK, right? So far so good. But why does Wireshark not calculate the RTT time for every ACK packet? Not that it looks wr...'''
date = "2014-06-21T15:31:00Z"
lastmod = "2014-06-21T17:05:00Z"
weight = 34017
keywords = [ "rtt" ]
aliases = [ "/questions/34017" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When is RTT calculated?](/questions/34017/when-is-rtt-calculated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34017-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I look at a TCP connection I see that nearly every ACK packet is used to transmit data to the other side which is perfectly fine. So in theory every sent packet should get an ACK, right? So far so good. But why does Wireshark not calculate the RTT time for every ACK packet? Not that it looks wrong, quite the opposite. But I would like to understand when Wireshark does calculate the RTT? Only for ACK packets with Len 0 (not always the case) or can it detect that multiple packets are ACKed by a delayed ACK?</p><p>Below is a typical ACK packet shown which should? have a calculated RTT time. Are RTT times in general useful or are they more confusing when Delayed ACKs are enabled for a socket? I am having a hard time to identify latency issues in the 200ms region where I have tons of 200ms RTT packets on some sockets. This makes it quite hard to identify latency issues in an application if high RTT times are so common.</p><p>A much more reliable sign of bad network are TCP Retransmits and Duplicate Acks. But RTT should be also helpful here.</p><pre><code>Transmission Control Protocol, Src Port: 8090 (8090), Dst Port: 9789 (9789), Seq: 2356870728, Ack: 991220798, Len: 1460
..
Flags: 0x010 (ACK)
...
SEQ/ACK analysis
Bytes in flight: 1460
No RTT???????????
Timestamps
Time since first frame in this TCP stream: 32.989695000 seconds
Time since previous frame in this TCP stream: 0.000314000 seconds</code></pre></div><div id="question-tags" class="tags-container tags">rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/9432d8dab23758894913ff56e3836f8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akraus1&#39;s gravatar image" /><p>akraus1<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akraus1 has no accepted answers">0%</span></p></div></div><div id="comments-container-34017" class="comments-container"></div><div id="comment-tools-34017" class="comment-tools"></div><div class="clear"></div><div id="comment-34017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34022"></span>

<div id="answer-container-34022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34022-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So in theory <strong>every sent packet</strong> should get an ACK, right?</p></blockquote><p>Actually, no. That's not the case. See the answer(s) to the following question for a brief explanation why: <a href="http://ask.wireshark.org/questions/33897/how-much-data-for-each-ack">http://ask.wireshark.org/questions/33897/how-much-data-for-each-ack</a></p><blockquote><p>But why does Wireshark <strong>not calculate the RTT</strong> time <strong>for every ACK</strong> packet?</p></blockquote><p>well, it <strong>does calculate</strong> the RTT for every 'valid' ACK, as far as I can see in the code (however: I did not look very thoroughly!).</p><blockquote><p>Only for ACK packets with Len 0 (not always the case)</p></blockquote><p>As I said: it calculates the RTT for every 'valid' ACK (not out-of order, not retransmission, etc.).</p><p>BTW: It's not the case, that Wireshark does <strong>not use</strong> the piggy-packed ACKs for RTT calculation. I have example captures, where you can see that. I guess, that in your example, the 'piggy-packed' ACK is for a frame that has been ACKed before. I can tell you for sure, if you post your capture file somewhere (google drive, dropbox, cloudshark.org).</p><blockquote><p>But RTT should be also helpful here.</p></blockquote><p>So, to answer your question: Yes, RTT values are helpful, but are only one piece of the puzzle.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '14, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34022" class="comments-container"><span id="34065"></span><div id="comment-34065" class="comment"><div id="post-34065-score" class="comment-score"></div><div class="comment-text"><p>Thanks for Kurt taking the time to give the right backgound.</p><pre><code>535 16.917983000    146.254.106.89  192.129.41.82   HTTP    986 Continuation or non-HTTP traffic
Transmission Control Protocol, Src Port: 44242 (44242), Dst Port: ctf (84), Seq: 3380, Ack: 1302, Len: 932

847 17.141959000    192.129.41.82   146.254.106.89  TCP 60  ctf &gt; 44242 [ACK] Seq=1302 Ack=**4312** Win=64768 Len=0
Transmission Control Protocol, Src Port: ctf (84), Dst Port: 44242 (44242), Seq: 1302, Ack: 4312, Len: 0

948 17.323640000    192.129.41.82   146.254.106.89  HTTP    1514    HTTP/1.1 200 OK [Unreassembled Packet]
Transmission Control Protocol, Src Port: ctf (84), Dst Port: 44242 (44242), Seq: 1302, Ack: **4312**, Len: 1460</code></pre><p>Packet <strong>535</strong> requests some http data from a server. The server Acks it in packet <strong>847</strong> 0,2s later which Wireshark correctly shows as RTT. Now the server sends more data with the same ACK number 4312 in packet <strong>948</strong> which shows no ACK number because this ACK number was already ACKed by our client. If we would calculate the RTT of this one we would end up with an RTT of over 400ms which is very suspicious but this includes the server processing time and not anything related to the TCP stack.</p><p>The reason why I was calculating this number is that I wrote a tool to calculate the RTT times of tcp packets on the fly without capturing the complete network traffic and only generating messages when the RTT reaches a certain threshold. To verify the numbers I have used Wireshark but my calculations were not correct all the time. TCP is quite complex after all but thanks to Wireshark I now have a pretty good understanding how TCP works.</p></div><div id="comment-34065-info" class="comment-info"><span class="comment-age">(23 Jun '14, 04:18)</span> akraus1</div></div><span id="34068"></span><div id="comment-34068" class="comment"><div id="post-34068-score" class="comment-score"></div><div class="comment-text"><blockquote><p>TCP is quite complex after all but thanks to Wireshark <strong>I now have a pretty good understanding how TCP works</strong>.</p></blockquote><p>Good!</p></div><div id="comment-34068-info" class="comment-info"><span class="comment-age">(23 Jun '14, 05:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34022" class="comment-tools"></div><div class="clear"></div><div id="comment-34022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

