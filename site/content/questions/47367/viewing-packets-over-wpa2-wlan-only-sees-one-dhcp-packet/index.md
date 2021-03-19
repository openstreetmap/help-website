+++
type = "question"
title = "Viewing packets over WPA2 wlan:  Only sees one DHCP packet?"
description = '''I am using Wireshark to analyse traffic on my home network, in particular examining packets sent between my Android phone and the AP of a WPA2 wireless network. To do this I have set my adapter into monitor mode, and entered the WLAN password and SSID under the 802.11 settings. Unfortunately, the on...'''
date = "2015-11-08T02:31:00Z"
lastmod = "2015-11-09T06:09:00Z"
weight = 47367
keywords = [ "decryption", "802.11" ]
aliases = [ "/questions/47367" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Viewing packets over WPA2 wlan: Only sees one DHCP packet?](/questions/47367/viewing-packets-over-wpa2-wlan-only-sees-one-dhcp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47367-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark to analyse traffic on my home network, in particular examining packets sent between my Android phone and the AP of a WPA2 wireless network. To do this I have set my adapter into monitor mode, and entered the WLAN password and SSID under the 802.11 settings.</p><p>Unfortunately, the only decrypted packet I seem to get from the analysis is a single DHCP ACK packet sent from the AP to the device. I've used the filter "eapol || ip" just so I can see that the EAPOL packets are received so that Wireshark can decrypt communication between the device and the AP, and see any IP datagrams sent between the two. I get the four EAPOL packets, and then straight after that the DHCP packet. But I never get anything else. I generate traffic by browsing websites, etc on my phone, but nothing comes up.</p><p>I have my suspicions that the network card or driver or something may be buggy, for the following reasons:</p><ol><li><p>When I put the card in monitor mode, the capture often stops after a random amount of time, spitting out the following message: "Unknown message from dumpcap, try to show it as a string: Can't restore interface wlan0 wireless mode (SIOCSIWMODE failed: Operation not permitted). Please adjust manually."</p></li><li><p>I've tested this using an open Wifi network and have had more success with unencrypted packets, but even then packets seem to be dropped. For example, I will see HTTP requests but not replies for certain machines, even after fiddling with TCP and HTTP options about reassembling packets.</p></li></ol><p>I'm running version 1.10.6 of Wireshark on Ubuntu 14.04, using an Atheros wireless chipset (ath9k driver for the Atheros AR9565)</p><p>Can anyone shed some light on this issue?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">decryption 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/992efab4a9405133dc0b9dde1d5e6b2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="borophyll&#39;s gravatar image" /><p>borophyll<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="borophyll has no accepted answers">0%</span></p></div></div><div id="comments-container-47367" class="comments-container"></div><div id="comment-tools-47367" class="comment-tools"></div><div class="clear"></div><div id="comment-47367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47431"></span>

<div id="answer-container-47431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47431-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Update to the latest kernel: <a href="https://www.kernel.org/">https://www.kernel.org/</a></li><li>Update to the latest ath9k drivers: <a href="https://wireless.wiki.kernel.org/en/users/drivers/ath9k">https://wireless.wiki.kernel.org/en/users/drivers/ath9k</a></li><li>Update to the latest Wireshark stable release: <a href="https://www.wireshark.org/download.html">https://www.wireshark.org/download.html</a></li></ol><p>I had a similar problem with my ath10k drivers. After performing all the upgrades as stated above, I had no issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-47431" class="comments-container"><span id="47448"></span><div id="comment-47448" class="comment"><div id="post-47448-score" class="comment-score"></div><div class="comment-text"><p>Thanks Amato, I will try this and let you know...</p></div><div id="comment-47448-info" class="comment-info"><span class="comment-age">(09 Nov '15, 22:07)</span> borophyll</div></div></div><div id="comment-tools-47431" class="comment-tools"></div><div class="clear"></div><div id="comment-47431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

