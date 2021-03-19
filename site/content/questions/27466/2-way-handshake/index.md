+++
type = "question"
title = "2-way handshake"
description = '''While looking at packet captured from netscalar device found a strange 2 way handshake where first packet was syn followed by syn-ack but third packet was ack with psh bit set and had data in it.Can anyone explain this?'''
date = "2013-11-26T23:05:00Z"
lastmod = "2013-11-28T20:10:00Z"
weight = 27466
keywords = [ "tcp" ]
aliases = [ "/questions/27466" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [2-way handshake](/questions/27466/2-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While looking at packet captured from netscalar device found a strange 2 way handshake where first packet was syn followed by syn-ack but third packet was ack with psh bit set and had data in it.Can anyone explain this?</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-27466" class="comments-container"></div><div id="comment-tools-27466" class="comment-tools"></div><div class="clear"></div><div id="comment-27466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27469"></span>

<div id="answer-container-27469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27469-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is allowed for TCP. Depends on the specific application implementation, the 3rd packet is allowed to carry application level data. Although this kind of cases are not much, but it was not uncommon in recent days.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-27469" class="comments-container"></div><div id="comment-tools-27469" class="comment-tools"></div><div class="clear"></div><div id="comment-27469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27545"></span>

<div id="answer-container-27545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27545-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is actually very common these days. It is still a 3 way handshake (ACK, PSH) but the application is also sending data as pointed out by @Zhoucengchao.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '13, 20:10</strong></p><img src="https://secure.gravatar.com/avatar/734cba29e4f3c280ebbfe8a61246bc3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ken15&#39;s gravatar image" /><p>Ken15<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ken15 has no accepted answers">0%</span></p></div></div><div id="comments-container-27545" class="comments-container"></div><div id="comment-tools-27545" class="comment-tools"></div><div class="clear"></div><div id="comment-27545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

