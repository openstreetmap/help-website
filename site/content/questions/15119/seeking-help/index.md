+++
type = "question"
title = "Seeking help"
description = '''Hi, I am new to wireshark. If someone help me to solve out my network issue, its highly appreciated. I have a network printer. It has static IP Address. Whenever some computers logged into the network, the printer get restarted and loses the connectivity. After reboots, stay connected some more time...'''
date = "2012-10-20T23:29:00Z"
lastmod = "2012-10-21T04:32:00Z"
weight = 15119
keywords = [ "printer", "protocol", "port" ]
aliases = [ "/questions/15119" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Seeking help](/questions/15119/seeking-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15119-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new to wireshark. If someone help me to solve out my network issue, its highly appreciated. I have a network printer. It has static IP Address. Whenever some computers logged into the network, the printer get restarted and loses the connectivity. After reboots, stay connected some more time and again rebooted. It happens through out the day until those 'unknown users' get off.</p><p>I have installed wireshark in the network, hoping it could help me to findout who is accessing the printer just before it goes reboot. Please help how to configure ws for this purpose. It is my first time use wireshark and ofcourse i am reading the manual :)</p><p>Your expert advise is welcome</p></div><div id="question-tags" class="tags-container tags">printer protocol port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '12, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/b401e840d22a5e922240a75d01d45c26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bashful&#39;s gravatar image" /><p>bashful<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bashful has no accepted answers">0%</span></p></div></div><div id="comments-container-15119" class="comments-container"><span id="15230"></span><div id="comment-15230" class="comment"><div id="post-15230-score" class="comment-score">1</div><div class="comment-text"><p>Are you sure that the static address you have assigned to the printer is outside the DHCP pool range? If a computer using DHCP connects to the network and obtains a lease to the IP address already assigned to the printer, it will cause the printer to get an error when it tries to access the network.</p></div><div id="comment-15230-info" class="comment-info"><span class="comment-age">(24 Oct '12, 13:39)</span> inetdog</div></div></div><div id="comment-tools-15119" class="comment-tools"></div><div class="clear"></div><div id="comment-15119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15123"></span>

<div id="answer-container-15123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15123-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>first thing you need to do is intercept the packets at your printer. you can even get by by putting a 10/100 hub there. The other option is to span/mirror the traffic to and from the printer port to your wireshark port.</p><p>i have quite a bit of stuff on my website for you to reference <a href="http://www.thetechfirm.com">www.thetechfirm.com</a></p><p>let me know when you have things setup and I'll walk you through the next part.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '12, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p>thetechfirm<br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-15123" class="comments-container"><span id="15126"></span><div id="comment-15126" class="comment"><div id="post-15126-score" class="comment-score"></div><div class="comment-text"><p>Hi Thanks for your reply. I am afraid i could fully understood the setup you mentioned above. My PC is on the same network where the printer is installed. The printer is reachable from my PC. why should i do need another hub in picture?</p><p>I have installed the Wireshark already in my PC.</p><p>Thanks and looking forward to your reply.</p></div><div id="comment-15126-info" class="comment-info"><span class="comment-age">(21 Oct '12, 06:12)</span> bashful</div></div><span id="15127"></span><div id="comment-15127" class="comment"><div id="post-15127-score" class="comment-score"></div><div class="comment-text"><p>I assumed the printer is connected to a switch.<br />
If so, you need to be able to capture all the traffic and to and from the printer.</p></div><div id="comment-15127-info" class="comment-info"><span class="comment-age">(21 Oct '12, 06:36)</span> thetechfirm</div></div><span id="15128"></span><div id="comment-15128" class="comment"><div id="post-15128-score" class="comment-score"></div><div class="comment-text"><p>Ofcourse, printer is connected to the switch. I need your help how to capture, what filter to use and how to read the result.</p><p>Thanks for your help</p></div><div id="comment-15128-info" class="comment-info"><span class="comment-age">(21 Oct '12, 07:07)</span> bashful</div></div><span id="15131"></span><div id="comment-15131" class="comment"><div id="post-15131-score" class="comment-score"></div><div class="comment-text"><p>before ypu can filter anything, how are you capturing the packets to and from the printer? for example, can you capture packets of anyone printing or pinging the printer?</p><p>if not, you need to either mirror the printer port - if you switch is manageable, or place a hub between the printer and switch so you can see the traffic.</p></div><div id="comment-15131-info" class="comment-info"><span class="comment-age">(21 Oct '12, 08:59)</span> thetechfirm</div></div><span id="15133"></span><div id="comment-15133" class="comment"><div id="post-15133-score" class="comment-score"></div><div class="comment-text"><p>I converted your conversations to comments since it's part of the original answer. Please keep using comments unless you really have a new answer to the original question :-)</p></div><div id="comment-15133-info" class="comment-info"><span class="comment-age">(21 Oct '12, 09:12)</span> Jasper ♦♦</div></div><span id="15140"></span><div id="comment-15140" class="comment not_top_scorer"><div id="post-15140-score" class="comment-score"></div><div class="comment-text"><p>Sorry, i didnt know that, I just typed in the 'your answer' box so far :)</p><blockquote><blockquote><p>can you capture packets of anyone printing or pinging the printer? This is what i want to do and need your help. I am connected to same switch where printer and other clients also connected. Its a cisco 2960 switch.</p></blockquote></blockquote><p>I want to capture any traffic going to and fro printer (or the LPD and RAW protocols)and identify from which client it is generated.</p><p>Thanks for the help</p></div><div id="comment-15140-info" class="comment-info"><span class="comment-age">(21 Oct '12, 20:44)</span> bashful</div></div><span id="15164"></span><div id="comment-15164" class="comment not_top_scorer"><div id="post-15164-score" class="comment-score"></div><div class="comment-text"><p>Also <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Wiki capture setup</a>.</p></div><div id="comment-15164-info" class="comment-info"><span class="comment-age">(22 Oct '12, 08:14)</span> Jaap ♦</div></div></div><div id="comment-tools-15123" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-15123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

