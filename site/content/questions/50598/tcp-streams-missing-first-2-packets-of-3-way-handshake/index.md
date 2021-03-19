+++
type = "question"
title = "TCP streams missing first 2 packets of 3-way handshake"
description = '''I have 30+ TCP streams in a trace that all have in common that they miss the first 2 packets in the 3-way handshake and have some weird SEQ/ACK numbers going on. The trace is done on the 156.7.53.9 computer. The data being sent is either SQL queries or simply a dot &quot;.&quot; Here is one such stream&#x27;s traf...'''
date = "2016-03-01T03:05:00Z"
lastmod = "2016-03-01T04:11:00Z"
weight = 50598
keywords = [ "handshake", "packets", "stream", "tcp", "missing" ]
aliases = [ "/questions/50598" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP streams missing first 2 packets of 3-way handshake](/questions/50598/tcp-streams-missing-first-2-packets-of-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 30+ TCP streams in a trace that all have in common that they miss the first 2 packets in the 3-way handshake and have some weird SEQ/ACK numbers going on. The trace is done on the 156.7.53.9 computer. The data being sent is either SQL queries or simply a dot "."</p><p>Here is one such stream's traffic: <a href="https://www.cloudshark.org/captures/ac136803a5cd">https://www.cloudshark.org/captures/ac136803a5cd</a></p><p><strong>Questions:</strong></p><p>-why would a large amount of TCP streams lack the first 2 packets in the handshake? I can't find any signs of packet loss elsewhere in the trace file.</p><p>-The 1st packet in this trace in reality is the 3rd packet of the TCP handshake. Why would the third packet in the handshake contain a "." ? Make sense to anyone?</p><p>-I cannot make sense of the ACKs and SEQ's going up/down all the time. Shouldn't they just keep going up as long as there is no packet loss?</p><p>Thanks, Skjalg</p></div><div id="question-tags" class="tags-container tags">handshake packets stream tcp missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '16, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/223d8af73ae670be0322e46e346a5e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skjalg&#39;s gravatar image" /><p>Skjalg<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skjalg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '16, 03:07</p></div></div><div id="comments-container-50598" class="comments-container"></div><div id="comment-tools-50598" class="comment-tools"></div><div class="clear"></div><div id="comment-50598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50601"></span>

<div id="answer-container-50601" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50601-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace you uploaded contains only TCP_KeepAlive packets with a single garbage byte.<br />
So there have been sessions sitting idle when you started the capture.<br />
Just the sequence and ack number being 1 doesn't make them the 3rd packet of the three-way handshake.<br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '16, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-50601" class="comments-container"><span id="50604"></span><div id="comment-50604" class="comment"><div id="post-50604-score" class="comment-score"></div><div class="comment-text"><p>That's one of the dangers of relative sequence numbers - it can fool you in some situations :-)</p></div><div id="comment-50604-info" class="comment-info"><span class="comment-age">(01 Mar '16, 04:59)</span> Jasper ♦♦</div></div><span id="50639"></span><div id="comment-50639" class="comment"><div id="post-50639-score" class="comment-score"></div><div class="comment-text"><p>The fact that ACKs/SEQs start at 0 regardless of where in the stream you start capturing allured me - makes perfect sense of course :-)</p><p>Did a little search on the garbage byte you mentioned and learned that these are in fact a part of TCP Keep Alives. Since many TCP implementations will not reliably deliver a segment containing only an ACK &amp; no data, it is common to use a garbage octet/byte as payload in a Keep Alive. By lowering the SEQ# accordingly, the receiving end will understand it is a Keep Alive and simply reply to the sender without passing any data to the application layer (since it knows it already acknowledged the data represented by the sender's SEQ#)</p><p>I live and learn :-)</p><p>Thanks Matthias!</p></div><div id="comment-50639-info" class="comment-info"><span class="comment-age">(01 Mar '16, 22:20)</span> Skjalg</div></div></div><div id="comment-tools-50601" class="comment-tools"></div><div class="clear"></div><div id="comment-50601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

