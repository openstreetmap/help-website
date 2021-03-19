+++
type = "question"
title = "Trying to trobleshooting MS Access database issues on my network"
description = '''Hi. I have an application based on MS Access 2010 database that is sometimes (very) slow over the network. On my server i have a back-end DB and on a client pc i have local front-end DB. So, previously i run test speed measurements over my 1Gb lan (using Iperf tool) and this report a good speed (112...'''
date = "2016-08-22T16:21:00Z"
lastmod = "2016-08-23T06:36:00Z"
weight = 55058
keywords = [ "access", "databaseperformance", "database" ]
aliases = [ "/questions/55058" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to trobleshooting MS Access database issues on my network](/questions/55058/trying-to-trobleshooting-ms-access-database-issues-on-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55058-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I have an application based on MS Access 2010 database that is sometimes (very) slow over the network. On my server i have a back-end DB and on a client pc i have local front-end DB. So, previously i run test speed measurements over my 1Gb lan (using Iperf tool) and this report a good speed (112 MBytes sec, optimal throughput). Running a session with wireshark shows me there is no problem on the network, but if i follow the stream between server and client i notice a (sometimes great) delay from client request and not from server response (or maybe i committed an error to read the trace? please see the picture, i'm not an expert). Thanks in advance.<img src="https://i.imgsafe.org/b884b264d1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">access databaseperformance database</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '16, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/b753d4f23394391316454795cbcf6036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlogiga&#39;s gravatar image" /><p>carlogiga<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlogiga has no accepted answers">0%</span></p></img></div></div><div id="comments-container-55058" class="comments-container"></div><div id="comment-tools-55058" class="comment-tools"></div><div class="clear"></div><div id="comment-55058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55073"></span>

<div id="answer-container-55073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Debugging by screenshots is close to impossible, but your screenshot shows that it takes the client 29 seconds from acknowledging the previous packet to think through what else it wants from the server. As such it looks as an application issue so Wireshark is not the tool to tell you more than this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '16, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Aug '16, 06:36</p></div></div><div id="comments-container-55073" class="comments-container"><span id="55292"></span><div id="comment-55292" class="comment"><div id="post-55292-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you reply. If i can confirm a theory that proves the issues is caused by a slow response by MS Access (and not by buggy or misconfigured network) it's ok for me. Because in this case i can test other configurations like putting both front-end and back-end DB on a SSD unit on the server, for example.</p></div><div id="comment-55292-info" class="comment-info"><span class="comment-age">(02 Sep '16, 06:30)</span> carlogiga</div></div></div><div id="comment-tools-55073" class="comment-tools"></div><div class="clear"></div><div id="comment-55073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

