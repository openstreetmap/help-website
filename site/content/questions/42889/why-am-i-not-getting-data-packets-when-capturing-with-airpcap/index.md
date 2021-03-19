+++
type = "question"
title = "Why am I not getting data packets when capturing with AirPcap?"
description = '''I’m trying to use AirPCap (Classic) with WireShark Version 1.12.5 (v1.12.5-0-g5819e5b from master-1.12) 64 bit on Win7 64 bit with WinPCap 4.1.3 to capture packets on a 2.4GHz Wireless-G network (Channel 6) encrypted with a known WPA-PSK key. The problem is that I’m seeing hardly any data packets (j...'''
date = "2015-06-04T10:43:00Z"
lastmod = "2015-06-04T10:43:00Z"
weight = 42889
keywords = [ "airpcap", "wifi" ]
aliases = [ "/questions/42889" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I not getting data packets when capturing with AirPcap?](/questions/42889/why-am-i-not-getting-data-packets-when-capturing-with-airpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42889-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’m trying to use AirPCap (Classic) with WireShark Version 1.12.5 (v1.12.5-0-g5819e5b from master-1.12) 64 bit on Win7 64 bit with WinPCap 4.1.3 to capture packets on a 2.4GHz Wireless-G network (Channel 6) encrypted with a known WPA-PSK key.</p><p>The problem is that I’m seeing hardly any data packets (just control and management packets) even though the two devices I’m interested in are clearly exchanging lots of data. Neither device is the capture PC (a recent vintage HP laptop running on AC power.)</p><p>I’m using for following settings although I’ve tried others with no luck</p><ul><li>promiscuous mode: on Packet size</li><li>filter: off buffer size: 2 megabytes</li><li>Channel 2437 [BG 6] offset 0 Capture</li><li>type: 802.11 + Radio Include 803.11</li><li>FCS in Frames: on FCS Filter: All</li><li>frames Decryption type: Wireshark</li><li>Decryption keys:</li><li>-- Type: WPA-PWD</li><li>-- Key: as appropriate for the network</li><li>-- SSID: as appropriate for the network</li></ul><p>The capture was started with a Nexus 9 tablet with Wifi disabled and then it was enabled to ensure that the capture includes the EAPOL packets. Display filter: “eapol” clearly include the four EAPOL packets exchanged between device Htc_07:bc:f9 (The Nexus 9 tablet) and Netgear_bd_e8:6a (The Netgear router acting as the AP) However, filtering with “ip” shows only 3 bogus (corrupted) packets. Using filter “wlan.addr == b4:ce:f6:07:bc:f9” (the MAC address of the Nexus 9) show a bunch of IEEE 802.11 control packets and a few encrypted IP Multicast packets but they are not decrypted using the WPA key.</p><p>Using a capture filter such as “wlan host b4:ce:f6:07:bc:f9” does not help either.</p><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">airpcap wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '15, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/2228cd6967bbbd0a5acf545925263e07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gengen&#39;s gravatar image" /><p>Gengen<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gengen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 04 Jun '15, 11:05</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42889" class="comments-container"><span id="42891"></span><div id="comment-42891" class="comment"><div id="post-42891-score" class="comment-score"></div><div class="comment-text"><p>Does the capture filter "type data" work?</p></div><div id="comment-42891-info" class="comment-info"><span class="comment-age">(04 Jun '15, 11:06)</span> Guy Harris ♦♦</div></div><span id="42892"></span><div id="comment-42892" class="comment"><div id="post-42892-score" class="comment-score"></div><div class="comment-text"><p>Can you put a sample capture on a network drive so I can look at the capture (such as Google Drive or Cloudshark)?</p></div><div id="comment-42892-info" class="comment-info"><span class="comment-age">(04 Jun '15, 12:14)</span> Amato_C</div></div></div><div id="comment-tools-42889" class="comment-tools"></div><div class="clear"></div><div id="comment-42889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

