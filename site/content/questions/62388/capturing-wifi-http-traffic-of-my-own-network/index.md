+++
type = "question"
title = "Capturing wifi http traffic of my own network"
description = '''I am trying to debug an app on my smart tv and I need to capture the http requests it does. since the tv is in another room, im first testing with a tablet. So first, I connect a wifi adapter (AWUS036H). Set it to monitor mode with airmon-ng start wlan0 8 (8 is my router channel). Then I start wires...'''
date = "2017-06-28T23:21:00Z"
lastmod = "2017-06-29T02:45:00Z"
weight = 62388
keywords = [ "protocol", "wifi", "http", "router" ]
aliases = [ "/questions/62388" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing wifi http traffic of my own network](/questions/62388/capturing-wifi-http-traffic-of-my-own-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62388-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to debug an app on my smart tv and I need to capture the http requests it does. since the tv is in another room, im first testing with a tablet.</p><p>So first, I connect a wifi adapter (AWUS036H). Set it to monitor mode with <code>airmon-ng start wlan0 8</code> (8 is my router channel).</p><p>Then I start wireshark, and start capturing on the interface wlan0mon. When I visit example.com on my tablet, this is what appears on wireshark:</p><p><img src="http://i.imgur.com/K9Me1en.png" alt="alt text" /></p><p>f0:4f:7c:xx:xx is my tablet mac address, if I remove that filter I still don't see any http traffic, all white stuff and nothing of the green stuff I see when capturing eth0.</p><p><strong>So how do I capture the http traffic that goes thru my wifi router?</strong></p><p>The wifi network is temporarily open btw, I removed all the security for the test.</p><p><strong>UPDATE:</strong></p><p>I tried reenabling the router security (WPA2-PSK), reconnected the tablet while wireshark was running (to capture the handshake), and visited example.com again. Added wpa-pwd:mypwd:ssid to the IEEE 802.11 protocol and when I click "apply", some packets that were previously identified as LLC protocol change to 802.11 protocol, so decryption seems to be working, but I still can't find any package containing http information.</p></div><div id="question-tags" class="tags-container tags">protocol wifi http router</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '17, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/224f891a450a1759c1d40529aa2810b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wokcz&#39;s gravatar image" /><p>wokcz<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wokcz has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jun '17, 23:52</p></div></div><div id="comments-container-62388" class="comments-container"></div><div id="comment-tools-62388" class="comment-tools"></div><div class="clear"></div><div id="comment-62388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62392"></span>

<div id="answer-container-62392" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62392-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've never seen a block ACK with a layer 3 IP address included - they all have Receiver Address and Transmitter Address (RA/TA), which are MAC addresses. I guess you have Wireshark configured to do some mapping from L2-&gt;L3?</p><p>This looks like one of two problems:</p><ol><li>You are too far away from the devices under test so you can only see the low data rate frames. Lower data rate frames travel further, so you will pick this up at a greater distance. Data frames (since we see block ACK, I presume QoS-Data frames but applies to regular Data frames as well) will typically be sent at higher data rates so won't travel as far as management and control frames.</li><li>The capture device does not have the same capabilities to pick up the modulation of the actual data frames you are looking for. For instance, your capture adapter is in monitor mode and can only do 802.11abg (just for an example). But the AP and the client you want to capture from can do 802.11 abgn/ac, 2SS, SGI, LDPC. You have no chance of picking up frames sent at the upper end of these capabilities with that adapter. Note from (1) that not all frames are sent at maximum data rates, so you will see SOME traffic, like mgmt/control frames, but you will miss most of the data.</li></ol><p>Since you didn't provide a trace I can't look at signal strengths to determine if the issue might a distance problem, and I can't deduce the running network parameters because I can't see the beacons/probes/assoc frames for your network to determine the actual capabilities to compare to your capture adapter (which google says is 802.11bg).</p><p>Block ACKs usually come along with 802.11n or HT capability, so most likely your issue is (2). The data frames are sent at 802.11n rates, and the capture adapter can't pick them up.</p><p>What to do?</p><p>This comes up often here -</p><ol><li>Buy a better capture adapter with at least same or better modulation capabilities than the network under review</li><li>Reduce the settings on the AP so that only 802.11bg is supported - no 802.11n / HT / WMM, etc. This will reduce your performance, but you might be able to pick up the traffic.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '17, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-62392" class="comments-container"><span id="62423"></span><div id="comment-62423" class="comment"><div id="post-62423-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. You were correct, the adapter only supports 802.11b/g and the router was set to use 802.11b/g/n. I've set b/g mode on the router and now I can see all the packets, including the http ones I needed. Thank you very much.</p></div><div id="comment-62423-info" class="comment-info"><span class="comment-age">(29 Jun '17, 12:51)</span> wokcz</div></div></div><div id="comment-tools-62392" class="comment-tools"></div><div class="clear"></div><div id="comment-62392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

