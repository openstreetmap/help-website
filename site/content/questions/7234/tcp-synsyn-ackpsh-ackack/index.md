+++
type = "question"
title = "TCP SYN/SYN ACK/PSH ACK/ACK"
description = '''Dear Wireshark, After the TCP connection established, the client program sent Packet #7 to the server to check the settings. The server replied Packet #8 (included the setting data) and Packet #9 (ACK) to the client. Since the client received Packet #8, it sent Packet #10 (ACK) to the server. The se...'''
date = "2011-11-04T03:35:00Z"
lastmod = "2011-11-09T23:36:00Z"
weight = 7234
keywords = [ "tcp" ]
aliases = [ "/questions/7234" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP SYN/SYN ACK/PSH ACK/ACK](/questions/7234/tcp-synsyn-ackpsh-ackack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7234-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Wireshark,</p><p>After the TCP connection established, the client program sent Packet #7 to the server to check the settings. The server replied Packet #8 (included the setting data) and Packet #9 (ACK) to the client. Since the client received Packet #8, it sent Packet #10 (ACK) to the server.</p><p>The sequence number of Packet #8 is 1, and the data length is 6, so the sequence number of the next packet sent by the server should be 7 (1+6). But in the WireShark log file as you can see, the sequence number of Packet #9 is still 1, not 7. Therefore the client will abandon Packet #9 since Packet #9 is not the ACK packet which the client expected to receive. So the client will re-transmit Packet #11 to the server, and the sequence number in the Packet #12 is 7, which is the correct ACK packet.</p><p>This symptom happened after every packet sent from the client.</p><p>Best Regards, Jimmy</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '11, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/55c0b8c5349381f5bcd8bebdf024e436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jimmy&#39;s gravatar image" /><p>Jimmy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jimmy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '11, 03:50</p></div></div><div id="comments-container-7234" class="comments-container"><span id="7245"></span><div id="comment-7245" class="comment"><div id="post-7245-score" class="comment-score">1</div><div class="comment-text"><p>Drop it on <a href="http://cloudshark.org/">CloudShark</a> and post the URL here, so we can all see the capture.</p></div><div id="comment-7245-info" class="comment-info"><span class="comment-age">(05 Nov '11, 02:54)</span> Jaap ♦</div></div><span id="7257"></span><div id="comment-7257" class="comment"><div id="post-7257-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap,</p><p>I cannot upload the capture by CloudShark, why?</p><p>Jimmy</p></div><div id="comment-7257-info" class="comment-info"><span class="comment-age">(06 Nov '11, 19:17)</span> Jimmy</div></div><span id="7271"></span><div id="comment-7271" class="comment"><div id="post-7271-score" class="comment-score"></div><div class="comment-text"><p>Why? What what? Why you cannot upload the capture to CloudShark? Ask the CloudShark people. You cannot upload because you're not allowed, and why do we need to see the capture? There are some strange items in your story. The devil is in the details here, which the capture can expose.</p></div><div id="comment-7271-info" class="comment-info"><span class="comment-age">(08 Nov '11, 01:49)</span> Jaap ♦</div></div><span id="7272"></span><div id="comment-7272" class="comment"><div id="post-7272-score" class="comment-score"></div><div class="comment-text"><p>It just shows "Upload in progress... Please wait." Can you provide your e-mail, then I can send the capture to you if you think it is ok. Thanks.</p><p>Jimmy</p></div><div id="comment-7272-info" class="comment-info"><span class="comment-age">(08 Nov '11, 02:12)</span> Jimmy</div></div><span id="7279"></span><div id="comment-7279" class="comment"><div id="post-7279-score" class="comment-score"></div><div class="comment-text"><p>Jimmy, click the "Contact" link over on CloudShark.org and they'll help you get the file uploaded.</p></div><div id="comment-7279-info" class="comment-info"><span class="comment-age">(08 Nov '11, 06:44)</span> zachad</div></div><span id="7321"></span><div id="comment-7321" class="comment not_top_scorer"><div id="post-7321-score" class="comment-score"></div><div class="comment-text"><p>Zachad,</p><p>It's the problem of IE. It's ok when I use the Firefox. The capture has been uploaded and the file name is Mitisubishi and Juggernaut Wireshark 10-6-2011. Thanks.</p><p>Jimmy</p></div><div id="comment-7321-info" class="comment-info"><span class="comment-age">(08 Nov '11, 23:33)</span> Jimmy</div></div></div><div id="comment-tools-7234" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-7234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7319"></span>

<div id="answer-container-7319" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7319-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess that's not about wireshark but about your client bugs, but still have you checked the 'relative sequence numbers' option in TCP protocol settings?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p>ShomeaX<br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div></div><div id="comments-container-7319" class="comments-container"><span id="7352"></span><div id="comment-7352" class="comment"><div id="post-7352-score" class="comment-score"></div><div class="comment-text"><p>http://cloudshark.org/captures/da0e06834b57 So, is this post just for the bugs of Wireshark? Thanks.</p><p>Jimmy</p></div><div id="comment-7352-info" class="comment-info"><span class="comment-age">(09 Nov '11, 19:58)</span> Jimmy</div></div><span id="7357"></span><div id="comment-7357" class="comment"><div id="post-7357-score" class="comment-score"></div><div class="comment-text"><p>of course no, sorry.</p></div><div id="comment-7357-info" class="comment-info"><span class="comment-age">(09 Nov '11, 23:36)</span> ShomeaX</div></div></div><div id="comment-tools-7319" class="comment-tools"></div><div class="clear"></div><div id="comment-7319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7355"></span>

<div id="answer-container-7355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7355-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>looks to me that both server and client do send data immediately upon connection.</p><p>that is server spits '00vP1x0d' string (#8) BEFORE it sends the ACK (#9) to client's '00vPx0d' data (#7). client ACKs (#10) its data and respond with retransmission (#11) for out-of-order ACK he just saw (#9). of course, server ACKs retransmission with duplicate ACK (#12).</p><p>next, the same story continues with #14/#15 packet and so on.</p><p>everybody operate according to RFC, the client/server program should not see any duplicate data. the only drawback is that bandwidth is used not effectively. what exactly your question is?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 23:36</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p>ShomeaX<br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div></div><div id="comments-container-7355" class="comments-container"><span id="7359"></span><div id="comment-7359" class="comment"><div id="post-7359-score" class="comment-score"></div><div class="comment-text"><p>The problem is happened in Packet #9 because this scenario will be produced in every packet sent from the client. The first time ACK is always not correct in sequence number.</p><p>Jimmy</p></div><div id="comment-7359-info" class="comment-info"><span class="comment-age">(09 Nov '11, 23:49)</span> Jimmy</div></div><span id="7360"></span><div id="comment-7360" class="comment"><div id="post-7360-score" class="comment-score"></div><div class="comment-text"><p>at application level, e.g. sockets, this should not be a problem, both duplicate ACK and retransmitted packet must be silently ignored. are you writting/debugging kernel mode driver? what is your operation system, programming language, used networking libraries - provide more info.</p></div><div id="comment-7360-info" class="comment-info"><span class="comment-age">(10 Nov '11, 01:02)</span> ShomeaX</div></div></div><div id="comment-tools-7355" class="comment-tools"></div><div class="clear"></div><div id="comment-7355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

