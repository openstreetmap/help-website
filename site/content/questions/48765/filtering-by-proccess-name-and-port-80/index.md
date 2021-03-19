+++
type = "question"
title = "Filtering by proccess name and port 80"
description = '''Hi, I would like to capture one of my pc in my LAN to watch the traffic to port 80 and process name. In other words, I would like to know which process (IE,Mozilla,Chrome, etc.) is trying to communicate with the internet. I am getting an alerts from our SIEM that my PC is trying to communicate with ...'''
date = "2015-12-31T01:55:00Z"
lastmod = "2015-12-31T07:11:00Z"
weight = 48765
keywords = [ "capture" ]
aliases = [ "/questions/48765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering by proccess name and port 80](/questions/48765/filtering-by-proccess-name-and-port-80)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48765-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to capture one of my pc in my LAN to watch the traffic to port 80 and process name. In other words, I would like to know which process (IE,Mozilla,Chrome, etc.) is trying to communicate with the internet. I am getting an alerts from our SIEM that my PC is trying to communicate with over 100 different IP addresses at the same time (in less than 5 min !!! ). Obviously this is not a standard behavior of an regular Pc in a standard LAN. So I would like to capture the process/malware/virus/botnet which trying to communicate with these 100 IP addresses. How can I manage this? What filter should I type? I have tried : tcp.port==80 but I need to add to this filter the process name field as well so I will be able to view the process that trying to communicate... What is the correct syntax that I should type in the filter?? Please help Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '15, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/6ab830c3f242095c961ff21df34aedba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syntax1127&#39;s gravatar image" /><p>syntax1127<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syntax1127 has no accepted answers">0%</span></p></div></div><div id="comments-container-48765" class="comments-container"></div><div id="comment-tools-48765" class="comment-tools"></div><div class="clear"></div><div id="comment-48765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48768"></span>

<div id="answer-container-48768" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48768-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No way to do that using Wireshark as Wireshark has no information about which process is bound to a particular source port.</p><p>You can use Wireshark to have a look at the payload of that traffic itself, but if it is encrypted or simply incomprehensible, it won't help you much.</p><p>If it is a virus, you'll most likely see just several instances of svchost.exe in the tasklist, which is a process used by many "legal" applications but often also by viruses. I'd recommend some "bootable anti-virus" software - you boot from a CD or a USB flash and scan your disk before any virus can run and thus hide itself from being spotted by normal anti-virus software.</p><p>But it can also be some communication software like Skype - instances of applications of this type often talk to each other using tcp ports 80 or 443 because these are often the only ones open at firewalls.</p><p>Also, if you have many windows open in your web browser, each of them may fetch advertisement from another site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '15, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48768" class="comments-container"></div><div id="comment-tools-48768" class="comment-tools"></div><div class="clear"></div><div id="comment-48768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

