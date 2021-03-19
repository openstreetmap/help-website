+++
type = "question"
title = "Modbus PLC is pre-maturely ending TCP session"
description = '''I have a scenario where a Modbus Master is polling a slave using Modbus TCP. A session is established, and then the Slave / PLC inadvertently sends a Fin,Ack and ends the Session before the Modbus Request is sent. I have looked through the packets looking at Timing , thinking that it is a timeout is...'''
date = "2015-12-15T15:48:00Z"
lastmod = "2015-12-17T10:24:00Z"
weight = 48553
keywords = [ "terminated", "session", "tcp" ]
aliases = [ "/questions/48553" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Modbus PLC is pre-maturely ending TCP session](/questions/48553/modbus-plc-is-pre-maturely-ending-tcp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48553-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a scenario where a Modbus Master is polling a slave using Modbus TCP. A session is established, and then the Slave / PLC inadvertently sends a Fin,Ack and ends the Session before the Modbus Request is sent. I have looked through the packets looking at Timing , thinking that it is a timeout issue, looking for un-expected ACK's or something like that, but nothing is apparent. I was wondering if anyone has had similar issues and could point me in the correct direction? What could cause the slave / server to end the session? The Master is at Port 3172</p><p>TCP: 3172 → 502 [SYN] Seq=0 Win=512 Len=0 MSS=532</p><p>TCP: 502 → 3172 [SYN, ACK] Seq=0 Ack=1 Win=512 Len=0 MSS=532</p><p>TCP: 3172 → 502 [ACK] Seq=1 Ack=1 Win=512 Len=0</p><p>TCP: 502 → 3172 [FIN, ACK] Seq=1 Ack=1 Win=512 Len=0</p><p>Modbus/TCP: Query: Trans: 101; Unit: 1, Func: 5: Write Single Coil</p></div><div id="question-tags" class="tags-container tags">terminated session tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/004329e8e48f3a975aae19e1ae75b57a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Little%20Sqrt&#39;s gravatar image" /><p>Little Sqrt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Little Sqrt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '15, 11:08</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48553" class="comments-container"><span id="48565"></span><div id="comment-48565" class="comment"><div id="post-48565-score" class="comment-score"></div><div class="comment-text"><p>We can't really help by just looking at your text excerpts of the TCP header details of the traffic. You haven't even shown the TCP header from the packet with the request.</p><p>Please post the actual capture somewhere publicly accessible, e.g. Google Drive, Dropbox etc.</p></div><div id="comment-48565-info" class="comment-info"><span class="comment-age">(16 Dec '15, 04:16)</span> grahamb ♦</div></div></div><div id="comment-tools-48553" class="comment-tools"></div><div class="clear"></div><div id="comment-48553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48563"></span>

<div id="answer-container-48563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48563-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check out this blog post:</p><p><a href="https://blog.packet-foo.com/2014/01/tcp-server-slamming-the-door/">https://blog.packet-foo.com/2014/01/tcp-server-slamming-the-door/</a></p><p>I'm not sure how much of it applies to Modbus, but it looks like a classical "no, you're not in my list of IPs I can talk to" aborts.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Dec '15, 04:13</p></div></div><div id="comments-container-48563" class="comments-container"><span id="48616"></span><div id="comment-48616" class="comment"><div id="post-48616-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, turns out that the PLC(server) is setup to receive Modbus requests from a particular port and IP, if it doesn't match, then it terminates the session.</p></div><div id="comment-48616-info" class="comment-info"><span class="comment-age">(17 Dec '15, 10:17)</span> Little Sqrt</div></div></div><div id="comment-tools-48563" class="comment-tools"></div><div class="clear"></div><div id="comment-48563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48617"></span>

<div id="answer-container-48617" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48617-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It turns out that the PLC (Server) is programmed to accept requests from a particular Port number. Consequently, I think that Jasper hit the nail on the head.</p><p>The thing that we can't figure out, is why the SRC Port numbers are incrementing upon each successive session??</p><p><a href="https://www.dropbox.com/s/whb0h1r55mn15cr/Server_Terminating_TCP_Session.pcapng?dl=0">https://www.dropbox.com/s/whb0h1r55mn15cr/Server_Terminating_TCP_Session.pcapng?dl=0</a></p><p>Here is the code if you want to have a look.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '15, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/004329e8e48f3a975aae19e1ae75b57a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Little%20Sqrt&#39;s gravatar image" /><p>Little Sqrt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Little Sqrt has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-48617" class="comments-container"><span id="48619"></span><div id="comment-48619" class="comment"><div id="post-48619-score" class="comment-score"></div><div class="comment-text"><p>This is a different question (and definitely not an answer to the existing one), so you should either raise it as such yourself or confirm that I may convert what you've just written into a new question.</p><p>But to give you the response quickly, using a different source tcp port when creating a new session is a normal client behaviour, as the pair of client and server sockets (ip:port) is the only identifier of the session to which a given packet belongs. So after closing one session, it is a good idea not to reuse the same socket pair for new sessions for some time, otherwise arrival of a delayed packet from the previous session could confuse the current session.</p><p>So after re-reading what you wrote (that the PLC expects the tcp requests to come from a single remote port), I wonder what were the reasons of the author of the PLC software (configuration?) to do so.</p></div><div id="comment-48619-info" class="comment-info"><span class="comment-age">(17 Dec '15, 11:00)</span> sindy</div></div></div><div id="comment-tools-48617" class="comment-tools"></div><div class="clear"></div><div id="comment-48617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

