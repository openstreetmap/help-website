+++
type = "question"
title = "Why can&#x27;t I see wifi traffic from my andoid phone?"
description = '''Greetings, I am quite new to Wireshark/Linux Kali. I am wondering if, according to my setup, (which I will describe shortly) I should be able to see wifi packets from my cell phone. I have 4 devices:   Macbook running Kali Linux and Wireshark with TP-LINK TL-WN722N. The interface is set to monitor m...'''
date = "2016-02-17T11:05:00Z"
lastmod = "2016-02-17T19:38:00Z"
weight = 50279
keywords = [ "wireshark" ]
aliases = [ "/questions/50279" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I see wifi traffic from my andoid phone?](/questions/50279/why-cant-i-see-wifi-traffic-from-my-andoid-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50279-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings, I am quite new to Wireshark/Linux Kali. I am wondering if, according to my setup, (which I will describe shortly) I should be able to see wifi packets from my cell phone.</p><p>I have 4 devices:</p><ol><li><p>Macbook running Kali Linux and Wireshark with TP-LINK TL-WN722N. The interface is set to monitor mode, channel 1 and is associated to my WIFI router's ESSID. I set up the decryption key for 802.11.</p></li><li><p>Sony Laptop connected to WIFI router on channel 1. In wireshark (running on macbook), once I've captured the handshake I can see everything from this laptop (http, dhcp, tcp etc...) That tells me the decryption key setup is functioning.</p></li><li><p>My Samsung android phone connected to exact same WIFI on channel 1. Once I capture the handshake, I can only see a few packets but it does not show me much of anything else. Is this normal for android devices? In my research, Ive seen where it was suggested to setup an AP(ie on my macbook) and have the android device connect to it to see the traffic.</p></li><li><p>Router is an ASUS AC68U, the 2.4 ghz Wireless Mode is set to Auto with b/g protection and 20/40 for the band.</p></li></ol><p>In Wireshark the EAPOL packet (4 of 4)802.11 radio info for my Android shows:</p><p>Phy type 802.11b (4)</p><p>Channel:1 Freq: 2412 MHZ</p><p>and for Sony laptop:</p><p>Phy type 802.11g (6)\</p><p>Channel: 1 Freq: 2412 MHZ</p><p>Why can't I see wifi traffic to/from my android phone? Do I have to set my interface to specifically capture 802.11b to see the packets from my android device? or is this just a red herring.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '16, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/fdf4d636f9ff92c00daae0ac00a658d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsixpack1&#39;s gravatar image" /><p>jsixpack1<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsixpack1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Feb '16, 16:50</p></div></div><div id="comments-container-50279" class="comments-container"></div><div id="comment-tools-50279" class="comment-tools"></div><div class="clear"></div><div id="comment-50279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50288"></span>

<div id="answer-container-50288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50288-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your first statement says: "The interface is set to monitor mode, channel 1 and is associated to my WIFI router's ESSID."</p><p>That's not how monitor mode works. Once you place your adapter in monitor mode and select a channel, you do not associate to any WLAN. The adapter will capture all the traffic on channel 1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '16, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-50288" class="comments-container"><span id="50304"></span><div id="comment-50304" class="comment"><div id="post-50304-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the info Amato_C. I appreciate that. Helps increase my knowledge.</p></div><div id="comment-50304-info" class="comment-info"><span class="comment-age">(18 Feb '16, 06:30)</span> jsixpack1</div></div><span id="50308"></span><div id="comment-50308" class="comment"><div id="post-50308-score" class="comment-score"></div><div class="comment-text"><p>If a provided answer solves your problem, please select it as accepted (little check mark). This helps others with similar problems.</p></div><div id="comment-50308-info" class="comment-info"><span class="comment-age">(18 Feb '16, 09:11)</span> Amato_C</div></div></div><div id="comment-tools-50288" class="comment-tools"></div><div class="clear"></div><div id="comment-50288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

