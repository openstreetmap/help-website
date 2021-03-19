+++
type = "question"
title = "what is the state of TCP  when it re-transmit packets after sending FIN"
description = ''' From THE NO.282 packet, we see that the TCP has sent a FIN, so the TCP is in FIN_WAIT_1 state. Since it receives multiple ACK to inform it to retrasmit, it begins to retransmit. So what is the state of TCP? '''
date = "2015-10-28T10:23:00Z"
lastmod = "2015-10-28T10:48:00Z"
weight = 47024
keywords = [ "tcp" ]
aliases = [ "/questions/47024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is the state of TCP when it re-transmit packets after sending FIN](/questions/47024/what-is-the-state-of-tcp-when-it-re-transmit-packets-after-sending-fin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/retr.png" alt="alt text" /></p><p>From THE NO.282 packet, we see that the TCP has sent a FIN, so the TCP is in FIN_WAIT_1 state. Since it receives multiple ACK to inform it to retrasmit, it begins to retransmit. So what is the state of TCP?</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/2203cfcd179ad33d34d4f6f0cdedb4da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kitty&#39;s gravatar image" /><p>kitty<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kitty has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47024" class="comments-container"></div><div id="comment-tools-47024" class="comment-tools"></div><div class="clear"></div><div id="comment-47024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47026"></span>

<div id="answer-container-47026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47026-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>10.0.0.1is in FIN_WAIT_1<br />
10.0.0.10 is in ESTABLISHED until it ACKs the FIN</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div></div><div id="comments-container-47026" class="comments-container"><span id="47027"></span><div id="comment-47027" class="comment"><div id="post-47027-score" class="comment-score"></div><div class="comment-text"><p>@Christian_R the NO.535 packet is a data packet from 10.0.0.1. If 10.0.0.1 is in FIN_WAIT_1, it can still send packets?</p></div><div id="comment-47027-info" class="comment-info"><span class="comment-age">(28 Oct '15, 10:52)</span> kitty</div></div><span id="47029"></span><div id="comment-47029" class="comment"><div id="post-47029-score" class="comment-score"></div><div class="comment-text"><p>Yes it still can serve TCP retrans requests of the other side.</p></div><div id="comment-47029-info" class="comment-info"><span class="comment-age">(28 Oct '15, 10:57)</span> Christian_R</div></div><span id="47030"></span><div id="comment-47030" class="comment"><div id="post-47030-score" class="comment-score"></div><div class="comment-text"><p>That is one reason why RST is used more often today.</p></div><div id="comment-47030-info" class="comment-info"><span class="comment-age">(28 Oct '15, 10:58)</span> Christian_R</div></div></div><div id="comment-tools-47026" class="comment-tools"></div><div class="clear"></div><div id="comment-47026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

