+++
type = "question"
title = "SYN, then Retransmission, then RSTACK"
description = '''Hello people, I have a strange issue. I have an apche mod_proxying an application server. It works, but at any time randomly I get a connection refused from the server resulting a 503 to the user. It doesn&#x27;t matter the traffic size, it can happen with 1 user too with just a request to a page. It hap...'''
date = "2013-09-17T15:25:00Z"
lastmod = "2013-09-18T16:03:00Z"
weight = 24870
keywords = [ "retransmissions", "rst+ack" ]
aliases = [ "/questions/24870" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SYN, then Retransmission, then RSTACK](/questions/24870/syn-then-retransmission-then-rstack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello people, I have a strange issue. I have an apche mod_proxying an application server. It works, but at any time randomly I get a connection refused from the server resulting a 503 to the user. It doesn't matter the traffic size, it can happen with 1 user too with just a request to a page. It happens like one request every 10000.</p><p>Wiresharking from the client I see the following, I send a SYN, then a TCP Retransmission after 3 seconds, and suddenly RST,ACK.</p><pre><code>694839  88.387936   10.10.1.1   10.10.65.65 TCP 74  50854 &gt; http-alt [SYN] Seq=0 Win=5840 Len=0 MSS=1460 SACK_PERM=1 TSval=2254806118 TSecr=0 WS=128
717344  91.387571   10.10.1.1   10.10.65.65 TCP 74  [TCP Retransmission] 50854 &gt; http-alt [SYN] Seq=0 Win=5840 Len=0 MSS=1460 SACK_PERM=1 TSval=2254809118 TSecr=0 WS=128
744094  95.079609   10.10.65.65 10.10.1.1   TCP 60  http-alt &gt; 50854 [RST, ACK] Seq=1 Ack=1 Win=5840 Len=0</code></pre><p>From the server, there is no connection seen. There is a firewall in the middle separating dmz from private network. Supposedly that firewall doesn't filter packets, just let it through. The application server is working fine. OS doesn't show transmission error. It doesn't occur on full GC. Can anybody give me a hint what else can I look? Thank you.</p></div><div id="question-tags" class="tags-container tags">retransmissions rst+ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/e0adae41d0b0d2401a132a02304a20dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Meli&#39;s gravatar image" /><p>Meli<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Meli has no accepted answers">0%</span></p></div></div><div id="comments-container-24870" class="comments-container"><span id="24874"></span><div id="comment-24874" class="comment"><div id="post-24874-score" class="comment-score"></div><div class="comment-text"><p>Can you provide the actual packet capture including the full TCP headers of these messages (<a href="http://www.cloudshark.org/)?">http://www.cloudshark.org/)?</a> Also can you capture between the server and the firewall? Firewall in between always makes me suspicious, especially with a client-side capture (where the RSTs are not necessarily originated from the server). It's possible some kind of logic on the firewall (application-layer rules, or even session limiting) could be causing this. It is odd to see one not responded to and an RST to the other, though.</p></div><div id="comment-24874-info" class="comment-info"><span class="comment-age">(17 Sep '13, 18:49)</span> Quadratic</div></div><span id="24923"></span><div id="comment-24923" class="comment"><div id="post-24923-score" class="comment-score"></div><div class="comment-text"><p>I'll try to cut/filter and post it, the file is huge. We capture the server tcp too, in that moment we should see an incoming connection with port 50854 but we couldn't find it. As I read, a retransmission would continue 3, 6, etc, seconds, and we don't see a pattern either because of the reset. Me mitigate this issue by decreasing the retry=0 in the mod_proxy, but it's not the solution. However, once in a while a 503 still occurs.</p></div><div id="comment-24923-info" class="comment-info"><span class="comment-age">(18 Sep '13, 08:46)</span> Meli</div></div></div><div id="comment-tools-24870" class="comment-tools"></div><div class="clear"></div><div id="comment-24870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24929"></span>

<div id="answer-container-24929" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24929-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If someone have this problem, be sure to check the ethernet, not only ram, cpu, ulimit, tcp values. In our case we missed ifconfig, as networking guys said they didn't see anything strange. However, surprise! we found RX error in frames which are CRC failure due to something wrong with the network interface. Thank you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/e0adae41d0b0d2401a132a02304a20dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Meli&#39;s gravatar image" /><p>Meli<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Meli has no accepted answers">0%</span></p></div></div><div id="comments-container-24929" class="comments-container"></div><div id="comment-tools-24929" class="comment-tools"></div><div class="clear"></div><div id="comment-24929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

