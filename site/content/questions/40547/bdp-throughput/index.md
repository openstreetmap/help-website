+++
type = "question"
title = "bdp = throughput"
description = '''Hola guys! Window size -if I understood TCP uses it for flow control.  BDP = throughput ? Please correct if I&#x27;m wrrong'''
date = "2015-03-13T17:43:00Z"
lastmod = "2015-03-14T03:32:00Z"
weight = 40547
keywords = [ "bdp" ]
aliases = [ "/questions/40547" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [bdp = throughput](/questions/40547/bdp-throughput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hola guys! Window size -if I understood TCP uses it for flow control.</p><p>BDP = throughput ?</p><p>Please correct if I'm wrrong</p></div><div id="question-tags" class="tags-container tags">bdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '15, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-40547" class="comments-container"><span id="40548"></span><div id="comment-40548" class="comment"><div id="post-40548-score" class="comment-score"></div><div class="comment-text"><p>Or is it the maximum throughput that can be achived on the link in question? I mean if the Window size is lower then the bandwidth delay product and I guess it's not an unusual condition we would not fully utilize the pipe because the transmission cannot exceed the WS, right?</p></div><div id="comment-40548-info" class="comment-info"><span class="comment-age">(13 Mar '15, 17:57)</span> adasko</div></div></div><div id="comment-tools-40547" class="comment-tools"></div><div class="clear"></div><div id="comment-40547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40552"></span>

<div id="answer-container-40552" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40552-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The bandwidth delay product (BDP) is an indication of the needed window size (WS) to let 1 TCP stream utilize the complete bandwidth of the connection.</p><p>If you turn the calculation around, one TCP session can only send one window size of payload per round trip, as it needs an ack to get confirmation that more data can be sent. If you add the protocol overhead of all the other layers you get the theoretical maximum bandwidth per tcp session. For an ethernet network, you get:</p><pre><code>BW = WS*8 * (1000/RTT) * 1518/1460 / 1000000

BW = Bandwidth in megabits per second
WS = Window size in bytes
RTT = Roundtrip time in milliseconds
1518 = frame length on the wire in bytes
1460 = TCP payload size in bytes, so assuming no extra IP or TCP options</code></pre><p>So for a 64K WS on a 1 Gbit/s connection with 10ms RTT, you get a maximum of ~54,5 Mbit/s for one TCP connection. If you want that one TCP connection to fully utilize the full 1 Gbit/s bandwidth, you can calculate the other way around:</p><pre><code>  WS = BW*1000000/8 * (RTT/1000) * (1460/1518)</code></pre><p>That's where you can see that you need to create a product of the BW and the delay (RTT). Any WS higher than the calculated value will make sure the connection is not stalled as a result of the RTT of the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '15, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40552" class="comments-container"><span id="40554"></span><div id="comment-40554" class="comment"><div id="post-40554-score" class="comment-score"></div><div class="comment-text"><p>thank you, this made it easier for me to understand.</p><p>but in practice the WS will be probably always lower than the calculated BDP ... ?</p><p>so, if let's say we have an backup running over a Gigabit Ethernet network with large RTT, and the actual Window Size advertised is way lower then the calculated BDP this could be one of the reasons why the transfer rate is low (at least one of the reasons ?). This because we would send less data and have to acknowledge it more often + considering the RTT this would cause the rate go down yes ?</p></div><div id="comment-40554-info" class="comment-info"><span class="comment-age">(14 Mar '15, 03:56)</span> adasko</div></div><span id="40555"></span><div id="comment-40555" class="comment"><div id="post-40555-score" class="comment-score">1</div><div class="comment-text"><p>(please use comments instead of new answers, that's how this site works best, se the FAQ for more details)</p><p>In practice the WS is usually smaller than the BDP if it is a line with high RTT and high BW. This is no problem as more than one client use more than one TCP stream and so combined they can consume the BW of the link.</p><p>In case you need to utilize the full BW of the link by one system using one TCP stream (like your backup scenario), you need to tune the WS of the receiving end to make sure the sender can keep sending data until the first part of the data is acknowledged (after one RTT).</p><p>So there are not more acknowledgements, it just takes longer for them to reach back to the server, so the WS needs to be big enough that the sender can keep sending while the acks are on the way back.</p><p>And yes, this is a very common problem when doing backups or data-replication over WAN links.</p></div><div id="comment-40555-info" class="comment-info"><span class="comment-age">(14 Mar '15, 04:03)</span> SYN-bit ♦♦</div></div><span id="40556"></span><div id="comment-40556" class="comment"><div id="post-40556-score" class="comment-score"></div><div class="comment-text"><p>thank you again, sorry for using the "answer" option.</p><p>so if the receiving window is not big enough isn't there a reason why the receiving host advertises it (instead of a larger one):</p><ul><li>is it possible that the receiving host is acknowledging data faster thn it can process it to the upper layer out of the buffer ? ( i don't know maybe the application is not writing the data as fast enough to the disk, tape etc.)</li><li>might it be the reasons the the receiving host is "busy" in terms of CPU /RAM usage ?</li><li>might it be a badly written application ?</li></ul><p>so should this thinks have to be taken in to count first before tuning the Window Size of the receiving host (if yes, there are probably many more reasons).</p><p>and what is your experience while running backups within a LAN. i think there shouldn't a high value of RTT at all neither packet lost. is it possible for a LAN topology that the WS is still way lower thn the calculated BDP ?</p><p>i know it's a lot but for now i found your answers way more clear than most of the articles out there :)</p></div><div id="comment-40556-info" class="comment-info"><span class="comment-age">(14 Mar '15, 04:17)</span> adasko</div></div><span id="40557"></span><div id="comment-40557" class="comment"><div id="post-40557-score" class="comment-score">1</div><div class="comment-text"><p>If you are troubleshooting a performance issue, then yes, you need to take all factors into account. But it is good to work at them one by one.</p><ul><li>Make a tracefile (at the sending side) and look for large chunks of data that are interrupted by a couple of ms delay, then an ACK comes in and the sender starts sending again. You can also see this as a "staircase" in the tcp streamgraph. Also notice the "bytes-in-flight" counter goes up to (almost) the WS of the receiver. Then you need to increase the WS as the RTT of the network is the problem.</li><li>If the application can not read data fast enough from the TCP buffers, you will see the WS go down slowly and if the condition continues, it will get lower than 1 MSS which will prevent the sender from sending a full sized frame. Usually the sender will then pause until the WS goes up or after a timer expires, it will send a smaller frame that will fill up the receive buffer of the receiver (the delay is used to prevent the silly window syndrome).</li></ul><p>So, since this is a wireshark Q&amp;A site, make a trace (at the sending side at least, but preferably on both sides, also for the learning experience that things look really different on both ends of the connection). With above information you should be able to determine if you are experiencing delays due to RTT/WS issues or server performance issues.</p></div><div id="comment-40557-info" class="comment-info"><span class="comment-age">(14 Mar '15, 04:32)</span> SYN-bit ♦♦</div></div><span id="40558"></span><div id="comment-40558" class="comment not_top_scorer"><div id="post-40558-score" class="comment-score"></div><div class="comment-text"><p>"bytes-in flight" so this will refer to the data sent but not acknowledge yet , yes ?</p><p>increasing the WS - so this would have to be done probably in registry on the receiving host ? i also came across something called auto-tuning if T'm not wrong but as far i understood it causes more issues - this i will have to read later on. but just for my understanding. first i would have to calculate the optimum Window Size, set it on the receiving host and no matter what this will be always the senders send windows and the receivers, receive window . yes ?</p><p>thank you again. you are a real champ. hope to have the same knowledge as you one day :(</p></div><div id="comment-40558-info" class="comment-info"><span class="comment-age">(14 Mar '15, 04:43)</span> adasko</div></div><span id="40559"></span><div id="comment-40559" class="comment"><div id="post-40559-score" class="comment-score">1</div><div class="comment-text"><p>Yes, BiF is referring the data that is not acknowledged yet.</p><p>Usually you configure a maximum window size and the system will start with a smaller value and then when needed increase it's size up to the configured maximum. Autotuning should do this automagically. Please note that this is just local for a system, so the senders buffers and the receievers buffers are independent of one-another.</p><p>You will learn, bit by bit, just like I did :-)</p></div><div id="comment-40559-info" class="comment-info"><span class="comment-age">(14 Mar '15, 05:05)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-40552" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-40552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

