+++
type = "question"
title = "Setup network card for wireshark"
description = '''I have two network card installed in my PC, one network card is connected to cooperation LAN, another is connected to my development system for sniffer the Ethernet data, anyone knows how to configure this card?'''
date = "2013-10-23T16:07:00Z"
lastmod = "2013-10-28T15:47:00Z"
weight = 26340
keywords = [ "network" ]
aliases = [ "/questions/26340" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Setup network card for wireshark](/questions/26340/setup-network-card-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26340-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two network card installed in my PC, one network card is connected to cooperation LAN, another is connected to my development system for sniffer the Ethernet data, anyone knows how to configure this card?</p></div><div id="question-tags" class="tags-container tags">network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/abbbd4f0eed2d71176528e800dd17d14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabbit&#39;s gravatar image" /><p>rabbit<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabbit has no accepted answers">0%</span></p></div></div><div id="comments-container-26340" class="comments-container"></div><div id="comment-tools-26340" class="comment-tools"></div><div class="clear"></div><div id="comment-26340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26348"></span>

<div id="answer-container-26348" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26348-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Normally, no special configuration is necessary to be able to capture, but it would be wise to disable all protocols on the card. So if you're running windows you should remove all protocol bindings by removing all checkmarks in the card properties. On Linux, you might configure your card as manual instead of static or dhcp.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26348" class="comments-container"></div><div id="comment-tools-26348" class="comment-tools"></div><div class="clear"></div><div id="comment-26348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26493"></span>

<div id="answer-container-26493" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26493-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi: I find the right answer, setup as the second card a "transparent bridge", then all the packet goes to my PC, wireshark can capture all those data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/abbbd4f0eed2d71176528e800dd17d14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabbit&#39;s gravatar image" /><p>rabbit<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabbit has no accepted answers">0%</span></p></div></div><div id="comments-container-26493" class="comments-container"></div><div id="comment-tools-26493" class="comment-tools"></div><div class="clear"></div><div id="comment-26493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

