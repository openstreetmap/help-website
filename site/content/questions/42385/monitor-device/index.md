+++
type = "question"
title = "Monitor Device"
description = '''Hello I&#x27;m trying to find the right tool for monitoring how much of the LAN bandwidth the devices on the LAN are using in real time. I have be told to try wireshark but I seem to on be able o monitor my own LAN connection not the entire network. Thanks in advance'''
date = "2015-05-14T04:17:00Z"
lastmod = "2015-05-14T05:42:00Z"
weight = 42385
keywords = [ "capture", "lan", "monitor", "localnetwork" ]
aliases = [ "/questions/42385" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor Device](/questions/42385/monitor-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42385-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I'm trying to find the right tool for monitoring how much of the LAN bandwidth the devices on the LAN are using in real time. I have be told to try wireshark but I seem to on be able o monitor my own LAN connection not the entire network.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">capture lan monitor localnetwork</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/974bc0f25afce2e1464f2da039d2389a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ginger1979&#39;s gravatar image" /><p>ginger1979<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ginger1979 has no accepted answers">0%</span></p></div></div><div id="comments-container-42385" class="comments-container"><span id="42386"></span><div id="comment-42386" class="comment"><div id="post-42386-score" class="comment-score"></div><div class="comment-text"><p>Must it be freeware? You want to do it, just by capturing the traffic? About what bandwith you are talking?</p></div><div id="comment-42386-info" class="comment-info"><span class="comment-age">(14 May '15, 04:26)</span> Christian_R</div></div><span id="42389"></span><div id="comment-42389" class="comment"><div id="post-42389-score" class="comment-score"></div><div class="comment-text"><p>Nope doesn't have to be free But will need a free trial) I want to see which device is using the most LAN traffic at a point in time. The problem is users copying large amounts of data across the network which is slowing the network down making other systems lag until the copy has finished.</p><p>So when some tell me the system is lagging I can see who is using all the Local Bandwidth</p><p>If this program could send alert to when a single device is using over say 20% of the LAN bandwidth that would be great.</p></div><div id="comment-42389-info" class="comment-info"><span class="comment-age">(14 May '15, 04:36)</span> ginger1979</div></div></div><div id="comment-tools-42385" class="comment-tools"></div><div class="clear"></div><div id="comment-42385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42391"></span>

<div id="answer-container-42391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42391-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe this tool could solve your prob. SteelCentral Packet Analyzer Personal Edition It should have all the functions you want, from my point of view.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-42391" class="comments-container"></div><div id="comment-tools-42391" class="comment-tools"></div><div class="clear"></div><div id="comment-42391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42392"></span>

<div id="answer-container-42392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42392-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to look at your capture setup, particularly in a switched network. See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a>, and note particularly the sections on capturing on switched networks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42392" class="comments-container"></div><div id="comment-tools-42392" class="comment-tools"></div><div class="clear"></div><div id="comment-42392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

