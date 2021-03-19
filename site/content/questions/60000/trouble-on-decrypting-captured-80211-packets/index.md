+++
type = "question"
title = "Trouble on decrypting captured 802.11 packets"
description = '''Hi, I&#x27;m a noob college student studying wireless networking I&#x27;m using Atheros 93xx chipset and Netgear X6 R8000 router with WPA2-PSK. I want to show ICMP packets around network area, so I used monitor mode to capture whole 802.11 wireless packets. But I failed to decrypt the packets. I&#x27;ve seen many ...'''
date = "2017-03-10T21:01:00Z"
lastmod = "2017-03-11T07:08:00Z"
weight = 60000
keywords = [ "wireless", "decryption", "802.11" ]
aliases = [ "/questions/60000" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trouble on decrypting captured 802.11 packets](/questions/60000/trouble-on-decrypting-captured-80211-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60000-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm a noob college student studying wireless networking</p><p>I'm using Atheros 93xx chipset and Netgear X6 R8000 router with WPA2-PSK.</p><p>I want to show ICMP packets around network area, so I used monitor mode to capture whole 802.11 wireless packets. But I failed to decrypt the packets.</p><p>I've seen many pages which show how to decrypt 802.11 packets but I failed all..</p><p>I followed instruction from</p><ul><li><a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></li><li><a href="https://www.wireshark.org/tools/wpa-psk.html">https://www.wireshark.org/tools/wpa-psk.html</a></li></ul><p>to decrypt packets but I failed.</p><p>After failure, I used airdecap-ng but it doesn't decrypt the packets, too.</p><p>Is there any more tries that I can do?</p></div><div id="question-tags" class="tags-container tags">wireless decryption 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 21:01</strong></p><img src="https://secure.gravatar.com/avatar/9c79dd2f8ef7fd4dc31511b1ef505e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jayheo&#39;s gravatar image" /><p>jayheo<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jayheo has no accepted answers">0%</span></p></div></div><div id="comments-container-60000" class="comments-container"></div><div id="comment-tools-60000" class="comment-tools"></div><div class="clear"></div><div id="comment-60000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60007"></span>

<div id="answer-container-60007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60007-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like you either don't have any data packets to decrypt (common problem) or you don't have the 4-way eapol handshake for the device under review (absolutely required). However, since you do not provide a trace to review, this is just guessing.</p><p>There are many questions on here related to this topic but for the most part they distill down to these two issues. Search and you will find lots of detail related to these topics and things to do, like degrade the communication capabilities to make it easier to capture frames, how to force a device to generate the eapol handshake, etc.</p><p>If you are sure you have data frames and the four way handshake, is the passphrase correct? Watch for SSIDs that have special characters and spaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '17, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-60007" class="comments-container"><span id="60010"></span><div id="comment-60010" class="comment"><div id="post-60010-score" class="comment-score"></div><div class="comment-text"><p>I checked captured file and found 4-way handshake with EAPOL protocol. There are many data packets denoted as 802.11 protocol. I double-checked my passphrase and I copied the passphrase/SSID from my router preferences.</p></div><div id="comment-60010-info" class="comment-info"><span class="comment-age">(11 Mar '17, 22:26)</span> jayheo</div></div><span id="60014"></span><div id="comment-60014" class="comment"><div id="post-60014-score" class="comment-score"></div><div class="comment-text"><p>I solved the problem by changing preference of Ignore the Protection bit from No to Yes - With IV. Thank you for advise me!</p></div><div id="comment-60014-info" class="comment-info"><span class="comment-age">(12 Mar '17, 05:02)</span> jayheo</div></div></div><div id="comment-tools-60007" class="comment-tools"></div><div class="clear"></div><div id="comment-60007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

