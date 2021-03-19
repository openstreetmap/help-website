+++
type = "question"
title = "Support for 802.11ac Wireless Adapter"
description = '''I use a Netgear A6210 USB adapter to do WiFi captures. Savvius OmniPeek has a driver to put it into promiscuous mode and it works well. It supports 802.11ac. Is there a way that Wireshark could be set up to support this adapter? Here&#x27;s a link to show the adapter on Amazon (which is where Savvius tel...'''
date = "2016-06-13T11:00:00Z"
lastmod = "2016-06-15T06:48:00Z"
weight = 53412
keywords = [ "wireless", "driver", "802.11ac" ]
aliases = [ "/questions/53412" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Support for 802.11ac Wireless Adapter](/questions/53412/support-for-80211ac-wireless-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53412-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use a Netgear A6210 USB adapter to do WiFi captures. Savvius OmniPeek has a driver to put it into promiscuous mode and it works well. It supports 802.11ac. Is there a way that Wireshark could be set up to support this adapter?</p><p>Here's a link to show the adapter on Amazon (which is where Savvius tells you to go to buy it). I'm at Sharkfest 2016 right now and will be for the rest of the week - I'm Ron Fox.</p><p><a href="https://www.amazon.com/Savvius-WiFI-Adapter-OmniPeek-802-11ac/dp/B0157LUUB0?ie=UTF8&amp;redirect=true">https://www.amazon.com/Savvius-WiFI-Adapter-OmniPeek-802-11ac/dp/B0157LUUB0?ie=UTF8&amp;redirect=true</a></p></div><div id="question-tags" class="tags-container tags">wireless driver 802.11ac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '16, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/c0c71d0fb9364ff5702351cbe2859232?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RonF&#39;s gravatar image" /><p>RonF<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RonF has no accepted answers">0%</span></p></div></div><div id="comments-container-53412" class="comments-container"><span id="53418"></span><div id="comment-53418" class="comment"><div id="post-53418-score" class="comment-score"></div><div class="comment-text"><p>Linux might work. Do you require windows?</p></div><div id="comment-53418-info" class="comment-info"><span class="comment-age">(13 Jun '16, 12:42)</span> Bob Jones</div></div><span id="53420"></span><div id="comment-53420" class="comment"><div id="post-53420-score" class="comment-score"></div><div class="comment-text"><p>Looks like I spoke too soon. I have several of these for use with OmniPeek and they enumerate on Linux as:</p><p>/home/admin# lsusb Bus 002 Device 005: ID 0846:9053 NetGear, Inc.</p><p>This link (<a href="https://wikidevi.com/wiki/Netgear_A6210)">https://wikidevi.com/wiki/Netgear_A6210)</a> says MediaTek has a driver, but there is none for my Kali Rolling install with kernel 4.4.0-kali1-amd64 built-in.</p><p>It's not worth the effort for me to go get some driver and compile, but you could try. On Windows, did you try npcap? That has never worked for me, but others have had success.</p></div><div id="comment-53420-info" class="comment-info"><span class="comment-age">(13 Jun '16, 13:55)</span> Bob Jones</div></div><span id="53468"></span><div id="comment-53468" class="comment"><div id="post-53468-score" class="comment-score"></div><div class="comment-text"><p>I'd prefer Windows. I'm working in a corporate environment where all the PC's have Windows on them. I could possibly get them to give me a dedicated laptop to use that I could convert over to Linux. I'm at Sharkfest and the development team have suggested I give npcap I try, which I plan to do as soon as I get back from this and have a chance to put it up on my secondary laptop.</p><p>If I WERE to put this up on Linux, what release/version of Linux should I use?</p></div><div id="comment-53468-info" class="comment-info"><span class="comment-age">(15 Jun '16, 09:15)</span> RonF</div></div><span id="53473"></span><div id="comment-53473" class="comment"><div id="post-53473-score" class="comment-score"></div><div class="comment-text"><p>Why not use the OmniPeek software? It works on Windows and Savvius (the company who develops AND SUPPORTS the OmniPeek software) provides the drivers for Windows.</p><p>As a user of OmniPeek, I prefer to use it rather than Wireshark to capture WiFi. However, I still use Wireshark for some post analysis.</p></div><div id="comment-53473-info" class="comment-info"><span class="comment-age">(15 Jun '16, 12:35)</span> Amato_C</div></div></div><div id="comment-tools-53412" class="comment-tools"></div><div class="clear"></div><div id="comment-53412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53421"></span>

<div id="answer-container-53421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53421-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Ron,</p><p>you can eventually give a try to <a href="https://github.com/nmap/npcap">Npcap</a> that is a fork of WinPcap using NDIS6.0 and that can capture WiFi packets depending on the drivers used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '16, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-53421" class="comments-container"></div><div id="comment-tools-53421" class="comment-tools"></div><div class="clear"></div><div id="comment-53421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53464"></span>

<div id="answer-container-53464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53464-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please use Npcap (together with Wireshark):</p><p><a href="https://github.com/nmap/npcap/releases">https://github.com/nmap/npcap/releases</a></p><p>Npcap has a feature called "Raw 802.11 Packet Capture": Npcap is able to see 802.11 packets instead of fake Ethernet packets on ordinary wireless adapters. You need to select the "Support raw 802.11 traffic (and monitor mode) for wireless adapters" option in the installation wizard to enable this feature.</p><ol><li><p>When your adapter is in Monitor Mode, Npcap will supply all 802.11 data + control + management packets with radiotap headers.</p></li><li><p>When your adapter is in Managed Mode, Npcap will only supply 802.11 data packets with radiotap headers.</p></li></ol><p>Moreover, Npcap provides the WlanHelper.exe tool to help you switch to Monitor Mode on Windows. See more details about this feature in section "For software that use Npcap raw 802.11 feature" in the docs. See more details about radiotap here: <a href="http://www.radiotap.org/">http://www.radiotap.org/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-53464" class="comments-container"><span id="53576"></span><div id="comment-53576" class="comment"><div id="post-53576-score" class="comment-score"></div><div class="comment-text"><p>I'm going to try this. I have a question; how do I install this with Wireshark? Do I simply install Wireshark, decline when it asks me if I want to install winpcap and then install this driver after I'm done? Or should I install this driver first?</p></div><div id="comment-53576-info" class="comment-info"><span class="comment-age">(20 Jun '16, 16:05)</span> RonF</div></div><span id="53577"></span><div id="comment-53577" class="comment"><div id="post-53577-score" class="comment-score"></div><div class="comment-text"><p>You can install Npcap driver first or later, the order doesn't matter. But when you install Wireshark first, you need to make sure you doesn't install WinPcap.</p></div><div id="comment-53577-info" class="comment-info"><span class="comment-age">(20 Jun '16, 17:00)</span> Yang Luo</div></div><span id="53617"></span><div id="comment-53617" class="comment"><div id="post-53617-score" class="comment-score"></div><div class="comment-text"><p>Hm. So I installed npcap 0.07 r17 and then installed Wireshark 2.0.4. I enabled "Raw 802.11 Packet Capture" but not the WinAPI compatibility mode. When I brought up Wireshark I told it to NOT install WinPcap. Upon actually starting the software it told me "Unable to load WinPcap (wpcap.dll); yuou will not be able to capture packets." I'm going to uninstall npcap and reinstall it using the WinAPI compatible mode to see if that works.</p></div><div id="comment-53617-info" class="comment-info"><span class="comment-age">(22 Jun '16, 13:06)</span> RonF</div></div><span id="53618"></span><div id="comment-53618" class="comment"><div id="post-53618-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 2.0.4 does not support Npcap installed without WinPcap compatibility mode. Only the very latest 2.1.1 development builds can.</p></div><div id="comment-53618-info" class="comment-info"><span class="comment-age">(22 Jun '16, 13:40)</span> Pascal Quantin</div></div><span id="53621"></span><div id="comment-53621" class="comment"><div id="post-53621-score" class="comment-score"></div><div class="comment-text"><p>Just as Pascal said, please download the latest 2.1.1 Wireshark here: <a href="https://www.wireshark.org/download/automated/win64/">https://www.wireshark.org/download/automated/win64/</a></p><p>Or you can add "C:\Windows\System32\Npcap" manually to your PATH, then re-login or reboot. Then you can use a stable version Wireshark too.</p></div><div id="comment-53621-info" class="comment-info"><span class="comment-age">(22 Jun '16, 17:31)</span> Yang Luo</div></div></div><div id="comment-tools-53464" class="comment-tools"></div><div class="clear"></div><div id="comment-53464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

