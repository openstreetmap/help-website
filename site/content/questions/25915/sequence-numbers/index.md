+++
type = "question"
title = "sequence numbers"
description = '''hi,  ive capture a http download with: tcpdump host x.x.x.x -c 100  wireshark shows me these sequence numbers for the first 5 packets: 0 0 1 1 1   but tcpdump shows: 1636902786 1161722083 1 1:192 1   tcpdump -vvr http-download.pcap | sed &#x27;s/1.2.3.4/myprivateip/g&#x27; | head -10 reading from file http-do...'''
date = "2013-10-11T06:31:00Z"
lastmod = "2013-10-11T10:43:00Z"
weight = 25915
keywords = [ "scapy" ]
aliases = [ "/questions/25915" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [sequence numbers](/questions/25915/sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25915-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>ive capture a http download with: tcpdump host x.x.x.x -c 100</p><p>wireshark shows me these sequence numbers for the first 5 packets:</p><pre><code>0
0
1
1
1</code></pre><p>but tcpdump shows:</p><pre><code>1636902786
1161722083
1
1:192
1</code></pre><p>tcpdump -vvr http-download.pcap | sed 's/1.2.3.4/myprivateip/g' | head -10</p><pre><code>reading from file http-download.pcap, link-type EN10MB (Ethernet)
21:26:33.318368 IP (tos 0x0, ttl 64, id 64732, offset 0, flags [DF], proto TCP (6), length 60)
    myprivateip.32773 &gt; zinc.canonical.com.http: Flags [S], cksum 0xa467 (incorrect -&gt; 0x8522), seq 1636902786, win 14600, options [mss 1460,sackOK,TS val 14211934 ecr 0,nop,wscale 4], length 0
21:26:33.338102 IP (tos 0x20, ttl 48, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    zinc.canonical.com.http &gt; myprivateip.32773: Flags [S.], cksum 0x7c95 (correct), seq 1161722083, ack 1636902787, win 5792, options [mss 1460,sackOK,TS val 2713111304 ecr 14211934,nop,wscale 7], length 0
21:26:33.338119 IP (tos 0x0, ttl 64, id 64733, offset 0, flags [DF], proto TCP (6), length 52)
    myprivateip.32773 &gt; zinc.canonical.com.http: Flags [.], cksum 0xa45f (incorrect -&gt; 0xbe6b), seq 1, ack 1, win 913, options [nop,nop,TS val 14211939 ecr 2713111304], length 0
21:26:33.338252 IP (tos 0x0, ttl 64, id 64734, offset 0, flags [DF], proto TCP (6), length 243)
    myprivateip.32773 &gt; zinc.canonical.com.http: Flags [P.], cksum 0xa51e (incorrect -&gt; 0xdcad), seq 1:192, ack 1, win 913, options [nop,nop,TS val 14211939 ecr 2713111304], length 191
21:26:33.358015 IP (tos 0x20, ttl 48, id 46062, offset 0, flags [DF], proto TCP (6), length 52)
    zinc.canonical.com.http &gt; myprivateip.32773: Flags [.], cksum 0xc105 (correct), seq 1, ack 192, win 54, options [nop,nop,TS val 2713111306 ecr 14211939], length 0</code></pre><p>whats with the difference?</p><p>offtopic, but you guys probably know it anyway: ive looked at python-scapy but have had some problems, are there other good python ways to read .pcap files?</p></div><div id="question-tags" class="tags-container tags">scapy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '13, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/9adcd1030ec748b5598d4de0a374f305?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newusergreek&#39;s gravatar image" /><p>newusergreek<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newusergreek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Oct '13, 07:03</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-25915" class="comments-container"></div><div id="comment-tools-25915" class="comment-tools"></div><div class="clear"></div><div id="comment-25915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25919"></span>

<div id="answer-container-25919" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25919-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The difference is that Wireshark is set to display relative sequence numbers, which scales the sequence numbers of all conversation partners down to start at zero. If you disable relative sequence numbers in Wireshark (Edit -&gt; Preferences -&gt; Protocols -&gt; TCP -&gt; Relative Sequence Numbers) you'll see the same results as in TCPDump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '13, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25919" class="comments-container"></div><div id="comment-tools-25919" class="comment-tools"></div><div class="clear"></div><div id="comment-25919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

