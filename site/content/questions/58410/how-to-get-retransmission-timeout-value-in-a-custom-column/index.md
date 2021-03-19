+++
type = "question"
title = "How to get Retransmission Timeout value in a custom column?"
description = '''I am trying to get the RTO in a custom column but it doesn´t work, also I can´t find the value manualy. In several tutorials the value is at &quot;Transmission Control Protocol&quot; -&amp;gt; &quot;SEQ/ACK Analysis&quot; -&amp;gt; &quot;TCP Analysis Flags&quot; -&amp;gt; &quot;Expert Info&quot; . But there is no &quot;TCP Analysis Flags&quot;. So I tried anot...'''
date = "2016-12-28T15:21:00Z"
lastmod = "2016-12-28T16:03:00Z"
weight = 58410
keywords = [ "column", "tcp.analysis.rto", "rto", "tcp" ]
aliases = [ "/questions/58410" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to get Retransmission Timeout value in a custom column?](/questions/58410/how-to-get-retransmission-timeout-value-in-a-custom-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58410-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to get the RTO in a custom column but it doesn´t work, also I can´t find the value manualy. In several tutorials the value is at "Transmission Control Protocol" -&gt; "SEQ/ACK Analysis" -&gt; "TCP Analysis Flags" -&gt; "Expert Info" . But there is no "TCP Analysis Flags". So I tried another way. . .<br />
<a href="https://www.wireshark.org/docs/dfref/t/tcp.html">https://www.wireshark.org/docs/dfref/t/tcp.html</a><br />
I added a new column at Column-Preferences:<br />
- FIELD NAME -&gt; tcp.analysis.rto<br />
- TYPE -&gt; custom<br />
But it stays empty. I am out of ideas.</p><p>greetings peacemaker</p></div><div id="question-tags" class="tags-container tags">column tcp.analysis.rto rto tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '16, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/ec66054f9698c5582b82d1718f1da905?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peacemaker&#39;s gravatar image" /><p>peacemaker<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peacemaker has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Dec '16, 16:17</p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></br></p></div></div><div id="comments-container-58410" class="comments-container"></div><div id="comment-tools-58410" class="comment-tools"></div><div class="clear"></div><div id="comment-58410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58411"></span>

<div id="answer-container-58411" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58411-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seems to work OK for me, as shown:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/rto.png" alt="alt text" /></p><p>with</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-12-28_18_58_57-Wireshark__Edit_Column_Details.png" alt="alt text" /></p><p>Do you actually have retransmissions for an RTO to be measured? Otherwise, I find this field will be blank.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '16, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></img></div></div><div id="comments-container-58411" class="comments-container"><span id="58412"></span><div id="comment-58412" class="comment"><div id="post-58412-score" class="comment-score"></div><div class="comment-text"><p>I created another file with trpt (transliterate protocol trace) there I got rxtcur (current retransmit value). But that file was rly huge and I wanted wireshark do all the work for me, so I spend a whole hour trying to get this goin. And in the end there were no retransmissions.</p><p>I thought I could get the current retransmit value sorted by wireshark but I guess my TCPdump didn´t contain that information ... time well spend I´d say</p></div><div id="comment-58412-info" class="comment-info"><span class="comment-age">(28 Dec '16, 16:44)</span> peacemaker</div></div></div><div id="comment-tools-58411" class="comment-tools"></div><div class="clear"></div><div id="comment-58411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

