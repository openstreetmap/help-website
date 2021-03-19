+++
type = "question"
title = "Discard/ignore data on capture"
description = '''Hello, When running a capture, how can I set up wireshark so that it does not save the data portion of a TCP packet? I am only interested in capturing the IP and TCP headers. Thanks! Scott'''
date = "2015-07-24T16:00:00Z"
lastmod = "2015-07-24T16:23:00Z"
weight = 44458
keywords = [ "ignore", "discard", "data", "tcp" ]
aliases = [ "/questions/44458" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Discard/ignore data on capture](/questions/44458/discardignore-data-on-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44458-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>When running a capture, how can I set up wireshark so that it does not save the data portion of a TCP packet? I am only interested in capturing the IP and TCP headers.</p><p>Thanks! Scott</p></div><div id="question-tags" class="tags-container tags">ignore discard data tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/fa8caa1775c52bd5d23f6ca90cb342fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goldscott&#39;s gravatar image" /><p>goldscott<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goldscott has no accepted answers">0%</span></p></div></div><div id="comments-container-44458" class="comments-container"></div><div id="comment-tools-44458" class="comment-tools"></div><div class="clear"></div><div id="comment-44458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44460"></span>

<div id="answer-container-44460" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44460-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Set the snaplen option for the interface in the capture options, <code>-s</code> on the command line see the Wiki <a href="https://wiki.wireshark.org/SnapLen">SnapLen</a> page for more info.</p><p>For just IP and TCP headers, assuming Ethernet and no IP or TCP options, then 68 bytes "should" be OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44460" class="comments-container"><span id="44461"></span><div id="comment-44461" class="comment"><div id="post-44461-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Graham, that's exactly what I needed!</p></div><div id="comment-44461-info" class="comment-info"><span class="comment-age">(24 Jul '15, 17:15)</span> goldscott</div></div><span id="44465"></span><div id="comment-44465" class="comment"><div id="post-44465-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44465-info" class="comment-info"><span class="comment-age">(25 Jul '15, 04:00)</span> grahamb ♦</div></div></div><div id="comment-tools-44460" class="comment-tools"></div><div class="clear"></div><div id="comment-44460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

