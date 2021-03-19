+++
type = "question"
title = "Offset range display filter"
description = '''Can I write a display filter that will look at offset &quot;X&quot; for a range of values (i.e from a000 to a800). '''
date = "2014-06-25T07:27:00Z"
lastmod = "2014-06-25T14:30:00Z"
weight = 34168
keywords = [ "fcoevmwaretestpacket" ]
aliases = [ "/questions/34168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Offset range display filter](/questions/34168/offset-range-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I write a display filter that will look at offset "X" for a range of values (i.e from a000 to a800).</p></div><div id="question-tags" class="tags-container tags">fcoevmwaretestpacket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/b63c38ee9d71dfd2108fd14cc477f628?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcove&#39;s gravatar image" /><p>pcove<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcove has no accepted answers">0%</span></p></div></div><div id="comments-container-34168" class="comments-container"></div><div id="comment-tools-34168" class="comment-tools"></div><div class="clear"></div><div id="comment-34168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34193"></span>

<div id="answer-container-34193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34193-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This filter would display packets within your range at offset 0 in the data portion</p><pre><code>data[0:2] ge a0:00 and data[0:2] le  a8:00</code></pre><p>Hope this helps</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-34193" class="comments-container"></div><div id="comment-tools-34193" class="comment-tools"></div><div class="clear"></div><div id="comment-34193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

