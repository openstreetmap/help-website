+++
type = "question"
title = "Slowdown in receiving data"
description = '''I&#x27;ve written a simple Windows client that connects to a hardware device (FPGA) over TCP/IP. When I click a button in the client it sends a small &quot;request&quot; to the device, then reads a response that the device returns - this data is approx 32kb in size. My code typically takes 2-3ms to read this respo...'''
date = "2016-01-29T01:10:00Z"
lastmod = "2016-01-29T01:10:00Z"
weight = 49618
keywords = [ "ack", "tcp" ]
aliases = [ "/questions/49618" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slowdown in receiving data](/questions/49618/slowdown-in-receiving-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49618-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a simple Windows client that connects to a hardware device (FPGA) over TCP/IP. When I click a button in the client it sends a small "request" to the device, then reads a response that the device returns - this data is approx 32kb in size.</p><p>My code typically takes 2-3ms to read this response back, and this timing remains consistent if I repeatedly click the button slowly (e.g. once per second). However if I start clicking the button more rapidly (e.g. every half a second) then after a few seconds the timings will drop to around 12ms and remain at that level, even if I go back to clicking the button slowly. If I close then reopen the connection on the client, then try again, it goes back to 2-3ms times.</p><p>Here are a couple of Wireshark screenshots - the first being a "fast" one, the second from when it has slowed down. The only thing that jumps out at me is the increased number of ACKs in the second screenshot. Any toughts? I'm a software dev so this sort of thing is out of my depth TBH!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ws1_BYOxtEZ.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/ws2_sDPKtuR.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '16, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/89bfbacc849835ca831d84ae6bd014aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andyste1&#39;s gravatar image" /><p>andyste1<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andyste1 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-49618" class="comments-container"><span id="49619"></span><div id="comment-49619" class="comment"><div id="post-49619-score" class="comment-score"></div><div class="comment-text"><p>If you can, post examples on <a href="https://www.cloudshark.org/">https://www.cloudshark.org/</a> instead of screenshots. Analyzing TCP behavior with screenshots is much more time consuming and sometimes not possible at all (depending on the screenshot).</p><p>If you worry about privacy, use TraceWrangler (<a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a>) to randomize all IP addresses and remove the TCP payload (verify it looks good before uploading, "good" meaning IPs are different and the packets have no TCP payload anymore).</p><p>Make sure that you include the TCP handshake, pls, because your screenshots start somewhere in the middle. It's often critical to know details that can be read from the first three packets (SYN - SYN/ACK - ACK), e.g. timings, TCP options, etc.</p></div><div id="comment-49619-info" class="comment-info"><span class="comment-age">(29 Jan '16, 01:21)</span> Jasper ♦♦</div></div></div><div id="comment-tools-49618" class="comment-tools"></div><div class="clear"></div><div id="comment-49618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

