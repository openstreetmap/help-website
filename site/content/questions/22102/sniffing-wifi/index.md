+++
type = "question"
title = "sniffing WIFI"
description = '''Hi everyone, My home network consists of several PC&#x27;s connected via Ethernet...as well as 2 laptops, 2 Ipads and 2 smartphones connected via WIFI (WPA2/TKIP). Ultimately I plan on using Security Onion to monitor all of my devices; however as a first step I tried to see if I could view all of the tra...'''
date = "2013-06-16T03:42:00Z"
lastmod = "2013-06-16T03:42:00Z"
weight = 22102
keywords = [ "sniffing", "wifi" ]
aliases = [ "/questions/22102" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [sniffing WIFI](/questions/22102/sniffing-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22102-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>My home network consists of several PC's connected via Ethernet...as well as 2 laptops, 2 Ipads and 2 smartphones connected via WIFI (WPA2/TKIP).</p><p>Ultimately I plan on using Security Onion to monitor all of my devices; however as a first step I tried to see if I could view all of the traffic via Wireshark, and I am only able to see the traffic from the laptop that I do the sniffing on. Obviously that laptop is connected to my WPA2 protected WLAN.</p><p>I have tried using Wireshark both in Windows 7 as well as in Linux (Backtrack) but the same thing happens. In Backtrack I am able to use airmon-ng and put the adapter into monitor mode, and can see the 802.11 control frames etc. But no matter what I seem to do, I am unable to get this to work. I have even checked and unchecked "promiscuous mode" in Wireshark.</p><p>My plan had been to use a DD-WRT router configured as a wireless repeater bridge to be the source for Security Onion. Even using the repeater bridge, which is already connected to my SSID, I am only able to see the traffic coming off the machine I use for sniffing. I do get a lot of ARP and other broadcast traffic to other IPs on my WLAN, but no TCP packets.</p><p>I know for a fact that I used to be able to sniff all traffic - I distinctly remember testing Driftnet out.</p><p>I was wondering if this has something to do with Windows 7; but it shouldnt make a difference in Backtrack Linux.<br />
</p><p>I have posted this question on DD-WRT's forum as well as Backtracks but have received no responses. I have also searched via Google but have come up with a bunch of conflicting answers.</p><p>BTW I have tried going into preferences and configuring the encryption key in the 802.11 settings. The problem is I am unable to set the channel via the wireless toolbar - both in Windows and Linux, when I display the wireless toolbar, almost everything on it is grayed out.</p><p>And once last thing - when I tried this last and was successful at sniffing all traffic I might have been using WEP. Would changing to WPA2 cause this??</p><p>Any help that you can give me would be greatly appreciated.</p><p>Mike</p></div><div id="question-tags" class="tags-container tags">sniffing wifi</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '13, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/e0252363d63ee2b6255f05fb919f69d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foolio&#39;s gravatar image" /><p>foolio<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foolio has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-22102" class="comments-container"><span id="22121"></span><div id="comment-22121" class="comment"><div id="post-22121-score" class="comment-score"></div><div class="comment-text"><p>Are you using an AirPcap radiotap?</p></div><div id="comment-22121-info" class="comment-info"><span class="comment-age">(17 Jun '13, 12:04)</span> John_Modlin</div></div><span id="22173"></span><div id="comment-22173" class="comment"><div id="post-22173-score" class="comment-score"></div><div class="comment-text"><p>I too would like to see the answers to your questions. However, you may want to go through your post and clarify what exactly your questions are in a 1. 2. 3. format so the experts here can cherry-pick what they want to answer and leave other questions/clarifications to others.</p></div><div id="comment-22173-info" class="comment-info"><span class="comment-age">(19 Jun '13, 08:48)</span> sandtiger333</div></div><span id="22174"></span><div id="comment-22174" class="comment"><div id="post-22174-score" class="comment-score"></div><div class="comment-text"><p>BTW, my admittedly novice sense is that your problem may be the wireless NIC or the NIC's driver you're attempting capture with. I know there are some NICs out there that are set up to do this (monitor mode, promiscuous mode, etc.) and some aren't.<br />
</p><p>You may want to detail the make/manufacturer/chipset of the NIC you're using and the drivers you're using for both Windows and Linux.<br />
</p><p>Also, I've run into n00b problems with packet capture due to misconfigured adapter settings when using virtual machines (e.g., running a BackTrack VM inside a Mac-host on VMWare Fusion). If you're using virtual machines you may also want to detail your settings there, too.</p></div><div id="comment-22174-info" class="comment-info"><span class="comment-age">(19 Jun '13, 08:54)</span> sandtiger333</div></div></div><div id="comment-tools-22102" class="comment-tools"></div><div class="clear"></div><div id="comment-22102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

