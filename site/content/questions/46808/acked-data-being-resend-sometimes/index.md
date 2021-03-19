+++
type = "question"
title = "Acked data being resend sometimes"
description = '''I have the following capture made via wireshark. For e.g. in line 96 it send the post request then it get OK ack in line 98. Again in line 99 it keep sending the same thing. I have check my application is only sending it ones. What could be going on at the network layer? I dont see the repetition at...'''
date = "2015-10-21T10:02:00Z"
lastmod = "2015-10-21T10:40:00Z"
weight = 46808
keywords = [ "java", "webservice" ]
aliases = [ "/questions/46808" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Acked data being resend sometimes](/questions/46808/acked-data-being-resend-sometimes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46808-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following capture made via wireshark. For e.g. in line 96 it send the post request then it get OK ack in line 98. Again in line 99 it keep sending the same thing. I have check my application is only sending it ones. What could be going on at the network layer? I dont see the repetition at the application layer. Because if its a bug in my app then it should be always repeating it. But it happens only sometimes. Just to add on those without problem I notice this [ACK] Seq=1. The value is always 1 for the Seq and with those there is not repetition?</p><pre><code>96  375.163057921   *.*.*.23   
*.*.*.12    HTTP/XML    592 POST /*********.asmx?WSDL HTTP/1.1  
97 
375.166722899   *.*.*.12    *.*.*.23    TCP 66  80?56912 [ACK] Seq=3068 Ack=1819 Win=130304 Len=0 TSval=18755499 TSecr=1624042020 
98 
375.244932864   *.*.*.12    *.*.*.23    HTTP/XML    714 HTTP/1.1 200 OK  
99 
375.244987515   *.*.*.23    *.*.*.12    TCP 66  56912?80 [ACK] Seq=1819 Ack=3716 Win=25600 Len=0 TSval=1624042102 TSecr=18755506 
100
375.302667374   *.*.*.23    *.*.*.12    TCP 449 [TCP segment of a reassembled PDU] 101 375.302702201   *.*.*.23   
*.*.*.12    HTTP/XML    592 POST /*********.asmx?WSDL HTTP/1.1  
102
375.306998164   *.*.*.12    *.*.*.23    TCP 66  80?56912 [ACK] Seq=3716 Ack=2728 Win=131328 Len=0 TSval=18755513 TSecr=1624042160 
103
375.399607915   *.*.*.12    *.*.*.23    HTTP/XML    714 HTTP/1.1 200 OK  
104
375.399705590   *.*.*.23    *.*.*.12    TCP 66  56912?80 [ACK] Seq=2728 Ack=4364 Win=26880 Len=0 TSval=1624042257 TSecr=18755522
105
375.456699174   *.*.*.23    *.*.*.12    TCP 449 [TCP segment of a reassembled PDU] 106 375.456734111   *.*.*.23   
*.*.*.12    HTTP/XML    592 POST /*********.asmx?WSDL HTTP/1.1  
107
375.463896220   *.*.*.12    *.*.*.23    TCP 66  80?56912 [ACK] Seq=4364 Ack=3637 Win=130304 Len=0 TSval=18755528 TSecr=1624042314</code></pre></div><div id="question-tags" class="tags-container tags">java webservice</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '15, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" /><p>newbie14<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '15, 10:19</p></div></div><div id="comments-container-46808" class="comments-container"><span id="46811"></span><div id="comment-46811" class="comment"><div id="post-46811-score" class="comment-score">1</div><div class="comment-text"><p>Could you provide us a trace at public accessible place?</p></div><div id="comment-46811-info" class="comment-info"><span class="comment-age">(21 Oct '15, 11:00)</span> Christian_R</div></div><span id="46812"></span><div id="comment-46812" class="comment"><div id="post-46812-score" class="comment-score"></div><div class="comment-text"><p>I dont get you what trace do you need please ?</p></div><div id="comment-46812-info" class="comment-info"><span class="comment-age">(21 Oct '15, 11:03)</span> newbie14</div></div><span id="46814"></span><div id="comment-46814" class="comment"><div id="post-46814-score" class="comment-score"></div><div class="comment-text"><p>The pcap file, from which you get the txt output.</p></div><div id="comment-46814-info" class="comment-info"><span class="comment-age">(21 Oct '15, 12:09)</span> Christian_R</div></div><span id="46821"></span><div id="comment-46821" class="comment"><div id="post-46821-score" class="comment-score"></div><div class="comment-text"><p>The problem it has all the ip address which I could not disclosed. But what is your say on the fast retransmit?</p></div><div id="comment-46821-info" class="comment-info"><span class="comment-age">(21 Oct '15, 19:15)</span> newbie14</div></div><span id="46822"></span><div id="comment-46822" class="comment"><div id="post-46822-score" class="comment-score">1</div><div class="comment-text"><p>Use TraceWrangler, available from www.tracewrangler.com, to anonymize the IP addresses.</p></div><div id="comment-46822-info" class="comment-info"><span class="comment-age">(21 Oct '15, 21:44)</span> Jim Aragon</div></div></div><div id="comment-tools-46808" class="comment-tools"></div><div class="clear"></div><div id="comment-46808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46809"></span>

<div id="answer-container-46809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46809-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe someone has another idea, but it seems as though the ACKs do different things.</p><ol><li>the first ACK (97) has <code>Seq=3068</code> and <code>Ack=1819</code></li><li>the second (102) has <code>Seq=3716 Ack=2728</code></li></ol><p>ACKs are also sent when a packet has not arrived to signal a need to resend. In that case, the <code>Ack</code> field contains the last correctly received packet. Thus, the first might be a "send the data again", while the second might be a "ok, it has all arrived".</p><p>This is called <em>fast recovery</em> and <a href="https://en.wikipedia.org/wiki/Fast_retransmit"><em>fast retransmit</em></a>. It is part of TCP's error recovery mechanism.</p><p>Different purposes of ACKs:</p><ul><li>window scaling</li><li>retransmit</li><li>data acknowledgement</li></ul><p>Sometimes the packets also cross on the layer (an ACK being sent to retransmit while the other packet is in transit).</p><p>In your case, have you considered posting the code at some Programmer's site (or here, if need be). Maybe it sends the data several times in some corner cases...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/0f479a594deab60e820a84e87409f955?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1234&#39;s gravatar image" /><p>user1234<br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1234 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Nov '15, 10:07</p></div></div><div id="comments-container-46809" class="comments-container"><span id="46813"></span><div id="comment-46813" class="comment"><div id="post-46813-score" class="comment-score"></div><div class="comment-text"><p>@user1234 I dont quite get you on the ack and seq=3068. If you say data have not arrived then why does the the other send 98 375.244932864 <em>.</em>.<em>.12</em> .<em>.</em>.23 HTTP/XML 714 HTTP/1.1 200 OK to say that is has received the data. But I notice the seq is not 1 but all those with normal flow the seq=1. How to diagnose based on the sequence 1?</p></div><div id="comment-46813-info" class="comment-info"><span class="comment-age">(21 Oct '15, 11:05)</span> newbie14</div></div><span id="46823"></span><div id="comment-46823" class="comment"><div id="post-46823-score" class="comment-score"></div><div class="comment-text"><p>That '200 OK' is the application layer talking. We're talking about retransmission at the transport layer. Dig out your <a href="https://en.wikipedia.org/wiki/OSI_model">OSI model</a> book to get the difference.</p></div><div id="comment-46823-info" class="comment-info"><span class="comment-age">(21 Oct '15, 22:46)</span> Jaap ♦</div></div><span id="46867"></span><div id="comment-46867" class="comment"><div id="post-46867-score" class="comment-score"></div><div class="comment-text"><p>My confusion is that why the application layer is sending the OK. It can only send if the earlier packet have reached meaning the packet send succesfully so why there is a retransmission then?</p></div><div id="comment-46867-info" class="comment-info"><span class="comment-age">(22 Oct '15, 19:58)</span> newbie14</div></div><span id="52463"></span><div id="comment-52463" class="comment"><div id="post-52463-score" class="comment-score"></div><div class="comment-text"><p>@newbie14: Yes, you were right. In this case (different ack/seq-numbers), the ACKs should acknowledge different data packets. So from the trace it seems as though the application is asked three times and responds three times.</p></div><div id="comment-52463-info" class="comment-info"><span class="comment-age">(12 May '16, 03:39)</span> user1234</div></div></div><div id="comment-tools-46809" class="comment-tools"></div><div class="clear"></div><div id="comment-46809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

