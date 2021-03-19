+++
type = "question"
title = "TLS and RC4"
description = '''Good afternoon, I need to filter from the capture that I have made only the IPs that use TLS and RC4 as an algorithm. When I want to filter through Cipher Suite it brings me as a result IPs that have many more algorithms and what I need to know is specifically where the connection was established. T...'''
date = "2017-10-26T11:08:00Z"
lastmod = "2017-10-26T12:31:00Z"
weight = 64247
keywords = [ "tls", "rc4" ]
aliases = [ "/questions/64247" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLS and RC4](/questions/64247/tls-and-rc4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good afternoon, I need to filter from the capture that I have made only the IPs that use TLS and RC4 as an algorithm. When I want to filter through Cipher Suite it brings me as a result IPs that have many more algorithms and what I need to know is specifically where the connection was established.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">tls rc4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '17, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/c99cd1600a2a3e23c758c5d74e4e0eb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lsalazar&#39;s gravatar image" /><p>lsalazar<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lsalazar has no accepted answers">0%</span></p></div></div><div id="comments-container-64247" class="comments-container"></div><div id="comment-tools-64247" class="comment-tools"></div><div class="clear"></div><div id="comment-64247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64251"></span>

<div id="answer-container-64251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64251-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Others may have something better; you could use the following display filter:</p><p><strong>ssl.handshake.version &gt;= 0x301 and ssl contains "rc4"</strong></p><p>Value 0x301 and above covers TLS 1.0 - 1.3</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/9591804f3aac21bac1d826cac0cd1109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Papa%20Packet&#39;s gravatar image" /><p>Papa Packet<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Papa Packet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '17, 12:33</p></div></div><div id="comments-container-64251" class="comments-container"><span id="64332"></span><div id="comment-64332" class="comment"><div id="post-64332-score" class="comment-score"></div><div class="comment-text"><p>HI thnks! but I can not filter what are the connections that were really established with the server and the reason for those that did not :-(</p></div><div id="comment-64332-info" class="comment-info"><span class="comment-age">(30 Oct '17, 07:45)</span> lsalazar</div></div><span id="64333"></span><div id="comment-64333" class="comment"><div id="post-64333-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-64333-info" class="comment-info"><span class="comment-age">(30 Oct '17, 23:17)</span> Jaap ♦</div></div></div><div id="comment-tools-64251" class="comment-tools"></div><div class="clear"></div><div id="comment-64251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

