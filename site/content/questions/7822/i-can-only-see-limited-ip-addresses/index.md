+++
type = "question"
title = "I can only see limited IP addresses"
description = '''Ok, I am new to Wireshark so I am still learning... The problem I am having is: I start Wireshark and a gazillion lines appear - but it is only a few of the IP addresses on the network (maybe 10 IPs out of 1300!). I have tried changing the filter to TCP &amp;amp; HTTP and I still only see a few IPs, wha...'''
date = "2011-12-07T07:32:00Z"
lastmod = "2011-12-07T11:30:00Z"
weight = 7822
keywords = [ "ip" ]
aliases = [ "/questions/7822" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I can only see limited IP addresses](/questions/7822/i-can-only-see-limited-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7822-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, I am new to Wireshark so I am still learning...</p><p>The problem I am having is:</p><p>I start Wireshark and a gazillion lines appear - but it is only a few of the IP addresses on the network (maybe 10 IPs out of 1300!). I have tried changing the filter to TCP &amp; HTTP and I still only see a few IPs, what am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '11, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/fd1b86ea492fcf3e1301d82f88d13102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clivethrust&#39;s gravatar image" /><p>clivethrust<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clivethrust has no accepted answers">0%</span></p></div></div><div id="comments-container-7822" class="comments-container"></div><div id="comment-tools-7822" class="comment-tools"></div><div class="clear"></div><div id="comment-7822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7825"></span>

<div id="answer-container-7825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7825-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you really have that many IP addresses to monitor, I'm going to assume that your network is mostly switched. You should check <em>where</em> in the network you are capturing from. It sounds like you have a small portion of the network on a hub or otherwise broadcast to a small group. You probably have something like this:</p><pre><code>YOU ------+HUB+-----+SWITCH+----{The rest of the network}
           +++
           |||
COMPUTER---+|+---COMPUTER
COMPUTER----+</code></pre><p>With this setup, you'll capture traffic for a small number of machines in the larger network. You should review your network topology to see if there would be a better place to capture traffic than where you are now. Check the <a href="http://wiki.wireshark.org/CaptureSetup" title="Capture Setup">Capture Setup</a> article for some more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7825" class="comments-container"><span id="7828"></span><div id="comment-7828" class="comment"><div id="post-7828-score" class="comment-score"></div><div class="comment-text"><p>I have connected the PC direct to the main switch and all traffic flows through this!</p><p>PC ---- switch ----- ALL IPs (only some visible)</p><p>This is a rural internet service from the PC I am able to connect to all the Motorola canopy equipment and I can trace (ping etc..) all customers static IP.</p><p>Fiber --- switch --- Backhaul --- Backhaul --- switch --- star BH | | PC</p></div><div id="comment-7828-info" class="comment-info"><span class="comment-age">(07 Dec '11, 10:41)</span> clivethrust</div></div><span id="7835"></span><div id="comment-7835" class="comment"><div id="post-7835-score" class="comment-score"></div><div class="comment-text"><p>In that case, I suggest you check to see if your main switch will support spanning or mirroring to that port. I would heartily recommend <em>against</em> using Wireshark directly to monitor the volume of traffic that is certainly going over that switch. Check <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet" title="Switched Ethernet">the Switched Ethernet</a> section as Guy suggests.</p><p>Can I ask why you need to monitor all of this traffic? I suspect you could diagnose problematic network behavior more easily somewhere else in the topology.</p></div><div id="comment-7835-info" class="comment-info"><span class="comment-age">(07 Dec '11, 11:57)</span> multipleinte...</div></div></div><div id="comment-tools-7825" class="comment-tools"></div><div class="clear"></div><div id="comment-7825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7834"></span>

<div id="answer-container-7834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7834-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the machine running Wireshark is plugged into a switch, there is no guarantee whatsoever that it will see all the traffic flowing through the switch; see <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">the "Switched Ethernet" section of the "CaptureSetup/Ethernet" page of the Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7834" class="comments-container"></div><div id="comment-tools-7834" class="comment-tools"></div><div class="clear"></div><div id="comment-7834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

