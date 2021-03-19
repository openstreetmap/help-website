+++
type = "question"
title = "will wireshark help diagnose this problem?"
description = '''I have a wired home network with 2 Macs and one Windows 7 PC. I have videos on 9 NAS&#x27;s connected to the network. The network contains a router, which is connected to a cable modem. The NAS&#x27;s are connected to a switch, which is connected to the router. The PC and Macs are connected to another switch,...'''
date = "2010-12-19T17:03:00Z"
lastmod = "2010-12-22T04:07:00Z"
weight = 1400
keywords = [ "speed", "internet" ]
aliases = [ "/questions/1400" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [will wireshark help diagnose this problem?](/questions/1400/will-wireshark-help-diagnose-this-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1400-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a wired home network with 2 Macs and one Windows 7 PC. I have videos on 9 NAS's connected to the network. The network contains a router, which is connected to a cable modem. The NAS's are connected to a switch, which is connected to the router. The PC and Macs are connected to another switch, also connected to the router. The switches are unmanaged. When the Windows 7 PC is connected to the network, Internet speed becomes very slow; when the connection of the PC to the network is broken, Internet speed on the Macs is very fast.</p><p>Would Wireshark help diagnose what problem could happening?</p></div><div id="question-tags" class="tags-container tags">speed internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '10, 17:03</strong></p><img src="https://secure.gravatar.com/avatar/93c800193ab6fd2773429b979881679e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyeman&#39;s gravatar image" /><p>eyeman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyeman has no accepted answers">0%</span></p></div></div><div id="comments-container-1400" class="comments-container"><span id="1436"></span><div id="comment-1436" class="comment"><div id="post-1436-score" class="comment-score"></div><div class="comment-text"><p>Drastically slower? It's possible that W7 is just using the available BW, or it's possible that it's trying to act as an internet gateway, only to give up because it's not supposed to be the internet gateway (internet sharing, I believe it's called). But if you capture on W7 as Jaap suggested, you might have a better idea.</p></div><div id="comment-1436-info" class="comment-info"><span class="comment-age">(21 Dec '10, 06:46)</span> hansangb</div></div></div><div id="comment-tools-1400" class="comment-tools"></div><div class="clear"></div><div id="comment-1400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1403"></span>

<div id="answer-container-1403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1403-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you could Wireshark the network connection of the Windows 7 PC when the problem shows and look at the statistics it reports to see what top talkers are, which end points are involved, etc. That could give you an idea where to look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '10, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1403" class="comments-container"><span id="1437"></span><div id="comment-1437" class="comment"><div id="post-1437-score" class="comment-score"></div><div class="comment-text"><p>I am new to Wireshark, but I did run it on the involved W7 PC..most of the capture shows (according to the color scheme) "Bad TCP"....it appears that the W7 is communicating with many different external IP addresses...I am not actively surfing the Web on the W7 PC. I am a noob, and would appreciate some guidance</p></div><div id="comment-1437-info" class="comment-info"><span class="comment-age">(21 Dec '10, 07:04)</span> eyeman</div></div><span id="1440"></span><div id="comment-1440" class="comment"><div id="post-1440-score" class="comment-score"></div><div class="comment-text"><p>Your average PC will be trying to connect to quite a lot of external addresses. Legitimate reasons include accessing DNS to resolve names to IP addresses, and then attempting to update software from Microsoft or other application vendors. However once updates are completed the only activity should be as a result of using applications like web browsers or mail programs.</p></div><div id="comment-1440-info" class="comment-info"><span class="comment-age">(21 Dec '10, 17:09)</span> martyvis</div></div><span id="1441"></span><div id="comment-1441" class="comment"><div id="post-1441-score" class="comment-score">1</div><div class="comment-text"><p>If you see a lot activity that appears to be to and from external addresses, it could be that your machine infected by some sort of malware (trojan/bot/rootkit). Wireshark will show the activity (probably Statistics:Endpoints is your best bet). If you feel your machine is comprised you might want to seek out a good AV or Spyware scanning software program to check it.</p></div><div id="comment-1441-info" class="comment-info"><span class="comment-age">(21 Dec '10, 17:09)</span> martyvis</div></div><span id="1442"></span><div id="comment-1442" class="comment"><div id="post-1442-score" class="comment-score"></div><div class="comment-text"><p>If the "Bad TCP" you are referring to, it is probably a red herring as a result of you using a TCP offloading driver on your network card. Refer to http://wiki.wireshark.org/TCP_Checksum_Verification</p></div><div id="comment-1442-info" class="comment-info"><span class="comment-age">(21 Dec '10, 17:13)</span> martyvis</div></div></div><div id="comment-tools-1403" class="comment-tools"></div><div class="clear"></div><div id="comment-1403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1452"></span>

<div id="answer-container-1452" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1452-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Martyvis, Jaap, Hansagb</p><p>Thanks for your help and suggestions.</p><p>The W7 did have some infections, picked up by Avira. I usually run updates and scans with Avira, as well as Malwarebytes Anti-malware; this was the first infection it's picked up in a while. I have the W7 PC disconnected from yhe network while I run another scan, and will Wireshark again tonight</p><p>Todd</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '10, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/93c800193ab6fd2773429b979881679e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyeman&#39;s gravatar image" /><p>eyeman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyeman has no accepted answers">0%</span></p></div></div><div id="comments-container-1452" class="comments-container"></div><div id="comment-tools-1452" class="comment-tools"></div><div class="clear"></div><div id="comment-1452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

