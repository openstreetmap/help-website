+++
type = "question"
title = "pcapng file from Raspberry Pi not readable on Ubuntu machine"
description = '''Hi all I&#x27;ve the following scenario:  I&#x27;ve Raspberry Pi (arm architecture) running Kali Linux where I launch tshark in order to capture net packets using followin command:  tshark -i eth0 -F pcapng -w capture.pcap -a duration:600   Once done, I&#x27;ve capure.pcap file containing all the packets readable ...'''
date = "2014-06-18T14:37:00Z"
lastmod = "2014-06-18T16:13:00Z"
weight = 33942
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/33942" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [pcapng file from Raspberry Pi not readable on Ubuntu machine](/questions/33942/pcapng-file-from-raspberry-pi-not-readable-on-ubuntu-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33942-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I've the following scenario: I've Raspberry Pi (arm architecture) running Kali Linux where I launch tshark in order to capture net packets using followin command: <code> tshark -i eth0 -F pcapng -w capture.pcap -a duration:600 </code> Once done, I've <strong>capure.pcap</strong> file containing all the packets readable from raspberry.</p><p>Well, if I move <strong>capture.pcap</strong> on Ubuntu 13.10 x64 , both Wireshark and tshark told me that <strong>capture.pcap</strong> is not recognized.</p><p>Same issue on viceversa.</p><p>Any idea?</p><p>thx</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '14, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/ba32dee00b2d8fb7e4bfbfca582c3948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blaskino&#39;s gravatar image" /><p>blaskino<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blaskino has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '14, 16:14</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-33942" class="comments-container"><span id="33943"></span><div id="comment-33943" class="comment"><div id="post-33943-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Well, if I move capture.pcap on Ubuntu 13.10 x64</p></blockquote><p>How do you <strong>move</strong> the file?</p><p>What is the output of the following commands</p><blockquote><p>file capture.pcap<br />
capinfos capture.pcap</p></blockquote></div><div id="comment-33943-info" class="comment-info"><span class="comment-age">(18 Jun '14, 15:33)</span> Kurt Knochner ♦</div></div><span id="33944"></span><div id="comment-33944" class="comment"><div id="post-33944-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, first of all thx for the answer. I move the <strong>capture.pcap</strong> file via ftp.<br />
The output of <strong>file capture.pcap</strong> is:<br />
<code> capture.cap: pcap-ng capture file - version 1.0</code></p><p>and the output of <strong>capinfos capture.pcap</strong> is:<br />
<code> File name:           capture.cap File type:           Wireshark/... - pcapng File encapsulation:  Ethernet Packet size limit:   file hdr: (not set) Number of packets:   4215  File size:           792 kB Data size:           651 kB Capture duration:    61 seconds Start time:          Wed Jun 18 21:53:35 2014 End time:            Wed Jun 18 21:54:36 2014 Data byte rate:      10 kBps Data bit rate:       85 kbps Average packet size: 154,52 bytes Average packet rate: 69 packets/sec SHA1:                a49d26d9cc4449eb71387372cc526e270eafc513 RIPEMD160:           11f4a65bb100b8137c24198a664a22ebf4ed3ccc MD5:                 7a0e43b3fae414638ca1da1be6e1f25f Strict time order:   True</code></p><p><code></code></p><p><code></code><br />
</p><p>Thanks again!</p></div><div id="comment-33944-info" class="comment-info"><span class="comment-age">(18 Jun '14, 15:44)</span> blaskino</div></div></div><div id="comment-tools-33942" class="comment-tools"></div><div class="clear"></div><div id="comment-33942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33945"></span>

<div id="answer-container-33945" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33945-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So that's the output of <code>capinfos capture.pcap</code> on the Raspberry Pi?</p><p>When you FTPed the capture file, did the FTP program indicate whether it was transferred in ASCII mode (which will <strong><em>NOT</em></strong> work - the copy will not be an exact copy and will not be readable) or in binary mode (which should work)?</p><p>What does <code>od -bc capture.pcap | head</code> print on the Ubuntu system?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '14, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-33945" class="comments-container"><span id="33948"></span><div id="comment-33948" class="comment"><div id="post-33948-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, yes, capinfos' output is on Raspberry Pi.<br />
</p><p>The output of <code> od -bc capture.pcap | head</code><br />
on the ubuntu system is:<br />
<code> 0000000 012 015 015 012 144 000 000 000 115 074 053 032 001 000 000 000          \n  \r  \r  \n   d  \0  \0  \0   M   &lt;   + 032 001  \0  \0  \0 0000020 377 377 377 377 377 377 377 377 003 000 014 000 114 151 156 165         377 377 377 377 377 377 377 377 003  \0  \f  \0   L   i   n   u 0000040 170 040 063 056 061 063 056 060 004 000 057 000 104 165 155 160           x       3   .   1   3   .   0 004  \0   /  \0   D   u   m   p 0000060 143 141 160 040 061 056 061 060 056 062 040 050 123 126 116 040           c   a   p       1   .   1   0   .   2       (   S   V   N   0000100 122 145 166 040 065 061 071 063 064 040 146 162 157 155 040 057           R   e   v       5   1   9   3   4       f   r   o   m       /</code></p><p><code></code></p><p><code></code></p><p>Thanx, now I check the transfer mode on ftp. I'll try also to get the file using a pendrive.</p></div><div id="comment-33948-info" class="comment-info"><span class="comment-age">(18 Jun '14, 23:05)</span> blaskino</div></div><span id="33950"></span><div id="comment-33950" class="comment"><div id="post-33950-score" class="comment-score"></div><div class="comment-text"><p>Solved! It's a matter of file trasfer as you said. Setting up ftp to binary mode both on client and server solved the issue.</p><p>Thanks again to <a href="http://ask.wireshark.org/users/79/guy-harris">Guy</a> and <a href="http://ask.wireshark.org/users/2593/kurt-knochner">Kurt</a></p></div><div id="comment-33950-info" class="comment-info"><span class="comment-age">(19 Jun '14, 00:57)</span> blaskino</div></div><span id="33963"></span><div id="comment-33963" class="comment"><div id="post-33963-score" class="comment-score">1</div><div class="comment-text"><p>@blaskino</p><p>I've moved around the comments and "answers" to create an actual answer.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-33963-info" class="comment-info"><span class="comment-age">(19 Jun '14, 11:14)</span> grahamb ♦</div></div></div><div id="comment-tools-33945" class="comment-tools"></div><div class="clear"></div><div id="comment-33945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

