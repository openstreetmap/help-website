+++
type = "question"
title = "TCP Previous segment not captured, why can&#x27;t I get to a printer?"
description = '''Hi, I have a host on local network 10.2.18.36 and I&#x27;m trying to manage a printer on a WAN destination in our branch office which has url https://10.5.5.241. Telnet to port 443 works fine, the bandwidth is not overloaded, the latency is ok. But the browser can&#x27;t open the page. Locally in the branch o...'''
date = "2015-07-03T03:31:00Z"
lastmod = "2015-07-03T05:30:00Z"
weight = 43843
keywords = [ "not", "segment", "captured", "tcp", "previous" ]
aliases = [ "/questions/43843" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Previous segment not captured, why can't I get to a printer?](/questions/43843/tcp-previous-segment-not-captured-why-cant-i-get-to-a-printer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43843-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a host on local network 10.2.18.36 and I'm trying to manage a printer on a WAN destination in our branch office which has url <a href="https://10.5.5.241">https://10.5.5.241</a>. Telnet to port 443 works fine, the bandwidth is not overloaded, the latency is ok. But the browser can't open the page. Locally in the branch office I can open the URL without problems. Here's the pcap: <a href="https://www.dropbox.com/s/ne0dr0asgv8fbuz/wire-test.pcapng?dl=0">https://www.dropbox.com/s/ne0dr0asgv8fbuz/wire-test.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags">not segment captured tcp previous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '15, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/3f57072917ff74a4578188c33b1aae48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="butch7&#39;s gravatar image" /><p>butch7<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="butch7 has no accepted answers">0%</span></p></div></div><div id="comments-container-43843" class="comments-container"></div><div id="comment-tools-43843" class="comment-tools"></div><div class="clear"></div><div id="comment-43843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43849"></span>

<div id="answer-container-43849" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43849-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 3-way handshake indicates that you have a net MSS of 1360 bytes (MTU 1400) available along the path.<br />
However the first 2 full size segments sent by the printer never make it to you.<br />
So obviously the adjust-mss that was occuring at your VPN edges wasn't enough to get you through the VPN tunnel unfragmented.<br />
You need to check how large your MTU size is using</p><pre><code>ping 10.5.5.241 -f -l 1400  
ping 10.5.5.241 -f -l 1380  
ping 10.5.5.241 -f -l 1360 ...</code></pre><p>and have the MSS adjusted to 40 bytes less<br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '15, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '15, 05:31</p></div></div><div id="comments-container-43849" class="comments-container"><span id="43881"></span><div id="comment-43881" class="comment"><div id="post-43881-score" class="comment-score"></div><div class="comment-text"><p>Thanks Matthias, that helped. Now I'm wondering why that situation occured? We have over 15 branch offices with the same VPN links (one operator) with the same mss-adjust 1360 on tunnels, and the only problem is with this one office.</p></div><div id="comment-43881-info" class="comment-info"><span class="comment-age">(06 Jul '15, 03:33)</span> butch7</div></div><span id="43884"></span><div id="comment-43884" class="comment"><div id="post-43884-score" class="comment-score"></div><div class="comment-text"><p>Well, we can only speculate as to why this occurs only in one branch office. One possible scenario: The problem might be that in this one branch office ICMP fragmentation required message are blocked and don't make it to the printer so basically PMTUD (Path MTU Discovery) wouldn't work there..</p><p>. If you're satisfied with the answer would you mind closing the question by accepting is - (click on the checkmark). Thanks</p></div><div id="comment-43884-info" class="comment-info"><span class="comment-age">(06 Jul '15, 04:48)</span> mrEEde</div></div></div><div id="comment-tools-43849" class="comment-tools"></div><div class="clear"></div><div id="comment-43849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

