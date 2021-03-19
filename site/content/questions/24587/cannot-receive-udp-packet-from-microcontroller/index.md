+++
type = "question"
title = "Cannot receive UDP packet from microcontroller"
description = '''I&#x27;m currently working on a UDP communication PC &amp;lt;-&amp;gt; ATmega16 (Atmel microcontroller) through the Ethernet. The ATmega16 controls the ENC28J60 (Ethernet module) through SPI. On the PC there is an application that simulates a UDP server/client.  When the packet is sent from the PC to the ATmega1...'''
date = "2013-09-11T11:50:00Z"
lastmod = "2013-09-11T13:30:00Z"
weight = 24587
keywords = [ "windows", "udp", "lost" ]
aliases = [ "/questions/24587" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot receive UDP packet from microcontroller](/questions/24587/cannot-receive-udp-packet-from-microcontroller)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm currently working on a UDP communication PC &lt;-&gt; ATmega16 (Atmel microcontroller) through the Ethernet. The ATmega16 controls the ENC28J60 (Ethernet module) through SPI. On the PC there is an application that simulates a UDP server/client.</p><p>When the packet is sent from the PC to the ATmega16, the packet is received without errors, but when the ATmega16A sends the UDP packet back to the PC, the packet is lost somewhere (the application doesn’t receive it).</p><p>The strange thing is that WireShark captures these packets coming to the PC and it seems they are valid. When sending the UDP packets form another PC (PC &lt;-&gt; PC), the packets are received normally.</p><p>Turning off Firewall in Windows did not help, and also the same problems appears in Linux. I know that this topic might be wrong for this forum, but can anybody explain why WireShark captures these packets, but my application doesn’t? ATmega16 (192.168.1.3), PC (192.168.1.2), sending and receiving goes through port number 1234.</p></div><div id="question-tags" class="tags-container tags">windows udp lost</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/a4fc057094b55d1f60459cea4138a4c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="punnkt&#39;s gravatar image" /><p>punnkt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="punnkt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '13, 12:05</p></div></div><div id="comments-container-24587" class="comments-container"><span id="24589"></span><div id="comment-24589" class="comment"><div id="post-24589-score" class="comment-score"></div><div class="comment-text"><p>If you can supply a packet capture - on <a href="http://cloudshark.org/">cloudshark</a> or any file sharing site of your choice - then maybe someone can take a look at it and see if anything stands out.</p></div><div id="comment-24589-info" class="comment-info"><span class="comment-age">(11 Sep '13, 12:22)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-24587" class="comment-tools"></div><div class="clear"></div><div id="comment-24587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24592"></span>

<div id="answer-container-24592" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24592-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Based on the capture file provided, Wireshark indicates that the UDP checksum of frame 25 is incorrect, thus the packet will be dropped.</p><pre><code>Checksum: 0x2a5b [incorrect, should be 0x2a4b (maybe caused by &quot;UDP checksum offload&quot;?)]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '13, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24592" class="comments-container"><span id="24684"></span><div id="comment-24684" class="comment"><div id="post-24684-score" class="comment-score"></div><div class="comment-text"><p>The problem was in checksum. I calculate UDP checksum like checksum for ICMP.</p><p>Sorry for not answering earlier because the site thinks my comments are spam.</p></div><div id="comment-24684-info" class="comment-info"><span class="comment-age">(14 Sep '13, 10:11)</span> punnkt</div></div></div><div id="comment-tools-24592" class="comment-tools"></div><div class="clear"></div><div id="comment-24592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24590"></span>

<div id="answer-container-24590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24590-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows please run the following command and check if the counters grow while you receive the UDP packets (highlighted below). If so, there is something wrong with the UDP packets.</p><blockquote><p>netstat -s</p></blockquote><pre><code>IPv4 Statistics

  Packets Received                   = 1070088
  Received Header Errors          = 0
  Received Address Errors         = 271
  Datagrams Forwarded                = 0
  Unknown Protocols Received         = 0
  Received Packets Discarded      = 67898
  Received Packets Delivered         = 1108133
  Output Requests                    = 1979878
  Routing Discards                   = 0
  Discarded Output Packets           = 5809
  Output Packet No Route             = 1
  Reassembly Required                = 0
  Reassembly Successful              = 0
  Reassembly Failures             = 0
  Datagrams Successfully Fragmented  = 0
  Datagrams Failing Fragmentation    = 0
  Fragments Created                  = 0

UDP Statistics for IPv4

  Datagrams Received    = 40722
  No Ports              = 352
  Receive Errors      = 67544
  Datagrams Sent        = 61341</code></pre><p>BTW: Please check if the destination MAC address is probably a broadcast address (ff:ff:ff:ff:ff:ff) or the IP address (255.255.255.255)?</p><p>Please also check that the source/destination ports of the UDP packet are correct, otherwise your Windows/Linux system will not be able to match a socket.</p><p>Basically the following values should be identical in both directions (obviously in reverse order):</p><ul><li>src/dst MAC address. A broadcast address may or may not work</li><li>src/dst IP address. A broadcast address may or may not work</li><li>source/destination ports</li></ul><p>See a similar problem here: <a href="http://goo.gl/KtJPIj">http://goo.gl/KtJPIj</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '13, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '13, 13:23</p></div></div><div id="comments-container-24590" class="comments-container"></div><div id="comment-tools-24590" class="comment-tools"></div><div class="clear"></div><div id="comment-24590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

