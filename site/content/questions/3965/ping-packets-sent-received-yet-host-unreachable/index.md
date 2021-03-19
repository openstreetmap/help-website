+++
type = "question"
title = "Ping Packets Sent &amp; Received Yet Host Unreachable"
description = '''We have a monitoring system on our Windows 7 Ultimate ( 64 bit, SP 1 ) that pings 1000+ IPs every 30 seconds to record latency and &quot;uptime&quot;. I have 3 IPs so far that work on every other connection/computer I try. I have verified firewall ( hardware ) is doing everything properly. I am able to ping t...'''
date = "2011-05-05T15:21:00Z"
lastmod = "2011-05-10T15:40:00Z"
weight = 3965
keywords = [ "unreachable", "windows7", "icmp", "ping", "reply" ]
aliases = [ "/questions/3965" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ping Packets Sent & Received Yet Host Unreachable](/questions/3965/ping-packets-sent-received-yet-host-unreachable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3965-score" class="post-score" title="current number of votes">0</div><span id="post-3965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a monitoring system on our Windows 7 Ultimate ( 64 bit, SP 1 ) that pings 1000+ IPs every 30 seconds to record latency and "uptime". I have 3 IPs so far that work on every other connection/computer I try.</p><p>I have verified firewall ( hardware ) is doing everything properly. I am able to ping the same IPs from another server we have at the same location. I have tried pinging with the software firewall turned off and the anti-virus program off and no effect. I have rebooted twice ( before and after the most recent updated for windows ), both times I have been able to ping those IPs for probably about 10+ minutes and then I get host unreachable from then on.</p><p>I started using Wireshark to packet sniff and I see the ping packet is getting a reply, which is very odd. Obviously the host is reachable because the ping packet reply came back in. So the question is what is causing the ping ICMP packet to report as unreachable. Anyone have any ideas?</p><p>I changed the IP to xx.xx in the example below as well as the reply packet.</p><pre><code>/// Ping Packet ( Sent / Received )

29  0.071804    192.168.2.112   64.105.xx.xx    ICMP    Echo (ping) request  (id=0x0018, seq(be/le)=2829/3339, ttl=128)
44  0.143773    64.105.xx.xx    192.168.2.112   ICMP    Echo (ping) reply    (id=0x0008, seq(be/le)=2829/3339, ttl=51)

// Reply Packet

0000  00 30 48 b9 80 5b 00 06  b1 0e 7a 44 08 00 45 00   .0H..[.. ..zD..E.
0010  00 3c da e7 00 00 33 01  76 0f 40 69 xx xx c0 a8   .&lt;....3. [email protected]
0020  02 70 00 00 4a 47 00 08  0b 0d 61 62 63 64 65 66   .p..JG.. ..abcdef
0030  67 68 69 6a 6b 6c 6d 6e  6f 70 71 72 73 74 75 76   ghijklmn opqrstuv
0040  77 61 62 63 64 65 66 67  68 69                     wabcdefg hi</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unreachable" rel="tag" title="see questions tagged &#39;unreachable&#39;">unreachable</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-reply" rel="tag" title="see questions tagged &#39;reply&#39;">reply</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '11, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/7e14877c9ce981e9c7f2c861abf88c93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolfjlupus&#39;s gravatar image" /><p><span>wolfjlupus</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolfjlupus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 May '11, 15:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-3965" class="comments-container"></div><div id="comment-tools-3965" class="comment-tools"></div><div class="clear"></div><div id="comment-3965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3967"></span>

<div id="answer-container-3967" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3967-score" class="post-score" title="current number of votes">4</div><span id="post-3967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wolfjlupus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ICMP ID's are not the same. So the PING program will not match the response to the request. It looks like a device between 192.168.2.112 and 64.105.xx.xx is messing up the ICMP ID's. Is there a NAT device in place between those hosts? Maybe it's tables are not large enough to translate that many ICMP packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '11, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3967" class="comments-container"><span id="4024"></span><div id="comment-4024" class="comment"><div id="post-4024-score" class="comment-score"></div><div class="comment-text"><p>Thank you Synbit, further packet sniffing at the firewall level shows it is the Sonicwall doing improper NATing even though it's set up properly. Once I removed the outbound NAT policy for it's specific IP it started working. The Sonicwall probably needs to be factory reset as it's pretty old and has been running for a long time.</p></div><div id="comment-4024-info" class="comment-info"><span class="comment-age">(10 May '11, 15:40)</span> <span class="comment-user userinfo">wolfjlupus</span></div></div></div><div id="comment-tools-3967" class="comment-tools"></div><div class="clear"></div><div id="comment-3967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

