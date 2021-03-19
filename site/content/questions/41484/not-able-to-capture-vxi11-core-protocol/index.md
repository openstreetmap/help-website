+++
type = "question"
title = "not able to capture VXI11 core protocol"
description = '''I facing problem capturing vxi11 core protocol. Me and my partner(both using wireshark v1.8.7). We are capturing the same instrument using p2p.  unfortunately only my partner able to capture vxi11 core while i getting STUN.  tried with different version of wireshark. Same issue. Please advice. Thank...'''
date = "2015-04-16T02:56:00Z"
lastmod = "2015-04-16T04:18:00Z"
weight = 41484
keywords = [ "vxi11", "protocol" ]
aliases = [ "/questions/41484" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [not able to capture VXI11 core protocol](/questions/41484/not-able-to-capture-vxi11-core-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41484-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I facing problem capturing vxi11 core protocol. Me and my partner(both using wireshark v1.8.7). We are capturing the same instrument using p2p. unfortunately only my partner able to capture vxi11 core while i getting STUN. tried with different version of wireshark. Same issue. Please advice. Thanks.</p></div><div id="question-tags" class="tags-container tags">vxi11 protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '15, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/41ec1fe3cc869d62d1fe6db012cb92b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrischiang&#39;s gravatar image" /><p>chrischiang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrischiang has no accepted answers">0%</span></p></div></div><div id="comments-container-41484" class="comments-container"></div><div id="comment-tools-41484" class="comment-tools"></div><div class="clear"></div><div id="comment-41484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41486"></span>

<div id="answer-container-41486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41486-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's probably a difference in TCP dissector preferences. Go look at the setting 'Try heuristic sub-dissectors first'. I think it should be checked in your case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '15, 05:31</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41486" class="comments-container"><span id="41516"></span><div id="comment-41516" class="comment"><div id="post-41516-score" class="comment-score"></div><div class="comment-text"><p>I just check on my setting. both me and my partner unchecked on "try heuristic sub-dissectors first" . we have the same setting in TCP and RPC preferences.</p></div><div id="comment-41516-info" class="comment-info"><span class="comment-age">(16 Apr '15, 18:41)</span> chrischiang</div></div></div><div id="comment-tools-41486" class="comment-tools"></div><div class="clear"></div><div id="comment-41486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

