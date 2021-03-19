+++
type = "question"
title = "Trying to understand Nagle"
description = '''I&#x27;ve been going thru some information about Nagle and Delayed ACKs and looking at some trace files of my own to see the the concepts in play. Here&#x27;s a partial of the trace I&#x27;ve been looking at. What I don&#x27;t understand is how packet 345 is getting put on the wire.  Packet 344 went out because it is f...'''
date = "2013-10-26T17:14:00Z"
lastmod = "2013-10-27T02:18:00Z"
weight = 26431
keywords = [ "nagle" ]
aliases = [ "/questions/26431" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to understand Nagle](/questions/26431/trying-to-understand-nagle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26431-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been going thru some information about Nagle and Delayed ACKs and looking at some trace files of my own to see the the concepts in play. Here's a partial of the trace I've been looking at. What I don't understand is how packet 345 is getting put on the wire.<br />
</p><p>Packet 344 went out because it is full MSS, but why did 345 go out before the ACK was received for 344? Doesn't that violate the Nagle buffering rule? Even if the PSH bit was set on packet 345 it shouldn't have gone out because there was unacknowledged traffic (344) on the wire unless the hold-down timer expired, right?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Nagle.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">nagle</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '13, 17:14</strong></p><img src="https://secure.gravatar.com/avatar/9501a0a9cba9c6ae399345ab0baf8b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsuida&#39;s gravatar image" /><p>dsuida<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsuida has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-26431" class="comments-container"></div><div id="comment-tools-26431" class="comment-tools"></div><div class="clear"></div><div id="comment-26431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26433"></span>

<div id="answer-container-26433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26433-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that the Nagle algorithm buffered more bytes than it cold fit into a single packet while waiting for the ACK that is coming in in packet 343, so it sends two packets (344 and 345). I base that assumption on the fact that the Size for packet 344 is 1500 according to your length column, so I guess that is the Ethernet payload size, and it is full.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '13, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26433" class="comments-container"><span id="26439"></span><div id="comment-26439" class="comment"><div id="post-26439-score" class="comment-score"></div><div class="comment-text"><ol><li>341 and 342 are the 3-way handshake. 343 - the client send 390 with PSH bit set. Data goes right away as there are no unACK'd packets. 344 - Server sends data and piggy-backs ACK for 343. 345 - server sends another chunk of data with PSH set, but is not MSS size and with very little delay. Nagle should not let this go, because it's not full MSS, as the client has not ACK'd 344 yet, nor has the Nagle timer expired (guessing on that last statement).</li></ol><p>Are you suggesting the Nagle timer has expired?</p></div><div id="comment-26439-info" class="comment-info"><span class="comment-age">(27 Oct '13, 08:51)</span> dsuida</div></div><span id="26446"></span><div id="comment-26446" class="comment"><div id="post-26446-score" class="comment-score"></div><div class="comment-text"><p>Oh, I oversaw the PSH bit being mentioned - PSH bits force immediate sending, overruling Nagle buffering. It is usually set for the last packet of a transmission consisting of multiple packets, so that there is no artificial delay caused by the wait for additional data that will never happen.</p></div><div id="comment-26446-info" class="comment-info"><span class="comment-age">(27 Oct '13, 11:13)</span> Jasper ♦♦</div></div></div><div id="comment-tools-26433" class="comment-tools"></div><div class="clear"></div><div id="comment-26433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

