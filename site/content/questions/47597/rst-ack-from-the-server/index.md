+++
type = "question"
title = "RST ACK from the server"
description = '''Hi All, Please advise on the below. I checked and RST-ACK is like FIN-ACK to close the connection. The problem is when this happens the webpage is not displayed. Say the TCP session is between 10.1.1.1 and 10.1.1.2 10.1.1.1----&amp;gt;syn 10.1.1.2 10.1.1.2----&amp;gt;syn-ack 10.1.1.1 10.1.1.1----&amp;gt;ack 10....'''
date = "2015-11-14T00:12:00Z"
lastmod = "2015-11-14T23:24:00Z"
weight = 47597
keywords = [ "rst+ack" ]
aliases = [ "/questions/47597" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [RST ACK from the server](/questions/47597/rst-ack-from-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47597-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Please advise on the below. I checked and RST-ACK is like FIN-ACK to close the connection. The problem is when this happens the webpage is not displayed.</p><p>Say the TCP session is between 10.1.1.1 and 10.1.1.2</p><p>10.1.1.1----&gt;syn 10.1.1.2</p><p>10.1.1.2----&gt;syn-ack 10.1.1.1</p><p>10.1.1.1----&gt;ack 10.1.1.2</p><p>------Omittied the data transfer-------</p><p>10.1.1.1 --&gt;RST,ACk 10.1.1.2</p><p>Question:</p><p>1)Without the (Fin-ACK) from 10.1.1.2, can 10.1.1.1 send (RST-ACK)?</p><p>2)If the above is yes, should 10.1.1.2 send (FIN-ACK) after (RST-ACK)? 3)Is the above Communication valid between the server and the client?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">rst+ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '15, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/6c685868d46cd97a6a734504d69f5373?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakeshreddy&#39;s gravatar image" /><p>rakeshreddy<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakeshreddy has no accepted answers">0%</span></p></div></div><div id="comments-container-47597" class="comments-container"></div><div id="comment-tools-47597" class="comment-tools"></div><div class="clear"></div><div id="comment-47597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47613"></span>

<div id="answer-container-47613" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47613-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>1) Yes, the server can actively terminate the connection any time it considers appropriate.<br />
</p><p>2) When the client gets the RST packet it makes no sense to send a FIN as the remote socket is no longer there to ACK it.</p><p>3) It causes the passive side to see a broken connection so it's not nice but valid and it's not uncommon to see a RST (abortive close) these days</p><p>From <a href="http://stackoverflow.com/questions/3757289/tcp-option-so-linger-zero-when-its-required">http://stackoverflow.com/questions/3757289/tcp-option-so-linger-zero-when-its-required</a></p><p><strong>When to use SO_LINGER with timeout 0</strong></p><p>... according to "UNIX Network Programming" third edition page 202-203, setting SO_LINGER with timeout 0 prior to calling close() will cause the normal termination sequence not to be initiated.</p><p>Instead, the peer setting this option and calling close() will send a RST (connection reset) which indicates an error condition and this is how it will be perceived at the other end. You will typically see errors like "Connection reset by peer".</p><p>Therefore, in the normal situation it is a really bad idea to set SO_LINGER with timeout 0 prior to calling close() – from now on called abortive close – in a server application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '15, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-47613" class="comments-container"><span id="47614"></span><div id="comment-47614" class="comment"><div id="post-47614-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Make sense.</p></div><div id="comment-47614-info" class="comment-info"><span class="comment-age">(14 Nov '15, 23:36)</span> rakeshreddy</div></div></div><div id="comment-tools-47613" class="comment-tools"></div><div class="clear"></div><div id="comment-47613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

