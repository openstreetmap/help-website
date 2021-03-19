+++
type = "question"
title = "TCP - server sends ACK RST right after ACK"
description = '''First and foremost: I&#x27;m not actually a network or system engineer so apologies in advance if I&#x27;m asking any noob questions. I&#x27;m currently experiencing erratic behaviour from a web server that I&#x27;m using. It has been working for several years without any issues but since a couple of days we are gettin...'''
date = "2016-04-01T01:05:00Z"
lastmod = "2016-04-01T01:11:00Z"
weight = 51332
keywords = [ "connection_reset", "reset", "tcp" ]
aliases = [ "/questions/51332" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP - server sends ACK RST right after ACK](/questions/51332/tcp-server-sends-ack-rst-right-after-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51332-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First and foremost: I'm not actually a network or system engineer so apologies in advance if I'm asking any noob questions.</p><p>I'm currently experiencing erratic behaviour from a web server that I'm using. It has been working for several years without any issues but since a couple of days we are getting (at random points in time) socket reconnect errors. When tracing this through Wireshark, I see that the SYN-handshake seems to be performed well, the HTTP GET gets an ACK packet, but then the server sends an RST, ACK packet, causing the session to be ended abruptly. At other times though, this doesn't give any issues and the server proceeds to transfer data.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_gjp2V82.PNG" alt="alt text" /> I was able to obtain a similar trace at server side, and it shows the same behaviour, so it doesn't look like packets are being dropped.</p><p>So my question would be:</p><p>is there any way I can find out wat the cause for the RST ACK packet was? Is it send by the TCP/IP stack at the server? Or can it be triggered by the web server application itself? Or can it be triggered by network devices in the middle, even though the source and destination address in the packets seem to only refer to the client and server?</p><p>Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">connection_reset reset tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '16, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/2fb30c9a2084996d1f7e29d4a07d255e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PLombaer&#39;s gravatar image" /><p>PLombaer<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PLombaer has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51332" class="comments-container"></div><div id="comment-tools-51332" class="comment-tools"></div><div class="clear"></div><div id="comment-51332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51333"></span>

<div id="answer-container-51333" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51333-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually this kind of behavior happens if the application on the server doesn't want to talk to the client IP (which the application only gets notified about after the handshake). It's not the TCP stack itself that sends the RST, it's doing it because the application closed the socket.</p><p>See also <a href="https://blog.packet-foo.com/2014/01/tcp-server-slamming-the-door/">https://blog.packet-foo.com/2014/01/tcp-server-slamming-the-door/</a> for some thoughts about a similar case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '16, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51333" class="comments-container"><span id="51337"></span><div id="comment-51337" class="comment"><div id="post-51337-score" class="comment-score"></div><div class="comment-text"><p>Hello Jasper, thanks for your reply. In the example you've shown, the refusal of the ftp server application seems to be based on blacklisted/whitelisted ip addresses. Is a connection refusal (at this level) always based on one of the tcp/ip protocol characteristics? Or could it be based on anything which the application decides to reset the connection for?</p></div><div id="comment-51337-info" class="comment-info"><span class="comment-age">(01 Apr '16, 01:49)</span> PLombaer</div></div><span id="51338"></span><div id="comment-51338" class="comment"><div id="post-51338-score" class="comment-score"></div><div class="comment-text"><p>it can be anything that makes the application close the socket. So it can be a blacklist/whitelist of any kind (usually IP based), or maybe an internal problem that forces it to abort serving the page (but you'd normally see a 5xx error for those).</p><p>I've also seen web frameworks not being able to deal with a high amount of concurrent sessions, either for performance reasons or license issues. Those are problems that usually show up after the application has run fine for a while (sometimes months) and the concurrent sessions increasing over time until they start to fail when more and more users are added.</p></div><div id="comment-51338-info" class="comment-info"><span class="comment-age">(01 Apr '16, 02:00)</span> Jasper ♦♦</div></div></div><div id="comment-tools-51333" class="comment-tools"></div><div class="clear"></div><div id="comment-51333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

