+++
type = "question"
title = "Apache server issue reset"
description = '''I have an apache server communicating with a server where the apache serve is ack as a proxy I am seeing reset when the two servers attempt to communicate with each other. I see the same Behavior in frame 6, 12, 17 and 23 just before the reset in each frame REQ: CPING AND A REQ: CPONG.  I have no id...'''
date = "2013-07-19T12:35:00Z"
lastmod = "2013-07-22T06:00:00Z"
weight = 23180
keywords = [ "apache_trace_files" ]
aliases = [ "/questions/23180" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Apache server issue reset](/questions/23180/apache-server-issue-reset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23180-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an apache server communicating with a server where the apache serve is ack as a proxy I am seeing reset when the two servers attempt to communicate with each other. I see the same Behavior in frame 6, 12, 17 and 23 just before the reset in each frame REQ: CPING AND A REQ: CPONG. I have no idea what that means can some help me with this pending issue 10.97.4.128 &lt; --- &gt; 10.97.12.142 Port 8009 port 8443 port 8080</p><p>Thanks in advanced</p><p><a href="https://www.cloudshark.org/captures/e51813ca818f">https://www.cloudshark.org/captures/e51813ca818f</a></p></div><div id="question-tags" class="tags-container tags">apache_trace_files</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '13, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p>ejohnson7<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-23180" class="comments-container"><span id="23183"></span><div id="comment-23183" class="comment"><div id="post-23183-score" class="comment-score"></div><div class="comment-text"><p>“socket 256 [10.97.4.128:50196 -&gt; 10.97.12.142:8009] and read 0 lingering bytes in 0 sec. jk_ajp_common.c (1267): (nodo1) can't receive the response header message from tomcat, network problems or tomcat (10.97.12.142:8009) is down (errno=54)</p></div><div id="comment-23183-info" class="comment-info"><span class="comment-age">(19 Jul '13, 15:51)</span> ejohnson7</div></div><span id="23184"></span><div id="comment-23184" class="comment"><div id="post-23184-score" class="comment-score"></div><div class="comment-text"><p>additional information about the issue just posted</p></div><div id="comment-23184-info" class="comment-info"><span class="comment-age">(19 Jul '13, 15:51)</span> ejohnson7</div></div></div><div id="comment-tools-23180" class="comment-tools"></div><div class="clear"></div><div id="comment-23180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23193"></span>

<div id="answer-container-23193" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23193-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The mentioned connection " 10.97.4.128 &lt; --- &gt; 10.97.12.142 Port 8009 port 8443 port 8080" is not inside the trace file.</p><p>In general: What do you expect from us in terms of what exactly is your question? You already asked a very related question with RST packets and got many useful hints, so I'm kind of confused what the problem in this trace is that you have to solve.</p><p>Don't get me wrong please but since this is no wireshark related question and people here are spending their spare time to look into issues you should keep that in mind and be a little more precise about your specifics.</p><p>In terms of what REQ: CPING AND A REQ: CPONG are, a simple Google Search for that string provides all info you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '13, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-23193" class="comments-container"><span id="23202"></span><div id="comment-23202" class="comment"><div id="post-23202-score" class="comment-score"></div><div class="comment-text"><p>Sorry it is labeled wrong and I should not have past this in to mislead you, but my question is do you think that the server 10.97.4.128 is resetting because it is not listing on port 8009? It occurs many all through the capture</p><p>And once again sorry for the misleading question</p><p>Thanks</p></div><div id="comment-23202-info" class="comment-info"><span class="comment-age">(20 Jul '13, 19:14)</span> ejohnson7</div></div><span id="23206"></span><div id="comment-23206" class="comment"><div id="post-23206-score" class="comment-score">1</div><div class="comment-text"><p>The Server at 10.97.4.128 is listening on port 8009, otherwise it wouldn't set up the TCP 3-way-handshake successfully and even answer to the CPING Request. For me, the reset is the normal way to close the connection after the client successfully CPINGed the server.</p></div><div id="comment-23206-info" class="comment-info"><span class="comment-age">(21 Jul '13, 06:06)</span> Landi</div></div><span id="23216"></span><div id="comment-23216" class="comment"><div id="post-23216-score" class="comment-score"></div><div class="comment-text"><p>Thanks Landi for the Reply</p></div><div id="comment-23216-info" class="comment-info"><span class="comment-age">(21 Jul '13, 13:08)</span> ejohnson7</div></div></div><div id="comment-tools-23193" class="comment-tools"></div><div class="clear"></div><div id="comment-23193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23225"></span>

<div id="answer-container-23225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23225-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K., from your <a href="http://ask.wireshark.org/questions/23109/what-are-all-the-reset">other question</a> we know, that the IP address (10.97.54.9) is a load balancer and that there are recurrent service checks where the LB tears down the TCP connection with a RESET.</p><p>Looking at your sample trace, I see repeating requests from 10.97.4.128 to 10.97.12.142. Although there is no noticeable constant interval, couldn't these connections be also probe request from the LB (or another involved system) to figure out if your Apache Jserv server is still available? Is the client IP (10.97.4.128) an IP address of the load balancer <strong>or</strong> or any other monitoring system (like Nagios)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '13, 06:00</p></div></div><div id="comments-container-23225" class="comments-container"><span id="23245"></span><div id="comment-23245" class="comment"><div id="post-23245-score" class="comment-score"></div><div class="comment-text"><p>not Kurt the ip address 10.97.4.128 is the Server</p></div><div id="comment-23245-info" class="comment-info"><span class="comment-age">(22 Jul '13, 11:22)</span> ejohnson7</div></div><span id="23246"></span><div id="comment-23246" class="comment"><div id="post-23246-score" class="comment-score"></div><div class="comment-text"><p>i am still working with the user and will updata you thanks</p></div><div id="comment-23246-info" class="comment-info"><span class="comment-age">(22 Jul '13, 11:25)</span> ejohnson7</div></div><span id="23268"></span><div id="comment-23268" class="comment"><div id="post-23268-score" class="comment-score"></div><div class="comment-text"><p>Ho can it be the "server" if it initiates the TCP connection? What does the term 'server' mean in your context? Apache server? If so, what is the system with the IP address 10.97.12.142? Is it a Tomcat server on a different system? If so, the traffic is (most likely) simple 'service check traffic', as @Landi already mentioned.</p></div><div id="comment-23268-info" class="comment-info"><span class="comment-age">(22 Jul '13, 16:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23225" class="comment-tools"></div><div class="clear"></div><div id="comment-23225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

