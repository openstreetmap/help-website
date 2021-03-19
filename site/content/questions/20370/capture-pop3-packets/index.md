+++
type = "question"
title = "Capture POP3 packets"
description = '''Hello Im trying to analyze the POP3 traffic on my network but Wireshark doesn&#x27;t capture anything on port 110 nor 995. What does this mean? Why can&#x27;t I see any packets? Shouldn&#x27;t I be able to even though they are encrypted? Thank you'''
date = "2013-04-12T02:23:00Z"
lastmod = "2013-04-12T02:27:00Z"
weight = 20370
keywords = [ "pop3" ]
aliases = [ "/questions/20370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture POP3 packets](/questions/20370/capture-pop3-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>Im trying to analyze the POP3 traffic on my network but Wireshark doesn't capture anything on port 110 nor 995. What does this mean? Why can't I see any packets? Shouldn't I be able to even though they are encrypted?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">pop3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '13, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/5fea58481cbc3b8c4d30db7c29230b22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metall&#39;s gravatar image" /><p>Metall<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metall has no accepted answers">0%</span></p></div></div><div id="comments-container-20370" class="comments-container"></div><div id="comment-tools-20370" class="comment-tools"></div><div class="clear"></div><div id="comment-20370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20371"></span>

<div id="answer-container-20371" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20371-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you should be if your capture setup is correct. You're saying you try to "analyze on your network" - does that mean that you want to capture packets from PCs other than the one you're on? If so, you need to do a SPAN or TAP session. For more information on how to capture packets on a network, try this Wiki page: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>On a side note: POP3 on port 110 is usually not encrypted, that is what port 995 is used for.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '13, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20371" class="comments-container"><span id="20372"></span><div id="comment-20372" class="comment"><div id="post-20372-score" class="comment-score"></div><div class="comment-text"><p>Yes thats right. I want to capture the packets from other PC's then mine. So I have to do a SPAN session in which I need to have access to the switch? Isn't there some other way? I thought Wireshark capture all traffic on the network, including what other hosts on the network is sending/recieveing :O</p></div><div id="comment-20372-info" class="comment-info"><span class="comment-age">(12 Apr '13, 02:59)</span> Metall</div></div><span id="20374"></span><div id="comment-20374" class="comment"><div id="post-20374-score" class="comment-score"></div><div class="comment-text"><p>Yes, you need a SPAN session, and for that you need to access the switch, which also means that it needs to be manageable and providing a SPAN port feature.</p><p>And no, Wireshark can only capture the packets that make it to the network card you're capturing on. In a switched network that will only mean unicasts that are directed at your card, broadcasts and multicasts. If you want to see more than that you need to SPAN the other machine(s) to force the switch to send you their packets as well.</p><p>The times of seeing everything other hosts send and receive are over since we replaced all the hubs with switches ;-)</p><p>(I converted your answer to a comment)</p></div><div id="comment-20374-info" class="comment-info"><span class="comment-age">(12 Apr '13, 03:02)</span> Jasper ♦♦</div></div><span id="20376"></span><div id="comment-20376" class="comment"><div id="post-20376-score" class="comment-score"></div><div class="comment-text"><p>Oh I see. But do you know about other software that can capture packets that is sent/recieved on other hosts on the network? I am doing an evaluation on the network considered to security. I am doing an undergraduated thesis and is on a company network, so I can not enter switches and routers. I am suppose to look and analyze the nework to see how much an intruder can see.</p></div><div id="comment-20376-info" class="comment-info"><span class="comment-age">(12 Apr '13, 03:21)</span> Metall</div></div><span id="20378"></span><div id="comment-20378" class="comment"><div id="post-20378-score" class="comment-score"></div><div class="comment-text"><p>No sniffing software can do this unless the packets arrive at the capturing card for some reason. The "legal" way of doing that is using SPAN ports, as you already know. The "illegal" way would be to apply hacking techniques like ARP cache poisoning, like the windows tool "Cain &amp; Abel" does. It forces the switch to redirect packets to your card by "spreading lies" on the network.</p><p>The usual answer to the question what an intruder can see is "not much, except broadcasts, multicasts and sometimes single flooded unicasts", <strong>unless</strong> he's leveraging ARP cache poisoning or other tricks. Or he could manage to hack into a switch first to create his own SPAN sessions, that is :-)</p></div><div id="comment-20378-info" class="comment-info"><span class="comment-age">(12 Apr '13, 03:25)</span> Jasper ♦♦</div></div></div><div id="comment-tools-20371" class="comment-tools"></div><div class="clear"></div><div id="comment-20371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

