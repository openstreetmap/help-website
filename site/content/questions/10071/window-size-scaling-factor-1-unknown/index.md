+++
type = "question"
title = "[Window size scaling factor: -1 (unknown)]"
description = '''What does this mean in a summary of the trace file? [Window size scaling factor: -1 (unknown)] I captured it on a linux server with tcpdump and am reading the file on a Windows PC with Wireshark.'''
date = "2012-04-11T18:04:00Z"
lastmod = "2012-04-11T19:00:00Z"
weight = 10071
keywords = [ "scaling", "window", "factor", "size" ]
aliases = [ "/questions/10071" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Window size scaling factor: -1 (unknown)\]](/questions/10071/window-size-scaling-factor-1-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10071-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What does this mean in a summary of the trace file? [Window size scaling factor: -1 (unknown)]</p><p>I captured it on a linux server with tcpdump and am reading the file on a Windows PC with Wireshark.</p></div><div id="question-tags" class="tags-container tags">scaling window factor size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '12, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/dc5c328374605e90fc31dc6236ef5db2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="godfreydanials&#39;s gravatar image" /><p>godfreydanials<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="godfreydanials has no accepted answers">0%</span></p></div></div><div id="comments-container-10071" class="comments-container"></div><div id="comment-tools-10071" class="comment-tools"></div><div class="clear"></div><div id="comment-10071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10073"></span>

<div id="answer-container-10073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10073-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>It means that the trace file does not contain the TCP three-way handshake, so Wireshark does not know whether window scaling is in use, and if it is, what the window scaling factor is. If Wireshark sees the three-way handshake, and window scaling is used, Wireshark will know what window scaling factor is used by each side. Wireshark will then calculate the true window size for you by multiplying the value in the window size field by the appropriate multiplier.</p><p>If Wireshark does not see the three-way handshake, it will simply report the value of the window size field, which may or may not be the true window size, and indicate "[window size scaling factor -1 (unknown)]"</p><p>See <a href="http://www.ietf.org/rfc/rfc1323.txt.pdf">RFC 1323</a> for the specification of the TCP window scale option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '12, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '12, 19:16</p></div></div><div id="comments-container-10073" class="comments-container"></div><div id="comment-tools-10073" class="comment-tools"></div><div class="clear"></div><div id="comment-10073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

