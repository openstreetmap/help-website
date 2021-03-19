+++
type = "question"
title = "My laptop makes weird connections, checked with Wireshark"
description = '''Hi,  I&#x27;ve been experiencing problems with my webmail server : The firewall blocks my IP address with the message : xxx.xxx.xxx.xxx# lfd: (imapd) Failed IMAP login from xxx.xxx.xxx.xxx (CA/Canada/bas1-quebec15-3096557528.dsl.bell.ca): 10 in the last 3600 secs - Fri Nov 21 07:20:13 2014  But, I have N...'''
date = "2014-11-21T11:04:00Z"
lastmod = "2014-11-21T16:04:00Z"
weight = 38049
keywords = [ "wireshark" ]
aliases = [ "/questions/38049" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [My laptop makes weird connections, checked with Wireshark](/questions/38049/my-laptop-makes-weird-connections-checked-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38049-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've been experiencing problems with my webmail server : The firewall blocks my IP address with the message : xxx.xxx.xxx.xxx# lfd: (imapd) Failed IMAP login from xxx.xxx.xxx.xxx (CA/Canada/bas1-quebec15-3096557528.dsl.bell.ca): 10 in the last 3600 secs - Fri Nov 21 07:20:13 2014</p><p>But, I have NO IMAP account anymore (only 1 POP3). So I've launch several programms to know about this weird connection which blocks my IP address from my server even when my laptop is OFF (at 7:20 am this morning I was sleeping and my laptop closed).</p><p>On Wiresharks, I see some connections to my ex-husband PC but I'm not sure how to interpret what I read. Does anybody can help me ?</p><p>Here is the report : <a href="http://www.cbwebconception.com/rep_wireshark21nov2014.pcapng">http://www.cbwebconception.com/rep_wireshark21nov2014.pcapng</a></p><p>The lines which make me afraid are from 1 to 22 (the beginning), where ERIC-PC is displayed (my ex-husband laptop, but my ex-husband live at 700 km from me, in GASPE). His IP address is 75.152.63.26. and this IP address is on lines 19 to 22. (it's a globetrotter / TELUS connection).</p><p>Please can you help me ? I'm afraid my ex-husband has access to my e-mail and /or files.</p><p>Thank you,</p><p>Chris</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '14, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/13acebdac5dee9235f8605003c030be6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris427&#39;s gravatar image" /><p>Chris427<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris427 has no accepted answers">0%</span></p></div></div><div id="comments-container-38049" class="comments-container"></div><div id="comment-tools-38049" class="comment-tools"></div><div class="clear"></div><div id="comment-38049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38052"></span>

<div id="answer-container-38052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38052-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The lines 19 to 22 are Windows file share (SMB/CIFS) connection attempts, but they fail. For some reason your PC tries to access his IP, maybe because you had some sort of mapped share? The DNS packets before that also look for a device called "ERIC-PC", so there is probably something configured on your PC to connect to that IP. If you don't know what it may be or cannot find out what software/setting this comes from you should consider reinstalling, just to be safe.</p><p>Also, just to be sure, you should change all your online passwords. It's the only way to be sure that he can't access your data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '14, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38052" class="comments-container"><span id="38053"></span><div id="comment-38053" class="comment"><div id="post-38053-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper !</p><p>Thank you for your comment.</p><p>What is "some sort of mapped share" ? The device called "ERIC-PC" is my Ex-husband. We are in court. Hard time. I had suspected him to read my e-mail or listen my phone calls. But now, I'm becoming a bit crazy when I see his laptop name and his IP address on the report.</p><p>I don't want to reinstal my system as if he could get my personnal information (my e-mail with my attorney for example), I want to keep the information to proove it.</p><p>Do you know how I can see what is sending and what is sent from my laptop to ERIC-PC ?</p><p>Many Thanks for your help,</p><p>Chris</p></div><div id="comment-38053-info" class="comment-info"><span class="comment-age">(21 Nov '14, 13:15)</span> Chris427</div></div><span id="38055"></span><div id="comment-38055" class="comment"><div id="post-38055-score" class="comment-score"></div><div class="comment-text"><p>Well, often PCs at home are doing peer to peer connections, e.g. to share music, pictures and videos. Microsoft Windows tries to establish this kinds of sharing groups automatically from Windows 7 and up, so maybe your PC was in a such a relation to your ex-husbands PC. The strange thing is that the connection is going out to a public IP - usually, those kinds of sharing connections are made within private networks.</p><p>In the trace you posted your PC tries to connect to your ex-husbands IP multiple times, but never succeeds. It's all Windows File share, not email or VoIP. You could configure your own firewall to block everything going to that IP, to be sure nothing gets out.</p><p>Otherwise, check if you have mapped drives on your PC, e.g. by checking if there is any drive letter in your explorer mapped to something starting with "\", especially "\eric-pc".</p><p>Maybe it's some sort of application that tries this, so you could also check in the control panel if there is any application you don't need anymore and deinstall it.</p><p>If you want to keep the system to prove something you should stop using it and get another PC that you can use instead.</p></div><div id="comment-38055-info" class="comment-info"><span class="comment-age">(21 Nov '14, 13:38)</span> Jasper ♦♦</div></div></div><div id="comment-tools-38052" class="comment-tools"></div><div class="clear"></div><div id="comment-38052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38060"></span>

<div id="answer-container-38060" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38060-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Jasper,</p><p>Thank you for your comment. " The strange thing is that the connection is going out to a public IP - usually, those kinds of sharing connections are made within private networks."</p><p>This is strange yes. and we have never shared anything with our computers. Maybe we had only the local printer in common. Which is strange too : his IP adresse in GASPE 75.152.63.26. Look at this line (from Wireshark report ) What is a TCP Retransmission ?</p><p>498787 10894.250517000 192.168.5.5 75.152.63.26 TCP 66 [TCP Retransmission] 8036→139 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1</p><p>Maybe today he cannot receive anything but I guess before the 9th of October he could receive.</p><p>Thank you,</p><p>Chris</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '14, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/13acebdac5dee9235f8605003c030be6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris427&#39;s gravatar image" /><p>Chris427<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris427 has no accepted answers">0%</span></p></div></div><div id="comments-container-38060" class="comments-container"></div><div id="comment-tools-38060" class="comment-tools"></div><div class="clear"></div><div id="comment-38060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

