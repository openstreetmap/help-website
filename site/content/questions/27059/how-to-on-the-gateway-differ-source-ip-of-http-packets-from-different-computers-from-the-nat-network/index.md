+++
type = "question"
title = "How to on the gateway differ source IP of HTTP packets from different computers from the nat network?"
description = '''Hi to all! I have next situation. My home computer has 100 Mbit cabel internet connection. Cabel from internet provider connected to network card in my PC. I have real IP address (for example 150.140.130.120) Also I have simple USB wifi modem witch can work as access point. I use Connectify Hotspot ...'''
date = "2013-11-17T11:51:00Z"
lastmod = "2013-11-17T17:16:00Z"
weight = 27059
keywords = [ "url", "connectify", "http", "gateway", "get" ]
aliases = [ "/questions/27059" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to on the gateway differ source IP of HTTP packets from different computers from the nat network?](/questions/27059/how-to-on-the-gateway-differ-source-ip-of-http-packets-from-different-computers-from-the-nat-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27059-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi to all!</p><p>I have next situation. My home computer has 100 Mbit cabel internet connection. Cabel from internet provider connected to network card in my PC. I have real IP address (for example 150.140.130.120) Also I have simple USB wifi modem witch can work as access point. I use Connectify Hotspot software to share my internet connection via wifi to other people and for my mobile devices also. All users who connected to my wifi have IP address 192.168.77.xxx)</p><p>My task: I want to see what web-sites users of my wifi point visits. I start Wireshark to capture packets from both interfaces (1st - is my real network card with internet cabel from my provider; 2nd - my wireless connection (it is created automatically by Connectify hotspot)). On both interfaces packets count permanently increases, little bit faster on real network connection, that is right. In the list of captured packets in Wireshark I see all HTTP GET\POST queries and Full request URI. I use this filter: http.request and http.request.method != M-SEARCH But I have one big problem... In all packets Source address is identical. And it equal IP address of my PC (150.140.130.120). I can<code>t see source IP address from wifi users (their IP address should be from 192.168.77.xxx subnetwork). Also I can</code>t see source IP address of packets from my mobile device. I can see all HTTP queries from my mobile device, but source of all packets is 150.140.130.120, but should be 192.168.77.59). If I try to use other filter like this (ip.addr == 192.168.77.59), I can<code>t see packets with HTTP GET\POST queries and Full request URI. I see only TCP, UDP, DNS packets and some HTTP packets but without GET\POST\URI headers. if I do not use any filters then same situation (i see packets but with real IP address of my PC 150.140.130.120), and many more other low-level packets. Maybe on gateway PC I need to some configure Wireshark to see correct IP addresses. Or maybe i need to use some solutions for NAT networks. I don</code>t know...</p><p>Please, help me to solve this problem. Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">url connectify http gateway get</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '13, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/12a192789095084a2fcddd120adef5fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SergeyV&#39;s gravatar image" /><p>SergeyV<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SergeyV has no accepted answers">0%</span></p></div></div><div id="comments-container-27059" class="comments-container"></div><div id="comment-tools-27059" class="comment-tools"></div><div class="clear"></div><div id="comment-27059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27060"></span>

<div id="answer-container-27060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27060-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Also <strong>I have simple USB wifi modem</strong> witch can work as access point. <strong>I use Connectify Hotspot software</strong> to share my internet connection via wifi<br />
start Wireshark to <strong>capture packets from both interfaces</strong> (2nd - <strong>my wireless connection (it is created automatically by Connectify hotspot))</strong>. On <strong>both interfaces packets count permanently increases,</strong></p></blockquote><p>O.K. apparently Connectify creates a 'virtual' interface that Wireshark is able to capture traffic, otherwise you would not see the counter increase on <strong>both</strong> interfaces. <strong>However</strong> as you don't see the internal addresses (192.168.77./24) I assume that WinPcap (the capture library of Wireshark) get only the already translated (NATed) packets from the 'virtual' interface. If that's the case, there is nothing you can do in Wireshark (configuration) to make it work, as it's apparently a limitation of Connectify.</p><p>To be absolutely sure, I suggest to capture only on the 'virtual' wifi interface and then check if you see any addresses from the network 192.168.77.0/24.</p><p>BTW: A similar problem with Connectify has been reported earlier.</p><blockquote><p><a href="http://ask.wireshark.org/questions/9375/unable-to-capture-soap-response">http://ask.wireshark.org/questions/9375/unable-to-capture-soap-response</a></p></blockquote><p>Only solution in your environment: Get another PC/Laptop and capture the wifi/wlan traffic instead of the interfaces on the PC with Connectify.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '13, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '13, 17:17</p></div></div><div id="comments-container-27060" class="comments-container"></div><div id="comment-tools-27060" class="comment-tools"></div><div class="clear"></div><div id="comment-27060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

