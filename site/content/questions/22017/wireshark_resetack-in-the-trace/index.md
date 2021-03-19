+++
type = "question"
title = "wireshark_Reset,ACK in the trace"
description = '''I have captured some data for a client, and the capture is an ssl3. from what I can tell it looks like the servers are communication using the three way handshake, then the two server communicate over a secure, connection, and then a https connection is initiated by one of the server or the applicat...'''
date = "2013-06-13T09:24:00Z"
lastmod = "2013-06-13T10:53:00Z"
weight = 22017
keywords = [ "ssl_connection" ]
aliases = [ "/questions/22017" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark\_Reset,ACK in the trace](/questions/22017/wireshark_resetack-in-the-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22017-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured some data for a client, and the capture is an ssl3. from what I can tell it looks like the servers are communication using the three way handshake, then the two server communicate over a secure, connection, and then a https connection is initiated by one of the server or the application, and finally transitions process ends with fin -ack -ack -Rst, ack and the process start over.</p><p>Question? Am I correct on that or is something else going on in the trace thanks for the help in advance.</p><p><a href="https://www.cloudshark.org/captures/9e2ba03160c3">https://www.cloudshark.org/captures/9e2ba03160c3</a></p></div><div id="question-tags" class="tags-container tags">ssl_connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p>ejohnson7<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-22017" class="comments-container"></div><div id="comment-tools-22017" class="comment-tools"></div><div class="clear"></div><div id="comment-22017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22020"></span>

<div id="answer-container-22020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22020-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no data transfer in the sessions in your tracefile. Although the snaplength prevents Wireshark from displaying the SSL handshake properly, the following sequence can be assumed, based on normal (resumed) SSL handshakes:</p><pre><code>1 C-&gt;S: SYN
2 S-&gt;C: SYN/ACK
3 C-&gt;S: ACK
4 C-&gt;S: ClientHello
5 S-&gt;C: ServerHello, ChangeCipherSpec, Finished
6 C-&gt;S: ChangeCipherSpec, Finished
7 C-&gt;S: FIN
8 S-&gt;C: ACK
9 S-&gt;C: RST</code></pre><p>Between frame 6 and 7 there should have been "ApplicationData" messages if there was data transfer between the two systems. Since the client is closing the connection, and the interval between the sessions is exactly 64 seconds (filter on tcp.flags==2 and look at the time difference between the odd lines and then the time difference between the even lines), it looks like there are two processes on 10.97.4.65 are monitoring the availability of the server by just performing the SSL handshake.</p><p>EDIT: removed the ServerHelloDone, as it is not part of a resumed SSL handshake</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '13, 23:48</p></div></div><div id="comments-container-22020" class="comments-container"><span id="22033"></span><div id="comment-22033" class="comment"><div id="post-22033-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for you advice so sh the reset set are just the connection closing no a bad thing correct</p></div><div id="comment-22033-info" class="comment-info"><span class="comment-age">(13 Jun '13, 19:51)</span> ejohnson7</div></div><span id="22034"></span><div id="comment-22034" class="comment"><div id="post-22034-score" class="comment-score"></div><div class="comment-text"><p>how can you tell there two processess on 10.97.4.65 monitoring this is new to me thanks</p></div><div id="comment-22034-info" class="comment-info"><span class="comment-age">(13 Jun '13, 19:59)</span> ejohnson7</div></div><span id="22039"></span><div id="comment-22039" class="comment"><div id="post-22039-score" class="comment-score"></div><div class="comment-text"><p>I can't tell for sure, but I see two sequences of SYN packets which are exactly 64 seconds apart (frame 1, 19, 37, 55, 73 are 64 seconds apart and frame 10, 28, 46, 64, 82 are 64 seconds apart)</p></div><div id="comment-22039-info" class="comment-info"><span class="comment-age">(14 Jun '13, 00:04)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-22020" class="comment-tools"></div><div class="clear"></div><div id="comment-22020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

