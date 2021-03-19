+++
type = "question"
title = "Start and end of slow-start phase"
description = '''I have a good understanding of slow-start phase, namely how it only lets a few packets send at first, however this amount increments until the max is found in order to avoid congestion. For the graph below however, how do I identify when the slow-start phase ends? I&#x27;m assuming it starts right in the...'''
date = "2013-02-04T09:56:00Z"
lastmod = "2013-02-07T17:28:00Z"
weight = 18287
keywords = [ "stevens", "graph", "slow", "tcp", "start" ]
aliases = [ "/questions/18287" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Start and end of slow-start phase](/questions/18287/start-and-end-of-slow-start-phase)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18287-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a good understanding of slow-start phase, namely how it only lets a few packets send at first, however this amount increments until the max is found in order to avoid congestion.</p><p>For the graph below however, how do I identify when the slow-start phase ends? I'm assuming it starts right in the begining at 0 seconds, which is when the connection would be established. I'm going to guess that the slow-start ends at 0.65 seconds? Which is when we only start seeing two dots (packets) on after another... Or rather would this just be because of congestion avoidance?</p><p><img src="http://i47.tinypic.com/5o2g9.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">stevens graph slow tcp start</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/5e2fa3f0291deba923a121e3cbde0d3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rikesh%20Padhiar&#39;s gravatar image" /><p>Rikesh Padhiar<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rikesh Padhiar has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '13, 09:57</p></div></div><div id="comments-container-18287" class="comments-container"></div><div id="comment-tools-18287" class="comment-tools"></div><div class="clear"></div><div id="comment-18287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18434"></span>

<div id="answer-container-18434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18434-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>May I direct you to the following article?</p><blockquote><p><code>http://packetlife.net/blog/2011/jul/5/tcp-slow-start/</code><br />
</p></blockquote><p>It explains what you see in the TCP stream graph in a nice way.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '13, 17:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18434" class="comments-container"></div><div id="comment-tools-18434" class="comment-tools"></div><div class="clear"></div><div id="comment-18434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

