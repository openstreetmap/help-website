+++
type = "question"
title = "trying to monitor iPhone traffic"
description = '''I&#x27;m a total noobie to this. My ultimate goal is to look at what info is &quot;leaked&quot; by my iPhone &amp;amp; Mac laptop when connected to a public WiFi connection. Originally I installed WS on a hard wired computer assuming that the wireless data must ultimately end up on the wired network to hit the router ...'''
date = "2015-06-14T12:37:00Z"
lastmod = "2015-06-14T13:34:00Z"
weight = 43149
keywords = [ "iphone" ]
aliases = [ "/questions/43149" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [trying to monitor iPhone traffic](/questions/43149/trying-to-monitor-iphone-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43149-score" class="post-score" title="current number of votes">0</div><span id="post-43149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a total noobie to this. My ultimate goal is to look at what info is "leaked" by my iPhone &amp; Mac laptop when connected to a public WiFi connection. Originally I installed WS on a hard wired computer assuming that the wireless data must ultimately end up on the wired network to hit the router and then be routed to the internet. When I filter for the phone IP and then browse or check mail all I see is MDNS to 224.0.0.251.</p><p>I then installed WS on a laptop and monitored the wireless interface. Again all I see is MDNS to 224.0.0.251.</p><p>Can some one give me some insight on this and is it possible to see what is seeking out of my phone?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '15, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/14234352aa48e365f5261c1e3b582813?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackP&#39;s gravatar image" /><p><span>JackP</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackP has no accepted answers">0%</span></p></div></div><div id="comments-container-43149" class="comments-container"></div><div id="comment-tools-43149" class="comment-tools"></div><div class="clear"></div><div id="comment-43149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43150"></span>

<div id="answer-container-43150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43150-score" class="post-score" title="current number of votes">1</div><span id="post-43150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(I assume this was on your home network, not on a public network.)</p><blockquote><p>all I see is MDNS</p></blockquote><p>The "M" in "MDNS" is key here; it stands for "multicast", and means the traffic you're capturing is multicast traffic, sent out to all hosts in the multicast group, not unicast traffic, sent by one host to another.</p><blockquote><p>Originally I installed WS on a hard wired computer assuming that the wireless data must ultimately end up on the wired network to hit the router and then be routed to the internet.</p></blockquote><p>I'm guessing that you have some sort of Wi-Fi device that has multiple Ethernet ports, and that you plugged the hardwired computer into one of those Ethernet ports.</p><p>If so, what you have in that device is probably a combination of an Ethernet switch, a Wi-Fi adapter, and a bridge between Wi-Fi and Ethernet. If the device is a combined cable modem/DSL modem/etc. and Wi-Fi/Ethernet device, the router inside the box either receives traffic directly from the Wi-Fi device and an internal port on the Ethernet switch, or from an internal port on the Ethernet switch, and routes Internet traffic onto the cable/DSL/etc. port. If it connects to a cable modem/DSL modem/etc., the router probably works similarly, except that it routes Internet traffic onto an Ethernet port marked "WAN" or "Internet" or something such as that, sending it to the cable modem/DSL modem/etc..</p><p>In any case, this means you're probably dealing with a <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">switched Ethernet</a> - and on a switch that probably does <em>not</em> support "port mirroring" or whatever the vendor would call it. If you have a combined modem/Wi-Fi/Ethernet device, you won't be able to capture the Internet traffic (without some very specialized equipment to sniff on the cable modem/DSL/etc. port, and I'm not sure whether that's even available to you). If you have a separate Wi-Fi/Ethernet device and modem, you could tap the traffic between the device and the modem <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_an_Ethernet_hub">by using an Ethernet hub</a> (careful, not a "hub" that's really a switch!) or <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_machine-in-the-middle">by making the hardwired computer into a "machine in the middle"</a> or <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_network_tap">by using a network tap</a> or other tricks listed there.</p><p>You would, of course, also have to capture in promiscuous mode on the Ethernet adapter.</p><blockquote><p>I then installed WS on a laptop and monitored the wireless interface.</p></blockquote><p>You would have to capture in <em>monitor mode</em> on the laptop, if that's possible; see <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">the Wireshark Wiki article on WLAN capturing</a>. If your network is protected, i.e. if it's using WEP or WPA/WPA2, you will also have to <a href="https://wiki.wireshark.org/HowToDecrypt802.11">configure Wireshark so that it can decrypt the traffic</a> and, if it's WPA/WPA2, ensure that you capture the "initial handshake" for each of the devices whose traffic you want to decrypt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '15, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43150" class="comments-container"></div><div id="comment-tools-43150" class="comment-tools"></div><div class="clear"></div><div id="comment-43150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43152"></span>

<div id="answer-container-43152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43152-score" class="post-score" title="current number of votes">0</div><span id="post-43152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some good reading material before trying to capture again:</p><ol><li>If you want to capture on the wired network: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></li><li>If you want to capture on the wireless network: <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '15, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43152" class="comments-container"></div><div id="comment-tools-43152" class="comment-tools"></div><div class="clear"></div><div id="comment-43152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

