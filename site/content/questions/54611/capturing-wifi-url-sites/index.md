+++
type = "question"
title = "Capturing Wifi URL sites"
description = '''Hello, I would like to monitor the URL traffic on my home wifi. I downloaded Wireshark and installed it on my Windows computer. I have successfully been able to capture all traffic from that computer to the network and can see the individual URLs visited. Now I would like to take it a step further a...'''
date = "2016-08-05T05:30:00Z"
lastmod = "2016-08-05T13:16:00Z"
weight = 54611
keywords = [ "wireshark" ]
aliases = [ "/questions/54611" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Wifi URL sites](/questions/54611/capturing-wifi-url-sites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54611-score" class="post-score" title="current number of votes">0</div><span id="post-54611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to monitor the URL traffic on my home wifi. I downloaded Wireshark and installed it on my Windows computer. I have successfully been able to capture all traffic from that computer to the network and can see the individual URLs visited. Now I would like to take it a step further and get the network traffic from 2 other Cell phones that hit the wifi network and use the internet on the phone. I have a verizon router and fios wifi. When I log into my router, I can see that it is set to something called compatibility mode which says it supports 802.11b/g/n.</p><p>It looks like I need Airpcap to capture this information. On the website, it looks like this can either be around $300 for a version of 802.11b/g or around $700 for a version of 802.11a/b/g/n. My question is which of these would I need? I assume I can get away with the $300 version since my router supports b/g, but is that actually the case?</p><p>At the end of the day, my ultimate goal is to be able to see all website visited by a cell phone internet that connects to my home wifi.<br />
</p><p>Are there other cheaper options out there than the $300 Airpcap to accomplish this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '16, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/51e5a23097a0b3079b90d07fcd4adc1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="questions123&#39;s gravatar image" /><p><span>questions123</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="questions123 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-54611" class="comments-container"></div><div id="comment-tools-54611" class="comment-tools"></div><div class="clear"></div><div id="comment-54611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54612"></span>

<div id="answer-container-54612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54612-score" class="post-score" title="current number of votes">0</div><span id="post-54612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hopefully you have looked at the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">Wireless capture</a>? That will inform you that WiFi capturing on Windows (without AirPcap) is difficult due to WinPcap limitations.</p><p>You might try the replacement for WinPcap, npcap as discussed on the page, or boot to a version of Linux that has better support for monitor mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '16, 06:06</strong> </span></p></div></div><div id="comments-container-54612" class="comments-container"></div><div id="comment-tools-54612" class="comment-tools"></div><div class="clear"></div><div id="comment-54612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54621"></span>

<div id="answer-container-54621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54621-score" class="post-score" title="current number of votes">0</div><span id="post-54621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Buying another wireless access point and eventually a second Ethernet card to your PC (e.g. an USB one) might be cheaper than AirPcap. You would then switch off the WiFi on the Verizon router and configure the new AP with the same channel, SSID, encryption mode and passphrase, and connect it to the Verizon modem using your PC as an intermediate switch or router. This way, all traffic from the AP to the modem (and internet) would run through your PC, so you could capture it on the wire rather than in the air. To date, npcap cannot capture packets bridged between two Ethernet ports, so you either have to use WinPcap or a routing mode (called "internet connection sharing" on Windows).</p><p>You may also use your PC as an access point directly if its wireless card can support an AP mode and if you find a software capable of making use of that mode. I haven't done that practically since Windows XP, though.</p><p>The AirPcap has to support all modes supported by the AP to be able to capture everything. So for a b/g only AirPcap, you would have to permit only b/g mode on your AP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54621" class="comments-container"></div><div id="comment-tools-54621" class="comment-tools"></div><div class="clear"></div><div id="comment-54621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

