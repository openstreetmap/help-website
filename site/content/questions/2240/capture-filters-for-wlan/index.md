+++
type = "question"
title = "Capture filters for WLAN"
description = '''Hi there, When capturing wireless 802.11 packets in Wireshark, is there a way to apply capture filters such as filtering specific SSID&#x27;s? The NIC is operating in monitor mode so it is capturing broadcast packets from other SSIDs that i do not want. Any help would be much appreciated. Thank you. Wire...'''
date = "2011-02-08T14:02:00Z"
lastmod = "2011-02-16T08:43:00Z"
weight = 2240
keywords = [ "capture-filter-wlan" ]
aliases = [ "/questions/2240" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filters for WLAN](/questions/2240/capture-filters-for-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>When capturing wireless 802.11 packets in Wireshark, is there a way to apply capture filters such as filtering specific SSID's? The NIC is operating in monitor mode so it is capturing broadcast packets from other SSIDs that i do not want.</p><p>Any help would be much appreciated.</p><p>Thank you.</p><p>Wireshark version 1.2.11 Ubuntu 10.10</p></div><div id="question-tags" class="tags-container tags">capture-filter-wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/0f5157cfbd821bf76c0752a20d274138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taj&#39;s gravatar image" /><p>taj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taj has no accepted answers">0%</span></p></div></div><div id="comments-container-2240" class="comments-container"></div><div id="comment-tools-2240" class="comment-tools"></div><div class="clear"></div><div id="comment-2240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2266"></span>

<div id="answer-container-2266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2266-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although not really regarding capture filters in wireshark, maybe this helps:</p><p>For generating the tracefiles I would recommend using airodumg-ng from the aircrack suite, especially when already running a linux OS.</p><p>Sample command for filtering specific SSID would be:</p><pre><code>airodumg-ng -c &lt;channelnumber or numbers&gt; --bssid &lt;MAC address of WLAN access point&gt; -w &lt;tracefilename to write to&gt; &lt;interface name of your wireless nic&gt;</code></pre><p>e.g. airodumg-ng -c 6 --bssid 00:13:29:11:22:33 -w /usr/sniffer/wireless-trace.pcap</p><p>Another advantage is, that airodump only captures one beacon frame per AP, thereby keeping trace fil size and readability much better</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '11, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-2266" class="comments-container"></div><div id="comment-tools-2266" class="comment-tools"></div><div class="clear"></div><div id="comment-2266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2281"></span>

<div id="answer-container-2281" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2281-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks Landi for your reply.</p><p>One issue that i am getting is that when i run the above script; i am not getting the transmitted traffic. The test was performed on two machines connected via a ad-hoc connection and they were constantly pinging each other during the airmon-ng capture. However, when i run the tracefile in Wireshark, it does not show the ICMP (ping) packets, it shows the IEEE traffic which is what i want but i also need to see those ICMP packets too. Any ideas??</p><p>Really appreciate all your help.</p><p>Taj</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '11, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/0f5157cfbd821bf76c0752a20d274138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taj&#39;s gravatar image" /><p>taj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taj has no accepted answers">0%</span></p></div></div><div id="comments-container-2281" class="comments-container"><span id="2344"></span><div id="comment-2344" class="comment"><div id="post-2344-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the late answer - been busy...</p><p>Do you only see IEEE 802.11 frames ? Because afaik ad-hoc enables WEP encryption thus you see encrypted traffic inside wireshark. Those ICMP packets would then be displayed as 802.11 Data frames.</p><p>If that's the case, you would have to enter the encryption key under the protocol preferences of 802.11 and by this enable wireshark to decrypt and display whats inside those frames</p></div><div id="comment-2344-info" class="comment-info"><span class="comment-age">(15 Feb '11, 04:32)</span> Landi</div></div><span id="2349"></span><div id="comment-2349" class="comment"><div id="post-2349-score" class="comment-score"></div><div class="comment-text"><p>Yes, im only seeing the IEEE 802.11 frames but i made sure that there was no security enabled on the adhoc network as i already that i wouldn't see the encrypted content. Any ideas?</p><p>Thanks again for your help.</p><p>Taj</p></div><div id="comment-2349-info" class="comment-info"><span class="comment-age">(15 Feb '11, 09:22)</span> taj</div></div><span id="2383"></span><div id="comment-2383" class="comment"><div id="post-2383-score" class="comment-score"></div><div class="comment-text"><p>urks... good question - did you completely disable security by setting No encryption and OPEN authentication ? My next guess would be setup was no encryption but shared authentication, which actually is a very weak way of "encrypting" wireless frames...</p><p>I just tried to setup ad-hoc to make a test trace, but my smartphone won't do ad-hoc, so next time I got thee stations, I will rerun the setup and take a look at my traces if I see the same problem.</p><p>Pls keep me updated on your case</p></div><div id="comment-2383-info" class="comment-info"><span class="comment-age">(16 Feb '11, 10:48)</span> Landi</div></div></div><div id="comment-tools-2281" class="comment-tools"></div><div class="clear"></div><div id="comment-2281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2373"></span>

<div id="answer-container-2373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2373-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>filter: wlan.bssid eq mac_address_of_access_point</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/86f2c7b0b9d516107c98f74559d08c10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vivekjo&#39;s gravatar image" /><p>vivekjo<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vivekjo has no accepted answers">0%</span></p></div></div><div id="comments-container-2373" class="comments-container"><span id="2380"></span><div id="comment-2380" class="comment"><div id="post-2380-score" class="comment-score"></div><div class="comment-text"><p>Yup that's the <em>display</em> filter - taj was looking for a capture filter</p></div><div id="comment-2380-info" class="comment-info"><span class="comment-age">(16 Feb '11, 10:24)</span> Landi</div></div></div><div id="comment-tools-2373" class="comment-tools"></div><div class="clear"></div><div id="comment-2373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

