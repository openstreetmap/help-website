+++
type = "question"
title = "How to hide ICMP packets?"
description = '''Hi, This is the first time I am using wireshark and facing below issue:- I have created my own dissector named IPTWP(UDP). While trying to filter IPTWP packets, the ICMP packets also get displayed. How to find out whats common between my dissector and ICMP dissector? Also, when looking at the ICMP t...'''
date = "2012-10-03T22:42:00Z"
lastmod = "2012-10-04T00:23:00Z"
weight = 14697
keywords = [ "filter", "udp", "icmp" ]
aliases = [ "/questions/14697" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to hide ICMP packets?](/questions/14697/how-to-hide-icmp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14697-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>This is the first time I am using wireshark and facing below issue:-</p><p>I have created my own dissector named IPTWP(UDP). While trying to filter IPTWP packets, the ICMP packets also get displayed. How to find out whats common between my dissector and ICMP dissector? Also, when looking at the ICMP tree, IPTWP is shown as a part of tree along with UDP and IPv4. Therefore, when i try to set filter to "udp only", the icmp packets are visible. I am not sure whats happening over here. Please help...</p><p>Thanks, Priyanka</p></div><div id="question-tags" class="tags-container tags">filter udp icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '12, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/f853b402d97db966da355b5ddaaa2931?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="priyankaB&#39;s gravatar image" /><p>priyankaB<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="priyankaB has no accepted answers">0%</span></p></div></div><div id="comments-container-14697" class="comments-container"></div><div id="comment-tools-14697" class="comment-tools"></div><div class="clear"></div><div id="comment-14697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14698"></span>

<div id="answer-container-14698" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14698-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're probably seeing ICMP packets sent in response to the IPTWP-over-UDP-over-IP packets, and those ICMP packets include a copy of some or all of the IP datagram in response to which they're sent; Wireshark dissects that copy of the IP datagram, so it finds IPTWP packets (presumably because enough of the IP datagram is in the ICMP response to include the IPTWP packet).</p><p>If you don't want to see them, try, for example, "udp and not icmp".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '12, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14698" class="comments-container"><span id="14702"></span><div id="comment-14702" class="comment"><div id="post-14702-score" class="comment-score"></div><div class="comment-text"><p>I have already tried [iptwp &amp;&amp; !icmp] and it worked i.e. no ICMP packets only IPTWP, but the client was not okay with it. Is there any other way to do it, if I set filter to "iptwp only" it hides all other packets(TCP, UDP, etc) except for ICMP. I am okay with whatever udp does since it is not part of dissector I have created, but iptwp should behave correctly, i.e. when filter is set to "iptwp only" it should hide all other packets - udp, icmp, tcp, etc.</p></div><div id="comment-14702-info" class="comment-info"><span class="comment-age">(04 Oct '12, 03:39)</span> priyankaB</div></div><span id="14711"></span><div id="comment-14711" class="comment"><div id="post-14711-score" class="comment-score"></div><div class="comment-text"><p>No, there's no other way to do it. If the client doesn't like it, they're more than welcome to use a packet sniffer that doesn't dissect the included IP datagram in ICMP packets.</p></div><div id="comment-14711-info" class="comment-info"><span class="comment-age">(04 Oct '12, 11:14)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14698" class="comment-tools"></div><div class="clear"></div><div id="comment-14698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

