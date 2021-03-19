+++
type = "question"
title = "TCP state of incoming packets - tcpdump"
description = '''Is there anyway to capture the sate of ONLY incoming packets to the sender (like the tcpprobe does) using either tcpdump or wireshark (or tshark)? I tried with the following command but i am not getting the right packets. This only captures packets with length of less than the MTU (outstanding bytes...'''
date = "2017-05-15T07:38:00Z"
lastmod = "2017-05-15T19:00:00Z"
weight = 61406
keywords = [ "packets", "tcpdump", "tshark", "tcp", "wireshark" ]
aliases = [ "/questions/61406" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP state of incoming packets - tcpdump](/questions/61406/tcp-state-of-incoming-packets-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyway to capture the sate of ONLY incoming packets to the sender (like the tcpprobe does) using either tcpdump or wireshark (or tshark)? I tried with the following command but i am not getting the right packets. This only captures packets with length of less than the MTU (outstanding bytes). I am sending an iperf traffic from the client (10.0.0.1) to the server (10.0.0.2).</p><blockquote><p>sudo tcpdump -i eth1 tcp and dst host 10.0.0.1 -w test.pcap</p></blockquote></div><div id="question-tags" class="tags-container tags">packets tcpdump tshark tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '17, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 May '17, 07:47</p></div></div><div id="comments-container-61406" class="comments-container"><span id="61415"></span><div id="comment-61415" class="comment"><div id="post-61415-score" class="comment-score"></div><div class="comment-text"><p>Can you clarify? A "sender" is someone sending, so it's outgoing, not incoming. Do you mean a "server"? Not really sure what you're trying to get... using the "dst host" part should make sure you only get one direction.</p></div><div id="comment-61415-info" class="comment-info"><span class="comment-age">(15 May '17, 13:31)</span> Jasper ♦♦</div></div><span id="61421"></span><div id="comment-61421" class="comment"><div id="post-61421-score" class="comment-score"></div><div class="comment-text"><p>yes the sender is someone sending Jasper and its ip is 10.0.0.1</p></div><div id="comment-61421-info" class="comment-info"><span class="comment-age">(16 May '17, 03:21)</span> armodes</div></div><span id="61440"></span><div id="comment-61440" class="comment"><div id="post-61440-score" class="comment-score"></div><div class="comment-text"><p>Then <code>dst host 10.0.0.1</code> will capture packets sent <em>to</em> the "sender". See my answer.</p></div><div id="comment-61440-info" class="comment-info"><span class="comment-age">(16 May '17, 11:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61406" class="comment-tools"></div><div class="clear"></div><div id="comment-61406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61416"></span>

<div id="answer-container-61416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61416-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both Wireshark/TShark/dumpcap and tcpdump capture packets, not "state", so I assume you mean that you only want to capture packets going in one direction. If the "sender" is the host sending the perf traffic, i.e. 10.0.0.1, you would want a filter of</p><pre><code>tcp and src host 10.0.0.1</code></pre><p>I.e., you want packets with the sender's IP address as the <em>source</em> (<code>src</code>), not as the <em>destination</em> (<code>dst</code>).</p><p>As for "packets with length of less than the MTU", I presume you mean "less than or equal to" - there's nothing that should prevent full-MTU-size packets from being captured - and the "M" in "MTU" stands for "maximum", so the only way you should ever see packets with a length <em>greater than</em> the MTU is if packets are being handed to the capture mechanism <em>after</em> TCP reassembly, for example, if the network adapter is doing TCP reassembly (TCP reassembly offloading) or if the kernel is not directly handing received packets to the capture mechanism but is, instead, handing the results of TCP reassembly to the capture mechanism.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '17, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61416" class="comments-container"><span id="61434"></span><div id="comment-61434" class="comment"><div id="post-61434-score" class="comment-score"></div><div class="comment-text"><p>but that's not how tcpprobe works.</p></div><div id="comment-61434-info" class="comment-info"><span class="comment-age">(16 May '17, 08:04)</span> armodes</div></div><span id="61439"></span><div id="comment-61439" class="comment"><div id="post-61439-score" class="comment-score"></div><div class="comment-text"><p>"probe" and "dump" are different words; why does the way that tcpprobe work matter here?</p></div><div id="comment-61439-info" class="comment-info"><span class="comment-age">(16 May '17, 11:17)</span> Guy Harris ♦♦</div></div><span id="61467"></span><div id="comment-61467" class="comment"><div id="post-61467-score" class="comment-score"></div><div class="comment-text"><p>because i want to infer the congestion window of the sender from the traffic that we capture</p></div><div id="comment-61467-info" class="comment-info"><span class="comment-age">(17 May '17, 17:58)</span> armodes</div></div><span id="61468"></span><div id="comment-61468" class="comment"><div id="post-61468-score" class="comment-score"></div><div class="comment-text"><p>Then you definitely need something that works differently from <a href="https://wiki.linuxfoundation.org/networking/tcpprobe">tcp_probe</a>, because the tcp_probe kernel module works by "inserting a hook into the tcp_recv processing path" on the machine on which you're running it - if you want to infer the congestion window <em>purely from network traffic</em>, you need something different. (It's like trying to diagnose a medical disorder without actually being able to do tests on the patient.)</p><p>I.e., the tcp_probe kernel module has access to the connection state on that machine - it can just get the congestion window from the kernel TCP code's data structure. Programs that capture network traffic do <strong><em>NOT</em></strong> have access to kernel state information, so they must <em>infer</em> it. It's <em>literally impossible</em> for tcpdump or TShark or Wireshark or any other network analyzer to work like a Linux kernel module such as tcp_probe.</p><p>So you'll have to capture whatever traffic is needed for whatever code you're going to use to read the capture and infer the congestion window (the congestion window is <em>not</em> something that's transmitted over the wire!), and, if you're going to use a capture filter, you'll have to use a capture filter that captures the traffic you need. <code>tcp and dst host 10.0.0.1</code> will capture packets sent <em>to</em> 10.0.0.1; <code>tcp and src host 10.0.0.1</code> will capture packets sent <em>from</em> 10.0.0.1; <code>tcp and host 10.0.0.1</code> will capture packets sent to <em>or</em> from 10.0.0.1.</p></div><div id="comment-61468-info" class="comment-info"><span class="comment-age">(17 May '17, 18:21)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61416" class="comment-tools"></div><div class="clear"></div><div id="comment-61416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

