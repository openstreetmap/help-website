+++
type = "question"
title = "How to Make the monitor computer shutup?"
description = '''I have had to disable my modems firewall, to get VOIP working. I&#x27;d like to check what traffic is hitting my router and what its doing with it. I have put a hub between the modem and the router, this is out in Public IP world, not even DMZ. I have stolen a public IP for my monitors network card (stat...'''
date = "2013-04-14T19:29:00Z"
lastmod = "2013-04-14T20:53:00Z"
weight = 20399
keywords = [ "windows", "noise", "beginner" ]
aliases = [ "/questions/20399" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Make the monitor computer shutup?](/questions/20399/how-to-make-the-monitor-computer-shutup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20399-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have had to disable my modems firewall, to get VOIP working. I'd like to check what traffic is hitting my router and what its doing with it. I have put a hub between the modem and the router, this is out in Public IP world, not even DMZ. I have stolen a public IP for my monitors network card (static, no gateway).</p><p>I've done a few captures OK, and noticed that WireShark set the network card to IP 0.0.0.0 while it was capturing. The only noise from my network card was a couple of arps announcing itself, absolutely no IP. (I thought this was a feature of promiscuous mode)</p><p>The last couple of tries however the IP was left unchanged and windows took off with reams of trash, straight onto the net (and using someone else's IP). How do I stop windows using the interface while I'm capturing?</p></div><div id="question-tags" class="tags-container tags">windows noise beginner</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '13, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/a0095c6dd1fc2ee09b5aaf17a1282f96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattrix&#39;s gravatar image" /><p>mattrix<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattrix has no accepted answers">0%</span></p></div></div><div id="comments-container-20399" class="comments-container"></div><div id="comment-tools-20399" class="comment-tools"></div><div class="clear"></div><div id="comment-20399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20401"></span>

<div id="answer-container-20401" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20401-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I'm stupid. Because it worked at first, I didn't think to change anything.</p><p>Solution is to disable TCP/IP altogether.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '13, 20:53</strong></p><img src="https://secure.gravatar.com/avatar/a0095c6dd1fc2ee09b5aaf17a1282f96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattrix&#39;s gravatar image" /><p>mattrix<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattrix has no accepted answers">0%</span></p></div></div><div id="comments-container-20401" class="comments-container"></div><div id="comment-tools-20401" class="comment-tools"></div><div class="clear"></div><div id="comment-20401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

