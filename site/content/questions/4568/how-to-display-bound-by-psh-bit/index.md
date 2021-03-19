+++
type = "question"
title = "How to Display &quot;Bound by PSH bit&quot;?"
description = '''Hi, A picture is worth a thousand words, so for explaining that actually the application is trying to steer TCP instead of leaving it to TCP, how can i:  1.graph or proof this phenomenon and  2.tell if it does a good job or not? link:A brief explanation of Bound by Push Bit All advice always highly ...'''
date = "2011-06-15T01:03:00Z"
lastmod = "2011-06-22T18:55:00Z"
weight = 4568
keywords = [ "graph", "psh", "boundbypsh" ]
aliases = [ "/questions/4568" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to Display "Bound by PSH bit"?](/questions/4568/how-to-display-bound-by-psh-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4568-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, A picture is worth a thousand words, so for explaining that actually the application is trying to steer TCP instead of leaving it to TCP, how can i: 1.graph or proof this phenomenon and 2.tell if it does a good job or not?</p><p>link:<a href="http://www.tcpipguide.com/free/t_TCPImmediateDataTransferPushFunction-2.htm">A brief explanation of Bound by Push Bit</a></p><p>All advice always highly appreciated!</p><p>regards, Marc</p></div><div id="question-tags" class="tags-container tags">graph psh boundbypsh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '11, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-4568" class="comments-container"><span id="4634"></span><div id="comment-4634" class="comment"><div id="post-4634-score" class="comment-score"></div><div class="comment-text"><p>Hi, maybe i should clarify: i'm searching for a way to prove that it's the application that uses the tcp function push (the tcp.flags.push == 1) to get more control. I'm thinking of recognizing a pattern, any idea's?</p></div><div id="comment-4634-info" class="comment-info"><span class="comment-age">(20 Jun '11, 06:00)</span> Marc</div></div></div><div id="comment-tools-4568" class="comment-tools"></div><div class="clear"></div><div id="comment-4568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4684"></span>

<div id="answer-container-4684" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4684-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can easily see this by using Stevens throughput graph. What you'll notice is clumps of transfers (sharp vertical slopes). At the end of the vertical jumps, you'll typically see the PSH bit in the packet. Another way to see it is to just watch how many bytes are being transferred from PSH to PSH bit. You can add the cumulative byte field as a column and use the "mark time reference" to see how many bytes are being transferred per push.</p><p>Many of my sharkfest presentations cover this scenario. Google for "sharkfest 2009" then grab "AU-4, AU-5 (Bae) Protocol Analysis in a Complex Enterprise" Look at case III.</p><p>If this doesn't make sense, let me know and I'll post some pics of what I'm talking about.</p><p>Good luck.</p><p>hsb</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '11, 18:55</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-4684" class="comments-container"><span id="4751"></span><div id="comment-4751" class="comment"><div id="post-4751-score" class="comment-score"></div><div class="comment-text"><p>First off: thak you verymuch for the answer! Hansang,</p><p>Saw the presentation for Sharkfest 2009, had a look at the ftp tracefile, worked out I had to look for sharp vertical slopes with a psh bit at the end, made a column for cumulative bytes, scrolled through the trace looking for pattern, I can see the rhythm in your trace [PSH,ACK],[ACK],[ACK],[ACK],[ACK],[PSH,ACK] but don’t see it in mine as clearly yet..,</p><p>I do need to zoom in quite a bit in the Stevens trace right?</p></div><div id="comment-4751-info" class="comment-info"><span class="comment-age">(25 Jun '11, 06:04)</span> Marc</div></div><span id="4773"></span><div id="comment-4773" class="comment"><div id="post-4773-score" class="comment-score"></div><div class="comment-text"><p>Yes, if you keep zooming in, you'll see the "banks" of packets that make up the sharp vertical track. If you want, you can use editcap to chop the packet to its header and email it to me. I can check it out for you.</p></div><div id="comment-4773-info" class="comment-info"><span class="comment-age">(27 Jun '11, 14:11)</span> hansangb</div></div><span id="4782"></span><div id="comment-4782" class="comment"><div id="post-4782-score" class="comment-score"></div><div class="comment-text"><p>allright, i'll work it down to the headers and mail it to you, thanks!</p></div><div id="comment-4782-info" class="comment-info"><span class="comment-age">(28 Jun '11, 04:01)</span> Marc</div></div><span id="4825"></span><div id="comment-4825" class="comment"><div id="post-4825-score" class="comment-score"></div><div class="comment-text"><p>yup, I got it. I'll take a look.</p></div><div id="comment-4825-info" class="comment-info"><span class="comment-age">(29 Jun '11, 16:38)</span> hansangb</div></div><span id="5112"></span><div id="comment-5112" class="comment"><div id="post-5112-score" class="comment-score"></div><div class="comment-text"><p>hansang, did you see the trace?</p></div><div id="comment-5112-info" class="comment-info"><span class="comment-age">(18 Jul '11, 23:57)</span> Marc</div></div></div><div id="comment-tools-4684" class="comment-tools"></div><div class="clear"></div><div id="comment-4684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

