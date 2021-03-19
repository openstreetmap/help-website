+++
type = "question"
title = "Modbus/tcp"
description = '''Hello I have develop a electronic card (client) for connect to a commercial controler(server) in modbus TCP. Can you tell me why the server don&#x27;t answer, to modbus tcp, my ip is 192.164.0.34. Thanks http://cloudshark.org/captures/4b8f9f3579b3'''
date = "2014-01-16T05:45:00Z"
lastmod = "2014-01-16T08:19:00Z"
weight = 28962
keywords = [ "modbus", "tcp" ]
aliases = [ "/questions/28962" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Modbus/tcp](/questions/28962/modbustcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28962-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I have develop a electronic card (client) for connect to a commercial controler(server) in modbus TCP. Can you tell me why the server don't answer, to modbus tcp, my ip is 192.164.0.34. Thanks</p><p><a href="http://cloudshark.org/captures/4b8f9f3579b3">http://cloudshark.org/captures/4b8f9f3579b3</a></p></div><div id="question-tags" class="tags-container tags">modbus tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '14, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/c941c0897422ff40f521a923f4461f2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregoire&#39;s gravatar image" /><p>gregoire<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregoire has one accepted answer">100%</span></p></div></div><div id="comments-container-28962" class="comments-container"></div><div id="comment-tools-28962" class="comment-tools"></div><div class="clear"></div><div id="comment-28962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28964"></span>

<div id="answer-container-28964" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28964-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have found the problem, i have not the same source port between the 7 (SYN) and 8(modbus) frame , but wireshark have not detect the problem!</p><p>Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/c941c0897422ff40f521a923f4461f2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregoire&#39;s gravatar image" /><p>gregoire<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregoire has one accepted answer">100%</span></p></div></div><div id="comments-container-28964" class="comments-container"><span id="28966"></span><div id="comment-28966" class="comment"><div id="post-28966-score" class="comment-score"></div><div class="comment-text"><p>That's a very odd TCP client.</p><p>As Wireshark is a packet analyzer not a Modbus master\slave, it doesn't particularly care that the "conversation" isn't proceeding using the same TCP stream as it just dissects the data seen on the wire. In particular consider a capture made after the start of the initial part of the conversation, Wireshark should still be able to dissect the traffic it has seen. Note that this isn't true for all protocols.</p><p>You can set Wireshark to display the ports used as columns and that may have lead to you (and me) spotting this earlier.</p></div><div id="comment-28966-info" class="comment-info"><span class="comment-age">(16 Jan '14, 09:18)</span> grahamb ♦</div></div></div><div id="comment-tools-28964" class="comment-tools"></div><div class="clear"></div><div id="comment-28964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28963"></span>

<div id="answer-container-28963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There seems to be some sort of connection issue between the client and the server. The server never responds to the client Modbus\TCP messages, and a long time later sends dup ACKS to the client SYN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-28963" class="comments-container"></div><div id="comment-tools-28963" class="comment-tools"></div><div class="clear"></div><div id="comment-28963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

