+++
type = "question"
title = "Packet Loss, retransmissions but no switch port errors."
description = '''This is a general question. We have an WAN based enterprise application where most sites traverse 8-12 hops before getting to a data center load balancer (CISCO 6509E) which sprays to a web server cluster. Using WireShark we are getting lost of re-transamissions (4%) coming from the load balancer at...'''
date = "2013-12-04T14:48:00Z"
lastmod = "2013-12-04T15:43:00Z"
weight = 27783
keywords = [ "loss", "errors", "port", "packet" ]
aliases = [ "/questions/27783" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Loss, retransmissions but no switch port errors.](/questions/27783/packet-loss-retransmissions-but-no-switch-port-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27783-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a general question. We have an WAN based enterprise application where most sites traverse 8-12 hops before getting to a data center load balancer (CISCO 6509E) which sprays to a web server cluster. Using WireShark we are getting lost of re-transamissions (4%) coming from the load balancer at the TCP level, but when we look at the devices along the path, we are not seeing any switch port errors along the way. I know that Ethernet is not responsible for reporting dropped packets, its the job of TCP. However, would I not see some error counter on the NIC cards (servers) or switch ports along the way? Is it possible to see that packet loss that we have seen yet not see anything on any of the switch ports?<br />
</p><p>Switch Name/ interface Time Max Utilization Queue Drops In/Out Tester Connection<br />
ITDCHLPBR1-Gb1/7 1000-1130 3.4 kbps 0/0</p><p>MITC Data center<br />
ITDCHLPBR1-TenGb8/1 1000-1130 348.3 Mbps 0/0 ITDCHLPBR2-TenGb8/1 1000-1130 357 Mbps 0/0 ITD-CHL-CORE-1-TenGb7/1 1000-1130 449.9 Mbps 0/0 ITD-CHL-CORE-2-TenGb7/1 1000-1130 388.6 Mbps 0/0</p><p>INTERNET DMZ<br />
ITD-CHL-CORE-1-TenGb8/1 1000-1130 67.1 Mbps 0/0 ITD-CHL-CORE-2-TenGb8/1 1000-1130 5.0 kbps 0/0 ITD-INTERNET-DMZ-1-TenGb5/4 1000-1130 58.2 Mbps 0/0 ITD-INTERNET-DMZ-2-TenGb5/4 1000-1130 24.2 kbps 0/0</p><p>HRCMS server farms<br />
ITDCHLPBR1-TenGb8/4 1000-1130 92.4 Mbps 0/0 ITDCHLPBR2-TenGb8/4 1000-1130 5 kbps 0/0 AIX-COMPLEX-1-TenGb1/4 1000-1130 86.1 Mbps 0/0 AIX-COMPLEX-2-TenGb1/4 1000-1130 61.6 kbps 0/0</p></div><div id="question-tags" class="tags-container tags">loss errors port packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '13, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/16c80ca493c77f3486cbb7ff38cc5d3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoberist&#39;s gravatar image" /><p>Zoberist<br />
<span class="score" title="0 reputation points">0</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoberist has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-27783" class="comments-container"></div><div id="comment-tools-27783" class="comment-tools"></div><div class="clear"></div><div id="comment-27783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27791"></span>

<div id="answer-container-27791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27791-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure that these are really retransmissions? Wireshark has a habit of marking packets as "Retransmission" when they're just "Out-of-Order", and those are a lot less problematic (well, in most cases they are no problem at all) than real packet loss. Even with retransmissions you need to ask yourself if they really have an impact on your application, because if the recovery is so fast that the user doesn't even notice the lost packets you might not want to waste time on tracking them down.</p><p>You should determine if the packet loss really occurred by looking at the TCP sequence and acknowledgement numbers. If there is packet loss then you should see that the client is using duplicate ACKs to signal the missing segment and a retransmission arriving for that segment. Please keep in mind that the TCP expert of Wireshark does not care about the RTT of the connection and flags packets as retransmissions if they arrive more than 3ms after the segment <strong>should</strong> have arrived in the first place. The 3ms is hard coded. If your connection has a RTT that is higher than that (which I guess from your description is probably has) you can easily run into the problem that the expert marks packets as retransmissions while they are Out-of-Orders in fact. This happens a lot if WAN acceleration devices are in use, because they often seem to reorder packets to optimize throughput and/or latency.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-27791" class="comments-container"></div><div id="comment-tools-27791" class="comment-tools"></div><div class="clear"></div><div id="comment-27791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

