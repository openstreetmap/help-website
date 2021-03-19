+++
type = "question"
title = "Why receiving RST because of many DUP ACKs?"
description = '''My server works for lots of clients concurrently (client amount is between 300-800 in any moment). I wrote a server and client implementation and clients getting disconnected somehow, which i dont why. Even i am getting disconnected rarely for this unknown reason. And this is ruining quality. I logg...'''
date = "2013-08-31T15:41:00Z"
lastmod = "2013-08-31T22:45:00Z"
weight = 24246
keywords = [ "disconnection", "tcp" ]
aliases = [ "/questions/24246" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why receiving RST because of many DUP ACKs?](/questions/24246/why-receiving-rst-because-of-many-dup-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24246-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My server works for lots of clients concurrently (client amount is between 300-800 in any moment).</p><p>I wrote a server and client implementation and clients getting disconnected somehow, which i dont why. Even i am getting disconnected rarely for this unknown reason. And this is ruining quality.</p><p>I logged in to server with WinSCP and made a test like this:</p><p>Started uploading a 200mb file to server and at %20 server disconnected me. WinSCP told me to enter name and password again. You can see last moments from below log:</p><p><a href="http://www.cloudshark.org/captures/3f5bd6711bb3">Cloudshark log</a></p><p>Time 5:42 where disconnection have happened. Real log file was 1300+ seconds, so this version is splitted.</p><p>Server operating system is Centos5 64bit with 1Gbit bandwidth.</p><p>I cant even upload a file to server without getting disconnected. What must i do to fix this?</p><p>Edit: There was a logical deadlock in my software. Deadlock was causing to not being able to read &amp; write sockets. Network buffers were filling up at this stage and linux was killing socket connections to fix problem at the end. That is why other softwares were being affected too.</p></div><div id="question-tags" class="tags-container tags">disconnection tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '13, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/811d1a0369cf12073720f1f1a6029425?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mumeka&#39;s gravatar image" /><p>mumeka<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mumeka has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Feb '15, 06:41</p></div></div><div id="comments-container-24246" class="comments-container"></div><div id="comment-tools-24246" class="comment-tools"></div><div class="clear"></div><div id="comment-24246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24248"></span>

<div id="answer-container-24248" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24248-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I cant even upload a file to server without getting disconnected.</p></blockquote><p>O.K. your problem seems to be affecting different applications on that server (own application, winscp, etc.), which leads me to the conclusion that there is a problem with either of these</p><ul><li>The server itself is somehow overloaded from time to time (CPU load)</li><li>The interface of the server is broken (or the driver). <strong>Check</strong> with <strong>netstat -ni</strong> and kernel logs (dmesg)</li><li>The switch or switch port of the server is broken or overloaded (flooding). <strong>Check</strong> the switch port statistics and the switch logs.</li><li>There is a network burst in the local network, that overloads local network components. <strong>Check</strong> with capture files taken at the server</li><li>Any other system in path to the server (firewalls, load balancer, router) are overloaded from time to time. <strong>Ask</strong> the admins</li></ul><blockquote><p>What must i do to fix this?</p></blockquote><p>Well, that's a lot of possible problems and you will not be able to identify all of them by looking at network traces (capture files), especially if you capture the traffic at the client (as in your sample on cloudshark).</p><p>The best way to eliminate (possibly) faulty components is to run some tests locally (client and server in the same subnet), to see if a file upload (scp) gets interrupted as well.</p><p>If <strong>YES</strong>: take a look at</p><ul><li>the switch and/or switch-port of the server</li><li>the server interface</li><li>the server load</li><li>iptables on the server (rate limiting or similar)</li></ul><p>If <strong>NO</strong>: take a look at</p><ul><li>other components in the path to the server (firewalls, router, etc.)</li></ul><p>To answer your question:</p><blockquote><p>Why receiving RST because of many DUP ACKs?</p></blockquote><p>The <strong>client</strong> closes the connection after many retries with a RESET. It (basically) gives up because there is no answer from the server anymore.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24248" class="comments-container"><span id="24363"></span><div id="comment-24363" class="comment"><div id="post-24363-score" class="comment-score"></div><div class="comment-text"><p>Your answer is very helpful. My first server machine was in another country, because of this problem, i rented another machine in my country. So this is a second server with same settings. So it is a low probability hardware has problems, it must be some configuration error. I tried to disable firewalls, but it did not help. I think same subnet test can be helpful, but i need a machine in same subnet first, so it will have to wait a bit.</p></div><div id="comment-24363-info" class="comment-info"><span class="comment-age">(04 Sep '13, 16:44)</span> mumeka</div></div><span id="24377"></span><div id="comment-24377" class="comment"><div id="post-24377-score" class="comment-score"></div><div class="comment-text"><blockquote><p>My first server machine was in another country, because of this problem, i rented another machine in my country. <strong>So this is a second server with same settings</strong>.</p></blockquote><p>O.K. this would certainly rule out hardware related issues, as you say. So, you should concentrate on the CPU load and probably on some network parameters of CentOS 5. Which one? Good question.</p><p>Did you think about a migration to CentOS 6?<br />
</p><p>BTW: Anything suspicious in the logs?</p></div><div id="comment-24377-info" class="comment-info"><span class="comment-age">(05 Sep '13, 05:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24248" class="comment-tools"></div><div class="clear"></div><div id="comment-24248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24253"></span>

<div id="answer-container-24253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24253-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace file provided was taken at the client side and is showing that one full-size segment <a href="http://www.cloudshark.org/captures/3f5bd6711bb3?filter=tcp%5B4%3A8%5D%20contains%2026d3%3A6ad4">tcp.seq==399361</a> is never acknowledged by the server while at the same time we still see packets in the reverse direction. So we can assume we still have connectivity and it is that single packet this is causing the problem.</p><p>"What must i do to fix this?" Hello, as Kurt mentions you should have a look at the server side and see whether CentOS is saw the retransmitted packets and if so, whether the seq/ack numbers are correct. (Compare the <strong>real</strong> sequence numbers in both client and server trace). Sometimes the TCP SACK option is confusing devices so it might be worth a try to disable it on the server side and see if it helps.</p><pre><code> /etc/sysctl.conf net.ipv4.tcp_sack = 0 
Then run &quot;/sbin/sysctl -p /etc/sysctl.conf&quot; to load the settings into the running kernel.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-24253" class="comments-container"><span id="24362"></span><div id="comment-24362" class="comment"><div id="post-24362-score" class="comment-score"></div><div class="comment-text"><p>i tried disabling sack but it did not help. I will try to get server side logs as well to compare ack values and to see if server is receiving retransmitted packages.</p></div><div id="comment-24362-info" class="comment-info"><span class="comment-age">(04 Sep '13, 16:25)</span> mumeka</div></div></div><div id="comment-tools-24253" class="comment-tools"></div><div class="clear"></div><div id="comment-24253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

