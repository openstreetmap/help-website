+++
type = "question"
title = "Log packets @ my router"
description = '''Hi,  We currently are having an issue with our router randomly dropping (internally). Our ISP replaced the router, but it&#x27;s still happening. She mentioned it could be a bad packet, etc. Is there a way to monitor a specific IP (the router - LAN side) so I can try and narrow what&#x27;s causing it to drop?...'''
date = "2011-09-28T10:09:00Z"
lastmod = "2011-09-29T01:47:00Z"
weight = 6625
keywords = [ "router", "wlan", "troubleshooting", "capture" ]
aliases = [ "/questions/6625" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Log packets @ my router](/questions/6625/log-packets-my-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6625-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We currently are having an issue with our router randomly dropping (internally). Our ISP replaced the router, but it's still happening. She mentioned it could be a bad packet, etc. Is there a way to monitor a specific IP (the router - LAN side) so I can try and narrow what's causing it to drop?</p><p>Thanks brian</p></div><div id="question-tags" class="tags-container tags">router wlan troubleshooting capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '11, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/0b88b74db642ecee69896f823fddd8ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slothy&#39;s gravatar image" /><p>slothy<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slothy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Sep '11, 00:04</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6625" class="comments-container"></div><div id="comment-tools-6625" class="comment-tools"></div><div class="clear"></div><div id="comment-6625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6634"></span>

<div id="answer-container-6634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6634-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Monitoring a specific IP from the outside can be done by setting a display filter to that IP address. An inside IP address can only be monitored if your router is capable of mirroring the date from other users to a specific port, which in most cases on home routers is not possible.</p><p>Anyways: You'll have to check if you see packet loss on the inside interfaces of your router. Try going for tcp.analysis.flags which will give you some idea what is happening inside your TCP connections and search for "previous segment lost" and "(Fast) Retransmission". Although Wireshark cannot tell 100% for sure, that there have been retransmissions, it might give you some hints on what to look for</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '11, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Sep '11, 01:49</p></div></div><div id="comments-container-6634" class="comments-container"></div><div id="comment-tools-6634" class="comment-tools"></div><div class="clear"></div><div id="comment-6634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

