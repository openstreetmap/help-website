+++
type = "question"
title = "RTP call flow discrimination"
description = '''Hi all, What about two RTP flows (two calls: another call just a few seconds after the first call with the same caller-callee) with the same IPs and ports (is it possible ???): first call (at time t): caller: IP:192.168.100.6 port:3000 &amp;lt;-&amp;gt; callee: IP:192.168.100.7 port 12687 second call (at t+...'''
date = "2013-05-31T05:58:00Z"
lastmod = "2013-05-31T20:12:00Z"
weight = 21652
keywords = [ "flow", "call", "rtp", "discrimination" ]
aliases = [ "/questions/21652" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP call flow discrimination](/questions/21652/rtp-call-flow-discrimination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21652-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>What about two RTP flows (two calls: another call just a few seconds after the first call with the same caller-callee) with the same IPs and ports (is it possible ???):</p><p>first call (at time t): caller: IP:192.168.100.6 port:3000 &lt;-&gt; callee: IP:192.168.100.7 port 12687</p><p>second call (at t+10 second, for example): caller: IP:192.168.100.6 port:3000 &lt;-&gt; callee: IP:192.168.100.7 port 12687</p><p>In this case, how to descriminate both flows ... ???</p><p>thanks for your help</p></div><div id="question-tags" class="tags-container tags">flow call rtp discrimination</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '13, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/31856543dad1a12f24073c17126cb1e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikuzar&#39;s gravatar image" /><p>ikuzar<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikuzar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 31 May '13, 07:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21652" class="comments-container"></div><div id="comment-tools-21652" class="comment-tools"></div><div class="clear"></div><div id="comment-21652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21685"></span>

<div id="answer-container-21685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21685-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From RFC 3550 section 5.2: "In RTP, multiplexing is provided by the destination transport address (network address and port number) which is different for each RTP session." So no, they must be unique for each individual session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 20:12</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21685" class="comments-container"></div><div id="comment-tools-21685" class="comment-tools"></div><div class="clear"></div><div id="comment-21685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

