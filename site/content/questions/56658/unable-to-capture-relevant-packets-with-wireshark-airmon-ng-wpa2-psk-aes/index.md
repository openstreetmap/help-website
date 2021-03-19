+++
type = "question"
title = "Unable to capture relevant packets with Wireshark / Airmon-ng WPA2-PSK (AES)"
description = '''Objective: Capture packets with info containing sites visited, usernames &amp;amp; passwords if any on WPA2-PSK (AES)wifi network. Monitor capable Alfa card used. Steps followed: airmon-ng check kill airmon-ng start wlan1 (window 1)airodump-ng -c [number] --bssid [bssidnumber] --shockack -w [filepath] w...'''
date = "2016-10-25T13:57:00Z"
lastmod = "2016-10-25T14:50:00Z"
weight = 56658
keywords = [ "airmon-ng", "wpa2", "wireshark" ]
aliases = [ "/questions/56658" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture relevant packets with Wireshark / Airmon-ng WPA2-PSK (AES)](/questions/56658/unable-to-capture-relevant-packets-with-wireshark-airmon-ng-wpa2-psk-aes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56658-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Objective: Capture packets with info containing sites visited, usernames &amp; passwords if any on WPA2-PSK (AES)wifi network. Monitor capable Alfa card used.</p><p>Steps followed:</p><p>airmon-ng check kill</p><p>airmon-ng start wlan1</p><p>(window 1)airodump-ng -c [number] --bssid [bssidnumber] --shockack -w [filepath] wlan1(mon)</p><p>(window 2) aireplay-ng -0 5 -a [bssidnumber] -c [targetMAC] wlan1(mon)</p><p>Target device looses connection to wifi and rejoins, I can see a handshake is captured in window 1</p><p>Browse HTTP sites on the target device (tried iPhone, laptop), fill out and submit login forms</p><p>Ctrl + C to stop capture</p><p>Open .cap with Wireshark</p><p>Preferences &gt; IE802.11 &gt; enable decryption &gt; enter generated key</p><p>At this stage I have to fiddle with settings such as ignore protection bit, and then I get some decrypted (coloured) results displayed in the grid...great :)</p><p>You'd think at this stage I'd be home and dry....only problem is I have no HTTP, HTTPS, DNS requests nor do I get any results when I search for the password I entered in the login form as a string.</p><p>Any ideas what I'm doing wrong?</p></div><div id="question-tags" class="tags-container tags">airmon-ng wpa2 wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '16, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/b46d7d743d7d4ef148c4a32f2be36f9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rootb33r&#39;s gravatar image" /><p>rootb33r<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rootb33r has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Oct '16, 13:58</p></div></div><div id="comments-container-56658" class="comments-container"></div><div id="comment-tools-56658" class="comment-tools"></div><div class="clear"></div><div id="comment-56658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56660"></span>

<div id="answer-container-56660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56660-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With no other detail, such as a trace, we can't be sure. However, this might give you some ideas to try:</p><p><a href="https://ask.wireshark.org/questions/54433/why-cant-i-capture-data-packets-in-monitor-mode?page=1&amp;focusedAnswerId=54437#54437">https://ask.wireshark.org/questions/54433/why-cant-i-capture-data-packets-in-monitor-mode?page=1&amp;focusedAnswerId=54437#54437</a></p><p><a href="https://ask.wireshark.org/questions/55637/wireshark-with-atheros-wireless-in-monitor-mode?page=1&amp;focusedAnswerId=55643#55643">https://ask.wireshark.org/questions/55637/wireshark-with-atheros-wireless-in-monitor-mode?page=1&amp;focusedAnswerId=55643#55643</a></p><p><a href="https://ask.wireshark.org/questions/14684/no-data-packets-when-turning-on-monitor-mode">https://ask.wireshark.org/questions/14684/no-data-packets-when-turning-on-monitor-mode</a></p><p><a href="https://ask.wireshark.org/questions/54835/having-issues-capturing-http-traffic-on-my-network">https://ask.wireshark.org/questions/54835/having-issues-capturing-http-traffic-on-my-network</a></p><p>I'd guess if you see some frames decrypted it is a likely a modulation issue and you can't decode regular data frames that are at high data rates. You might see multicast/broadcast as they are sent at lower rates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '16, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Oct '16, 14:55</p></div></div><div id="comments-container-56660" class="comments-container"><span id="56664"></span><div id="comment-56664" class="comment"><div id="post-56664-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. I'll go through the links tomorrow. It does sound like what you said about the data rates may be right as I definitely am seeing some information....just not what I really want to see.</p><p>The capture card specifically is the awus036h. 'Promiscuous' mode has never been explicitly turned on, but I understand that is a Wireshark setting(?) and I'm simply viewing the .cap with Wireshark rather than capturing with it.</p></div><div id="comment-56664-info" class="comment-info"><span class="comment-age">(25 Oct '16, 16:15)</span> rootb33r</div></div></div><div id="comment-tools-56660" class="comment-tools"></div><div class="clear"></div><div id="comment-56660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

