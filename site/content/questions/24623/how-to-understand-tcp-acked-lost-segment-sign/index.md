+++
type = "question"
title = "How to understand &quot;TCP ACKed lost segment&quot; sign"
description = '''I did a iperf testing between two virtual machines on the same hardware computer. There are lot of &quot;TCP ACKed lost segment&quot; segment displayed. What does this message mean? For example, host A &amp;amp; B  A send sequence 1000 (1byte) to B B acked 1001 with &quot;TCP ACKed lost segment&quot; sign  Does it mean tha...'''
date = "2013-09-13T00:08:00Z"
lastmod = "2013-09-13T00:15:00Z"
weight = 24623
keywords = [ "lost_segment" ]
aliases = [ "/questions/24623" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to understand "TCP ACKed lost segment" sign](/questions/24623/how-to-understand-tcp-acked-lost-segment-sign)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24623-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I did a iperf testing between two virtual machines on the same hardware computer. There are lot of "TCP ACKed lost segment" segment displayed. What does this message mean? For example, host A &amp; B</p><ol><li>A send sequence 1000 (1byte) to B</li><li>B acked 1001 with "TCP ACKed lost segment" sign</li></ol><p>Does it mean that B actually do get the sequence byte 1000 from the perspective of TCP stack, but wireshark didn't capture sequence 1000 byte? But if wireshark didn't see the packet, how does it know that B's TCP stack has got the sequence 1000?</p></div><div id="question-tags" class="tags-container tags">lost_segment</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-24623" class="comments-container"></div><div id="comment-tools-24623" class="comment-tools"></div><div class="clear"></div><div id="comment-24623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24624"></span>

<div id="answer-container-24624" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24624-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, B got the packet with sequence 1000 and 1 byte, and sent an acknowledge number 1001. Wireshark did not see the packet with sequence 1000, but it saw the acknowlege of 1001. So it marks that acknowledge as "B confirmed it got sequence 1000 with 1 byte, but <strong>I</strong> didn't see that one".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24624" class="comments-container"><span id="24626"></span><div id="comment-24626" class="comment"><div id="post-24626-score" class="comment-score"></div><div class="comment-text"><p>thank you, Jasper for your confirmation. Do you know why we explicitly develop this expert sign to highlight such segments? What does this sign try to tell us, I mean the network analyst?</p></div><div id="comment-24626-info" class="comment-info"><span class="comment-age">(13 Sep '13, 01:43)</span> SteveZhou</div></div><span id="24629"></span><div id="comment-24629" class="comment"><div id="post-24629-score" class="comment-score"></div><div class="comment-text"><p>This message (or "sign" as you call it) is very helpful, because it tells you that the packet with sequence 1000 was not lost between client and server. The capture process was just not quick enough to record it into the trace. Without the message you might suspect packet loss between client and server, while there wasn't.</p></div><div id="comment-24629-info" class="comment-info"><span class="comment-age">(13 Sep '13, 02:18)</span> Jasper ♦♦</div></div><span id="24632"></span><div id="comment-24632" class="comment"><div id="post-24632-score" class="comment-score"></div><div class="comment-text"><p>I got you. thanks a lot!</p></div><div id="comment-24632-info" class="comment-info"><span class="comment-age">(13 Sep '13, 02:50)</span> SteveZhou</div></div></div><div id="comment-tools-24624" class="comment-tools"></div><div class="clear"></div><div id="comment-24624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

