+++
type = "question"
title = "tcp retransmission vs tcp port numbers reused"
description = '''Hi, I&#x27;m currently debugging an issue where HTTP and HTTPs requests are sent to the switch web server using a wget script from crontab every minute from a workstation. After 1-2 hours the switch resets it self(reboots). When connecting wire shark i see alot of TCP re transmission requests just before...'''
date = "2015-06-19T04:36:00Z"
lastmod = "2015-06-19T13:26:00Z"
weight = 43360
keywords = [ "switch", "http", "https", "tcp" ]
aliases = [ "/questions/43360" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp retransmission vs tcp port numbers reused](/questions/43360/tcp-retransmission-vs-tcp-port-numbers-reused)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43360-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm currently debugging an issue where HTTP and HTTPs requests are sent to the switch web server using a wget script from crontab every minute from a workstation. After 1-2 hours the switch resets it self(reboots). When connecting wire shark i see alot of TCP re transmission requests just before the switch loses its ip hangs and resets. I also see alot of ARP request in the wire shark asking to resolve the switch ip when the switch hangs.</p><p>In the older builds this issue isn't present. I ran this test similarly on the same switch with an older build. The switch does not reset it self and in the wire shark logs i see 'tcp port numbers reused'.</p><p>Is this an area to suspect as to why the switch resets itself?</p></div><div id="question-tags" class="tags-container tags">switch http https tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/bff2683f6bd6c90d241cdac0f6482546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V_A&#39;s gravatar image" /><p>V_A<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V_A has no accepted answers">0%</span></p></div></div><div id="comments-container-43360" class="comments-container"><span id="43362"></span><div id="comment-43362" class="comment"><div id="post-43362-score" class="comment-score"></div><div class="comment-text"><p>Older builds of what, Wireshark?</p><p>What version(s) of Wireshark are you using, and where in the network are you making the captures? A diagram of the network would help, along with a capture file exhibiting the problem. Use <a href="https://www.tracewrangler.com/">TraceWrangler</a> to anonymise the capture if you need to.</p></div><div id="comment-43362-info" class="comment-info"><span class="comment-age">(19 Jun '15, 05:13)</span> grahamb ♦</div></div><span id="43365"></span><div id="comment-43365" class="comment"><div id="post-43365-score" class="comment-score"></div><div class="comment-text"><p>older builds of the switch software, i'm using wire shark 1.8.10, ill upload both captures. The topology looks like:</p><p>wireshark on linux box ----switch---dhcp server</p><p>How do i upload the capture?</p></div><div id="comment-43365-info" class="comment-info"><span class="comment-age">(19 Jun '15, 05:31)</span> V_A</div></div><span id="43384"></span><div id="comment-43384" class="comment"><div id="post-43384-score" class="comment-score"></div><div class="comment-text"><p>YOu can use cloudshark at <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a></p></div><div id="comment-43384-info" class="comment-info"><span class="comment-age">(19 Jun '15, 12:47)</span> mrEEde</div></div><span id="43436"></span><div id="comment-43436" class="comment"><div id="post-43436-score" class="comment-score"></div><div class="comment-text"><p>I tried uploading the capture, but my files are 8MB in size. I'll capture again and try with smaller files..</p></div><div id="comment-43436-info" class="comment-info"><span class="comment-age">(22 Jun '15, 04:49)</span> V_A</div></div></div><div id="comment-tools-43360" class="comment-tools"></div><div class="clear"></div><div id="comment-43360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43385"></span>

<div id="answer-container-43385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43385-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this an area to suspect as to why the switch resets itself?</p></blockquote><p>sounds like a firmware bug that's triggered by</p><ul><li>the number of frames (counter overflow)</li><li>a byte pattern in the traffic</li><li>too high temperature</li><li>anything else you can imagine</li></ul><p>I would be surprised we you would see the reason for this in the capture file. I would rather suggest to enable debug logging in the switch and monitor that via the serial console.</p><blockquote><p>When connecting wire shark i see a lot of TCP re transmission requests just before the switch loses its ip hangs and resets.</p></blockquote><p>That's (most certainly) because the switch has already stopped forwarding frames a few seconds before it reboots.</p><blockquote><p>I also see a lot of ARP request in the wire shark asking to resolve the switch ip when the switch hangs.</p></blockquote><p>Strange. Who asked for the switch MAC/IP?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '15, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jun '15, 13:27</p></div></div><div id="comments-container-43385" class="comments-container"><span id="43435"></span><div id="comment-43435" class="comment"><div id="post-43435-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your inputs.</p><p>Since the switch resets, there is no crash data or logs saved. One error message i observed when connecting the debugger was this:</p><pre><code>I/O: [err] evsignal_init: socketpair: Too many open files</code></pre><p><code></code></p><code></code><p><code></code></p><p><code></code></p><p>would the switch reset because there were many tcp connections? Is that plausible?</p><p>ARP requests was coming from the IP of the linux box connected to the switch, which was sending the http/https requests. where should i start debugging?</p></div><div id="comment-43435-info" class="comment-info"><span class="comment-age">(22 Jun '15, 04:47)</span> V_A</div></div></div><div id="comment-tools-43385" class="comment-tools"></div><div class="clear"></div><div id="comment-43385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

