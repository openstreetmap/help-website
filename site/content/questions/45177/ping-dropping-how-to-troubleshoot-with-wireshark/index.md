+++
type = "question"
title = "Ping dropping-how to troubleshoot with Wireshark?"
description = '''Hi all. This is my first experience with Wireshark. It seems quite powerful, and I hope it can help me track down my issue. I have 2 computers that I connect via a standard ethernet cable. They ping each other, and the pings connect solidly over the course of ~45 seconds. Then at that time, they fai...'''
date = "2015-08-17T15:46:00Z"
lastmod = "2015-08-17T19:15:00Z"
weight = 45177
keywords = [ "ping" ]
aliases = [ "/questions/45177" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ping dropping-how to troubleshoot with Wireshark?](/questions/45177/ping-dropping-how-to-troubleshoot-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45177-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. This is my first experience with Wireshark. It seems quite powerful, and I hope it can help me track down my issue.</p><p>I have 2 computers that I connect via a standard ethernet cable. They ping each other, and the pings connect solidly over the course of ~45 seconds. Then at that time, they fail to connect, and remain in that state permanently. I have the Wireshark output during all of this. But I don't know how to interpret the entries to troubleshoot the failed connection.</p><p>My 2 computers are:</p><p>192.168.1.5 - Desktop</p><p>192.168.1.6 - Laptop</p><p>They are the only 2 devices on my network, besides my iphone (192.168.1.4).</p><p>I'm so novice, I don't even know how to best insert Wireshark output into this post :-/ Here is the best I could do (sorry, no color coding--I'd love to learn how though). The first 2 entries are the last successful ping request/reply pair (I have omitted the previous). Then there are a bunch of entries that are unknown to me. Then the 3rd to last entry contains the first unanswered ping request.</p><pre><code>3115    533.729890000   192.168.1.5 192.168.1.6 ICMP    74  Echo (ping) request  id=0x0001, seq=540/7170, ttl=128 (reply in 3116)

3116    533.730324000   192.168.1.6 192.168.1.5 ICMP    74  Echo (ping) reply    id=0x0001, seq=540/7170, ttl=128 (request in 3115)

3117    533.731652000   D-LinkIn_47:57:3c   Broadcast   ARP 42  Who has 192.168.1.1?  Tell 192.168.1.5 (duplicate use of 192.168.1.5 detected!)

3118    533.849742000   fe80::6406:d055:d00f:b955   ff02::16    ICMPv6  90  Multicast Listener Report Message v2

3119    533.873497000   fe80::6406:d055:d00f:b955   ff02::16    ICMPv6  90  Multicast Listener Report Message v2

3120    533.875137000   fe80::6406:d055:d00f:b955   ff02::16    ICMPv6  90  Multicast Listener Report Message v2

3121    533.891959000   fe80::6406:d055:d00f:b955   ff02::16    ICMPv6  90  Multicast Listener Report Message v2

3122    533.894931000   fe80::6406:d055:d00f:b955   ff02::1:3   LLMNR   84  Standard query 0x494c  A wpad

3123    533.896001000   fe80::6406:d055:d00f:b955   ff02::1:3   LLMNR   92  Standard query 0x3b26  ANY dragonblight

3124    533.905965000   fe80::6406:d055:d00f:b955   ff02::c UDP 1054    Source port: 61731  Destination port: 3702

3125    533.994791000   fe80::6406:d055:d00f:b955   ff02::1:3   LLMNR   84  Standard query 0x494c  A wpad

3126    533.995849000   fe80::6406:d055:d00f:b955   ff02::1:3   LLMNR   92  Standard query 0x3b26  ANY dragonblight

3127    534.096998000   fe80::6406:d055:d00f:b955   ff02::c UDP 1054    Source port: 61731  Destination port: 3702

3128    534.111754000   fe80::6406:d055:d00f:b955   ff02::c SSDP    179 M-SEARCH * HTTP/1.1

3129    534.139202000   fe80::6406:d055:d00f:b955   ff02::c SSDP    181 M-SEARCH * HTTP/1.1

3130    534.254803000   D-LinkIn_47:57:3c   Broadcast   ARP 42  Who has 192.168.1.1?  Tell 192.168.1.5 (duplicate use of 192.168.1.5 detected!)

3131    534.273732000   fe80::6406:d055:d00f:b955   ff02::16    ICMPv6  90  Multicast Listener Report Message v2

3132    534.730984000   192.168.1.5 192.168.1.6 ICMP    74  Echo (ping) request  id=0x0001, seq=541/7426, ttl=128 (no response found!)

3133    535.254859000   D-LinkIn_47:57:3c   Broadcast   ARP 42  Who has 192.168.1.1?  Tell 192.168.1.5 (duplicate use of 192.168.1.5 detected!)

3134    535.895965000   fe80::6406:d055:d00f:b955   ff02::16    ICMPv6  90  Multicast Listener Report Message v2</code></pre></div><div id="question-tags" class="tags-container tags">ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '15, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/d1c1d6f926debb272b9b24b14d6c121f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cag8f&#39;s gravatar image" /><p>cag8f<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cag8f has no accepted answers">0%</span></p></div></div><div id="comments-container-45177" class="comments-container"></div><div id="comment-tools-45177" class="comment-tools"></div><div class="clear"></div><div id="comment-45177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45183"></span>

<div id="answer-container-45183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45183-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have 2 devices assigned the same IPv4 address of 192.168.1.5. See packet 3117: "duplicate use of 192.168.1.5 detected!"</p><p>This may be caused by a network element assigned a static IP address of 192.168.1.5. I assume you are using a wireless router with LAN ports. If you have access to the router, look at the associated clients before connecting your desktop to the router</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '15, 19:15</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-45183" class="comments-container"><span id="45184"></span><div id="comment-45184" class="comment"><div id="post-45184-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I saw that duplicate IP address notification. But I managed to resolve this particular issue. I set a static IP for each machine, then connected them directly via ethernet. Pings to each other connected without issue, indefinitely.</p><p>This is all however, in an attempt to troubleshoot a more overarching issue I'm having with my 2 computers. I will create a new post for that.</p><p>Thanks again.</p><p>edit: I should note that there were no other devices (that I know of) connected to this router. It is my personal router at home.</p></div><div id="comment-45184-info" class="comment-info"><span class="comment-age">(17 Aug '15, 23:13)</span> cag8f</div></div></div><div id="comment-tools-45183" class="comment-tools"></div><div class="clear"></div><div id="comment-45183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

