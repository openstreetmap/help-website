+++
type = "question"
title = "TCP receive window"
description = '''Hello, I am trying to undestand TCP receive window. For example, on a iperf test, if I plot the TCP Time-Sequence Graph selecting any packet from client to server (remember iperf makes the test moving data from client to server), i see the above line looks like it is limiting the sender to send more...'''
date = "2015-04-26T00:26:00Z"
lastmod = "2015-04-27T07:25:00Z"
weight = 41849
keywords = [ "receive", "window", "tcp" ]
aliases = [ "/questions/41849" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP receive window](/questions/41849/tcp-receive-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to undestand TCP receive window. For example, on a iperf test, if I plot the TCP Time-Sequence Graph selecting any packet from client to server (remember iperf makes the test moving data from client to server), i see the above line looks like it is limiting the sender to send more data. But how that info can be found from a client to server packet? If I am not wrong, the "windows size" is the RWIN size, which means the amount of data that can be "received" by the client, which is not what we want to test. Am I correct?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags">receive window tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '15, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/c03858acb70e7fc056be382cd384dcbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luicson&#39;s gravatar image" /><p>luicson<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luicson has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 26 Apr '15, 05:21</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41849" class="comments-container"></div><div id="comment-tools-41849" class="comment-tools"></div><div class="clear"></div><div id="comment-41849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41886"></span>

<div id="answer-container-41886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41886-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>RWIN is the amount of data that can be received by the <strong>receiver</strong>, meaning: the node that gets the data. It doesn't matter what you call a client or a server; both have window sizes. The window size of one is the amount the other can send without having to wait for an ACK, and vice versa. So if your "client" is sending data to the "server" it's the server's RWIN that matters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41886" class="comments-container"></div><div id="comment-tools-41886" class="comment-tools"></div><div class="clear"></div><div id="comment-41886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41884"></span>

<div id="answer-container-41884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41884-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your question is about TCP Window size and Flow control, I think this section from the TCP/IP Guide should provide you the best answer:</p><p><a href="http://www.tcpipguide.com/free/t_TCPWindowSizeAdjustmentandFlowControl-2.htm">http://www.tcpipguide.com/free/t_TCPWindowSizeAdjustmentandFlowControl-2.htm</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-41884" class="comments-container"></div><div id="comment-tools-41884" class="comment-tools"></div><div class="clear"></div><div id="comment-41884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

