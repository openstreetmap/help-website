+++
type = "question"
title = "Troubleshooting slow FTP speed"
description = '''client 10.240.12.251(as C251) and client 10.224.180.179(as C179) connected with 30M long distance leased line, with round-trip time 36ms.  when upload from C251 to C179 via FTP, speed will be 3.5MBps, it&#x27;s fine.  while download from C179 to C251 via FTP, speed drop to 538KBps, it&#x27;s hard to accept it...'''
date = "2015-10-09T04:06:00Z"
lastmod = "2015-10-09T08:19:00Z"
weight = 46428
keywords = [ "ftp", "tcp" ]
aliases = [ "/questions/46428" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting slow FTP speed](/questions/46428/troubleshooting-slow-ftp-speed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46428-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>client 10.240.12.251(as C251) and client 10.224.180.179(as C179) connected with 30M long distance leased line, with round-trip time 36ms. when upload from C251 to C179 via FTP, speed will be 3.5MBps, it's fine. while download from C179 to C251 via FTP, speed drop to 538KBps, it's hard to accept it. the download session is captured and uploaded to cloudshark @: <a href="https://www.cloudshark.org/captures/458343b01b3c">https://www.cloudshark.org/captures/458343b01b3c</a> it seems that thare are many "Tcp Dup Ack", "TCP Retransmission" &amp; "TCP Out-Of-Order"</p><p>it's really appreciate that anyone can help to find the root cause, thanks.</p></div><div id="question-tags" class="tags-container tags">ftp tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '15, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/817a1d23e48fc99690e8415704e8c4dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevin&#39;s gravatar image" /><p>kevin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '15, 04:09</p></div></div><div id="comments-container-46428" class="comments-container"></div><div id="comment-tools-46428" class="comment-tools"></div><div class="clear"></div><div id="comment-46428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46435"></span>

<div id="answer-container-46435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46435-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The root cause is packet loss and a relatively high retransmission timeout at the sender combined with a delayed_ACK at the receiver.<br />
There are 3 instances where the transmission stalls, twice because of the 330 ms RTO at the sender and once due to the 200 delayACK timer at the receiver<br />
</p><pre><code>(frame.number&gt;109&amp;&amp;frame.number&lt;113)||(frame.number&gt;1444&amp;&amp;frame.number&lt;1447)</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-7_v0qwCLm.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '15, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '15, 08:20</p></div></div><div id="comments-container-46435" class="comments-container"><span id="46443"></span><div id="comment-46443" class="comment"><div id="post-46443-score" class="comment-score"></div><div class="comment-text"><p>Hi MrEEde, a few observation here, packet 111 is not retransmission and looks 346 ms delay here could be due to APP(FTP), and about packet 1446, even here 340 ms delay doesnt looks to be due to RTO bcause due to sack enabled sender has the information to make intelligent decisions about which packets to retransmit.</p></div><div id="comment-46443-info" class="comment-info"><span class="comment-age">(10 Oct '15, 03:48)</span> kishan pandey</div></div><span id="46464"></span><div id="comment-46464" class="comment"><div id="post-46464-score" class="comment-score"></div><div class="comment-text"><p>Having a trace at the receiver only we and wireshark cannot recognize packet 111 as a retransmission (as we didn't see the original transmission arriving). Still my bet is that - if we took a trace at the sender - we would see this sement being sent twice .</p><p>Packet 1146 is in fact flagged as a retransmission with tcp.analysis.rto gt 0.3 arriving with a delay of 336 ms after 1444 (which already was a retransmission... So - with an RTT of 36 ms - this is too close to the default MinRTO 300ms of the windows server to be coincidental ....</p></div><div id="comment-46464-info" class="comment-info"><span class="comment-age">(12 Oct '15, 03:13)</span> mrEEde</div></div></div><div id="comment-tools-46435" class="comment-tools"></div><div class="clear"></div><div id="comment-46435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

