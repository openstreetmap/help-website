+++
type = "question"
title = "respond and connection time"
description = '''Hi everybody, I&#x27;m new user in wireshark. I have 2 ip address (client and server), i need to determine the connection time and the respond time between the 2. is it the tcp delta time? Thank you for your help.'''
date = "2015-03-30T01:39:00Z"
lastmod = "2015-03-30T03:57:00Z"
weight = 40990
keywords = [ "http", "tcp" ]
aliases = [ "/questions/40990" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [respond and connection time](/questions/40990/respond-and-connection-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40990-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I'm new user in wireshark. I have 2 ip address (client and server), i need to determine the connection time and the respond time between the 2. is it the tcp delta time?</p><p>Thank you for your help.</p></div><div id="question-tags" class="tags-container tags">http tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '15, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/90875c0c2524531263f27b57e1d27ea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hub&#39;s gravatar image" /><p>hub<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hub has no accepted answers">0%</span></p></div></div><div id="comments-container-40990" class="comments-container"></div><div id="comment-tools-40990" class="comment-tools"></div><div class="clear"></div><div id="comment-40990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40994"></span>

<div id="answer-container-40994" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40994-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without a clear definition of "connection time" and "response time", I can only guess what you are asking for, so here is my first attempt.</p><p><strong>connection time:</strong></p><p>If you are interested in the time between SYN and SYN ACK, or the time it takes for the three-way handshake, you can set a time reference on the SYN flag (click on the frame and press CTRL-T) and then look at the timestamp of SYN-ACK or the timestamp of the first data frame. See (1) and (2) in the screenshot below.</p><p><strong>response time:</strong></p><p>This can be virtually anything, from RTT analysis at TCP level up to response time for a HTTP GET. See (3) (time reference for GET) and (4) answer from server (some tools call this "first byte") and (5) final frame of the answer (wireshark shows the HTTP answer in the info field in the last frame.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/response_time_analysis.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 30 Mar '15, 09:48</p></div></div><div id="comments-container-40994" class="comments-container"><span id="41025"></span><div id="comment-41025" class="comment"><div id="post-41025-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much</p></div><div id="comment-41025-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:52)</span> hub</div></div><span id="41026"></span><div id="comment-41026" class="comment"><div id="post-41026-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p></div><div id="comment-41026-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40994" class="comment-tools"></div><div class="clear"></div><div id="comment-40994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

