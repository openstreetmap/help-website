+++
type = "question"
title = "Convert TCP streams only to pcap (or any Wireshark compatible format)"
description = '''I&#x27;m writing a network application, and would like to add the ability for it to save all of its own sent/received data to disk. By itself, the problem is simple, I could just invent a file format that stores sent/received packets along with timestamps and network addresses... but I would like to use ...'''
date = "2015-09-09T04:36:00Z"
lastmod = "2015-09-09T06:54:00Z"
weight = 45735
keywords = [ "file-format", "tcp_stream" ]
aliases = [ "/questions/45735" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Convert TCP streams only to pcap (or any Wireshark compatible format)](/questions/45735/convert-tcp-streams-only-to-pcap-or-any-wireshark-compatible-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45735-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a network application, and would like to add the ability for it to save all of <em>its own</em> sent/received data to disk. By itself, the problem is simple, I could just invent a file format that stores sent/received packets along with timestamps and network addresses... but I would like to use a format that's compatible with Wireshark, so I can use it to inspect the captures. I know I could also use libpcap and record a real packet capture, but I'd like to avoid the dependency + root privilege / system configuration requirement.</p><p>The problem with using formats such as pcap in this case is that these formats store the packets in their entirety, including Ethernet, IP and TCP headers. On the application level, I do not have this information - only data received by recv() and sent by send(). Writing .pcap files would mean faking Ethernet/IP/TCP headers, as well as TCP handshakes etc.</p><p>So, what's the easiest way to write a Wireshark-compatible format (or a format convertible to it) from <em>within</em> a network application?</p></div><div id="question-tags" class="tags-container tags">file-format tcp_stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '15, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/7fb5115cde6961cfaa7433d2a8228599?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CyberShadow&#39;s gravatar image" /><p>CyberShadow<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CyberShadow has one accepted answer">100%</span></p></div></div><div id="comments-container-45735" class="comments-container"></div><div id="comment-tools-45735" class="comment-tools"></div><div class="clear"></div><div id="comment-45735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45738"></span>

<div id="answer-container-45738" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45738-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Figured out a way - use text2pcap:</p><p>First, save or convert your captured data to the following text format (one file per connection / TCP stream):</p><p><code>O 2015-09-09 00:00:00.000001 00000000 01 02 03 04 05 I 2015-09-09 00:00:00.000002 00000000 01 02 03 04 05 O 2015-09-09 00:00:00.000003 00000000 02 03 04 05 06 I 2015-09-09 00:00:00.000004 00000000 02 03 04 05 06</code></p><p>Then, run:</p><p><code>text2pcap -t "%Y-%m-%d %H:%M:%S." -T 55555,1234 -4 127.0.0.1,1.2.3.4 -D -n input.txt output.pcapng</code></p><p>Replace ports and IPs with the real ones as appropriate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '15, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/7fb5115cde6961cfaa7433d2a8228599?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CyberShadow&#39;s gravatar image" /><p>CyberShadow<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CyberShadow has one accepted answer">100%</span></p></div></div><div id="comments-container-45738" class="comments-container"></div><div id="comment-tools-45738" class="comment-tools"></div><div class="clear"></div><div id="comment-45738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

