+++
type = "question"
title = "What is an acceptable number of Bad TCP packets?"
description = '''I&#x27;m considering these packets as &quot;Bad TCP&quot; (as suggested by Laura C) (tcp.analysis.flags) &amp;amp;&amp;amp; !(tcp.analysis.window_update) I&#x27;m just curious at what % should I start getting worried and start digging through the OSI layers.'''
date = "2015-03-26T10:29:00Z"
lastmod = "2015-03-26T14:14:00Z"
weight = 40909
keywords = [ "tcpflags", "tcp.analysis.flags", "tcp" ]
aliases = [ "/questions/40909" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is an acceptable number of Bad TCP packets?](/questions/40909/what-is-an-acceptable-number-of-bad-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm considering these packets as "Bad TCP" (as suggested by Laura C) (tcp.analysis.flags) &amp;&amp; !(tcp.analysis.window_update)</p><p>I'm just curious at what % should I start getting worried and start digging through the OSI layers.</p></div><div id="question-tags" class="tags-container tags">tcpflags tcp.analysis.flags tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/4a4df10c701372e5dbbb8015a1d6b67b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_harrold&#39;s gravatar image" /><p>patrick_harrold<br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_harrold has no accepted answers">0%</span></p></div></div><div id="comments-container-40909" class="comments-container"></div><div id="comment-tools-40909" class="comment-tools"></div><div class="clear"></div><div id="comment-40909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40917"></span>

<div id="answer-container-40917" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40917-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "Bad TCP" coloring rule (tcp.analysis.flags &amp;&amp; !tcp.analysis.window_update) is a quick indicator of what's wrong with TCP communications in a trace file, but it's a crude measure, so we really can't give a percentage that's meaningful.</p><p>While it matches mostly bad things, it also includes things that aren't necessarily bad, such as out-of-order packets, and Keep-Alive and Keep-Alive ACK packets. Also, note that Wireshark can misidentify out-of-order packets as retransmissions and vice versa.</p><p>In the case of packet loss, for each lost packet there should ideally be one retransmission. However, the number of duplicate ACKs will very greatly depending on the round-trip time between the two systems. So if the systems are close together, for each lost packet you will see (depending on where you're capturing) one "previous segment not captured," one retransmission or fast retransmission, and a <em>small</em> number of duplicate ACKs. If the systems are far apart, you will see one "previous segment not captured," one retransmission or fast retransmission, and a <em>large</em> number of duplicate ACKs. Since duplicate ACKs match the Bad TCP rule, the percentage of Bad TCP will vary simply based on how far apart the two systems are, even though the actual level of packet loss might not be very different.</p><p>Obviously, the smaller the percentage of Bad TCP the better, but you need to do a deeper analysis than just comparing to a percentage.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-40917" class="comments-container"><span id="41037"></span><div id="comment-41037" class="comment"><div id="post-41037-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the detailed reply Jim.</p><p>I never knew that tcp.analysis.flags also included keep-alive packets, and had not considered that the out-of-order packets were not necessarily "bad."And a single duplicate ACK is probably acceptable in most cases.</p><p>It seems that for this specific filter there is no ball-park percentage/rule. However, do you have a suggested filter that you might use for an initial look at the overall health of a specific trace? Any pointers/links/etc would be very appreciated.</p></div><div id="comment-41037-info" class="comment-info"><span class="comment-age">(30 Mar '15, 13:52)</span> patrick_harrold</div></div><span id="41044"></span><div id="comment-41044" class="comment"><div id="post-41044-score" class="comment-score">1</div><div class="comment-text"><p>You can filter a lot of the false positives with:</p><p>&amp;&amp; !tcp.analysis.duplicate_ack_num &gt; 1</p><p>chained to the end of your filter.</p><p>It wont make it better, but it will show you fewer chains and give you a more realistic feel for the amount of retransmissions. Most retransmissions will then appear with an "Out Of Order" or "Previous segment not captured" in close proximity.</p></div><div id="comment-41044-info" class="comment-info"><span class="comment-age">(31 Mar '15, 03:03)</span> DarrenWright</div></div></div><div id="comment-tools-40917" class="comment-tools"></div><div class="clear"></div><div id="comment-40917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

