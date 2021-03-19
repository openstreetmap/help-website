+++
type = "question"
title = "Network Print aborts (Windows Server) TCP DUP ACK - TCP RST"
description = '''Hi I need some help with a strange issue. We&#x27;ve got a virtual Windows print server (192.168.13.20) and bunch of network printers. At one printer (192.168.12.28), some huge jobs (a few hundret pages) are aborting sporadically. Subnet is 192.168.8.0/21 The VM-Host has got teamed NIC&#x27;s. In Wireshark i ...'''
date = "2016-11-07T07:26:00Z"
lastmod = "2016-11-07T08:14:00Z"
weight = 57053
keywords = [ "windows", "reset", "printing", "disconnect", "tcp" ]
aliases = [ "/questions/57053" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Network Print aborts (Windows Server) TCP DUP ACK - TCP RST](/questions/57053/network-print-aborts-windows-server-tcp-dup-ack-tcp-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57053-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I need some help with a strange issue. We've got a virtual Windows print server (192.168.13.20) and bunch of network printers. At one printer (192.168.12.28), some huge jobs (a few hundret pages) are aborting sporadically. Subnet is 192.168.8.0/21 The VM-Host has got teamed NIC's.</p><p>In Wireshark i can see, that the printer is sending some TCP Dup ACK's an the server is sending some retransmits before sending TCP-Reset to that printer.</p><p>On our switches RSTP is enabled and configured and there are no port errors down the way.</p><p>Does anyone have an idea whats causing this behaviour?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark-printer_oTqY3Cc.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">windows reset printing disconnect tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/698f8ccd3fe61537ce80158e0b8000b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DennisM&#39;s gravatar image" /><p>DennisM<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DennisM has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '16, 01:45</p></div></div><div id="comments-container-57053" class="comments-container"><span id="57116"></span><div id="comment-57116" class="comment"><div id="post-57116-score" class="comment-score"></div><div class="comment-text"><p>To give a little more details: Windows printserver is a virtual machine. Its host machine is connected to an HP-ProcurveSwitch[1] (RSTP-Rootbridge Prio 0). Another HP (Aruba)-Switch[2] (RSTP Prio 4096)is connected via two trunked 1000SX(Fiber)-lines. Connected to that switch is another Switch[3] (Cisco SG300-52, RSTP Prio 20480) on which the printer is connected. Every switch has got its newest firmware. Is it possible that problem is caused due to different vendors?</p></div><div id="comment-57116-info" class="comment-info"><span class="comment-age">(07 Nov '16, 22:40)</span> DennisM</div></div></div><div id="comment-tools-57053" class="comment-tools"></div><div class="clear"></div><div id="comment-57053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57065"></span>

<div id="answer-container-57065" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57065-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A screenshot is not so good for an analysis, but I will try. Seems you got some packet loss. Maybe you have somewhere a duplex-mismatch, if rstp does not report any problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-57065" class="comments-container"><span id="57115"></span><div id="comment-57115" class="comment"><div id="post-57115-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. I checked duplex-settings but could not find any mismatch on the way between server and printer.</p></div><div id="comment-57115-info" class="comment-info"><span class="comment-age">(07 Nov '16, 22:30)</span> DennisM</div></div><span id="57118"></span><div id="comment-57118" class="comment"><div id="post-57118-score" class="comment-score"></div><div class="comment-text"><p>No, I think your switches are ok so far. Where did you take the trace. Maybe the problem is inside the vm environment.</p></div><div id="comment-57118-info" class="comment-info"><span class="comment-age">(07 Nov '16, 23:04)</span> Christian_R</div></div><span id="57135"></span><div id="comment-57135" class="comment"><div id="post-57135-score" class="comment-score"></div><div class="comment-text"><p>This was captured on that Windows-VM. There are several printers connected to that print server. It is a bit curious, that this problem seems to exists only with that printer. I had already tried to operate the printer at another switch.-same issue here (traced via mirror-port on printer-side).</p></div><div id="comment-57135-info" class="comment-info"><span class="comment-age">(08 Nov '16, 01:14)</span> DennisM</div></div><span id="57137"></span><div id="comment-57137" class="comment"><div id="post-57137-score" class="comment-score"></div><div class="comment-text"><p>How is the printer interface configured? Autoneg or fix values?</p></div><div id="comment-57137-info" class="comment-info"><span class="comment-age">(08 Nov '16, 01:30)</span> Christian_R</div></div><span id="57140"></span><div id="comment-57140" class="comment"><div id="post-57140-score" class="comment-score"></div><div class="comment-text"><p>Server resets the connection because it does not see answers (ACKs) to it's retransmissions. These retransmissions could be dropped a) somewhere on the path or b) by the printer itself. To check where exactly retransmissions have been dropped (or even printer's ACKs were dropped) it would be nice to do printer-side capture (for example, mirroring the port which is heading directly to the printer) and examine this capture.</p><p>Check it out also that printer answered ARP query later, so it's IP stack remains alive.</p><p>Anyway, it would be better if you could share printer-side capture (not just screenshot).</p></div><div id="comment-57140-info" class="comment-info"><span class="comment-age">(08 Nov '16, 01:39)</span> Packet_vlad</div></div><span id="57601"></span><div id="comment-57601" class="comment not_top_scorer"><div id="post-57601-score" class="comment-score"></div><div class="comment-text"><p>I've been in contact with the manufacturer of that printer, because this issue occurs even with an identical printer. Tested it on different switches with different hops in between. They said, that eventually their TCP-IP-implementation or some hardwary might be faulty. The error occurs sporadically and i'm unable to force reproduce it. Unfortunately the error still remains but i ran wireshark on the print server and at the printers-switch (portmirror) at the same time. It shows the same picture on both sides, so i'm sure there are no drop on the line.<img src="https://osqa-ask.wireshark.org/upfiles/wireshark-printer-server-printer-identical.JPG" alt="Compare" /></p></div><div id="comment-57601-info" class="comment-info"><span class="comment-age">(24 Nov '16, 05:41)</span> DennisM</div></div><span id="57602"></span><div id="comment-57602" class="comment not_top_scorer"><div id="post-57602-score" class="comment-score"></div><div class="comment-text"><p>About what printer do we talk? Manufacture and Modell?</p></div><div id="comment-57602-info" class="comment-info"><span class="comment-age">(24 Nov '16, 06:04)</span> Christian_R</div></div></div><div id="comment-tools-57065" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-57065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

