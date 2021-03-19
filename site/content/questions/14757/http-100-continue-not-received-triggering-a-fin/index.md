+++
type = "question"
title = "HTTP 100 Continue not received triggering a FIN"
description = '''HI,  I am facing a very strange issue. After a successful TCP Handshake, client sends an HTTP Request. Server received it, and responded with a HTTP 100 Continue and right after with a HTPP 200 OK. But on the client, the Continue doesn&#x27;t arrive. Instead, only a TCP packet arrives acknowledging the f...'''
date = "2012-10-07T10:58:00Z"
lastmod = "2012-10-12T15:23:00Z"
weight = 14757
keywords = [ "fyn", "continue", "http" ]
aliases = [ "/questions/14757" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP 100 Continue not received triggering a FIN](/questions/14757/http-100-continue-not-received-triggering-a-fin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14757-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI, I am facing a very strange issue. After a successful TCP Handshake, client sends an HTTP Request. Server received it, and responded with a HTTP 100 Continue and right after with a HTPP 200 OK.</p><p>But on the client, the Continue doesn't arrive. Instead, only a TCP packet arrives acknowledging the fist HTTP request with the right SEQ,ACK. (The normal flow would be receiving the HTTP 100 with the right SEQ,ACK).</p><p>Client then waits for 1sec and sends a FYN, which is correctly negotiated with the server.</p><p>This cycle continues for 5 or so rounds, until finally the Continue arrives and the client gets the right info from the server.</p><p>I suspect something on the network (WAAS or FW) are tampering with the packets.</p><p>How can i troubleshoot?</p></div><div id="question-tags" class="tags-container tags">fyn continue http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '12, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/599929aa65406761d15533f022ed2d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctxsvc&#39;s gravatar image" /><p>ctxsvc<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctxsvc has one accepted answer">33%</span></p></div></div><div id="comments-container-14757" class="comments-container"></div><div id="comment-tools-14757" class="comment-tools"></div><div class="clear"></div><div id="comment-14757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="14974"></span>

<div id="answer-container-14974" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14974-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It was the Cisco WAAS, we disabled it and HTTP didnt fail.</p><p>we dont know what was the WAAS doing though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '12, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/599929aa65406761d15533f022ed2d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctxsvc&#39;s gravatar image" /><p>ctxsvc<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctxsvc has one accepted answer">33%</span></p></div></div><div id="comments-container-14974" class="comments-container"></div><div id="comment-tools-14974" class="comment-tools"></div><div class="clear"></div><div id="comment-14974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14759"></span>

<div id="answer-container-14759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14759-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ideally you would have to capture from the server and client side and compare traces</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '12, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p>thetechfirm<br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-14759" class="comments-container"><span id="14760"></span><div id="comment-14760" class="comment"><div id="post-14760-score" class="comment-score"></div><div class="comment-text"><p>HI thetechfirm,</p><p>thanks for the reply.</p><p>That is what i did, i compared the traces on the laptop and on the server. That is how i know HTTP responses are leaving the server but not reaching the client laptop.</p><p>My problem, i think, is that there are so many devices in the middle that i loose visibility.</p><p>I know that packets arrive to the server with a Public IP, and that could be a Cisco FW or ASA doing NATs and who knows what else.</p><p>brgrds</p></div><div id="comment-14760-info" class="comment-info"><span class="comment-age">(07 Oct '12, 12:08)</span> ctxsvc</div></div></div><div id="comment-tools-14759" class="comment-tools"></div><div class="clear"></div><div id="comment-14759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14761"></span>

<div id="answer-container-14761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14761-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to move your capture point along the path until you find the device that's dropping or modifying packets. Continue to capture at the server, but move your downstream capture point from the laptop towards the server one device at a time. As soon as you see that all the HTTP 100 Continue packets that leave the server are captured at the other capture point, you know that you've just moved upstream of the device that's dropping the packets.</p><p>When you think you've found the responsible device, confirm by capturing on each side of that device.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '12, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14761" class="comments-container"><span id="14762"></span><div id="comment-14762" class="comment"><div id="post-14762-score" class="comment-score"></div><div class="comment-text"><p>HI Jim,</p><p>totally agree. I will start placing laptops closer to the server.</p><p>From your experience, what is a good way to set this up in an enterprise cisco environent? Putting a PC running wireshark connected to the destination port of a SPAN session configured on a switch or its variants ( RSPAN and ERSPAN)?</p><p>Any other good tool? I heard Riverbed has a TurboPCAP network card on some software too.</p><p>brgrds</p></div><div id="comment-14762-info" class="comment-info"><span class="comment-age">(07 Oct '12, 13:42)</span> ctxsvc</div></div><span id="14763"></span><div id="comment-14763" class="comment"><div id="post-14763-score" class="comment-score"></div><div class="comment-text"><p>I agree with Jim.</p></div><div id="comment-14763-info" class="comment-info"><span class="comment-age">(07 Oct '12, 13:49)</span> thetechfirm</div></div></div><div id="comment-tools-14761" class="comment-tools"></div><div class="clear"></div><div id="comment-14761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

