+++
type = "question"
title = "high value in &quot;bytes in flight&quot; and alot retranmission"
description = '''Hi,   after reading on &quot;bytes in flight&quot;, if in my network i saw a high value under &quot;bytes in flight&quot; and sub sequences a lot retransmission, does it mean the remote side is no processing the data fast enough, so the acknowledgment are no being able send back. Due to this it cause the client to retr...'''
date = "2013-04-15T10:22:00Z"
lastmod = "2013-04-15T10:31:00Z"
weight = 20429
keywords = [ "tcp-bytes-in-flight" ]
aliases = [ "/questions/20429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [high value in "bytes in flight" and alot retranmission](/questions/20429/high-value-in-bytes-in-flight-and-alot-retranmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, after reading on "bytes in flight", if in my network i saw a high value under "bytes in flight" and sub sequences a lot retransmission, does it mean the remote side is no processing the data fast enough, so the acknowledgment are no being able send back. Due to this it cause the client to retransmit the data again ? to over come this issue? do i need to slim down the bandwidth for connecting to the server side(WAN) ?</p></div><div id="question-tags" class="tags-container tags">tcp-bytes-in-flight</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '13, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/ba7415b503be15241d880cab78574700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="splibytes&#39;s gravatar image" /><p>splibytes<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="splibytes has no accepted answers">0%</span></p></div></div><div id="comments-container-20429" class="comments-container"></div><div id="comment-tools-20429" class="comment-tools"></div><div class="clear"></div><div id="comment-20429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20431"></span>

<div id="answer-container-20431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20431-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>High values of byte in flight may have two major reasons:</p><ol><li>the receiving node is slow when processing incoming data, which leads to acknowledges being delayed</li><li>the RTT of the link is pretty high, so the sender has to push out a lot of data before the first acknowledge can even make it back to him</li></ol><p>You'll need to check your initial RTT (from the TCP handshake) to be able to tell if the second version is likely or not. Sometimes retransmissions are needlessly issued when a sender gets nervous and sends retransmissions just because the acknowledge takes too long to come back, but you may also have real packet loss. Which is which is something that you need to analyze in your trace - needless retransmissions are usually identified by seeing both retransmission and original, as well as often getting a DSACK option in the acknowledges.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20431" class="comments-container"><span id="20440"></span><div id="comment-20440" class="comment"><div id="post-20440-score" class="comment-score"></div><div class="comment-text"><p>thanks, i found that is does have both retransmission and original ack and the server reply a dsack to the client, sound like packet drop do happen some where in the network.</p></div><div id="comment-20440-info" class="comment-info"><span class="comment-age">(15 Apr '13, 18:32)</span> splibytes</div></div></div><div id="comment-tools-20431" class="comment-tools"></div><div class="clear"></div><div id="comment-20431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

