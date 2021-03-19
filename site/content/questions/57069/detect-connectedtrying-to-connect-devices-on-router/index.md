+++
type = "question"
title = "Detect connected/trying to connect devices on router"
description = '''Hi, i am a student and completely new to wire shark, i need some assistance in a project. I want to know that how can i use wire shark in order to detect devices that are connected to my router and that are trying to connect my router.(frankly i actually don&#x27;t know if we can do it using wire shark o...'''
date = "2016-11-07T09:35:00Z"
lastmod = "2016-11-08T08:28:00Z"
weight = 57069
keywords = [ "router" ]
aliases = [ "/questions/57069" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Detect connected/trying to connect devices on router](/questions/57069/detect-connectedtrying-to-connect-devices-on-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i am a student and completely new to wire shark, i need some assistance in a project. I want to know that how can i use wire shark in order to detect devices that are connected to my router and that are trying to connect my router.(frankly i actually don't know if we can do it using wire shark or not, but a software "wireless network watcher" can easily detect connected devices so i thought it will also be possible on wire shark). What i already tried is npcap 0.10, but after installing it when i run wire shark, on initializing it kept on asking for admin permission, i had to force stop it, and since then wire shark isn't even showing available connections. If i have to use npcap then kindly tell me how to resolve my problem in 2nd part first.</p><p>*if i don't need to use npcap then no need to discuss second problem.</p><p>I have to submit my proposal within next 2 days so kindly help me fast.</p></div><div id="question-tags" class="tags-container tags">router</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/ea15d3aa8f9f1599053b7a1e5ca68e6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abdullah&#39;s gravatar image" /><p>Abdullah<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abdullah has no accepted answers">0%</span></p></div></div><div id="comments-container-57069" class="comments-container"><span id="57080"></span><div id="comment-57080" class="comment"><div id="post-57080-score" class="comment-score">1</div><div class="comment-text"><p>Is your intention to run the detection software at the router itself or to monitor the traffic "in the air" by another equipment next to the router? If the latter and if the monitoring machine should be a Windows one, you have to use npcap and, on top of it, a WLAN adaptor which properlys support promiscuous and monitoring mode at the same time and capture the traffic properly, which is a requirement not every WLAN adaptor &amp; driver for Windows can fulfil. So think twice before submitting the proposal.</p></div><div id="comment-57080-info" class="comment-info"><span class="comment-age">(07 Nov '16, 10:09)</span> sindy</div></div></div><div id="comment-tools-57069" class="comment-tools"></div><div class="clear"></div><div id="comment-57069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57076"></span>

<div id="answer-container-57076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>npcap is still considered experimental for usage with Wireshark, the regular WinPcap as installed by the Wireshark installer still works well on all Windows versions.</p><p>Whether either of those capture libraries will help solve your issue is another matter though. To see other wireless traffic from other devices to your router (really an AP) requires the wireless card in your PC to be put into "Monitor mode" and historically this has been difficult on Windows due to driver issues, although npcap "might" make this a bit better. You'll probably have more success running a version of Linux though, e.g Kali linux.</p><p>See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">Wireless Capture</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57076" class="comments-container"><span id="57112"></span><div id="comment-57112" class="comment"><div id="post-57112-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/CHECK.png" alt="alt text" /> I have attched the screen shot of device manager that shows i have network monitor driver installed. The issue is how to use it. <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a> i already consulted this link before posting here but couldn't get several thing... can i get steps how to: 1. properly install npcap 2. how to use monitor mode</p><p>because neither on youtube nor on discusssion forum i could get any satisfactory answer.</p></div><div id="comment-57112-info" class="comment-info"><span class="comment-age">(07 Nov '16, 17:50)</span> Abdullah</div></div><span id="57152"></span><div id="comment-57152" class="comment"><div id="post-57152-score" class="comment-score"></div><div class="comment-text"><p>can i expect some help?</p></div><div id="comment-57152-info" class="comment-info"><span class="comment-age">(08 Nov '16, 05:51)</span> Abdullah</div></div><span id="57154"></span><div id="comment-57154" class="comment"><div id="post-57154-score" class="comment-score"></div><div class="comment-text"><p>These seem to be npcap issues, so the best place for support for that is ... npcap. According to the npcap Github <a href="https://github.com/nmap/npcap">page</a> the place for such support is the mailing list [email protected]</p></div><div id="comment-57154-info" class="comment-info"><span class="comment-age">(08 Nov '16, 06:06)</span> grahamb ♦</div></div><span id="57155"></span><div id="comment-57155" class="comment"><div id="post-57155-score" class="comment-score"></div><div class="comment-text"><p>NPcap development is a one man (@Yang Luo) show, and it is very dynamic. So wireless monitoring mode was supported for a while, then not, and now it seems to be supported again. However, your success heavily depends on what your wireless card's driver can do. In the previous era where NPcap did support monitoring on wireless, you had to use an associated command line utility called WlanHelper to switch the wireless NIC from STA mode to monitoring mode so that you could monitor using NPcap, and I don't know about any advance here (i.e. still no communication channel between Wireshark and NPcap which would make the Wlan Helper obsolete).</p><p>In my case (Intel wireless chipset), I was never able to decrypt a WPA encrypted packet by Wireshark, with no clear reason ever identified. @Yang Luo says he blindly copies the 802.11 frames received from the driver, Wireshark doesn't claim any issue with the frame because the Intel's driver doesn't provide the FCS... so you have to try your luck, install Npcap with wireless monitoring support, switch your WLAN NIC to monitoring mode (which will deassociate it from the network, so you can either be connected or monitor, not both - this does not happen on Mac).</p></div><div id="comment-57155-info" class="comment-info"><span class="comment-age">(08 Nov '16, 06:29)</span> sindy</div></div></div><div id="comment-tools-57076" class="comment-tools"></div><div class="clear"></div><div id="comment-57076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57170"></span>

<div id="answer-container-57170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57170-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi @Abdullah, thanks for using Npcap.</p><blockquote><p>but after installing it when i run wire shark, on initializing it kept on asking for admin permission</p></blockquote><p>Do not install Npcap with "Restrict Npcap driver's access to Administrators only" option checked. This option will prompt UAC window every time Wireshark invokes Npcap DLLs.</p><blockquote><p>I have attched the screen shot of device manager that shows i have network monitor driver installed. The issue is how to use it. <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a> i already consulted this link before posting here but couldn't get several thing... can i get steps how to: 1. properly install npcap 2. how to use monitor mode</p></blockquote><p>If you mean "Network Monitor 3" from Microsoft, that's unnecessary. All you need is the latest Wireshark and Npcap. And about the monitor mode usage, it's very simple. Just use the Wireshark GUI, don't use WlanHelper.exe. In Wireshark GUI (QT version), go to "Capture options", click the checkbox in "Monitor Mode" column of your wireless adapter, then click "Start". You will be capturing raw 802.11 traffic in monitor mode now. Quitting the capture will turn the adapter back to managed mode automatically. If your "Monitor Mode" checkbox is unselectable, it somehow means that your adapter doesn't support monitor mode. To double-check it, you can run "WlanHelper.exe &lt;adapter_name&gt; modes" to get all supported operation modes by your adapter. If "monitor" doesn't show up, then your adapter doesn't support it for sure. The adapter name used in WlanHelper.exe commands is the same name in your "Network Connections" window.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '16, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '16, 08:31</p></div></div><div id="comments-container-57170" class="comments-container"></div><div id="comment-tools-57170" class="comment-tools"></div><div class="clear"></div><div id="comment-57170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

