+++
type = "question"
title = "[RST, ACK] immediately after FIN flag"
description = '''Hi, I&#x27;m trying to figure out a problem where I&#x27;m getting multiple socket exceptions on client machines on the network. Clients always connect to the server, send some data and the server always sends some data back to every client. I&#x27;ve run a prolonged capture and I&#x27;m seeing that when the problem oc...'''
date = "2016-01-24T18:47:00Z"
lastmod = "2016-01-25T07:40:00Z"
weight = 49495
keywords = [ "3" ]
aliases = [ "/questions/49495" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[RST, ACK\] immediately after FIN flag](/questions/49495/rst-ack-immediately-after-fin-flag)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49495-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to figure out a problem where I'm getting multiple socket exceptions on client machines on the network. Clients always connect to the server, send some data and the server always sends some data back to every client. I've run a prolonged capture and I'm seeing that when the problem occurs, the server seems to be sending the data back to the client, but almost immediately after that the server sends an RST+ACK packet, as shown below:</p><pre><code>No.     Time        Source     SRC_Port Destination   DST_Port        Protocol Length Info

3634    0.000   203.38.235.197  62379   10.0.8.29   610 TCP         62379→610 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=682375632 TSecr=0

3635    0.000   10.0.8.29   610 203.38.235.197  62379   TCP         610→62379 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 SACK_PERM=1 TSval=292263667 TSecr=682375632

3636    0.000   203.38.235.197  62379   10.0.8.29   610 TCP         62379→610 [ACK] Seq=1 Ack=1 Win=14600 Len=0 TSval=682375632 TSecr=292263667

3637    0.000   203.38.235.197  62379   10.0.8.29   610 TCP         62379→610 [PSH, ACK] Seq=1 Ack=1 Win=14600 Len=341 TSval=682375632 TSecr=292263667

3638    0.000   203.38.235.197  62379   10.0.8.29   610 TCP         62379→610 [ACK] Seq=342 Ack=1 Win=14600 Len=1448 TSval=682375632 TSecr=292263667

3639    0.000   10.0.8.29   610 203.38.235.197  62379   TCP         610→62379 [ACK] Seq=1 Ack=1790 Win=65160 Len=0 TSval=292263667 TSecr=682375632

3640    0.000   10.0.8.29   610 203.38.235.197  62379   TCP         610→62379 [FIN, ACK] Seq=1 Ack=1790 Win=65160 Len=0 TSval=292263667 TSecr=682375632

3641    0.000   10.0.8.29   610 203.38.235.197  62379   TCP         610→62379 [RST, ACK] Seq=2 Ack=1790 Win=0 Len=0

3642    0.000   203.38.235.197  62379   10.0.8.29   610 TCP         62379→610 [PSH, ACK] Seq=1790 Ack=1 Win=14600 Len=5 TSval=682375632 TSecr=292263667

3643    0.000   10.0.8.29   610 203.38.235.197  62379   TCP         610→62379 [RST] Seq=1 Win=0 Len=0`</code></pre><p>Any suggestion will be very much helpful for me to resolve the issue.</p><p>Regards, Nikhil Keshrwani</p></div><div id="question-tags" class="tags-container tags">3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '16, 18:47</strong></p><img src="https://secure.gravatar.com/avatar/b3873c3e126949153f571624d0fa6949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikhil174&#39;s gravatar image" /><p>Nikhil174<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikhil174 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '16, 00:49</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49495" class="comments-container"><span id="49502"></span><div id="comment-49502" class="comment"><div id="post-49502-score" class="comment-score"></div><div class="comment-text"><p>Could you share us a trace file? Without a tracefile it is hard to give you some reliable statements.<br />
But the behaviour you are asking about, could be some kind of "half-duplex close". Which is used by some implementation as a workaround for the time_wait behaviour.<br />
of course in your case the RST can be an indication of a failure, too.<br />
But without the capture it hard to tell, as I already said.<br />
Have you ever compared this session with a session where everything went fine?</p></div><div id="comment-49502-info" class="comment-info"><span class="comment-age">(25 Jan '16, 03:31)</span> Christian_R</div></div><span id="49505"></span><div id="comment-49505" class="comment"><div id="post-49505-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/file/d/0Bwpm-1j243baM3pkS3hmTnVxZXc/view?usp=sharing">https://drive.google.com/file/d/0Bwpm-1j243baM3pkS3hmTnVxZXc/view?usp=sharing</a></p><p>Thanks for the reply here is the file you can download</p><p>Regards, Nikhil</p></div><div id="comment-49505-info" class="comment-info"><span class="comment-age">(25 Jan '16, 07:07)</span> Nikhil174</div></div><span id="49511"></span><div id="comment-49511" class="comment"><div id="post-49511-score" class="comment-score"></div><div class="comment-text"><p>Easily said: I guess the problem is application related. Because the server (10.0.8.29) is sending a FIN packet.</p><p><strong>Does the logfiles(Server OS or Server Application) give you some hints to identify the cause of the FIN´s?</strong></p><p>Furthermore I can´t exactly say (delta time is very low + internal server behaviour) if the FIN is send immediately after the end of the Three-Way-Handshake (Stream Indx 365) or if the first client packet is causing the FIN (for example like Stream Indx 1).</p><p>But I guess relative reliable, that the RST is only a follow up or normal.</p></div><div id="comment-49511-info" class="comment-info"><span class="comment-age">(25 Jan '16, 12:57)</span> Christian_R</div></div></div><div id="comment-tools-49495" class="comment-tools"></div><div class="clear"></div><div id="comment-49495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49506"></span>

<div id="answer-container-49506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To me it looks like two issues at the same time</p><ul><li><p>one is that the server does not like something about the sending client or about the data contents and so it sends a FIN before the client has managed to say all it wanted to say. This would be supported by the fact that I can never see any answer of the server, the session always contains only data sent by the client. So repeating @Christian_R's question - do you have also any successful sessions or all look like this?</p></li><li><p>another one is that in many cases, the server sends the RST just about 40-50 microseconds after the FIN it has sent itself, i.e. it most likely does not send it as a reaction to reception of another packet from the client after it has sent the FIN (assuming the capture is taken at the server itself). So I would assume that if it is not a plain bug, it may be the server's attempt to release its session descriptors for eventual new session coming from the same port of the same client, as @Christian_R has suggested.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '16, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-49506" class="comments-container"></div><div id="comment-tools-49506" class="comment-tools"></div><div class="clear"></div><div id="comment-49506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

