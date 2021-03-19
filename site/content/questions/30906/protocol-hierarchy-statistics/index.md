+++
type = "question"
title = "protocol hierarchy statistics"
description = '''I am looking at the protocol hierarchy statistics and with TCP, I see 84.83% of TCP packets. But when expand the TCP tree, the protocols under TCP (like Data, SSL, SSH protocol, etc...) do not add up to 84.83%. Can somebody help me understand this? Thanks'''
date = "2014-03-17T20:01:00Z"
lastmod = "2014-03-17T21:42:00Z"
weight = 30906
keywords = [ "statistics", "protocol", "port", "tcp", "network" ]
aliases = [ "/questions/30906" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [protocol hierarchy statistics](/questions/30906/protocol-hierarchy-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30906-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at the protocol hierarchy statistics and with TCP, I see 84.83% of TCP packets. But when expand the TCP tree, the protocols under TCP (like Data, SSL, SSH protocol, etc...) do not add up to 84.83%. Can somebody help me understand this? Thanks</p></div><div id="question-tags" class="tags-container tags">statistics protocol port tcp network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p>character9<br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div></div><div id="comments-container-30906" class="comments-container"></div><div id="comment-tools-30906" class="comment-tools"></div><div class="clear"></div><div id="comment-30906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30911"></span>

<div id="answer-container-30911" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30911-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The difference is due to TCP packets that have no data, known as "pure TCP" or sometimes "naked TCP." These would include the SYN and SYN/ACK packets, ACK packets with no data, and FIN or RESET packets.</p><p>For example, if a packet has no data, then Wireshark does not consider it to be HTTP even if it uses port 80 and even if it is part of an HTTP session. It is TCP only. This is how Wireshark treats all higher-level protocols that run on TCP.</p><p>To see these packets, apply a display filter of "tcp.len==0".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '14, 21:42</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-30911" class="comments-container"></div><div id="comment-tools-30911" class="comment-tools"></div><div class="clear"></div><div id="comment-30911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

