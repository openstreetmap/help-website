+++
type = "question"
title = "Why would a server ack a packet and then ack the same packet plus one?"
description = '''An FTPS upload sometimes works and sometimes fails. The client sends all the data but has not had it all acknowledged. It then sends FIN to close it&#x27;s half session. The server is sending DUP ACKs because it has not receives several of the packets. The DUP ACKs result in retransmissions as they shoul...'''
date = "2015-10-05T06:18:00Z"
lastmod = "2015-10-05T06:18:00Z"
weight = 46365
keywords = [ "ack", "early", "command", "fin" ]
aliases = [ "/questions/46365" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why would a server ack a packet and then ack the same packet plus one?](/questions/46365/why-would-a-server-ack-a-packet-and-then-ack-the-same-packet-plus-one)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46365-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>An FTPS upload sometimes works and sometimes fails. The client sends all the data but has not had it all acknowledged. It then sends FIN to close it's half session. The server is sending DUP ACKs because it has not receives several of the packets. The DUP ACKs result in retransmissions as they should. The server ACKs a retransmission of a 1460 byte packet and then ACKs one byte more. The client retransmits one byte past the previous segment. Server asks for the original next segment but does not accept it.</p><pre><code>-&gt; seq 36044 len 1460 next seq 37504 
&lt;- Dup ACK 37504
-&gt; seq 37504 len 1460 next seq 38964
&lt;- ACK 37505                              **** SEEMS QUITE ABNORMAL ****** 
-&gt; seq 37505 len 1460 next seq 38965  TCP OUT OF ORDER     ****** BUT RETRANSMITTED ANYWAY *****
&lt;- Dup ACK 37505                          ********* This cones back immediately  
&lt;- Ack 38964                              ********* NOW BACK TO NORMAL BUT REJECTED BY SERVER
-&gt; seq 38964 len 1460 next seq 40424      ********* NEVER GETS PAST THIS ************
&lt;- Ack 38964</code></pre><p>The retransmitted data occurs after RTO. Each duplicate ACK comes back one RTT later (.203,..486, 1.007, 2, 4, 8, 16)until server sends FIN at sequence 146 which is Acked as 147. Server resets.</p><pre><code>&lt;- seq 146 0 next seq 38964
-&gt; Ack 147      
&lt;- RST  seq 147</code></pre><p>To me it seems like the client has received the ACK for a FIN with an incorrect and very early sequence number. It won't except anymore data - it thinks it is done?</p><p>Sessions that don't have this odd Ack+1 all work.</p><p>Have you ever seen anything like this? I don't think there is anything but firewalls and the internet between client and server. I can't blame this on a proxy.</p><p>Please let me know what you think.</p><p>Thank you</p><p>R F Hayden</p></div><div id="question-tags" class="tags-container tags">ack early command fin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '15, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/3ed0568ce0feb88b20bd673ba0a380a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arfhayden&#39;s gravatar image" /><p>arfhayden<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arfhayden has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '15, 06:24</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46365" class="comments-container"><span id="46381"></span><div id="comment-46381" class="comment"><div id="post-46381-score" class="comment-score"></div><div class="comment-text"><p>Hard to comment on this description, can you share the capture file somewhere? Are the TTLs of the 'server' the same or are they different on the suspicious ACKs (&lt;- ACK 37505) ?</p></div><div id="comment-46381-info" class="comment-info"><span class="comment-age">(06 Oct '15, 06:44)</span> mrEEde</div></div></div><div id="comment-tools-46365" class="comment-tools"></div><div class="clear"></div><div id="comment-46365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

