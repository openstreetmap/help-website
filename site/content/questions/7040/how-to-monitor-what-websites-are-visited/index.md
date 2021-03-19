+++
type = "question"
title = "How to monitor what websites are visited"
description = '''Hi, I have a Laptop with wireless connection (windows), Im trying to simply monitor what websites the 2 other users (my kids) are accessing. One of the computers is connected via Ethernet Cable (windows), and the other is connected wireless (and is a Mac) How do i get to the point where i see a list...'''
date = "2011-10-22T06:40:00Z"
lastmod = "2012-01-19T09:23:00Z"
weight = 7040
keywords = [ "wireless", "monitoring", "websites" ]
aliases = [ "/questions/7040" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to monitor what websites are visited](/questions/7040/how-to-monitor-what-websites-are-visited)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7040-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a Laptop with wireless connection (windows), Im trying to simply monitor what websites the 2 other users (my kids) are accessing. One of the computers is connected via Ethernet Cable (windows), and the other is connected wireless (and is a Mac)</p><p>How do i get to the point where i see a list of websites (ex. http://www.google.com/) the users are accessing?</p><p>(sorry for my bad english)</p><p>it would really help to get some professionel guidance Im looking forward to getting help soon..</p><p>--HamDer...</p></div><div id="question-tags" class="tags-container tags">wireless monitoring websites</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '11, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/24f850b088ea9782d9876835ee737105?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HamDer&#39;s gravatar image" /><p>HamDer<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HamDer has no accepted answers">0%</span></p></div></div><div id="comments-container-7040" class="comments-container"></div><div id="comment-tools-7040" class="comment-tools"></div><div class="clear"></div><div id="comment-7040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8398"></span>

<div id="answer-container-8398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8398-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>connect a 100m hub, not switch, between the wireless router and your internet modem connection. (This way you're using the hub to broadcast all the inbound and outbound traffic to your computer. A switch won't work for this purpose unless your switch is sophisticated enough to do port spanning or port mirroring). Plug your laptop into the hub. Now you can see all the traffic between your network and the internet. Run a capture. Go to Statistics | HTTP | Load Distribution and type http.host. Now look at the "HTTP Requests by HTTP Hosts". This will show you all the HTTP type traffic coming in and out of your network.<br />
Looking at traffic the way you're hooked up now you will only see your own traffic and Local LAN netbios broadcasts from the other computers on your network.<br />
John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '12, 20:53</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-8398" class="comments-container"></div><div id="comment-tools-8398" class="comment-tools"></div><div class="clear"></div><div id="comment-8398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8478"></span>

<div id="answer-container-8478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8478-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Creating account on opendns.com and the whole http traffic is monitored. great for families with little children. within the opendns center you are able to configure with a few clicks restrictions (porn,p2p etc).</p><p>have fun</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '12, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/0827cad2801866423f44909176837d00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="macschussel&#39;s gravatar image" /><p>macschussel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="macschussel has no accepted answers">0%</span></p></div></div><div id="comments-container-8478" class="comments-container"></div><div id="comment-tools-8478" class="comment-tools"></div><div class="clear"></div><div id="comment-8478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

