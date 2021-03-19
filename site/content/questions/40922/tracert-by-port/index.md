+++
type = "question"
title = "&#x27;tracert&#x27; by port"
description = '''We believe ATT is blocking ISAKMP (port 500) traffic somewhere on their mobile network.  Using a laptop with a CSpire phone as a MIFI hotspot, Sonicwall VPN software works flawlessly. Same system using an ATT phone as a MIFI hotspot throws up ISAKMP errors - the same error one would get if there was...'''
date = "2015-03-26T16:50:00Z"
lastmod = "2015-03-27T03:15:00Z"
weight = 40922
keywords = [ "tracert" ]
aliases = [ "/questions/40922" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# ['tracert' by port](/questions/40922/tracert-by-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We believe ATT is blocking ISAKMP (port 500) traffic somewhere on their mobile network.</p><p>Using a laptop with a CSpire phone as a MIFI hotspot, Sonicwall VPN software works flawlessly.</p><p>Same system using an ATT phone as a MIFI hotspot throws up ISAKMP errors - the same error one would get if there was a break in the wireless path.</p><p>In troubleshooting (simpler) routing issues in the past, I was able to TRACERT to a specific IP address and it was clear where the traffic was blocked. We sent the IP address of the offending router to Comcast and they fixed the issue.</p><p>Could someone recommend a method to see where along the route the ISAKMP traffic is being blocked?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tracert</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/bb22f32e663b48f7d57ec4d288399d90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matrixmike&#39;s gravatar image" /><p>matrixmike<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matrixmike has no accepted answers">0%</span></p></div></div><div id="comments-container-40922" class="comments-container"></div><div id="comment-tools-40922" class="comment-tools"></div><div class="clear"></div><div id="comment-40922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40924"></span>

<div id="answer-container-40924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40924-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Could someone recommend a method to see where along the route the ISAKMP traffic is being blocked?</p></blockquote><p>send IKE frames with increasing IP TTL and test where you don't get "ICMP time exceeded" answers anymore, if they send them at all.</p><p>Scapy is a good tool to send those frames:</p><blockquote><p><a href="http://www.secdev.org/projects/scapy/">http://www.secdev.org/projects/scapy/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40924" class="comments-container"></div><div id="comment-tools-40924" class="comment-tools"></div><div class="clear"></div><div id="comment-40924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40933"></span>

<div id="answer-container-40933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40933-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's more likely to be some kind of MTU issue rather than operator actively blocking packets.</p><p>You can try forcing your laptop to use smaller MTU size</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '15, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-40933" class="comments-container"></div><div id="comment-tools-40933" class="comment-tools"></div><div class="clear"></div><div id="comment-40933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40934"></span>

<div id="answer-container-40934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40934-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've used <a href="http://pwhois.org/lft/index.who">lft</a> to troubleshoot an identical issue with another ISP in the past as it can use tcp or udp as the bearer protocol for testing rather than icmp as in standard traceroute. Unfortunately lft isn't available for Windows.</p><p>lft was needed because in our issue the ISP had an egress filter on a router that blocked udp port 500 but allowed icmp to pass through, thus traceroute worked but lft showed where the block was.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '15, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40934" class="comments-container"></div><div id="comment-tools-40934" class="comment-tools"></div><div class="clear"></div><div id="comment-40934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

