+++
type = "question"
title = "How does &quot;tcp.analysis.retransmission&quot; work?"
description = '''Hello world, I want to understand how wireshark detect retransmission, or in other words, how it implements the filter &quot;tcp.analysis.retransmission&quot;. I&#x27;ve found several related posts: https://ask.wireshark.org/questions/25609/how-does-wireshark-detect-tcp-retransmissions https://ask.wireshark.org/qu...'''
date = "2017-10-18T20:07:00Z"
lastmod = "2017-10-18T23:17:00Z"
weight = 64019
keywords = [ "filter", "retransmissions", "wireshark" ]
aliases = [ "/questions/64019" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How does "tcp.analysis.retransmission" work?](/questions/64019/how-does-tcpanalysisretransmission-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64019-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello world,</p><p>I want to understand how wireshark detect retransmission, or in other words, how it implements the filter "tcp.analysis.retransmission".</p><p>I've found several related posts:</p><p><a href="https://ask.wireshark.org/questions/25609/how-does-wireshark-detect-tcp-retransmissions">https://ask.wireshark.org/questions/25609/how-does-wireshark-detect-tcp-retransmissions</a></p><p><a href="https://ask.wireshark.org/questions/16771/tcpanalysisretransmission">https://ask.wireshark.org/questions/16771/tcpanalysisretransmission</a></p><p>However, I'm still not sure about the details. The real cases seem to be more complex than just comparing SEQ. For example, I have found a retransmission packet has a different SEQ from the original packet (only +1 to the original SEQ though).</p><p>Therefore I'm looking for help - could anyone point out somewhere in the wireshark source code for me to better understand the mechanism?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">filter retransmissions wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '17, 20:07</strong></p><img src="https://secure.gravatar.com/avatar/3fe2cbdac3898f5f53d665006a304051?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zzy&#39;s gravatar image" /><p>zzy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zzy has no accepted answers">0%</span></p></div></div><div id="comments-container-64019" class="comments-container"></div><div id="comment-tools-64019" class="comment-tools"></div><div class="clear"></div><div id="comment-64019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64021"></span>

<div id="answer-container-64021" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64021-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could start <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-tcp.c;h=42e85b140963af63a90d681631d8d36e6c5caf65;hb=HEAD#l1850">here</a> looking at the sequence number analysis. What it comes down to is keeping track of the bytes already seen, and checking the new received TCP packet where the bytes fit into the stream.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '17, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-64021" class="comments-container"><span id="64027"></span><div id="comment-64027" class="comment"><div id="post-64027-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much! That's exactly what I need!</p></div><div id="comment-64027-info" class="comment-info"><span class="comment-age">(19 Oct '17, 08:14)</span> zzy</div></div><span id="64028"></span><div id="comment-64028" class="comment"><div id="post-64028-score" class="comment-score"></div><div class="comment-text"><p>A while back I tried to document TCP analysis behavior in the <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html">User's Guide</a>. The retransmission check compares the current sequence number with the next expected sequence number, but it can be superseded by several other checks, e.g. fast retransmission or out-of-order.</p></div><div id="comment-64028-info" class="comment-info"><span class="comment-age">(19 Oct '17, 08:24)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-64021" class="comment-tools"></div><div class="clear"></div><div id="comment-64021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

