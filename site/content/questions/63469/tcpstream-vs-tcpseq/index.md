+++
type = "question"
title = "TCP.Stream VS TCP.Seq"
description = '''What is the differences between tcp.stream and tcp.seq in wireshark field? Are the packets with same tcp.stream should have same tcp.seq?(why if not?)'''
date = "2017-08-14T05:56:00Z"
lastmod = "2017-08-14T06:27:00Z"
weight = 63469
keywords = [ "tcp.stream", "wireshark" ]
aliases = [ "/questions/63469" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP.Stream VS TCP.Seq](/questions/63469/tcpstream-vs-tcpseq)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63469-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the differences between tcp.stream and tcp.seq in wireshark field?</p><p>Are the packets with same tcp.stream should have same tcp.seq?(why if not?)</p></div><div id="question-tags" class="tags-container tags">tcp.stream wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '17, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/1595a24111dff7d0376d456e91895399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zahra&#39;s gravatar image" /><p>Zahra<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zahra has no accepted answers">0%</span></p></div></div><div id="comments-container-63469" class="comments-container"></div><div id="comment-tools-63469" class="comment-tools"></div><div class="clear"></div><div id="comment-63469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63470"></span>

<div id="answer-container-63470" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63470-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>tcp.seq is the sequence number for the TCP header so it reflects what was actually on the wire.</p><p>tpc.stream is a wireshark generated (hence it has [] around it in the UI) value that is used to show the different tcp streams or connections in a capture.</p><p>The values will normally be different as they are entirely different things.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '17, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63470" class="comments-container"></div><div id="comment-tools-63470" class="comment-tools"></div><div class="clear"></div><div id="comment-63470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

