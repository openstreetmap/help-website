+++
type = "question"
title = "How to check the MTU network in wireshark ??"
description = '''I have a question, when I use the ping with parametrs &quot;-f&quot; until find the MTU, the max size what I can ping, is 1472, but the size of the fragmenteds packages in Wireshark, is 1500, 1480 data and 20 header. What is the true MTU?'''
date = "2015-06-28T10:23:00Z"
lastmod = "2015-06-28T11:53:00Z"
weight = 43633
keywords = [ "mtu", "ping", "wireshark" ]
aliases = [ "/questions/43633" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to check the MTU network in wireshark ??](/questions/43633/how-to-check-the-mtu-network-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43633-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a question, when I use the ping with parametrs "-f" until find the MTU, the max size what I can ping, is 1472, but the size of the fragmenteds packages in Wireshark, is 1500, 1480 data and 20 header. What is the true MTU?</p></div><div id="question-tags" class="tags-container tags">mtu ping wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '15, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/8004a34f69cf59abf5dc3feb820e39df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Igor%20Ramos&#39;s gravatar image" /><p>Igor Ramos<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Igor Ramos has no accepted answers">0%</span></p></div></div><div id="comments-container-43633" class="comments-container"></div><div id="comment-tools-43633" class="comment-tools"></div><div class="clear"></div><div id="comment-43633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43635"></span>

<div id="answer-container-43635" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43635-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MTU size is 1500 and includes 20 bytes IP_header, 8 byte ICMP_header and 1472 bytes ICMP payload.</p><p>Regards Matthias</p><p>IP Header <img src="http://nmap.org/book/images/hdr/MJB-IP-Header-800x576.png" alt="alt text" /></p><p>ICMP Header <img src="http://nmap.org/book/images/hdr/MJB-ICMP-Header-800x392.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '15, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jun '15, 11:54</p></div></div><div id="comments-container-43635" class="comments-container"><span id="43637"></span><div id="comment-43637" class="comment"><div id="post-43637-score" class="comment-score"></div><div class="comment-text"><p>Thank you guy, you helped me a lot. Very good response !!!</p></div><div id="comment-43637-info" class="comment-info"><span class="comment-age">(28 Jun '15, 12:16)</span> Igor Ramos</div></div></div><div id="comment-tools-43635" class="comment-tools"></div><div class="clear"></div><div id="comment-43635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

