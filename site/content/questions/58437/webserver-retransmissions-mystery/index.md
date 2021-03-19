+++
type = "question"
title = "Webserver Retransmissions mystery"
description = '''We have a public facing website that runs on a platform with Apache Web Server + Application Firewall (Imperva) + App Server (Sybase EAServer). This is in production and it&#x27;s been running fine. But, recently when a developer made some changes, the pages started loading slo...w. First we blamed it on...'''
date = "2016-12-30T16:42:00Z"
lastmod = "2016-12-31T09:26:00Z"
weight = 58437
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/58437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Webserver Retransmissions mystery](/questions/58437/webserver-retransmissions-mystery)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a public facing website that runs on a platform with Apache Web Server + Application Firewall (Imperva) + App Server (Sybase EAServer). This is in production and it's been running fine. But, recently when a developer made some changes, the pages started loading slo...w. First we blamed it on new Bootstrap libraries used.</p><p>To make matters more puzzling, this page and images loaded fine on cell phones. (Later we realized, it may have to do with file size.. Does cell phones received reduced image size?). I may be wrong, but the slowness seems to be more severe on Windows clients.</p><p>We were able to reproduce in test and after some testing, I narrowed it down an image and further testing revealed, the slowness was due to any file (JPG, PNG, CSS, JS) above 20 - 30K in size.</p><p>At this point, I tested the same file with SFTP with the same results. So, the nature of the problem turned out to be, as simple as, Downloading files &gt; 20k was slow and Uploads were fine.</p><p>One particular image file, 79k in size, would load half way through in browser and stall for up to 2 minutes to complete. Another (71k) would blur for 2 minutes to develop.</p><p>I put Wireshark on the client side (I don't have rights on server) to see there were a lot of packet Retransmissions and/or DUP ACK in the trace.</p><p>Few additional tests (excluding Imperva altogether) revealed imperva server is adding that delay. We checled, that there is no Firewall rule causing this, as the file is finally let through.</p><p>Webserver on Debian Linux, Imperva appliance uses Centos and App server on Win 2k8.</p><p>I am currently looking at solving it by tuning TCP settings, but I am not all that familiar with it. I can work with the admins to change the settings as needed. I am seeking any advice or tips from the experts here. Thanks in advance. (So far, I've tried, TCP window scaling, sack etc and nothing seem to help).</p><p>If it will be of any help, I am attaching <a href="http://pastebin.com/mGT4yEiK">here</a>, a flow graph export from wireshark, for the download of an image in browser (HTTPS)</p></div><div id="question-tags" class="tags-container tags">retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '16, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/5c6ab73c1cbc9cc9bf032fe9115f88b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kanishqa&#39;s gravatar image" /><p>kanishqa<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kanishqa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Dec '16, 17:03</p></div></div><div id="comments-container-58437" class="comments-container"></div><div id="comment-tools-58437" class="comment-tools"></div><div class="clear"></div><div id="comment-58437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58443"></span>

<div id="answer-container-58443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58443-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Kanishqa, and welcome to ask.wireshark.org</p><p>A first glance reveals a few retransmissions, which most certainly cause delay. The connection(s) start with a round trip time (RTT) of 2 msec. A bit later we see packets marked as "Retransmission" coming in with a delay of 400 msec or more. A good start could be switch counters and port status to identify full duplex / half duplex mismatch (that is, if 100 MBit links are involved).</p><p>To identify the exact source of the packet loss it might be useful to capture packets either using SPAN ports, maybe even taps.</p><p>It would be most useful, if you could provide a tracefile. If you worry about private data (even, if the traffic is encrypted), you can clean with the TraceWrangler, which is available for free at <a href="https://www.tracewrangler.com"></a><a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '16, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-58443" class="comments-container"><span id="58444"></span><div id="comment-58444" class="comment"><div id="post-58444-score" class="comment-score"></div><div class="comment-text"><p>@PacketHunter,</p><p>Thanks for taking the time and for the detailed response. That's the best answer I have gotten so far. For the last week or so, we have been running around, blaming everything under the sun :). Thankfully, we have been able to narrow down to download only. Is that what led you to think, it's a duplex issue?</p><p>Our network team said, switches were ok, but I will show them your answer next week. Hopefully, they will be able to figure out. To capture packets like you mentioned, can Wireshark do it?</p><p>I am a developer who happened to be in this spot to find a solution for the problem that started as a programming issue :). But, I am eager to learn. Is there any link or diagram you can share, to get me started on this topic, so I can be ready to discuss with the network team?</p><p>I will post the trace file and any other findings shortly.</p><p>Happy New Year!</p><p>Sam</p></div><div id="comment-58444-info" class="comment-info"><span class="comment-age">(31 Dec '16, 10:41)</span> kanishqa</div></div><span id="58445"></span><div id="comment-58445" class="comment"><div id="post-58445-score" class="comment-score">1</div><div class="comment-text"><p>Hi Sam / Kanishqa</p><p>A good start is the web site <a href="https://blog.packet-foo.com">https://blog.packet-foo.com</a>. Check out the network capture playbook. By the way, the FDX/HDX issue (that's full duplex / half duplex) would only appear on 10 or 100 MBit Ethernet. Make sure to check both the settings on the end-systems and servers.</p><p>Happy new year and good hunting.</p></div><div id="comment-58445-info" class="comment-info"><span class="comment-age">(31 Dec '16, 12:27)</span> packethunter</div></div></div><div id="comment-tools-58443" class="comment-tools"></div><div class="clear"></div><div id="comment-58443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

