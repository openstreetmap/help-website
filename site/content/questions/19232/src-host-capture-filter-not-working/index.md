+++
type = "question"
title = "src host capture filter not working!"
description = '''Hi.I need to see packets coming from OR going to ip xxx.xxx.xxx.xxx using capture filter but src host capture filter not working for me! I write src host 192.168.1.100 (My IP) and I capture traffic to or from my IP address but I want to capture only traffic from this IP.Also, is there any way to see...'''
date = "2013-03-06T09:49:00Z"
lastmod = "2013-03-06T09:56:00Z"
weight = 19232
keywords = [ "capture", "capture-filter", "src" ]
aliases = [ "/questions/19232" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [src host capture filter not working!](/questions/19232/src-host-capture-filter-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19232-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.I need to see packets coming from OR going to ip xxx.xxx.xxx.xxx using capture filter but src host capture filter not working for me! I write src host 192.168.1.100 (My IP) and I capture traffic to or from my IP address but I want to capture only traffic from this IP.Also, is there any way to see the capture process, the number of captured packets, etc as in Tshark (linux terminal):</p><p>[]# tshark -i eth1 dst host 207.35.208.194 or src host 207.35.208.194</p><p>Capturing on eth1</p><p>0.000000 208.77.1.33 -&gt; 207.35.208.194 SIP Status: 200 OK (1 bindings)</p><p>7.475218 208.77.1.33 -&gt; 207.35.208.194 SIP Status: 200 OK (1 bindings)</p><p>6 packets captured</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">capture capture-filter src</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '13, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/a334020eacdd8a7faf0f3e9d0d1cf678?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zig69&#39;s gravatar image" /><p>zig69<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zig69 has no accepted answers">0%</span></p></div></div><div id="comments-container-19232" class="comments-container"></div><div id="comment-tools-19232" class="comment-tools"></div><div class="clear"></div><div id="comment-19232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19236"></span>

<div id="answer-container-19236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19236-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To limit captures for packets to or from a host use the capture filter <code>host a.b.c.d</code>.</p><p>I don't understand the second part of the question, are you talking about the Wireshark GUI?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19236" class="comments-container"><span id="19237"></span><div id="comment-19237" class="comment"><div id="post-19237-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks but I need to capture only traffic <strong>from</strong> my IP, and yes, I am talking about WS GUI (I see all traffic to and from my host in GUI using src host a.b.c.d and I need to see only traffic exiting from my host... Thanks again!</p></div><div id="comment-19237-info" class="comment-info"><span class="comment-age">(06 Mar '13, 10:05)</span> zig69</div></div><span id="19238"></span><div id="comment-19238" class="comment"><div id="post-19238-score" class="comment-score">1</div><div class="comment-text"><p>instead of <strong>src host x.x.x.xx</strong> please use <strong>src x.x.x.x</strong></p></div><div id="comment-19238-info" class="comment-info"><span class="comment-age">(06 Mar '13, 10:17)</span> Kurt Knochner ♦</div></div><span id="19244"></span><div id="comment-19244" class="comment"><div id="post-19244-score" class="comment-score"></div><div class="comment-text"><p>Both forms are working properly for me on PortableApps version 1.8.5.</p></div><div id="comment-19244-info" class="comment-info"><span class="comment-age">(06 Mar '13, 12:24)</span> Jim Aragon</div></div></div><div id="comment-tools-19236" class="comment-tools"></div><div class="clear"></div><div id="comment-19236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

