+++
type = "question"
title = "Dual Wireshark processes"
description = '''Is it possible to use one laptop to capture two different sniffs from two different vlans and if so, what NICS and windows OS does Wireshark support for this? We need to capture two different segments from one router at the same time and only want to use one laptop to do this. Is it possible, or wil...'''
date = "2012-11-26T15:37:00Z"
lastmod = "2012-11-26T16:46:00Z"
weight = 16340
keywords = [ "multi-process", "dual" ]
aliases = [ "/questions/16340" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dual Wireshark processes](/questions/16340/dual-wireshark-processes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16340-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to use one laptop to capture two different sniffs from two different vlans and if so, what NICS and windows OS does Wireshark support for this? We need to capture two different segments from one router at the same time and only want to use one laptop to do this. Is it possible, or will we need four separate laptops?</p></div><div id="question-tags" class="tags-container tags">multi-process dual</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '12, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/78e9347fcef0e24c704d4176c71b3789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rudy&#39;s gravatar image" /><p>Rudy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rudy has no accepted answers">0%</span></p></div></div><div id="comments-container-16340" class="comments-container"></div><div id="comment-tools-16340" class="comment-tools"></div><div class="clear"></div><div id="comment-16340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16341"></span>

<div id="answer-container-16341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16341-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Basically your question comes down to wether or not you're able to get the relevant packets the NICs of the laptop. You can run multiple Wireshark (or better yet: dumpcap) processes on a single laptop, but you need to keep in mind that the data rate should not exceed the write speed of the disk, otherwise you'll lose packets.</p><p>So if you have one router, the question is if you can SPAN or TAP into the links and direct the frames to the laptop. If you can, (and the data rate is not too much for a single system) I see no problem. Maybe you could give a little schematic here which helps determining the point of capture so we can take a look at what you're trying to do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16341" class="comments-container"></div><div id="comment-tools-16341" class="comment-tools"></div><div class="clear"></div><div id="comment-16341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

