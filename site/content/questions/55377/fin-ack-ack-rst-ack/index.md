+++
type = "question"
title = "[FIN, ACK] -&gt; [ACK] -&gt; [RST, ACK]"
description = ''' Server is 172..50 and client is 130...5. Clients gets 10060 &quot;A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.&quot; From wireshark trace, I see 8 packets of [FIN, ACK] t...'''
date = "2016-09-07T09:57:00Z"
lastmod = "2016-09-07T10:10:00Z"
weight = 55377
keywords = [ "tcp" ]
aliases = [ "/questions/55377" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[FIN, ACK\] -&gt; \[ACK\] -&gt; \[RST, ACK\]](/questions/55377/fin-ack-ack-rst-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55377-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-09-07_12-52-08_q8pa9Xi.png" alt="alt text" /></p><p>Server is 172<em>.</em>.50 and client is 130.<em>.</em>.5. Clients gets 10060 "A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond." From wireshark trace, I see 8 packets of [FIN, ACK] then [ACK] then again [RST, ACK]. What does this mean? The same pattern is observed on client side. Thank you for your help!</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '16, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/0d87e0c4dc7c1c82959c6335ffe10843?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gyuunyuu&#39;s gravatar image" /><p>gyuunyuu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gyuunyuu has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 07 Sep '16, 10:00</p></div></div><div id="comments-container-55377" class="comments-container"></div><div id="comment-tools-55377" class="comment-tools"></div><div class="clear"></div><div id="comment-55377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55378"></span>

<div id="answer-container-55378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55378-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your TCP connection is shutdown. The reason why is in the application, your network traffic nor Wireshark will tell you that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '16, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55378" class="comments-container"><span id="55379"></span><div id="comment-55379" class="comment"><div id="post-55379-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, Thanks for the reply. Are you saying it's normal to have [RST, ACK] for every FIN packet?</p></div><div id="comment-55379-info" class="comment-info"><span class="comment-age">(07 Sep '16, 10:51)</span> gyuunyuu</div></div></div><div id="comment-tools-55378" class="comment-tools"></div><div class="clear"></div><div id="comment-55378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

