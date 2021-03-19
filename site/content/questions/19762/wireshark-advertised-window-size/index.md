+++
type = "question"
title = "Wireshark - Advertised Window size"
description = '''Hi, I&#x27;m new in here and would like to ask a question. I&#x27;m currently working on my Bachelor thesis. I need to change receiver buffer (advertised window). and, except for Wireshark I need to use another application - FlowGrind (to get Congestion window, as that is not present in packet and can`t be se...'''
date = "2013-03-22T13:35:00Z"
lastmod = "2013-03-25T12:50:00Z"
weight = 19762
keywords = [ "window", "advertised" ]
aliases = [ "/questions/19762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - Advertised Window size](/questions/19762/wireshark-advertised-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19762-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new in here and would like to ask a question. I'm currently working on my Bachelor thesis. I need to change receiver buffer (advertised window). and, except for Wireshark I need to use another application - FlowGrind (to get Congestion window, as that is not present in packet and can`t be seen in Wireshark). The thing is: When I set "receiver buffer size (advertised window) in FlowGrind and then run it, I see different Windows size in Wireshark. For example: FlowGrind - Wireshark 400 - 1200, 2000 - 1460, 4000 - 2896, 6000 - 4392. After simple calculation, I found out that the Wireshark value is always about 70% of value set in FlowGrind. IS ANYBODY ABLE TO EXPLAIN THAT, PLEASE?</p><p>Thank you in advance</p><p>Radim</p></div><div id="question-tags" class="tags-container tags">window advertised</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '13, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/198f364985a629d7dd0991bc6a838e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="radim0574&#39;s gravatar image" /><p>radim0574<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="radim0574 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '13, 14:22</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-19762" class="comments-container"></div><div id="comment-tools-19762" class="comment-tools"></div><div class="clear"></div><div id="comment-19762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19822"></span>

<div id="answer-container-19822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19822-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Flowgrind documentation speaks of the receive buffer size and the advertised window as if they are the same thing. Strictly speaking, they are not. The receive buffer size is the size of the buffer that is allocated in memory to receive incoming TCP data on that connection. Once this buffer is allocated, its size does not generally change.</p><p>The advertised window is the amount of space <em>available</em> in the receive buffer. While the size of the buffer does not change, the amount of space available in the buffer changes. As incoming data is received and is stored in the buffer, the amount of space available (the advertised window) goes down. Then when the application pulls data out of the receive buffer, the amount of space available goes up.</p><p>Wireshark shows the actual advertised window, which changes dynamically.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19822" class="comments-container"><span id="19835"></span><div id="comment-19835" class="comment"><div id="post-19835-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thank you for your answer, however, that doesn`t clear this up at all:). My text focuses on two things: 1) Wireshark - Congestion windown (ANY possibility how to find out) 2) FlowGrind &amp; Wireshark "Advertiised window" differences as mentioned above, in my firt text</p><p>Regards,</p><p>Radim</p></div><div id="comment-19835-info" class="comment-info"><span class="comment-age">(26 Mar '13, 04:48)</span> radim0574</div></div></div><div id="comment-tools-19822" class="comment-tools"></div><div class="clear"></div><div id="comment-19822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

