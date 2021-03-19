+++
type = "question"
title = "Remote server not responding"
description = '''Hi I have a Windows 2008 server running a bespoke app that needs to speak to a vendor server named vendor.domain.com on the Internet on port 443. Unfortunately, the application is not working - the vendor says that it&#x27;s because our server can&#x27;t speak with vendor.domain.com If I ping vendor.domain.co...'''
date = "2012-09-27T14:19:00Z"
lastmod = "2012-09-27T14:27:00Z"
weight = 14576
keywords = [ "connectivity", "ping" ]
aliases = [ "/questions/14576" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote server not responding](/questions/14576/remote-server-not-responding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14576-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a Windows 2008 server running a bespoke app that needs to speak to a vendor server named <a href="http://vendor.domain.com">vendor.domain.com</a> on the Internet on port 443.</p><p>Unfortunately, the application is not working - the vendor says that it's because our server can't speak with <a href="http://vendor.domain.com">vendor.domain.com</a></p><p>If I ping <a href="http://vendor.domain.com">vendor.domain.com</a> from the server, then I get "request timed out", although it does resolve to 66.9.37.193 (example).</p><p>I'm pretty sure that the vendor server, or something along the way, is dropping the ping because ICMP is not allowed.</p><p>I've got a wireshark trace of the ping to 66.9.37.193 from the server - what should I be looking for to provde that the pings are being dropped?</p></div><div id="question-tags" class="tags-container tags">connectivity ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '12, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/0bfdf61da8695f1c30b6518ba5e299ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harrydolan&#39;s gravatar image" /><p>Harrydolan<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harrydolan has no accepted answers">0%</span></p></div></div><div id="comments-container-14576" class="comments-container"></div><div id="comment-tools-14576" class="comment-tools"></div><div class="clear"></div><div id="comment-14576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14577"></span>

<div id="answer-container-14577" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14577-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the vendor is dropping (instead of "rejecting") your ICMP Echo Request packets you have no way of proving that he does that, because unlike a reject you'll not see an "ICMP Communication Prohibited" coming back.</p><p>If I were you I'd do a simple test... open a web browser on the server, and have it connect to <a href="https://vendor.domain.com">https://vendor.domain.com</a> (or <a href="http://vendor.domain.com:443">http://vendor.domain.com:443</a>) while Wireshark is running. If you see a TCP Three Way Handshake to the vendor's IP the route working and the port is open.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '12, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14577" class="comments-container"><span id="14578"></span><div id="comment-14578" class="comment"><div id="post-14578-score" class="comment-score"></div><div class="comment-text"><p>Hello Jasper</p><p>Thanks for answering!!</p><p>I am actually fairly new to Wireshark and trying to learn best how it works :-)</p><p>I can indeed reach <a href="https://vendor.domain.com">https://vendor.domain.com</a> - but how do I see the 3 way handshake in Wireshark, what steps do I need to follow or code to enter in the bar to see this converstion only?</p></div><div id="comment-14578-info" class="comment-info"><span class="comment-age">(27 Sep '12, 15:00)</span> Harrydolan</div></div><span id="14579"></span><div id="comment-14579" class="comment"><div id="post-14579-score" class="comment-score"></div><div class="comment-text"><p>Also, how can I see if the vendor is actually Rejecting the ICMP packet, what can I look for in WS?</p></div><div id="comment-14579-info" class="comment-info"><span class="comment-age">(27 Sep '12, 15:02)</span> Harrydolan</div></div><span id="14580"></span><div id="comment-14580" class="comment"><div id="post-14580-score" class="comment-score"></div><div class="comment-text"><p>filter on the IP address of the vendor by entering "ip.addr==66.9.37.193" into the filter bar. Then take a look if you see any packet coming back to your IP. If he's rejecting your packets you might see a "ICMP destination unreachable" packet with the subtype of "communication prohibited" (which you can see if looking at the ICMP layer inside the packet).</p><p>The Three Way Handshake would be the TCP Packet sequence "SYN - SYN/ACK - ACK". Take a look at the TCP flags to see if you got any of those packets. "SYN" is your outgoing connection request, "SYN/ACK" would be the vendors "good" answer.</p></div><div id="comment-14580-info" class="comment-info"><span class="comment-age">(27 Sep '12, 15:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-14577" class="comment-tools"></div><div class="clear"></div><div id="comment-14577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

