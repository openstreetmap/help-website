+++
type = "question"
title = "[PSH, ACK] long Delay"
description = '''Hi, we running a system with one server and 4 clients. All 4 clients send their data at the same time to a server. Sometimes we have big delay, which is a big problem for our system. To figure out whats happens, we run IPERF on all 4 clients(Linux). The server is an windows system. If all 4 clients ...'''
date = "2016-12-13T14:42:00Z"
lastmod = "2016-12-13T23:46:00Z"
weight = 58055
keywords = [ "ack", "delay", "windows7", "psh", "linux" ]
aliases = [ "/questions/58055" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[PSH, ACK\] long Delay](/questions/58055/psh-ack-long-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58055-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, we running a system with one server and 4 clients. All 4 clients send their data at the same time to a server. Sometimes we have big delay, which is a big problem for our system. To figure out whats happens, we run IPERF on all 4 clients(Linux). The server is an windows system. If all 4 clients sending datas at the same time to the server, we got a very long delay, up to &gt;10sec. But only client has this delay. We can't explan whats going on. On wireshark we can see, that the client sends an PSH ACK an after that we have delays. What could be a reason for that and how can we fix this?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/log_YSsjsMV.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ack delay windows7 psh linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '16, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/03902a31bb2d48dc92b7fe2108a3f2ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Toxic&#39;s gravatar image" /><p>Toxic<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Toxic has no accepted answers">0%</span></p></img></div></div><div id="comments-container-58055" class="comments-container"></div><div id="comment-tools-58055" class="comment-tools"></div><div class="clear"></div><div id="comment-58055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58066"></span>

<div id="answer-container-58066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58066-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In this case you should disable Delayed ACK at the windows system 192.168.1.2.</p><p>Here I found a small howto:</p><p><a href="https://m.youtube.com/watch?v=mJccXn8rSIw">https://m.youtube.com/watch?v=mJccXn8rSIw</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '16, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-58066" class="comments-container"></div><div id="comment-tools-58066" class="comment-tools"></div><div class="clear"></div><div id="comment-58066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

