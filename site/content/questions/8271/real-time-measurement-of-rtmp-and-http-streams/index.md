+++
type = "question"
title = "Real Time measurement of RTMP and HTTP streams"
description = '''Hello, I&#x27;m now looking into WireShark with hope that it will have the capability to display an incoming stream&#x27;s bit rate for RTMP and HTTP. In reading the User Guide I see that it has; Statistic infos: -y display average data rate (in bytes/sec) -i display average data rate (in bits/sec) -z display...'''
date = "2012-01-07T19:44:00Z"
lastmod = "2012-01-08T14:41:00Z"
weight = 8271
keywords = [ "http", "bitrate", "rtmp" ]
aliases = [ "/questions/8271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Real Time measurement of RTMP and HTTP streams](/questions/8271/real-time-measurement-of-rtmp-and-http-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8271-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm now looking into WireShark with hope that it will have the capability to display an incoming stream's bit rate for RTMP and HTTP. In reading the User Guide I see that it has; Statistic infos: -y display average data rate (in bytes/sec) -i display average data rate (in bits/sec) -z display average packet size (in bytes) -x display average packet rate (in packets/sec) This seems to be what I am looking for. Am I correct on this assumption? I searched the User Guide for information on RTMP and did not find any information on this. Why doesn't WireShark mention RTMP? What does Broadcom Netlink have to do with WireShark? Thank you for your response. will</p></div><div id="question-tags" class="tags-container tags">http bitrate rtmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '12, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/6c566db4ab452f1914ca1a13e35151ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="will&#39;s gravatar image" /><p>will<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="will has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 21:00</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8271" class="comments-container"></div><div id="comment-tools-8271" class="comment-tools"></div><div class="clear"></div><div id="comment-8271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8279"></span>

<div id="answer-container-8279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8279-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's not a question, that's three questions.</p><p>The answer to the first question is "No. Those are command-line options for the capinfos command; that command does <em>NOT</em> dissect packets, and knows nothing whatsoever about TCP connections, much less about RTMP or HTTP streams."</p><p>The answer to the second question is "The same question could be asked about many of the other thousand or so protocols Wireshark supports. If it doesn't do anything other than dissect a protocol, there's not much for the User's Guide to say about the protocol."</p><p>The answer to the third question is "It's an Ethernet network adapter card, and Wireshark can capture on Ethernets using libpcap/WinPcap and an Ethernet network adapter card."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '12, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8279" class="comments-container"><span id="8280"></span><div id="comment-8280" class="comment"><div id="post-8280-score" class="comment-score"></div><div class="comment-text"><p>Guy Harris, thank you for answering the three questions. About the third question/answer; "It's an Ethernet network adapter card, and Wireshark can capture on Ethernets using libpcap/WinPcap and an Ethernet network adapter card." If I install WinPCap/NDF will WireShark be able to display the incoming stream rate for RTMP and HTTP video streams? I greatly appreciate your expertise.</p></div><div id="comment-8280-info" class="comment-info"><span class="comment-age">(08 Jan '12, 16:58)</span> will</div></div><span id="8283"></span><div id="comment-8283" class="comment"><div id="post-8283-score" class="comment-score"></div><div class="comment-text"><p>I assume by "NDF" you mean "NPF", which stands for Network Packet Filter, <a href="http://www.winpcap.org/docs/docs_412/html/group__NPF.html">the kernel portion of WinPcap</a>. So "[installing] WinPcap/NDF" is really just "installing WinPcap" (which is done by default when you install Wireshark on Windows).</p><p>Installing WinPcap makes no difference for displaying the incoming stream rate; it just controls whether Wireshark can capture network traffic on Windows.</p><p>Wireshark currently has no statistic to calculate streaming rates for RTMP or HTTP; installing WinPcap won't make a difference.</p></div><div id="comment-8283-info" class="comment-info"><span class="comment-age">(09 Jan '12, 11:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8279" class="comment-tools"></div><div class="clear"></div><div id="comment-8279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

