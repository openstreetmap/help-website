+++
type = "question"
title = "Capturing at two interfaces with distinct capture filters to debug NAT with port forwarding"
description = '''I would like to capture traffic between two interfaces to debug NAT with port forwarding on a Windows Server 2012 R2, which shall translate requests to TCP port 817[0..9] on the &quot;internet&quot; interface (IP 192.168.88.252, behind another NAT router board) to TCP ports 80 on devices (IP 192.168.0.17[0..9...'''
date = "2016-08-22T02:39:00Z"
lastmod = "2016-08-22T03:30:00Z"
weight = 55038
keywords = [ "filter", "multiple-interfaces", "port-forwarding", "nat" ]
aliases = [ "/questions/55038" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing at two interfaces with distinct capture filters to debug NAT with port forwarding](/questions/55038/capturing-at-two-interfaces-with-distinct-capture-filters-to-debug-nat-with-port-forwarding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55038-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to capture traffic between two interfaces to debug NAT with port forwarding on a Windows Server 2012 R2, which shall translate requests to TCP port 8<strong>17</strong>[0..9] on the "internet" interface (IP 192.168.88.252, behind another NAT router board) to TCP ports 80 on devices (IP 192.168.0.<strong>17</strong>[0..9]) connected to the "intranet" interface (IP 192.168.0.1).</p><p>Currently, requests over the internet in a web browser using an URL with port number (e.g. "http://<em>dynamic.dns</em>:8171") return a "connection refused" error, so I have to suspect that the port forwarding in the Windows Server was not configured correctly, and I hope that a multi-interface capture with a narrow filter would help discovering where and why the connection fails.</p><p>Capturing the "internet" interface alone already proved that requests from the internet through a router board arrive in the server, so the "transparent" port forwarding in the router board (same port pass-through for the given range) appears to be correct...</p><p>How do I set up WireShark 2.0.5(+) x86-64 to capture two interfaces at once, and select filters per interface (a port range for the "internet" interface, an IP address range for the "intranet" interface)?</p></div><div id="question-tags" class="tags-container tags">filter multiple-interfaces port-forwarding nat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '16, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/552129d4e02e7b2b326bcc9d1bdfc467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LigH&#39;s gravatar image" /><p>LigH<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LigH has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Aug '16, 04:52</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55038" class="comments-container"></div><div id="comment-tools-55038" class="comment-tools"></div><div class="clear"></div><div id="comment-55038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55039"></span>

<div id="answer-container-55039" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55039-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>At the welcome screen, click once at one of the interfaces, and fill in the capture filter form field with the filter expression for the interface currently chosen.</p><p>Then, click once at the other interface you want to capture at, and fill in the same capture filter form field with the filter expression for that interface.</p><p>Next, hold Ctrl and click once the first interface. Both will become selected (and highlighted accordingly). Don't touch the capture filter form field, and press the "start capture" button (the blue fin symbol right below <code>File</code> in the upper left corner). Double-clicking on one of the interfaces is also possible but requires a special sequence of Ctrl and click.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '16, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55039" class="comments-container"><span id="55040"></span><div id="comment-55040" class="comment"><div id="post-55040-score" class="comment-score"></div><div class="comment-text"><p>You can also use the Capture Options dialog to set per interface filter expressions and then capture on multiple interfaces.</p></div><div id="comment-55040-info" class="comment-info"><span class="comment-age">(22 Aug '16, 03:40)</span> grahamb ♦</div></div><span id="55041"></span><div id="comment-55041" class="comment"><div id="post-55041-score" class="comment-score"></div><div class="comment-text"><p>Thank you, sindy, that worked well so far. And unfortunately, it shows that the port forwarding does not happen inside the Windows Server, so this is a useful anchor for the following countermeasures.</p><p>I just hope there is a more efficient filter than a sequence of single hosts when an IP range does not easily match a subnet mask (host 192.168.0.170 or host 192.168.0.171 or [...] or host 192.168.0.179).</p></div><div id="comment-55041-info" class="comment-info"><span class="comment-age">(22 Aug '16, 04:02)</span> LigH</div></div><span id="55042"></span><div id="comment-55042" class="comment"><div id="post-55042-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, your hope is in vain. If you insist that the filtering is done using a <strong>capture</strong> filter, the answer to <a href="https://ask.wireshark.org/questions/53965/struggling-to-get-correct-answer-ip-range">this Question</a> provides all the details.</p><p>But if you could live with a <strong>display</strong> filter further narrowing the packet list, the answer to <a href="https://ask.wireshark.org/questions/54517/what-is-the-display-filter-syntax-to-specify-an-ip-subnet">this Question</a> may be helpful.</p></div><div id="comment-55042-info" class="comment-info"><span class="comment-age">(22 Aug '16, 04:16)</span> sindy</div></div><span id="55043"></span><div id="comment-55043" class="comment"><div id="post-55043-score" class="comment-score"></div><div class="comment-text"><p>By using some CIDR ranges with the <code>net</code> primitive you could use a filter of:</p><pre><code>host 192.168.0.170 or host 192.168.1.171 or net 192.168.1.172/30 or net 192.168.1.176/30</code></pre><p>If you don't mind .168 &amp; .169 being included, then you could use:</p><pre><code>net 192.168.1.168/29 or net 192.168.1.176/30</code></pre></div><div id="comment-55043-info" class="comment-info"><span class="comment-age">(22 Aug '16, 04:20)</span> grahamb ♦</div></div></div><div id="comment-tools-55039" class="comment-tools"></div><div class="clear"></div><div id="comment-55039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

