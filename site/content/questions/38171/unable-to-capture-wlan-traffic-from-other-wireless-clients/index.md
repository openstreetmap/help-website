+++
type = "question"
title = "Unable to capture wlan traffic from other wireless clients"
description = '''Sorry, this is maybe a recurring topic but I still don&#x27;t see clearly the reason why I can&#x27;t sniff the traffic from other wireless clients connected to my access point. My host machine is running under ubuntu 14.04, with a wireshark version 1.10.6 and a wireless NIC &quot;Intel Corporation Wireless 7260 (...'''
date = "2014-11-26T06:47:00Z"
lastmod = "2014-11-26T06:47:00Z"
weight = 38171
keywords = [ "capture", "wlan" ]
aliases = [ "/questions/38171" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture wlan traffic from other wireless clients](/questions/38171/unable-to-capture-wlan-traffic-from-other-wireless-clients)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38171-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sorry, this is maybe a recurring topic but I still don't see clearly the reason why I can't sniff the traffic from other wireless clients connected to my access point. My host machine is running under ubuntu 14.04, with a wireshark version 1.10.6 and a wireless NIC "Intel Corporation Wireless 7260 (rev 83)"</p><p>I used airmon-ng to create an interface in monitor mode (mon0) in the operating channel.</p><blockquote><p>sudo airmon-ng start wlan0 6</p></blockquote><p>In practice, I stay associated to the AP but I can only sniff my own traffic. I read that this could be due to the half duplex communication which could prevent to capture all the packets. So I tried to disable the WiFi in the Network manager to put my card in a pure sniffing mode but then I don't capture anything. Note that before starting the capture while WiFi is diabled, I used the following commands to set up the wlan interface:</p><blockquote><p>sudo rfkill wlan0 unblock wifi</p><p>sudo ifconfig wlan0 up</p><p>sudo ifconfig mon0 up<br />
</p></blockquote><p>I also tried airodump-ng to remove any doubt regarding the wireshark configuration (e.g Promiscuous mode) and again no packets from other clients...</p><p>Is the monitor mode of my wireless card very specific and prevents to capture the traffic from other wireless clients? How to make sure that this is a limitation from my wireless card? Note that I gave a try with the Linux Mint 17 distribution but it didn't help.</p><p>I heard about the special USB capture adapter ("AirPCAP") but I though that it was particularly required under windows but not linux. Should I use this kind of adapter or is there something wrong or missing in my configuration setup?<br />
</p><p>Thank you for any feedback.</p></div><div id="question-tags" class="tags-container tags">capture wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/77edc37d015886d219a56c1619cedabe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnunes&#39;s gravatar image" /><p>pnunes<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnunes has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-38171" class="comments-container"></div><div id="comment-tools-38171" class="comment-tools"></div><div class="clear"></div><div id="comment-38171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

