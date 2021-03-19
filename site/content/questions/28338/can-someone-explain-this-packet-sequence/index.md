+++
type = "question"
title = "Can someone explain this packet sequence?"
description = '''I am debugging intermittent connection issues between a client and server application and when running WireShark the following packet sequence occurs:  Server -&amp;gt; Client [FIN, PSH, ACK]  Client -&amp;gt; Server [ACK]   Client -&amp;gt; Server [PSH, ACK]   Server -&amp;gt; Client [RST, ACK]   Client -&amp;gt; Serv...'''
date = "2013-12-23T06:21:00Z"
lastmod = "2013-12-25T07:55:00Z"
weight = 28338
keywords = [ "rst", "fin" ]
aliases = [ "/questions/28338" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can someone explain this packet sequence?](/questions/28338/can-someone-explain-this-packet-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28338-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am debugging intermittent connection issues between a client and server application and when running WireShark the following packet sequence occurs:</p><pre><code> Server -&gt; Client [FIN, PSH, ACK]
 Client -&gt; Server [ACK] 
 Client -&gt; Server [PSH, ACK] 
 Server -&gt; Client [RST, ACK] 
 Client -&gt; Server [FIN, PSH, ACK] 
 Server -&gt; Client [RST] 
 Client -&gt; Server [SYN] //start of new connection</code></pre><p>Can anyone help explain what is going on here? It looks to me like the server is initiating closing the connection, but why does it send an RST after already having sent the FIN and received the ACK, and then send another RST?</p></div><div id="question-tags" class="tags-container tags">rst fin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '13, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/0562ca04e265894460832fcdccfedbf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mclaassen&#39;s gravatar image" /><p>mclaassen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mclaassen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Dec '13, 08:26</p></div></div><div id="comments-container-28338" class="comments-container"><span id="28385"></span><div id="comment-28385" class="comment"><div id="post-28385-score" class="comment-score"></div><div class="comment-text"><p>Are server and client isolated when this happens? I.e., there's no possibility an errant or misconfigured "server" is "polluting" the connection?</p></div><div id="comment-28385-info" class="comment-info"><span class="comment-age">(25 Dec '13, 03:33)</span> rickhg12hs</div></div></div><div id="comment-tools-28338" class="comment-tools"></div><div class="clear"></div><div id="comment-28338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28387"></span>

<div id="answer-container-28387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28387-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>without further information (time stamps, sequence numbers, length of the frames, etc.) I can only speculate. Here is what <strong>could</strong> have happened.</p><p>The server software decided to close the connection (reason unknown) and sends a FIN. After that, the server is in the state FIN WAIT 1 (see <a href="http://commons.wikimedia.org/wiki/File:Tcp_state_diagram_fixed.svg">TCP state diagram</a>). In that state it expects either a FIN/ACK or an ACK. However, the client sends two ACKs, one with a PSH flags, indicating that there is more data to 'push' to the server side application. As the server application does not expect any further data (see FIN), it 'might' send a RST in return to signal to the client to stop sending any further data (I did <strong>not</strong> check the RFC to figure out if that's the way the server should/could react). After the RST, the client closes the connection with a FIN/ACK (again with a PSH flag !?). Why this is again answered with a RST, remains unclear, as there is not enough information available. After some time, the client tries to re-establish the communication with the server (SYN).</p><p>Why this happened in the shown sequence, might have several reasons. As you did not add the time stamps and other information (sequence number, length, etc.) I could only speculate and that's going to happen in this case ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '13, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28387" class="comments-container"></div><div id="comment-tools-28387" class="comment-tools"></div><div class="clear"></div><div id="comment-28387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

