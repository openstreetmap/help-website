+++
type = "question"
title = "How to capture Wi-Fi traffic from another machine"
description = '''My network topology is as below: Internet ------ Wireless Router --(Via WIRED LAN)-- PC (with Wireshark)  |  |--(Via Wifi WPA2-PSK)-- Android Phone  I can capture http traffic on my PC (wired directly with Wireless router), but not for my Android Phone. By filtering with the MAC address of my Androi...'''
date = "2012-11-25T05:10:00Z"
lastmod = "2014-01-29T09:19:00Z"
weight = 16273
keywords = [ "wifi", "http" ]
aliases = [ "/questions/16273" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture Wi-Fi traffic from another machine](/questions/16273/how-to-capture-wi-fi-traffic-from-another-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My network topology is as below:</p><pre><code>Internet ------ Wireless Router --(Via WIRED LAN)-- PC (with Wireshark)
                          |
                          |--(Via Wifi WPA2-PSK)-- Android Phone</code></pre><p>I can capture http traffic on my PC (wired directly with Wireless router), but not for my Android Phone. By filtering with the MAC address of my Android as source, only DHCP,ICMPv6,ARP are captured. How can I setup Wireshark to capture http traffic on my Android? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">wifi http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '12, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/1090c41c3979ae845f8f0d6ac868eedd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blue&#39;s gravatar image" /><p>blue<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blue has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '12, 11:28</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16273" class="comments-container"></div><div id="comment-tools-16273" class="comment-tools"></div><div class="clear"></div><div id="comment-16273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16277"></span>

<div id="answer-container-16277" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16277-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I setup Wireshark to capture http traffic on my Andriod? Thanks in advance.</p></blockquote><p>You can't, as your router will not send the traffic from your android phone to your PC. What you have seen (ARP, DHCP, etc.) is just broadcast traffic, which will be broadcasted to the network.</p><p><strong>UPDATE</strong>:</p><p>If you want to capture the traffic of your android phone you have these options:</p><ul><li><p>capture the wifi/wlan traffic on your PC. However, that requires a WLAN NIC in your PC and most certainly you must run the PC with linux to be able to operate the WLAN NIC in monitor mode. Monitor mode on Windows depends on the NIC driver and is only supported with a few WLAN NICs on Windows 7 (NDIS6 compatible driver).</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/WLAN</code><br />
</p></blockquote></li><li>Figure out if your router is able to mirror traffic from the WLAN interface to the LAN interface. Search the docs for something like "port mirror" or "port mirroring". If that option is available, mirror the whole WLAN traffic to the LAN interface, where your PC is connected to. Then run Wireshark on the PC.</li><li>Place a switch with port mirroring capabilities between your router and the "Internet" (presumably between the DSL modem and the router). Then mirror the whole traffic from the router interface to another port on that switch and connect your PC to that port. See the following wiki entry.</li></ul><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code><br />
</p></blockquote><ul><li>Add a second ethernet NIC to your PC and configure a bridge. Then place your PC between the router and the DSL modem (or DSL router). Capture the traffic on your PC on any of the two bridged interfaces.</li></ul><blockquote><p><code>http://windows.microsoft.com/en-US/windows-vista/Create-a-network-bridge</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '12, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '12, 12:51</p></div></div><div id="comments-container-16277" class="comments-container"><span id="16410"></span><div id="comment-16410" class="comment"><div id="post-16410-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot! Very useful suggestions!</p></div><div id="comment-16410-info" class="comment-info"><span class="comment-age">(28 Nov '12, 22:23)</span> blue</div></div></div><div id="comment-tools-16277" class="comment-tools"></div><div class="clear"></div><div id="comment-16277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29275"></span>

<div id="answer-container-29275" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29275-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Place an old HUB between WLAN Access point and Network. Then connect temporarily your PC to the HUB. If the WLAN access point is a router and the gateway into the internet you probably need another WLAN access point and connect your Android phone to this new access point.</p><p>WLAN AP (new) -&gt; HUB -&gt; WLAN AP and Router -&gt; Internet</p><pre><code>                  |
                  +--&gt; Monitoring PC</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '14, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/7f0e89375d0e0310cf3eb43df015efe2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hardbreaker&#39;s gravatar image" /><p>hardbreaker<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hardbreaker has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '14, 09:25</p></div></div><div id="comments-container-29275" class="comments-container"></div><div id="comment-tools-29275" class="comment-tools"></div><div class="clear"></div><div id="comment-29275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

