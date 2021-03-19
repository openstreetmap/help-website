+++
type = "question"
title = "protocol hierarchy % packet for tcp"
description = '''I am looking at the Protocol Hierarchy for TCP in the Statistics&amp;gt;Protocol Hierarchy and it does not seem to add up as far as the % packets is concerned. I have TCP as 94.76%. But when I expand the selection for TCP, the protocols are around 0.03%, except 27.24% for SSL. I added up the protocols u...'''
date = "2015-02-07T12:48:00Z"
lastmod = "2015-02-07T14:33:00Z"
weight = 39696
keywords = [ "hierarchy", "protocol" ]
aliases = [ "/questions/39696" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [protocol hierarchy % packet for tcp](/questions/39696/protocol-hierarchy-packet-for-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at the Protocol Hierarchy for TCP in the Statistics&gt;Protocol Hierarchy and it does not seem to add up as far as the % packets is concerned. I have TCP as 94.76%. But when I expand the selection for TCP, the protocols are around 0.03%, except 27.24% for SSL. I added up the protocols under TCP and it did not add up to 94.76%. It is barely 30%. Am I missing something? Thanks</p></div><div id="question-tags" class="tags-container tags">hierarchy protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '15, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/b68ecd02e11309f135e5caf5e144f2a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaja&#39;s gravatar image" /><p>jaja<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaja has no accepted answers">0%</span></p></div></div><div id="comments-container-39696" class="comments-container"></div><div id="comment-tools-39696" class="comment-tools"></div><div class="clear"></div><div id="comment-39696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39697"></span>

<div id="answer-container-39697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39697-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, not really - it's just that the protocol hierarchy does not have an "other" row for the remaining percentage. Think of the missing rest of just that - data that Wireshark could not classify any further.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '15, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39697" class="comments-container"><span id="39698"></span><div id="comment-39698" class="comment"><div id="post-39698-score" class="comment-score"></div><div class="comment-text"><p>Ahh... That makes sense... Thx</p></div><div id="comment-39698-info" class="comment-info"><span class="comment-age">(07 Feb '15, 12:53)</span> jaja</div></div></div><div id="comment-tools-39697" class="comment-tools"></div><div class="clear"></div><div id="comment-39697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39700"></span>

<div id="answer-container-39700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39700-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A packet must have data in it for Wireshark to classify it with the higher-level protocol. If it does not have any data, then Wireshark considers it TCP only. Packets on port 80 with data in them are HTTP, but packets on port 80 with no data are listed as TCP, not HTTP. Using this rule, connection establishment packets, connection termination packets, and ACK packets with no data are just TCP and are not further classified in the Protocol Hierarchy. You can see this same behavior in the Protocol column of the main Wireshark display. Assuming you're looking at a trace in which data is flowing in one direction only, most of the "missing" packets under TCP are probably ACK packets</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '15, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-39700" class="comments-container"><span id="39701"></span><div id="comment-39701" class="comment"><div id="post-39701-score" class="comment-score"></div><div class="comment-text"><p>I learn new things everyday. Thank you very much.</p></div><div id="comment-39701-info" class="comment-info"><span class="comment-age">(07 Feb '15, 17:09)</span> jaja</div></div></div><div id="comment-tools-39700" class="comment-tools"></div><div class="clear"></div><div id="comment-39700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

