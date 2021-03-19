+++
type = "question"
title = "Performance Testing iperf"
description = '''I am doing some performance testing using iperf between 2 Windows 2008 servers with a latency of around 80ms and a minimum available bandwidth of 200Mbps. According to the following URL http://www.switch.ch/network/tools/tcp_throughput/ the optimal TCP window size should be around 2MB required tcp b...'''
date = "2013-11-24T11:41:00Z"
lastmod = "2013-11-25T03:59:00Z"
weight = 27319
keywords = [ "tcpwindowsize" ]
aliases = [ "/questions/27319" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Performance Testing iperf](/questions/27319/performance-testing-iperf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27319-score" class="post-score" title="current number of votes">0</div><span id="post-27319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing some performance testing using iperf between 2 Windows 2008 servers with a latency of around 80ms and a minimum available bandwidth of 200Mbps.</p><p>According to the following URL <a href="http://www.switch.ch/network/tools/tcp_throughput/">http://www.switch.ch/network/tools/tcp_throughput/</a> the optimal TCP window size should be around 2MB</p><p>required tcp buffer to reach 200 Mbps with RTT of 80.0 ms &gt;= 2048.0 KByte</p><p>What throughput should I expect to see with this setting? Should it be reaching 200Mbps or what would be a more realistic value?</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '13, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/c566a3572252e6465980c2584cb67bbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanBlaney&#39;s gravatar image" /><p><span>IanBlaney</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanBlaney has no accepted answers">0%</span></p></div></div><div id="comments-container-27319" class="comments-container"></div><div id="comment-tools-27319" class="comment-tools"></div><div class="clear"></div><div id="comment-27319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27327"></span>

<div id="answer-container-27327" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27327-score" class="post-score" title="current number of votes">0</div><span id="post-27327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well under 'ideal conditions', you can get up to ~190-195 Mbit/s. However, the real world is never ideal. So, if you get anything below that (which would be perfectly normal ;-)), there are many factors that can limit your throughput.</p><ul><li>'misbehaving' devices on the path, like switches, routers, firewalls, QoS devices, WAN accelerators</li><li>packet loss on the line</li><li>issues with the NIC driver of your Windows 2008 systems</li><li>TCP/IP offloading problems (also NIC driver related)</li><li>over provisioning of your provider (selling more bandwidth than he can actually guarantee at any time)</li></ul><p>You can try to run iperf on two Linux systems (boot the PCs from a CDROM or flash drive), just to eliminate a possible impact of Windows 2008 and/or NIC driver issues. If you get the same (bad) results with iperf on Linux, you should capture the traffic and look for packet loss (retransmission, massive dup ACK, etc.)</p><p>BTW: What is the throughput you get with iperf on Windows 2008 with TCP (given the fact you have chosen the correct window and buffer sizes)? And what is the throughput if you test with UDP (iperf can do that as well)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '13, 05:42</strong> </span></p></div></div><div id="comments-container-27327" class="comments-container"><span id="27335"></span><div id="comment-27335" class="comment"><div id="post-27335-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt</p><p>Many thanks for you answer. At the moment we are getting around 25-30Mbps when using TCP. There are WAN accelerators (Citrix) in between which we suspect are not configured properly and may be causing the issue. Taking packet captures at both ends we see strange things happening with the window size and scaling.</p><p>The accelerators are managed by a third party and we are in the process of getting the traffic between the iperf servers configured as passthrough mode.</p><p>We have tested using 2 linux clients and get much the same results. UDP throughput is around 120-130Mbps.</p><p>Ian</p></div><div id="comment-27335-info" class="comment-info"><span class="comment-age">(25 Nov '13, 02:13)</span> <span class="comment-user userinfo">IanBlaney</span></div></div><span id="27339"></span><div id="comment-27339" class="comment"><div id="post-27339-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There are WAN accelerators (Citrix) in between which we suspect are not configured properly and may be causing the issue.</p></blockquote><p>You could place the two testing devices in front of the WAN accelerator if that is possible in your environment, or switch the WAN accelerators off during the test. Please consider, that those devices are not the only ones, that can cause trouble.</p></div><div id="comment-27339-info" class="comment-info"><span class="comment-age">(25 Nov '13, 03:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27327" class="comment-tools"></div><div class="clear"></div><div id="comment-27327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

