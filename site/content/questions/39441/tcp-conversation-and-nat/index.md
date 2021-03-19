+++
type = "question"
title = "TCP conversation and NAT"
description = '''I have what might seem a basic question but I really do not know or can find the answer. The question is; if I have a TCP connection from a server which is from a public IP (Client) to a Private IP (Server)which is through a NAT, is the TCP conversation from Client to Server? Or is it from Client to...'''
date = "2015-01-27T14:11:00Z"
lastmod = "2015-01-28T06:56:00Z"
weight = 39441
keywords = [ "tcp", "nat", "retransmissions" ]
aliases = [ "/questions/39441" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TCP conversation and NAT](/questions/39441/tcp-conversation-and-nat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have what might seem a basic question but I really do not know or can find the answer. The question is; if I have a TCP connection from a server which is from a public IP (Client) to a Private IP (Server)which is through a NAT, is the TCP conversation from Client to Server? Or is it from Client to NAT device, then NAT device to server?</p><p>The reason why I ask, if I see retransmissions on the client to NAT device should I also see it from NAT device to server? My thoughts are that the TCP conversation is end to end, from the client to server.</p><p>Thanks M</p></div><div id="question-tags" class="tags-container tags">tcp nat retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '15, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/dca0681ac6c9b452d89aa8e1a3d19e72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmarrun&#39;s gravatar image" /><p>gmarrun<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmarrun has no accepted answers">0%</span></p></div></div><div id="comments-container-39441" class="comments-container"></div><div id="comment-tools-39441" class="comment-tools"></div><div class="clear"></div><div id="comment-39441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39442"></span>

<div id="answer-container-39442" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39442-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP connections through NAT devices are end-to-end, which means that the client is talking to the server on layer 4. NAT translates IP addresses (layer 3), so they can change, but the TCP connection does not terminate at the NAT gateway. Proxy servers would do that kind of thing, but not NAT gateways.</p><p>And yes, you should see the same segments being retransmitted, but since the IP addresses are changed at least partially they can be hard to find.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '15, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39442" class="comments-container"><span id="39444"></span><div id="comment-39444" class="comment"><div id="post-39444-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response and explanation. Greatly Appreciated.</p></div><div id="comment-39444-info" class="comment-info"><span class="comment-age">(27 Jan '15, 14:37)</span> gmarrun</div></div></div><div id="comment-tools-39442" class="comment-tools"></div><div class="clear"></div><div id="comment-39442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39455"></span>

<div id="answer-container-39455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39455-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should also verify that only NAT is occurring and not PAT. Most routers perform PAT (Port address translation) in which the IP address and the TCP port numbers are modified when connecting from private to public IP addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '15, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-39455" class="comments-container"></div><div id="comment-tools-39455" class="comment-tools"></div><div class="clear"></div><div id="comment-39455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

