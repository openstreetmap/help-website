+++
type = "question"
title = "How do I exclude own traffic from wireshark when in promiscuous mode?"
description = '''How do I exclude own traffic from wireshark when in promiscuous mode?'''
date = "2012-07-10T04:58:00Z"
lastmod = "2012-07-10T05:35:00Z"
weight = 12553
keywords = [ "exclude" ]
aliases = [ "/questions/12553" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I exclude own traffic from wireshark when in promiscuous mode?](/questions/12553/how-do-i-exclude-own-traffic-from-wireshark-when-in-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12553-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I exclude own traffic from wireshark when in promiscuous mode?</p></div><div id="question-tags" class="tags-container tags">exclude</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '12, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/63c50004c4f6eaf3235b9ea836f4b6cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sorin&#39;s gravatar image" /><p>sorin<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sorin has no accepted answers">0%</span></p></div></div><div id="comments-container-12553" class="comments-container"></div><div id="comment-tools-12553" class="comment-tools"></div><div class="clear"></div><div id="comment-12553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12555"></span>

<div id="answer-container-12555" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12555-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Two options:</p><ol><li>You could use a filter to exclude anything with ether destination same as your MAC address. Determine the MAC address of your capture card, and set a capture filter: "not ether host xx:xx:xx:xx:xx:xx"</li><li>assuming you're running Windows: if you do not need to communicate on the capture card you could just remove all protocol bindings on the card settings. Open the network card properties and remove all checkmarks next to the various stuff that is shown there. I'm not sure how to do something similar on other OSes, but I guess if you're not configuring anything for a network card on Linux it will basically do the same.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '12, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12555" class="comments-container"><span id="12556"></span><div id="comment-12556" class="comment"><div id="post-12556-score" class="comment-score"></div><div class="comment-text"><p>Jasper, for linux (and other unixes as well), as you said. Alternatively the following for an already configured interface: <strong><code>ifconfig eth0 0.0.0.0</code></strong>. Replace eth0 with the name of your capturing interface.</p></div><div id="comment-12556-info" class="comment-info"><span class="comment-age">(10 Jul '12, 06:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12555" class="comment-tools"></div><div class="clear"></div><div id="comment-12555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

