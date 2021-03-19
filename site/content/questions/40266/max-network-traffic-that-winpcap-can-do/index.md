+++
type = "question"
title = "Max network traffic that WinPcap can do"
description = '''I want to know  what the max network traffic that Wireshark(WinPcap) can capture without packet losses ?'''
date = "2015-03-04T20:27:00Z"
lastmod = "2015-03-05T06:01:00Z"
weight = 40266
keywords = [ "traffic" ]
aliases = [ "/questions/40266" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Max network traffic that WinPcap can do](/questions/40266/max-network-traffic-that-winpcap-can-do)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40266-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know what the max network traffic that Wireshark(WinPcap) can capture without packet losses ?</p></div><div id="question-tags" class="tags-container tags">traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '15, 20:27</strong></p><img src="https://secure.gravatar.com/avatar/2cb33c69b9adc4985e5bcd9bd1b7892e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msphone&#39;s gravatar image" /><p>msphone<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msphone has no accepted answers">0%</span></p></div></div><div id="comments-container-40266" class="comments-container"></div><div id="comment-tools-40266" class="comment-tools"></div><div class="clear"></div><div id="comment-40266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40284"></span>

<div id="answer-container-40284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40284-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As fast as the platform will let you. This depends on how fast the network hardware can receive packets (its line speed), then how fast the network driver can push them into the network stack, then how fast the network stack can get copies to the capture interface, then how fast winpcap can process these (are there filters to be applied?), then how fast the file system can flush the writes out to storage. And all this software may be running on the same OS, maybe sharing a core and memory.</p><p>As you can see, there's no theoretical limit (maybe there is one in the API's used, I don't know), only a practical one, and its multi faceted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40284" class="comments-container"><span id="40371"></span><div id="comment-40371" class="comment"><div id="post-40371-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot</p></div><div id="comment-40371-info" class="comment-info"><span class="comment-age">(08 Mar '15, 17:13)</span> msphone</div></div><span id="40378"></span><div id="comment-40378" class="comment"><div id="post-40378-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40378-info" class="comment-info"><span class="comment-age">(09 Mar '15, 03:05)</span> grahamb ♦</div></div></div><div id="comment-tools-40284" class="comment-tools"></div><div class="clear"></div><div id="comment-40284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

