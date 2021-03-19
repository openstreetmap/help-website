+++
type = "question"
title = "Duplicate Acks and Fast Retransmissions"
description = '''How when analyzing a wireshark capture can it be determined that duplicate ACKs are a result of loss or missing packets versus delay ?'''
date = "2013-07-02T06:04:00Z"
lastmod = "2013-07-02T07:25:00Z"
weight = 22554
keywords = [ "analysis" ]
aliases = [ "/questions/22554" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate Acks and Fast Retransmissions](/questions/22554/duplicate-acks-and-fast-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22554-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How when analyzing a wireshark capture can it be determined that duplicate ACKs are a result of loss or missing packets versus delay ?</p></div><div id="question-tags" class="tags-container tags">analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/4b2756286190a5e2ffa23ca75688e4b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="George%20Ciampo&#39;s gravatar image" /><p>George Ciampo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="George Ciampo has no accepted answers">0%</span></p></div></div><div id="comments-container-22554" class="comments-container"></div><div id="comment-tools-22554" class="comment-tools"></div><div class="clear"></div><div id="comment-22554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22556"></span>

<div id="answer-container-22556" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22556-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually by looking at the time it took for the packet that was requested by Duplicate ACK to finally arrive. You need to consider the round trip time and ask yourself "could the sender have known that the packet was lost when it was sent"? E.g. if you see a packet coming in as a "retransmission" within 3 ms after the receiver started dup acking for it and the RTT is 100ms you can be pretty sure that it is just an out out order arrival and thus the duplicate acks a result of delay.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22556" class="comments-container"></div><div id="comment-tools-22556" class="comment-tools"></div><div class="clear"></div><div id="comment-22556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

