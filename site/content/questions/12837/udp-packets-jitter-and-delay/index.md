+++
type = "question"
title = "UDP packets&#x27; jitter and delay"
description = '''Dear all,  I&#x27;m new in Wireshark and I would like to know if it&#x27;s possible to get the delay and jitter of UDP packets directly in WireShark. I saw many examples on Internet but they are all about RTP protocol.  Thank you in advance for your help. Best regards. '''
date = "2012-07-18T13:48:00Z"
lastmod = "2012-07-19T09:53:00Z"
weight = 12837
keywords = [ "delay", "udp", "jitter" ]
aliases = [ "/questions/12837" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [UDP packets' jitter and delay](/questions/12837/udp-packets-jitter-and-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12837-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all, I'm new in Wireshark and I would like to know if it's possible to get the delay and jitter of UDP packets directly in WireShark. I saw many examples on Internet but they are all about RTP protocol. Thank you in advance for your help. Best regards.</p></div><div id="question-tags" class="tags-container tags">delay udp jitter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '12, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/eb05e181ca9874c93fa5812b5f270959?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nezha&#39;s gravatar image" /><p>nezha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nezha has no accepted answers">0%</span></p></div></div><div id="comments-container-12837" class="comments-container"></div><div id="comment-tools-12837" class="comment-tools"></div><div class="clear"></div><div id="comment-12837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12861"></span>

<div id="answer-container-12861" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12861-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @Jaap said: Currently Wireshark can only calculate jitter for RTP, as nothing else is implemented. However, it would be possible to calculate UDP jitter.</p><p><strong>Explanation</strong><br />
In general you can calculate UDP jitter, however, to do it in the correct way, you would need two capture files. One in front of the client and one in front of the server to be able to calculate the transmission time (delay) and then the variation of delay (jitter). This is called <a href="http://en.wikipedia.org/wiki/Packet_delay_variation">Packet Delay Variation</a>.</p><p>The following link describes it in a nice way<br />
</p><blockquote><p><code>http://nms.lcs.mit.edu/~hari/papers/CS294/paper/node5.html</code><br />
</p></blockquote><p>Cite: "Jitter: The jitter of a packet stream is defined as the mean deviation of the difference in packet spacing at the receiver compared to the sender, for a pair of packets...."</p><p>Basically, you could do it with one capture file as well, if you accept the time delta between two frame timestamps (in a capture file) to be the variation of network delay. However that's not really correct.</p><ol><li>it does not take into account delays at the sender side (within the application)</li><li>a packet could take a different route and could arrive in front of another (earlier) packet.</li></ol><p><strong>This would void the calculation!</strong></p><p>If you don't care about this, you can calculate (a kind of) jitter as the variation of the frame timestamp delta (<code>frame.time_delta</code> or <code>frame.time_delta_displayed</code>). See link to shell script below.</p><p>With RTP it's much easier to calculate jitter, as every RTP packet carries a timestamp value (<code>rtp.timestamp</code>).</p><p>Search for 'Timestamp' in the following page:<br />
</p><blockquote><p><code>http://www.networksorcery.com/enp/protocol/rtp.htm</code><br />
</p></blockquote><p>With that timestamp it is possible to calculate jitter with only one capture file, as you can calculate the time delta between two RTP packets and use the timestamp within those packets as a reference for "out of order packets" and "delay at the sender" (basically!).</p><p>See <a href="http://wiki.wireshark.org/RTP_statistics">How jitter is calculated</a> in the Wireshark RTP Wiki and the following link.</p><p>Search for "jitter estimator formula": <code>http://toncar.cz/Tutorials/VoIP/VoIP_Basics_Jitter.html</code><br />
</p><p>There are tools for UDP jitter measurement.</p><ul><li>iperf (<a href="http://code.google.com/p/xjperf/">xjperf</a>) does it's own measurement. It does <strong>not</strong> need a capture file..</li><li>There is another approach that uses <a href="http://babilonline.blogspot.de/2008/05/jitter.html">shell scripting and <strong>tshark</strong></a>.</li></ul><p><del>So basically, one could implement "UDP jitter" calculation in Wireshark, if the problem described above (delay at sender, out of order packet arrival) is simply ignored or accepted. This could be done as a TAP, similar to the RTP statistics TAP. <strong>Volunteers are welcome</strong> ;-)</del></p><p><strong>UPDATE:</strong> Thinking again about the possibility to calculate UDP jitter with just one capture file, I come to the conclusion, that it's <strong>NOT possible</strong> to get any <strong>usable values</strong>. So, you can't just ignore or accept the problem I mentioned above, as the error rate would be unknown, which makes the data useless.</p><p><strong>Reason</strong>: If you measure only at one side, you are measuring a mix of delay at the sender and delay in the network.</p><pre><code>      Sender                     Network           Receiver
p(1): ts(1)                       dn(1)            tr(1)
p(2): ts(2) = ts(1) + ds(2)       dn(2)            tr(2)
p(3): ts(3) = ts(2) + ds(3)       dn(3)            tr(3)

p = packet 1,2,3,...
ts = send time at sender
tr = receive time at receiver
dn = delay in the network

Delay:  tr(2) - tr(1) = [ts(2) + dn(2)] - [ts(1) + dn(1)]
                      = [ts(1) + ds(2) + dn(2)] - [ts(1) + dn(1)] 
                      = ds(2) + [dn(2) - dn(1)]
                      = ds(2) + [&quot;variation network delay&quot;]
</code></pre><p>So, what you are measuring is actually the sum of delay at the sender (ds - delay in the stack, the application, etc.) and the variation in delay on the network (dn(2) - dn(1)). Actually you are just interested in the variation of network delay (jitter). The delay at the sender (ds) could well be much higher than the variation of delay in the network (d(n+1) - d(n)), so you can only use that value if the delay at the sender (ds) is zero. Hoewever, that is something you cannot assume.</p><p><strong>Conclusion:</strong> To calculate UDP jitter, you need either two capture files (as I mentioned in the first place) or timestamps in the packet, which is not the case for standard UDP. The other option is to actively measure it with a tool like xjperf.</p><p>Sorry for my confusion about the "one capture file theory". One should always do the math and not rely on the stomach ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '12, 00:50</p></div></div><div id="comments-container-12861" class="comments-container"><span id="12867"></span><div id="comment-12867" class="comment"><div id="post-12867-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for your reply. So, if I have understood correctly, I can calculate the jitter by myself( using two .pcap files, one from the sender and the second from the receiver); I can also use a shell script where I enter the .pcap file or the xjperf tool. Can I ask an other question please: if I use the shell code, how can this sript calculate the jitter since we enter only the pcap file from the receiver side, it needs also the information about transmission times to find the delay and then the jitter of each packet? Thank you very much.</p></div><div id="comment-12867-info" class="comment-info"><span class="comment-age">(19 Jul '12, 14:59)</span> nezha</div></div><span id="12868"></span><div id="comment-12868" class="comment"><div id="post-12868-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I can calculate the jitter by myself( using two .pcap files, one from the sender and the second from the receiver);</p></blockquote><p>Yes, this is the only way to do it right (correct calculation). You need to calculate the delay (transmission time) for each packt. That is: delay = timestamp_sender - timestamp_receiver. HINT: The time source of both capture machines need to be synchronized to the same base (e.g. with NTP). Then calculate the variation of delay.</p><blockquote><p>I can also use a shell script where I enter the .pcap file or the xjperf tool.</p></blockquote><p>xjperf measures the jitter of its own UDP test packets. So this is an active test of a connection with test data sent over a link.</p><blockquote><p>if I use the shell code, how can this sript calculate the jitter since we enter only the pcap file from the receiver side, it needs also the information about transmission times to find the delay and then the jitter of each packet?</p></blockquote><p>That's correct and you get the real transmission times only by using two capture files!</p><p>HOWEVER, if you can assume, that there is a constant stream of packets, without much delay in the sender application and without "out of order" arrival, then the difference between the arrival time of packet n and the arrival time of n+1 can be used as a rough estimation of the transmission time. That's how the shell script (link above) works. It's not 100% correct, but a good estimation and better than nothing, if you have only one capture file ;-)</p></div><div id="comment-12868-info" class="comment-info"><span class="comment-age">(19 Jul '12, 16:00)</span> Kurt Knochner ♦</div></div><span id="12876"></span><div id="comment-12876" class="comment"><div id="post-12876-score" class="comment-score"></div><div class="comment-text"><p>see my UPDATE in the answer!</p></div><div id="comment-12876-info" class="comment-info"><span class="comment-age">(19 Jul '12, 23:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12861" class="comment-tools"></div><div class="clear"></div><div id="comment-12861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12854"></span>

<div id="answer-container-12854" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12854-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>UDP has no delay or jitter, since it has no notion of time or sequence. That's what RTP is about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-12854" class="comments-container"></div><div id="comment-tools-12854" class="comment-tools"></div><div class="clear"></div><div id="comment-12854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

