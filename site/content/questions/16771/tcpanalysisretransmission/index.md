+++
type = "question"
title = "tcp.analysis.retransmission"
description = '''Hi, Can anyone tell me that How is the tcp.analysis.retransmission works? Is it analysis only on time interval or other thing?'''
date = "2012-12-11T10:18:00Z"
lastmod = "2012-12-11T10:41:00Z"
weight = 16771
keywords = [ "retransmission" ]
aliases = [ "/questions/16771" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tcp.analysis.retransmission](/questions/16771/tcpanalysisretransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16771-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Can anyone tell me that How is the tcp.analysis.retransmission works? Is it analysis only on time interval or other thing?</p></div><div id="question-tags" class="tags-container tags">retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '12, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/d3610777cf99431bf56fb2f784e6c791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saruul&#39;s gravatar image" /><p>Saruul<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saruul has no accepted answers">0%</span></p></div></div><div id="comments-container-16771" class="comments-container"></div><div id="comment-tools-16771" class="comment-tools"></div><div class="clear"></div><div id="comment-16771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16773"></span>

<div id="answer-container-16773" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16773-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is triggered when a packet containing a sequence is seen that should have arrived earlier, which means that there must have been a gap in the packet sequence that the "retransmission" packet closes or partially closes. If I remember correctly it also needs to arrive more than 3ms after the gap starts, otherwise it is marked as out of order, but I may be mistaken.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16773" class="comments-container"><span id="16782"></span><div id="comment-16782" class="comment"><div id="post-16782-score" class="comment-score"></div><div class="comment-text"><p>Heh - you just answered a question we were discussing in a live trouleshooting/diagnostic discussion - many thanks!</p></div><div id="comment-16782-info" class="comment-info"><span class="comment-age">(11 Dec '12, 13:34)</span> wesmorgan1</div></div><span id="16845"></span><div id="comment-16845" class="comment"><div id="post-16845-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jasper :) I think wireshark is the best packet analyzer for TCP packets.</p></div><div id="comment-16845-info" class="comment-info"><span class="comment-age">(13 Dec '12, 10:59)</span> Saruul</div></div><span id="24066"></span><div id="comment-24066" class="comment"><div id="post-24066-score" class="comment-score"></div><div class="comment-text"><p>This post is helpful :). I was just checking a network trace with duplex mismatch. I was trying to calculate how much data did I unnecessarily transfer. I was uploading 3MB big file. When I checked amount of transferred data using filter "data", there was 4,2MB transferred (about 30% more). But when I was checking retransferred data using tcp.analysis.retransmission, there was just about 6% more. And then I finally tried filter "tcp.analysis.retransmission || tcp.analysis.out_of_order" and got the desired amount 30% of data more. There really were several packets visible twice where one of them was segment out of order.</p></div><div id="comment-24066-info" class="comment-info"><span class="comment-age">(26 Aug '13, 08:45)</span> garw</div></div></div><div id="comment-tools-16773" class="comment-tools"></div><div class="clear"></div><div id="comment-16773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

