+++
type = "question"
title = "how can I capture traffic between two devices on Wi-Fi"
description = '''Hello I have difficult setup I will try to explain and then ask the question: (IP-192.168.0.100) -------------- (IP 192.168.0.1) ---------------- (IP 192.168.0.200) Mobile phone with Wifi --connected -- PC with Wifi USB stick -- connected -- Mobile phone with Wifi I am running WireShark on my pc and...'''
date = "2013-08-19T06:53:00Z"
lastmod = "2013-08-19T13:43:00Z"
weight = 23847
keywords = [ "capture", "wi-fi" ]
aliases = [ "/questions/23847" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how can I capture traffic between two devices on Wi-Fi](/questions/23847/how-can-i-capture-traffic-between-two-devices-on-wi-fi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23847-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have difficult setup I will try to explain and then ask the question:</p><p>(IP-192.168.0.100) -------------- (IP 192.168.0.1) ---------------- (IP 192.168.0.200)</p><p>Mobile phone with Wifi --connected -- PC with Wifi USB stick -- connected -- Mobile phone with Wifi</p><p>I am running WireShark on my pc and i am capturing traffic that cumming thru the USB port the problem is I cannot see unicast traffic between two mobile devices (between 192.168.0.100 and 192.168.0.200)</p><p>I think that my pc doing the routing on this WiFi connection so why i cannot see traffic between this two devices also I see traffic with destination of 192.168.0.1 is there any check box that I need to add or some routing that I need to capture it.</p><p>Please advise Thanks in advance Boris Shlichvsoki</p></div><div id="question-tags" class="tags-container tags">capture wi-fi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '13, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/173e0eeb7a600f3c0a8f7a879b163e31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boris&#39;s gravatar image" /><p>Boris<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boris has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '13, 13:36</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23847" class="comments-container"></div><div id="comment-tools-23847" class="comment-tools"></div><div class="clear"></div><div id="comment-23847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23852"></span>

<div id="answer-container-23852" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23852-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To capture, on a Wi-Fi network, unicast traffic not sent to or from the capturing machine, you will probably need to capture in monitor mode. <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">The Wireshark Wiki article on WLAN captures</a> gives a lot of detail on that; the way you capture in monitor mode is OS-dependent - newer versions of libpcap on non-Windows OSes, and current versions of Wireshark, attempt to let you do it by checking a checkbox, but, for various reasons, that doesn't necessarily work on Linux or *BSD, and it doesn't work at all on Windows (to capture in monitor mode on Windows, you'd need to capture with a tool such as <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> or use an <a href="http://www.riverbed.com/products-solutions/products/performance-management/wireshark-enhancement-products/Wireless-Traffic-Packet-Capture.html">AirPcap device</a> with Wireshark).</p><p>Note that, if the network you're on is "protected", using WEP or WPA/WPA2, you will need to be able to decrypt it; details on that are in <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki article on decrypting 802.11</a> - note that, for WPA/WPA2, you will need to capture the traffic that appears when the other hosts associate with the network, so you might have to turn the mobile phones off before starting your traffic capture and turn them back on again after the capture starts. Note also that capture filters work on <em>undecrypted</em> packets, so, if the traffic is encrypted, you can't use capture filters on anything at the IP layer (such as IP addresses) or above, you can only filter at the MAC layer (MAC addresses, frame types, and so forth). You can use <em>display</em> filters once the traffic is decrypted, however.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '13, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23852" class="comments-container"><span id="23863"></span><div id="comment-23863" class="comment"><div id="post-23863-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have installed app that called Microsoft Network Monitor as you advised and applied there monitor mode Now I see all the traffic between all devices it was very helpful</p><p><strong>Thanks for your help Guy</strong> :-)</p></div><div id="comment-23863-info" class="comment-info"><span class="comment-age">(20 Aug '13, 02:01)</span> Boris</div></div></div><div id="comment-tools-23852" class="comment-tools"></div><div class="clear"></div><div id="comment-23852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

