+++
type = "question"
title = "TCP analysis / interpertation - ACKs and lost segments"
description = '''Hi, I&#x27;m trying to perform TCP analysis, or at least learn how to do it, and I would really appreciate some information about the following filter fields. tcp.analysis.ack_lost_segment tcp.analysis.lost_segment tcp.analysis.duplicate_ack tcp.analysis.retransmission I&#x27;m not really sure about the first...'''
date = "2012-06-18T04:36:00Z"
lastmod = "2012-06-18T06:00:00Z"
weight = 12016
keywords = [ "ack", "analysis", "lost", "tcp" ]
aliases = [ "/questions/12016" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP analysis / interpertation - ACKs and lost segments](/questions/12016/tcp-analysis-interpertation-acks-and-lost-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to perform TCP analysis, or at least learn how to do it, and I would really appreciate some information about the following filter fields.</p><p>tcp.analysis.ack_lost_segment tcp.analysis.lost_segment tcp.analysis.duplicate_ack tcp.analysis.retransmission</p><p>I'm not really sure about the first two, since I've read in some places that they might be due to drops in Wireshark while capturing, and might not be a real issue of the TCP stream. This is somewhat confusing :(</p><p>Thank you in advance!</p></div><div id="question-tags" class="tags-container tags">ack analysis lost tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/cef428b430cb37a72ae6f9f439413973?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fashasha&#39;s gravatar image" /><p>fashasha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fashasha has no accepted answers">0%</span></p></div></div><div id="comments-container-12016" class="comments-container"></div><div id="comment-tools-12016" class="comment-tools"></div><div class="clear"></div><div id="comment-12016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12018"></span>

<div id="answer-container-12018" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12018-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does this help you?</p><blockquote><p><code>http://wiki.wireshark.org/TCP_Analyze_Sequence_Numbers</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12018" class="comments-container"><span id="12022"></span><div id="comment-12022" class="comment"><div id="post-12022-score" class="comment-score"></div><div class="comment-text"><p>Great, it's exactly the page I was looking for! Much appreciated, Kurt.</p></div><div id="comment-12022-info" class="comment-info"><span class="comment-age">(18 Jun '12, 07:16)</span> fashasha</div></div></div><div id="comment-tools-12018" class="comment-tools"></div><div class="clear"></div><div id="comment-12018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

