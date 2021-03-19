+++
type = "question"
title = "this frame is a suspected retransmission i get that a lot from wire shark what is it and how do i stop it"
description = '''Retransmissions are triggered by duplicate acks or a retransmission timer expiring. In your case it&#x27;s the client asking for the same segment over and over. The server&#x27;s retransmitted segments never arrive at the client though - when they are a full MSS 1460 in size i saw this on the page someones an...'''
date = "2014-11-08T11:35:00Z"
lastmod = "2014-11-08T16:23:00Z"
weight = 37702
keywords = [ "wireshark" ]
aliases = [ "/questions/37702" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [this frame is a suspected retransmission i get that a lot from wire shark what is it and how do i stop it](/questions/37702/this-frame-is-a-suspected-retransmission-i-get-that-a-lot-from-wire-shark-what-is-it-and-how-do-i-stop-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37702-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Retransmissions are triggered by duplicate acks or a retransmission timer expiring. In your case it's the client asking for the same segment over and over. The server's retransmitted segments never arrive at the client though - when they are a full MSS 1460 in size i saw this on the page someones answer i just need some explanation of what it is how do i stop it i have no clue</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '14, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/08a002781d656e49c05a3be0352280e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MostUnlikedOnPS4&#39;s gravatar image" /><p>MostUnlikedO...<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MostUnlikedOnPS4 has no accepted answers">0%</span></p></div></div><div id="comments-container-37702" class="comments-container"></div><div id="comment-tools-37702" class="comment-tools"></div><div class="clear"></div><div id="comment-37702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37705"></span>

<div id="answer-container-37705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The description you're looking at there is one where a client isn't receiving a packet that the server is sending, and the way that condition is represented at the TCP level of a trace (ie: when the server's RTO timer expires without an ack for the segment, or when fast retransmission is triggered by duplicate ACKs from the client, the server retransmits).</p><p>As for "How do I stop it", that depends on the cause. There are all kinds of reasons why a client might not receive a packet sent to it from a server. "Why does packet loss happen" is too broad a question to answer in this way so I suggest you tailor your question to be specific to the scenario that you are looking at in your network, including details on the network topology and a sample trace if possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '14, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-37705" class="comments-container"></div><div id="comment-tools-37705" class="comment-tools"></div><div class="clear"></div><div id="comment-37705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

