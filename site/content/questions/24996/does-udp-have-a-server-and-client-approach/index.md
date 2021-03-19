+++
type = "question"
title = "does udp have a  server and client approach"
description = '''can any one tell me if there is a concept of server and client in udp as it is in tcp?? I have an option like,, as a syn packet needs to be first sent in tcp communication,,there is a server (listener who waits for syn packet) and client(who sends syn packet).but as this is not the case in udp,, the...'''
date = "2013-09-20T04:08:00Z"
lastmod = "2013-09-20T04:16:00Z"
weight = 24996
keywords = [ "udp", "tcp" ]
aliases = [ "/questions/24996" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [does udp have a server and client approach](/questions/24996/does-udp-have-a-server-and-client-approach)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24996-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can any one tell me if there is a concept of server and client in udp as it is in tcp??</p><p>I have an option like,, as a syn packet needs to be first sent in tcp communication,,there is a server (listener who waits for syn packet) and client(who sends syn packet).but as this is not the case in udp,, there is no client and server..</p><p>am i right??</p></div><div id="question-tags" class="tags-container tags">udp tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/14ae6741f009eb9551c897744110e25f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raja%20Balaji&#39;s gravatar image" /><p>Raja Balaji<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raja Balaji has no accepted answers">0%</span></p></div></div><div id="comments-container-24996" class="comments-container"></div><div id="comment-tools-24996" class="comment-tools"></div><div class="clear"></div><div id="comment-24996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25000"></span>

<div id="answer-container-25000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25000-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, UDP uses clients and server just the same (example: DNS servers).</p><p>UDP is stateless, though, which means there is no session setup/handshake like with TCP. You can still implement client/server communication in a similar way, by putting the session handling in a protocol on top of UDP. TFTP does something like this by numbering its datagrams with a sequence number that is "acknowledged".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25000" class="comments-container"><span id="25002"></span><div id="comment-25002" class="comment"><div id="post-25002-score" class="comment-score"></div><div class="comment-text"><p>If I don't implement any thing on the top of udp as you told, there is no client and server..whoever wants to send data can send it at any time.. is that right??</p></div><div id="comment-25002-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:26)</span> Raja Balaji</div></div><span id="25010"></span><div id="comment-25010" class="comment"><div id="post-25010-score" class="comment-score">1</div><div class="comment-text"><p>yes, anyone can send data at any time. Still you often have client/server concepts - the system offering services (like DNS) is a server, the system using that service is a client.</p><p>You do not need to have a state-aware connection to have a client/server construct. It's just a question of who is requesting information, and who is waiting for someone else to do the request.</p></div><div id="comment-25010-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:44)</span> Jasper ♦♦</div></div></div><div id="comment-tools-25000" class="comment-tools"></div><div class="clear"></div><div id="comment-25000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

