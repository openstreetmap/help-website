+++
type = "question"
title = "ack vs read app"
description = '''hello, TCP as a streaming protocol.Question is when the receiver is acknowledging an packet will it still wait for the application to read the data from the buffer and only than remove it from the buffer?  Thank you'''
date = "2016-03-12T15:16:00Z"
lastmod = "2016-03-13T00:02:00Z"
weight = 50848
keywords = [ "ack" ]
aliases = [ "/questions/50848" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ack vs read app](/questions/50848/ack-vs-read-app)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50848-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>TCP as a streaming protocol.Question is when the receiver is acknowledging an packet will it still wait for the application to read the data from the buffer and only than remove it from the buffer?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '16, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-50848" class="comments-container"></div><div id="comment-tools-50848" class="comment-tools"></div><div class="clear"></div><div id="comment-50848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50849"></span>

<div id="answer-container-50849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50849-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Of course - acknowledging packets only means that it has been received and put into the receive window buffer. As soon as the application picks up the packet (well, the "segment", to be more exact) the free receive window size grows again. That's why you sometimes see the window size drop - that's when the packets were acknowledged, but the application is slow in pulling segments from the window buffer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '16, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50849" class="comments-container"><span id="50850"></span><div id="comment-50850" class="comment"><div id="post-50850-score" class="comment-score"></div><div class="comment-text"><p>How could I troubleshoot whether it's the network or host / application that is slowing down the performance? Could I use Wirehsark for this ?</p></div><div id="comment-50850-info" class="comment-info"><span class="comment-age">(13 Mar '16, 01:36)</span> adasko</div></div><span id="50851"></span><div id="comment-50851" class="comment"><div id="post-50851-score" class="comment-score">1</div><div class="comment-text"><p>Sure. It depends on your capture location and skill of analyzing TCP behavior. If you don't see massive packet loss or delays caused by the network (for which you'd need to capture both at client and server and compare the packets) it's usually the application.</p></div><div id="comment-50851-info" class="comment-info"><span class="comment-age">(13 Mar '16, 01:40)</span> Jasper ♦♦</div></div><span id="50853"></span><div id="comment-50853" class="comment"><div id="post-50853-score" class="comment-score"></div><div class="comment-text"><p>Could it be also the host itself not just the application ?</p></div><div id="comment-50853-info" class="comment-info"><span class="comment-age">(13 Mar '16, 04:17)</span> adasko</div></div><span id="50854"></span><div id="comment-50854" class="comment"><div id="post-50854-score" class="comment-score"></div><div class="comment-text"><p>Yes, but that's still harder to prove usually. You'd look at slow TCP based reaction times (to see that the stack is under stress) and other things. I'd recommend checking the host stats with onboard performance monitoring.</p></div><div id="comment-50854-info" class="comment-info"><span class="comment-age">(13 Mar '16, 04:28)</span> Jasper ♦♦</div></div><span id="50855"></span><div id="comment-50855" class="comment"><div id="post-50855-score" class="comment-score"></div><div class="comment-text"><p>so an indication that the problem is with the receiving app would be a small window size advertised to the sender even though packets are getting ACK'ed ?</p></div><div id="comment-50855-info" class="comment-info"><span class="comment-age">(13 Mar '16, 04:55)</span> adasko</div></div></div><div id="comment-tools-50849" class="comment-tools"></div><div class="clear"></div><div id="comment-50849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

