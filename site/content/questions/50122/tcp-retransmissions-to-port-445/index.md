+++
type = "question"
title = "TCP Retransmissions to port 445"
description = '''Hello guys, I have these SYN packets going from the IP 192.168.10.64, a quarantine server running on VMWare, and to 172.16.128.52 on port 445, a machine connected with VPN on a different location. Every packet goes from this IP to the other. The capture has been made from the firewall. So this is ho...'''
date = "2016-02-12T00:52:00Z"
lastmod = "2016-02-12T05:56:00Z"
weight = 50122
keywords = [ "tcp", "retransmissions", "445", "syn" ]
aliases = [ "/questions/50122" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmissions to port 445](/questions/50122/tcp-retransmissions-to-port-445)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50122-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>I have these SYN packets going from the IP 192.168.10.64, a quarantine server running on VMWare, and to 172.16.128.52 on port 445, a machine connected with VPN on a different location.</p><p>Every packet goes from this IP to the other.</p><p>The capture has been made from the firewall.</p><p>So this is how it occurs:</p><ol><li>On first message the source MAC address is the quarantine server's one, and the destination MAC is my firewall. (TTL=128)</li><li>Second message is marked as TCP Out-Of-Order; the source MAC address is the firewall's and the destination is the Cisco router. (TTL=127)</li><li>Third message is a TCP Retransmission, the source MAC is the router's and the destination is the firewall. (TTL=126)</li><li>Fourth message is another TCP Retransmission, source MAC is the firewall, destination is the router. (TTL=125)</li><li>From this moment, third and fourth message repeat themselves until TTL decreases to 28. And then it just stops.</li></ol><p>Not even one second later, a new SYN packet from the quarantine's MAC address goes to the firewall's MAC address, with a new source port. Still the same source &amp; destination IP.</p><p>Do you have an idea of what could be the reason of all these retransmissions ? Is this a normal behavior ?</p><p>Thank you very much for your time.</p><p>Edit: <a href="http://s000.tinyupload.com/download.php?file_id=08702454594609573568&amp;t=0870245459460957356848235">here</a> is the pcap file, i used the filter "ip.addr == 192.168.10.64 &amp;&amp; ip.addr == 172.16.128.52"</p></div><div id="question-tags" class="tags-container tags">tcp retransmissions 445 syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '16, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/d44ea9f599925115fec0965219a48b9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ITDeo&#39;s gravatar image" /><p>ITDeo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ITDeo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '16, 02:49</p></div></div><div id="comments-container-50122" class="comments-container"><span id="50124"></span><div id="comment-50124" class="comment"><div id="post-50124-score" class="comment-score"></div><div class="comment-text"><p>You'll likely get a much more informed response if you post a capture somewhere publicly available, rather than your textual interpretation of it.</p></div><div id="comment-50124-info" class="comment-info"><span class="comment-age">(12 Feb '16, 02:21)</span> grahamb ♦</div></div><span id="50128"></span><div id="comment-50128" class="comment"><div id="post-50128-score" class="comment-score"></div><div class="comment-text"><p>You're right, I edited &amp; added the file</p></div><div id="comment-50128-info" class="comment-info"><span class="comment-age">(12 Feb '16, 02:51)</span> ITDeo</div></div></div><div id="comment-tools-50122" class="comment-tools"></div><div class="clear"></div><div id="comment-50122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50139"></span>

<div id="answer-container-50139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50139-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have a routing loop there.</p><p>The 1st packet goes from the sender to the firewall box.</p><p>The 2nd packet goes from the firewall box to the Cisco router.</p><p>The 3rd packet goes from the Cisco router back to the firewall.</p><p>Then this loop repeats until the TTL fulfils its purpose and stops that because it reaches 0.</p><p>So please check why the firewall uses the Cisco as its route for packets to 172.16.128.52, and why the Cisco uses the firewall as its route for these packets, and fix the routing at that box at which it is wrong.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '16, 05:58</p></div></div><div id="comments-container-50139" class="comments-container"></div><div id="comment-tools-50139" class="comment-tools"></div><div class="clear"></div><div id="comment-50139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

