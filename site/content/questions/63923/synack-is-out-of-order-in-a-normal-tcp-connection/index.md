+++
type = "question"
title = "[SYN,ACK] is out of order in a normal TCP connection"
description = '''Hi, I have captured TCP packet handshake in my nodes, the TCP handshake look very strange, I called A is the sender and B is the receiver A-&amp;gt;B SYN B-&amp;gt;A SYN,ACK A-&amp;gt;B ACK  then it&#x27;s strange that A continues send a duplicated ACK, then B sends to A an TCP out of order of packet [SYN,ACK] A-&amp;gt...'''
date = "2017-10-16T03:06:00Z"
lastmod = "2017-10-16T03:48:00Z"
weight = 63923
keywords = [ "packet" ]
aliases = [ "/questions/63923" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [\[SYN,ACK\] is out of order in a normal TCP connection](/questions/63923/synack-is-out-of-order-in-a-normal-tcp-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have captured TCP packet handshake in my nodes, the TCP handshake look very strange, I called A is the sender and B is the receiver</p><pre><code>A-&gt;B  SYN
B-&gt;A  SYN,ACK
A-&gt;B  ACK</code></pre><p>then it's strange that A continues send a duplicated ACK, then B sends to A an TCP out of order of packet [SYN,ACK]</p><pre><code>A-&gt;B TCP DUP ACK #1
B-&gt;A TCP Out-of-order [SYN,ACK]
A-&gt;B TCP DUP ACK #2
A-&gt;B TCP DUP ACK #3</code></pre><p>Could you please let me know how [SYN,ACK] can be out-of-order and why A sends TCP dup ACK 3 times in this case?</p><p>Thanks a lot, Brs Naruto</p></div><div id="question-tags" class="tags-container tags">packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '17, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/64fdf481625cbc639e6456d8716f5509?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naruto&#39;s gravatar image" /><p>naruto<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naruto has no accepted answers">0%</span></p></div></div><div id="comments-container-63923" class="comments-container"></div><div id="comment-tools-63923" class="comment-tools"></div><div class="clear"></div><div id="comment-63923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63927"></span>

<div id="answer-container-63927" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63927-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd say you have problems with the ACKs from A not getting through to B. I guess the picture at node B looks like this:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Packetloss_z0odmsF.png" alt="alt text" /></p><p>You should capture at B to verify if packets are lost.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '17, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '17, 06:07</p></div></div><div id="comments-container-63927" class="comments-container"><span id="63930"></span><div id="comment-63930" class="comment"><div id="post-63930-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for your feedback but in my case the TCP DUP ACK is of the last ACK frame of handshake step. I mean it is the duplicate of the last ACK send from A, not the ACK in [SYN,ACK]</p></div><div id="comment-63930-info" class="comment-info"><span class="comment-age">(16 Oct '17, 04:21)</span> naruto</div></div><span id="63931"></span><div id="comment-63931" class="comment"><div id="post-63931-score" class="comment-score"></div><div class="comment-text"><p>of course. The handshake ACK from A never arrives at B, which it why it retransmits SYN/ACK. I updated my answer with a drawing.</p></div><div id="comment-63931-info" class="comment-info"><span class="comment-age">(16 Oct '17, 05:55)</span> Jasper ♦♦</div></div></div><div id="comment-tools-63927" class="comment-tools"></div><div class="clear"></div><div id="comment-63927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

