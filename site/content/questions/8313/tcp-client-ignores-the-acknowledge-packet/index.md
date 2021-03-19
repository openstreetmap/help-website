+++
type = "question"
title = "TCP Client ignores the acknowledge packet"
description = '''Can someone please help me with this. The TCP client just ignores the ACK packet, and kept resending packet 53741 until the connection is time out. Where could be the issue?  67011 103.330429 192.168.232.6 192.168.233.6 TCP 590 [TCP Retransmission] tsp &amp;gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=...'''
date = "2012-01-10T20:02:00Z"
lastmod = "2012-01-11T01:44:00Z"
weight = 8313
keywords = [ "ack" ]
aliases = [ "/questions/8313" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Client ignores the acknowledge packet](/questions/8313/tcp-client-ignores-the-acknowledge-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8313-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone please help me with this. The TCP client just ignores the ACK packet, and kept resending packet 53741 until the connection is time out. Where could be the issue?</p><pre><code> 67011 103.330429  192.168.232.6  192.168.233.6  TCP  590  [TCP Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=536   //client send packet 53741
 67048 103.358386  192.168.233.6  192.168.232.6  TCP  66   icl-twobase1 &gt; tsp [ACK] Seq=3683 Ack=53741 Win=261072 Len=0 SLE=54049 SRE=58188       //server send ACK to packet 53741
 67050 103.358535  192.168.233.6  192.168.232.6  TCP  66   [TCP Dup ACK 67048#1] icl-twobase1 &gt; tsp [ACK] Seq=3683 Ack=53741 Win=261072 Len=0 SLE=54049 SRE=58188  // ACK to 53741 send again
 67052 103.358685  192.168.233.6  192.168.232.6  TCP  66   [TCP Dup ACK 67048#2] icl-twobase1 &gt; tsp [ACK] Seq=3683 Ack=53741 Win=261072 Len=0 SLE=54049 SRE=58188  // ACK to 53741 send again
 67053 103.358703  192.168.232.6  192.168.233.6  TCP  362  [TCP Fast Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=308   //seems client didn&#39;t recognize the ACK packet, and resend packet 53741

 69414 107.036796  192.168.232.6  192.168.233.6  TCP  590  [TCP Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=536  // seems client didn&#39;t recognize the ACK packet, and resend packet 53741 after 4 sec
 74328 114.171542  192.168.232.6  192.168.233.6  TCP  590  [TCP Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=536 //another resend packet 53741 after 7 sec
 83850 128.663773  192.168.232.6  192.168.233.6  TCP  590  [TCP Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=536 //another resend packet 53741 after 14 sec
102074 157.423329  192.168.232.6  192.168.233.6  TCP  590  [TCP Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=536 //another resend packet 53741 after 29 sec
119462 215.163865  192.168.232.6  192.168.233.6  TCP  590  [TCP Retransmission] tsp &gt; icl-twobase1 [ACK] Seq=53741 Ack=3683 Win=262144 Len=536 //another resend packet 53741 after 58 sec

150535 332.202312  192.168.233.6  192.168.232.6  TCP  60   icl-twobase1 &gt; tsp [FIN, ACK] Seq=3683 Ack=53741 Win=261072 Len=0 //FIN
150536 332.202335  192.168.232.6  192.168.233.6  TCP  54   tsp &gt; icl-twobase1 [RST] Seq=53741 Win=0 Len=0 //client send RST, TCP connection is closed at this point</code></pre></div><div id="question-tags" class="tags-container tags">ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '12, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/f5f7856f9dbf52bfa77f0ac520f19b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wirewarrior&#39;s gravatar image" /><p>Wirewarrior<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wirewarrior has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '12, 00:26</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8313" class="comments-container"></div><div id="comment-tools-8313" class="comment-tools"></div><div class="clear"></div><div id="comment-8313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8316"></span>

<div id="answer-container-8316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8316-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, an ACK value of 53741 does not mean "I have received your packet with SEQ=53471", it means "I have received data up to (but not including) SEQ 53471".</p><p>Then there is SACK, which means Selective Acknowledgements. In frame 67048 the server ACK's up to SEQ 53741, but it also says it has received SEQ-54049 to 58188 (SLE=54049 SRE=58188). So the client needs to resend 53741 to 54048 and can then send data starting from 58188.</p><p>Now, the client does send that part of data repeatedly, but the server stops sending ACK's to tell the client that it did receive the data. So either the server was suddenly disconnected from the network or maybe something on route was blocking/dropping the traffic.</p><p>So in this case, the client does not ignore the ACKs, it perfectly heard them and acted on them :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '12, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '12, 02:40</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8316" class="comments-container"></div><div id="comment-tools-8316" class="comment-tools"></div><div class="clear"></div><div id="comment-8316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

