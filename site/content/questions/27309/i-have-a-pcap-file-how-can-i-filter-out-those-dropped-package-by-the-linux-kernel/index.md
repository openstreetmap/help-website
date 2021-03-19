+++
type = "question"
title = "I have a pcap file. how can I filter out those dropped package by the linux kernel?"
description = '''Recently, I find one of my server face a drop package problem in a specific minute  netstat -in Kernel Interface table Iface MTU Met RX-OK RX-ERR RX-DRP RX-OVR TX-OK TX-ERR TX-DRP TX-OVR Flg bond0 1500 0 1418046670 0 743 0 1047132418 0 0 0 BMmRU bond1 1500 0 92980025302 3 79 0 54995070900 0 0 0 BMmR...'''
date = "2013-11-24T08:14:00Z"
lastmod = "2013-11-24T08:28:00Z"
weight = 27309
keywords = [ "drop", "tcpdump" ]
aliases = [ "/questions/27309" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I have a pcap file. how can I filter out those dropped package by the linux kernel?](/questions/27309/i-have-a-pcap-file-how-can-i-filter-out-those-dropped-package-by-the-linux-kernel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27309-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently, I find one of my server face a drop package problem in a specific minute</p><hr /><pre><code>netstat -in
Kernel Interface table
Iface       MTU Met    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
bond0      1500   0 1418046670      0    743      0 1047132418      0      0      0 BMmRU
bond1      1500   0 92980025302      3     79      0 54995070900      0      0      0 BMmRU
eth0       1500   0 924882226      0      0      0 761949059      0      0      0 BMsRU
eth1       1500   0 493164444      0    743      0 285183359      0      0      0 BMsRU
eth4       1500   0 92979828163      3     79      0 54995070878      0      0      0 BMsRU
eth5       1500   0   197139      0      0      0       22      0      0      0 BMsRU
lo        16436   0 37524597      0      0      0 37524597      0      0      0 LRU</code></pre><hr /><p>I have use following tcpdump to capture the the eth1 traffic during that minute.</p><pre><code>tcpdump -i eth1 -w /tmp/drop_find.pcap</code></pre><p>How can I filter out the dropped package by the kernel or something else in this pcap file using wireshark?</p><p>Or how do I know which package is dropped by the destination? can those dropped package by destination can be captured by tcpdump?</p></div><div id="question-tags" class="tags-container tags">drop tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '13, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/3dba745953c129c5c1b2713010991dd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newcryout&#39;s gravatar image" /><p>newcryout<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newcryout has no accepted answers">0%</span></p></div></div><div id="comments-container-27309" class="comments-container"><span id="27310"></span><div id="comment-27310" class="comment"><div id="post-27310-score" class="comment-score"></div><div class="comment-text"><p>here is the uploaded tcpdump pcap file.</p><p><a href="http://pan.baidu.com/s/1mXL1k">drop_link.pcap</a></p></div><div id="comment-27310-info" class="comment-info"><span class="comment-age">(24 Nov '13, 08:28)</span> newcryout</div></div></div><div id="comment-tools-27309" class="comment-tools"></div><div class="clear"></div><div id="comment-27309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27311"></span>

<div id="answer-container-27311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27311-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I filter out the dropped package by the kernel or something else in this pcap file using wireshark?</p></blockquote><p>you probably can't, as the kernel might have dropped the packets due to a lack of buffer space. If that was the case, libpcap (the capture library of tcpdump) will never have seen those packets either, so those dropped packets are <strong>not</strong> in the capture file.</p><p>There is a small chance, that the packets have been dropped due to a frame checksum error. In that case you might (or might not) see those frames in the capture file. It depends where and when the kernel drops that kind of packets.</p><p>Please apply the following display filter: <code>expert.message contains "checksum"</code></p><blockquote><p>Or how do I know which package is dropped by the destination? can those dropped package by destination can be captured by tcpdump?</p></blockquote><p>To see those dropped frames you need to do this:</p><ul><li>capture all frames in <strong>front</strong> of the system, on a mirror/monitor port of the switch, with another PC</li><li>at the same time capture all frames <strong>on the system</strong> (with tcpdump)</li><li>compare the two capture files. Those frames that are in the 'external' capture file, but are missing in the 'internal' file, will be the dropped frames.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '13, 08:34</p></div></div><div id="comments-container-27311" class="comments-container"><span id="27312"></span><div id="comment-27312" class="comment"><div id="post-27312-score" class="comment-score"></div><div class="comment-text"><blockquote><p>here is the uploaded tcpdump pcap file.</p></blockquote><p>O.K. there are no checksum errors in that file, so I guess the dropped frames are being caused by missing buffer space at some time. In that case, please follow the procedure I mentioned.</p></div><div id="comment-27312-info" class="comment-info"><span class="comment-age">(24 Nov '13, 08:32)</span> Kurt Knochner ♦</div></div><span id="27313"></span><div id="comment-27313" class="comment"><div id="post-27313-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for the quick response. And you have give me a great idea of the mirror the port. before I do that, I have little more question for this drop package thing.</p><p>As you have mentioned that, when package drop because of lack of buffer and checksum. these package will never seen by tcpdump.</p><p>so if there is any other possibility that some package dropped by other reason can be seen by tcpdump (libpcap)?</p><p>or I can say, all the package dropped by the kernel will never be captured by tcpdump (libpacap)?</p><p>as I know all the tools used to capture package in linux are using the libpcap. I don't know if this libpcap can do some capture operation before linux kernel drop packages.</p><hr /><p>because this eth1 is a slave NIC for the bond0. the traffic in the eth1, should be very low. this can be confirm in the pcap file I have attached. so I think the kernel will not drop the package because of the out of buffer reason.</p></div><div id="comment-27313-info" class="comment-info"><span class="comment-age">(24 Nov '13, 09:08)</span> newcryout</div></div><span id="27318"></span><div id="comment-27318" class="comment"><div id="post-27318-score" class="comment-score"></div><div class="comment-text"><blockquote><p>so if there is any other possibility that some package dropped by other reason can be seen by tcpdump (libpcap)?</p></blockquote><p>I can't tell you. I have seen both cases. Packtes being dropped by the kernel were seen by libpcap and some were not depends on the reason for the drop.</p><blockquote><p>or I can say, all the package dropped by the kernel will never be captured by tcpdump (libpacap)?</p></blockquote><p>see above.</p><blockquote><p>so I think the kernel will not drop the package because of the out of buffer reason.</p></blockquote><p>Who knows. Maybe there was a microburst with lots of traffic to a multicast IP/MAC address and at some time your kernel buffer was filled for a short period of time.</p></div><div id="comment-27318-info" class="comment-info"><span class="comment-age">(24 Nov '13, 10:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27311" class="comment-tools"></div><div class="clear"></div><div id="comment-27311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

