+++
type = "question"
title = "Acquire USB device signal without driver"
description = '''Hi, I&#x27;m new to USB sniffing, so please be patient! Here&#x27;s what I&#x27;m trying to achieve. I bought an electricity consumption monitoring system, MTP3100, http://www.mtpinc.com/Products.htm?CD=97&amp;amp;ID=616 A transmitter module reads my household electric consumption every 10 seconds, and sends it to the...'''
date = "2017-03-29T07:29:00Z"
lastmod = "2017-03-29T07:29:00Z"
weight = 60407
keywords = [ "sniffing", "raspbian", "driver", "usb", "mtp3100" ]
aliases = [ "/questions/60407" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Acquire USB device signal without driver](/questions/60407/acquire-usb-device-signal-without-driver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60407-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm new to USB sniffing, so please be patient!</p><p>Here's what I'm trying to achieve. I bought an electricity consumption monitoring system, MTP3100, <a href="http://www.mtpinc.com/Products.htm?CD=97&amp;ID=616">http://www.mtpinc.com/Products.htm?CD=97&amp;ID=616</a></p><p>A transmitter module reads my household electric consumption every 10 seconds, and sends it to the monitor, where it is refreshed every 10 seconds. The monitor stores a 2-year daily/weekly/monthly/yearly history, but does not save the real-time data (i.e. every 10 seconds).</p><p>On the other hand, it is possible to plug the monitor in a computer to download the history (not the real-time data), and also to display (yes, only display) the real-time consumption chart (yes you understood, every 10 seconds).</p><p>I wish to acquire the real-time data which is passed from the monitor to my computer and store it somehow in several files on my local server (managed by a raspberry pi). I know it sounds a bit freak to store 10-second data, but I want to see the impact of powering appliances, lowering the temperature overnight, etc. etc. Please do not reply "why the hell would you do that", or something along these lines, just assume I can handle all this data.</p><p>Here's the catch, the software and USB driver are only available for Windows. While my main computer can dual boot Mint/Win10, I'd wish to monitor my real-time consumption 24/7 on my raspberry Pi (OS is Raspbian).</p><p>So my questions,</p><ul><li>Would it be possible to sniff the USB traffic to acquire my real-time power usage (regardless of the OS, just seeing if this is feasible)</li><li>If this is feasible, can I acquire the USB traffic from a plugged device even though I have no installed driver for this device (since driver are windows only)</li><li>If I must use windows (which I fear will be the case), I guess I'll have to install a virtual machine on my Raspberry Pi with win7 or else, right?</li><li>In either cases (sniffing in Linux or Windows), what would be the best way to interpret and store the acquired data (generic guidelines would be much appreciated).</li></ul><p>Thanks to all for your advices.</p></div><div id="question-tags" class="tags-container tags">sniffing raspbian driver usb mtp3100</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '17, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/c70492e1435233ac7248f04ca8bbadd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="habskovy27&#39;s gravatar image" /><p>habskovy27<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="habskovy27 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '17, 07:51</p></div></div><div id="comments-container-60407" class="comments-container"></div><div id="comment-tools-60407" class="comment-tools"></div><div class="clear"></div><div id="comment-60407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

