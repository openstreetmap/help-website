+++
type = "question"
title = "How to calculate the total network traffic pass though a Gigabit NIC with high precision?"
description = '''Hi, I am using a Windows PC. I would like to calculate the total network traffic pass though a Gigabit NIC between time t1 and t2. In my case, accuracy is very important. I don&#x27;t want to miss any packet. And the network speed during t1-t2 is &amp;gt;900Mbps. Is it possible to use tshark/tcpdump/dumpcap/...'''
date = "2012-06-30T09:25:00Z"
lastmod = "2012-07-02T00:55:00Z"
weight = 12348
keywords = [ "winpcap", "dumpcap", "network", "tshark" ]
aliases = [ "/questions/12348" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to calculate the total network traffic pass though a Gigabit NIC with high precision?](/questions/12348/how-to-calculate-the-total-network-traffic-pass-though-a-gigabit-nic-with-high-precision)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12348-score" class="post-score" title="current number of votes">0</div><span id="post-12348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using a Windows PC. I would like to calculate the total network traffic pass though a Gigabit NIC between time t1 and t2. In my case, accuracy is very important. I don't want to miss any packet. And the network speed during t1-t2 is &gt;900Mbps.</p><p>Is it possible to use tshark/tcpdump/dumpcap/Winpcap to calculate the total network traffic for a Gigabit NIC with high accuracy?</p><p>Assuming that a user sent a 1GB file through the NIC to TCP port 7000, and I use tshark/tcpdump/dumpcap/Winpcap to capture the network traffic and dump it to a pcap file. After that, if I use wireshark to analyze the pcap file and calculate the total network traffic sent to TCP port 7000, am I able to get 1GB exactly?</p><p>Some users from other forums told me that the speed of disk I/O will become the bottleneck in my test. The server may not be able to write the pcap file fast enough to disk.</p><p>Actually the packets' contents and the pcap file are not important to me. I just want to calculate the total network traffic.</p><p>I am looking for a software which can:</p><ol><li>check the packet size when a packet pass through a NIC</li><li>record the packet size, and then add it to a "cumulative network traffic" variable</li><li>turn to the next packet, without recording the previous packet's contents to a pcap file.</li><li>no need to write to disk</li></ol><p>Is tshark/tcpdump/dumpcap/Winpcap able to perform these functions with high accuracy? If not, what software should I use?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '12, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/38babbb3ad0f16b1e9acaf000ebec978?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Patrick_L&#39;s gravatar image" /><p><span>Patrick_L</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Patrick_L has no accepted answers">0%</span></p></div></div><div id="comments-container-12348" class="comments-container"></div><div id="comment-tools-12348" class="comment-tools"></div><div class="clear"></div><div id="comment-12348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12363"></span>

<div id="answer-container-12363" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12363-score" class="post-score" title="current number of votes">0</div><span id="post-12363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Patrick_L has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can't you just query the traffic counters on the interface e.g. by using WMI?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '12, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-12363" class="comments-container"></div><div id="comment-tools-12363" class="comment-tools"></div><div class="clear"></div><div id="comment-12363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

