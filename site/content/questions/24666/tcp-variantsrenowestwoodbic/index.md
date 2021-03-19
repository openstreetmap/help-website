+++
type = "question"
title = "tcp variants(reno,westwood,bic)"
description = '''sir i asked about that how to evaluate the performance of different variants of TCP ie. like reno ,westwood ,bic etc sir pls help how to differentiate between these variants and how to evaluate the performance of individual variant like for reno throughput and rtt graph plsss help '''
date = "2013-09-13T21:34:00Z"
lastmod = "2013-09-14T04:33:00Z"
weight = 24666
keywords = [ "tcp" ]
aliases = [ "/questions/24666" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tcp variants(reno,westwood,bic)](/questions/24666/tcp-variantsrenowestwoodbic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24666-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>sir i asked about that how to evaluate the performance of different variants of TCP ie. like reno ,westwood ,bic etc sir pls help how to differentiate between these variants and how to evaluate the performance of individual variant like for reno throughput and rtt graph plsss help</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 21:34</strong></p><img src="https://secure.gravatar.com/avatar/d316fdeb8063b3195b7cc70909561df0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shaziya%20islam&#39;s gravatar image" /><p>shaziya islam<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shaziya islam has no accepted answers">0%</span></p></div></div><div id="comments-container-24666" class="comments-container"></div><div id="comment-tools-24666" class="comment-tools"></div><div class="clear"></div><div id="comment-24666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24668"></span>

<div id="answer-container-24668" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24668-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Okay, I already told you what to do in your other question, but here it is in a more specific form:</p><ol><li>Find the specifications for each of the stack you want to evaluate. This can be a difficult task, because not all of them are easily found, but reading RFCs probably helps.</li><li>Do a differential compare between the stack types to see what kind of features/behavior they have that other stacks don't. Examples are RTO, Fast Retransmit, Slow Start, Congestion Avoidance, Fast Recovery, Binary Increase Congestion Control, and multiple algorithms looking at send rates and RTT.</li><li>Find out what OS has what kind of stack. Most rare stacks are probably available for UNIX style OSes.</li><li>Setup test systems that use the particular stack (this will be quite time consuming) and run tests while capturing</li><li>Analyse traces to see if the behavior shows as expected. Filter for tcp.analysis.flags to see TCP expert messages, and use I/O Graph and the TCP graphs in the statistics menu</li><li>Write your paper.</li></ol><p>Good luck. Don't ask this question again before you have more specific things to ask, please.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24668" class="comments-container"></div><div id="comment-tools-24668" class="comment-tools"></div><div class="clear"></div><div id="comment-24668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24674"></span>

<div id="answer-container-24674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24674-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think a network simulator is a far better tool to compare different TCP implementation details, than only looking at differences in the capture file. Obviously Wireshark will be very valuable, but within a network simulator you'll have much more options to trace and analyze performance characteristics.</p><p>Network simulators:</p><blockquote><p><a href="http://www.wand.net.nz/~stj2/nsc/">http://www.wand.net.nz/~stj2/nsc/</a><br />
<a href="http://www.wand.net.nz/~stj2/nsc/">http://www.wand.net.nz/~stj2/nsc/</a><br />
many more. Just search google.</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-24674" class="comments-container"></div><div id="comment-tools-24674" class="comment-tools"></div><div class="clear"></div><div id="comment-24674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

