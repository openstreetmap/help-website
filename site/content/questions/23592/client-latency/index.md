+++
type = "question"
title = "client latency"
description = '''Hi, I came across a trace where my monitoring point is close to the client. I am looking at the response time of the basic TCP handshake SYN- SYN/ACK ACK My SYN/ACK from the server takes reasonable time but my ACK from the client is sporadic and taking longer time. what could be the potential reason...'''
date = "2013-08-06T16:12:00Z"
lastmod = "2013-08-08T02:52:00Z"
weight = 23592
keywords = [ "client", "response", "time" ]
aliases = [ "/questions/23592" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [client latency](/questions/23592/client-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23592-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I came across a trace where my monitoring point is close to the client. I am looking at the response time of the basic TCP handshake SYN- SYN/ACK ACK</p><p>My SYN/ACK from the server takes reasonable time but my ACK from the client is sporadic and taking longer time.</p><p>what could be the potential reason the client is taking longer time to ACK.</p></div><div id="question-tags" class="tags-container tags">client response time</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '13, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/adfa43f849103e9c0bbbbd91e819760e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pappu&#39;s gravatar image" /><p>pappu<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pappu has no accepted answers">0%</span></p></div></div><div id="comments-container-23592" class="comments-container"></div><div id="comment-tools-23592" class="comment-tools"></div><div class="clear"></div><div id="comment-23592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23594"></span>

<div id="answer-container-23594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I interpret the issue as: Mostly the ack from the client comes in within sub-ms but occasionally it takes x ms. There are two reasons why this could happen:</p><ol><li>The client's TCP didn't see the syn-ack in time</li><li>The client's TCP didn't process the packet in time</li></ol><p>My first guess would be the client is running in a virtualized environment and doesn't get dispatched in time. Do you see higher delays also later in the conversation?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '13, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-23594" class="comments-container"><span id="25350"></span><div id="comment-25350" class="comment"><div id="post-25350-score" class="comment-score"></div><div class="comment-text"><p>thank you for your reply.... clients are not running in virtual environment. It is a regular PC at a store which has T1 connectivity back to the datacenter. I have a feeling the PC is late in processing ...probably old PC....some application like java on the PC is taking time to process the data received.</p></div><div id="comment-25350-info" class="comment-info"><span class="comment-age">(29 Sep '13, 18:41)</span> pappu</div></div></div><div id="comment-tools-23594" class="comment-tools"></div><div class="clear"></div><div id="comment-23594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23634"></span>

<div id="answer-container-23634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23634-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>what could be the potential reason</strong> the client is taking longer time to ACK.</p></blockquote><p>a large network load on the client. If the internal transmit buffers are filled up, it will take longer to get the ACK out on the line.</p><p>There is probably also a duplex problem on the client. If the client works in half duplex mode and receives/sends a lot of traffic, this could also cause delays in sending the ACKs, due to collisions and other network related problems.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23634" class="comments-container"></div><div id="comment-tools-23634" class="comment-tools"></div><div class="clear"></div><div id="comment-23634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

