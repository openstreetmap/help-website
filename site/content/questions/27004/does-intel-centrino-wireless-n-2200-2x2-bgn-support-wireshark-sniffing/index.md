+++
type = "question"
title = "Does Intel Centrino Wireless-N 2200 (2x2 BGN) support wireshark sniffing"
description = '''Hi Am using Lenovo Thinkpad T430 with Intel Centrino Wireless-N 2200 (2x2 BGN) as built in WLAN card. Ubuntu OS is running on this. Want to use WLAN card as WLAN sniffer. Does this WLAN card support monitor mode ?  sudo ifconfig wlan0 down sudo iwconfig wlan0 mode monitor sudo iwconfig wlan0 channel...'''
date = "2013-11-14T07:08:00Z"
lastmod = "2013-11-14T07:47:00Z"
weight = 27004
keywords = [ "t430", "thinkpad" ]
aliases = [ "/questions/27004" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Intel Centrino Wireless-N 2200 (2x2 BGN) support wireshark sniffing](/questions/27004/does-intel-centrino-wireless-n-2200-2x2-bgn-support-wireshark-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27004-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Am using Lenovo Thinkpad T430 with Intel Centrino Wireless-N 2200 (2x2 BGN) as built in WLAN card. Ubuntu OS is running on this.</p><p>Want to use WLAN card as WLAN sniffer. Does this WLAN card support monitor mode ?</p><ol><li>sudo ifconfig wlan0 down</li><li>sudo iwconfig wlan0 mode monitor</li><li>sudo iwconfig wlan0 channel 1</li><li>sudo ifconfig wlan0 up</li><li>sudo wireshark &amp;</li></ol><p>Unfortunately following error is coming after step 3 :: Error for wireless request “set frequency” (8B04) : Set failed on device wlan0 ; Device or resource busy</p></div><div id="question-tags" class="tags-container tags">t430 thinkpad</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/2023742ab6587c90ae933726d0edda56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vamsi&#39;s gravatar image" /><p>vamsi<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vamsi has no accepted answers">0%</span></p></div></div><div id="comments-container-27004" class="comments-container"></div><div id="comment-tools-27004" class="comment-tools"></div><div class="clear"></div><div id="comment-27004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27006"></span>

<div id="answer-container-27006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27006-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>please follow the instructions in my answer to a similar question, especially the airmon-ng part to enable <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode">monitor mode</a>:</p><blockquote><p><a href="http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version">http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version</a></p><p>Error for wireless request “set frequency” (8B04) : Set failed on device wlan0 ; <strong>Device or resource busy</strong></p></blockquote><p>The device might be in use by another tool. On Ubuntu it could be the "Network Manager". Please disable the Network Manager and then try again.</p><blockquote><p><a href="https://help.ubuntu.com/community/NetworkManager#Disabling_NetworkManager">https://help.ubuntu.com/community/NetworkManager#Disabling_NetworkManager</a><br />
<a href="http://dijks.wordpress.com/2012/07/06/how-to-disable-network-manager-in-ubuntu-12-04-precise/">http://dijks.wordpress.com/2012/07/06/how-to-disable-network-manager-in-ubuntu-12-04-precise/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-27006" class="comments-container"><span id="27032"></span><div id="comment-27032" class="comment"><div id="post-27032-score" class="comment-score"></div><div class="comment-text"><p>Hey</p><p>Thanks for quick suggestion. I stopped network manager, but even then it comes as follows ::</p><p>sudo stop network-manager sudo ifconfig wlan0 down sudo iwconfig wlan0 mode monitor sudo iwconfig wlan0 channel 6</p><p>Error for wireless request “set frequency” (8B04) : Set failed on device wlan0 ; Device or resource busy</p></div><div id="comment-27032-info" class="comment-info"><span class="comment-age">(15 Nov '13, 03:55)</span> vamsi</div></div><span id="27033"></span><div id="comment-27033" class="comment"><div id="post-27033-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Set failed on device wlan0 ; Device or resource busy</p></blockquote><p>well, Network Manager was just the most likely tool. There might be others on your system. As we don't know the configuration of your system, you are the only one that to figure out what software is accessing the card. Sorry ...</p><p>BTW: You are not connected to a wireless network via wlan0 while you try to run airmon-ng, are you?</p></div><div id="comment-27033-info" class="comment-info"><span class="comment-age">(15 Nov '13, 04:57)</span> Kurt Knochner ♦</div></div><span id="27064"></span><div id="comment-27064" class="comment"><div id="post-27064-score" class="comment-score"></div><div class="comment-text"><p>I made sure WiFi is not connected. Infact, its disabled.</p></div><div id="comment-27064-info" class="comment-info"><span class="comment-age">(17 Nov '13, 19:26)</span> vamsi</div></div><span id="27267"></span><div id="comment-27267" class="comment"><div id="post-27267-score" class="comment-score"></div><div class="comment-text"><p>You ran:</p><ol><li>sudo iwconfig wlan0 mode monitor</li><li>sudo iwconfig wlan0 channel 1</li></ol><p>Maybe you should try to run it in the opposite order</p><ol><li>sudo iwconfig wlan0 channel 1</li><li>sudo iwconfig wlan0 mode monitor</li></ol></div><div id="comment-27267-info" class="comment-info"><span class="comment-age">(22 Nov '13, 02:29)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27006" class="comment-tools"></div><div class="clear"></div><div id="comment-27006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

