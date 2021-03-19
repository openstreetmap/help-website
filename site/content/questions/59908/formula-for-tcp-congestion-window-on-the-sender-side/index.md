+++
type = "question"
title = "Formula for TCP Congestion window on the sender side"
description = '''I wanted to do a TCP congestion window analysis. As shown in the 7th column of the csv file found in this link- we can see the congestion window increases and sometimes decreases. But I don&#x27;t seem to understand the pattern when it decreases, why it increases by a certain number (for example: from 25...'''
date = "2017-03-08T01:44:00Z"
lastmod = "2017-03-08T12:40:00Z"
weight = 59908
keywords = [ "congestion-control", "tcp", "congestion" ]
aliases = [ "/questions/59908" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Formula for TCP Congestion window on the sender side](/questions/59908/formula-for-tcp-congestion-window-on-the-sender-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59908-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to do a TCP congestion window analysis. As shown in the 7th column of the csv file found in this link- we can see the congestion window increases and sometimes decreases. But I don't seem to understand the pattern when it decreases, why it increases by a certain number (for example: from 25 to 29). Is it because of the sequence number or?</p><p>Is there any formula that calculates this?</p></div><div id="question-tags" class="tags-container tags">congestion-control tcp congestion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '17, 11:33</p></div></div><div id="comments-container-59908" class="comments-container"></div><div id="comment-tools-59908" class="comment-tools"></div><div class="clear"></div><div id="comment-59908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59931"></span>

<div id="answer-container-59931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59931-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Nice File. How did you create it? Normally the CWND and SSTHRESH are hidden.</p><p>So if the sender sends a packet the cwnd is reduced by the amount of the bytes of the segments. If he receives an ACK for that segment the CWND is increased by the ACKed data. The exactly size and behaviour of the cwnd depends also on the congestion algorithm which is actually used.</p><p><a href="http://packetlife.net/blog/2011/jul/5/tcp-slow-start/">http://packetlife.net/blog/2011/jul/5/tcp-slow-start/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '17, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '17, 01:16</p></div></div><div id="comments-container-59931" class="comments-container"></div><div id="comment-tools-59931" class="comment-tools"></div><div class="clear"></div><div id="comment-59931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

