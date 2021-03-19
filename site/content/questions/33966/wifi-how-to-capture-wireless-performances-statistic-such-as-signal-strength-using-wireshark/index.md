+++
type = "question"
title = "Wifi - How to capture wireless performances statistic (such as signal strength) using Wireshark"
description = '''Hi, I wonder if there is a way to capture WiFi wireless performance statistics (such as signal strength) using Wireshark? I try to add the column &quot;RSSI&quot; in Wireshark but it is showing up as empty. Next, I use Netmon and I could add the column &quot;RSSI&quot; in Netmon. And values are showing up. My question ...'''
date = "2014-06-19T13:04:00Z"
lastmod = "2014-06-19T14:40:00Z"
weight = 33966
keywords = [ "setup", "signal", "wifi", "quality", "strength" ]
aliases = [ "/questions/33966" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wifi - How to capture wireless performances statistic (such as signal strength) using Wireshark](/questions/33966/wifi-how-to-capture-wireless-performances-statistic-such-as-signal-strength-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33966-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I wonder if there is a way to capture WiFi wireless performance statistics (such as signal strength) using Wireshark? I try to add the column "RSSI" in Wireshark but it is showing up as empty.</p><p>Next, I use Netmon and I could add the column "RSSI" in Netmon. And values are showing up. My question is why Netmon is able to do it but not Wireshark?</p><p>Also, is there a way to see signal quality, noise , interference, throughput of Wifi signals with Wireshark?</p><p>Any tools/software that you will suggest me buying in order to see such network statistics?</p></div><div id="question-tags" class="tags-container tags">setup signal wifi quality strength</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '14, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/287024c5a663404a19410f0e8a7df8e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kohck&#39;s gravatar image" /><p>kohck<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kohck has no accepted answers">0%</span></p></div></div><div id="comments-container-33966" class="comments-container"></div><div id="comment-tools-33966" class="comment-tools"></div><div class="clear"></div><div id="comment-33966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33968"></span>

<div id="answer-container-33968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33968-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question is why Netmon is able to do it but not Wireshark?</p></blockquote><p>Netmon is able to do it because its driver for packet capture supports NDIS 6, and thus supports putting adapters into monitor mode, so it can get the signal strength for packets it captures.</p><p>Wireshark is not able to do it on Windows because it uses WinPcap to capture packets on Windows, and WinPcap's driver <em>doesn't</em> support NDIS 6 and <em>can't</em> put adapters into monitor mode, so it <em>can't</em> get the signal strength for packets it captures on Windows.</p><blockquote><p>Also, is there a way to see signal quality, noise , interference, throughput of Wifi signals with Wireshark?</p></blockquote><p>Yes. Either:</p><ul><li>buy <a href="http://www.riverbed.com/products/performance-management-control/network-performance-management/wireless-packet-capture.html">an AirPcap adapter</a> and use that to capture on Windows;</li><li>install Linux on your machine (libpcap, which is what Wireshark uses for packet capture on UN*X, doesn't require a driver of its own, and the OS allows adapters to be put into monitor mode);</li><li>buy another machine running Linux or OS X and use that to capture the signal strength;</li><li>install Linux on a virtual machine (using a virtual machine program that lets you connect USB devices to a virtual machine) and plug a USB Wi-Fi adapter into your machine, connect it to Linux, and do your capturing with that adapter on Linux.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jun '14, 14:41</p></div></div><div id="comments-container-33968" class="comments-container"></div><div id="comment-tools-33968" class="comment-tools"></div><div class="clear"></div><div id="comment-33968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

