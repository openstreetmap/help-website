+++
type = "question"
title = "Monitoring a single IP"
description = '''I have Wireshark loaded on a Windows 8 OS and I want to monitor another IP from a computer on my network. I read a couple responses to others with the same question but none of the answers are working for me. I went to Capture Filter and used &quot;host xxx.xxx.xxx.xxxx.&quot; This does not capture anything f...'''
date = "2015-07-03T17:23:00Z"
lastmod = "2015-07-03T20:27:00Z"
weight = 43854
keywords = [ "single-ip" ]
aliases = [ "/questions/43854" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring a single IP](/questions/43854/monitoring-a-single-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark loaded on a Windows 8 OS and I want to monitor another IP from a computer on my network. I read a couple responses to others with the same question but none of the answers are working for me.</p><p>I went to Capture Filter and used "host xxx.xxx.xxx.xxxx." This does not capture anything from the machine I am trying to monitor. However, this will capture packets that I send to the machine I want to monitor from the machine that I have Wireshark loaded on. For example, ICMP traffic will show up on Wireshark if I ping the monitored machine from the Windows 8 machine with Wireshark.</p><p>Am I doing something wrong here or is that Wireshark isn't meant to work like this?</p></div><div id="question-tags" class="tags-container tags">single-ip</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '15, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/36a3abbb6d9d95f9a268abb04b6cd9b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexwallace23&#39;s gravatar image" /><p>alexwallace23<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexwallace23 has no accepted answers">0%</span></p></div></div><div id="comments-container-43854" class="comments-container"></div><div id="comment-tools-43854" class="comment-tools"></div><div class="clear"></div><div id="comment-43854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43859"></span>

<div id="answer-container-43859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43859-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is likely down to oyu using a switched Ethernet network. Each machine will be plugged into a switch port and thus Wireshark will only capture traffic directed to or from the capture machine. To capture traffic from another machine that is directed elsewhere than the capture machine you'll need to either "tap" into the Ethernet connection of the other machine, or if your switch hardware allows it, "span" or "monitor" the port of the target machine to the port of the capture machine.</p><p>See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a>, in particular the section on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">Switched Ethernet</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '15, 20:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '15, 20:27</p></div></div><div id="comments-container-43859" class="comments-container"></div><div id="comment-tools-43859" class="comment-tools"></div><div class="clear"></div><div id="comment-43859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

