+++
type = "question"
title = "Trying to identify the source of some traffic"
description = '''Hi there. I&#x27;m trying to use Wireshark to identify whatever software is behind some traffic on my PC. Unfortunately, while I&#x27;ve identfied some likely packets, I know virtually nothing about how to read them. I can&#x27;t see anything immediately obvious, so can someone tell me how, if it&#x27;s even possible? ...'''
date = "2013-07-21T10:34:00Z"
lastmod = "2013-07-21T10:55:00Z"
weight = 23210
keywords = [ "origin", "sofware" ]
aliases = [ "/questions/23210" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Trying to identify the source of some traffic](/questions/23210/trying-to-identify-the-source-of-some-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23210-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there.</p><p>I'm trying to use Wireshark to identify whatever software is behind some traffic on my PC. Unfortunately, while I've identfied some likely packets, I know virtually nothing about how to read them. I can't see anything immediately obvious, so can someone tell me how, if it's even possible?</p><p>A little background: I have another PC on my home LAN which is acting as a media centre and network storage. I want it to go to sleep whenever it's not busy, but I also want it to wake on LAN whenever the other computers in the house need to access it. At the moment, it's set to sleep after 10 minutes, but when any of the other computers in the house are turned on, the media PC tends to be woken up almost immediately after going to sleep - typically between 30 seconds and 2 minutes. I want to find out what software or function is causing the other PCs to wake the media PC so that I can stop it from happening so often.</p><p>I've watched the media PC wake from sleep and then looked for packets sent to that PC at the same time as it woke up. I've got four particular packets which I guess are responsible for the wakeup: looking in the Info field in Wireshark, they're all the same, apart from the source port. Here's an example:</p><p>50666 &gt; wsdapi [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1</p><p>I'm assuming that there isn't enough information in the info field to tell me what's actually sending the packet. I've looked through the full details for one of these packets and I don't recognise anything in it as the originating software, but as I said, I don't know enough to know what I'm looking for, if it's even in there.</p><p>Can someone please advise me? Is it possible to identify the software sending these wake-up packets? If so, how? I've saved one of the capture files, so I assume that I can strip out the four packets I've flagged and post them in here if that's useful.</p><p>Thanks in advance,</p><p>Neil.</p></div><div id="question-tags" class="tags-container tags">origin sofware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '13, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/9656a36332178b9769ee4a5f2c2f0469?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NJMorf&#39;s gravatar image" /><p>NJMorf<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NJMorf has no accepted answers">0%</span></p></div></div><div id="comments-container-23210" class="comments-container"><span id="23213"></span><div id="comment-23213" class="comment"><div id="post-23213-score" class="comment-score"></div><div class="comment-text"><p>If you can access the sending device e.g. another PC simply go for netstat in a console window like cmd.exe under Windows.</p><p>Netstat can show the associated Process ID for the network sessions, especially for TCP connections. Just lookup the port numbers there and then you have at least the process initiating the connection you're looking for</p></div><div id="comment-23213-info" class="comment-info"><span class="comment-age">(21 Jul '13, 12:33)</span> Landi</div></div><span id="23217"></span><div id="comment-23217" class="comment"><div id="post-23217-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks, I'll try that too.</p></div><div id="comment-23217-info" class="comment-info"><span class="comment-age">(21 Jul '13, 13:36)</span> NJMorf</div></div></div><div id="comment-tools-23210" class="comment-tools"></div><div class="clear"></div><div id="comment-23210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23211"></span>

<div id="answer-container-23211" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23211-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't (at present) identify which process is transmitting traffic, so only using Wireshark you would have to identify the process from inspecting the traffic.</p><p>The (minimal) traffic details you have posted show the process is attempting to open a connection (the SYN) to the NAS. The destination port is the one used for <a href="http://en.m.wikipedia.org/wiki/Web_Services_for_Devices">wsdapi</a> a protocol used for accessing printers and file shares so you might be on the right track.</p><p>Network Monitor from Microsoft can associate the traffic with the sending process, so using that would help you somewhat, but I think it likely that the traffic will be coming from a system process and thus from a 'host' process that is home to a few services.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '13, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23211" class="comments-container"><span id="23215"></span><div id="comment-23215" class="comment"><div id="post-23215-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks for the pointers. I've installed Network Monitor, I'll see what it can tell me.</p></div><div id="comment-23215-info" class="comment-info"><span class="comment-age">(21 Jul '13, 12:46)</span> NJMorf</div></div></div><div id="comment-tools-23211" class="comment-tools"></div><div class="clear"></div><div id="comment-23211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

