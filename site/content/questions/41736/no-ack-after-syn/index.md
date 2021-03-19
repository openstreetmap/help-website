+++
type = "question"
title = "No ACK after SYN"
description = '''I have a hardware unit (192.168.98.1) and a PC (192.168.100.100). The unit contains a FTP client, trying to connect an FTP server on the PC. The unit sends a SYN command, but this command is never answered by the PC.  The PC is running Windows XP. Any idea why? Is there any log in the PC to determin...'''
date = "2015-04-23T12:00:00Z"
lastmod = "2015-04-28T11:26:00Z"
weight = 41736
keywords = [ "ack", "ftp", "syn" ]
aliases = [ "/questions/41736" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [No ACK after SYN](/questions/41736/no-ack-after-syn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41736-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a hardware unit (192.168.98.1) and a PC (192.168.100.100). The unit contains a FTP client, trying to connect an FTP server on the PC. The unit sends a SYN command, but this command is never answered by the PC.</p><p>The PC is running Windows XP.</p><p>Any idea why? Is there any log in the PC to determine if the SYN is received and decoded?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/New_Bitmap_Image_TWmJH2Uf.bmp" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ack ftp syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '15, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/9d214390e5bb9491264fc724da7ba128?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidFournier&#39;s gravatar image" /><p>DavidFournier<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidFournier has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '15, 14:29</p></div></div><div id="comments-container-41736" class="comments-container"><span id="41746"></span><div id="comment-41746" class="comment"><div id="post-41746-score" class="comment-score"></div><div class="comment-text"><p>Are the checksums IP and TCP correct?</p></div><div id="comment-41746-info" class="comment-info"><span class="comment-age">(23 Apr '15, 13:35)</span> mrEEde</div></div><span id="41783"></span><div id="comment-41783" class="comment"><div id="post-41783-score" class="comment-score"></div><div class="comment-text"><p>Yes TCP chcksum are correct.</p><p><strong><a href="http://1drv.ms/1boFByo">-&gt; Here is the pcapng file &lt;-</a></strong></p></div><div id="comment-41783-info" class="comment-info"><span class="comment-age">(24 Apr '15, 08:29)</span> DavidFournier</div></div></div><div id="comment-tools-41736" class="comment-tools"></div><div class="clear"></div><div id="comment-41736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="41928"></span>

<div id="answer-container-41928" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41928-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Problem solved: the issue was on the client side. The 2 padding bytes of the SYN packet's TCP header were corrupted and contained 0x64 0x64 instead of 0x00 0x00 or 0xFF 0xFF.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/9d214390e5bb9491264fc724da7ba128?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidFournier&#39;s gravatar image" /><p>DavidFournier<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidFournier has one accepted answer">100%</span></p></div></div><div id="comments-container-41928" class="comments-container"></div><div id="comment-tools-41928" class="comment-tools"></div><div class="clear"></div><div id="comment-41928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41742"></span>

<div id="answer-container-41742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41742-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One of the following things:</p><ul><li>the PC is offline</li><li>the local firewall of the PC blocks the request</li><li>a security device (e.g. firewall) between client and server blocks the request</li><li>an IP filter in the FTP server software blocks the request</li><li>the packets are lost somewhere on the way</li><li>One of the routers between client and server does not know a route to 192.168.100.x and drops the packet without sending any ICMP messages (or you did not capture those ICMP messages)</li><li>The client is using the wrong MAC address for the server (for whatever reason), if the subnet is 192.168.0.0/16</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '15, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '15, 12:34</p></div></div><div id="comments-container-41742" class="comments-container"><span id="41743"></span><div id="comment-41743" class="comment"><div id="post-41743-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, thanks for your help.</p><p>The unit and the PC are connected through a router, locally, but none of them are connected to a large 'network' (internet, intranet, etc..).</p><p>Since WireShark sees the SYN requests, it means they have reached the PC, right? So the packets are not dropped, or lost.</p></div><div id="comment-41743-info" class="comment-info"><span class="comment-age">(23 Apr '15, 12:43)</span> DavidFournier</div></div><span id="41744"></span><div id="comment-41744" class="comment"><div id="post-41744-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Since WireShark sees the SYN requests, it means they have reached the PC</p></blockquote><p>That's only the case if you cpatured on the PC!</p><p>If that's true, then it's either the local firewall or any other IP filter including endpoint security software or a filter in the FTP server software itself.</p><p>BTW: Is the PC multi-homed, meaning: Does it have multiple interfaces?</p></div><div id="comment-41744-info" class="comment-info"><span class="comment-age">(23 Apr '15, 12:45)</span> Kurt Knochner ♦</div></div><span id="41745"></span><div id="comment-41745" class="comment"><div id="post-41745-score" class="comment-score"></div><div class="comment-text"><p>Indeed the capture is done on the PC.</p><p>Also, the PC is multi-homed, but 2 out of the 3 interfaces are disabled to avoid interface confusion. Only the concerned one is enabled.</p><p>Are there any known implicit system IP filters?</p><p>The local firewall is disabled, just so you know.</p><p>Thanks again.</p></div><div id="comment-41745-info" class="comment-info"><span class="comment-age">(23 Apr '15, 13:06)</span> DavidFournier</div></div><span id="41757"></span><div id="comment-41757" class="comment"><div id="post-41757-score" class="comment-score"></div><div class="comment-text"><p>The connection establishment process is handled by the kernel. The FTP server process does not know that a SYN packet has been received. When connection establishment is complete, the FTP listener is notified by the kernel that a connection has been established. So if the FTP server was blocking the IP address we would see:</p><p>SYN SYN/ACK ACK RESET</p><p>If the FTP daemon/process is not running, the SYN packet should be responded to with a RESET.</p></div><div id="comment-41757-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:46)</span> Jim Aragon</div></div></div><div id="comment-tools-41742" class="comment-tools"></div><div class="clear"></div><div id="comment-41742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41785"></span>

<div id="answer-container-41785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The SYNs are probably discarded because the 'real' initial sequence number is zero. Also : The urgent pointer field is nonzero while the URG flag is not set</p><p>What a strange TCP stack ..</p><hr /><p>The "tcp port numbers reused" flag is a bug in wireshark. The client port numbers <em>are</em> incrementing, 5001 then 5002.<br />
In fact the first session in the trace is already flagged this way, maybe a problem with the port reuse detection algorithm when the initial sequence number is 0.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-222_eOrhdkU.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-223.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '15, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '15, 08:28</p></div></div><div id="comments-container-41785" class="comments-container"><span id="41787"></span><div id="comment-41787" class="comment"><div id="post-41787-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde. Is there a way to force the PC (Windows? Firewall?) to accept these packets, even if the sequence number is zero, and urgent pointer is nonzero?</p></div><div id="comment-41787-info" class="comment-info"><span class="comment-age">(24 Apr '15, 08:50)</span> DavidFournier</div></div><span id="41829"></span><div id="comment-41829" class="comment"><div id="post-41829-score" class="comment-score"></div><div class="comment-text"><p>I doubt that there is a way to accept those. There has been good reasons to use random initial sequence numbers. CERT Advisory CA-2001-09 Statistical Weaknesses in TCP/IP Initial Sequence Numbers <a href="http://www.cert.org/advisories/CA-2001-09.html">http://www.cert.org/advisories/CA-2001-09.html</a></p><p>So letting these connections in would impose a security risk ... What kind of hardware unit is this ?</p><p>If this is a Barco iCon H600 the problem might be fixed in INFOT V1.25 ... • ftp client hanging is solved</p><p><a href="http://www.barco.com/en/mybarco/mysupport/productsupport/documentation?productid=a42a61cc-33bd-4ed9-938a-3ee309098229">http://www.barco.com/en/mybarco/mysupport/productsupport/documentation?productid=a42a61cc-33bd-4ed9-938a-3ee309098229</a></p></div><div id="comment-41829-info" class="comment-info"><span class="comment-age">(25 Apr '15, 08:53)</span> mrEEde</div></div></div><div id="comment-tools-41785" class="comment-tools"></div><div class="clear"></div><div id="comment-41785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

