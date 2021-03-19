+++
type = "question"
title = "Ping id doesn&#x27;t match"
description = '''Have any of you seen situations where the id in a ping reply does not match the id in the request? We&#x27;ve seen 4 occurrences this year. This is likely a Windows 7 bug but if it was ever seen I think it would be by this audience. The only web hit I found was one item about Windows 2000 back in 2003, a...'''
date = "2015-09-14T08:56:00Z"
lastmod = "2015-09-14T12:51:00Z"
weight = 45828
keywords = [ "ics", "ping" ]
aliases = [ "/questions/45828" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ping id doesn't match](/questions/45828/ping-id-doesnt-match)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45828-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have any of you seen situations where the id in a ping reply does not match the id in the request? We've seen 4 occurrences this year. This is likely a Windows 7 bug but if it was ever seen I think it would be by this audience. The only web hit I found was one item about Windows 2000 back in 2003, and it didn't apply to our systems.</p><p>199 19.483937 10.234.10.113 10.234.10.25 ICMP 74 Echo (ping) request id=0x0001, seq=242/61952, ttl=128 200 19.484187 10.234.10.25 10.234.10.113 ICMP 74 Echo (ping) reply id=0x0100, seq=242/61952, ttl=128</p><p>When it occurs, it persists, but only between those two computers and only in one direction. The pinger can ping other systems fine, and the pingee can be pinged by other systems fine. The pingee can ping the pinger fine. Changing cabling, even eliminating routers and going direct, makes no difference. Nor does changing IP addresses. Nor does rebooting. It's been seen with different Ethernet hardware. The only solution we've found is to reload from the OS up. Capture on both sides simultaneously shows that it is the pingee changing the id at some level outside of wireshark.</p><p>It causes our software to think that the pingee is unreachable. The .NET Ping class must be comparing ids, which seems correct to me.</p><p>It has happened with both 32-bit and 64-bit pingees.</p><p>A capture and my notes which points squarely at Internet Connection Sharing as the culprit. <a href="https://www.cloudshark.org/captures/4fadc0835230">https://www.cloudshark.org/captures/4fadc0835230</a></p><p>Any Microsofties around who can look at the code?</p></div><div id="question-tags" class="tags-container tags">ics ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '15, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/b3a36a856efb60f32f8d059c184a4102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lordbah&#39;s gravatar image" /><p>lordbah<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lordbah has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Sep '15, 08:28</p></div></div><div id="comments-container-45828" class="comments-container"></div><div id="comment-tools-45828" class="comment-tools"></div><div class="clear"></div><div id="comment-45828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45832"></span>

<div id="answer-container-45832" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45832-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Notice that the reply ID, 0x0100, is exactly what you'd get if you reversed the two bytes of the request ID, 0x0001. I'd check the whole trace to see if that's always true: Whenever the IDs don't match, the bytes are reversed. If so, then it appears that there is some sort of bug on the reply system relating to network byte order. Wireshark will show you the ICMP Identifier field both ways in the Packet Details pane.</p><p>In any case, this shouldn't be happening, so if these packets are correctly identified and the packet with ID 0x0100 really is a response to the ping with ID 0x0001, then there's probably nothing you can do unless the OS vendor already knows about this and has come up with a patch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '15, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-45832" class="comments-container"><span id="45833"></span><div id="comment-45833" class="comment"><div id="post-45833-score" class="comment-score"></div><div class="comment-text"><p>I did notice that. Initially I thought maybe it only occurred when 32-bit was pinging 64-bit, but later it happened with 32-to-32. When it is mismatched, it is always swapped like that in every reply to requests from that one requester, but the value is always 0001 from Win7 so there's not a wide range of examples. The really strange part is that when it gets this way, it'll only do it for replies to one pinger - other pingers get a non-swapped (i.e. correct) id in reply.</p><p>Based on sequence number matching and timing I believe it really is the matching reply.</p></div><div id="comment-45833-info" class="comment-info"><span class="comment-age">(14 Sep '15, 13:08)</span> lordbah</div></div><span id="46259"></span><div id="comment-46259" class="comment"><div id="post-46259-score" class="comment-score"></div><div class="comment-text"><p>Found a similar question at <a href="https://ask.wireshark.org/questions/3965/ping-packets-sent-received-yet-host-unreachable">https://ask.wireshark.org/questions/3965/ping-packets-sent-received-yet-host-unreachable</a></p><p>In my case the NAT is being done by Windows Internet Connection Sharing. If the issue is the size of a table which maps ICMP ids, does anyone know how to change that size in ICS?</p></div><div id="comment-46259-info" class="comment-info"><span class="comment-age">(29 Sep '15, 08:18)</span> lordbah</div></div></div><div id="comment-tools-45832" class="comment-tools"></div><div class="clear"></div><div id="comment-45832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

