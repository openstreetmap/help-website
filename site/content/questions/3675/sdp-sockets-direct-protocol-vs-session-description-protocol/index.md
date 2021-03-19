+++
type = "question"
title = "SDP - Sockets Direct Protocol vs. Session Description Protocol"
description = '''At Wireshark 1.5.1 Release Notes I can read, &#x27;Infiniband Sockets Direct Protocol (SDP)&#x27; is supported now. Wireshark 1.5.1 itself says at internals-&amp;gt;supported protocols (show), it supports &#x27;SDP (Session Description Protocol)&#x27;. Who is right? I need SDP (Sockets Direct Protocol). Thanks in advance, ...'''
date = "2011-04-21T01:37:00Z"
lastmod = "2012-10-18T23:24:00Z"
weight = 3675
keywords = [ "sdp" ]
aliases = [ "/questions/3675" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SDP - Sockets Direct Protocol vs. Session Description Protocol](/questions/3675/sdp-sockets-direct-protocol-vs-session-description-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At Wireshark 1.5.1 Release Notes I can read, 'Infiniband Sockets Direct Protocol (SDP)' is supported now. Wireshark 1.5.1 itself says at internals-&gt;supported protocols (show), it supports 'SDP (Session Description Protocol)'. Who is right? I need SDP (Sockets Direct Protocol). Thanks in advance, Wolfgang</p></div><div id="question-tags" class="tags-container tags">sdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '11, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/2b16f2bfa5f3898236a742b687509edf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wolfgang&#39;s gravatar image" /><p>Wolfgang<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wolfgang has no accepted answers">0%</span></p></div></div><div id="comments-container-3675" class="comments-container"></div><div id="comment-tools-3675" class="comment-tools"></div><div class="clear"></div><div id="comment-3675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3676"></span>

<div id="answer-container-3676" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3676-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both are right. Infiniband Socket Direct Protocol can be found under the name "Infiniband SDP", and filtered using "ib_sdp".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '11, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3676" class="comments-container"><span id="3677"></span><div id="comment-3677" class="comment"><div id="post-3677-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap for your fast answer. This helps me one step further. I now find the filter and the right protocol. Unfortunately there are no SDP packets in my traces. When I run TCP over Infiniband I can see all expected packts in the trace. When we run SDP over Infiniband, the traces are empty (not really empty, but the packets I expect are missing). When I enable only Infiniband SDP peotocol, there are only unknown packets in the trace, when I enable all protocols, there are mainly TCP packets, no single SDP packet.</p><p>Any help ist appreciated, Wolfgang</p></div><div id="comment-3677-info" class="comment-info"><span class="comment-age">(21 Apr '11, 03:59)</span> Wolfgang</div></div><span id="3876"></span><div id="comment-3876" class="comment"><div id="post-3876-score" class="comment-score">1</div><div class="comment-text"><p>Ok, one more step: You cannot directly filter SDP protocols while capturing. Seen here: http://wiki.wireshark.org/SDP?action=show&amp;redirect=SessionDescriptionProtocol</p><p>Wolfgang</p></div><div id="comment-3876-info" class="comment-info"><span class="comment-age">(02 May '11, 06:39)</span> Wolfgang</div></div></div><div id="comment-tools-3676" class="comment-tools"></div><div class="clear"></div><div id="comment-3676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15100"></span>

<div id="answer-container-15100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15100-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are still looking for something about Session Description Protocol, you should check this out: <a href="http://www.ozekiphone.com/what-is-sdp-session-description-protocol-352.html">http://www.ozekiphone.com/what-is-sdp-session-description-protocol-352.html</a> SDP is explained in this article with Ozeki Phone System XE. It helped me a lot :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '12, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/0e3a984b7b5d2e9b61fbfa9ebfb36934?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michaelharris&#39;s gravatar image" /><p>michaelharris<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michaelharris has no accepted answers">0%</span></p></div></div><div id="comments-container-15100" class="comments-container"></div><div id="comment-tools-15100" class="comment-tools"></div><div class="clear"></div><div id="comment-15100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

