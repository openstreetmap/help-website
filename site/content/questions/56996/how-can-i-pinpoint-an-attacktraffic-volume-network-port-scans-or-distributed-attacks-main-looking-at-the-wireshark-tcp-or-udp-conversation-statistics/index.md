+++
type = "question"
title = "how can I pinpoint  an attack(traffic volume,   network, port scans or distributed attacks) main looking at the wireshark TCP or UDP conversation statistics"
description = '''Good Day every one  Please i have problem with understand how one can pinpoint an attack(traffic volume, network, port scans or distributed attacks) main looking at the wireshark TCP or UDP conversation statistics. Please i am a novice in this area.  Please i need answer on the significance of an at...'''
date = "2016-11-04T12:48:00Z"
lastmod = "2016-11-05T07:01:00Z"
weight = 56996
keywords = [ "traffic-flow", "packet-capture", "packet", "wireshark" ]
aliases = [ "/questions/56996" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can I pinpoint an attack(traffic volume, network, port scans or distributed attacks) main looking at the wireshark TCP or UDP conversation statistics](/questions/56996/how-can-i-pinpoint-an-attacktraffic-volume-network-port-scans-or-distributed-attacks-main-looking-at-the-wireshark-tcp-or-udp-conversation-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56996-score" class="post-score" title="current number of votes">0</div><span id="post-56996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good Day every one Please i have problem with understand how one can pinpoint an attack(traffic volume, network, port scans or distributed attacks) main looking at the wireshark TCP or UDP conversation statistics. Please i am a novice in this area. Please i need answer on the significance of an attack on TCP or UDP conversatios features and how what those feature stands for such as Packets, Bytes, port, ... etc main looking at the there statistical outputs?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic-flow" rel="tag" title="see questions tagged &#39;traffic-flow&#39;">traffic-flow</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '16, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/2684ca6915e0a949c2442e7ca10cad91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moronto&#39;s gravatar image" /><p><span>moronto</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moronto has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Nov '16, 12:49</strong> </span></p></div></div><div id="comments-container-56996" class="comments-container"></div><div id="comment-tools-56996" class="comment-tools"></div><div class="clear"></div><div id="comment-56996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57012"></span>

<div id="answer-container-57012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57012-score" class="post-score" title="current number of votes">2</div><span id="post-57012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you need this answer to investigate an ongoing attack or is this a question for some university assignment?</p><p>In case of an ongoing attack I suggest that you hire a consultant or (depending on the scale) even bring in a whole incident respone team.</p><p>Malicious traffic can manifest itself in a number of ways:</p><ul><li>Distributed Denial of Service Attacks (DDoS) can come with any type of packet.</li><li>Most efficient are unsolicited DNS and NTP responses. This would be a "reflection attack"</li><li>Other attacks use ICMP, HTTP or HTTPS traffic</li><li>Poorly written web applications can be overwhelmed with a surprisingly small number of HTTP or HTTPS requests: If a certain transaction, say a complex database query, keeps the server busy for several hundred milliseconds or longer</li><li><p>Analysis: Often DDoS attacks target one destination IP address. Look out for top receivers in the conversation statistics.</p></li><li><p>A port scan uses literally every TCP and UDP port.</p></li><li>A full port scan sends 64 k Packets TCP and UDP</li><li>Variations limit themselves to about 1'000 common services.</li><li>Another malicious operation is "OS fingerprinting". It looks similar to a port scans, but uses still less packets to identify the operating system.</li><li><p>Analysis: Find the system that is accessing a ton of different TCP and UDP ports</p></li><li><p>A good hacker who is executing a well planned attack would blend in with the routine traffic.</p></li><li>You will see "Comand and control traffic" (C2 for short) when a compromised computer receives a command or uploads stolen data.</li><li>Another part is the internal attack traffic, which often uses completely different protocols.</li><li>Both parts can be easy spot (say, an internal port scan) or very well camouflaged, if the attacker is blending in with HTTPS traffic from thousands of users.</li><li>Analysis: This requires some experience in network analysis. An Intrusion Detection System (IDS) is highly recommended. You use SNORT or SURICATA to parse the trace file and look for malicious activity.</li><li>A good start is Christian Landströms talk on APT traffic from the last Sharkfest EU conference.</li></ul><p>If you have a suspicious trace file you can probably upload it for review by someone in the community.</p><p>Good hunting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '16, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-57012" class="comments-container"></div><div id="comment-tools-57012" class="comment-tools"></div><div class="clear"></div><div id="comment-57012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

