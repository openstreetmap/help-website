+++
type = "question"
title = "how to get cwnd in Wireshark?"
description = '''how to get cwnd in Wireshark?'''
date = "2011-03-15T02:07:00Z"
lastmod = "2011-03-15T16:29:00Z"
weight = 2820
keywords = [ "cwnd" ]
aliases = [ "/questions/2820" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get cwnd in Wireshark?](/questions/2820/how-to-get-cwnd-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2820-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to get cwnd in Wireshark?</p></div><div id="question-tags" class="tags-container tags">cwnd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '11, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/b9d8b5100ac69ceb6d1a4e3c5913be56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tcper&#39;s gravatar image" /><p>tcper<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tcper has no accepted answers">0%</span></p></div></div><div id="comments-container-2820" class="comments-container"></div><div id="comment-tools-2820" class="comment-tools"></div><div class="clear"></div><div id="comment-2820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2846"></span>

<div id="answer-container-2846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2846-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean the congestion window, then, to quote <a href="http://www.ietf.org/rfc/rfc2581.txt">RFC 2581</a>, "The congestion window (cwnd) is a sender-side limit on the amount of data the sender can transmit into the network before receiving an acknowledgment (ACK)"; it's a parameter inside the TCP network stack - its value is not transmitted in network packets, so you won't see it as a field in the dissection of a TCP packet.</p><p>It <em>might</em> be possible to infer it by seeing the sender sending smaller TCP segments than would be possible given the receive window, but that doesn't guarantee that the number of bytes transmitted is the congestion window value - there might be other reasons (such as not having enough data to transmit to fill up the receiver's window) why the sender didn't send a full window's worth of data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2846" class="comments-container"></div><div id="comment-tools-2846" class="comment-tools"></div><div class="clear"></div><div id="comment-2846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

