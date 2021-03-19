+++
type = "question"
title = "Fast-retransmission when received one duplicate ack?"
description = '''I found a tcp packets as follows: The third packets is a dup ack packets(includeing sack option,indicate some packets is not received),then the server retransmission the packet soon.According to the RFC,above 3 duplicate acks,the tcp sender then can retransmission the packets,why the strange happene...'''
date = "2012-12-04T04:32:00Z"
lastmod = "2012-12-04T04:47:00Z"
weight = 16535
keywords = [ "ack", "duplicate" ]
aliases = [ "/questions/16535" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fast-retransmission when received one duplicate ack?](/questions/16535/fast-retransmission-when-received-one-duplicate-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16535-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I found a tcp packets as follows: The third packets is a dup ack packets(includeing sack option,indicate some packets is not received),then the server retransmission the packet soon.According to the RFC,above 3 duplicate acks,the tcp sender then can retransmission the packets,why the strange happened:Fast-retransmission when received one duplicate ack?</p><pre><code>1. &quot;10.0.30.146&quot;     &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;15974 &gt; 2806 [ACK] Seq=31116425 Ack=1 Win=5040  Len=1260&quot;
2. &quot;10.0.30.146&quot;     &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;15974 &gt; 2806 [ACK] Seq=31117685 Ack=1 Win=5040  Len=1260&quot;
3. &quot;10.50.0.45&quot;  &quot;10.0.30.146&quot;   &quot;TCP&quot;   &quot;[TCP Dup ACK 36104#1] 2806 &gt; 15974 [ACK] Seq=1 Ack=31101305 Win=131072 Len=0 SLE=31107605 SRE=31108865&quot;
4. &quot;10.0.30.146&quot;     &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;[TCP Retransmission] 15974 &gt; 2806 [ACK] Seq=31101305 Ack=1 Win=5040 Len=1260&quot;
5.&quot;10.50.0.45&quot;   &quot;10.0.30.146&quot;   &quot;TCP&quot;   &quot;[TCP Dup ACK 36104#2] 2806 &gt; 15974 [ACK] Seq=1 Ack=31101305 Win=131072 Len=0 SLE=31107605 SRE=31115165&quot;
6.&quot;10.0.30.146&quot;  &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;[TCP Retransmission] 15974 &gt; 2806 [ACK] Seq=31102565 Ack=1 Win=5040  Len=1260&quot;
7.&quot;10.50.0.45&quot;   &quot;10.0.30.146&quot;   &quot;TCP&quot;   &quot;[TCP Dup ACK 36104#3] 2806 &gt; 15974 [ACK] Seq=1 Ack=31101305 Win=131072 Len=0 SLE=31107605 SRE=31116425&quot;
8.&quot;10.0.30.146&quot;  &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;[TCP Retransmission] 15974 &gt; 2806 [ACK] Seq=31103825 Ack=1 Win=5040 Len=1260&quot;
9.&quot;10.50.0.45&quot;   &quot;10.0.30.146&quot;   &quot;TCP&quot;   &quot;[TCP Dup ACK 36104#4] 2806 &gt; 15974 [ACK] Seq=1 Ack=31101305 Win=131072 Len=0 SLE=31107605 SRE=31118945&quot;
10.&quot;10.0.30.146&quot;     &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;[TCP Retransmission] 15974 &gt; 2806 [ACK] Seq=31105085 Ack=1 Win=5040  Len=1260&quot;
11.&quot;10.50.0.45&quot;  &quot;10.0.30.146&quot;   &quot;TCP&quot;   &quot;2806 &gt; 15974 [ACK] Seq=1 Ack=31103825 Win=131072 Len=0 SLE=31107605 SRE=31118945&quot;
12.&quot;10.0.30.146&quot;     &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;[TCP Retransmission] 15974 &gt; 2806 [ACK] Seq=31106345 Ack=1 Win=5040  Len=1260&quot;
13.&quot;10.50.0.45&quot;  &quot;10.0.30.146&quot;   &quot;TCP&quot;   &quot;2806 &gt; 15974 [ACK] Seq=1 Ack=31105085 Win=131072 Len=0 SLE=31107605 SRE=31118945&quot;
14.&quot;10.0.30.146&quot;     &quot;10.50.0.45&quot;    &quot;TCP&quot;   &quot;15974 &gt; 2806 [ACK] Seq=31118945 Ack=1 Win=5040  Len=1260&quot;</code></pre></div><div id="question-tags" class="tags-container tags">ack duplicate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/7fdbac8aac2e38813e1fc1da4c6efdf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chinasan&#39;s gravatar image" /><p>chinasan<br />
<span class="score" title="0 reputation points">0</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chinasan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '12, 08:24</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-16535" class="comments-container"></div><div id="comment-tools-16535" class="comment-tools"></div><div class="clear"></div><div id="comment-16535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16536"></span>

<div id="answer-container-16536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16536-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd say the sender retransmits BECAUSE of the SACK option, which tells it what packet is missing... there is no reason to wait for a 3rd duplicate ACK to do a fast retransmission when SACK already tells the story.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16536" class="comments-container"><span id="16538"></span><div id="comment-16538" class="comment"><div id="post-16538-score" class="comment-score"></div><div class="comment-text"><p>You mean just one duplicate ack with sack received,the sender will re-transmission these packets?</p></div><div id="comment-16538-info" class="comment-info"><span class="comment-age">(04 Dec '12, 05:10)</span> chinasan</div></div><span id="16539"></span><div id="comment-16539" class="comment"><div id="post-16539-score" class="comment-score"></div><div class="comment-text"><p>yes. SACK is the best of the three strategies because it can report exactly what part is missing, while the others can only tell up to what sequence number everything was received successfully. If you have SACK working on both stacks you do not need triple duplicate acks anymore to trigger a Fast Retransmission. SACK is "negotiated" in the TCP Three Way Handshake packets.</p></div><div id="comment-16539-info" class="comment-info"><span class="comment-age">(04 Dec '12, 06:08)</span> Jasper ♦♦</div></div><span id="16540"></span><div id="comment-16540" class="comment"><div id="post-16540-score" class="comment-score"></div><div class="comment-text"><p>@Chinasan and Jasper: Not neccessarily true: SACK is a method to even faster retransmit packets if e.g. there is only a single data packet lost and thus no more ACKs incoming to trigger Fast Retransmission. That is the case, if the ACK containing SACK information is the last ACK from the data-reciever. In that case SACK triggers retransmission before Retransmission timeout.</p><p>In an out-of-order scenario you of course see a single DUP Ack containing SACK options, but because a short time period after that the next ACK tells that everything is OK, no retransmission occurs.</p><p>To sum up: SACK followed by a short time period triggers retransmission of packets, but the sending stack would always wait for further ACKs if more data is in flight to see if the DUP Ack with SACK options is just an out-of-order, or if there is really something wrong with the transmission. In that case, SACK has no timimg advantage to fast retransmission, but is definitely more precise in stating exaclty which segments need to be retransmitted</p></div><div id="comment-16540-info" class="comment-info"><span class="comment-age">(04 Dec '12, 06:35)</span> Landi</div></div><span id="16544"></span><div id="comment-16544" class="comment"><div id="post-16544-score" class="comment-score"></div><div class="comment-text"><p>All I'm saying is that you can see retransmissions without a third duplicate ACK because of SACK triggering it in this case. Yes, there is the timing issue etc, but the question was why there is no more dup ACKs but still a retransmission. And that is because of the SACK :-)</p></div><div id="comment-16544-info" class="comment-info"><span class="comment-age">(04 Dec '12, 07:26)</span> Jasper ♦♦</div></div><span id="16547"></span><div id="comment-16547" class="comment"><div id="post-16547-score" class="comment-score"></div><div class="comment-text"><p>Dear Jasper and Landi, I'm confused with your answers. Actually,the duplicate acks mean the out of order or packets lost,the sender just received one duplicate acks,how can judge out-of-order or lost?Sack just identified which some packets expected,which some packets are received. sorry I can not comment using my iPad,so answer my own question to ask.</p></div><div id="comment-16547-info" class="comment-info"><span class="comment-age">(04 Dec '12, 08:14)</span> chinasan</div></div><span id="16549"></span><div id="comment-16549" class="comment not_top_scorer"><div id="post-16549-score" class="comment-score"></div><div class="comment-text"><p>Dup Ack means that an acknowledge number that was seen before is seen again, acknowledging the same data again. They can both appear as a result of out-of-order arrivals as well as packet loss. Same with SACK - there can be SACK options present in dup ack packets when there is just an out-of-order situation.</p><p>Actual packet loss is basically determined by the amount of dup acks (Fast Retransmission) or existance of SACK (with a little delay to make sure the packet isn't late and really lost) or long delay ("old" Retransmission timeout)</p></div><div id="comment-16549-info" class="comment-info"><span class="comment-age">(04 Dec '12, 08:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16536" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-16536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

