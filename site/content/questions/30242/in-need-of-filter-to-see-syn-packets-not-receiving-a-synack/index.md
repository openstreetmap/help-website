+++
type = "question"
title = "In need of filter to see SYN packets not receiving a SYN/ACK"
description = '''Hi I am trying to filter a packet capture where I can view SYNs not receiving a SYN/ACK back. I am not sure how to accomplish this. Erik'''
date = "2014-02-27T11:30:00Z"
lastmod = "2014-02-28T07:31:00Z"
weight = 30242
keywords = [ "packet-capture", "syn", "wireshark" ]
aliases = [ "/questions/30242" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [In need of filter to see SYN packets not receiving a SYN/ACK](/questions/30242/in-need-of-filter-to-see-syn-packets-not-receiving-a-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30242-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am trying to filter a packet capture where I can view SYNs not receiving a SYN/ACK back. I am not sure how to accomplish this.</p><p>Erik</p></div><div id="question-tags" class="tags-container tags">packet-capture syn wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/f3e606a99b3ca3dc384476ba3755f356?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protongeek&#39;s gravatar image" /><p>protongeek<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protongeek has no accepted answers">0%</span></p></div></div><div id="comments-container-30242" class="comments-container"></div><div id="comment-tools-30242" class="comment-tools"></div><div class="clear"></div><div id="comment-30242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30245"></span>

<div id="answer-container-30245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30245-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming the client enters retransmission if it is not receiving a SYN-ACK in time a possible filter would be <code>tcp.analysis.retransmission and tcp.flags.syn==1</code> - This will not catch the initial SYN packet though.<br />
</p><p>If it sends a RST after giving up this filter might catch those</p><pre><code> (tcp.flags.reset==1 and tcp.seq==1)</code></pre><p>You can combine those with a 'or' of course</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Feb '14, 13:11</p></div></div><div id="comments-container-30245" class="comments-container"></div><div id="comment-tools-30245" class="comment-tools"></div><div class="clear"></div><div id="comment-30245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30269"></span>

<div id="answer-container-30269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30269-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>see my answers (and the links therein) to the same question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/10640/how-to-find-syn-not-followed-by-a-synack">http://ask.wireshark.org/questions/10640/how-to-find-syn-not-followed-by-a-synack</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '14, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30269" class="comments-container"></div><div id="comment-tools-30269" class="comment-tools"></div><div class="clear"></div><div id="comment-30269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

