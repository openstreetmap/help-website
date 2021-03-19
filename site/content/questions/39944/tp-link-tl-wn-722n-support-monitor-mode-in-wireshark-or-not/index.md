+++
type = "question"
title = "tp-link tl- wn 722n support monitor mode in wireshark or not?"
description = '''Hello,  I am using atheros 9271 chipset,when I am using wireshark,wlan0 link layer header type available only ethernet and docsis,802.11 plus radiotap header not available,and I cant select monitor mode,it is grey color.but when I use this command &#x27;airmon-ng start wlan0&#x27; monitor mode enabled,after t...'''
date = "2015-02-19T04:48:00Z"
lastmod = "2015-02-20T15:37:00Z"
weight = 39944
keywords = [ "wireshark" ]
aliases = [ "/questions/39944" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tp-link tl- wn 722n support monitor mode in wireshark or not?](/questions/39944/tp-link-tl-wn-722n-support-monitor-mode-in-wireshark-or-not)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39944-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using atheros 9271 chipset,when I am using wireshark,wlan0 link layer header type available only ethernet and docsis,802.11 plus radiotap header not available,and I cant select monitor mode,it is grey color.but when I use this command 'airmon-ng start wlan0' monitor mode enabled,after this in wireshark interface list mon0 available,in the mon0 interface's link layer header type's available 802.11 plus radiotap header but not selectable,what is the reason for all?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '15, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/862faa5d26b66d1e5ade6679e966563c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hackerguru1989&#39;s gravatar image" /><p>hackerguru1989<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hackerguru1989 has no accepted answers">0%</span></p></div></div><div id="comments-container-39944" class="comments-container"><span id="39966"></span><div id="comment-39966" class="comment"><div id="post-39966-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "not selectable" in "in the mon0 interface's link layer header type's available 802.11 plus radiotap header but not selectable"? Do you mean that you can't select the mon0 interface and capture on it or do you mean that you can't select a link-layer header type? If it's that you can't select a link-layer header type, that's because it <em>only</em> supports 802.11+radiotap (which is the case with most Wi-Fi adapters on Linux when capturing in monitor mode).</p></div><div id="comment-39966-info" class="comment-info"><span class="comment-age">(19 Feb '15, 19:44)</span> Guy Harris ♦♦</div></div><span id="39994"></span><div id="comment-39994" class="comment"><div id="post-39994-score" class="comment-score"></div><div class="comment-text"><p>Sir I can select Mon 0 interface,but I can't select mon0's link layer header type.my wlan0 interface's link layer header type contains only ethernet and docsis only,802.11 plus radiotap not available.any problem with my wireless adapter(atheros ar-9271 chipset)?</p></div><div id="comment-39994-info" class="comment-info"><span class="comment-age">(20 Feb '15, 15:20)</span> hackerguru1989</div></div></div><div id="comment-tools-39944" class="comment-tools"></div><div class="clear"></div><div id="comment-39944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39995"></span>

<div id="answer-container-39995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39995-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On most OSes, you don't get to select the link-layer header type for 802.11 interfaces independently of monitor mode (and even the *BSD exceptions may not still be exceptions to that rule).</p><p>If you're not in monitor mode, you either get a choice of Ethernet and DOCSIS or only a choice of Ethernet. (The choice of DOCSIS is there to allow sniffing DOCSIS traffic that some types of Cisco cable modem equipment at the cable company will put on an Ethernet, using Ethernet physical-layer framing but <em>not</em> Ethernet MAC-layer headers; this doesn't apply to Wi-Fi, and libpcap will, if it can determine whether an interface offering the Ethernet link-layer type is a real Ethernet interface or not, offer DOCSIS only for Ethernet. It appears from what you're saying that libpcap needs to try harder to determine that on Linux.)</p><p>If you are in monitor mode, on <em>some</em> operating systems, you might get a choice of 802.11 without radio information ("802.11") and 802.11 with radio information in some format or formats ("802.11 plus radiotap", "802.11 plus AVS", etc.) For most interface, Linux only offers 802.11 plus radiotap.</p><p>So, there <em>is</em> no problem, other than than some annoying libpcap issues that prevent you from selecting monitor mode from within Wireshark (by using the checkbox) rather than having to use airmon-ng. (Changing libpcap to avoid using libnl, which should get rid of those issues, is on my to-do list, but it'd take some work.)</p><p>If you don't want to capture in monitor mode, capture on wlan0, and live with only getting Ethernet headers (which means only getting data frames, not getting some 802.11 details, and not getting radio information). That's a limitation of Linux, not of Wireshark or of your adapter and its driver.</p><p>If you do want to capture in monitor mode, capture on mon0, and live with only getting 802.11 headers + radiotap radio metadata headers (which means you can get frames other than data frames, will get 802.11 details, and will get radio information - but, if you're capturing on a "protected" network, using WEP or WPA/WPA2, you'll have to give Wireshark the network password to get it to decrypt the traffic so you can see details <em>beyond</em> the 802.11 header, and will have to capture the initial EAPOL handshake for all hosts whose traffic you want to decrypt; this also means that you can't use capture filters, as they don't work on encrypted data). That's a limitation of Linux, not of Wireshark or of your adapter and its driver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '15, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-39995" class="comments-container"><span id="40018"></span><div id="comment-40018" class="comment"><div id="post-40018-score" class="comment-score"></div><div class="comment-text"><p>hello sir, which wireless usb adapter support monitor mode and promiscuous mode,and also i need interface link layer:802.11 plus radiotap header.i am using tp-link tl-wn722n.so tell me which wireless adapter i have to buy?</p></div><div id="comment-40018-info" class="comment-info"><span class="comment-age">(23 Feb '15, 03:15)</span> hackerguru1989</div></div><span id="40033"></span><div id="comment-40033" class="comment"><div id="post-40033-score" class="comment-score"></div><div class="comment-text"><p>If airmon-ng was able to create a mon0 interface for your adapter, it supports monitor mode.</p><p>If you have a mon0 interface, try capturing on that; if you don't have a mon0 interface, run airmon-ng to create the mon0 interface, and then try capturing on that.</p></div><div id="comment-40033-info" class="comment-info"><span class="comment-age">(23 Feb '15, 10:50)</span> Guy Harris ♦♦</div></div><span id="40094"></span><div id="comment-40094" class="comment"><div id="post-40094-score" class="comment-score"></div><div class="comment-text"><p>sir i am able to enable monitor mode at airmon-ng,but i can not enable monitor mode in wireshark.</p></div><div id="comment-40094-info" class="comment-info"><span class="comment-age">(26 Feb '15, 03:59)</span> hackerguru1989</div></div><span id="40096"></span><div id="comment-40096" class="comment"><div id="post-40096-score" class="comment-score"></div><div class="comment-text"><p>you don't have to enable monitor mode in Wireshark, just capture on mon0 after you have created it with airmon-ng!</p></div><div id="comment-40096-info" class="comment-info"><span class="comment-age">(26 Feb '15, 04:46)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-39995" class="comment-tools"></div><div class="clear"></div><div id="comment-39995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

