+++
type = "question"
title = "large packet problem"
description = '''We are having a issue with a client not being about to access a server. I don’t see a packet size large then 1518 going across the network, we think that may be the issue, we are seeing RST ACK and Retransmissions together I am not sure what that means, can anyone tell me what is retransmitting and ...'''
date = "2013-04-13T17:08:00Z"
lastmod = "2013-04-14T04:27:00Z"
weight = 20389
keywords = [ "mtu", "packet_size" ]
aliases = [ "/questions/20389" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [large packet problem](/questions/20389/large-packet-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having a issue with a client not being about to access a server. I don’t see a packet size large then 1518 going across the network, we think that may be the issue, we are seeing RST ACK and Retransmissions together I am not sure what that means, can anyone tell me what is retransmitting and why looking at the trace?</p><p><a href="https://www.cloudshark.org/captures/103e92950859">https://www.cloudshark.org/captures/103e92950859</a></p></div><div id="question-tags" class="tags-container tags">mtu packet_size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '13, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/b616f858ccbee3de56d053f1b002a757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ernest%20Johnson&#39;s gravatar image" /><p>Ernest Johnson<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ernest Johnson has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '13, 14:42</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20389" class="comments-container"></div><div id="comment-tools-20389" class="comment-tools"></div><div class="clear"></div><div id="comment-20389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20393"></span>

<div id="answer-container-20393" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20393-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The net MTU size along the route is only 1460 bytes as the client's SYN packet offers a 'reduced' MSS value of 1420 bytes. In the reverse direction the server's MSS value obviously doesn't get reduced and the client attempts to send a full packet but this doesn't arrive. Path MTU discovery seems to fail as the client finally retransmits with a tcp.len of 536 but this packet gets a reset from the server - probably coming in too late.</p><p>The solution to this is have the router/fw adjust the server's MSS value to 1420 as it flows to the client. You might want to reduce your mtu size to 1460 as a circumvention. BTW: Your largest outbound packets have an ip.len of 576 which is the default mtu size. Windows uses this when you disable PMTUD at the server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '13, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '13, 08:53</p></div></div><div id="comments-container-20393" class="comments-container"><span id="20402"></span><div id="comment-20402" class="comment"><div id="post-20402-score" class="comment-score"></div><div class="comment-text"><p>Thank You ver much</p></div><div id="comment-20402-info" class="comment-info"><span class="comment-age">(14 Apr '13, 21:41)</span> Ernest Johnson</div></div><span id="20408"></span><div id="comment-20408" class="comment"><div id="post-20408-score" class="comment-score">1</div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-20408-info" class="comment-info"><span class="comment-age">(15 Apr '13, 01:15)</span> Kurt Knochner ♦</div></div><span id="21278"></span><div id="comment-21278" class="comment"><div id="post-21278-score" class="comment-score"></div><div class="comment-text"><p>that was the problem, we remover the device that was changing the MSS the client end</p></div><div id="comment-21278-info" class="comment-info"><span class="comment-age">(19 May '13, 16:04)</span> Ernest Johnson</div></div></div><div id="comment-tools-20393" class="comment-tools"></div><div class="clear"></div><div id="comment-20393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

