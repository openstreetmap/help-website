+++
type = "question"
title = "Can&#x27;t access private_data"
description = '''I need to read the packet sequence somehow (or otherwise identify retransmissions) from my dissect_foo, but I can&#x27;t read data from private_data. According to packet-tcp.h, private_data is in pinfo and can be accessed for information about the packet. Unfortunately the value of private_data is NULL s...'''
date = "2015-01-19T10:48:00Z"
lastmod = "2015-01-19T12:59:00Z"
weight = 39291
keywords = [ "dissector", "retransmissions", "tcp", "sequence" ]
aliases = [ "/questions/39291" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't access private\_data](/questions/39291/cant-access-private_data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39291-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to read the packet sequence somehow (or otherwise identify retransmissions) from my dissect_foo, but I can't read data from private_data. According to packet-tcp.h, private_data is in pinfo and can be accessed for information about the packet. Unfortunately the value of private_data is NULL so I can't do anything with it. Other than modifying packet-tcp itself, is there any way that I can identify whether a packet is a retransmission?</p></div><div id="question-tags" class="tags-container tags">dissector retransmissions tcp sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '15, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/ca562b18c08fc77caf70657719e1629f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicole_identity&#39;s gravatar image" /><p>nicole_identity<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicole_identity has no accepted answers">0%</span></p></div></div><div id="comments-container-39291" class="comments-container"></div><div id="comment-tools-39291" class="comment-tools"></div><div class="clear"></div><div id="comment-39291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39298"></span>

<div id="answer-container-39298" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39298-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The tcp_analysis structure can be retrieved thanks to the get_tcp_conversation_data() function. The flags can then be retrieved by doing a lookup on the acked_table (see tcp_analyze_get_acked_struct() function in packet-tcp.c for details).</p><p>If you want to have access to the tcpinfo struct, then the method differs depending on the version you use: pinfo-&gt;private_data is no more used in master branch (1.99.X version). Instead the structure is given in the data parameter of your dissector (you must register your dissector as new_dissector_t to have access to it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '15, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39298" class="comments-container"></div><div id="comment-tools-39298" class="comment-tools"></div><div class="clear"></div><div id="comment-39298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

