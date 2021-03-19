+++
type = "question"
title = "capture shows other hosts information"
description = '''Hi, I started wireshark on my notebook to capture what was going on my NIC, but I am surprised to see other hosts communications not destinated for my NIC as well (note that my switchport is not configured in span mode). I am having ip address of 172.16.224.162. Address A,Address B,Packets,Bytes,Pac...'''
date = "2011-04-11T02:28:00Z"
lastmod = "2011-04-11T03:25:00Z"
weight = 3437
keywords = [ "traffic", "unnecessary", "captured" ]
aliases = [ "/questions/3437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture shows other hosts information](/questions/3437/capture-shows-other-hosts-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I started wireshark on my notebook to capture what was going on my NIC, but I am surprised to see other hosts communications not destinated for my NIC as well (note that my switchport is not configured in span mode). I am having ip address of 172.16.224.162.</p><p>Address A,Address B,Packets,Bytes,Packets A-&gt;B,Bytes A-&gt;B,Packets A&lt;-B,Bytes A&lt;-B,Rel Start,Duration,bps A-&gt;B,bps A&lt;-B 172.25.219.2,224.0.0.10,17,1258,17,1258,0,0,0.057954000,73.6765,136.60,N/A 172.16.224.129,224.0.0.10,17,1258,17,1258,0,0,3.172119000,72.4497,138.91,N/A 172.16.224.162,172.25.218.16,111,33433,53,10370,58,23063,4.771098000,61.9298,1339.58,2979.24 172.16.224.162,172.25.221.18,9,1534,6,964,3,570,16.455411000,60.7066,127.04,75.12 172.16.224.209,172.25.221.18,2,120,0,0,2,120,18.893031000,0.0021,N/A,458891.01 <strong>172.16.224.195,172.25.221.18,2,120,0,0,2,120,18.893376000,0.0008,N/A,1166464.16 172.16.224.184,172.25.218.16,1,304,0,0,1,304,34.119187000,0.0000,N/A,N/A</strong> 172.16.224.210,172.16.224.255,6,552,6,552,0,0,44.369611000,3.7658,1172.66,N/A 172.16.224.206,255.255.255.255,1,342,1,342,0,0,45.879366000,0.0000,N/A,N/A 172.16.224.196,172.16.224.255,34,3633,34,3633,0,0,46.496769000,30.6426,948.48,N/A 172.16.224.162,172.25.218.13,138,84042,61,10937,77,73105,72.798605000,1.2638,69231.05,462753.58</p></div><div id="question-tags" class="tags-container tags">traffic unnecessary captured</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/68024cef03bcde103326f32d3e3295f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Benson%20Low&#39;s gravatar image" /><p>Benson Low<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Benson Low has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 22:24</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3437" class="comments-container"></div><div id="comment-tools-3437" class="comment-tools"></div><div class="clear"></div><div id="comment-3437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3438"></span>

<div id="answer-container-3438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3438-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This happens quite frequently in most networks. As soon as the switch does not know the MAC address of a destination node (because either the station wasn't addressed before or, more likely, the MAC address table entry got discarded after a while) he has to flood the frame to all ports. As soon as the destination node answers the switch will learn which port the MAC is at, and forward all further frames directly.</p><p>You should always see just one single frame to a destination MAC like that, and none of the following frames after the MAC was learned. Exception is, if the destination MAC does not answer at all, but in that case you'll just see multiple retries to get the frame delivered from the source.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3438" class="comments-container"><span id="3459"></span><div id="comment-3459" class="comment"><div id="post-3459-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks, it does make sense. But if the mac address is unknown, is there suppose to be a arp broadcast to learn the mac address? what i am seeing is a unicast layer2 instead of a broadcast, unless we are talking about mac address table has aged out at the switch level.</p><p>Appreciate if you could enlighten me on these. :)</p></div><div id="comment-3459-info" class="comment-info"><span class="comment-age">(11 Apr '11, 22:45)</span> Benson Low</div></div><span id="3460"></span><div id="comment-3460" class="comment"><div id="post-3460-score" class="comment-score">1</div><div class="comment-text"><p>Correct, if the sender doesn't know the MAC address you should see an ARP broadcast containing a request for the MAC to an IP address. What you probably have there is that the sending node does still know the MAC address (or has a static entry for it), but the switch forgot about it. I saw this a lot when there was a long MAC caching time on workstations but a lot shorter caching time on the switches.</p></div><div id="comment-3460-info" class="comment-info"><span class="comment-age">(11 Apr '11, 23:40)</span> Jasper ♦♦</div></div><span id="3461"></span><div id="comment-3461" class="comment"><div id="post-3461-score" class="comment-score">2</div><div class="comment-text"><p>One of the most common sources for flooding is asymmetric routing. When traffic from the host follows a different path as traffic to the host, a switch along the path might not see the traffic coming from the host and therefor it ages out the entry for the host in the forwarding table. As the ARP timeout is usually larger than the aging timer on a switch (on cisco the default arp timeout is 4 hours and the mac aging timer is 5 minutes), the traffic towards the host starts to get flooded once the mac aging timer runs out until the host sends out a broadcast.</p></div><div id="comment-3461-info" class="comment-info"><span class="comment-age">(12 Apr '11, 00:35)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3438" class="comment-tools"></div><div class="clear"></div><div id="comment-3438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

