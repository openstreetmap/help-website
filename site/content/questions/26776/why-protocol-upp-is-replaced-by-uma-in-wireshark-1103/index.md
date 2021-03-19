+++
type = "question"
title = "Why Protocol UPP is replaced by UMA in wireshark 1.10.3"
description = '''hi team I have installed wireshark 1.10.3 and am not getting UPP ptotocol here. While analyzing logs, i found that all logs for upp are presented here but the protocol is showing &quot;UMA&quot;. Please find the error if it there and also confirm to me. Thanks manish'''
date = "2013-11-08T06:32:00Z"
lastmod = "2013-11-08T10:25:00Z"
weight = 26776
keywords = [ "about_wireshark" ]
aliases = [ "/questions/26776" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Protocol UPP is replaced by UMA in wireshark 1.10.3](/questions/26776/why-protocol-upp-is-replaced-by-uma-in-wireshark-1103)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26776-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi team</p><p>I have installed wireshark 1.10.3 and am not getting UPP ptotocol here. While analyzing logs, i found that all logs for upp are presented here but the protocol is showing "UMA".</p><p>Please find the error if it there and also confirm to me.</p><p>Thanks manish</p></div><div id="question-tags" class="tags-container tags">about_wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '13, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/3fe4a03295800ce5f5b9d962fa5d1766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metalica%20Loopie3&#39;s gravatar image" /><p>Metalica Loo...<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metalica Loopie3 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '14, 07:29</p></div></div><div id="comments-container-26776" class="comments-container"><span id="26789"></span><div id="comment-26789" class="comment"><div id="post-26789-score" class="comment-score"></div><div class="comment-text"><p>just for the records: What is the UPP protocol?</p></div><div id="comment-26789-info" class="comment-info"><span class="comment-age">(08 Nov '13, 15:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26776" class="comment-tools"></div><div class="clear"></div><div id="comment-26776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26781"></span>

<div id="answer-container-26781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26781-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, UMA dissector registers itself to port 14401. You can change this in Edit -&gt; Preferences -&gt; Protocols -&gt; UMA -&gt; UMA TCP ports. You can also deactivate the UMA dissector with Analyze -&gt; Enabled Protocols.</p><p>Wireshark does not provide a UPP dissector though, unless you have a custom version / plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '13, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-26781" class="comments-container"></div><div id="comment-tools-26781" class="comment-tools"></div><div class="clear"></div><div id="comment-26781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

