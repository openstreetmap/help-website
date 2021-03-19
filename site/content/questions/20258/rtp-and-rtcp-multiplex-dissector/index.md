+++
type = "question"
title = "RTP and RTCP Multiplex dissector"
description = '''According to RFC 5761: &quot;Multiplexing RTP Data and Control Packets on a Single Port&quot;, RTP and RTCP packets are on the same ports.Can wireshark decode RTCP packets from the Multiplex packets?'''
date = "2013-04-09T19:40:00Z"
lastmod = "2013-04-10T05:57:00Z"
weight = 20258
keywords = [ "rtcp", "rtp", "multiplex" ]
aliases = [ "/questions/20258" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP and RTCP Multiplex dissector](/questions/20258/rtp-and-rtcp-multiplex-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20258-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to RFC 5761: "Multiplexing RTP Data and Control Packets on a Single Port", RTP and RTCP packets are on the same ports.Can wireshark decode RTCP packets from the Multiplex packets?</p></div><div id="question-tags" class="tags-container tags">rtcp rtp multiplex</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '13, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/077901f4416726db1f4638c70745bd72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="west&#39;s gravatar image" /><p>west<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="west has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '13, 04:10</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-20258" class="comments-container"></div><div id="comment-tools-20258" class="comment-tools"></div><div class="clear"></div><div id="comment-20258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20277"></span>

<div id="answer-container-20277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20277-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is already an enhancement bug to implement that functionality</p><blockquote><p><code>https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8355</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20277" class="comments-container"><span id="20326"></span><div id="comment-20326" class="comment"><div id="post-20326-score" class="comment-score"></div><div class="comment-text"><p>@west: can you add a sample capture file with multiplexed RTP/RTCP to the bug?</p></div><div id="comment-20326-info" class="comment-info"><span class="comment-age">(11 Apr '13, 04:10)</span> Jaap ♦</div></div></div><div id="comment-tools-20277" class="comment-tools"></div><div class="clear"></div><div id="comment-20277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

