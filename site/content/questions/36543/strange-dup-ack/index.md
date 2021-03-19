+++
type = "question"
title = "Strange dup ack"
description = '''Can someone explain the dup ack at packet no. 13? Thank you in advance '''
date = "2014-09-23T12:52:00Z"
lastmod = "2014-09-26T08:50:00Z"
weight = 36543
keywords = [ "ack", "dupack", "duplicatedack" ]
aliases = [ "/questions/36543" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange dup ack](/questions/36543/strange-dup-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone explain the dup ack at packet no. 13? Thank you in advance <img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-09-23_at_21.47.27.png" alt="Capture dup ack" /></p></div><div id="question-tags" class="tags-container tags">ack dupack duplicatedack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/e1f10dfea2a6a0469adb5ad9fefda1a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="becco981&#39;s gravatar image" /><p>becco981<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="becco981 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:07</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-36543" class="comments-container"></div><div id="comment-tools-36543" class="comment-tools"></div><div class="clear"></div><div id="comment-36543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36638"></span>

<div id="answer-container-36638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36638-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet #06 client sends 445 bytes<br />
Packet #07 server acks 445 bytes (immediate ack, application hasn't read the data yet)<br />
Packet #08 client sends 9 bytes (Nagle disabled at the client)<br />
Packet #09 is the server sending 506 bytes<br />
Packet #10 is the server sending a window_update (the appl now has read 445 bytes from #6)<br />
Packet #11 is the client acking packet #9 (ack# 507) (immediate ack<br />
Packet #12 is the server acking 9 bytes from packet 8, application hasn't read the data yet) Packet #13 is the second ack for packet # 9</p><p>So wireshark is right in telling you that frame 13 is a duplicate ack.<br />
Why the (Linux) client sends an immediate ack to an empty ack from the server I don't know. I think the scenario is caused by both TCP stacks sending immediate (not delaying) acknowledgements.</p><hr /><p>Modification:<br />
I would say the trace is showing how disabling Nagle and delayed_ACK might cause some unwanted packets to flow over the wire.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '14, 22:02</p></div></div><div id="comments-container-36638" class="comments-container"><span id="36652"></span><div id="comment-36652" class="comment"><div id="post-36652-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde,do you think that seq no. of packet #10 is right(seq 1),i think it should be 507 and then in packet#12 seq no. comes back to normal 507.</p></div><div id="comment-36652-info" class="comment-info"><span class="comment-age">(27 Sep '14, 07:02)</span> kishan pandey</div></div><span id="36672"></span><div id="comment-36672" class="comment"><div id="post-36672-score" class="comment-score"></div><div class="comment-text"><p>Well spotted, Kishan!<br />
</p><p>The seq# of packet 10 indicates that it was created earlier by TCP (between packet 7 and 8). All those packets are traced in a very short timeframe of less than 100 µs so when the capture point cuts them the outbound packets are out_of_order already.</p></div><div id="comment-36672-info" class="comment-info"><span class="comment-age">(28 Sep '14, 21:49)</span> mrEEde</div></div></div><div id="comment-tools-36638" class="comment-tools"></div><div class="clear"></div><div id="comment-36638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

