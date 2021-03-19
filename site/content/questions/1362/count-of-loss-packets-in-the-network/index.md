+++
type = "question"
title = "count of loss packets in the network"
description = '''I´m using wireshark for study the traffic between a client and a server in my own machine. I study the traffic on the interface lo and after I study the traffic on the network (client and server in separate machines) on the interface eth0 I always see the conversations in stadistics for study the nu...'''
date = "2010-12-15T13:24:00Z"
lastmod = "2011-09-20T02:46:00Z"
weight = 1362
keywords = [ "count", "loss", "packets" ]
aliases = [ "/questions/1362" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [count of loss packets in the network](/questions/1362/count-of-loss-packets-in-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1362-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I´m using wireshark for study the traffic between a client and a server in my own machine. I study the traffic on the interface lo and after I study the traffic on the network (client and server in separate machines) on the interface eth0 I always see the conversations in stadistics for study the number of packets sent and received by client and server and I always obtain the same number for sent and received, I mean, I can´t see the number of loss packets in the network??Becuase I tried with putting loss packets and always obtain the same number for packets sents and for packets received..how can I see the number of loss packets??Because all packets server sent cannot arrive to the client...Maybe I´m doing something wrong or I don´t understand well how works wireshark??</p><p>Thank you very much for your help!</p></div><div id="question-tags" class="tags-container tags">count loss packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '10, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/fd9aa395fb6ce6af5ce9781541fa9357?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Susana26&#39;s gravatar image" /><p>Susana26<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Susana26 has no accepted answers">0%</span></p></div></div><div id="comments-container-1362" class="comments-container"><span id="1367"></span><div id="comment-1367" class="comment"><div id="post-1367-score" class="comment-score"></div><div class="comment-text"><p>If you captured on the sending and receiving hosts, you will see a difference in the number of packets. For example, if you're sending from A -&gt; B, and the loss is in the direction from A -&gt; B, and you're capturing on both, you'll see the packet leave A but never arrive at B. Are you capturing on both sides?</p></div><div id="comment-1367-info" class="comment-info"><span class="comment-age">(15 Dec '10, 15:34)</span> hansangb</div></div><span id="1370"></span><div id="comment-1370" class="comment"><div id="post-1370-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your replies. How I have to do to capture in both sides?I didn´t do anything more than start the capture and see the traffic that is in both sides.And in convewrsations I can see the traffic from A -&gt; B and from B-&gt;A and always the packets received is the same than the sent. Where I have to put that capture ib both sides?</p><p>What I´m doing is sending udp traffic between a client and a server. More send udp packets but there are much more traffic from the server becausae his always send a file divided in smaller packets. I don´t put any special to do the capture and I studied the packets sent and received in stadistics-&gt;conversations. But is what I don´t understand. For one experiments I force that packets losses in the network. The traffic from sewrver to the cliente increases comparring with the normal situation but always the number of packets received in B is the same than the packets sent by A. Is what I don´t understand well. Maybe I have to select some option in wireshark..I´m new in it sorry..</p><p>But if you could help me..</p></div><div id="comment-1370-info" class="comment-info"><span class="comment-age">(16 Dec '10, 00:41)</span> Susana26</div></div><span id="1373"></span><div id="comment-1373" class="comment"><div id="post-1373-score" class="comment-score"></div><div class="comment-text"><p>And another thing. The packets that appear dropeed in the status bar, are pakcets that are sent by because of my machine I can not process so wireshark can not count and manage it? VBefore I told you that I wath the results in Stadistics -&gt;Conversations but really I take the results from Stadistics -&gt; Endpointsa where appears the number of packets sent and received by each part that takes part in the communication. I´m wrong? Thank you!!!</p></div><div id="comment-1373-info" class="comment-info"><span class="comment-age">(16 Dec '10, 02:36)</span> Susana26</div></div></div><div id="comment-tools-1362" class="comment-tools"></div><div class="clear"></div><div id="comment-1362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="1365"></span>

<div id="answer-container-1365" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1365-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You really cannot see a lost packet. You can only detect it has occurred based on behavior in an upper layer protocol like TCP. Alternatively, you can gather traffic on two endpoints and make a comparison. With that being said, please let me know more specifically how you are capturing and analyzing traffic, what you are trying to understand through your analysis and what type of traffic you are looking at.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '10, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-1365" class="comments-container"></div><div id="comment-tools-1365" class="comment-tools"></div><div class="clear"></div><div id="comment-1365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1375"></span>

<div id="answer-container-1375" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1375-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How I have to do to capture in both sides?I didn´t do anything more than start the capture and see the traffic that is in both sides.And in conversations I can see the traffic from A -&gt; B and from B-&gt;A and always the packets received is the same than the sent. Where I have to put that capture ib both sides?</p></blockquote><p>What I was saying here is if you copy traffic on or near A and on or near B. If the same packets are in both captures then there is very likely no loss of packets. If the packets from A &gt; B is always equal to the packets from B &gt; A, that sort of indicates that it is a symmetric or at least somewhat predictable protocol.</p><blockquote><p>What I´m doing is sending udp traffic between a client and a server. More send udp packets but there are much more traffic from the server becausae his always send a file divided in smaller packets. I don´t put any special to do the capture and I studied the packets sent and received in stadistics-&gt;conversations. But is what I don´t understand. For one experiments I force that packets losses in the network. The traffic from sewrver to the cliente increases comparring with the normal situation but always the number of packets received in B is the same than the packets sent by A. Is what I don´t understand well. Maybe I have to select some option in wireshark..I´m new in it sorry..</p></blockquote><p>Since we are talking about UDP, there's not a lot in the protocol itself that could tell us if packets are being dropped or not. So what we have to do is think about the UDP payload, which would be the protocols in the Session, Presentation, and Application layers (of the OSI model). I guess the thing I am getting at is exactly how should wireshark tell us if there are missing packets? From a wire perspective, we would generally either see a gap in communication (downstream from what's causing the drops) or we would see retransmits (if we are up stream from what is causing the drops). In TCP, we have sequence numbers that we can determine if our capture is in one of those two locations. In UDP, we have no sequence numbers, so we have to know about the protocol in the payload, or compare our capture to a capture that was on the other side of a device causing the drops. Make sense?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '10, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1375" class="comments-container"><span id="1430"></span><div id="comment-1430" class="comment"><div id="post-1430-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your replay Paul but I don´t understand very well what you mean.</p><p>What I was saying here is if you copy traffic on or near A and on or near B. If the same packets are in both captures then there is very likely no loss of packets. If the packets from A &gt; B is always equal to the packets from B &gt; A, that sort of indicates that it is a symmetric or at least somewhat predictable protocol.</p><p>Yes, I can see in Stadistics-&gt; Endpoints that the packets sent by A are the same than the packets received by B but there is loss packets because I introduce it. I can see how the number of packets increases compared to the situation where there is no traffic loss but I cannot understand why the number of packets received by B is the same sent by A when I´m make that there are loss packets.</p><p>Since we are talking about UDP, there's not a lot in the protocol itself that could tell us if packets are being dropped or not. So what we have to do is think about the UDP payload, which would be the protocols in the Session, Presentation, and Application layers (of the OSI model). I guess the thing I am getting at is exactly how should wireshark tell us if there are missing packets? From a wire perspective, we would generally either see a gap in communication (downstream from what's causing the drops) or we would see retransmits (if we are up stream from what is causing the drops). In TCP, we have sequence numbers that we can determine if our capture is in one of those two locations. In UDP, we have no sequence numbers, so we have to know about the protocol in the payload, or compare our capture to a capture that was on the other side of a device causing the drops. Make sense?</p><p>Sorry but I don´t understand very well this. I´m working with UDP traffic but I have the same problem for TCP traffic. I force a taffic loss but I always see the same number of packets received than sent. What sense has this?I can´t see the number of loss packets with wireshark??</p><p>Thanks a lot for your help!!</p></div><div id="comment-1430-info" class="comment-info"><span class="comment-age">(21 Dec '10, 05:05)</span> Susana26</div></div></div><div id="comment-tools-1375" class="comment-tools"></div><div class="clear"></div><div id="comment-1375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1439"></span>

<div id="answer-container-1439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1439-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most well-designed protocols that use UDP as transport have some sort of identification or sequence number - if the application needs to be aware of lost datagrams. If you look at the specs for DNS or RTP or SNMP you will find this. Wireshark does track some of these identifiers - for instance it can report on lost RTP packets.</p><p>Also note that the IP header also has an ID. Usually a machine will increment this for each IP packet it sends. If you know that your sender is only sending traffic to one destination you may be able to make use of this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '10, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1439" class="comments-container"></div><div id="comment-tools-1439" class="comment-tools"></div><div class="clear"></div><div id="comment-1439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6064"></span>

<div id="answer-container-6064" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6064-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would also love to know how to count the number of lost packets with regard to sending so if I run tshark, or wireshark, I can see a lost packet for example when it sends the SYN and never gets the SYN,ACK so it resends the SYN again. Is there a way to get a count of all lost packets from the sender where it had to resend? Then, I can just run this on both sides to get the total number of lost packets between two machines.</p><p>I am currently running on EC2 and am seeing I think major packet loss but not sure how to count the number. Anyone know how to count the number of resends from one end to get the number lost?</p><p>(or maybe there is a script out there that can take tshark input and spit out number of packets resent).</p><p>thanks, Dean</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '11, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/47b75de06e7da72e041e05dfc5a7704f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dean%20Hiller&#39;s gravatar image" /><p>Dean Hiller<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dean Hiller has no accepted answers">0%</span></p></div></div><div id="comments-container-6064" class="comments-container"></div><div id="comment-tools-6064" class="comment-tools"></div><div class="clear"></div><div id="comment-6064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6458"></span>

<div id="answer-container-6458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6458-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How to get a count of resent packets? (same thing as lost packets in the one direction without counting lost packets in the oppossite direction of course)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '11, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/47b75de06e7da72e041e05dfc5a7704f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dean%20Hiller&#39;s gravatar image" /><p>Dean Hiller<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dean Hiller has no accepted answers">0%</span></p></div></div><div id="comments-container-6458" class="comments-container"></div><div id="comment-tools-6458" class="comment-tools"></div><div class="clear"></div><div id="comment-6458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

