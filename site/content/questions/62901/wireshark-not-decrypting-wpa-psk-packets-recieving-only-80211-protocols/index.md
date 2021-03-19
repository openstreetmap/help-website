+++
type = "question"
title = "Wireshark not decrypting WPA-PSK packets recieving only 802.11 protocols"
description = '''I want to monitor the traffic on my LAN. If I don&#x27;t set Monitor mode and leave only promiscous mode, I got only traffic from my machine. If I enable Monitor mode and add the 64characters long raw preshared key as described here I got traffic from other devices BUT only got 802.11 protocol (no HTTP, ...'''
date = "2017-07-19T20:38:00Z"
lastmod = "2017-07-20T03:47:00Z"
weight = 62901
keywords = [ "802.11", "monitoring", "monitor-mode" ]
aliases = [ "/questions/62901" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not decrypting WPA-PSK packets recieving only 802.11 protocols](/questions/62901/wireshark-not-decrypting-wpa-psk-packets-recieving-only-80211-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62901-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to monitor the traffic on my LAN. If I don't set Monitor mode and leave only promiscous mode, I got only traffic from my machine. If I enable Monitor mode and add the 64characters long raw preshared key as described <a href="https://wiki.wireshark.org/HowToDecrypt802.11">here</a> I got traffic from other devices BUT only got 802.11 protocol (no HTTP, TCP, etc...). I'm using wireshar 2.2.7 and Linux with kernel version 4.9.37. What am I missing?</p><p><strong>Update</strong> Following the instructions of the answer of Bob Jones, I managed to obtain the EAPOL handshake of my mobile device by just restarting its connection, however, I couldn't do the same for my laptop because when I restart its connection it seems to get only Message 1 and 3 as in the picture below:</p><p><img src="https://i.imgur.com/fRdEyIz.png" alt="eapol-capture" /></p></div><div id="question-tags" class="tags-container tags">802.11 monitoring monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '17, 20:38</strong></p><img src="https://secure.gravatar.com/avatar/6ece0ce27402bf3a1010dfed0e06438d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fabiotk&#39;s gravatar image" /><p>Fabiotk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fabiotk has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jul '17, 14:16</p></div></div><div id="comments-container-62901" class="comments-container"></div><div id="comment-tools-62901" class="comment-tools"></div><div class="clear"></div><div id="comment-62901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62919"></span>

<div id="answer-container-62919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62919-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There could be many reasons why you cannot decrypt and you don't provide enough information to really determine what the root cause is. The usual suspects:</p><ol><li>From the link you provide, it indicates that you need all four eapol handshake packets but you don't describe how you are capturing them as they usually can take some effort to collect.</li><li>You may not have any actual data in the trace to decrypt due to modulation or other differences (e.g. distance). For instance, your capture adapter is only 802.11bgn, but you are trying to capture 802.11ac traffic from your smartphone. Or you are too far away from the device and the AP so you only see low speed control frames, not high speed data frames (type Data or QoS-Data).</li><li>Passphrase or SSID could be incorrect for the network, or special characters are in use.</li><li>Other reasons...</li></ol><p>There is a sample trace on the wireshark website that can be decrypted, we assume that is decrypted properly as a test?</p><p>This issue comes up often - an example:</p><p><a href="https://ask.wireshark.org/questions/61469/unable-to-decrypt-wifi-data">https://ask.wireshark.org/questions/61469/unable-to-decrypt-wifi-data</a></p><p>Notice how we were able to determine root cause when a trace was provided along with all the relevant information (test passphrase/SSID, etc).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '17, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-62919" class="comments-container"><span id="63026"></span><div id="comment-63026" class="comment"><div id="post-63026-score" class="comment-score"></div><div class="comment-text"><p>Could you then decrypt the mobile phone data since you have all four eapol handshake frames?</p><p>Are you capturing and connecting with the laptop at the same time (HonHai MAC)? If so , you might want to move to a different device to do the capture.</p></div><div id="comment-63026-info" class="comment-info"><span class="comment-age">(23 Jul '17, 14:42)</span> Bob Jones</div></div></div><div id="comment-tools-62919" class="comment-tools"></div><div class="clear"></div><div id="comment-62919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

