+++
type = "question"
title = "iperf test duration"
description = '''Hello, i am running iperf to send traffic from one computer to another, &amp;amp; i am using tcpdump to capture packets (1000,000 and more) on both sides of the sender and receiver, the problem is tcpdump captured much LESS than the 1 million packets on both sides, and i changed the test duration random...'''
date = "2015-07-09T10:49:00Z"
lastmod = "2015-07-13T08:38:00Z"
weight = 44021
keywords = [ "test", "iperf", "tcpdump", "time" ]
aliases = [ "/questions/44021" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [iperf test duration](/questions/44021/iperf-test-duration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44021-score" class="post-score" title="current number of votes">0</div><span id="post-44021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i am running iperf to send traffic from one computer to another, &amp; i am using tcpdump to capture packets (1000,000 and more) on both sides of the sender and receiver, the problem is tcpdump captured much LESS than the 1 million packets on both sides, and i changed the test duration randomly from 10 seconds to 100 seconds, it solved the problem at the sender-side &amp; i got my 1000,000 captures, but NOT at the receiver where i got only 108,000 captures, now i don't know what is causing this, and i could not find an answer on the internet, any help to get my 1 million captures at the sender and receiver??</p><p>i used for the server: iperf -s</p><p>And for the client: iperf -c ipAddress -t 100</p><p>and for the capture tool i used: tcpdump -i eth1 -s 0 -c 1000000 -w /dev/shm/new.pcap "tcp"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-test" rel="tag" title="see questions tagged &#39;test&#39;">test</span> <span class="post-tag tag-link-iperf" rel="tag" title="see questions tagged &#39;iperf&#39;">iperf</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '15, 05:12</strong> </span></p></div></div><div id="comments-container-44021" class="comments-container"></div><div id="comment-tools-44021" class="comment-tools"></div><div class="clear"></div><div id="comment-44021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44030"></span>

<div id="answer-container-44030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44030-score" class="post-score" title="current number of votes">0</div><span id="post-44030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I see the following possible problems:</p><p>At both sides: tcpdump might not be able to record all packets (disk I/O) and thus it drops some of them.<br />
<strong>Solution:</strong> don't capture the full frame size, meaning use option -s (snaplength), like -s 100. Futhermore check the statistics of tcpdump at the end of the capture session (dropped packets).</p><p>At the <strong>receiver</strong> side: There could be packet loss in the network (normal for every network) and thus you see less frames on the receiver side than on the sender side.<br />
<strong>Solution:</strong> iperf will tell you if there was packet loss in the report.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '15, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-44030" class="comments-container"><span id="44037"></span><div id="comment-44037" class="comment"><div id="post-44037-score" class="comment-score"></div><div class="comment-text"><p>okay you are right but still couldn't solve the problem, i had my snaplen set to the default -s 0, i changed it as you said to -s 100 which solved the problem at the receiver but i had the same problem at the sender again! i got million packets at the receiver and only 30,000 at the sender, and iperf did not show any Losses so i don't know what to do, how do i set my framesize? i am using tcp, also i tried -s 1500 since eth mtu is 1500 but it did not work either, is this problem in tcpdump only or i will have it if i change to tshark or other?</p></div><div id="comment-44037-info" class="comment-info"><span class="comment-age">(10 Jul '15, 02:00)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="44039"></span><div id="comment-44039" class="comment"><div id="post-44039-score" class="comment-score"></div><div class="comment-text"><blockquote><p>also is this problem in tcpdump only or i will have it if i change to tshark or other?</p></blockquote><p>tcpdump and tshark are using the same capturing library, called libpcap, so you will have the same issue if it's a load problem.</p><p>You can try to separate traffic generation and capturing, to prevent resource overloading on the sender (CPU, Network I/O, disk I/O, etc.).</p><p>So, run iperf on the sender and do the capturing part on a different system via switch port mirroring.</p></div><div id="comment-44039-info" class="comment-info"><span class="comment-age">(10 Jul '15, 02:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="44089"></span><div id="comment-44089" class="comment"><div id="post-44089-score" class="comment-score"></div><div class="comment-text"><p>but actually i need the same environment for the test and i have to fix this instead of replacing the system...i am not overloading the sender as the receiver is not generating data packets just ack packets and im using 1G interface on both sides...any suggestions?</p></div><div id="comment-44089-info" class="comment-info"><span class="comment-age">(13 Jul '15, 05:02)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="44090"></span><div id="comment-44090" class="comment"><div id="post-44090-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@yas1234</span> - When performing the iperf stream and packet capture at the sender, what is the system utilization?<br />
I had a similar issue in which the OS was limiting the amount of resources allocated to any one data stream. Some suggestions:</p><ol><li><p>Try using a smaller throughput and see if the issue is resolved. Then gradually increase the throughput until you see the issue - very time consuming!</p></li><li><p>Perform the same throughput and look at your system utilization. If they reach or near 100%, then cutback the throughput.</p></li></ol><p>In my case, I had to add a second source to create the overall throughout required for the test.</p></div><div id="comment-44090-info" class="comment-info"><span class="comment-age">(13 Jul '15, 06:41)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="44091"></span><div id="comment-44091" class="comment"><div id="post-44091-score" class="comment-score"></div><div class="comment-text"><p>how do i see my system's utilization ?</p></div><div id="comment-44091-info" class="comment-info"><span class="comment-age">(13 Jul '15, 06:46)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="44094"></span><div id="comment-44094" class="comment not_top_scorer"><div id="post-44094-score" class="comment-score"></div><div class="comment-text"><p>Depends on the OS:</p><ol><li><p>Windows = Windows Task Manager, press CTRL+ALT+DEL and select the Task Manager</p></li><li><p>Linux distros = use the top command</p></li></ol></div><div id="comment-44094-info" class="comment-info"><span class="comment-age">(13 Jul '15, 07:04)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="44099"></span><div id="comment-44099" class="comment not_top_scorer"><div id="post-44099-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but actually i need the same environment for the test and <strong>i have to fix this</strong> instead of replacing the system.</p></blockquote><p>To fix what exactly? Does iperf show packet loss or is it just the fact that you don't see everything in the capture file?</p></div><div id="comment-44099-info" class="comment-info"><span class="comment-age">(13 Jul '15, 08:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-44030" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-44030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

