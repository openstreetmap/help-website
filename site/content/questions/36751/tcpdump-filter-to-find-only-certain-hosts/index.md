+++
type = "question"
title = "tcpdump filter to find only certain hosts"
description = '''I&#x27;ve been trying to come up with a tcpdump filter to find all IPv4 hosts that fit x.x.x.35 - I just need to see packets that are hosts ending in .35 and I don&#x27;t care about the network numbers.'''
date = "2014-10-01T04:16:00Z"
lastmod = "2014-10-01T04:50:00Z"
weight = 36751
keywords = [ "filter", "host" ]
aliases = [ "/questions/36751" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tcpdump filter to find only certain hosts](/questions/36751/tcpdump-filter-to-find-only-certain-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to come up with a tcpdump filter to find all IPv4 hosts that fit x.x.x.35 - I just need to see packets that are hosts ending in .35 and I don't care about the network numbers.</p></div><div id="question-tags" class="tags-container tags">filter host</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '14, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/512bd1e2b603c9a1f3536716fb8c2540?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James%20Steinmetz&#39;s gravatar image" /><p>James Steinmetz<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James Steinmetz has no accepted answers">0%</span></p></div></div><div id="comments-container-36751" class="comments-container"></div><div id="comment-tools-36751" class="comment-tools"></div><div class="clear"></div><div id="comment-36751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36752"></span>

<div id="answer-container-36752" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36752-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://www.wains.be/pub/networking/tcpdump_advanced_filters.txt">here</a> for some advanced filters, but basically you need to slice the ip header in the correct spot:</p><pre><code>-f &quot;ip[15] = 35 or ip[19] = 35&quot;</code></pre><p>quote as required for your shell.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '14, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36752" class="comments-container"><span id="36754"></span><div id="comment-36754" class="comment"><div id="post-36754-score" class="comment-score"></div><div class="comment-text"><p>That did the trick and will help me continue to learn the more complex filter methods - THANK YOU.</p></div><div id="comment-36754-info" class="comment-info"><span class="comment-age">(01 Oct '14, 04:58)</span> James Steinmetz</div></div><span id="36755"></span><div id="comment-36755" class="comment"><div id="post-36755-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-36755-info" class="comment-info"><span class="comment-age">(01 Oct '14, 05:10)</span> grahamb ♦</div></div></div><div id="comment-tools-36752" class="comment-tools"></div><div class="clear"></div><div id="comment-36752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

