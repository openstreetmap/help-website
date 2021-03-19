+++
type = "question"
title = "Monitor mode capture in an encrypted network"
description = '''Hi, Here is my situation. I got a AWUS036NHE card and install it on a Ubuntu machine. I managed to put the AWUS in monitor mode , installed gpk and wireshark and right now I see the card in wireshark. I also managed to set up the card in monitor mode in wireshark and I try to listen to trafic in my ...'''
date = "2016-01-12T07:10:00Z"
lastmod = "2016-01-12T07:30:00Z"
weight = 49125
keywords = [ "decryption", "monitor", "mode" ]
aliases = [ "/questions/49125" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor mode capture in an encrypted network](/questions/49125/monitor-mode-capture-in-an-encrypted-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49125-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Here is my situation. I got a AWUS036NHE card and install it on a Ubuntu machine. I managed to put the AWUS in monitor mode , installed gpk and wireshark and right now I see the card in wireshark. I also managed to set up the card in monitor mode in wireshark and I try to listen to trafic in my wireless network which is WPA2 encrypted. I have an STB that connects to my router to access video content. Beside video content there are http requests, DNS resolutions and I can see all these if I run the STB through wired network, through my 2 network card computer set up in ICS in Windows. In this wired configuration, the capture is done in promiscuous mode and under protocol I see DNS, HTTP, RTMP....etc. When I switch to wireless and go in monitor mode I only see 802.11 frames under protocol and I wasn't able to figure yet how to extract usefull information from those frames. When I talk about useful information I am only referring strictly to communication information like DNS names that the STB is trying to access, HTTP requests, RTMP requests and their respective IP addresses. I am not interested in the payload, respectively the video content or HTTP page content. I know that the communication between STB and router is encrypted, but I do have the WPA2 key. I noticed that Wireshark can decrypt the frames, but when I wanted to add the key I only had WEP and WPA in Wireshark. Do I have to install some extra modules to get WPA2 decryption in Wireshark, or it should work by filling my wireless key under WPA password? Any idea how can I extract a useful conversation from these frames once decrypted, in order for me to make sense.... Any help is appreciated. I am very beginner with Ubuntu/Linux, so if anything needs to be added in Ubuntu/wireshark, please write me all the commands....Do not assume I know how to do this or that... It took me a whole day to install wireshark and put the AWUS adapter in monitor mode....</p><p>Thank you.</p><p>Regards,</p><p>Joe</p></div><div id="question-tags" class="tags-container tags">decryption monitor mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/cd9a402c65876beb2d331c451e17987a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joe%20Smith&#39;s gravatar image" /><p>Joe Smith<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joe Smith has no accepted answers">0%</span></p></div></div><div id="comments-container-49125" class="comments-container"></div><div id="comment-tools-49125" class="comment-tools"></div><div class="clear"></div><div id="comment-49125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49126"></span>

<div id="answer-container-49126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49126-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are some helpful resources just a Google away:</p><ol><li>The Wireshark Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">Wireless LAN Capture</a>.</li><li>The Wireshark Wiki page on <a href="https://wiki.wireshark.org/HowToDecrypt802.11">802.11 Decryption</a>.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49126" class="comments-container"></div><div id="comment-tools-49126" class="comment-tools"></div><div class="clear"></div><div id="comment-49126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

