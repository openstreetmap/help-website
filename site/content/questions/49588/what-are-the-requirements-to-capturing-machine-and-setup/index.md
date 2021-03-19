+++
type = "question"
title = "What are the requirements to capturing machine and setup?"
description = '''let&#x27;s assume I have the proper (capable) NIC and CPU power needed.  nearly nothing is running on the machine.  (which will be best to monitor via? tap or span?) would it be able to handle a 10Gbps network rate ? afterwards, lets assume I also run some investigator (such as NetWitness Investigator) o...'''
date = "2016-01-28T04:29:00Z"
lastmod = "2016-01-28T08:38:00Z"
weight = 49588
keywords = [ "setup", "bandwidth", "resources" ]
aliases = [ "/questions/49588" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What are the requirements to capturing machine and setup?](/questions/49588/what-are-the-requirements-to-capturing-machine-and-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49588-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>let's assume I have the proper (capable) NIC and CPU power needed. nearly nothing is running on the machine.</p><p>(which will be best to monitor via? tap or span?)</p><p>would it be able to handle a 10Gbps network rate ?</p><p>afterwards, lets assume I also run some investigator (such as NetWitness Investigator) on the machine. would Wireshark still be able to handle the network rate?</p></div><div id="question-tags" class="tags-container tags">setup bandwidth resources</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '16, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/29612e08852632502d03e114c0ac462c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n2disk&#39;s gravatar image" /><p>n2disk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n2disk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 28 Jan '16, 04:45</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49588" class="comments-container"><span id="49590"></span><div id="comment-49590" class="comment"><div id="post-49590-score" class="comment-score"></div><div class="comment-text"><p>@n2disk, what you wrote was definitely not an Answer to your older Question. It could have been a Comment, but it seemed to me it would serve you better to convert it into a new Question rather than a Comment to an Answer to the original one.</p></div><div id="comment-49590-info" class="comment-info"><span class="comment-age">(28 Jan '16, 04:47)</span> sindy</div></div><span id="49591"></span><div id="comment-49591" class="comment"><div id="post-49591-score" class="comment-score"></div><div class="comment-text"><p>Of course, if you don't like my title, you can use "edit" to change it to a more appropriate one.</p></div><div id="comment-49591-info" class="comment-info"><span class="comment-age">(28 Jan '16, 04:48)</span> sindy</div></div></div><div id="comment-tools-49588" class="comment-tools"></div><div class="clear"></div><div id="comment-49588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49593"></span>

<div id="answer-container-49593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you ask about "which will be best method of monitoring, span or tap", I guess you need to monitor a single link of 10 Gbps, not a complete traffic of a switch with several 10 Gbps traffic ports on it. If this is true, then a tap has a lower potential of errors than a span port. There is <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">a whole page dedicated to the details on Wireshark wiki</a>.</p><p>If by chance you had in mind capturing on a switch where multiple 10 Gbit/s ports are in use, a single 10 Gbit/s SPAN port is quite likely to be overbooked - but as a single tap is not applicable at all for such case, I guess you didn't have this in mind.</p><p>But regardless whether you use SPAN on a switch or a tap, you need <em>two</em> 10 Gbit/s ports on the capturing machine to be able to capture all traffic from a single full-duplex 10 Gbit/s line (and, logically, also two SPAN ports on the switch. Taps usually come with one mirror port for each direction).</p><p>Wireshark or tshark do much more than just capture, and so does the "investigator" software. So if you do not need to analyse your captured traffic online and round-the-clock, your best bet is to use only dumpcap, which just saves the captured packets into a file and does not analyse them at all (except that you may use capture filter to prevent some packets from being saved to the file). This reduces the CPU requirements to an absolute minimum, and also switches off any memory problems, as @Jasper has explained in <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">this nice article</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49593" class="comments-container"><span id="49600"></span><div id="comment-49600" class="comment"><div id="post-49600-score" class="comment-score"></div><div class="comment-text"><p>Thank you for you answer.</p><p>as you were saying, I'm monitoring on a single link of 10 Gbps.</p><p>I'm afraid I wasn't clear about my question. My main goal is to monitor and save ALL(!) my network traffic and later analyze the captured .pcap (I could use an On-The-Fly indexing but I don't think Wireshark support it).</p><p>what will be the best way to do so, while supporting 10Gbps network rate (on a single link as you suggested) if even possible with Wireshark.</p></div><div id="comment-49600-info" class="comment-info"><span class="comment-age">(28 Jan '16, 08:22)</span> n2disk</div></div><span id="49603"></span><div id="comment-49603" class="comment"><div id="post-49603-score" class="comment-score"></div><div class="comment-text"><p>OK. In modern servers, the network cards use direct memory access to store packets, and the hard disk controllers use direct memory access to retrieve data; the CPU just organizes that process but does not need to touch every single byte. So you need some 3 GByte/s minimum transfer rate of your disk and preferably a hardware architecture where the network cards' operation does not interfere with disk controller operation, and also about 3 Gbytes of disk space for each second of your intended capture. Or, seen from the other end, a 1 TB disk is sufficient for about 330 seconds of capture, which is just about 5 minutes. Logically, the disk must be connected to the capturing machine using a faster interface than a 10 Gbit/s Ethernet, so use of network storage to have sufficient capacity would need even faster links to be used. Is all this (disk capacity and available channel bandwidth) a non-issue for you?</p><p>You can get at half of those values if you capture each direction separately and merge them later.</p></div><div id="comment-49603-info" class="comment-info"><span class="comment-age">(28 Jan '16, 08:45)</span> sindy</div></div></div><div id="comment-tools-49593" class="comment-tools"></div><div class="clear"></div><div id="comment-49593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49602"></span>

<div id="answer-container-49602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49602-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds to me that you are trying to capture and analyze a large amount of data. I would recommend to investigate other solutions rather than Wireshark.<br />
</p><p>I write this knowing that I might get some negative feedback from the Wireshark community. However, there seems to be two different types of thinking when it comes to capturing and analyzing network traffic:</p><ol><li>Macro-capturing = the need to capture all traffic and analyze a large amount of data. This type of capturing is done by IT departments to ensure connectivity across the network. There are many solutions for this need, but nearly all require some type of purchase (i.e., you need to spend some money to get the correct hardware, software and post-analysis tools). For example, NetScout and Savvius are 2 companies that provide these types of products.</li><li>Micro-capturing = the need to capture specific traffic between two devices (or a few devices) and analyze the stream from a particular device. This type of capturing is mainly done by development and testing teams to ensure proper communication and protocol analysis. The best solution for this type of need is Wireshark.</li></ol><p>If you are trying to capture a 10Gbps link over an extended time, you might want to investigate option one further.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></p></div></div><div id="comments-container-49602" class="comments-container"><span id="49612"></span><div id="comment-49612" class="comment"><div id="post-49612-score" class="comment-score"></div><div class="comment-text"><p>No negative feedback allowed on this comment, as it is essentially correct. Always use the right tool for the job, and these cases require such distinction.</p></div><div id="comment-49612-info" class="comment-info"><span class="comment-age">(28 Jan '16, 13:57)</span> Jaap ♦</div></div></div><div id="comment-tools-49602" class="comment-tools"></div><div class="clear"></div><div id="comment-49602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

