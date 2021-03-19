+++
type = "question"
title = "TCP Dump, cannot understand these 4 lines?"
description = '''I need support understanding these 4 lines. looks like tcp dump but im actully not understanding what exactly is happening here.  13:13:22.407445 IP 192.168.246.128.54955 &amp;gt; 192.168.246.13.80: S 2910497703:2910497703(0) win 5840 &amp;lt;mss 1460,sackok,timestamp=&quot;&quot; 518611=&quot;&quot; 0,nop,wscale=&quot;&quot; 6=&quot;&quot;&amp;gt; 1...'''
date = "2014-11-17T12:18:00Z"
lastmod = "2014-11-17T12:44:00Z"
weight = 37911
keywords = [ "nmap", "tcpdump", "tcp", "wireshark" ]
aliases = [ "/questions/37911" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dump, cannot understand these 4 lines?](/questions/37911/tcp-dump-cannot-understand-these-4-lines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37911-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need support understanding these 4 lines. looks like tcp dump but im actully not understanding what exactly is happening here.</p><ol><li>13:13:22.407445 IP 192.168.246.128.54955 &gt; 192.168.246.13.80: S 2910497703:2910497703(0) win 5840 &lt;mss 1460,sackok,timestamp="" 518611="" 0,nop,wscale="" 6=""&gt;</li><li>13:13:22.407560 IP 192.168.246.13.80 &gt; 192.168.246.128.54955: S 3762608065:3762608065(0) ack 2910497704 win 64240 &lt;mss 1460,nop,wscale="" 0,nop,nop,timestamp="" 0="" 0,nop,nop,sackok=""&gt;</li><li>13:13:22.407963 IP 192.168.246.128.54955 &gt; 192.168.246.13.80: . ack 1 win 92 &lt;nop,nop,timestamp 518611="" 0=""&gt;</li><li>13:13:22.408321 IP 192.168.246.128.54955 &gt; 192.168.246.13.80: R 1:1(0) ack 1 win 92 &lt;nop,nop,timestamp 518611="" 0=""&gt;</li></ol></div><div id="question-tags" class="tags-container tags">nmap tcpdump tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/cb7634e4c879c2726a631cf06b124f39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kell90&#39;s gravatar image" /><p>Kell90<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kell90 has no accepted answers">0%</span></p></div></div><div id="comments-container-37911" class="comments-container"></div><div id="comment-tools-37911" class="comment-tools"></div><div class="clear"></div><div id="comment-37911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37912"></span>

<div id="answer-container-37912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37912-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a 3-way handshake between a linux client (192.168.246.128) and a windows http server.</p><pre><code>    Linux           Windows
      ----- SYN -----&gt; 
      &lt;---- SYN_ACK--- 
      ------ACK -----&gt; 
      ------RST -----&gt;</code></pre><p>The 4th packet is a RESET of the connection - pretty early to my taste. So it looks like you are just checking whether the http server is active and operational. Network monitors do this often.</p><p>PS.: Is this part of your homework???</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '14, 12:51</p></div></div><div id="comments-container-37912" class="comments-container"><span id="37913"></span><div id="comment-37913" class="comment"><div id="post-37913-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for the fast reply, my question now is where do you identify that the IP 128 is a linux client?</p></div><div id="comment-37913-info" class="comment-info"><span class="comment-age">(17 Nov '14, 12:51)</span> Kell90</div></div><span id="37916"></span><div id="comment-37916" class="comment"><div id="post-37916-score" class="comment-score"></div><div class="comment-text"><p>That comes form 20+ years experience of reading traces ... ;-)</p></div><div id="comment-37916-info" class="comment-info"><span class="comment-age">(17 Nov '14, 13:37)</span> mrEEde</div></div><span id="37929"></span><div id="comment-37929" class="comment"><div id="post-37929-score" class="comment-score"></div><div class="comment-text"><p>OS details from 3 way handshake in trace can be derieved from Initial RWIN size, Find this link for more details, <a href="http://www.netresec.com/?page=Blog&amp;month=2011-11&amp;post=Passive-OS-Fingerprinting">http://www.netresec.com/?page=Blog&amp;month=2011-11&amp;post=Passive-OS-Fingerprinting</a></p></div><div id="comment-37929-info" class="comment-info"><span class="comment-age">(17 Nov '14, 20:41)</span> kishan pandey</div></div></div><div id="comment-tools-37912" class="comment-tools"></div><div class="clear"></div><div id="comment-37912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

