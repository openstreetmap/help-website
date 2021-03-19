+++
type = "question"
title = "Help understand wireshark log"
description = '''Hello, I´m new wireshark. I have a IPSEC VPN with a client. Now I need to access the 398 port of his server, but it´s not working. My ip : 172.16.30.2 Client ip: 10.2.1.133 I type on cmd : “telnet 10.2.1.133 398” and got the error below Connecting To 10.2.1.133...Could not open connection to the hos...'''
date = "2016-07-28T11:24:00Z"
lastmod = "2016-07-30T17:26:00Z"
weight = 54412
keywords = [ "wireshark" ]
aliases = [ "/questions/54412" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help understand wireshark log](/questions/54412/help-understand-wireshark-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54412-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I´m new wireshark.</p><p>I have a IPSEC VPN with a client. Now I need to access the 398 port of his server, but it´s not working.</p><p>My ip : 172.16.30.2<br />
Client ip: 10.2.1.133</p><p>I type on cmd : “telnet 10.2.1.133 398” and got the error below</p><p>Connecting To 10.2.1.133...Could not open connection to the host, on port 398 : Connect failed.</p><p>So I´ve ran wireshark with filter <code>tcp.port == 398</code></p><pre><code>176 2.092776 172.16.30.2 10.2.1.133 TCP 66 51166 &amp;#8594; 398 [SYN, ECN, CWR] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
247 5.088552 172.16.30.2 10.2.1.133 TCP 66 [TCP Retransmission] 51166 &amp;#8594; 398 [SYN, ECN, CWR] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
401 11.096685 172.16.30.2 10.2.1.133 TCP 62 [TCP Retransmission] 51166 &amp;#8594; 398 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1</code></pre><p>Bad tcp = black line</p><p>I´ve understood that my computer (172.16.30.2) ask a conection [SYN, ECN, CWR], but the other side didn´t answer, so is the problem client?<br />
</p><p>Is it possible to know if the other site got my packet?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/fb8b07b9533757b66d91248c52896bda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fabiomoraes055&#39;s gravatar image" /><p>fabiomoraes055<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fabiomoraes055 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jul '16, 07:45</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-54412" class="comments-container"></div><div id="comment-tools-54412" class="comment-tools"></div><div class="clear"></div><div id="comment-54412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54413"></span>

<div id="answer-container-54413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54413-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to know if the other site got my packet?</p></blockquote><p>If someone at their end can run Wireshark or tcpdump, then yes.</p><blockquote><p>the other side didn´t answer</p></blockquote><p>Or it has answered but the answer never got back to your PC, possibly due to routing misconfiguration on their side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '16, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54413" class="comments-container"></div><div id="comment-tools-54413" class="comment-tools"></div><div class="clear"></div><div id="comment-54413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54464"></span>

<div id="answer-container-54464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54464-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This could be due to one of several possible problems.</p><p>But if your capture filter is set for only TCP port 398, then you might be missing part of the picture.</p><p>1) Blocked Port Symptoms: Attempt to capture using no filter and check for any ICMP packets which have "administratively filtered" in the payload. This will happen if a router/switch/ACL or firewall/proxy server blocks that port from passing through to the destination. The source IP address of that device blocking the port will be in the ICMP packet itself and can easily point you to where the port is being blocked.</p><p>2) Route configuration Symptoms: Try to ping 10.2.1.133 and see if you get a reply. If you get a reply, you know the route is properly configured. If you don't get a reply, it could be either because ICMP packets are blocked or there might be a possible route configuration problem.</p><p>3) VPN configuration Symptoms: When making an IPSEC VPN connection, you usually need to have both UDP port 500 and ESP (protocol 1) ports open. Are the IPSEC Phase I and Phase II handshakes completing properly?</p><p>4) Capture Interface selection: When capturing IPSec packets from the PC using IPSec, you have to option to choose either the standard network interface (to capture IPSec handshaking protocols) or the VPN tunneled interface (to capture the unencrypted packets). So make sure you choose the proper interface to look at the proper packets.</p><p>But it's easiest to have the other side capture packets as well to see whether they really received the packets or not.</p><p>FWIW</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '16, 17:26</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p>wbenton<br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-54464" class="comments-container"></div><div id="comment-tools-54464" class="comment-tools"></div><div class="clear"></div><div id="comment-54464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

