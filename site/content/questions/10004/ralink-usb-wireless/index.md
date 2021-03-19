+++
type = "question"
title = "Ralink usb wireless"
description = '''I have a USB Dongle WIFI Device. - DEVICE INSTANCE = USB&#92;VID_148F&amp;amp;PID_3070&#92;1.0 (which translates to) RAILINK RT3070 Which integrates a CMOS RF, MAC, Baseband and USB interface into a single-chip. They fully comply with IEEE 802.11a/b/g/n and IEEE 802.11b/g/n Drivers are Ralink - UTILITY = 4.1.3....'''
date = "2012-04-06T23:29:00Z"
lastmod = "2012-04-07T00:35:00Z"
weight = 10004
keywords = [ "capture-setup" ]
aliases = [ "/questions/10004" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ralink usb wireless](/questions/10004/ralink-usb-wireless)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10004-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a USB Dongle WIFI Device. - DEVICE INSTANCE = USB\VID_148F&amp;PID_3070\1.0<br />
(which translates to)<br />
RAILINK RT3070<br />
Which integrates a CMOS RF, MAC, Baseband and USB interface into a single-chip.<br />
They fully comply with IEEE 802.11a/b/g/n and IEEE 802.11b/g/n<br />
Drivers are Ralink - UTILITY = 4.1.3.0<br />
DRIVER = 3.2.4.0<br />
SDK = 1.1.2.0<br />
Shows up as "Wireless Network Connection 8" at Windoze level.<br />
Wireshark see's it as "IEEE 802.11 Wireless Card(Mircosoft Packet Schedular)"<br />
I am running win/xp pro - ver 2002<br />
service pack 3<br />
Running Wireshark gives an error; - The capture session could not be initiated<br />
(failed to set hardware filter to promiscuous mode).<br />
Please check that<br />
"\Device\NPF_{E5B3D4C9-249B-409F-BDCC-5A9881706AA8}" is the proper interface.<br />
Help can be found at:<br />
<a href="http://wiki.wireshark.org/WinPcap">http://wiki.wireshark.org/WinPcap</a><br />
<a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a><br />
WireShark help seems to indicate, USB devices can't be monitored in Windoze - which leaves me very confused since my Air-Pcap USB DONGLE works just fine under XP.<br />
What does Air-Pcap have Ralink dosen't???<br />
Can Ralink RT3070 device be made to work with WireShark???<br />
GPW would like to Know.</p></div><div id="question-tags" class="tags-container tags">capture-setup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '12, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/e9068dc2f9d80c3e987612e5f8759cb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roboprogramer&#39;s gravatar image" /><p>roboprogramer<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roboprogramer has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-10004" class="comments-container"></div><div id="comment-tools-10004" class="comment-tools"></div><div class="clear"></div><div id="comment-10004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10006"></span>

<div id="answer-container-10006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10006-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It should perhaps also have directed you to <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a>, which says</p><blockquote><p><strong>Windows</strong></p><p>Capturing WLAN traffic on Windows depends on WinPcap and on the underlying network adapters and drivers. Unfortunately, most drivers/adapters support neither monitor mode, nor seeing 802.11 headers when capturing, nor capturing non-data frames.</p><p>Promiscuous mode can be set; unfortunately, it's often crippled. In this mode many drivers don't supply packets at all, or don't supply packets sent by the host.</p><p><strong>If you experience any problems capturing packets on WLANs, try to switch promiscuous mode off.</strong> In this case you will have to capture traffic on the host you're interested in.</p></blockquote><p>This is because:</p><ol><li>WinPcap uses version 5, rather than version 6, of the "NDIS" interface for connecting to the Windows networking stack, and NDIS version 5 doesn't support "native Wi-Fi" and thus doesn't support "monitor mode";</li><li>even if it did support NDIS version 6, Windows XP doesn't, so you'd have to run Vista or 7 to get that;</li><li>Microsoft's specifications for Wi-Fi drivers, as I remember, essentially say that promiscuous mode is not allowed to work.</li></ol><p>AirPcap devices aren't regular Wi-Fi adapters; they're special devices for passively capturing Wi-Fi traffic, so they don't use the "NDIS" interface, and thus can do things you can't do with WinPcap and regular Wi-Fi adapters.</p><p>Other operating systems, such as Linux, and {Free,Net,Open,DragonFly}BSD, don't have those limitations; an RT3070 device <em>might</em> support capturing in monitor mode, depending on the capabilities of the hardware and the driver.</p><p>If all you want to do is capture traffic to and from your machine, <em>that</em> should work even on Windows - just turn promiscuous mode off and see whether that works.</p><p>(As for USB, if the Wireshark help referred you to, or said something similar to, what <a href="http://wiki.wireshark.org/CaptureSetup/USB">http://wiki.wireshark.org/CaptureSetup/USB</a> said, what it's saying is not that you can't capture on USB network adapters - Wireshark doesn't know anything special about USB network adapters, and neither does WinPcap or even the Windows networking stack, so they can't distinguish USB adapters from, for example, PCI adapters - it's saying that you can't capture <em>raw USB traffic at the bus level</em> on Windows the way you can on Linux.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '12, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-10006" class="comments-container"><span id="10081"></span><div id="comment-10081" class="comment"><div id="post-10081-score" class="comment-score"></div><div class="comment-text"><p>Thanks on the USB and “raw” clarification, that one didn’t sink in at all. I see it now as I read between the lines.</p><p>I finally caught the fact that I had set my capture templates for capturing with “promiscuous mode” on as a default.</p><p>I haven’t been in that area for a long time and forgot about it. Every adapter I have tried for a very long time</p><p>worked with this mode “default on” and the Ralink RT3070 has been the first to complain.</p><p>Now that I remember how/where to turned it off, it appears to work ok. Now I can start to figure out why I</p><p>can’t get any throughput using this interface.</p><p>Sure don’t like the massive duplicate packet storms I am seeing with this USB chip.</p><p>Thanks for the reply. It’s solved.</p><p>(Hope this formatting holds. It didn't on the question. Hope it's readable if it doesn't.) Here goes.</p></div><div id="comment-10081-info" class="comment-info"><span class="comment-age">(11 Apr '12, 22:06)</span> roboprogramer</div></div><span id="10082"></span><div id="comment-10082" class="comment"><div id="post-10082-score" class="comment-score"></div><div class="comment-text"><p>P.S. how come award points don't seem to work. Could not award any.</p></div><div id="comment-10082-info" class="comment-info"><span class="comment-age">(11 Apr '12, 22:13)</span> roboprogramer</div></div><span id="10088"></span><div id="comment-10088" class="comment"><div id="post-10088-score" class="comment-score"></div><div class="comment-text"><p>@roboprogramer</p><p>I converted your "answer" to a comment as this is a Q&amp;A site not a forum, please see the <a href="http://ask.wireshark.org/faq/">FAQ</a>.</p><p>To "award" points, just accept the answer given by clicking on the "check" mark icon at the start of the answer.</p></div><div id="comment-10088-info" class="comment-info"><span class="comment-age">(12 Apr '12, 02:27)</span> grahamb ♦</div></div></div><div id="comment-tools-10006" class="comment-tools"></div><div class="clear"></div><div id="comment-10006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

