+++
type = "question"
title = "pointing retransmission packet"
description = '''I&#x27;m using MPTCP and there are retransmissions when fail or errors. Those retransmission packets have different sequence number but same data sequence number(DSN) as the original packets. But there is no information that it&#x27;s a retransmission packet. So I want to mark that it&#x27;s a retransmission packe...'''
date = "2017-07-11T02:27:00Z"
lastmod = "2017-07-11T04:22:00Z"
weight = 62661
keywords = [ "compare", "datasequencenumber" ]
aliases = [ "/questions/62661" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pointing retransmission packet](/questions/62661/pointing-retransmission-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62661-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using MPTCP and there are retransmissions when fail or errors. Those retransmission packets have different sequence number but same data sequence number(DSN) as the original packets. But there is no information that it's a retransmission packet. So I want to mark that it's a retransmission packet. How would I approach this task?</p></div><div id="question-tags" class="tags-container tags">compare datasequencenumber</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/3a702eaa9f4d90c81f74480545063c71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ngn505&#39;s gravatar image" /><p>ngn505<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ngn505 has no accepted answers">0%</span></p></div></div><div id="comments-container-62661" class="comments-container"><span id="62663"></span><div id="comment-62663" class="comment"><div id="post-62663-score" class="comment-score"></div><div class="comment-text"><p>Do you mean Modbus TCP?</p></div><div id="comment-62663-info" class="comment-info"><span class="comment-age">(11 Jul '17, 03:03)</span> grahamb ♦</div></div><span id="62664"></span><div id="comment-62664" class="comment"><div id="post-62664-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.multipath-tcp.org/">https://www.multipath-tcp.org/</a></p></div><div id="comment-62664-info" class="comment-info"><span class="comment-age">(11 Jul '17, 03:07)</span> sindy</div></div></div><div id="comment-tools-62661" class="comment-tools"></div><div class="clear"></div><div id="comment-62661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62666"></span>

<div id="answer-container-62666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62666-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the doc directory in the sources. There you'll find a README on request-response tracking. That could be used to track the DSN vs seq# and find duplicates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62666" class="comments-container"><span id="62692"></span><div id="comment-62692" class="comment"><div id="post-62692-score" class="comment-score"></div><div class="comment-text"><p>yeah I've read that but don't really understand how to apply what it says..</p></div><div id="comment-62692-info" class="comment-info"><span class="comment-age">(11 Jul '17, 22:38)</span> ngn505</div></div><span id="62693"></span><div id="comment-62693" class="comment"><div id="post-62693-score" class="comment-score"></div><div class="comment-text"><p>The best way to find out is reading other dissector source code. In this case look at ICMP for example.</p></div><div id="comment-62693-info" class="comment-info"><span class="comment-age">(11 Jul '17, 23:04)</span> Jaap ♦</div></div><span id="62694"></span><div id="comment-62694" class="comment"><div id="post-62694-score" class="comment-score"></div><div class="comment-text"><p>First, have you checked the <code>In depth analysis of Data Sequence Signals (DSS) mappings</code> tickbox in <code>Edit -&gt; Preferences -&gt; Protocols -&gt; MPTCP</code>? If not, does doing so solve your issue?</p></div><div id="comment-62694-info" class="comment-info"><span class="comment-age">(11 Jul '17, 23:06)</span> sindy</div></div></div><div id="comment-tools-62666" class="comment-tools"></div><div class="clear"></div><div id="comment-62666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

