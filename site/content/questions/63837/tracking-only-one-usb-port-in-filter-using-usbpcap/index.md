+++
type = "question"
title = "Tracking only one USB Port in Filter using USBPcap"
description = '''I want to capture only one USB Port but I get the traffic from all other ports in the filter which confuses my project. Any solution for this?'''
date = "2017-10-12T03:14:00Z"
lastmod = "2017-10-12T06:28:00Z"
weight = 63837
keywords = [ "filter", "usbpcap", "usb" ]
aliases = [ "/questions/63837" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tracking only one USB Port in Filter using USBPcap](/questions/63837/tracking-only-one-usb-port-in-filter-using-usbpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63837-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture only one USB Port but I get the traffic from all other ports in the filter which confuses my project. Any solution for this?</p></div><div id="question-tags" class="tags-container tags">filter usbpcap usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '17, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/680eda71b2bfea24fc09f6608e86f25c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saisudheer8&#39;s gravatar image" /><p>saisudheer8<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saisudheer8 has no accepted answers">0%</span></p></div></div><div id="comments-container-63837" class="comments-container"></div><div id="comment-tools-63837" class="comment-tools"></div><div class="clear"></div><div id="comment-63837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63842"></span>

<div id="answer-container-63842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63842-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on what you call "port". The tree topology of the USB allows to connect several hubs in a chain, and there is no static mapping of physical ports of the hubs to USB addresses of connected devices.</p><p>The only thing resembling a capture filter to be available in USBPcap is the choice of root hub on which to capture. When running USBPcapCmd from command line, it is mandatory to choose a root hub. When running USBPcap from Wireshark or tshark, each root hub is offered as a separate extcap interface. Full stop.</p><p>(To make things even more confusing, a USB device connected to the very same physical port is seen as connected to one root hub if it is a USB 1.1/2.0 device but as connected to another root hub if it is a USB 3.0 device).</p><p>The mapping between physical USB ports of the computer and/or of external hubs and the USB address (bus.device.endpoint) is dynamically created during the enumeration phase. So if you have two USB keyboards and insert them in different order after restart of the computer, their USB addresses differ between cases.</p><p>So your best bet is to run USBPcapCmd.exe before inserting the devices you want to capture, and to analyse the enumeration phase to identify the bus and device IDs you'll use in your display filter expression to show only frames to/from the devices you are interested in. If necessary, you can save only frames matching the display filter into another .pcap file.</p><p>If you need your "project" to handle .pcap files fully automatically, without any manual pre-processing, you'll have to include analysis of the enumeration phase or some heuristic into it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '17, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63842" class="comments-container"><span id="63843"></span><div id="comment-63843" class="comment"><div id="post-63843-score" class="comment-score"></div><div class="comment-text"><p>To elaborate more on what I meant by "port", I have 3 root hubs and under my root hub 3, there are 6 ports which are specified in USBPcapCmd.exe as [Port 1], [Port 2], ... [Port 6]. I am interested only in [Port 4].</p><p>I can filter out the captured packets in Wireshark. However, I have limited knowledge on how to apply display filter expression in USBPcapCmd.exe. It would be very helpful if you can share a manual or example.</p></div><div id="comment-63843-info" class="comment-info"><span class="comment-age">(12 Oct '17, 06:52)</span> saisudheer8</div></div><span id="63846"></span><div id="comment-63846" class="comment"><div id="post-63846-score" class="comment-score"></div><div class="comment-text"><p>Seems I wasn't clear enough to ground your optimism. There seems to be no (0) way to apply a display filter directly in USBPcapCmd.exe. You have to capture everything what runs through the chosen root hub into a .pcap file, and apply the display filter in Wireshark/tshark when processing that .pcap file further.</p><p>Maybe Desowin has implemented some finer capture filter but he hasn't documented it. I was unable to find anything at all in his code when dealing with another issue, you may be more successful <a href="https://github.com/desowin/usbpcap">here</a>.</p><p>Also, you cannot display-filter up to physical port number because USBPcap does not store the information about physical port(s) of the hub(s) as metadata into the .pcap file as there is no space reserved for that purpose. This could be theoretically possible if USBPcap would use .pcapng format and translate such data into a text string such as "USB physical address 1.2.1.3.4" and store the string as interface name but it currently doesn't.</p></div><div id="comment-63846-info" class="comment-info"><span class="comment-age">(12 Oct '17, 07:35)</span> sindy</div></div><span id="63847"></span><div id="comment-63847" class="comment"><div id="post-63847-score" class="comment-score"></div><div class="comment-text"><p>Got you! Thanks for the detailed explanation <a href="https://ask.wireshark.org/users/19586/sindy">@sindy</a>. I will filter out the necessary info in Wireshark. You guys are the best!</p></div><div id="comment-63847-info" class="comment-info"><span class="comment-age">(12 Oct '17, 07:56)</span> saisudheer8</div></div><span id="63849"></span><div id="comment-63849" class="comment"><div id="post-63849-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/43550/saisudheer8">@saisudheer8</a></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-63849-info" class="comment-info"><span class="comment-age">(12 Oct '17, 09:12)</span> grahamb ♦</div></div></div><div id="comment-tools-63842" class="comment-tools"></div><div class="clear"></div><div id="comment-63842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

