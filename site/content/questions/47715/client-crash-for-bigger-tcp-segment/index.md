+++
type = "question"
title = "[closed] Client crash for bigger TCP segment"
description = '''hi, 1) I am sending 4000 Bytes data by following command count =write(nd,&quot; xxxxxxxxxxxxx.... 4000 times&quot; &quot;,4000); 2) confirmed by printing count in the socket programe and by wireshark also last packet is having PSH flag also... 3) But Rx side 1448 bytes only printing Client is sending reset the con...'''
date = "2015-11-18T06:44:00Z"
lastmod = "2015-11-18T07:04:00Z"
weight = 47715
keywords = [ "rst", "tcpflags" ]
aliases = [ "/questions/47715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Client crash for bigger TCP segment](/questions/47715/client-crash-for-bigger-tcp-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>1) I am sending 4000 Bytes data by following command count =write(nd," xxxxxxxxxxxxx.... 4000 times" ",4000);</p><p>2) confirmed by printing count in the socket programe and by wireshark also</p><p>last packet is having PSH flag also... 3) But Rx side 1448 bytes only printing</p><p>Client is sending reset the connection ???? I under stood client is crashing ???? Some one told me to send the last packet with out PUSH flag...</p><p>Can u tell how to send last packet without push flag ???</p><p>Why my client is crashing ??? what is the best solution ????</p><p>Problem is much similar to</p><p><a href="https://ask.wireshark.org/questions/47542/tcp-retransmission-server-sends-wrong-seqno">https://ask.wireshark.org/questions/47542/tcp-retransmission-server-sends-wrong-seqno</a></p><p>regards</p></div><div id="question-tags" class="tags-container tags">rst tcpflags</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p>srinu_bel<br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 18 Nov '15, 06:59</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-47715" class="comments-container"><span id="47718"></span><div id="comment-47718" class="comment"><div id="post-47718-score" class="comment-score"></div><div class="comment-text"><p>Not a topic for Wireshark, this is a network programming question.</p></div><div id="comment-47718-info" class="comment-info"><span class="comment-age">(18 Nov '15, 06:59)</span> grahamb ♦</div></div></div><div id="comment-tools-47715" class="comment-tools"></div><div class="clear"></div><div id="comment-47715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 18 Nov '15, 06:59

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47719"></span>

<div id="answer-container-47719" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47719-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not the right place to ask, I'd ask that at <a href="http://stackoverflow.com/questions">Stackoverflow programmers' Q&amp;A</a>, because it is an application and/or driver related question, not Wireshark or network traffic analysis one.</p><p>But by not sending the PSH flag you'll likely not save the receiving application from crashing, as the PSH flag just tells the receiving tcp stack to flush the buffer towards the application without eventually waiting for more packets to arrive. So in my understanding, the solution would be to send smaller packets <strong>with</strong> PSH flag at the sending side, so that the application never receives too much data in one batch.</p><p>I would even dare to speculate that various applications may suffer from the same issue as their authors have misunderstood the tcp concept of a stream and can only handle messages whose size matches the popular MTU.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '15, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47719" class="comments-container"></div><div id="comment-tools-47719" class="comment-tools"></div><div class="clear"></div><div id="comment-47719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

